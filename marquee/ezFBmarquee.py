# ezFBmarquee.py() : a simple marquee for the micropython framebuffer.

# - Copyright (c) Owen Carter

import framebuf

# Basic marquee class
class ezFBmarquee():

    def __init__(self, display, font, x=0, y=0, width=None, pre=0, pad=0.33, pause=0, hgap=0, fg=1, bg=0, verbose=False):

        self._device = display
        self._font = font
        self._x = x
        self._y = y
        self._pre = max(pre,0)
        self._pad = max(pad,0)
        self._dpause = self._pause = max(0,int(pause))
        self._hgap = int(hgap)
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
            print('{}: init()'.format(self.name))
            print('  x: {}, y: {}, height: {}, width: {}'.format(self._x, self._y, self._height, self._width))
            print('  pad: {}, default pause: {}, hgap: {}'.format(self._pad, self._dpause, self._hgap))
            print('  fg: {}, bg: {}'.format(self._fg, self._bg))
 
    def _line_size(self, string, hgap):
        # Find the pixel size of a string with hgap applied
        x = 0
        missing = self._missing = []
        for char in string:
            glyph, _, char_width = self._font.get_ch(char)
            if glyph is None:
                missing.append(char)
                continue
            x += char_width + hgap
        x = x - hgap if x != 0 else x   # remove any trailing hgap
        if len(missing) > 0:
            self._missing = sorted(set(missing))
        return x

    def _makescroll(self, string, hgap, pad):
        # Make the framebuffer that we 'scroll' across the output buffer
        self._stepping = True
        # Work out how long our string will be once rendered
        self._stringwidth = self._line_size(string, hgap)
        # padding size between repeats, in px
        self._padding = int(self._width * pad)
        # determine if we need to animate
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
        for c in string:
            xpos += self._put_char(c, xpos, hgap)
        xpos = xpos - hgap if xpos != 0 else xpos   # remove any trailing hgap
        if not self._stepping:
            return  # skip rollover space and chars
        xpos += self._padding
        for c in string:
            if xpos >= self._sbwide:
                break
            xpos += self._put_char(c, xpos, hgap)

    def _put_char(self, char, x, hgap):
        # fetch the glyph
        glyph, char_height, char_width = self._font.get_ch(char)
        if glyph is None:
            return 0  # Nothing to write
        # blit the glyph with the background transparent
        buf = bytearray(glyph)
        charbuf = framebuf.FrameBuffer(buf, char_width, char_height, self._font_format)
        self._scrollframe.blit(charbuf, x, 0, 0)
        return char_width + hgap

    def _stop(self):
        self._string = None
        self._scrollcount = 0
        self._stepping = False
        self._stringwidth = 0
        self._padding = 0
        self._sbwide = 0
        del self._scrollframe, self._scrollbuf
        # Fill the output area with current background
        self._device.rect(self._x, self._y, self._width, self._height, self._bg, True)
        if self._verbose:
            print('{}: stop()'.format(self.name))

    def text(self, string, pre=None, pad=None, pause=None, hgap=None, fg=None, bg=None):
        self._string = None   # stop ISR step() calls
        # start marquee with string, returns false if not animated
        # always do defaults
        pre = self._pre if pre is None else max(pre,0)
        pad = self._pad if pad is None else max(pad,0)
        self._pause = self._dpause if pause is None else max(0,int(pause))
        hgap = self._hgap if hgap is None else int(hgap)
        fg = self._fg if fg is None else fg
        bg = self._bg if bg is None else bg
        # set color map
        self._palette.pixel(0, 0, bg)
        self._palette.pixel(self._font_colors -1, 0, fg)
        # stop when string is None
        if string is None:
            self._stop()
            return False
        # only take the first line of the string
        string = string.split('\n')[0]
        # Create and fill the scroll buffer
        self._makescroll(string, hgap, pad)
        self._scrollcount = -int(self._width * pre)
        # Give info as needed
        if self._verbose:
            print('{}: start()\n  string: {}'.format(self.name, string))
            print('  string width: {}px,  pad: {}px'.format(self._stringwidth, self._padding))
            print('  fg: {}, bg: {}, hgap: {}'.format(fg, bg, hgap))
            print('  pad: {}, pause: {}'.format(pad, self._pause))
            if len(self._missing) > 0:
                m = '  The following requested characters could not be found in the font:\n  {}'
                print(m.format(self._missing))
        # Set active and show the initial output
        self._outframe.fill(0)
        self._string = string
        self.step(0) 
        return self._stepping

    def step(self, step=1, event='rollover'):
        # Step the marquee as necesscary
        if event not in ['rollover', 'endstr', 'endpad', 'endchr']:
            raise ValueError('{}: step(), Unknown event {}'.format(self.name, event))
        # do nothing if we are not active
        if self._string is None:
            return False
        # do animation step, note if we hit an event
        res = False
        if self._stepping and (self._pause == 0) and (step > 0):
            self._scrollcount += step
            if (self._scrollcount >= (self._stringwidth - self._width)) and event == 'endchr':
                # the last character of the string just became visible
                self._scrollcount = 0
                res = True
                if self._verbose:
                    print('{}: last character'.format(self.name))
            if (self._scrollcount >= (self._stringwidth + self._padding - self._width)) and event == 'endpad':
                # the full end padding of the string just became visible
                self._scrollcount = 0
                res = True
                if self._verbose:
                    print('{}: last character'.format(self.name))
            elif (self._scrollcount >= self._stringwidth) and event == 'endstr':
                # the last character of the string has been scrolled off
                self._scrollcount = 0
                res = True
                if self._verbose:
                    print('{}: padding end'.format(self.name))
            elif (self._scrollcount >= (self._stringwidth + self._padding)) and event == 'rollover':
                # the string has wrapped around to the beginning
                self._scrollcount = 0
                res = True
                if self._verbose:
                    print('{}: rollover to start'.format(self.name))
        # blit the scrollbuffer over outbuffer offset by scroll value
        self._outframe.blit(self._scrollframe, -self._scrollcount, 0)
        # blit the output framebuffer to screen, we rely on the blit() for cropping
        # this is where colors are applied (via palette), no transparency
        self._device.blit(self._outframe, self._x, self._y, -1, self._palette)
        # decrease the pause count if necesscary
        self._pause = max(0, self._pause - 1)
        return res

    def pause(self, pause):
        self._pause = max(0, int(pause))
        if self._verbose:
            print('{}: pause: {}'.format(self.name, self._pause))
