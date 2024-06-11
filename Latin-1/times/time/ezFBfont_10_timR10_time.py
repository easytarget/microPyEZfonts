'''
    ezFBfont_10_timR10_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original timR10.bdf font file was sourced from the U8G2 project:
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
# Font: timR10
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/timR10.bdf', './time-char.set', 'True']
# Date: 2024-06-11 17:35:26

version = '0.33'
name = '-Adobe-Times-Medium-R-Normal--14-100-100-100-P-74-ISO10646-1'
family = 'times'
weight = 'medium'
size = 14

def height():
    return 10

def baseline():
    return 10

def max_width():
    return 8

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'3'],
 43:[b'\x00\x00\x00\x10\x10\x10\xfe\x10\x10\x10',b'8'],
 45:[b'\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00',b'4'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00`',b'4'],
 48:[b'x\xcc\x84\x84\x84\x84\x84\x84\xccx',b'7'],
 49:[b'\x10p\x10\x10\x10\x10\x10\x10\x10|',b'7'],
 50:[b'8lD\x04\x0c\x08\x10 D|',b'7'],
 51:[b'x\x8c\x04\x0808\x04\x04\xccx',b'7'],
 52:[b'\x08\x18\x18(hH\x88\xfc\x08\x08',b'7'],
 53:[b'< @p\x18\x0c\x04\x04Hp',b'7'],
 54:[b'\x0c\x10 @x\xcc\x84\x84\xccx',b'7'],
 55:[b'\xfc\x84\x08\x08\x10\x10  @@',b'7'],
 56:[b'8LDd8LDDD8',b'7'],
 57:[b'x\xcc\x84\x84\xccx\x08\x10 \xc0',b'7'],
 58:[b'\x00\x00\x00`\x00\x00\x00\x00\x00`',b'4'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 10, int(_g[c][1])

