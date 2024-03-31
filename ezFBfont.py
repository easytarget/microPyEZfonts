# ezFBfont.py() : a simple string writer for small mono displays and user selected fonts.

# Extensively re-worked from the 'writer' class by
# Peter Hinch:
#  https://github.com/peterhinch/micropython-font-to-py
# - Released under the MIT License (MIT). See LICENSE.
# - Copyright (c) 2019-2021 Peter Hinch

import framebuf
from uctypes import bytearray_at, addressof
from sys import implementation

# a table to find color space from the framebuffer format
colorspaces = {
                framebuf.MONO_VLSB : 2,
                framebuf.MONO_HLSB : 2,
                framebuf.MONO_HMSB : 2,
                framebuf.RGB565 : 65536,
                framebuf.GS2_HMSB: 4,
                framebuf.GS4_HMSB: 16,
                framebuf.GS8 : 256,
                }

# Basic string printing class
class ezFBfont():

    def __init__(self, device,
                 font,
                 fg = None,
                 bg = None,
                 tkey = None,
                 halign = None,
                 valign = None,
                 colors = None,
                 verbose = False):

        self._device = device
        self._font = font
        self._verbose = verbose
        self.name = self._font.__name__

        # allow to work with reverse or normal font mapping
        if font.hmap():
            self._map = framebuf.MONO_HMSB if font.reverse() else framebuf.MONO_HLSB
        else:
            raise ValueError('Font must be horizontally mapped.')

        # currently only support monochrome fonts
        self._font_colors = 2
        self._palette_format = framebuf.RGB565

        # number of colors
        if colors is None:
            errtxt = 'Cannot determine number of colors from driver, supply with colors=N at init.'
            try:
                format = device.format  # framebuffer format
            except Exception as e:
                if self._verbose:
                    print(errtxt, '\nassuming a 2 color (mono) display')
                format = framebuf.MONO_VLSB
            try:
                self.colors = colorspaces[format]
            except KeyError:
                raise ValueError(errtxt + 'Unknown format: ' + str(format))
        else:
            self.colors = colors
        # default color scheme
        self.fg = self.colors - 1
        self.bg = 0
        self.tkey = -1
        # default alignment
        self.halign = 'left'
        self.valign = 'top'
        # apply user color and alignment overrides
        self.set_default(fg, bg, tkey, halign, valign)

    def _color_range(self, color):
        # forces colors into correct range (0...max)
        if color < 0:
            color = 0
        if color >= self.colors:
            color = self.colors -1
        return color

    def _tkey_range(self, tkey):
        # forces tkey into correct range (0...max)
        if tkey < -1:
            tkey = 0
        if tkey >= self._font_colors:
            tkey = self._font_colors -1
        return tkey

    def _check_halign(self, halign):
        if halign not in ('left','center','right'):
            raise ValueError('Unknown horizontal alignment: ' + halign)
        return halign

    def _check_valign(self, valign):
        if valign not in ('top','center','baseline','bottom'):
            raise ValueError('Unknown vertical alignment: ' + valign)
        return valign

    def _line_size(self, string):
        # Todo: replace/integrate into main char class.
        # Needs mods for rotated strings, padding
        if not len(string):
            return 0,0
        x = 0
        for char in string:
            _, _, char_width = self._font.get_ch(char)
            x += char_width
        return x, self._font.height()

    def _put_char(self, char, x, y, fg, bg, tkey):
        # fetch the glyph
        glyph, char_height, char_width = self._font.get_ch(char)
        if glyph is None:
            return 0, 0  # Nothing to print. skip.
        # buffers
        palette_buf = bytearray(self._font_colors * 2)
        buf = bytearray(glyph)
        # Mirror, flip and turn here, adjusting char-width and height
        # assemble color map
        palette = framebuf.FrameBuffer(palette_buf, self._font_colors, 1, self._palette_format)
        palette.pixel(0, 0, bg)
        palette.pixel(self.colors -1, 0, fg)
        # fetch and blit the glyph
        charbuf = framebuf.FrameBuffer(buf, char_width, char_height, self._map)
        self._device.blit(charbuf, x, y, tkey, palette)
        return char_width, char_height

    def set_default(self, fg=None, bg=None, tkey=None, halign=None, valign=None):
        if fg is not None:
            self.fg = self._color_range(fg)
        if bg is not None:
            self.bg = self._color_range(bg)
        if tkey is not None:
            self.tkey = self._tkey_range(tkey)
        if halign is not None:
            self.halign = self._check_halign(halign)
        if valign is not None:
            self.valign = self._check_valign(valign)
        if self._verbose:
            fstr = '{} = colors: {}, fg: {}, bg: {}, tr: {}, halign: {}, valign: {}'
            print(fstr.format(self.name, self.colors, self.fg, self.bg, self.tkey,
                              self.halign, self.valign))

    def size(self, string):
        lines = string.split('\n')
        w = h = 0
        # todo: orientation
        for line in lines:
            x, y = self._line_size(line)
            if x > w:  # record the widest line
                w = x
            h = h + y  # total the height
        return w, h

    def rect(self, string, x, y, halign=None, valign=None):
        if halign is None:
            halign = self.halign
        else:
            halign = self._check_halign(halign)
        if valign is None:
            valign = self.valign
        else:
            valign = self._check_valign(valign)
        wide, high = self.size(string)
        # todo: position offset
        xmin = x
        if halign is 'center':
            xmin = int(x - (wide / 2))
        elif halign is 'right':
            xmin = x - wide
        ymin = y
        if valign is 'baseline':
            ymin = y - self._font.baseline()
        elif valign is 'center':
            ymin = int(y - (high / 2))
        elif valign is 'bottom':
            ymin = y - high
        return xmin,ymin,wide,high

    def write(self, string, x, y, fg=None, bg=None, tkey=None, halign=None, valign=None):
        if len(string) == 0:
            return
        # Argument overrides
        if fg is None:
            fg = self.fg
        else:
            fg = self._color_range(fg)
        if bg is None:
            bg = self.bg
        else:
            bg = self._color_range(bg)
        if tkey is None:
            tkey = self.tkey
        else:
            tkey = self._tkey_range(tkey)
        if halign is None:
            halign = self.halign
        else:
            halign = self._check_halign(halign)
        if valign is None:
            valign = self.valign
        else:
            valign = self._check_valign(valign)
        # todo: orient
        lines = string.split('\n')
        # vertical alignment
        high = len(lines) * self._font.height()
        ypos = y
        if valign is 'baseline':
            ypos = y - self._font.baseline()
        elif valign is 'center':
            ypos = int(y - (high / 2))
        elif valign is 'bottom':
            ypos = y - high
        for line in lines:
            # horizontal alignment
            wide = self._line_size(line)[0]
            xpos = x
            if halign is 'center':
                xpos = int(x - (wide / 2))
            elif halign is 'right':
                xpos = x - wide
            # write the line
            for char in line:
                if ord(char) in range(self._font.min_ch(), self._font.max_ch() + 1):
                    cx, _ = self._put_char(char, xpos, ypos, fg, bg, tkey)
                    # needs mods for orientation
                    xpos = xpos + cx
                else:
                    print('unprintable char: "' + char + '" (' + str(ord(char)) + ')')
            # needs mods for alignment and orientation
            ypos = ypos + self._font.height()
        return
