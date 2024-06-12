'''
    ezFBfont_18_helvB14_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original helvB14.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Copyright (c) 1984, 1987 Adobe Systems Incorporated. All Rights Reserved. Copyright (c) 1988, 1991 Digital Equipment Corporation. All Rights Reserved."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    COMMENT ISO10646-1 extension by Markus Kuhn <mkuhn@acm.org>, 2001-03-20
    COMMENT 
    COMMENT +
    COMMENT  Copyright 1984-1989, 1994 Adobe Systems Incorporated.
    COMMENT  Copyright 1988, 1994 Digital Equipment Corporation.
    COMMENT
    COMMENT  Adobe is a trademark of Adobe Systems Incorporated which may be
    COMMENT  registered in certain jurisdictions.
    COMMENT  Permission to use these trademarks is hereby granted only in
    COMMENT  association with the images described in this file.
    COMMENT
    COMMENT  Permission to use, copy, modify, distribute and sell this software
    COMMENT  and its documentation for any purpose and without fee is hereby
    COMMENT  granted, provided that the above copyright notices appear in all
    COMMENT  copies and that both those copyright notices and this permission
    COMMENT  notice appear in supporting documentation, and that the names of
    COMMENT  Adobe Systems and Digital Equipment Corporation not be used in
    COMMENT  advertising or publicity pertaining to distribution of the software
    COMMENT  without specific, written prior permission.  Adobe Systems and
    COMMENT  Digital Equipment Corporation make no representations about the
    COMMENT  suitability of this software for any purpose.  It is provided "as
    COMMENT  is" without express or implied warranty.
    COMMENT -
    NOTICE "Helvetica is a trademark of Linotype-Hell AG and/or its subsidiaries.  "
'''
# Code generated by bdf2dict.py
# Font: helvB14
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/helvB14.bdf', '_', './num-char.set']
# Date: 2024-06-12 20:08:09

version = '0.33'
name = '-Adobe-Helvetica-Bold-R-Normal--20-140-100-100-P-105-ISO10646-1'
family = 'helvetica'
weight = 'bold'
size = 20

def height():
    return 18

def baseline():
    return 14

def max_width():
    return 16

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 176

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'5'],
 37:[b'\x00\x00x`\xfc`\xcc\xc0\xcc\x80\xfd\x80{\x00\x02\x00\x06\xf0\r\xf8\t\x98\x19\x981\xf80\xf0\x00\x00\x00\x00\x00\x00\x00\x00',b'16'],
 40:[b'\x1c80p`\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0`p08\x1c',b'7'],
 41:[b'\xe0p08\x18\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1880p\xe0',b'7'],
 42:[b'\x10\x00\xd6\x00|\x008\x00l\x00D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 43:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x18\x00\x18\x00\xff\x00\xff\x00\x18\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'11'],
 44:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0\xe0`\xc0\x80\x00',b'5'],
 45:[b'\x00\x00\x00\x00\x00\x00\x00\xf8\xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x00',b'6'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0\xe0\x00\x00\x00\x00',b'5'],
 47:[b'\x18\x18\x188000p``\xe0\xc0\xc0\xc0\x00\x00\x00\x00',b'5'],
 48:[b'\x00\x00\x1c\x00\x7f\x00w\x00\xe3\x80\xe3\x80\xe3\x80\xe3\x80\xe3\x80\xe3\x80\xe3\x80w\x00\x7f\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 49:[b'\x00\x00\x1c\x00<\x00\xfc\x00\xfc\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 50:[b'\x00\x00>\x00\x7f\x00\xe3\x80\xe3\x80\x03\x80\x07\x00\x1f\x00>\x00x\x00p\x00\xe0\x00\xff\x80\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 51:[b'\x00\x00>\x00\x7f\x00\xe7\x00\xe3\x00\x07\x00\x1e\x00\x1f\x00\x07\x80\x03\x80\xe3\x80\xe7\x80\x7f\x00>\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 52:[b'\x00\x00\x07\x00\x0f\x00\x1f\x00?\x007\x00w\x00g\x00\xe7\x00\xff\x80\xff\x80\x07\x00\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 53:[b'\x00\x00\xff\x00\xff\x00\xe0\x00\xe0\x00\xfe\x00\xff\x00\xe7\x80\x03\x80\x03\x80\xe3\x80\xe7\x80\xff\x00~\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 54:[b'\x00\x00?\x00\x7f\x80q\x80\xe0\x00\xee\x00\xff\x00\xf3\x80\xe1\x80\xe1\x80\xe1\x80\xf3\x80\x7f\x00>\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 55:[b'\x00\x00\xff\x80\xff\x80\x03\x80\x07\x00\x0e\x00\x0e\x00\x1c\x00\x1c\x008\x008\x00p\x00p\x00p\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 56:[b'\x00\x00>\x00\x7f\x00\xe3\x80\xe3\x80\xe3\x80\x7f\x00>\x00w\x00\xe3\x80\xe3\x80\xe3\x80\x7f\x00>\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 57:[b'\x00\x00>\x00\x7f\x00\xe7\x80\xc3\x80\xc3\x80\xc3\x80\xe7\x80\x7f\x80;\x80\x03\x80\xc7\x00\xff\x00~\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 58:[b'\x00\x00\x00\x00\xe0\xe0\xe0\x00\x00\x00\x00\xe0\xe0\xe0\x00\x00\x00\x00',b'6'],
 176:[b'\x00x\xfc\xcc\xcc\xfcx\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'7'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 18, int(_g[c][1])

