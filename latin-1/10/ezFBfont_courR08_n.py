'''
    ezFBfont_courR08_n : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original courR08.bdf font file was sourced from the U8G2 project:
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
# Font: courR08 Char set: b' %()*+,-./0123456789:\xb0'
# Cmd: ['bdf2dict.py', 'bdf-sources/courR08.bdf', '../latin-1/n-char.set']
# Date: 2024-06-04 14:20:52

version = '0.33'
name = '-Adobe-Courier-Medium-R-Normal--11-80-100-100-M-60-ISO10646-1'
family = 'Courier'
weight = 'Medium'
size = 11

def height():
    return 10

def baseline():
    return 8

def max_width():
    return 6

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 176

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 37:[b'\x00\xe0\xa4\xc80\\\x94\x18\x00\x00'],
 40:[b'\x00\x10  @@@  \x10'],
 41:[b'\x00@  \x10\x10\x10  @'],
 42:[b'\x00 \xd8 P\x00\x00\x00\x00\x00'],
 43:[b'\x00\x00  \xf8  \x00\x00\x00'],
 44:[b'\x00\x00\x00\x00\x00\x00\x00\x10\x10 '],
 45:[b'\x00\x00\x00\x00x\x00\x00\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00\x00  \x00\x00'],
 47:[b'\x04\x08\x10\x10  @@\x80\x00'],
 48:[b'\x000HHHHH0\x00\x00'],
 49:[b'\x00\x10p\x10\x10\x10\x10x\x00\x00'],
 50:[b'\x000H\x08\x10 @x\x00\x00'],
 51:[b'\x000H\x080\x08H0\x00\x00'],
 52:[b'\x00\x100P\x90\xf8\x10\x10\x00\x00'],
 53:[b'\x00x@@p\x08\x08p\x00\x00'],
 54:[b'\x008@@pHH0\x00\x00'],
 55:[b'\x00xH\x08\x10\x10  \x00\x00'],
 56:[b'\x000HH0HH0\x00\x00'],
 57:[b'\x000HH8\x08\x08p\x00\x00'],
 58:[b'\x00\x00\x00  \x00  \x00\x00'],
 176:[b'\x000H0\x00\x00\x00\x00\x00\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()

