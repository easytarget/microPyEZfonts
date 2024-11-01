# ezFBmarquee.py() : a simple marquee for the micropython framebuffer.
# See WRITER.md for documentation

# - Copyright (c) Owen Carter

import framebuf

# Basic marquee class
class ezFBmarquee():

    def __init__(self, display, font,
                 x=0, y=0,
                 width=None,
                 mode='marquee',
                 pad=0.33, pause=0, hgap=0,
                 fg=1, bg=0,
                 cswap = False,
                 verbose=False):

        self._device = display
        self._font = font
        self._x = x
        self._y = y
        self._mode = self._checkmode(mode)
        self._pad = max(pad,0)
        self._dpause = self._pause = max(-1,int(pause))
        self._hgap = int(hgap)
        self._fg = fg
        self._bg = bg
        self._cswap = cswap
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
            print('{}: init()\n  mode: {}'.format(self.name, self._mode))
            print('  x: {}, y: {}, height: {}, width: {}'.format(self._x, self._y, self._height, self._width))
            print('  pad: {}, default pause: {}, hgap: {}'.format(self._pad, self._dpause, self._hgap))
            print('  fg: {}, bg: {}'.format(self._fg, self._bg))

    def _line_size(self, string, hgap):
        # Find the pixel size of a string with hgap applied
        x = 0
        self._missing = []
        for char in string:
            glyph, _, char_width = self._font.get_ch(char)
            if glyph is None:
                self._missing.append(char)
                continue
            x += char_width + hgap
        x = x - hgap if x != 0 else x   # remove any trailing hgap
        if len(self._missing) > 0:
            self._missing = sorted(set(self._missing))
        return x

    def _checkmode(self, mode):
        if mode not in ['marquee', 'scroller']:
            raise ValueError("{}: unknown mode '{}'".format(self.name, mode))
        return mode

    def _makescroll(self, string, mode, hgap, pad):
        # Make the framebuffer that we 'scroll' across the output buffer
        # Work out how long our string will be once rendered
        self._stringwidth = max(self._line_size(string, hgap), 1)
        # Make the framebuffer that we scroll the output framebuffer over
        if mode == 'marquee':
            self._padding = int(self._width * pad)
            self._sbwide = self._stringwidth + self._padding + self._width
            self._start = 0
            self._end = max(self._width, self._stringwidth + self._padding)
        elif mode == 'scroller':
            self._padding = self._width
            self._sbwide = self._stringwidth + self._width
            self._start = - self._padding
            self._end = self._stringwidth
        sbbytes = ((self._sbwide - 1) // 8 ) + 1
        self._scrollbuf =  bytearray(sbbytes * self._height)
        self._scrollframe = framebuf.FrameBuffer(self._scrollbuf, self._sbwide, self._height, self._font_format)
        # write our string, add the seperator, then start the string again
        xpos = 0
        for c in string:
            xpos += self._put_char(c, xpos, hgap)
        xpos = xpos - hgap if xpos != 0 else xpos   # remove any trailing hgap
        if (xpos >= self._width) and (mode == 'marquee'):
            xpos += self._padding
            for c in string:
                if xpos >= self._sbwide:
                    break
                xpos += self._put_char(c, xpos, hgap)
        # determine if we need to animate
        self._stepping = True
        if (self._stringwidth <= self._width) and (mode == 'marquee'):
            self._stepping = False
        # fill the outframe with the first frame
        self._outframe.blit(self._scrollframe, -self._start, 0)

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

    def stop(self):
        self._string = None
        self._count = 0
        self._stepping = False
        self._stringwidth = 0
        self._padding = 0
        self._sbwide = 0
        # delete the scroll buffer and frame
        del self._scrollframe, self._scrollbuf
        # clean the output framebuffer
        self._outframe.fill(0)
        # Fill the output area with current background
        self._device.rect(self._x, self._y, self._width, self._height, self._bg, True)
        if self._verbose:
            print('{}: stop()'.format(self.name))

    def start(self, string, mode=None, pause=None, pad=None, hgap=None, fg=None, bg=None):
        def swap_bytes(color):
            # flip the left and right bytes in a 16 bit color word if required
            return ((color & 255) << 8) + (color >> 8) if self._cswap else color

        if self._string is not None:
            self.stop()
        mode = self._mode if mode is None else self._checkmode(mode)
        self._pause = self._dpause if pause is None else max(-1,int(pause))
        pad = self._pad if pad is None else max(pad,0)
        hgap = self._hgap if hgap is None else int(hgap)
        fg = self._fg if fg is None else fg
        bg = self._bg if bg is None else bg
        # set color map
        self._palette.pixel(0, 0, swap_bytes(bg))
        self._palette.pixel(self._font_colors -1, 0, swap_bytes(fg))
        # Create and fill the scroll buffer and attributes
        self._makescroll(string, mode, hgap, pad)
        # Set active and show the initial output
        self._string = string
        self._count = self._start
        self.step(0)
        # Give info as needed
        if self._verbose:
            print('{}: start()\n  {}: {}'.format(self.name, mode, string))
            print('  string width: {}px,  pad: {}px'.format(self._stringwidth, self._padding))
            print('  fg: {}, bg: {}, hgap: {}'.format(fg, bg, hgap))
            print('  pad: {}, pause: {}'.format(pad, self._pause))
            if not self._stepping:
                print('  marquee string is shorter than output width, not animating')
            if len(self._missing) > 0:
                m = '  The following requested characters could not be found in the font:\n  {}'
                print(m.format(self._missing))

    def step(self, steps=1):
        # Step the marquee as necesscary
        steps = max(0,min(steps, self._width))
        if self._string is None:
            return False
        # Do animation step
        res = False
        if (self._pause == 0) and (steps > 0):
            self._count += steps
            # Blit the scrollbuffer over outbuffer offset by scroll value
            if self._stepping:
                self._outframe.blit(self._scrollframe, -self._count, 0)
            # Catch rollover
            if self._count >= self._end:
                self._count = self._start
                res = True
                if self._verbose:
                    print('{}: rollover'.format(self.name))
        # Blit the output frame to screen, with colors are applied via palette
        self._device.blit(self._outframe, self._x, self._y, -1, self._palette)
        # Decrease the pause count towards zero
        self._pause = -1 if self._pause == -1 else max(0, self._pause - 1)
        # return rollover status
        return res

    def pause(self, pause):
        # Pause for the next 'pause' steps
        self._pause = max(-1, int(pause))
        if self._verbose:
            print('{}: pause: {}'.format(self.name, self._pause))

    def active(self):
        # Return true if active
        return False if self._string is None else True
