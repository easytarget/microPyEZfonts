'''
    ezFBfont_08_m2icon_7_lower : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original m2icon_7.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "public domain"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    COMMENT
    COMMENT  This font is copyrighted by its author, who reserves all rights under
    COMMENT  national and international copyright laws.
    COMMENT
    COMMENT  Produced with bdfedit, a tcl/tk font editing program
    COMMENT    written by Thomas A. Fine
    COMMENT    Email to my last name at head.cfa.harvard.edu
    COMMENT    http://hea-www.harvard.edu/~fine/
'''
# Code generated by bdf2dict.py
# Font: m2icon_7
# Cmd: [bdf2dict.py], ['Symbols-bdf-sources/m2icon_7.bdf', '_', './lower-char.set']
# Date: 2024-06-13 11:38:09

version = '0.33'
name = 'm2icon_7'
family = ''
weight = 'medium'
size = None

def height():
    return 8

def baseline():
    return 7

def max_width():
    return 13

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 65

def max_ch():
    return 104

_g = {
 65:[b'\x0f\x00\xff\x80\x80\x80\x80\x80\x80\x80\x80\x80\xff\x80\x00\x00',b'10'],
 66:[b'8h\xe8\x88\x88\x88\xf8\x00',b'6'],
 67:[b'\x00\x00\xd8pp\xd8\x00\x00',b'6'],
 68:[b'\x00\x00\x03\x00\x06\x00\x0c\x00\xd8\x00p\x00 \x00\x00\x00',b'9'],
 69:[b'\x00\xfc\x84\x84\x84\x84\xfc\x00',b'7'],
 70:[b'\x00\xfc\x84\xb4\xb4\x84\xfc\x00',b'7'],
 71:[b'\x00\xfc\xfc\xfc\xfc\xfc\xfc\x00',b'7'],
 72:[b'\xfe\x00\x82\x00\x82\x00\x82\x00\x82\x00\x82\x00\xfe\x00\x00\x00',b'9'],
 73:[b'\xfe\x00\x82\x00\xba\x00\xba\x00\xba\x00\x82\x00\xfe\x00\x00\x00',b'9'],
 74:[b'\xfe\x00\xfe\x00\xfe\x00\xfe\x00\xfe\x00\xfe\x00\xfe\x00\x00\x00',b'9'],
 75:[b'\x00\xf8\x8c\x8c\x8c\xfc|\x00',b'7'],
 76:[b'\x00\xf8\x8c\xac\x8c\xfc|\x00',b'7'],
 77:[b'\x00\xf8\xfc\xfc\xfc\xfc|\x00',b'8'],
 78:[b'\xfc\x00\x86\x00\x86\x00\x86\x00\x86\x00\xfe\x00~\x00\x00\x00',b'9'],
 79:[b'\xfc\x00\x86\x00\xb6\x00\xb6\x00\x86\x00\xfe\x00~\x00\x00\x00',b'9'],
 80:[b'\xfc\x00\xfe\x00\xfe\x00\xfe\x00\xfe\x00\xfe\x00~\x00\x00\x00',b'9'],
 81:[b'\x00x\xcc\x84\x84\xccx\x00',b'7'],
 82:[b'\x00x\xcc\xb4\xb4\xccx\x00',b'7'],
 83:[b'\x00x\xfc\xfc\xfc\xfcx\x00',b'7'],
 97:[b'\x10\x000\x00_\x00\x81\x00_\x000\x00\x10\x00\x00\x00',b'9'],
 98:[b'\x10(D\xee((8\x00',b'8'],
 102:[b'\x0f\x00\xff\x80\x80\x80\x9f\xf0\xa0 \xc0@\xff\x80\x00\x00',b'13'],
 103:[b'\x80\x80\x80\x80\x80\x80\x80\x80',b'2'],
 104:[b'\x10\x00\x00\x00\x10\x00\xba\x00\x10\x00\x00\x00\x10\x00\x00\x00',b'12'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 8, int(_g[c][1])

