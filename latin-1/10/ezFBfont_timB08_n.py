'''
    ezFBfont_timB08_n : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original timB08.bdf font file was sourced from the U8G2 project:
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
    NOTICE "Times is a trademark of Linotype-Hell AG and/or its subsidiaries."
'''
# Code generated by bdf2dict.py
# Font: timB08 Char set: b' %()*+,-./0123456789:\xb0'
# Cmd: ['bdf2dict.py', 'bdf-sources/timB08.bdf', '../latin-1/n-char.set']
# Date: 2024-06-04 14:21:29

version = '0.33'
name = '-Adobe-Times-Bold-R-Normal--11-80-100-100-P-57-ISO10646-1'
family = 'Times'
weight = 'Bold'
size = 11

def height():
    return 10

def baseline():
    return 7

def max_width():
    return 9

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',2],
 37:[b';\x00n\x00t\x00\x08\x00\x17\x00-\x00N\x00\x00\x00\x00\x00\x00\x00',9],
 40:[b' `@\xc0\xc0\xc0\xc0@` ',3],
 41:[b'\x80\xc0@````@\xc0\x80',4],
 42:[b' \xf8p\xf8 \x00\x00\x00\x00\x00',6],
 43:[b'\x00\x00  \xf8  \x00\x00\x00',6],
 44:[b'\x00\x00\x00\x00\x00`` \x00\x00',4],
 45:[b'\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x00',3],
 46:[b'\x00\x00\x00\x00\x00\xc0\xc0\x00\x00\x00',3],
 47:[b'  `@\xc0\x80\x80\x00\x00\x00',3],
 48:[b'`\xd0\xd0\xd0\xd0\xd0`\x00\x00\x00',5],
 49:[b'`\xe0````\xf0\x00\x00\x00',5],
 50:[b'`\xf00 @\xf0\xf0\x00\x00\x00',5],
 51:[b'`\xb00`0\xb0\xe0\x00\x00\x00',5],
 52:[b'\x100P\x90\xf800\x00\x00\x00',5],
 53:[b'\xe0\xe0\x80\xe00\xb0\xe0\x00\x00\x00',5],
 54:[b'0`\xc0\xf0\xd0\xd0`\x00\x00\x00',5],
 55:[b'x\xf0\x900 ``\x00\x00\x00',5],
 56:[b'`\xd0\xd0`\xb0\xb0`\x00\x00\x00',5],
 57:[b'`\xb0\xb0\xb0p0\xe0\x00\x00\x00',5],
 58:[b'\x00\x00``\x00``\x00\x00\x00',4],
 176:[b'`\x90`\x00\x00\x00\x00\x00\x00\x00',4],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), _g[c][1]
