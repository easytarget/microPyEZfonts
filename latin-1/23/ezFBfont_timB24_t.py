'''
    ezFBfont_timB24_t : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original timB24.bdf font file was sourced from the U8G2 project:
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
# Font: timB24 Char set: b' +-.0123456789:'
# Cmd: ['bdf2dict.py', 'bdf-sources/timB24.bdf', '../latin-1/t-char.set']
# Date: 2024-06-04 14:21:31

version = '0.33'
name = '-Adobe-Times-Bold-R-Normal--34-240-100-100-P-177-ISO10646-1'
family = 'Times'
weight = 'Bold'
size = 34

def height():
    return 23

def baseline():
    return 23

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',8],
 43:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00?\xff\x80?\xff\x80?\xff\x80\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00',19],
 45:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x7f\x80\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',11],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008|||8',8],
 48:[b'\x03\xc0\x0f\xf0\x0ep\x1c8<8<<<<|>|>|>|>|>|>|>|>|><<<<<<\x1c8\x0ep\x07\xe0\x03\xc0',16],
 49:[b'\x00\xc0\x03\xc0\x0f\xc0\x7f\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x07\xc0\x0f\xe0\x7f\xfc',16],
 50:[b'\x03\xc0\x0f\xf0\x1f\xf8?\xf80\xfc`|@|\x00|\x00x\x00x\x00x\x00\xf0\x00\xe0\x01\xc0\x01\x80\x03\x00\x07\x01\x0e\x03\x1c\x06?\xfe\x7f\xfe\xff\xfc\xff\xfc',16],
 51:[b'\x03\xe0\x0f\xf8\x1f\xf8\x18|0< <\x00<\x008\x00`\x01\xf0\x07\xf8\x07\xfc\x01\xfc\x00~\x00>\x00\x1e\x00\x1e\x00\x1e0\x1cx\x1c|8?\xe0\x0f\x80',16],
 52:[b'\x008\x00x\x00x\x00\xf8\x01\xf8\x03x\x03x\x06x\x0cx\x0cx\x18x0x0x`x\x7f\xfe\x7f\xfe\x7f\xfe\x7f\xfe\x00x\x00x\x00x\x00x\x00x',16],
 53:[b'\x0f\xfc\x0f\xfc\x0f\xfc\x0f\xfc\x18\x00\x18\x00\x10\x00\x1f\x00?\xc0?\xf0?\xf8?\xf8\x01\xfc\x00|\x00<\x00\x1c\x00\x1c\x00\x1c0\x18x\x18|0?\xe0\x0f\x80',16],
 54:[b'\x00\x0e\x00x\x01\xe0\x03\xc0\x07\x80\x0f\x00\x1f\x00\x1e\x00>\x00?\xf0~\xf8|||<|>|>|>|><><<<<\x1c8\x0ep\x07\xe0',16],
 55:[b'?\xfc?\xfc\x7f\xfc\x7f\xfc`\x18@8@8\x000\x00p\x00p\x00`\x00\xe0\x00\xe0\x01\xc0\x01\xc0\x01\xc0\x03\x80\x03\x80\x03\x80\x07\x00\x07\x00\x07\x00\x0e\x00',16],
 56:[b'\x07\xf0\x1fx\x1e<<<<\x1c<\x1c>\x1c?8\x1f\xf0\x1f\xc0\x0f\xe0\x07\xf0\x1f\xf88\xfc8~p>p\x1ep\x1ep\x1ex\x1c<<?\xf8\x0f\xe0',16],
 57:[b'\x07\xe0\x0ep\x1c8<<<<|<|>|>|>|><>>>\x1f~\x0f\xfc\x00|\x00x\x00\xf8\x00\xf0\x01\xe0\x03\xc0\x07\x80\x1e\x00p\x00',16],
 58:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x1f\x00\x1f\x00\x1f\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x1f\x00\x1f\x00\x1f\x00\x0e\x00',11],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), _g[c][1]
