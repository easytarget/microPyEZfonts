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

    def __init__(self, device,
                 font,
                 size = None,
                 fmt = None,
                 color = None,
                 halign = 'left',
                 valign = 'top',
                 rot = 0,
                 verbose=True):
        self._device = device
        self._font = font
        self._fmt = fmt
        self._verbose = verbose

        if font.height() >= device.height or font.max_width() >= device.width:
            raise ValueError('Font too large for screen')

        # Allow to work with reverse or normal font mapping
        if font.hmap():
            self.map = framebuf.MONO_HMSB if font.reverse() else framebuf.MONO_HLSB
        else:
            raise ValueError('Font must be horizontally mapped.')

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

        if fmt is None:
            try:
                self._format = device.format  # pixel format
            except Exception as e:
                errtxt = 'Cannot determine screen format from driver, supply with fmt=XXX at init.'
                raise ValueError(errtxt + repr(e))
        else:
                self._format = fmt

        self._colormax = colorspaces[self._format] -1
        self._fg, self._bg, self._tkey = self._check_color(color)
        self._halign = self._check_halign(halign)
        self._valign = self._check_valign(valign)
        self._dir = self._check_rot(rot)

        if self._verbose:
            fstr = 'width: {}, height: {}\nfg: {}, bg: {}, tr: {}'
            print(fstr.format(device.width, device.height,
                              self._fg, self._bg, self._tkey))

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
        print(color)
        return color

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

    def _check_rot(self, rot):
        # returns a 'direction' tuple, (X,Y) giving direction in each axis (-1|0|1)
        #if rot not in (0,90,120,270): <- when rotated text is implemented!
        if rot not in (0,):
            raise ValueError('Unsupported rotation angle: ' + rot)
        if self._verbose:
            print('rotation angle: ' + str(rot))
        if rot == 0:
            return(1,0)
        elif rot == 90:
            return(0,1)
        elif rot == 180:
            return(-1,0)
        elif rot == 270:
            return(0,-1)

    def size(self, string):
        if not len(string):
            return (0,0)
        x = 0
        for char in string[:-1]:
            _, _, char_width = self.font.get_ch(char)
            x += char_width
        return (x,self._font.height())

    def area(self, string, pos, halign=None, valign=None):
        # tbd
	# ignore clipping!
        xmin = xmax = ymin = ymax = 0
        return (xmin,xmax,ymin,ymax)

     def write(self, string, pos, color=None, halign=None, valign=None):
        # todo
	# return clipping status
        return False

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
