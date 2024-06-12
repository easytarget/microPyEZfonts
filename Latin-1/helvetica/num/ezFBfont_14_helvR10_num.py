'''
    ezFBfont_14_helvR10_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original helvR10.bdf font file was sourced from the U8G2 project:
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
# Font: helvR10
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/helvR10.bdf', '_', './num-char.set']
# Date: 2024-06-12 20:08:18

version = '0.33'
name = '-Adobe-Helvetica-Medium-R-Normal--14-100-100-100-P-76-ISO10646-1'
family = 'helvetica'
weight = 'medium'
size = 14

def height():
    return 14

def baseline():
    return 11

def max_width():
    return 12

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'4'],
 37:[b'p\x80\x89\x00\x89\x00r\x00\x02\x00\x04\x00\x08\x00\t\xc0\x12 \x12 !\xc0\x00\x00\x00\x00\x00\x00',b'12'],
 40:[b' @@\x80\x80\x80\x80\x80\x80\x80\x80@@ ',b'5'],
 41:[b'\x80@@        @@\x80',b'5'],
 42:[b' \xa8p\xa8 \x00\x00\x00\x00\x00\x00\x00\x00\x00',b'7'],
 43:[b'\x00\x00\x00\x00\x00\x00\x10\x00\x10\x00\x10\x00\xfe\x00\x10\x00\x10\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 44:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00@@@\x80\x00',b'3'],
 45:[b'\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00',b'4'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00',b'3'],
 47:[b'\x10\x10   @@@\x80\x80\x80\x00\x00\x00',b'4'],
 48:[b'x\x84\x84\x84\x84\x84\x84\x84\x84\x84x\x00\x00\x00',b'8'],
 49:[b' \xe0         \x00\x00\x00',b'8'],
 50:[b'x\x84\x84\x04\x08\x10 @\x80\x80\xfc\x00\x00\x00',b'8'],
 51:[b'x\x84\x84\x04\x048\x04\x04\x84\x84x\x00\x00\x00',b'8'],
 52:[b'\x04\x0c\x14$D\x84\x84\xfe\x04\x04\x04\x00\x00\x00',b'8'],
 53:[b'\xfc\x80\x80\x80\xf8\x04\x04\x04\x84\x84x\x00\x00\x00',b'8'],
 54:[b'x\x84\x80\x80\xb8\xc4\x84\x84\x84\x84x\x00\x00\x00',b'8'],
 55:[b'\xfc\x04\x08\x08\x10\x10  @@@\x00\x00\x00',b'8'],
 56:[b'x\x84\x84\x84\x84x\x84\x84\x84\x84x\x00\x00\x00',b'8'],
 57:[b'x\x84\x84\x84\x84|\x04\x04\x84\x84x\x00\x00\x00',b'8'],
 58:[b'\x00\x00\x00\x80\x80\x00\x00\x00\x00\x80\x80\x00\x00\x00',b'3'],
 176:[b'`\x90\x90`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'6'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 14, int(_g[c][1])

