# ezFBstr.py() : a simple string writer for small mono displays and user selected fonts.

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
class ezFBstr():

    def __init__(self, device, font, fmt=framebuf.MONO_VLSB, color=None, halign='left', valign='top', rot=0, verbose=True):
        self._device = device
        self._font = font
        self._fmt = fmt

        if font.height() >= device.height or font.max_width() >= device.width:
            raise ValueError('Font too large for screen')

        # Allow to work with reverse or normal font mapping
        if font.hmap():
            self.map = framebuf.MONO_HMSB if font.reverse() else framebuf.MONO_HLSB
        else:
            raise ValueError('Font must be horizontally mapped.')
        if verbose:
            fstr = 'Orientation: Horizontal. Reversal: {}. Width: {}. Height: {}.'
            print(fstr.format(font.reverse(), device.width, device.height))

        self._screenwidth = device.width  # In pixels
        self._screenheight = device.height

        self._colormax = colorspaces[fmt] -1

        # Need to test color range and transparency key
        # put in a local func()
        self._fg = color[0]
        self._bg = color[1]
        self._tkey = color[2]

        # Alignment also needs testing
        # put in a local func()
        self._halign = _check_halign(halign)
        self._valign = _check_valign(valign)
        self._rot = rot

    def _check_color(self, color):
        ret = (self._colormax, 0, -1)
        if color is None:
            return ret
        if len(color) not in (1,2,3):
            raise ValueError('Unknown color tuple: ' + str(color))
        ret[0] = self._color_range(color[0])
        if len(color) > 1:
            ret[1] = self._color_range(color[1])
        else:
            ret[1] = 0
        if len(color) > 2:
            if color[2] != -1:
                ret[2] = self._color_range(color[2])
            else:
                ret[2] = -1
        return ret

    def _color_range(self, color):
        if color < 0:
            color = 0
        if color > self._colormax:
            color = self._colormax
        return color

    def _check_halign(self, halign):
        if halign not in ('left','center','right'):
            raise ValueError('Unknown horizontal alignment: ' + halign)
        if verbose:
            print('horizontal alignment: ' + halign)
        return halign

    def _check_valign(self, valign):
        if valign not in ('top','center','baseline','bottom'):
            raise ValueError('Unknown vertical alignment: ' + valign)
        if verbose:
            print('vertical alignment: ' + valign)
        return valign

    def size(self, string):
        if not len(string):
            return (0,0)
        x = 0
        for char in string[:-1]:
            _, _, char_width = self.font.get_ch(char)
            x += char_width
        return (x,self._font.height())

    def area(self, string, (x,y), halign='left', valign='top'):
        # tbd
        xmin = xmax = ymin = ymax = 0
        return (xmin,xmax,ymin,ymax)

    def _put_char(self, char, recurse):
        glyph, char_height, char_width = self.font.get_ch(char)

    # Method using blitting. Efficient rendering for monochrome displays.
    # Tested on SSD1306. Invert is for black-on-white rendering.
    def _printchar(self, char, invert=False, recurse=False):
        s = self._getstate()
        self._get_char(char, recurse)
        if self.glyph is None:
            return  # All done
        buf = bytearray(self.glyph)
        if invert:
            for i, v in enumerate(buf):
                buf[i] = 0xFF & ~ v
        fbc = framebuf.FrameBuffer(buf, self.clip_width, self.char_height, self.map)
        self.device.blit(fbc, s.text_col, s.text_row)
        s.text_col += self.char_width
        self.cpos += 1

    @property
    def color(self):
        return(self._fg, self._bg, self._tkey)

    @color.setter
    def color(self, fg=self._fg, bg=self._bg, tkey=-1):
        # check in range
        self._fg = fg
        self._bg = bg
        self._tkey = tkey
