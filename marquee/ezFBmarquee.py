# ezFBmarquee.py() : a simple marquee for the micropython framebuffer.

# - Copyright (c) Owen Carter

import framebuf
# Use repl_1306 instead of framebuffer for dev.
from repl_1306 import REPL_1306

# Basic marquee class
class ezFBmarquee():

    def __init__(self, display, font,
                 string,
                 x = 0,
                 y = 0,
                 width = None,
                 seperation = 0.33,
                 pause = 500,
                 hgap = 0,
                 verbose = False):

        self._display = display
        self._font = font
        self._string = string.split('\n')[0]
        self._x = x
        self._y = y
        self._seperation = max(seperation,0)
        self._pause = max(pause,0)
        self._hgap = hgap
        self._verbose = verbose
        self.name = 'marquee_' + self._font.__name__
        self.animated = True

        # font details; only monochrome HLSB fonts are supported
        self._font_format = framebuf.MONO_HLSB
        self._font_colors = 2
        self._palette_format = framebuf.RGB565  # support up to 65536 colors when blitting
        if verbose:
            print('{}: string: {}, x: {}, y: {}, width: {}'.format(self.name, self._string, x, y, width))

        stringwidth, self._height = self._line_size(self._string)
        print('string width', stringwidth)

        try:
            displaywide = self._display.width
        except:
            raise ValueError('cannot determine target framebuffer width')

        print('displaywide: ', displaywide)

        available = displaywide - self._x
        print('available:', available)

        if width is None:
            self._width = available
        else:
            self._width = min(width, available)

        print('marquee width:', self._width)

        if stringwidth <= self._width:
            if verbose:
                print('{}: string width ({}) is smaller than marquee box width ({}), not animating'.format(self.name, stringwidth, self._width))
            self.animated = False

        # Make the scroll framebuffer
        sbwide = stringwidth + int(self._width * self._seperation) + self._width
        sbbytes = ((sbwide - 1) // 8 ) + 1
        print(sbwide, self._height, sbbytes)
        #self._scrollbuf =  bytearray(sbbytes * self._height, framebuf.MONO_HLSB)
        #self._scrollframe =  framebuffer(self._scrollbuf, sbwide, self._height, framebuf.MONO_HLSB)
        self._scrollframe = REPL_1306(sbwide, self._height)
        self._scrollframe.rect(0,0,sbwide, self._height, 1)
        #self._scrollframe.line(0,0,sbwide - 1, self._height - 1, 1)
        #self._scrollframe.line(0,self._height - 1, sbwide - 1, 0, 1)
        # show the initial output
        self.step(0) 
 
    # Functions

    def _line_size(self, string):
        x = 0
        for char in string:
            _, _, char_width = self._font.get_ch(char)
            x += char_width + self._hgap if char_width > 0 else 0
        x = x - self._hgap if x != 0 else x   # remove any trailing hgap
        return x, self._font.height()

    def step(self, step=1):
        #if not self.animated:
        #    return
        # do animation step
        if step > 0:
            self._scrollframe.scroll(-step, 0)
        self._scrollframe.show()
        return

    def stop(self):
        # cleanup and de buffer etc
        return
