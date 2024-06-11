'''
    ezFBfont_11_helvB10_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original helvB10.bdf font file was sourced from the U8G2 project:
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
# Font: helvB10
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/helvB10.bdf', './time-char.set', 'True']
# Date: 2024-06-11 17:34:08

version = '0.33'
name = '-Adobe-Helvetica-Bold-R-Normal--14-100-100-100-P-82-ISO10646-1'
family = 'helvetica'
weight = 'bold'
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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'4'],
 43:[b'\x00\x00\x00\x00\x00\x00\x18\x00\x18\x00\x18\x00\xff\x00\x18\x00\x18\x00\x18\x00\x00\x00',b'9'],
 45:[b'\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x00',b'4'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00``',b'4'],
 48:[b'8l\xc6\xc6\xc6\xc6\xc6\xc6\xc6l8',b'8'],
 49:[b'\x0c<\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c',b'8'],
 50:[b'|\xc6\xc6\x06\x0e\x0c\x180`\xc0\xfe',b'8'],
 51:[b'|\xc6\xc6\x06\x06<\x06\x06\xc6\xc6|',b'8'],
 52:[b'\x06\x0e\x1e6f\xc6\xc6\xff\x06\x06\x06',b'8'],
 53:[b'~``\xc0\xfc\x0e\x06\x06\xc6\xccx',b'8'],
 54:[b'<ff\xc0\xdc\xe6\xc6\xc6\xc6\xc6|',b'8'],
 55:[b'\xfe\x06\x0c\x0c\x18\x1800```',b'8'],
 56:[b'|\xc6\xc6\xc6\xc6|\xc6\xc6\xc6\xc6|',b'8'],
 57:[b'|\xc6\xc6\xc6\xc6\xc6~\x06\xc6\xccx',b'8'],
 58:[b'\x00\x00\x00``\x00\x00\x00\x00``',b'5'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 11, int(_g[c][1])
