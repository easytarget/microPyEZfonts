'''
    ezFBfont_08_open_iconic_check_1x_lower : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_check_1x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: open_iconic_check_1x
# Cmd: [bdf2dict.py], ['Symbols-bdf-sources/open_iconic_check_1x.bdf', './lower-char.set', 'True']
# Date: 2024-06-11 17:21:08

version = '0.33'
name = '"open_iconic_check_1x"'
family = 'None'
weight = 'None'
size = None

def height():
    return 8

def baseline():
    return 8

def max_width():
    return 8

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 64

def max_ch():
    return 68

_g = {
 64:[b'\x00\x02\x07N\xfcx0\x00'],
 65:[b'<~\xfb\xf3\xc7\xff~<'],
 66:[b'<~\xdb\xe7\xe7\xdb~<'],
 67:[b'\xf8\x82\x84\x98\x82\x82\xfe\x00'],
 68:[b'B\xe7~<<~\xe7B'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 8, 8
