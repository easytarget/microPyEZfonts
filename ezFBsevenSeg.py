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
version = '0.33'
name = '0.0.1'
family = 'fixed'
weight = 'medium'
size = 32

h = 32    # height
w = 16    # width
s = 0     # slant, todo!
c = True  # cache

def height():
    return h

def baseline():
    return h

def max_width():
    return w

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return charmap.keys[0]

def max_ch():
    return return charmap.keys()[-1]

def set(high=None, wide=None, slanted=None, cached=None, pre=None)
    _clean_cache()
    # modify defaults as required
    h = high if high is not None else h
    wide = wide if wide is not None else w
    slant = slanted if slant is not None else s
    cahched = cached if cached is not None else c
    # constrain to value and type
    h = int(max(5,h))           # integer, min = 5
    w = int(max(5,w))           # integer, min = 5
    s = int((max(-h,min(h,s)))  # integer, max = (+/-)height
    c = bool(cached)            # bool
    # precache
    if pre is not None:
        for ch in pre[0:-1]:
            _gen(ch)

def get():
    # returns height, width, slant, cache(bool)
    # and the currently chached chars as a list
    return w, h, s, c, cache.keys().sort()

# segment polygons
segs = {}

# character polygon lists
chars = {}

# dictionary to hold cached chars
_g = {}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 26, 16
