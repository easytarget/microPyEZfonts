'''
    ezFBfont_08_5x8_upper : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 5x8.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Public domain font.  Share and enjoy."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: 5x8
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/5x8.bdf', '_', './upper-char.set']
# Date: 2024-06-12 20:06:29

version = '0.33'
name = '-Misc-Fixed-Medium-R-Normal--8-80-75-75-C-50-ISO10646-1'
family = 'fixed'
weight = 'medium'
size = 8

def height():
    return 8

def baseline():
    return 7

def max_width():
    return 5

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 95

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00'],
 33:[b'\x00    \x00 \x00'],
 34:[b'\x00PPP\x00\x00\x00\x00'],
 35:[b'PP\xf8P\xf8PP\x00'],
 36:[b' p\xa0p(p \x00'],
 37:[b'\x00@P P\x10\x00\x00'],
 38:[b'@\xa0\xa0@\xa0\xa0P\x00'],
 39:[b'\x00   \x00\x00\x00\x00'],
 40:[b'\x00 @@@@ \x00'],
 41:[b'\x00@    @\x00'],
 42:[b'\x00\x00\x90`\xf0`\x90\x00'],
 43:[b'\x00\x00  \xf8  \x00'],
 44:[b'\x00\x00\x00\x00\x000 @'],
 45:[b'\x00\x00\x00\x00\xf0\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00 p '],
 47:[b'\x00\x10\x10 @\x80\x80\x00'],
 48:[b'\x00 PPPP \x00'],
 49:[b'\x00 `   p\x00'],
 50:[b'\x00`\x90\x10`\x80\xf0\x00'],
 51:[b'\x00\xf0 `\x10\x90`\x00'],
 52:[b'\x00 `\xa0\xf0  \x00'],
 53:[b'\x00\xf0\x80\xe0\x10\x90`\x00'],
 54:[b'\x00`\x80\xe0\x90\x90`\x00'],
 55:[b'\x00\xf0\x10  @@\x00'],
 56:[b'\x00`\x90`\x90\x90`\x00'],
 57:[b'\x00`\x90\x90p\x10`\x00'],
 58:[b'\x00\x00``\x00``\x00'],
 59:[b'\x00\x0000\x000 @'],
 60:[b'\x00\x10 @@ \x10\x00'],
 61:[b'\x00\x00\x00\xf0\x00\xf0\x00\x00'],
 62:[b'\x00@ \x10\x10 @\x00'],
 63:[b'\x00 P\x10 \x00 \x00'],
 64:[b'0H\x98\xa8\xa8\x90@0'],
 65:[b'\x00`\x90\x90\xf0\x90\x90\x00'],
 66:[b'\x00\xe0\x90\xe0\x90\x90\xe0\x00'],
 67:[b'\x00`\x90\x80\x80\x90`\x00'],
 68:[b'\x00\xe0\x90\x90\x90\x90\xe0\x00'],
 69:[b'\x00\xf0\x80\xe0\x80\x80\xf0\x00'],
 70:[b'\x00\xf0\x80\xe0\x80\x80\x80\x00'],
 71:[b'\x00`\x90\x80\xb0\x90`\x00'],
 72:[b'\x00\x90\x90\xf0\x90\x90\x90\x00'],
 73:[b'\x00p    p\x00'],
 74:[b'\x00p   \xa0@\x00'],
 75:[b'\x00\x90\xa0\xc0\xa0\xa0\x90\x00'],
 76:[b'\x00\x80\x80\x80\x80\x80\xf0\x00'],
 77:[b'\x00\x90\xf0\xf0\x90\x90\x90\x00'],
 78:[b'\x00\x90\xd0\xf0\xb0\xb0\x90\x00'],
 79:[b'\x00`\x90\x90\x90\x90`\x00'],
 80:[b'\x00\xe0\x90\x90\xe0\x80\x80\x00'],
 81:[b'\x00`\x90\x90\xd0\xb0`\x10'],
 82:[b'\x00\xe0\x90\x90\xe0\x90\x90\x00'],
 83:[b'\x00`\x90@ \x90`\x00'],
 84:[b'\x00p     \x00'],
 85:[b'\x00\x90\x90\x90\x90\x90`\x00'],
 86:[b'\x00\x90\x90\x90\x90``\x00'],
 87:[b'\x00\x90\x90\x90\xf0\xf0\x90\x00'],
 88:[b'\x00\x90\x90``\x90\x90\x00'],
 89:[b'\x00\x88\x88P   \x00'],
 90:[b'\x00\xf0\x10 @\x80\xf0\x00'],
 91:[b'\x00p@@@@p\x00'],
 92:[b'\x00\x80\x80@ \x10\x10\x00'],
 93:[b'\x00p\x10\x10\x10\x10p\x00'],
 94:[b'\x00 P\x00\x00\x00\x00\x00'],
 95:[b'\x00\x00\x00\x00\x00\x00\x00\xf0'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 8, 5

