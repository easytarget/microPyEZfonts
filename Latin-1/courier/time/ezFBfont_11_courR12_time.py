'''
    ezFBfont_11_courR12_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original courR12.bdf font file was sourced from the U8G2 project:
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
# Font: courR12
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/courR12.bdf', './time-char.set', 'True']
# Date: 2024-06-11 17:33:55

version = '0.33'
name = '-Adobe-Courier-Medium-R-Normal--17-120-100-100-M-100-ISO10646-1'
family = 'courier'
weight = 'medium'
size = 17

def height():
    return 11

def baseline():
    return 11

def max_width():
    return 10

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 58

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 43:[b'\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00\x08\x00'],
 45:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00'],
 48:[b'\x1c\x00"\x00"\x00A\x00A\x00A\x00A\x00A\x00"\x00"\x00\x1c\x00'],
 49:[b'\x08\x00\x18\x00h\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x7f\x00'],
 50:[b'\x1c\x00"\x00A\x00\x01\x00\x01\x00\x02\x00\x04\x00\x08\x00\x10\x00!\x00\x7f\x00'],
 51:[b'\x1c\x00"\x00A\x00\x02\x00\x0c\x00\x02\x00\x01\x00\x01\x00A\x00"\x00\x1c\x00'],
 52:[b'\x06\x00\x06\x00\n\x00\x12\x00\x12\x00"\x00B\x00\x7f\x00\x02\x00\x02\x00\x0f\x00'],
 53:[b'?\x00 \x00 \x00 \x00<\x00"\x00\x01\x00\x01\x00A\x00"\x00\x1c\x00'],
 54:[b'\x0e\x000\x00 \x00@\x00\\\x00b\x00A\x00A\x00A\x00"\x00\x1c\x00'],
 55:[b'?\x00!\x00\x01\x00\x02\x00\x02\x00\x02\x00\x04\x00\x04\x00\x04\x00\x08\x00\x08\x00'],
 56:[b'\x0c\x00\x12\x00!\x00!\x00\x1e\x00\x12\x00!\x00!\x00!\x00\x12\x00\x0c\x00'],
 57:[b'\x1c\x00"\x00A\x00A\x00#\x00\x1d\x00\x01\x00\x01\x00\x02\x00\x06\x008\x00'],
 58:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 11, 10

