# ezFBfont.py() : a simple string writer for small mono displays and user selected fonts.

# Extensively re-worked from the 'writer' class by
# Peter Hinch:
#  https://github.com/peterhinch/micropython-font-to-py
# - Released under the MIT License (MIT). See LICENSE.
# - Copyright (c) 2019-2021 Peter Hinch

import framebuf
from uctypes import bytearray_at, addressof
from sys import implementation

# a table to find max color and data width
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
                 halign = 'left',
                 valign = 'baseline',
                 size = None,
                 colors = None,
                 verbose=False):

        self._device = device
        self._font = font
        self._verbose = verbose
        self._dir = (1,0)   # will change for oriented text etc.

        # Sanity check
        if font.height() >= device.height or font.max_width() >= device.width:
            raise ValueError('Font too large for screen')
        # Allow to work with reverse or normal font mapping
        if font.hmap():
            self.map = framebuf.MONO_HMSB if font.reverse() else framebuf.MONO_HLSB
        else:
            raise ValueError('Font must be horizontally mapped.')
        # Screen size
        if size is None:
            try:
                self._screenwidth = device.width  # In pixels
                self._screenheight = device.height
            except Exception as e:
                errtxt = 'Cannot determine screen size from driver, supply with size=(x,y) at init.'
                raise ValueError(errtxt + repr(e))
        else:
            self._screenwidth = size[0]  # In pixels
            self._screenheight = size[1]
        # Number of colors
        if colors is None:
            errtxt = 'Cannot determine number of colors from driver, supply with colors=N at init.'
            try:
                format = device.format  # framebuffer format
            except Exception as e:
                raise ValueError(errtxt + repr(e))
            try:
                self._colors = colorspaces[format]
            except KeyError:
                raise ValueError('Unknown format. ' + errtxt)
        else:
            self._colors = colors
        # default color scheme
        self.fg = self._colors - 1
        self.bg = 0
        self.tkey = -1
        # Set user color and alignment overrides
        self.set_default(fg, bg, tkey, halign, valign)
        # Fluff
        if self._verbose:
            fstr = 'width: {}, height: {}\nfg: {}, bg: {}, tr: {}'
            print(fstr.format(device.width, device.height,
                              self._fg, self._bg, self._tkey))

    def _color_range(self, color):
        # forces colors into correct range (0...max)
        if color < 0:
            color = 0
        if color >= self._colors:
            color = self._colors -1
        return color

    def _tkey_range(self, tkey):
        # forces colors into correct range (0...max)
        if tkey < -1:
            tkey = 0
        if tkey >= self._colors:
            tkey = self._colors -1
        return tkey

    def _check_halign(self, halign):
        if halign not in ('left','center','right'):
            raise ValueError('Unknown horizontal alignment: ' + halign)
        if self._verbose:
            print('horizontal alignment: ' + halign)
        return halign

    def _check_valign(self, valign):
        if valign not in ('top','center','baseline','bottom'):
            raise ValueError('Unknown vertical alignment: ' + valign)
        if self._verbose:
            print('vertical alignment: ' + valign)
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
        pal = bytearray((self._colors // 8) + 1)
        buf = bytearray(glyph)
        # Mirror, flip and turn here, adjusting char-width and height
        # assemble color map
        palette = framebuf.FrameBuffer(pal, self._colors, 1, self.map)
        palette.pixel(0, 0, bg)
        palette.pixel(self._colors -1, 0, fg)
        # fetch and blit the glyph
        charbuf = framebuf.FrameBuffer(buf, char_width, char_height, self.map)
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
            self._halign = self._check_halign(halign)
        if valign is not None:
            self._valign = self._check_valign(valign)

    def size(self, string):
        lines = string.split('\n')
        w = h = 0
        # todo. padding affects this
        for line in lines:
            x, y = self._line_size(line)
            if x > w:  # record the widest line
                w = x
            h = h + y  # total the height
        return w, h

    def rect(self, string, x, y, halign=None, valign=None):
        wide, high = self.size(string)
        # todo: position offset
        xmin = x
        ymin = y
        return xmin,ymin,wide,high

    def write(self, string, x, y, fg=None, bg=None, tkey=None, halign=None, valign=None):
        # todo: alignment, return clipping status
        xpos = x
        ypos = y
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
        xmax = ymax = xmin = ymin = 0
        # align! orient.
        for char in string:
            if char is '\n':
                # needs mods for alignment
                xpos = x
                ypos = ypos + self._font.height()
            elif ord(char) in range(self._font.min_ch(), self._font.max_ch() + 1):
                cx, cy = self._put_char(char, xpos, ypos, fg, bg, tkey)
                xpos = xpos + (cx * self._dir[0])
                ypos = ypos + (cy * self._dir[1])
            else:
                print('unprintable char: "' + char + '" (' + str(ord(char)) + ')')
        return  # (add cliping status check)
