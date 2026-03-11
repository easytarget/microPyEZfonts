'''
    ezFBsevenSeg.py: part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py
'''
'''
MIT License

Copyright (c) 2026 Owen Carter

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from framebuf import FrameBuffer, MONO_HLSB
from math import ceil


# character element lists
# - index is the integer character ord(),
_CHARS_FULL = {
    32 : [],                                    # space
    45 : ['bm'],                                # negative: '-'
    48 : ['bt','bb','lu','ll','ru','rl'],       # 0
    49 : ['ru','rl'],                           # 1
    50 : ['bt','bm','bb','ll','ru'],            # 2
    51 : ['bt','bm','bb','ru','rl'],            # 3
    52 : ['bm','lu','ru','rl'],                 # 4
    53 : ['bt','bm','bb','lu','rl'],            # 5
    54 : ['bt','bm','bb','lu','ll','rl'],       # 6
    55 : ['bt','ru','rl'],                      # 7
    56 : ['bt','bm','bb','lu','ll','ru','rl'],  # 8
    57 : ['bt','bm','bb','lu','ru','rl'],       # 9
    65 : ['bt','bm','lu','ll','ru','rl'],       # A
    66 : ['bm','bb','lu','ll','rl'],            # B
    67 : ['bt','bb','lu','ll'],                 # C
    68 : ['bm','bb','ll','rl','ru'],            # D
    69 : ['bt','bm','bb','lu','ll'],            # E
    70 : ['bt','bm','lu','ll'],                 # F
}

_CHARS_HALF = {
    46 : ['de'],       # decimal point: '.'
    58 : ['cu','cl'],  # semicolon: ':'
    183 : ['dm'],      # middle dot: unicode u+00B7
    729 : ['da'],      # dot above: unicode u+02D9
    8201 : [],         # thin space: unicode u+2009
}

_ALL_CHARS = list(_CHARS_FULL.keys()) + list(_CHARS_HALF.keys())

class SEVEN_SEG:
    # Some (faked) standard fields for mPY fonts
    version = '1.0'
    name = 'seven_segment'
    family = 'lcd'
    weight = 'medium'
    size = 32   # default

    def __init__(self, height, width,
                 led_high=None, led_wide=None,
                 led_thick=3, led_gap=3,
                 use_cache=True, precache=None):
        self.__name__ = '{}-{}x{}'.format(self.__module__, height, width)
        # Sensible (?) defaults
        led_high = int(height * 0.8) if led_high is None else led_high
        led_wide = int(width * 0.8) if led_wide is None else led_wide
        self.set(height, width, led_high, led_wide, led_thick, led_gap, use_cache, precache)

    '''
        Internal methods specific to the Seven Segment font
    '''

    def _gen(self, ch):
        # Generate a char using segment map
        if ch in _CHARS_FULL.keys():
            return self._render_full(_CHARS_FULL[ch])
        else:
            return self._render_half(_CHARS_HALF[ch])

    def _render_full(self, segments):
        # Render the char using a framebuf, returns a bytearray
        bytewide = ((self._wide - 1) // 8) + 1
        buf = bytearray(self._high * bytewide)
        canvas = FrameBuffer(buf, self._wide, self._high, MONO_HLSB)
        self._draw_full(canvas, self._led_wide, self._led_high, self._led_thick, self._led_gap, segments)
        buf.append(self._wide)
        return buf

    def _render_half(self, segments):
        # Render the char using a half-width framebuf, returns a bytearray
        wide = ceil(self._wide/2)
        led_wide = ceil(self._led_wide/2)
        bytewide = ((wide - 1) // 8) + 1
        buf = bytearray(self._high * bytewide)
        canvas = FrameBuffer(buf, wide, self._high, MONO_HLSB)
        self._draw_half(canvas, led_wide, self._led_high, self._led_thick, segments)
        buf.append(wide)
        return buf

    def _draw_full(self, canvas, X, Y, T, G, elements):
        '''
            Draw a Full-Width character using the 7 led segments
        '''
        # Draw the required bars in full (intersecting)
        M = int(Y/2)
        for l in range(T):
            if 'bt' in elements:
                canvas.hline(l, l, X-(2*l), 1)
            if 'lu' in elements:
                canvas.vline(l, l, M-(2*l), 1)
            if 'ru' in elements:
                canvas.vline(X-l-1, l, M-(2*l), 1)
            if 'bm' in elements:
                canvas.hline(l, M+l, X-(2*l), 1)
            if 'll' in elements:
                canvas.vline(l, M+l, M-(2*l), 1)
            if 'rl' in elements:
                canvas.vline(X-l-1,  M+l, M-(2*l), 1)
            if 'bb' in elements:
                canvas.hline(l, Y-l-1, X-(2*l), 1)
        # Now create the gaps that seperate them
        for l in range(G):
            f = (l+1)//2
            (x, y) = (f, 0) if l % 2 else (0, f)
            canvas.line(x, y, T + x, T + y, 0)
            canvas.line(X - x - 1, y, X - T - x - 1, T + y, 0)
            canvas.line(x, M + y, T + x, M + T + y, 0)
            canvas.line(X - x - 1, M + y, X - T - x - 1, M + T + y, 0)
            canvas.line(x, Y - y - 1, T + x, Y - T - y - 1, 0)
            canvas.line(X - x - 1, Y - y - 1, X - T - x - 1, Y - T - y - 1, 0)

    def _draw_half(self, canvas, X, Y, T, elements):
        U = int(Y*0.35)
        M = int(Y/2)
        L = int(Y*0.68)
        C = int(X/2)
        i = int(T/2)
        if 'de' in elements:
            canvas.rect(C-i, Y-T, T, T, 1, True)
        if 'dm' in elements:
            canvas.rect(C-i, M-i, T, T, 1, True)
        if 'da' in elements:
            canvas.rect(C-i, 0, T, T, 1, True)
        if 'cu' in elements:
            canvas.rect(C-i, U-i, T, T, 1, True)
        if 'cl' in elements:
            canvas.rect(C-i, L-i, T, T, 1, True)

    '''
        Standard public methods for a micropython font
    '''

    def height(self):
        return self._high

    def baseline(self):
        return self._high

    def max_width(self):
        return self._wide

    def hmap(self):
        return True

    def reverse(self):
        return False

    def monospaced(self):
        return False

    def min_ch(self):
        return min(_ALL_CHARS)

    def max_ch(self):
        return max(_ALL_CHARS)

    # NEEDS HEAVY RE_WRITE
    def set(self, height=None, width=None,
                  led_high=None, led_wide=None,
                  led_thick=None, led_gap=None,
                  cached=None, precache=None):
        '''
            Set the font parameters
            -   See init() for description.
            -   All parameters are optional
            -   Always clears the cache
        '''
        # Always clean cache
        self._cache = {}
        # constrain
        # TODO
        # set new value as necesscary
        self._high = height if height is not None else self._high
        self._wide = width if width is not None else self._wide
        self._led_high = led_high if led_high is not None else self._led_high
        self._led_wide = led_wide if led_wide is not None else self._led_wide
        self._led_thick = led_thick if led_thick is not None else self._led_thick
        self._led_gap = led_gap if led_gap is not None else self._led_gap
        self._use_cache = cached if cached is not None else self._use_cache
        # Pre-cache any chars passed by 'pre'
        # - this works even if caching is disabled
        if precache is not None:
            for ch in precache:
                _, _, _ = self.get_ch(ch)

    # DEBUG: remove this later..
    def info(self):
        # useful for debug; returns height, width
        # cache active(bool),and any current chached chars as a list
        c = list(self._cache.keys())
        c.sort()
        return self._wide, self._high, self._led_thick, self._led_gap, self._use_cache, c

    '''
        get_ch() returns the glyph data
    '''
    def get_ch(self, ch):
        c = ord(ch)
        if c not in _ALL_CHARS:
            return None, 0, 0
        if c not in self._cache.keys():
            buf = self._gen(c)
            if self._use_cache:
               self._cache[c] = buf
        else:
            buf = self._cache[c]
        return memoryview(buf), self._high, int(buf[-1])

