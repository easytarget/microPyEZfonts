'''
    ezFBfont_11_timR12_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original timR12.bdf font file was sourced from the U8G2 project:
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
# Font: timR12
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/timR12.bdf', './time-char.set', 'True']
# Date: 2024-06-11 17:35:28

version = '0.33'
name = '-Adobe-Times-Medium-R-Normal--17-120-100-100-P-84-ISO10646-1'
family = 'times'
weight = 'medium'
size = 17

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'4'],
 43:[b'\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00\x00\x00',b'9'],
 45:[b'\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x00',b'5'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00@@',b'4'],
 48:[b'8DD\x82\x82\x82\x82\x82DD8',b'8'],
 49:[b'\x08\x18(\x08\x08\x08\x08\x08\x08\x08\x1c',b'8'],
 50:[b'8D\x82\x02\x02\x04\x08\x10 B\xfc',b'8'],
 51:[b'8D\x84\x08\x108\x04\x02\x02\xc4x',b'8'],
 52:[b'\x02\x06\n\n\x12""B\xff\x02\x02',b'8'],
 53:[b'>  @x\x04\x02\x02\x02\x8cp',b'8'],
 54:[b'\x0e0@@\x98\xe4\x82\x82\x82D8',b'8'],
 55:[b'\xfe\x82\x84\x04\x08\x08\x10\x10\x10  ',b'8'],
 56:[b'\x18$BB$\x18$BB$\x18',b'8'],
 57:[b'8D\x82\x82\x82F:\x04\x04\x18\xe0',b'8'],
 58:[b'\x00\x00\x00@@\x00\x00\x00\x00@@',b'4'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 11, int(_g[c][1])

