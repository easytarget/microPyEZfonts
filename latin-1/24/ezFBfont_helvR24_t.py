'''
    ezFBfont_helvR24_t : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original helvR24.bdf font file was sourced from the U8G2 project:
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
# Font: helvR24 Char set: b' +-.0123456789:'
# Cmd: ['bdf2dict.py', 'bdf-sources/helvR24.bdf', '../latin-1/t-char.set']
# Date: 2024-06-04 14:21:02

version = '0.33'
name = '-Adobe-Helvetica-Medium-R-Normal--34-240-100-100-P-176-ISO10646-1'
family = 'Helvetica'
weight = 'Medium'
size = 34

def height():
    return 24

def baseline():
    return 24

def max_width():
    return 19

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',9],
 43:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x7f\xff\xc0\x7f\xff\xc0\x7f\xff\xc0\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\x00\x00',19],
 45:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',11],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00',9],
 48:[b'\x03\xe0\x00\x0f\xf8\x00\x1f\xfc\x00\x1e<\x00<\x1e\x008\x0e\x008\x0e\x00p\x07\x00p\x07\x00p\x07\x00p\x07\x00p\x07\x00p\x07\x00p\x07\x00p\x07\x00p\x07\x00p\x07\x008\x0e\x008\x0e\x008\x1e\x00\x1e<\x00\x1f\xfc\x00\x0f\xf8\x00\x03\xe0\x00',18],
 49:[b'\x00\x18\x00\x008\x00\x008\x00\x00x\x00\x01\xf8\x00\x07\xf8\x00\x07\xf8\x00\x008\x00\x008\x00\x008\x00\x008\x00\x008\x00\x008\x00\x008\x00\x008\x00\x008\x00\x008\x00\x008\x00\x008\x00\x008\x00\x008\x00\x008\x00\x008\x00\x008\x00',18],
 50:[b'\x03\xe0\x00\x0f\xf8\x00\x1f\xfc\x00<\x1e\x008\x0e\x00x\x07\x00p\x07\x00p\x07\x00\x00\x07\x00\x00\x0e\x00\x00\x1e\x00\x00<\x00\x00x\x00\x01\xf0\x00\x03\xe0\x00\x0f\x80\x00\x1e\x00\x00<\x00\x008\x00\x00p\x00\x00p\x00\x00\x7f\xff\x00\x7f\xff\x00\x7f\xff\x00',18],
 51:[b'\x03\xe0\x00\x0f\xf8\x00\x1f\xfc\x00\x1c\x1c\x008\x0e\x008\x0e\x008\x0e\x008\x0e\x00\x00\x0e\x00\x00\x1c\x00\x01\xfc\x00\x01\xf8\x00\x01\xfc\x00\x00\x1e\x00\x00\x0f\x00\x00\x07\x00p\x07\x00p\x07\x00p\x07\x008\x0e\x00<\x1e\x00\x1f\xfc\x00\x0f\xf8\x00\x03\xe0\x00',18],
 52:[b'\x00\x0c\x00\x00\x1c\x00\x00<\x00\x00<\x00\x00|\x00\x00\xfc\x00\x01\xdc\x00\x01\xdc\x00\x03\x9c\x00\x07\x1c\x00\x07\x1c\x00\x0e\x1c\x00\x1c\x1c\x00\x1c\x1c\x008\x1c\x00p\x1c\x00\x7f\xff\x80\x7f\xff\x80\x7f\xff\x80\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00',18],
 53:[b'\x1f\xfe\x00\x1f\xfe\x00\x1f\xfe\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x008\x00\x008\x00\x00;\xe0\x00?\xf8\x00?\xfc\x00<>\x008\x0e\x00\x00\x0f\x00\x00\x07\x00\x00\x07\x00\x00\x07\x00p\x07\x00p\x0f\x00x\x0e\x00<>\x00?\xfc\x00\x1f\xf8\x00\x07\xc0\x00',18],
 54:[b'\x01\xe0\x00\x07\xf8\x00\x0f\xfc\x00\x1e\x1c\x00\x1c\x0e\x008\x0e\x008\x00\x008\x00\x000\x00\x00q\xe0\x00w\xf8\x00\x7f\xfc\x00|\x1e\x00x\x0e\x00x\x07\x00p\x07\x00p\x07\x000\x07\x008\x07\x008\x0e\x00\x1c\x1e\x00\x1f\xfc\x00\x0f\xf8\x00\x03\xe0\x00',18],
 55:[b'\x7f\xff\x00\x7f\xff\x00\x7f\xff\x00\x00\x07\x00\x00\x0e\x00\x00\x0c\x00\x00\x1c\x00\x008\x00\x008\x00\x00p\x00\x00p\x00\x00\xe0\x00\x00\xe0\x00\x01\xc0\x00\x01\xc0\x00\x03\x80\x00\x03\x80\x00\x03\x80\x00\x07\x00\x00\x07\x00\x00\x07\x00\x00\x0e\x00\x00\x0e\x00\x00\x0e\x00\x00',18],
 56:[b'\x03\xe0\x00\x0f\xf8\x00\x1f\xfc\x00\x1c\x1e\x008\x0e\x008\x0e\x008\x0e\x008\x0e\x00<\x1e\x00\x1e<\x00\x0f\xf8\x00\x07\xf0\x00\x1f\xfc\x00<\x1e\x008\x0e\x00p\x07\x00p\x07\x00p\x07\x00p\x07\x00x\x0e\x00<\x1e\x00\x1f\xfc\x00\x0f\xf8\x00\x03\xe0\x00',18],
 57:[b'\x03\xe0\x00\x0f\xf8\x00\x1f\xfc\x00<>\x008\x1e\x00x\x0e\x00p\x0f\x00p\x07\x00p\x07\x00p\x07\x00p\x0f\x00p\x0f\x008\x1f\x00?\xff\x00\x1f\xf7\x00\x07\xe7\x00\x00\x07\x00\x00\x0e\x00p\x0e\x00x\x1e\x00<<\x00\x1f\xf8\x00\x1f\xf0\x00\x07\xc0\x00',18],
 58:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00',9],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), _g[c][1]
