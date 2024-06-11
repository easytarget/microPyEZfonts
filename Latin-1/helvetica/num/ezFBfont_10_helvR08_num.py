'''
    ezFBfont_10_helvR08_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original helvR08.bdf font file was sourced from the U8G2 project:
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
# Font: helvR08
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/helvR08.bdf', './num-char.set', 'True']
# Date: 2024-06-11 17:34:19

version = '0.33'
name = '-Adobe-Helvetica-Medium-R-Normal--11-80-100-100-P-56-ISO10646-1'
family = 'helvetica'
weight = 'medium'
size = 11

def height():
    return 10

def baseline():
    return 8

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
    return 176

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'3'],
 37:[b'd\x00\x94\x00h\x00\x08\x00\x10\x00\x16\x00)\x00&\x00\x00\x00\x00\x00',b'9'],
 40:[b' @@\x80\x80\x80\x80@@ ',b'4'],
 41:[b'\x80@@    @@\x80',b'4'],
 42:[b'\xa0@\xa0\x00\x00\x00\x00\x00\x00\x00',b'4'],
 43:[b'\x00\x00  \xf8  \x00\x00\x00',b'6'],
 44:[b'\x00\x00\x00\x00\x00\x00\x00@@\x80',b'3'],
 45:[b'\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x00',b'4'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00@\x00\x00',b'3'],
 47:[b'  @@@@\x80\x80\x00\x00',b'3'],
 48:[b'p\x88\x88\x88\x88\x88\x88p\x00\x00',b'6'],
 49:[b'\x100\x10\x10\x10\x10\x10\x10\x00\x00',b'6'],
 50:[b'p\x88\x08\x080@\x80\xf8\x00\x00',b'6'],
 51:[b'p\x88\x080\x08\x08\x88p\x00\x00',b'6'],
 52:[b'\x100PP\x90\xf8\x10\x10\x00\x00',b'6'],
 53:[b'x@@p\x08\x08\x88p\x00\x00',b'6'],
 54:[b'p\x88\x80\xf0\x88\x88\x88p\x00\x00',b'6'],
 55:[b'\xf8\x08\x10  @@@\x00\x00',b'6'],
 56:[b'p\x88\x88p\x88\x88\x88p\x00\x00',b'6'],
 57:[b'p\x88\x88\x88x\x08\x88p\x00\x00',b'6'],
 58:[b'\x00\x00@\x00\x00\x00\x00@\x00\x00',b'3'],
 176:[b'`\x90\x90`\x00\x00\x00\x00\x00\x00',b'4'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 10, int(_g[c][1])

