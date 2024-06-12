'''
    ezFBfont_10_6x13B_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 6x13B.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Public domain font.  Share and enjoy."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: 6x13B
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/6x13B.bdf', '_', './time-char.set']
# Date: 2024-06-12 20:06:45

version = '0.33'
name = '-Misc-Fixed-Bold-R-SemiCondensed--13-120-75-75-C-60-ISO10646-1'
family = 'fixed'
weight = 'bold'
size = 13

def height():
    return 10

def baseline():
    return 9

def max_width():
    return 6

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 58

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 43:[b'\x00\x0000\xfc00\x00\x00\x00'],
 45:[b'\x00\x00\x00\x00\xfc\x00\x00\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00\x00\x000x0'],
 48:[b'0x\xcc\xcc\xcc\xcc\xccx0\x00'],
 49:[b'0p\xf000000\xfc\x00'],
 50:[b'x\xcc\xcc\x0c\x180`\xc0\xfc\x00'],
 51:[b'\xfc\x0c\x180x\x0c\x0c\xccx\x00'],
 52:[b'\x18\x188xX\xd8\xfc\x18\x18\x00'],
 53:[b'\xfc\xc0\xc0\xf8\xec\x0c\x0c\xccx\x00'],
 54:[b'8`\xc0\xc0\xf8\xec\xcc\xccx\x00'],
 55:[b'\xfc\x0c\x18\x1800```\x00'],
 56:[b'x\xcc\xcc\xccx\xcc\xcc\xccx\x00'],
 57:[b'x\xcc\xcc\xdc|\x0c\x0c\x18p\x00'],
 58:[b'\x000x0\x00\x000x0\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 10, 6

