'''
    ezFBfont_tom_thumb_n : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original tom-thumb.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT """""MIT"""""

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: tom-thumb Char set: b' %()*+,-./0123456789:\xb0'
# Cmd: ['bdf2dict.py', 'bdf-sources/tom-thumb.bdf', '../latin-1/n-char.set']
# Date: 2024-06-04 14:21:35

version = '0.33'
name = '-Raccoon-Fixed4x6-Medium-R-Normal--6-60-75-75-P-40-ISO10646-1'
family = 'Fixed4x6'
weight = 'Medium'
size = 6

def height():
    return 5

def baseline():
    return 5

def max_width():
    return 4

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
 32:[b'\x00\x00\x00\x00\x00'],
 37:[b'\x80 @\x80 '],
 40:[b' @@@ '],
 41:[b'\x80@@@\x80'],
 42:[b'\xa0@\xa0\x00\x00'],
 43:[b'\x00@\xe0@\x00'],
 44:[b'\x00\x00\x00@\x80'],
 45:[b'\x00\x00\xe0\x00\x00'],
 46:[b'\x00\x00\x00\x00@'],
 47:[b'  @\x80\x80'],
 48:[b'`\xa0\xa0\xa0\xc0'],
 49:[b'@\xc0@@@'],
 50:[b'\xc0 @\x80\xe0'],
 51:[b'\xc0 @ \xc0'],
 52:[b'\xa0\xa0\xe0  '],
 53:[b'\xe0\x80\xc0 \xc0'],
 54:[b'`\x80\xe0\xa0\xe0'],
 55:[b'\xe0 @\x80\x80'],
 56:[b'\xe0\xa0\xe0\xa0\xe0'],
 57:[b'\xe0\xa0\xe0 \xc0'],
 58:[b'\x00@\x00@\x00'],
 176:[b'@\xa0@\x00\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()

