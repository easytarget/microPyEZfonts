'''
    ezFBfont_13_7x14B_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 7x14B.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Public domain font.  Share and enjoy."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: 7x14B
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/7x14B.bdf', './num-char.set', 'True']
# Date: 2024-06-11 17:33:07

version = '0.33'
name = '-Misc-Fixed-Bold-R-Normal--14-130-75-75-C-70-ISO10646-1'
family = 'fixed'
weight = 'bold'
size = 14

def height():
    return 13

def baseline():
    return 11

def max_width():
    return 7

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 176

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 37:[b'\x00l\xdc\xd8p\x10 8l\xec\xd8\x00\x00'],
 40:[b'\x0c\x1800`````00\x18\x0c'],
 41:[b'`0\x18\x18\x0c\x0c\x0c\x0c\x0c\x18\x180`'],
 42:[b'\x00\xb4\xb4x0x\xb4\xb4\x00\x00\x00\x00\x00'],
 43:[b'\x00\x00\x00000\xfc000\x00\x00\x00'],
 44:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x008\x18\x180'],
 45:[b'\x00\x00\x00\x00\x00\x00\xfc\x00\x00\x00\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x0000\x00\x00'],
 47:[b'\x0c\x0c\x0c\x18\x18000``\xc0\xc0\xc0'],
 48:[b'\x00x\xcc\xcc\xcc\xcc\xcc\xcc\xcc\xccx\x00\x00'],
 49:[b'\x000p\xf0000000\xfc\x00\x00'],
 50:[b'\x00x\xcc\xcc\x0c\x18\x180`\xc0\xfc\x00\x00'],
 51:[b'\x00x\xcc\xcc\x0c8\x0c\x0c\xcc\xccx\x00\x00'],
 52:[b'\x00\x08\x18\x188x\xd8\xd8\xfc\x18\x18\x00\x00'],
 53:[b'\x00\xfc\xc0\xc0\xf8\xcc\x0c\x0c\xcc\xccx\x00\x00'],
 54:[b'\x008l\xcc\xc0\xf8\xcc\xcc\xcc\xccx\x00\x00'],
 55:[b'\x00\xfc\xcc\xd8\x18000000\x00\x00'],
 56:[b'\x00x\xcc\xcc\xccxx\xcc\xcc\xccx\x00\x00'],
 57:[b'\x00x\xcc\xcc\xcc\xcc|\x0c\xcc\xd8p\x00\x00'],
 58:[b'\x00\x00\x0000\x00\x00\x0000\x00\x00\x00'],
 176:[b'8ll8\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 13, 7

