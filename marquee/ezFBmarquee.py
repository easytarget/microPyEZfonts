# ezFBmarquee.py() : a simple marquee for the micropython framebuffer.

# - Copyright (c) Owen Carter

import framebuf

# Basic marquee class
class ezFBmarquee():

    def __init__(self, display, font, y=0, hgap=0, fg=1, bg=0, width=None, verbose=False):

        self._device = display
        self._font = font
        self._y = y
        self._hgap = hgap
        self._fg = fg
        self._bg = bg
        self._verbose = verbose

        self.name = 'marquee_' + self._font.__name__
        self._string = None

        # font details; only monochrome HLSB fonts are supported
        self._font_format = framebuf.MONO_HLSB
        self._font_colors = 2
        self._palette_format = framebuf.RGB565  # support up to 65536 colors when blitting
        # color map
        self._palette_buf = bytearray(self._font_colors * 2)
        self._palette = framebuf.FrameBuffer(self._palette_buf, self._font_colors, 1, self._palette_format)
        # Get height of marquee
        self._height = self._font.height()
        # Get width of marquee (full device width)
        try:
            self._width = self._device.width
        except: 
            if width is None:
                r = "{}: Cannot determine display width; use 'width=<n>' in init()"
                raise ValueError(r.format(self.name))
            else:
                self._width = width
        # Give info as needed
        if self._verbose:
            print('{}:'.format(self.name))
            print('  y: {}, height: {}, width: {}'.format(self._y, self._height, self._width))
            print('  fg: {}, bg: {}, hgap: {}'.format(self._fg, self._bg, self._hgap))
 
    def _line_size(self, string):
        x = 0
        for char in string:
            _, _, char_width = self._font.get_ch(char)
            x += char_width + self._hgap if char_width > 0 else 0
        x = x - self._hgap if x != 0 else x   # remove any trailing hgap
        return x, self._font.height()

    def _makescroll(self):
        self._stepping = True
        # Work out how long our string will be once rendered
        self._stringwidth, _ = self._line_size(self._string)
        # padding size between repeats, in px
        self._padding = int(self._width * self._seperation)
        # Give info as needed
        if self._verbose:
            print('{}:\n  string: {}\n  string width: {}'.format(self.name, self._string, self._stringwidth))
            print('  seperation: {}\n  pause: {}'.format(self._padding, self._pause))
            print('  fg: {}, bg: {}, hgap: {}'.format(self._fg, self._bg, self._hgap))
        # determine if we need to animate at all (static marquee always re-drawn on step())
        if self._stringwidth <= self._width:
            self._stepping = False
            if self._verbose:
                p = '{}: string width ({}) is smaller than screen width ({}), not animating'
                print(p.format(self.name, self._stringwidth, self._width))
        # Make the framebuffer that we scroll
        self._sbwide = self._stringwidth + self._padding + self._width
        sbbytes = ((self._sbwide - 1) // 8 ) + 1
        self._scrollbuf =  bytearray(sbbytes * self._height)
        self._scrollframe = framebuf.FrameBuffer(self._scrollbuf, self._sbwide, self._height, self._font_format)

    def _fillscroll(self):
        # clean the scrollbuffer
        self._stepcount = 0
        self._scrollframe.fill(0)
        # write our string, add the seperator, then start the string again
        xpos = 0
        for c in self._string:
            xpos += self._put_char(c, xpos) + self._hgap
        xpos = xpos - self._hgap if xpos != 0 else xpos   # remove any trailing hgap
        if not self._stepping:
            return  # skip rollover space and chars
        xpos += self._padding
        for c in self._string:
            if xpos >= self._sbwide:
                break
            xpos += self._put_char(c,xpos) + self._hgap

    def _put_char(self, char, x):
        # fetch the glyph
        glyph, char_height, char_width = self._font.get_ch(char)
        if glyph is None:
            return 0  # Nothing to write
        # blit the glyph, make the background transparent..
        buf = bytearray(glyph)
        charbuf = framebuf.FrameBuffer(buf, char_width, char_height, self._font_format)
        self._scrollframe.blit(charbuf, x, 0, 0)
        return char_width

    def _stop(self, clean=True):
        self._string = None
        self._stepcount = 0
        self._stepping = False
        self._stringwidth = 0
        self._padding = 0
        self._sbwide = 0
        del self._scrollframe, self._scrollbuf
        if clean:
            self._device.rect(0, self._y, self._width, self._height, self._bg, True)

    def show(self, string, seperation=0.5, pause=0, hgap=None, fg=None, bg=None):
        # start marquee with string, returns false if not animated
        self._fg = self._fg if fg is None else fg
        self._bg = self._bg if bg is None else bg
        # stop when string is None (but still set fg/bg)
        if string is None:
            self._stop()
            return False
        # only take the first line of the string
        self._string = string.split('\n')[0]
        self._seperation = max(seperation,0)
        self._hgap = self._hgap if hgap is None else hgap
        # Initial pause
        self.pause(pause)
        # set color map
        self._palette.pixel(0, 0, self._bg)
        self._palette.pixel(self._font_colors -1, 0, self._fg)
        # Create the scroll buffer
        self._makescroll()
        # Fill for the first time
        self._fillscroll()
        # Show the initial output
        self.step(0) 
        return self._stepping

    def step(self, step=1):
        # skip if we are not active
        if self._string is None:
            return False
        # do animation step
        roll = False
        if self._stepping and (self._pause == 0) and (step > 0):
            self._scrollframe.scroll(-step, 0)
            self._stepcount += step
            if self._stepcount >= self._stringwidth + self._padding:
                self._fillscroll()
                roll = True
        # blit the output framebuffer to screen, we rely on the blit() for cropping
        # this is where colors are applied (via palette)
        self._device.blit(self._scrollframe, 0, self._y, -1, self._palette)
        self._pause = max(0, self._pause - 1)
        return roll

    def pause(self, pause=None):
        if pause is not None:
            self._pause = max(pause, -1)
            if self._verbose:
                print('pause: {}'.format(self._pause))
        return self._pause
