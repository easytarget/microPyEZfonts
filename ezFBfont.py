# ezFBfont.py() : a simple string writer for small mono displays and user selected fonts.
# See MARQUEE.md for documentation

# Extensively re-worked from the 'writer' class by
# Peter Hinch:
#  https://github.com/peterhinch/micropython-font-to-py
# - Released under the MIT License (MIT). See LICENSE.
# - Copyright (c) 2019-2021 Peter Hinch

import framebuf

# Basic string writing class
class ezFBfont():

    def __init__(self, device,
                 font,
                 fg = 1,
                 bg = 0,
                 tkey = -1,
                 halign = 'left',
                 valign = 'top',
                 vgap = 0,
                 hgap = 0,
                 split = '\n',
                 cswap = False,
                 verbose = False):

        self._device = device
        self._font = font
        self.name = self._font.__name__

        # font and color; only monochrome HLSB fonts are supported
        self._font_format = framebuf.MONO_HLSB
        self._font_colors = 2
        self._palette_format = framebuf.RGB565  # support up to 65536 colors when blitting
        # byte order for 16bit colors
        self._cswap = cswap
        # inform
        if verbose:
            fstr = '{} : initialised: height: {}, {} width: {}, baseline: {}'
            print(fstr.format(self.name, self._font.height(),
                              'fixed' if self._font.monospaced() else 'max',
                              self._font.max_width(), self._font.baseline()))
        # apply init color and alignment as default
        self.set_default(fg, bg, tkey, halign, valign, hgap, vgap, split, verbose)

    def _check_halign(self, h):
        if h not in ('left','center','right'):
            raise ValueError('Unknown horizontal alignment: ' + h)
        return h

    def _check_valign(self, v):
        if v not in ('top','center','baseline','bottom'):
            raise ValueError('Unknown vertical alignment: ' + v)
        return v

    def _line_size(self, string):
        x = 0
        for char in string:
            _, _, char_width = self._font.get_ch(char)
            x += char_width + self.hgap if char_width > 0 else 0
        x = x - self.hgap if x != 0 else x   # remove any trailing hgap
        return x, self._font.height()

    def _swap_bytes(self, color):
        # flip the left and right bytes in a 16 bit color word if required
        return ((color & 255) << 8) + (color >> 8) if self._cswap else color

    def _put_char(self, char, x, y, fg, bg, tkey):
        # fetch the glyph
        glyph, char_height, char_width = self._font.get_ch(char)
        if glyph is None:
            return None, None  # Nothing to write
        # buffers
        palette_buf = bytearray(self._font_colors * 2)
        buf = bytearray(glyph)
        # assemble color map
        palette = framebuf.FrameBuffer(palette_buf, self._font_colors, 1, self._palette_format)
        palette.pixel(0, 0, self._swap_bytes(bg))
        palette.pixel(self._font_colors -1, 0, self._swap_bytes(fg))
        # fetch and blit the glyph
        charbuf = framebuf.FrameBuffer(buf, char_width, char_height, self._font_format)
        self._device.blit(charbuf, x, y, tkey, palette)
        return char_width, char_height

    def set_default(self, fg=None, bg=None, tkey=None,
                    halign=None, valign=None, hgap=None, vgap=None, split=None, verbose=None):
        # Sets the default value for all supplied arguments
        self.fg = self.fg if fg is None else fg
        self.bg = self.bg if bg is None else bg
        self.tkey = self.tkey if tkey is None else tkey
        self.halign = self.halign if halign is None else self._check_halign(halign)
        self.valign = self.valign if valign is None else self._check_valign(valign)
        self.hgap = self.hgap if hgap is None else hgap
        self.vgap = self.vgap if vgap is None else vgap
        self.split = self.split if split is None else split
        self._verbose = self._verbose if verbose is None else verbose
        if self._verbose:
            fstr = '{} = fg: {}, bg: {}, tkey: {}, halign: {}, valign: {}, hgap: {}, vgap: {}, split: {}'
            print(fstr.format(self.name, self.fg, self.bg, self.tkey,
                              self.halign, self.valign, self.hgap, self.vgap, repr(split)))

    def size(self, string):
        if len(string) == 0:
            return 0, 0
        lines = string.split(self.split)
        w = 0
        for line in lines:
            x, _ = self._line_size(line)
            w = max(w, x)  # record the widest line
        h = (len(lines) * (self._font.height() + self.vgap)) - self.vgap
        return w, h

    def rect(self, string, x, y, halign=None, valign=None):
        if len(string) == 0:
            return x, y, 0, 0
        # apply alignment overrides
        halign = self.halign if halign is None else self._check_halign(halign)
        valign = self.valign if valign is None else self._check_valign(valign)
        # get the x,y size of the rendered string
        wide, high = self.size(string)
        # apply alignment
        xmin = x
        if halign == 'center':
            xmin = int(x - (wide / 2))
        elif halign == 'right':
            xmin = x - wide
        ymin = y
        if valign == 'baseline':
            ymin = y - self._font.baseline()
        elif valign == 'center':
            ymin = int(y - (high / 2))
        elif valign == 'bottom':
            ymin = y - high
        # return the result
        return xmin,ymin,wide,high

    def write(self, string, x, y, fg=None, bg=None, tkey=None,
              halign=None, valign=None):
        if len(string) == 0:
            return True
        all_chars = True
        # Argument overrides
        fg = self.fg if fg is None else fg
        bg = self.bg if bg is None else bg
        tkey = self.tkey if tkey is None else tkey
        halign = self.halign if halign is None else self._check_halign(halign)
        valign = self.valign if valign is None else self._check_valign(valign)
        # Break the string into lines
        lines = string.split(self.split)
        # vertical alignment
        high = (len(lines) * (self._font.height() + self.vgap)) - self.vgap
        ypos = y
        if valign == 'baseline':
            ypos = y - self._font.baseline() + 1
        elif valign == 'center':
            ypos = int(y - (high / 2))
        elif valign == 'bottom':
            ypos = y - high
        for line in lines:
            wide, high = self._line_size(line)
            # horizontal alignment
            if halign == 'left':
                xpos = x
            elif halign == 'right':
                xpos = x - wide
            else:
                xpos = int(x - (wide / 2))
            # write the line
            for char in line:
                cx, _ = self._put_char(char, xpos, ypos, fg, bg, tkey)
                if cx is None:
                    if self._verbose:
                        print('{}: missing char: {} (0x{:02X})'.format(self.name, repr(char), ord(char)))
                    all_chars = False
                else:
                    xpos += cx + self.hgap
            ypos += high + self.vgap
        return all_chars
