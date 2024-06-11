'''
    ezFBfont_11_timB12_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original timB12.bdf font file was sourced from the U8G2 project:
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
# Font: timB12
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/timB12.bdf', './time-char.set', 'True']
# Date: 2024-06-11 17:35:15

version = '0.33'
name = '-Adobe-Times-Bold-R-Normal--17-120-100-100-P-88-ISO10646-1'
family = 'times'
weight = 'bold'
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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'5'],
 43:[b'\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x7f\x00\x08\x00\x08\x00\x08\x00',b'9'],
 45:[b'\x00\x00\x00\x00\x00\x00\xf0\xf0\x00\x00\x00',b'5'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00``',b'4'],
 48:[b'\x18$fffffff$\x18',b'8'],
 49:[b'\x08x\x18\x18\x18\x18\x18\x18\x18\x18~',b'8'],
 50:[b'8|\x9c\x0c\x0c\x08\x18\x10"|\xfc',b'8'],
 51:[b'8|\x8c\x08\x10<\x0e\x06\xc6\xccx',b'8'],
 52:[b'\x04\x0c\x1c,,L\x8c\xfe\xfe\x0c\x0c',b'8'],
 53:[b'\x1f> 8|\x0e\x06\x06\xc6\xccp',b'8'],
 54:[b'\x06\x1800xffff$\x18',b'8'],
 55:[b'~~\x84\x04\x0c\x08\x08\x18\x100 ',b'8'],
 56:[b'8D\xc6\xe4x<N\xc6\xc6D8',b'8'],
 57:[b'\x18$ffff>\x0c\x0c\x18`',b'8'],
 58:[b'\x00\x00\x00\x00``\x00\x00\x00``',b'5'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 11, int(_g[c][1])

