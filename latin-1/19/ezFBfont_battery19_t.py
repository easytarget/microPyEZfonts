'''
    ezFBfont_battery19_t : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original battery19.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Created with Fony 1.4.7"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    COMMENT Exported by Fony v1.4.7
'''
# Code generated by bdf2dict.py
# Font: battery19 Char set: b' +-.0123456789:'
# Cmd: ['bdf2dict.py', 'bdf-sources/battery19.bdf', '../latin-1/t-char.set']
# Date: 2024-06-04 14:20:49

version = '0.33'
name = 'battery19'
family = 'None'
weight = 'None'
size = None

def height():
    return 19

def baseline():
    return 19

def max_width():
    return 9

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 48

def max_ch():
    return 54

_g = {
 48:[b'<\x00\xff\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\xff\x00'],
 49:[b'<\x00\xff\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xff\x00'],
 50:[b'<\x00\xff\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xff\x00'],
 51:[b'<\x00\xff\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xff\x00'],
 52:[b'<\x00\xff\x00\x81\x00\x81\x00\x81\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xff\x00'],
 53:[b'<\x00\xff\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xff\x00'],
 54:[b'<\x00\xff\x00\x81\x00\x81\x00\x81\x00\x89\x00\x89\x00\x99\x00\x99\x00\xbd\x00\xbd\x00\x99\x00\x99\x00\x91\x00\x91\x00\x81\x00\x81\x00\x81\x00\xff\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()

