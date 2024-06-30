# ezFBmarquee.py() : a simple marquee for the micropython framebuffer.

# - Copyright (c) Owen Carter

import framebuf

# Basic marquee class
class ezFBmarquee():

    def __init__(self, display, font, x=0, y=0, width=None, hgap=0, fg=1, bg=0, verbose=False):

        self._device = display
        self._font = font
        self._x = x
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
        if width is None:
            try:
                self._width = self._device.width - self._x
            except: 
                r = "{}: Cannot determine display width; use 'width=<n>' in init()"
                raise ValueError(r.format(self.name))
        else:
            self._width = width
        # output framebuffer
        outbytes = ((self._width - 1) // 8 ) + 1
        self._outbuf = bytearray(outbytes * self._height)
        self._outframe = framebuf.FrameBuffer(self._outbuf, self._width, self._height, self._font_format)
        # Give info as needed
        if self._verbose:
            print('{}:'.format(self.name))
            print('  x: {}, y: {}, height: {}, width: {}'.format(self._x, self._y, self._height, self._width))
            print('  fg: {}, bg: {}, hgap: {}'.format(self._fg, self._bg, self._hgap))
 
    def _line_size(self, string):
        x = 0
        missing = self._missing = []
        for char in string:
            glyph, _, char_width = self._font.get_ch(char)
            if glyph is None:
                missing.append(char)
            x += char_width + self._hgap if char_width > 0 else 0
        x = x - self._hgap if x != 0 else x   # remove any trailing hgap
        if len(missing) > 0:
            self._missing = sorted(set(missing))
        return x, self._font.height()

    def _makescroll(self):
        self._stepping = True
        # Work out how long our string will be once rendered
        self._stringwidth, _ = self._line_size(self._string)
        # padding size between repeats, in px
        self._padding = int(self._width * self._seperation)
        # Give info as needed
        if self._verbose:
            print('{}:\n  string: {}'.format(self.name, self._string))
            print('  string width: {}px,  seperation: {}px'.format(self._stringwidth, self._padding))
            print('  fg: {}, bg: {}, hgap: {}'.format(self._fg, self._bg, self._hgap))
            print('  pause: {}'.format(self._padding, self._pause))
            if len(self._missing) > 0:
                m = '  The following requested characters could not be found in the font:\n{}'
                print(m.format(self.name, self._missing))
        # determine if we need to animate at all (static marquee always re-drawn on step())
        if self._stringwidth <= self._width:
            self._stepping = False
            if self._verbose:
                p = '{}: string width ({}) is smaller than screen width ({}), not animating'
                print(p.format(self.name, self._stringwidth, self._width))
        # Make the framebuffer that we scroll the output framebuffer over
        self._sbwide = self._stringwidth + self._padding + self._width
        sbbytes = ((self._sbwide - 1) // 8 ) + 1
        self._scrollbuf =  bytearray(sbbytes * self._height)
        self._scrollframe = framebuf.FrameBuffer(self._scrollbuf, self._sbwide, self._height, self._font_format)
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
        # blit the glyph with the background transparent
        buf = bytearray(glyph)
        charbuf = framebuf.FrameBuffer(buf, char_width, char_height, self._font_format)
        self._scrollframe.blit(charbuf, x, 0, 0)
        return char_width

    def _stop(self):
        self._string = None
        self._scrollcount = 0
        self._stepping = False
        self._stringwidth = 0
        self._padding = 0
        self._sbwide = 0
        del self._scrollframe, self._scrollbuf
        # blank; fill the output area with current background
        self._device.rect(self._x, self._y, self._width, self._height, self._bg, True)

    def set(self, string, seperation=0.5, pause=0, hgap=None, fg=None, bg=None):
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
        self._pause = max(0,int(pause))
        self._hgap = self._hgap if hgap is None else hgap
        # set color map
        self._palette.pixel(0, 0, self._bg)
        self._palette.pixel(self._font_colors -1, 0, self._fg)
        # Create and fill the scroll buffer
        self._makescroll()
        self._scrollcount = 0
        # Show the initial output
        self.step(0) 
        return self._stepping

    def step(self, step=1):
        # do nothing if we are not active
        if self._string is None:
            return False
        # do animation step, note if we rollover
        roll = False
        if self._stepping and (self._pause == 0) and (step > 0):
            self._scrollcount += step
            if self._scrollcount >= self._stringwidth + self._padding:
                self._scrollcount = 0
                roll = True
        # blit the scrollbuffer over outbuffer offset by scroll value
        self._outframe.blit(self._scrollframe, -self._scrollcount, 0)
        # blit the output framebuffer to screen, we rely on the blit() for cropping
        # this is where colors are applied (via palette), no transparency
        self._device.blit(self._outframe, self._x, self._y, -1, self._palette)
        # decrease the pause count if necesscary
        self._pause = max(0, self._pause - 1)
        return roll

    def pause(self, pause):
        self._pause = max(0, int(pause))
        if self._verbose:
            print('pause: {}'.format(self._pause))
