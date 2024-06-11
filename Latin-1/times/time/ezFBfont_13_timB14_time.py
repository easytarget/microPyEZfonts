'''
    ezFBfont_13_timB14_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original timB14.bdf font file was sourced from the U8G2 project:
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
# Font: timB14
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/timB14.bdf', './time-char.set', 'True']
# Date: 2024-06-11 17:35:17

version = '0.33'
name = '-Adobe-Times-Bold-R-Normal--20-140-100-100-P-100-ISO10646-1'
family = 'times'
weight = 'bold'
size = 20

def height():
    return 13

def baseline():
    return 13

def max_width():
    return 11

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'5'],
 43:[b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\xff\xc0\xff\xc0\x0c\x00\x0c\x00\x0c\x00\x0c\x00',b'11'],
 45:[b'\x00\x00\x00\x00\x00\x00\xf8\xf8\xf8\x00\x00\x00\x00',b'6'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ppp',b'5'],
 48:[b'<\x00f\x00g\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00f\x00f\x00<\x00',b'9'],
 49:[b'\x1c\x00<\x00\xfc\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x7f\x00',b'9'],
 50:[b'<\x00~\x00\xcf\x00\x87\x00\x07\x00\x07\x00\x06\x00\x0c\x00\x18\x001\x00c\x00\xff\x00\xff\x00',b'9'],
 51:[b'<\x00~\x00\x8f\x00\x07\x00\x0e\x00\x1c\x00>\x00\x0f\x00\x07\x80\x03\x80\xc3\x00\xe6\x00|\x00',b'9'],
 52:[b'\x0e\x00\x1e\x00\x1e\x00.\x00.\x00N\x00\xce\x00\x8e\x00\xff\x00\xff\x00\x0e\x00\x0e\x00\x0e\x00',b'9'],
 53:[b'?\x00?\x00>\x00@\x00x\x00~\x00?\x00\x07\x80\x03\x80\x03\x80\xc3\x00\xe6\x00\xfc\x00',b'9'],
 54:[b'\x07\x00\x1c\x008\x00p\x00`\x00\xfc\x00\xe6\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00f\x00<\x00',b'9'],
 55:[b'\xff\x00\xff\x00\xfe\x00\x86\x00\x0c\x00\x0c\x00\x0c\x00\x18\x00\x18\x008\x000\x000\x00p\x00',b'9'],
 56:[b'<\x00f\x00\xe3\x00\xe3\x00\xf6\x00|\x00<\x00~\x00\xcf\x00\xc7\x00\xc3\x00\xe7\x00~\x00',b'9'],
 57:[b'<\x00f\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00g\x00?\x00\x07\x00\x06\x00\x0e\x00<\x00\xf0\x00',b'9'],
 58:[b'\x00\x00\x00\x00ppp\x00\x00\x00ppp',b'5'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 13, int(_g[c][1])
