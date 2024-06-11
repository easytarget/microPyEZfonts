'''
    ezFBfont_10_7x13_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 7x13.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Public domain font.  Share and enjoy."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: 7x13
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/7x13.bdf', './num-char.set', 'True']
# Date: 2024-06-11 17:32:54

version = '0.33'
name = '-Misc-Fixed-Medium-R-Normal--13-120-75-75-C-70-ISO10646-1'
family = 'fixed'
weight = 'medium'
size = 13

def height():
    return 10

def baseline():
    return 9

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 37:[b'D\xa4H\x10\x10 H\x94\x88\x00'],
 40:[b'\x08\x10\x10   \x10\x10\x08\x00'],
 41:[b' \x10\x10\x08\x08\x08\x10\x10 \x00'],
 42:[b'\x00\x00H0\xfc0H\x00\x00\x00'],
 43:[b'\x00\x00\x10\x10|\x10\x10\x00\x00\x00'],
 44:[b'\x00\x00\x00\x00\x00\x00\x0080@'],
 45:[b'\x00\x00\x00\x00|\x00\x00\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x108\x10'],
 47:[b'\x04\x04\x08\x08\x10  @@\x00'],
 48:[b'0H\x84\x84\x84\x84\x84H0\x00'],
 49:[b'\x100P\x10\x10\x10\x10\x10|\x00'],
 50:[b'x\x84\x84\x04\x080@\x80\xfc\x00'],
 51:[b'\xfc\x04\x08\x108\x04\x04\x84x\x00'],
 52:[b'\x08\x18(H\x88\x88\xfc\x08\x08\x00'],
 53:[b'\xfc\x80\x80\xb8\xc4\x04\x04\x84x\x00'],
 54:[b'8@\x80\x80\xb8\xc4\x84\x84x\x00'],
 55:[b'\xfc\x04\x08\x10\x10  @@\x00'],
 56:[b'x\x84\x84\x84x\x84\x84\x84x\x00'],
 57:[b'x\x84\x84\x8ct\x04\x04\x08p\x00'],
 58:[b'\x00\x00\x108\x10\x00\x00\x108\x10'],
 176:[b'0HH0\x00\x00\x00\x00\x00\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 10, 7

