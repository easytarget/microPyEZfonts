'''
    ezFBfont_13_timB10_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original timB10.bdf font file was sourced from the U8G2 project:
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
# Font: timB10
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/timB10.bdf', './num-char.set', 'True']
# Date: 2024-06-11 17:35:14

version = '0.33'
name = '-Adobe-Times-Bold-R-Normal--14-100-100-100-P-76-ISO10646-1'
family = 'times'
weight = 'bold'
size = 14

def height():
    return 13

def baseline():
    return 10

def max_width():
    return 14

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'3'],
 37:[b'8\xc0g\xc0\xc5\x80\xc9\x00s\x00\x06p\x04\xc8\r\x88\x19\x90\x18\xe0\x00\x00\x00\x00\x00\x00',b'14'],
 40:[b'\x100 ``````` 0\x10',b'5'],
 41:[b'@` 0000000 `@',b'5'],
 42:[b'\x10T88T\x10\x00\x00\x00\x00\x00\x00\x00',b'7'],
 43:[b'\x00\x00\x00\x10\x10\x10\xfe\x10\x10\x10\x00\x00\x00',b'8'],
 44:[b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0@\x80\x00',b'3'],
 45:[b'\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x00',b'4'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\x00\x00\x00',b'3'],
 47:[b'\x10\x100 `@@\xc0\x80\x80\x00\x00\x00',b'4'],
 48:[b'xH\xcc\xcc\xcc\xcc\xcc\xccHx\x00\x00\x00',b'7'],
 49:[b'0\xf00000000\xfc\x00\x00\x00',b'7'],
 50:[b'8|\x8c\x0c\x0c\x180@\xfc\xfc\x00\x00\x00',b'7'],
 51:[b'8|\x8c\x0c8\x1c\x0c\xc4\xecx\x00\x00\x00',b'7'],
 52:[b'\x1888X\x98\x98\xfc\xfc\x18\x18\x00\x00\x00',b'7'],
 53:[b'||@x|\x0c\x04\xc4\xccx\x00\x00\x00',b'7'],
 54:[b'\x1c0`\xe0\xf8\xcc\xcc\xcc\xccx\x00\x00\x00',b'7'],
 55:[b'\xfc\xfc\x8c\x08\x18\x10\x10  `\x00\x00\x00',b'7'],
 56:[b'x\xcc\xcc\xecxx\xcc\xcc\xccx\x00\x00\x00',b'7'],
 57:[b'x\xcc\xcc\xcc\xcc|\x188p\xc0\x00\x00\x00',b'7'],
 58:[b'\x00\x00\x00``\x00\x00\x00``\x00\x00\x00',b'4'],
 176:[b'0HH0\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'6'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 13, int(_g[c][1])
