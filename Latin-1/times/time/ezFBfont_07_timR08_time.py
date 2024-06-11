'''
    ezFBfont_07_timR08_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original timR08.bdf font file was sourced from the U8G2 project:
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
# Font: timR08
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/timR08.bdf', './time-char.set', 'True']
# Date: 2024-06-11 17:35:24

version = '0.33'
name = '-Adobe-Times-Medium-R-Normal--11-80-100-100-P-54-ISO10646-1'
family = 'times'
weight = 'medium'
size = 11

def height():
    return 7

def baseline():
    return 7

def max_width():
    return 6

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00',b'2'],
 43:[b'\x00\x00  \xf8  ',b'6'],
 45:[b'\x00\x00\x00\x00\xe0\x00\x00',b'4'],
 46:[b'\x00\x00\x00\x00\x00\x00@',b'3'],
 48:[b'`\x90\x90\x90\x90\x90`',b'5'],
 49:[b' `    p',b'5'],
 50:[b'`\x90\x10  @\xf0',b'5'],
 51:[b'`\x90\x10`\x10\x10\xe0',b'5'],
 52:[b'\x100P\x90\xf8\x10\x10',b'5'],
 53:[b'p@\xe0\x10\x10\x10\xe0',b'5'],
 54:[b'0@\xe0\x90\x90\x90`',b'5'],
 55:[b'\xf0\x90  @@@',b'5'],
 56:[b'`\x90\x90`\x90\x90`',b'5'],
 57:[b'`\x90\x90\x90p \xc0',b'5'],
 58:[b'\x00\x00@\x00\x00\x00@',b'3'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 7, int(_g[c][1])

