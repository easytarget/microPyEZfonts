'''
    ezFBfont_b10_b_n : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original b10_b.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "(c) Copyright 2000-2003 /efont/ The Electronic Font Open Laboratory."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: b10_b Char set: b' %()*+,-./0123456789:\xb0'
# Cmd: ['bdf2dict.py', 'bdf-sources/b10_b.bdf', '../latin-1/n-char.set']
# Date: 2024-06-04 14:20:01

version = '0.33'
name = '-Efont-Biwidth-Bold-R-Normal--10-100-75-75-P-50-ISO10646-1'
family = 'Biwidth'
weight = 'Bold'
size = 10

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
 37:[b'\xc0\xd0`\xd00\x00\x00'],
 40:[b'`\xc0\xc0\xc0\xc0`\x00'],
 41:[b'\xc0````\xc0\x00'],
 42:[b'\x00\xb0\xe0\xf0\xe0\xb0\x00'],
 43:[b'\x00``\xf8``\x00'],
 44:[b'\x00\x00\x00\x00p`\xc0'],
 45:[b'\x00\x00\x00\xf0\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00`\xf0`'],
 47:[b'00`\xc0\x80\x80\x00'],
 48:[b'`\xd0\xd0\xd0\xd0`\x00'],
 49:[b'`\xe0```\xf0\x00'],
 50:[b'\xe0\xb00\xe0\x80\xf0\x00'],
 51:[b'\xf0`\xe00\xb0\xe0\x00'],
 52:[b'`\xe0\xa0\xf0``\x00'],
 53:[b'\xf0\x80\xe00\xb0\xe0\x00'],
 54:[b'\xe0\x80\xe0\xb0\xb0\xe0\x00'],
 55:[b'\xf00``\xc0\xc0\x00'],
 56:[b'\xe0\xb0\xe0\xb0\xb0\xe0\x00'],
 57:[b'\xe0\xb0\xb0\xf00\xe0\x00'],
 58:[b'\x00\xe0\xe0\x00\xe0\xe0\x00'],
 176:[b'`\xd0`\x00\x00\x00\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()

