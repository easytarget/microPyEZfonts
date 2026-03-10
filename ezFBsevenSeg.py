'''
    ezFBsevenSeg.py: part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py
'''
'''
    Copyright:
'''
from framebuf import FrameBuffer, MONO_HLSB
from math import ceil, floor
from array import array

version = '0.33'
name = '0.0.1'
family = 'fixed'
weight = 'medium'
size = 32

_high  = 32    # height
_wide  = 16    # width
_cache = True  # cached

def height():
    return _high

def baseline():
    return _high

def max_width():
    return _wide

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return min(_all_chars)

def max_ch():
    return max(_all_chars)

# character polygon lists
# - index is the integer character ord(),
# - value is a tuple with:
# - keep these list ordered or max_char() will be wrong.
_chars_full = {
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

_chars_half = {
    46 : ['de'],       # decimal point: '.'
    58 : ['cu','cl'],  # semicolon: ':'
    8201 : [],         # thin space: unicode u+2009
}

_all_chars = list(_chars_full.keys()) + list(_chars_half.keys())

# dictionary to hold cached chars
_g = {}

def _clean_cache():
    global _g
    _g = {}

def _gen(ch):
    # Generate a char using segment map
    if ch in _chars_half.keys():
        return _render_half(_chars_half[ch])
    else:
        return _render_full(_chars_full[ch])

def _render_full(segments):
    # Render the char using a framebuf
    # returns a bytearray
    bytewide = ((_wide - 1) // 8) + 1
    buf = bytearray(_high * bytewide)
    canvas = FrameBuffer(buf, _wide, _high, MONO_HLSB)
    _draw_full(canvas, _wide, _high, segments, thick=2, gap=1)
    buf.append(_wide)
    return buf

def _render_half(segments):
    # Render the char using a framebuf
    # returns a bytearray
    wide = ceil(_wide/2)
    bytewide = ((wide - 1) // 8) + 1
    buf = bytearray(_high * bytewide)
    canvas = FrameBuffer(buf, wide, _high, MONO_HLSB)
    _draw_full(canvas, wide, _high, segments, thick=2, gap=1)
    buf.append(wide)
    return buf

def _draw_full(canvas, X, Y, elements, thick, gap):
    # Main body bars
    M = int(Y/2)
    for l in range(thick):
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
    # Now create gaps between them
    for l in range(gap):
        f = (l+1)//2
        (x, y) = (f, 0) if l % 2 else (0, f)
        canvas.line(x, y, thick+x, thick+y, 0)
        canvas.line(X - x-1, y, X-thick-x-1, thick+y, 0)
        canvas.line(x, M+y, thick+x, M+thick + y, 0)
        canvas.line(X-x-1, M+y, X-thick-x-1, M + thick+y, 0)
        canvas.line(x, Y-y-1, thick+x, Y-thick-y - 1, 0)
        canvas.line(X-x-1, Y-y-1, X-thick-x-1, Y-thick-y-1, 0)


# NEEDS HEAVY RE_WRITE
def set(height=None, width=None, thick=None, gap=None, cached=None, pre=None):
    # Always clean cache, then set/override defaults
    # - Pre-cache any chars passed by 'pre'
    global _high, _wide, _cache
    _clean_cache()
    # modify defaults as required
    _high = height if height is not None else _high
    _wide = width if width is not None else _wide
    _cache = cached if cached is not None else _cache
    # constrain to value and type
    _high = int(max(5, _high))  # integer, min = 5
    _wide = int(max(5, _wide))  # integer, min = 5
    _cache = bool(_cache)     # bool
    # precache
    if pre is not None:
        for ch in pre:
            _, _, _ = get_ch(ch)

def info():
    # useful for debug; returns height, width
    # cache active(bool),and any current chached chars as a list
    c = list(_g.keys())
    c.sort()
    return _wide, _high, _cache, c

def get_ch(ch):
    c = ord(ch)
    if c not in _all_chars:
        return None, 0, 0
    if c not in _g.keys():
        buf = _gen(c)
        if _cache:
           _g[c] = buf
    else:
        buf = _g[c]
    return memoryview(buf), _high, int(buf[-1])

