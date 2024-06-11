'''
    ezFBfont_09_symb08_base : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original symb08.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Copyright (c) 1984, 1987 Adobe Systems Incorporated. All Rights Reserved. Copyright (c) 1988, 1991 Digital Equipment Corporation. All Rights Reserved."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
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
# Font: symb08
# Cmd: [bdf2dict.py], ['Symbols-bdf-sources/symb08.bdf', './base-char.set', 'True']
# Date: 2024-06-11 17:21:48

version = '0.33'
name = '-Adobe-Symbol-Medium-R-Normal--11-80-100-100-P-61-Adobe-FontSpecific'
family = 'symbol'
weight = 'medium'
size = 11

def height():
    return 9

def baseline():
    return 7

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
    return 63

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'3'],
 33:[b'@@@@@\x00@\x00\x00',b'3'],
 34:[b'\x82D|((\x10\x10\x00\x00',b'7'],
 35:[b'PP\xf8P\xf8PP\x00\x00',b'5'],
 36:[b'\xf8\x08\x08x\x08\x08\xf8\x00\x00',b'6'],
 37:[b'd\xbc\xa8V**D\x00\x00',b'8'],
 38:[b' PPl\x98\x98l\x00\x00',b'7'],
 39:[b'\x00\x00\xe0\x10p\x10\xe0\x00\x00',b'5'],
 40:[b' @@\x80\x80\x80@@ ',b'4'],
 41:[b'\x80@@   @@\x80',b'4'],
 42:[b'\x00\x00P P\x00\x00\x00\x00',b'5'],
 43:[b'\x00\x00  \xf8  \x00\x00',b'6'],
 44:[b'\x00\x00\x00\x00\x00\x00@@\x80',b'2'],
 45:[b'\x00\x00\x00\x00\xf8\x00\x00\x00\x00',b'6'],
 46:[b'\x00\x00\x00\x00\x00\x00\x80\x00\x00',b'2'],
 47:[b'  @@@\x80\x80\x00\x00',b'3'],
 48:[b'`\x90\x90\x90\x90\x90`\x00\x00',b'5'],
 49:[b' `    p\x00\x00',b'5'],
 50:[b'`\x90\x10  @\xf0\x00\x00',b'5'],
 51:[b'`\x90\x10`\x10\x10\xe0\x00\x00',b'5'],
 52:[b'\x100P\x90\xf8\x10\x10\x00\x00',b'5'],
 53:[b'p@\xe0\x10\x10\x10\xe0\x00\x00',b'5'],
 54:[b'p\x80\xe0\x90\x90\x90`\x00\x00',b'5'],
 55:[b'\xf0\x90  @@@\x00\x00',b'5'],
 56:[b'`\x90\x90`\x90\x90`\x00\x00',b'5'],
 57:[b'`\x90\x90\x90p \xc0\x00\x00',b'5'],
 58:[b'\x00\x00\x80\x00\x00\x00\x80\x00\x00',b'2'],
 59:[b'\x00\x00@\x00\x00\x00@@\x80',b'2'],
 60:[b'\x00\x00\x0c0\xc00\x0c\x00\x00',b'7'],
 61:[b'\x00\x00\x00\xf8\x00\xf8\x00\x00\x00',b'6'],
 62:[b'\x00\x00\xc00\x0c0\xc0\x00\x00',b'6'],
 63:[b' P\x10  \x00 \x00\x00',b'5'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 9, int(_g[c][1])

