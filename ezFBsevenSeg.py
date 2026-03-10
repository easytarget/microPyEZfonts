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
    return _chars.keys[0]

def max_ch():
    return _chars.keys()[-1]

# segment polygons
# - indexed by an abbreviated name
# - values are a list of x,y pairs between 0->1 that are scaled for use in framebuf.poly()
_segs = {
    # conventional 7 segment
    'ul' : [0.1333, 0, 0.2, 0.0323, 0.8, 0.0323, 0.8667, 0],                  # base,
    'ml' : [0.1333, 0.4516, 0.2, 0.4839, 0.8, 0.4839, 0.8667, 0.4516],        # middle
    'bl' : [0.1333, 1, 0.2, 0.9677, 0.7333, 0.9677, 0.8667, 1],               # base
    'lu' : [0.0667, 0.0323, 0.0667, 0.4194, 0.1333, 0.4194, 0.1333, 0.0645],  # left upper
    'll' : [0.0667, 0.4839, 0.0667, 0.9677, 0.1333, 0.9355, 0.1333, 0.5161],  # left lower
    'ru' : [0.9333, 0.0323, 0.9333, 0.4194, 0.8667, 0.4194, 0.8667, 0.0645],  # right upper
    'rl' : [0.9333, 0.4839, 0.9333, 0.9677, 0.8667, 0.9355, 0.8667, 0.5161],  # right lower
    # Special Symbols - TODO:REDUCE
   'dec' : [0.4286, 0.9677, 0.4286, 1, 0.5714, 1, 0.5714, 0.9677],            # decimal point
   'cou' : [0.4286, 0.2581, 0.4286, 0.2903, 0.5714, 0.2903, 0.5714, 0.2581],  # colon upper
   'col' : [0.4286, 0.6452, 0.4286, 0.6774, 0.5714, 0.6774, 0.5714, 0.6452],  # colon lower
   'min' : [0.1429, 0.4516, 0.1429, 0.4839, 0.8571, 0.4839, 0.8571, 0.4516],  # minus
   'pls' : [0.4286, 0.3226, 0.4286, 0.6129, 0.5714, 0.6129, 0.5714, 0.3226],  # plus (bar, goes with minus)
   'sel' : [0.1429, 0, 0.1429, 0.1613, 0.2857, 0.1613, 0.2857, 0],            # seconds left
   'ser' : [0.7143, 0, 0.7143, 0.1613, 0.8571, 0.1613, 0.8571, 0],            # seconds right
   'mns' : [0.4286, 0, 0.4286, 0.1613, 0.5714, 0.1613, 0.5714, 0],            # minutes
   'dgl' : [0.1429, 0.0323, 0.1429, 0.129, 0.2857, 0.129, 0.2857, 0.0323],    # degrees left
   'dgr' : [0.7143, 0.0323, 0.7143, 0.129, 0.8571, 0.129, 0.8571, 0.0323],    # degrees right
   'dgu' : [0.2857, 0, 0.2857, 0.0323, 0.7143, 0.0323, 0.7143, 0],            # degrees upper
   'dgb' : [0.2857, 0.129, 0.2857, 0.1613, 0.7143, 0.1613, 0.7143, 0.129],    # degrees lower  
   'pul' : [0.1429, 0, 0.1429, 0.0323, 0.2857, 0.0323, 0.2857, 0],            # percent upper left
   'plr' : [0.7143, 0.1935, 0.7143, 0.2258, 0.8571, 0.2258, 0.8571, 0.1935],  # percent lower right
   'psl' : [0.1429, 0.1935, 0.1429, 0.2258, 0.7143, 0.0323, 0.7143, 0],       # percent slant
}

# character polygon lists
# - index is the integer character ord(),
# - value is a tuple with:
#   (active segments(list), full(bool:False=halfwidth)
# - keep this list ordered or max_char() will be wrong.
_chars = {
    32 : ([],False),                                   # space
    34 : (['sel','ser'],False),                        # "
    37 : (['pul','plr','psl'],False),                  # %
    39 : (['mns'],False),                              # '
    43 : (['min','pls'],False),                        # +
    45 : (['min'],False),                              # -
    46 : (['dec'],False),                              # .
    48 : (['ul','bl','lu','ll','ru','rl'],True),       # 0
    49 : (['ru','rl'],True),                           # 1
    50 : (['ul','ml','bl','ll','ru'],True),            # 2
    51 : (['ul','ml','bl','ru','rl'],True),            # 3
    52 : (['ml','lu','ru','rl'],True),                 # 4
    53 : (['ul','ml','bl','lu','rl'],True),            # 5
    54 : (['ul','ml','bl','lu','ll','rl'],True),       # 6
    55 : (['ul','ru','rl'],True),                      # 7
    56 : (['ul','ml','bl','lu','ll','ru','rl'],True),  # 8
    57 : (['ul','ml','bl','lu','ru','rl'],True),       # 9
    58 : (['cou','col'],False),                        # :
    65 : (['ul','ml','lu','ll','ru','rl'],True),       # A
    66 : (['ml','bl','lu','ll','rl'],True),            # B
    67 : (['ul','bl','lu','ll'],True),                 # C
    68 : (['ml','bl','ll','rl','ru'],True),            # D
    69 : (['ul','ml','bl','lu','ll'],True),            # E
    70 : (['ul','ml','lu','ll'],True),                 # F
   176 : (['dgl','dgr','dgu','dgb'],False),            # °
}

# dictionary to hold cached chars
_g = {}

'''
def conv():
    for k in _segs.keys():
        new = array('i',[])
        if k in ['ul','ml','bl','lu','ll','ru','rl']:
            ws = 1 / 15
        else:
            ws = 1 / 7
        hs = 1 / 31
        print('{:>8} '.format("'{}'".format(k)), end=': [')
        for i in range(0,len(_segs[k]),2):
            x = round(_segs[k][i] * ws, 4)
            y = round(_segs[k][i+1] * hs, 4)
            print('{:g}, {:g}'.format(x,y), end=', ')
        print(']')
'''

def _clean_cache():
    global _g
    _g = {}

def _gen(ch):
    # Generate a char using segment map and adds
    # - returns false if char not available
    ch = ord(ch) if type(ch) is str else ch
    if ch not in _chars.keys():
        return None
    return _render(*_chars[ch])

def _render(segments,iswide):
    # Render the char using a framebuf
    # returns a bytearray
    # cache if needed
    # if wide is False; do a half-width char.  TODO
    wide = _wide if iswide else ceil(_wide/2)
    bytewide = ((wide - 1) // 8) + 1
    buf = bytearray(_high * bytewide)
    canvas = FrameBuffer(buf, wide, _high, MONO_HLSB)
    for poly in segments:
        pa = array('i',[])
        pd = _segs[poly]
        for i in range(0,len(pd),2):
            pa.append(round(pd[i] * wide))
            pa.append(round(pd[i+1] * _high))
        canvas.poly(0,0,pa,1,True)
    buf.append(wide)
    return buf


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
            _, _, _ = get_ch(ch)

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
        buf = _gen(c)
        if _cache:
           _g[c] = buf
    else:
        buf = _g[c]
    return memoryview(buf), _high, int(buf[-1])

