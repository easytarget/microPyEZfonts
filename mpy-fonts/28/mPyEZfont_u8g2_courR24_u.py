'''
    mPyEZfont_u8g2_courR24_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original courR24.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "Copyright (c) 1984, 1987 Adobe Systems Incorporated. All Rights Reserved. Copyright (c) 1988, 1991 Digital Equipment Corporation. All Rights Reserved."

    Original Comments from source (may include copyright info):

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
'''

# Code generated by font_to_py.py.
# Font: courR24.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/u-char.set u8g2/tools/font/bdf/courR24.bdf 0 tmp_mPyEZfont_u8g2_courR24_u.py
version = '0.33'

def height():
    return 28

def baseline():
    return 22

def max_width():
    return 20

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 95

_font =\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf0\x00\x0e\x1c'\
b'\x00\x08\x04\x00\x08\x04\x00\x00\x06\x00\x00\x02\x00\x00\x06\x00'\
b'\x00\x04\x00\x00\x1c\x00\x00\x70\x00\x00\x40\x00\x00\x40\x00\x00'\
b'\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x01\xf0'\
b'\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00'\
b'\x00\x00\x20\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00'\
b'\x00\x70\x00\x00\x20\x00\x00\x20\x00\x00\x20\x00\x00\x20\x00\x00'\
b'\x20\x00\x00\x20\x00\x00\x20\x00\x00\x20\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x70\x00\x00\xf8\x00\x00\x70\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x0f\x1e\x00\x0f\x1e\x00'\
b'\x0f\x1e\x00\x0f\x1e\x00\x0f\x1e\x00\x06\x0c\x00\x06\x0c\x00\x04'\
b'\x08\x00\x04\x08\x00\x04\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x88\x00'\
b'\x00\x88\x00\x00\x88\x00\x00\x88\x00\x01\x98\x00\x01\x10\x00\x01'\
b'\x10\x00\x01\x10\x00\x0f\xff\x00\x01\x10\x00\x01\x10\x00\x01\x10'\
b'\x00\x01\x10\x00\x01\x10\x00\x1f\xfe\x00\x01\x10\x00\x01\x10\x00'\
b'\x01\x10\x00\x01\x30\x00\x02\x20\x00\x02\x20\x00\x02\x20\x00\x02'\
b'\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00'\
b'\x00\x40\x00\x00\x40\x00\x00\x40\x00\x01\xf2\x00\x07\x1e\x00\x04'\
b'\x06\x00\x08\x02\x00\x08\x00\x00\x0c\x00\x00\x06\x00\x00\x03\xc0'\
b'\x00\x00\x78\x00\x00\x0e\x00\x00\x03\x00\x00\x01\x00\x00\x01\x00'\
b'\x08\x03\x00\x0c\x06\x00\x0f\x1c\x00\x09\xf0\x00\x00\x40\x00\x00'\
b'\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x00\x06'\
b'\x60\x00\x0c\x30\x00\x08\x10\x00\x08\x10\x00\x0c\x30\x00\x06\x60'\
b'\x00\x03\xc1\xc0\x00\x0e\x00\x00\x70\x00\x03\x80\x00\x1c\x00\x00'\
b'\x00\x3c\x00\x00\x66\x00\x00\xc3\x00\x00\x81\x00\x00\x81\x00\x00'\
b'\xc3\x00\x00\x66\x00\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf8\x00\x03\x30'\
b'\x00\x06\x00\x00\x04\x00\x00\x04\x00\x00\x06\x00\x00\x02\x00\x00'\
b'\x03\x00\x00\x07\x80\x00\x0c\x86\x00\x08\xcc\x00\x18\x48\x00\x10'\
b'\x68\x00\x18\x38\x00\x08\x30\x00\x0c\x78\x00\x07\xce\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70'\
b'\x00\x00\x70\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00'\
b'\x00\xe0\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x04\x00\x00\x0c'\
b'\x00\x00\x08\x00\x00\x18\x00\x00\x10\x00\x00\x30\x00\x00\x30\x00'\
b'\x00\x20\x00\x00\x20\x00\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00'\
b'\x60\x00\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00\x20\x00\x00\x20'\
b'\x00\x00\x30\x00\x00\x30\x00\x00\x10\x00\x00\x18\x00\x00\x08\x00'\
b'\x00\x0c\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00'\
b'\x00\x04\x00\x00\x06\x00\x00\x02\x00\x00\x03\x00\x00\x01\x00\x00'\
b'\x01\x80\x00\x01\x80\x00\x00\x80\x00\x00\x80\x00\x00\xc0\x00\x00'\
b'\xc0\x00\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00\x00\xc0'\
b'\x00\x00\x80\x00\x00\x80\x00\x01\x80\x00\x01\x80\x00\x01\x00\x00'\
b'\x03\x00\x00\x02\x00\x00\x06\x00\x00\x04\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x14\x00\x00\x00\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00'\
b'\x00\x40\x00\x08\x42\x00\x0f\x5e\x00\x01\xf0\x00\x00\xe0\x00\x00'\
b'\xa0\x00\x01\xb0\x00\x03\x18\x00\x02\x08\x00\x06\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00'\
b'\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x3f\xff'\
b'\x80\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00'\
b'\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x01\xe0\x00\x01\xe0\x00\x03\xc0\x00\x03\xc0\x00\x03'\
b'\x00\x00\x07\x00\x00\x06\x00\x00\x06\x00\x00\x04\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xff\x80\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\xe0\x00\x01\xf0\x00\x01\xf0\x00\x00\xe0\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x02\x00\x00\x06\x00\x00\x04\x00\x00\x04\x00\x00\x0c'\
b'\x00\x00\x08\x00\x00\x18\x00\x00\x10\x00\x00\x30\x00\x00\x20\x00'\
b'\x00\x20\x00\x00\x60\x00\x00\x40\x00\x00\xc0\x00\x00\x80\x00\x00'\
b'\x80\x00\x01\x80\x00\x01\x00\x00\x03\x00\x00\x02\x00\x00\x06\x00'\
b'\x00\x04\x00\x00\x04\x00\x00\x0c\x00\x00\x08\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x01\xf0'\
b'\x00\x03\x18\x00\x06\x0c\x00\x04\x04\x00\x04\x04\x00\x08\x02\x00'\
b'\x08\x02\x00\x08\x02\x00\x08\x02\x00\x08\x02\x00\x08\x02\x00\x08'\
b'\x02\x00\x08\x02\x00\x08\x02\x00\x0c\x06\x00\x04\x04\x00\x04\x04'\
b'\x00\x06\x0c\x00\x03\x18\x00\x01\xf0\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\xc0\x00\x03\xc0\x00\x0e\x40\x00\x00\x40\x00'\
b'\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00'\
b'\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40'\
b'\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x0f\xfe\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x01\xf8\x00\x06\x0c\x00'\
b'\x0c\x02\x00\x08\x02\x00\x08\x02\x00\x00\x02\x00\x00\x06\x00\x00'\
b'\x04\x00\x00\x0c\x00\x00\x18\x00\x00\x30\x00\x00\x60\x00\x00\xc0'\
b'\x00\x01\x80\x00\x03\x00\x00\x06\x00\x00\x0c\x00\x00\x18\x00\x00'\
b'\x10\x01\x00\x1f\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00'\
b'\x01\xf0\x00\x07\x1c\x00\x0c\x06\x00\x00\x02\x00\x00\x02\x00\x00'\
b'\x02\x00\x00\x02\x00\x00\x04\x00\x00\x08\x00\x00\xf0\x00\x00\x0c'\
b'\x00\x00\x02\x00\x00\x01\x00\x00\x01\x00\x00\x01\x00\x00\x01\x00'\
b'\x00\x03\x00\x18\x06\x00\x0e\x1c\x00\x03\xf0\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x28\x00\x00\x28\x00\x00'\
b'\x48\x00\x00\xc8\x00\x00\x88\x00\x01\x08\x00\x03\x08\x00\x02\x08'\
b'\x00\x04\x08\x00\x0c\x08\x00\x08\x08\x00\x10\x08\x00\x1f\xff\x00'\
b'\x00\x08\x00\x00\x08\x00\x00\x08\x00\x00\x08\x00\x00\x08\x00\x00'\
b'\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x07\xfe\x00\x04'\
b'\x00\x00\x04\x00\x00\x04\x00\x00\x04\x00\x00\x04\x00\x00\x04\x00'\
b'\x00\x04\xf0\x00\x07\x9c\x00\x04\x06\x00\x00\x02\x00\x00\x03\x00'\
b'\x00\x01\x00\x00\x01\x00\x00\x01\x00\x00\x03\x00\x18\x02\x00\x0c'\
b'\x06\x00\x07\x1c\x00\x01\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x7c\x00\x01\xc2\x00\x03\x00\x00\x02\x00\x00\x06\x00'\
b'\x00\x04\x00\x00\x0c\x00\x00\x08\xf8\x00\x0b\x8e\x00\x0a\x02\x00'\
b'\x0c\x03\x00\x0c\x01\x00\x0c\x01\x00\x0c\x01\x00\x0c\x01\x00\x04'\
b'\x01\x00\x06\x03\x00\x02\x02\x00\x03\x8e\x00\x00\xf8\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x0f\xfe\x00\x08\x02\x00\x08\x02'\
b'\x00\x00\x06\x00\x00\x04\x00\x00\x04\x00\x00\x0c\x00\x00\x08\x00'\
b'\x00\x08\x00\x00\x18\x00\x00\x10\x00\x00\x10\x00\x00\x30\x00\x00'\
b'\x20\x00\x00\x20\x00\x00\x20\x00\x00\x60\x00\x00\x40\x00\x00\x40'\
b'\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x01\xf0'\
b'\x00\x06\x0c\x00\x04\x04\x00\x0c\x06\x00\x08\x02\x00\x08\x02\x00'\
b'\x0c\x06\x00\x04\x04\x00\x03\x18\x00\x01\xf0\x00\x07\x1c\x00\x04'\
b'\x04\x00\x0c\x06\x00\x08\x02\x00\x08\x02\x00\x08\x02\x00\x0c\x06'\
b'\x00\x04\x04\x00\x07\x1c\x00\x01\xf0\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00'\
b'\x00\x00\x00\x00\x01\xf0\x00\x07\x0c\x00\x04\x06\x00\x0c\x02\x00'\
b'\x08\x03\x00\x08\x03\x00\x08\x03\x00\x08\x03\x00\x0c\x05\x00\x04'\
b'\x0d\x00\x07\x39\x00\x01\xe1\x00\x00\x02\x00\x00\x02\x00\x00\x02'\
b'\x00\x00\x04\x00\x00\x0c\x00\x00\x18\x00\x00\xe0\x00\x07\x80\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x01'\
b'\xf0\x00\x01\xf0\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x01\xf0\x00'\
b'\x01\xf0\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\xe0\x00\x01\xf0\x00\x01\xf0\x00\x00\xe0\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xe0\x00'\
b'\x01\xe0\x00\x03\xc0\x00\x03\x80\x00\x03\x80\x00\x07\x00\x00\x06'\
b'\x00\x00\x06\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00'\
b'\x03\x80\x00\x0e\x00\x00\x38\x00\x00\xe0\x00\x01\x80\x00\x07\x00'\
b'\x00\x1c\x00\x00\x30\x00\x00\x1c\x00\x00\x07\x00\x00\x01\x80\x00'\
b'\x00\xe0\x00\x00\x38\x00\x00\x0e\x00\x00\x03\x80\x00\x00\x80\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x3f\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x3f\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x38\x00\x00\x0e\x00'\
b'\x00\x03\x80\x00\x00\xe0\x00\x00\x30\x00\x00\x1c\x00\x00\x07\x00'\
b'\x00\x01\x80\x00\x07\x00\x00\x1c\x00\x00\x30\x00\x00\xe0\x00\x03'\
b'\x80\x00\x0e\x00\x00\x38\x00\x00\x20\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf0\x00\x0e\x1c'\
b'\x00\x08\x04\x00\x08\x04\x00\x00\x06\x00\x00\x02\x00\x00\x06\x00'\
b'\x00\x04\x00\x00\x1c\x00\x00\x70\x00\x00\x40\x00\x00\x40\x00\x00'\
b'\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x01\xf0'\
b'\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x01\xf0\x00\x03\x18'\
b'\x00\x06\x08\x00\x0c\x0c\x00\x08\x04\x00\x18\x04\x00\x10\x04\x00'\
b'\x10\x1c\x00\x10\x74\x00\x10\xc4\x00\x10\x84\x00\x10\x84\x00\x10'\
b'\x84\x00\x10\xc4\x00\x10\x64\x00\x10\x3e\x00\x10\x00\x00\x18\x00'\
b'\x00\x08\x00\x00\x0c\x00\x00\x06\x00\x00\x03\x1c\x00\x01\xf0\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x1f\xe0\x00\x00\xa0\x00\x00\xa0\x00'\
b'\x01\x10\x00\x01\x10\x00\x01\x10\x00\x02\x08\x00\x02\x08\x00\x02'\
b'\x08\x00\x04\x04\x00\x04\x04\x00\x04\x04\x00\x0f\xfe\x00\x08\x02'\
b'\x00\x08\x02\x00\x10\x01\x00\x10\x01\x00\x30\x01\x80\xfe\x0f\xe0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf8\x00'\
b'\x08\x06\x00\x08\x02\x00\x08\x03\x00\x08\x01\x00\x08\x01\x00\x08'\
b'\x03\x00\x08\x02\x00\x08\x06\x00\x0f\xfc\x00\x08\x03\x00\x08\x01'\
b'\x00\x08\x01\x80\x08\x00\x80\x08\x00\x80\x08\x01\x80\x08\x01\x00'\
b'\x08\x03\x00\x7f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x01\xf1\x00\x07\x1d\x00\x08\x03\x00\x18\x01\x00\x10'\
b'\x01\x00\x30\x01\x00\x20\x00\x00\x20\x00\x00\x20\x00\x00\x20\x00'\
b'\x00\x20\x00\x00\x20\x00\x00\x20\x00\x00\x30\x00\x00\x10\x00\x00'\
b'\x18\x01\x00\x08\x07\x00\x07\x1c\x00\x01\xf0\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xe0\x00\x10\x38\x00\x10'\
b'\x0c\x00\x10\x06\x00\x10\x02\x00\x10\x03\x00\x10\x01\x00\x10\x01'\
b'\x00\x10\x01\x00\x10\x01\x00\x10\x01\x00\x10\x01\x00\x10\x01\x00'\
b'\x10\x03\x00\x10\x02\x00\x10\x06\x00\x10\x0c\x00\x10\x38\x00\x7f'\
b'\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f'\
b'\xfe\x00\x08\x02\x00\x08\x02\x00\x08\x02\x00\x08\x02\x00\x08\x22'\
b'\x00\x08\x20\x00\x08\x20\x00\x0f\xe0\x00\x08\x20\x00\x08\x20\x00'\
b'\x08\x20\x00\x08\x00\x00\x08\x01\x00\x08\x01\x00\x08\x01\x00\x08'\
b'\x01\x00\x08\x01\x00\x7f\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x7f\xff\x00\x08\x01\x00\x08\x01\x00\x08\x01'\
b'\x00\x08\x01\x00\x08\x21\x00\x08\x20\x00\x08\x20\x00\x0f\xe0\x00'\
b'\x08\x20\x00\x08\x20\x00\x08\x20\x00\x08\x00\x00\x08\x00\x00\x08'\
b'\x00\x00\x08\x00\x00\x08\x00\x00\x08\x00\x00\x7f\xc0\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf1\x00\x07\x1d'\
b'\x00\x0c\x03\x00\x18\x01\x00\x10\x01\x00\x30\x01\x00\x20\x00\x00'\
b'\x20\x00\x00\x20\x00\x00\x20\x00\x00\x20\x00\x00\x20\x3f\x80\x20'\
b'\x01\x00\x30\x01\x00\x10\x01\x00\x18\x01\x00\x0c\x01\x00\x07\x07'\
b'\x00\x01\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x3f\x1f\x80\x08\x02\x00\x08\x02\x00\x08\x02\x00\x08\x02\x00'\
b'\x08\x02\x00\x08\x02\x00\x08\x02\x00\x08\x02\x00\x0f\xfe\x00\x08'\
b'\x02\x00\x08\x02\x00\x08\x02\x00\x08\x02\x00\x08\x02\x00\x08\x02'\
b'\x00\x08\x02\x00\x08\x02\x00\x3f\x1f\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x0f\xfe\x00\x00\x40\x00\x00\x40\x00'\
b'\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00'\
b'\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40'\
b'\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x0f\xfe\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xc0'\
b'\x00\x04\x00\x00\x04\x00\x00\x04\x00\x00\x04\x00\x00\x04\x00\x00'\
b'\x04\x00\x00\x04\x00\x00\x04\x00\x00\x04\x00\x00\x04\x00\x10\x04'\
b'\x00\x10\x04\x00\x10\x04\x00\x10\x04\x00\x18\x0c\x00\x08\x08\x00'\
b'\x0c\x38\x00\x03\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x7f\x0f\xc0\x08\x02\x00\x08\x06\x00\x08\x04\x00\x08'\
b'\x08\x00\x08\x18\x00\x08\x20\x00\x08\x60\x00\x09\xc0\x00\x0e\x60'\
b'\x00\x08\x10\x00\x08\x18\x00\x08\x08\x00\x08\x0c\x00\x08\x04\x00'\
b'\x08\x04\x00\x08\x06\x00\x08\x02\x00\x7f\x03\xc0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xe0\x00\x02\x00\x00\x02'\
b'\x00\x00\x02\x00\x00\x02\x00\x00\x02\x00\x00\x02\x00\x00\x02\x00'\
b'\x00\x02\x00\x00\x02\x00\x00\x02\x00\x00\x02\x00\x00\x02\x00\x80'\
b'\x02\x00\x80\x02\x00\x80\x02\x00\x80\x02\x00\x80\x02\x00\x80\x3f'\
b'\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8'\
b'\x03\xe0\x28\x02\x80\x28\x02\x80\x24\x04\x80\x24\x04\x80\x22\x08'\
b'\x80\x22\x08\x80\x21\x10\x80\x21\x10\x80\x21\x10\x80\x20\xa0\x80'\
b'\x20\xa0\x80\x20\x40\x80\x20\x40\x80\x20\x00\x80\x20\x00\x80\x20'\
b'\x00\x80\x20\x00\x80\xfe\x07\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\xf8\x1f\xc0\x1c\x01\x00\x14\x01\x00\x12\x01'\
b'\x00\x12\x01\x00\x11\x01\x00\x10\x81\x00\x10\x81\x00\x10\x41\x00'\
b'\x10\x41\x00\x10\x21\x00\x10\x21\x00\x10\x11\x00\x10\x11\x00\x10'\
b'\x09\x00\x10\x09\x00\x10\x05\x00\x10\x07\x00\x7f\x03\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf0\x00\x06\x0c'\
b'\x00\x0c\x06\x00\x18\x03\x00\x10\x01\x00\x30\x01\x80\x20\x00\x80'\
b'\x20\x00\x80\x20\x00\x80\x20\x00\x80\x20\x00\x80\x20\x00\x80\x20'\
b'\x00\x80\x30\x01\x80\x10\x01\x00\x18\x03\x00\x0c\x06\x00\x06\x0c'\
b'\x00\x01\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x7f\xf0\x00\x08\x1c\x00\x08\x02\x00\x08\x03\x00\x08\x01\x00'\
b'\x08\x01\x00\x08\x01\x00\x08\x03\x00\x08\x02\x00\x08\x1c\x00\x0f'\
b'\xf0\x00\x08\x00\x00\x08\x00\x00\x08\x00\x00\x08\x00\x00\x08\x00'\
b'\x00\x08\x00\x00\x08\x00\x00\x7f\xe0\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x01\xf0\x00\x07\x1c\x00\x0c\x06\x00'\
b'\x18\x03\x00\x10\x01\x00\x30\x01\x80\x20\x00\x80\x20\x00\x80\x20'\
b'\x00\x80\x20\x00\x80\x20\x00\x80\x20\x00\x80\x20\x00\x80\x30\x01'\
b'\x80\x10\x01\x00\x18\x03\x00\x0e\x0e\x00\x03\x18\x00\x01\xf0\x00'\
b'\x00\x80\x00\x03\xf1\x80\x06\x1f\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf0\x00'\
b'\x08\x1c\x00\x08\x02\x00\x08\x03\x00\x08\x01\x00\x08\x01\x00\x08'\
b'\x03\x00\x08\x02\x00\x08\x0c\x00\x0f\xf0\x00\x08\x30\x00\x08\x18'\
b'\x00\x08\x0c\x00\x08\x06\x00\x08\x02\x00\x08\x03\x00\x08\x01\x00'\
b'\x08\x01\x80\x7f\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x01\xf2\x00\x07\x1a\x00\x0c\x06\x00\x08\x06\x00\x08'\
b'\x02\x00\x08\x02\x00\x08\x00\x00\x0c\x00\x00\x07\x00\x00\x01\xe0'\
b'\x00\x00\x38\x00\x00\x0c\x00\x00\x06\x00\x10\x02\x00\x10\x02\x00'\
b'\x18\x02\x00\x1c\x06\x00\x17\x1c\x00\x11\xf0\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xff\x80\x20\x40\x80\x20'\
b'\x40\x80\x20\x40\x80\x20\x40\x80\x20\x40\x80\x20\x40\x80\x00\x40'\
b'\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00'\
b'\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x0f'\
b'\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f'\
b'\x1f\xc0\x10\x01\x00\x10\x01\x00\x10\x01\x00\x10\x01\x00\x10\x01'\
b'\x00\x10\x01\x00\x10\x01\x00\x10\x01\x00\x10\x01\x00\x10\x01\x00'\
b'\x10\x01\x00\x10\x01\x00\x10\x01\x00\x18\x03\x00\x08\x02\x00\x0c'\
b'\x06\x00\x07\x1c\x00\x01\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\xfe\x0f\xe0\x30\x01\x80\x10\x01\x00\x10\x01'\
b'\x00\x18\x03\x00\x08\x02\x00\x08\x02\x00\x0c\x06\x00\x04\x04\x00'\
b'\x04\x04\x00\x06\x0c\x00\x02\x08\x00\x03\x18\x00\x01\x10\x00\x01'\
b'\x10\x00\x00\xa0\x00\x00\xa0\x00\x00\xe0\x00\x00\x40\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7e\x0f\xc0\x20\x00'\
b'\x80\x20\x00\x80\x20\x00\x80\x20\x00\x80\x30\xe1\x80\x10\xa1\x00'\
b'\x10\xa1\x00\x11\x11\x00\x11\x11\x00\x11\x11\x00\x11\x11\x00\x13'\
b'\x19\x00\x12\x09\x00\x1a\x0b\x00\x0a\x0a\x00\x0a\x0a\x00\x0c\x06'\
b'\x00\x0c\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x3e\x0f\x80\x18\x03\x00\x08\x02\x00\x0c\x06\x00\x04\x04\x00'\
b'\x02\x08\x00\x01\x10\x00\x01\xb0\x00\x00\xe0\x00\x00\x40\x00\x00'\
b'\xe0\x00\x01\x10\x00\x02\x08\x00\x06\x0c\x00\x04\x04\x00\x08\x02'\
b'\x00\x18\x03\x00\x30\x01\x80\x7e\x0f\xc0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x3e\x0f\x80\x18\x03\x00\x0c\x06\x00'\
b'\x04\x04\x00\x06\x0c\x00\x02\x08\x00\x01\x10\x00\x01\xb0\x00\x00'\
b'\xa0\x00\x00\xe0\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40'\
b'\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x07\xfc\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xfe\x00'\
b'\x08\x02\x00\x08\x06\x00\x08\x04\x00\x08\x0c\x00\x08\x18\x00\x00'\
b'\x10\x00\x00\x30\x00\x00\x60\x00\x00\xc0\x00\x00\x80\x00\x01\x80'\
b'\x00\x03\x01\x00\x02\x01\x00\x06\x01\x00\x0c\x01\x00\x08\x01\x00'\
b'\x18\x01\x00\x1f\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x7c\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00'\
b'\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40'\
b'\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00'\
b'\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00'\
b'\x40\x00\x00\x40\x00\x00\x7c\x00\x00\x00\x00\x00\x00\x00\x14\x00'\
b'\x08\x00\x00\x0c\x00\x00\x04\x00\x00\x04\x00\x00\x06\x00\x00\x02'\
b'\x00\x00\x03\x00\x00\x01\x00\x00\x01\x80\x00\x00\x80\x00\x00\x80'\
b'\x00\x00\xc0\x00\x00\x40\x00\x00\x60\x00\x00\x20\x00\x00\x20\x00'\
b'\x00\x30\x00\x00\x10\x00\x00\x18\x00\x00\x08\x00\x00\x0c\x00\x00'\
b'\x04\x00\x00\x04\x00\x00\x06\x00\x00\x02\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x07\xc0\x00\x00'\
b'\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40'\
b'\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00'\
b'\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00'\
b'\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40'\
b'\x00\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00'\
b'\x40\x00\x00\xe0\x00\x01\xb0\x00\x01\x10\x00\x03\x18\x00\x06\x0c'\
b'\x00\x04\x04\x00\x0c\x06\x00\x08\x02\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\xff\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00'

