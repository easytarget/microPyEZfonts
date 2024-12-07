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
from math import ceil
from array import array

version = '0.33'
name = '0.0.1'
family = 'fixed'
weight = 'medium'
size = 32

_high  = 32    # height
_wide  = 16    # width
_slant = 0     # slant (TODO!)
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
    return _chars.keys[0]

def max_ch():
    return _chars.keys()[-1]

# segment polygons
# - indexed by an abbreviated name
# - values are an integer array of x,y pairs for use in framebuf.poly()
_segs = {
    'ul' : array('i', [1, 0, 2, 1, 13, 1, 14, 0]),  # base,
    'ml' : array('i', [1, 13, 2, 14, 13, 14, 14, 13]),  # middle
    'bl' : array('i', [1, 31, 2, 30, 13, 30, 14, 31]),  # base
    'lu' : array('i', [0, 1, 0, 12, 1, 12, 1, 2]),  # left upper
    'll' : array('i', [0, 14, 0, 30, 1, 29, 1, 15]),  # left lower
    'ru' : array('i', [15, 1, 15, 12, 14, 12, 14, 2]),  # right upper
    'rl' : array('i', [15, 14, 15, 30, 14, 29, 14, 15]),  # right lower
}

# character polygon lists
# - index is the integer character ord(),
# - value is a tuple with:
#   (active segments(list), full(bool:False=halfwidth)
# - keep this list ordered or max_char() will be wrong.
_chars = {
    32 : ([],True),                                    # space
    48 : (['ul','bl','lu','ll','ru','rl'],True),       # 0
    49 : (['ru','rl'],True),                           # 1
    50 : (['ul','ml','bl','ll','ru'],True),  # 2
    51 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # 3
    52 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # 4
    53 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # 5
    54 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # 6
    55 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # 7
    56 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # 8
    59 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # 9
    65 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # A
    66 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # B
    67 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # C
    68 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # D
    69 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # E
    70 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # F
}

# dictionary to hold cached chars
_g = {}

def _clean_cache():
    global _g
    _g = {}
    
def _gen(ch):
    # Generate a char using segment map.
    # - returns false if char not available
    ch = ord(ch) if type(ch) is str else ch
    if ch not in _chars.keys():
        return False
    print('rendering: ',ch)
    _g[ch] = _render(*_chars[ch])
    
def _render(segs,iswide):
    # Render the char using a framebuf
    # returns a bytearray
    # cache if needed
    # if wide is False; do a half-width char.  TODO
    wide = _wide if iswide else ceil(_wide/2)
    bytewide = ((wide - 1) // 8) + 1
    _buf = bytearray(_high * bytewide)
    _canvas = FrameBuffer(_buf, wide, _high, MONO_HLSB)
    for poly in segs:
        _canvas.poly(0,0,_segs[poly],1,True)
    return _buf
    

def set(height=None, width=None, slant=None, cached=None, pre=None):
    # Always clean cache, then set/override defaults
    # - Pre-cache any chars passed by 'pre'
    global _high, _wide, _slant, _cache
    _clean_cache()
    # modify defaults as required
    _high = height if height is not None else _high
    _wide = width if width is not None else _wide
    _slant = slant if slant is not None else _slant
    _cache = cached if cached is not None else _cache
    # constrain to value and type
    _high = int(max(5, _high))  # integer, min = 5
    _wide = int(max(5, _wide))  # integer, min = 5
    _slant = int(max(-_high, min(_high, _slant)))  # integer, max = (+/-)height
    _cache = bool(_cache)     # bool
    # precache
    if pre is not None:
        for ch in pre:
            _gen(ch)

def info():
    # useful for debug; returns height, width, slant,
    # cache active(bool),and any current chached chars as a list
    c = list(_g.keys())
    c.sort()
    return _wide, _high, _slant, _cache, c

def get_ch(ch):
    c = ord(ch)
    if c not in _chars.keys():
        return None, 0, 0
    if c not in _g.keys():
        _gen(ch)
    return memoryview(_g[c]), _high, _wide   # todo, half-wide..
