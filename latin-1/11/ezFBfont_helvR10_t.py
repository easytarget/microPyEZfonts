'''
    ezFBfont_helvR10_t : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original helvR10.bdf font file was sourced from the U8G2 project:
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
# Font: helvR10 Char set: b' +-.0123456789:'
# Cmd: ['bdf2dict.py', 'bdf-sources/helvR10.bdf', '../latin-1/t-char.set']
# Date: 2024-06-04 14:21:00

version = '0.33'
name = '-Adobe-Helvetica-Medium-R-Normal--14-100-100-100-P-76-ISO10646-1'
family = 'Helvetica'
weight = 'Medium'
size = 14

def height():
    return 11

def baseline():
    return 11

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
    return 58

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',4],
 43:[b'\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00\x00\x00',9],
 45:[b'\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x00',4],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00@@',3],
 48:[b'<BBBBBBBBB<',8],
 49:[b'\x088\x08\x08\x08\x08\x08\x08\x08\x08\x08',8],
 50:[b'<BB\x02\x04\x08\x10 @@~',8],
 51:[b'<BB\x02\x02\x1c\x02\x02BB<',8],
 52:[b'\x04\x0c\x14$D\x84\x84\xfe\x04\x04\x04',8],
 53:[b'~@@@|\x02\x02\x02BB<',8],
 54:[b'<B@@\\bBBBB<',8],
 55:[b'~\x02\x04\x04\x08\x08\x10\x10   ',8],
 56:[b'<BBBB<BBBB<',8],
 57:[b'<BBBB>\x02\x02BB<',8],
 58:[b'\x00\x00\x00@@\x00\x00\x00\x00@@',3],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), _g[c][1]
