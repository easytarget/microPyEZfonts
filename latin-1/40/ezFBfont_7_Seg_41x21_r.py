'''
    ezFBfont_7_Seg_41x21_r : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 7_Seg_41x21.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Created with Fony 1.4.0.2"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    COMMENT Exported by Fony v1.4.0.2
'''
# Code generated by bdf2dict.py
# Font: 7_Seg_41x21 Char set: b' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
# Cmd: ['bdf2dict.py', 'bdf-sources/7_Seg_41x21.bdf', '../latin-1/r-char.set']
# Date: 2024-06-04 14:19:46

version = '0.33'
name = '7_Seg_41x21'
family = 'None'
weight = 'None'
size = None

def height():
    return 40

def baseline():
    return 1

def max_width():
    return 21

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 43

def max_ch():
    return 58

_g = {
 43:[b'',13],
 44:[b'',7],
 45:[b'',13],
 46:[b'',7],
 48:[b'',21],
 49:[b'',21],
 50:[b'',21],
 51:[b'',21],
 52:[b'',21],
 53:[b'',21],
 54:[b'',21],
 55:[b'',21],
 56:[b'',21],
 57:[b'',21],
 58:[b'',7],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), _g[c][1]

