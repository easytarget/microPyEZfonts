'''
    ezFBfont_07_5x8_num : generated as part of the microPyEZfonts repository
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
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/5x8.bdf', '_', './num-char.set']
# Date: 2024-06-12 20:06:29

version = '0.33'
name = '-Misc-Fixed-Medium-R-Normal--8-80-75-75-C-50-ISO10646-1'
family = 'fixed'
weight = 'medium'
size = 8

def height():
    return 7

def baseline():
    return 6

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
    return 176

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00'],
 37:[b'@P P\x10\x00\x00'],
 40:[b' @@@@ \x00'],
 41:[b'@    @\x00'],
 42:[b'\x00\x90`\xf0`\x90\x00'],
 43:[b'\x00  \xf8  \x00'],
 44:[b'\x00\x00\x00\x000 @'],
 45:[b'\x00\x00\x00\xf0\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00 p '],
 47:[b'\x10\x10 @\x80\x80\x00'],
 48:[b' PPPP \x00'],
 49:[b' `   p\x00'],
 50:[b'`\x90\x10`\x80\xf0\x00'],
 51:[b'\xf0 `\x10\x90`\x00'],
 52:[b' `\xa0\xf0  \x00'],
 53:[b'\xf0\x80\xe0\x10\x90`\x00'],
 54:[b'`\x80\xe0\x90\x90`\x00'],
 55:[b'\xf0\x10  @@\x00'],
 56:[b'`\x90`\x90\x90`\x00'],
 57:[b'`\x90\x90p\x10`\x00'],
 58:[b'\x00``\x00``\x00'],
 176:[b' P \x00\x00\x00\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 7, 5

