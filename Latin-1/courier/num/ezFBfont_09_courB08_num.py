'''
    ezFBfont_09_courB08_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original courB08.bdf font file was sourced from the U8G2 project:
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
    NOTICE "No mark"
'''
# Code generated by bdf2dict.py
# Font: courB08
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/courB08.bdf', './num-char.set', 'True']
# Date: 2024-06-11 17:33:39

version = '0.33'
name = '-Adobe-Courier-Bold-R-Normal--11-80-100-100-M-60-ISO10646-1'
family = 'courier'
weight = 'bold'
size = 11

def height():
    return 9

def baseline():
    return 7

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 37:[b'\xe0\xa8\xf0 x\xa88\x00\x00'],
 40:[b'\x10 ```` \x10\x00'],
 41:[b'@ 0000 @\x00'],
 42:[b'\x10x0H\x00\x00\x00\x00\x00'],
 43:[b'\x00  \xf8  \x00\x00\x00'],
 44:[b'\x00\x00\x00\x00\x00\x000 @'],
 45:[b'\x00\x00\x00\xf8\x00\x00\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00\x000\x00\x00'],
 47:[b'\x08\x08\x10\x10  @@\x00'],
 48:[b'p\xd8\xd8\xd8\xd8\xd8p\x00\x00'],
 49:[b'0\xf00000\xfc\x00\x00'],
 50:[b'p\xd8\x180`\xd8\xf8\x00\x00'],
 51:[b'p\xd8\x18p\x18\xd8p\x00\x00'],
 52:[b'\x188X\xd8\xfc\x18\x18\x00\x00'],
 53:[b'\xf8\xc0\xf0\xd8\x18\x98\xf0\x00\x00'],
 54:[b'p\xd8\xc0\xf0\xd8\xd8p\x00\x00'],
 55:[b'\xf8\xd8\x1800``\x00\x00'],
 56:[b'p\xd8\xd8p\xd8\xd8p\x00\x00'],
 57:[b'p\xd8\xd8x\x18\xd8p\x00\x00'],
 58:[b'\x00\x00\x000\x00\x000\x00\x00'],
 176:[b'0H0\x00\x00\x00\x00\x00\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 9, 6