_index =\
b'\x00\x00\x56\x00\xac\x00\x02\x01\x58\x01\xae\x01\x04\x02\x5a\x02'\
b'\xb0\x02\x06\x03\x5c\x03\xb2\x03\x08\x04\x5e\x04\xb4\x04\x0a\x05'\
b'\x60\x05\xb6\x05\x0c\x06\x62\x06\xb8\x06\x0e\x07\x64\x07\xba\x07'\
b'\x10\x08\x66\x08\xbc\x08\x12\x09\x68\x09\xbe\x09\x14\x0a\x6a\x0a'\
b'\xc0\x0a\x16\x0b\x6c\x0b\xc2\x0b\x18\x0c\x6e\x0c\xc4\x0c\x1a\x0d'\
b'\x70\x0d\xc6\x0d\x1c\x0e\x72\x0e\xc8\x0e\x1e\x0f\x74\x0f\xca\x0f'\
b'\x20\x10\x76\x10\xcc\x10\x22\x11\x78\x11\xce\x11\x24\x12\x7a\x12'\
b'\xd0\x12\x26\x13\x7c\x13\xd2\x13\x28\x14\x7e\x14\xd4\x14\x2a\x15'\
b'\x80\x15\xd6\x15'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 28
    return _mvfont[doff + 2:next_offs], 28, width
 
