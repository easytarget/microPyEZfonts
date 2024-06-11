'''
    ezFBfont_11_6x13_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 6x13.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Public domain font.  Share and enjoy."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: 6x13
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/6x13.bdf', './num-char.set', 'True']
# Date: 2024-06-11 17:32:43

version = '0.33'
name = '-Misc-Fixed-Medium-R-SemiCondensed--13-120-75-75-C-60-ISO10646-1'
family = 'fixed'
weight = 'medium'
size = 13

def height():
    return 11

def baseline():
    return 10

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
    return 176

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 37:[b'\x00H\xa8P\x10 @P\xa8\x90\x00'],
 40:[b'\x10  @@@@@  \x10'],
 41:[b'@  \x10\x10\x10\x10\x10  @'],
 42:[b'\x00 \xa8p\xa8 \x00\x00\x00\x00\x00'],
 43:[b'\x00\x00\x00  \xf8  \x00\x00\x00'],
 44:[b'\x00\x00\x00\x00\x00\x00\x00\x000 @'],
 45:[b'\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00 p '],
 47:[b'\x00\x08\x08\x10\x10 @@\x80\x80\x00'],
 48:[b'\x00 P\x88\x88\x88\x88\x88P \x00'],
 49:[b'\x00 `\xa0     \xf8\x00'],
 50:[b'\x00p\x88\x88\x08\x10 @\x80\xf8\x00'],
 51:[b'\x00\xf8\x08\x10 p\x08\x08\x88p\x00'],
 52:[b'\x00\x10\x100PP\x90\xf8\x10\x10\x00'],
 53:[b'\x00\xf8\x80\x80\xb0\xc8\x08\x08\x88p\x00'],
 54:[b'\x00p\x88\x80\x80\xf0\x88\x88\x88p\x00'],
 55:[b'\x00\xf8\x08\x10\x10  @@@\x00'],
 56:[b'\x00p\x88\x88\x88p\x88\x88\x88p\x00'],
 57:[b'\x00p\x88\x88\x88x\x08\x08\x88p\x00'],
 58:[b'\x00\x00\x00 p \x00\x00 p '],
 176:[b'\x000HH0\x00\x00\x00\x00\x00\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 11, 6

