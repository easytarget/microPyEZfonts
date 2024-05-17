'''
    mPyEZfont_u8g2_timR24_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original timR24.bdf font file was sourced from the U8G2 project:
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
# Font: timR24.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./u-char.set -e 32 ../u8g2/tools/font/bdf/timR24.bdf 0 tmp_mPyEZfont_u8g2_timR24_u.py
version = '0.33'

def height():
    return 31

def baseline():
    return 25

def max_width():
    return 32

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
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0b\x00\x00\x00\x00\x00\x0c\x00\x1e\x00\x1e\x00\x1e\x00'\
b'\x1e\x00\x1e\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x0c\x00'\
b'\x1e\x00\x1e\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0e\x00\x00\x00\x00\x00\x38\xe0\x38\xe0\x38\xe0\x38\xe0'\
b'\x10\x40\x10\x40\x10\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x06\x18\x00\x06\x18\x00'\
b'\x06\x18\x00\x06\x18\x00\x06\x18\x00\x06\x18\x00\x06\x18\x00\x06'\
b'\x18\x00\x7f\xff\x00\x7f\xff\x00\x0c\x30\x00\x0c\x30\x00\x0c\x30'\
b'\x00\x0c\x30\x00\xff\xfe\x00\xff\xfe\x00\x18\x60\x00\x18\x60\x00'\
b'\x18\x60\x00\x18\x60\x00\x18\x60\x00\x18\x60\x00\x18\x60\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x00\x00\x80\x00\x80\x03\xf0\x0e\x9c\x0c\x8e\x18\x86\x18'\
b'\x82\x18\x82\x1c\x80\x1e\x80\x0f\x80\x0f\xc0\x07\xe0\x01\xf0\x00'\
b'\xf8\x00\xbc\x00\x9c\x00\x8e\x00\x8e\x20\x86\x20\x86\x30\x8e\x38'\
b'\x8c\x1c\x98\x07\xf0\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00'\
b'\x00\x1b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x10\x00\x07'\
b'\x60\xf0\x00\x0e\x3f\x20\x00\x1c\x10\x60\x00\x1c\x10\xc0\x00\x38'\
b'\x10\x80\x00\x38\x11\x80\x00\x38\x31\x00\x00\x30\x23\x00\x00\x30'\
b'\x62\x00\x00\x30\x46\x1e\x00\x19\x84\x3b\x00\x0f\x0c\x71\x80\x00'\
b'\x18\xe0\x80\x00\x10\xe0\x80\x00\x31\xc0\x80\x00\x21\xc0\x80\x00'\
b'\x61\xc1\x80\x00\x41\x81\x00\x00\xc1\x83\x00\x00\x81\x82\x00\x01'\
b'\x80\xcc\x00\x01\x00\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3e\x00\x00\x00\x63\x00'\
b'\x00\x00\xc3\x80\x00\x00\xc1\x80\x00\x01\xc1\x80\x00\x01\xc1\x80'\
b'\x00\x01\xc3\x00\x00\x01\xe3\x00\x00\x00\xe6\x00\x00\x00\xfc\x7f'\
b'\x00\x00\xf0\x1c\x00\x01\xf0\x18\x00\x07\x78\x10\x00\x0e\x3c\x30'\
b'\x00\x1c\x1c\x20\x00\x18\x1e\x60\x00\x38\x0f\xc0\x00\x38\x07\x80'\
b'\x00\x38\x03\xc0\x00\x3c\x07\xe0\x80\x1e\x0c\xff\x00\x1f\xf8\x7e'\
b'\x00\x07\xe0\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00'\
b'\x00\x70\x70\x70\x70\x20\x20\x20\x20\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00'\
b'\x00\x00\x00\x00\x00\xc0\x01\x80\x03\x00\x06\x00\x0e\x00\x0c\x00'\
b'\x1c\x00\x1c\x00\x18\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x18\x00\x1c\x00\x1c\x00'\
b'\x0c\x00\x0e\x00\x06\x00\x03\x00\x01\x80\x00\xc0\x00\x00\x0b\x00'\
b'\x00\x00\x00\x00\x60\x00\x30\x00\x18\x00\x0c\x00\x0e\x00\x06\x00'\
b'\x07\x00\x07\x00\x03\x00\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80'\
b'\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x00\x07\x00\x07\x00'\
b'\x06\x00\x0e\x00\x0c\x00\x18\x00\x30\x00\x60\x00\x00\x00\x11\x00'\
b'\x00\x00\x00\x00\x00\x00\x01\x80\x00\x03\xc0\x00\x01\x80\x00\x31'\
b'\x8c\x00\x3d\xbc\x00\x1d\xb8\x00\x03\xc0\x00\x1d\xb8\x00\x3d\xbc'\
b'\x00\x31\x8c\x00\x01\x80\x00\x03\xc0\x00\x01\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00'\
b'\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00\x7f\xff\x80\x7f'\
b'\xff\x80\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00\x00\xc0'\
b'\x00\x00\xc0\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x18\x3c\x3c\x1c\x04\x08\x10\x00\x00\x00\x0b\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f'\
b'\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x18\x3c\x3c\x18\x00\x00\x00\x00\x00\x00\x0a\x00'\
b'\x00\x00\x00\x00\x00\xc0\x00\xc0\x01\x80\x01\x80\x03\x80\x03\x00'\
b'\x03\x00\x03\x00\x06\x00\x06\x00\x06\x00\x0e\x00\x0c\x00\x0c\x00'\
b'\x1c\x00\x18\x00\x18\x00\x18\x00\x30\x00\x30\x00\x30\x00\x70\x00'\
b'\x60\x00\x60\x00\xc0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x03\xc0\x0e\x70\x1c\x38\x18\x18\x38\x1c\x38\x1c'\
b'\x30\x0c\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e'\
b'\x70\x0e\x70\x0e\x70\x0c\x38\x1c\x38\x1c\x18\x18\x1c\x38\x0e\x70'\
b'\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\xc0\x01\xc0\x07\xc0\x0d\xc0\x01\xc0\x01\xc0'\
b'\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0'\
b'\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x03\xe0'\
b'\x0f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x07\xe0\x0f\xf0\x1c\xf8\x30\x3c\x20\x3c\x60\x1c'\
b'\x40\x1c\x00\x1c\x00\x1c\x00\x18\x00\x38\x00\x30\x00\x60\x00\x60'\
b'\x00\xc0\x01\x80\x03\x00\x06\x00\x0c\x02\x18\x06\x3f\xfc\x7f\xf8'\
b'\xff\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x03\xe0\x0f\xf0\x18\x78\x30\x38\x20\x38\x00\x38'\
b'\x00\x30\x00\x30\x00\x60\x00\xc0\x01\xf0\x07\xf8\x00\x7c\x00\x1c'\
b'\x00\x1c\x00\x0c\x00\x0c\x00\x0c\x00\x1c\x00\x18\x38\x30\x3c\xe0'\
b'\x1f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\x30\x00\x70\x00\x70\x00\xf0\x00\xb0\x01\xb0'\
b'\x03\x30\x02\x30\x06\x30\x0c\x30\x08\x30\x18\x30\x30\x30\x20\x30'\
b'\x7f\xfe\x7f\xfe\x7f\xfe\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30'\
b'\x00\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x07\xfc\x0f\xf8\x0f\xf0\x08\x00\x18\x00\x10\x00'\
b'\x3f\x00\x3f\xc0\x3f\xe0\x03\xf0\x00\xf0\x00\x78\x00\x38\x00\x38'\
b'\x00\x18\x00\x18\x00\x18\x00\x18\x00\x30\x00\x30\x70\x60\x79\xc0'\
b'\x3f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\x3c\x00\xe0\x01\xc0\x07\x80\x0f\x00\x0e\x00'\
b'\x1c\x00\x3c\x00\x38\x00\x39\xe0\x7b\xf8\x7c\x3c\x70\x1c\x70\x1e'\
b'\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x38\x0e\x38\x0c\x1c\x1c\x0e\x30'\
b'\x03\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x1f\xfe\x3f\xfe\x30\x0c\x60\x0c\x40\x1c\x00\x18'\
b'\x00\x18\x00\x18\x00\x30\x00\x30\x00\x30\x00\x70\x00\x60\x00\x60'\
b'\x00\xe0\x00\xc0\x00\xc0\x00\xc0\x01\x80\x01\x80\x01\x80\x03\x80'\
b'\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x07\xe0\x0e\x38\x1c\x1c\x38\x0c\x38\x0c\x38\x0c'\
b'\x38\x1c\x3c\x18\x1f\x30\x0f\xc0\x07\xe0\x03\xf0\x06\xf8\x1c\x7c'\
b'\x18\x3c\x38\x1e\x30\x1e\x30\x0e\x30\x0e\x38\x0e\x18\x1c\x1c\x38'\
b'\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x03\xc0\x0c\x70\x18\x38\x38\x1c\x30\x1c\x70\x0e'\
b'\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x78\x0e\x38\x0e\x3c\x1e\x1f\x7e'\
b'\x07\xdc\x00\x1c\x00\x38\x00\x38\x00\x70\x00\xe0\x01\xc0\x07\x80'\
b'\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x18\x00\x3c\x00\x3c\x00\x18\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x3c\x00\x3c\x00'\
b'\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x18\x00\x3c\x00\x3c\x00\x18\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x3c\x00\x3c\x00'\
b'\x1c\x00\x04\x00\x08\x00\x10\x00\x00\x00\x00\x00\x00\x00\x13\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x80\x00\x03\x80\x00\x0f\x80\x00\x3e'\
b'\x00\x00\xf8\x00\x03\xe0\x00\x0f\x80\x00\x3e\x00\x00\x78\x00\x00'\
b'\x78\x00\x00\x3e\x00\x00\x0f\x80\x00\x03\xe0\x00\x00\xf8\x00\x00'\
b'\x3e\x00\x00\x0f\x80\x00\x03\x80\x00\x00\x80\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x7f\xff\x80\x7f\xff\x80\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xff\x80\x7f\xff\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x20\x00\x00\x38\x00\x00\x3e\x00\x00\x0f\x80\x00\x03'\
b'\xe0\x00\x00\xf8\x00\x00\x3e\x00\x00\x0f\x80\x00\x03\xc0\x00\x03'\
b'\xc0\x00\x0f\x80\x00\x3e\x00\x00\xf8\x00\x03\xe0\x00\x0f\x80\x00'\
b'\x3e\x00\x00\x38\x00\x00\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00'\
b'\x00\x07\xc0\x1c\xe0\x30\x70\x30\x70\x38\x38\x38\x38\x18\x38\x00'\
b'\x70\x00\x70\x00\x60\x00\xe0\x00\xc0\x01\x80\x01\x00\x03\x00\x02'\
b'\x00\x02\x00\x00\x00\x00\x00\x03\x00\x07\x80\x07\x80\x03\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x07\xfc\x00\x00\x3e\x0f\x00\x00\x78\x01'\
b'\x80\x01\xe0\x00\xc0\x03\x80\x00\x60\x07\x00\x00\x30\x07\x00\x00'\
b'\x30\x0e\x01\xe3\x18\x1c\x07\xd7\x18\x1c\x07\x1f\x08\x1c\x0e\x0e'\
b'\x08\x38\x1c\x0e\x08\x38\x1c\x0c\x08\x38\x1c\x1c\x08\x38\x38\x1c'\
b'\x18\x38\x38\x1c\x10\x38\x38\x38\x30\x38\x38\x38\x20\x1c\x38\x78'\
b'\x60\x1c\x1d\xdc\xc0\x1c\x0f\x0f\x80\x0e\x00\x00\x00\x06\x00\x00'\
b'\x00\x07\x00\x00\x00\x03\x80\x00\x00\x01\xe0\x01\x80\x00\x7c\x0f'\
b'\x00\x00\x1f\xfc\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x18\x00\x00\x18\x00\x00\x38\x00\x00\x3c\x00\x00\x3c\x00'\
b'\x00\x7e\x00\x00\x6e\x00\x00\x4e\x00\x00\xc7\x00\x00\x87\x00\x01'\
b'\x87\x80\x01\x83\x80\x01\x03\x80\x03\x03\xc0\x03\x01\xc0\x07\xff'\
b'\xe0\x06\x01\xe0\x0c\x00\xe0\x0c\x00\xf0\x18\x00\xf0\x18\x00\x78'\
b'\x38\x00\x78\x7e\x01\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00'\
b'\x7f\xff\x00\x1f\x07\xc0\x0e\x01\xe0\x0e\x00\xe0\x0e\x00\xf0\x0e'\
b'\x00\x70\x0e\x00\x70\x0e\x00\xf0\x0e\x00\xe0\x0e\x01\xe0\x0e\x07'\
b'\xc0\x0f\xff\x00\x0e\x03\xc0\x0e\x00\xf0\x0e\x00\x70\x0e\x00\x78'\
b'\x0e\x00\x38\x0e\x00\x38\x0e\x00\x78\x0e\x00\x70\x0e\x00\xf0\x1f'\
b'\x03\xe0\x7f\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\xff\x88\x03\xc1\xf8\x07\x00\x78\x0e\x00\x38\x1c\x00\x18\x1c\x00'\
b'\x18\x38\x00\x08\x38\x00\x08\x78\x00\x00\x78\x00\x00\x78\x00\x00'\
b'\x78\x00\x00\x78\x00\x00\x78\x00\x00\x78\x00\x00\x38\x00\x00\x38'\
b'\x00\x00\x1c\x00\x00\x1c\x00\x08\x0e\x00\x18\x07\x00\x30\x03\xc1'\
b'\xe0\x00\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x7f\xff'\
b'\x00\x1f\x03\xc0\x0e\x00\xe0\x0e\x00\x70\x0e\x00\x38\x0e\x00\x38'\
b'\x0e\x00\x1c\x0e\x00\x1c\x0e\x00\x1e\x0e\x00\x1e\x0e\x00\x1e\x0e'\
b'\x00\x1e\x0e\x00\x1e\x0e\x00\x1e\x0e\x00\x1e\x0e\x00\x1c\x0e\x00'\
b'\x1c\x0e\x00\x38\x0e\x00\x38\x0e\x00\x70\x0e\x00\xe0\x1f\x03\xc0'\
b'\x7f\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x7f\xff\xe0'\
b'\x1f\x01\xe0\x0e\x00\x60\x0e\x00\x20\x0e\x00\x20\x0e\x00\x00\x0e'\
b'\x00\x00\x0e\x00\x00\x0e\x00\x80\x0e\x00\x80\x0e\x01\x80\x0f\xff'\
b'\x80\x0e\x01\x80\x0e\x00\x80\x0e\x00\x80\x0e\x00\x00\x0e\x00\x00'\
b'\x0e\x00\x10\x0e\x00\x10\x0e\x00\x30\x0e\x00\x60\x1f\x01\xe0\x7f'\
b'\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x7f\xff\xc0\x1f'\
b'\x03\xc0\x0e\x00\xc0\x0e\x00\x40\x0e\x00\x40\x0e\x00\x00\x0e\x00'\
b'\x00\x0e\x00\x00\x0e\x01\x00\x0e\x01\x00\x0e\x03\x00\x0f\xff\x00'\
b'\x0e\x03\x00\x0e\x01\x00\x0e\x01\x00\x0e\x00\x00\x0e\x00\x00\x0e'\
b'\x00\x00\x0e\x00\x00\x0e\x00\x00\x0e\x00\x00\x1f\x00\x00\x7f\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\xff\x98\x03\xc3'\
b'\xf8\x07\x00\x78\x0e\x00\x38\x1c\x00\x18\x1c\x00\x18\x38\x00\x08'\
b'\x38\x00\x00\x78\x00\x00\x78\x00\x00\x78\x00\x00\x78\x01\xfe\x78'\
b'\x00\x7c\x78\x00\x38\x78\x00\x38\x38\x00\x38\x38\x00\x38\x1c\x00'\
b'\x38\x1c\x00\x38\x0e\x00\x38\x07\x00\x38\x03\xc0\xf0\x00\xff\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x7f\xc3\xfe\x1f\x00\xf8'\
b'\x0e\x00\x70\x0e\x00\x70\x0e\x00\x70\x0e\x00\x70\x0e\x00\x70\x0e'\
b'\x00\x70\x0e\x00\x70\x0e\x00\x70\x0e\x00\x70\x0f\xff\xf0\x0e\x00'\
b'\x70\x0e\x00\x70\x0e\x00\x70\x0e\x00\x70\x0e\x00\x70\x0e\x00\x70'\
b'\x0e\x00\x70\x0e\x00\x70\x0e\x00\x70\x1f\x00\xf8\x7f\xc3\xfe\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x0b\x00\x00\x00\x00\x00\x7f\xc0\x1f\x00\x0e\x00\x0e\x00\x0e'\
b'\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e'\
b'\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e'\
b'\x00\x1f\x00\x7f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x0d\x00\x00\x00\x00\x00\x0f\xf8\x03\xe0\x01\xc0\x01\xc0\x01'\
b'\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01'\
b'\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x61\xc0\x71'\
b'\x80\x73\x80\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x18\x00\x00\x00\x00\x00\x00\x00\x7f\xe3\xfc\x1f\x00\xf0\x0e'\
b'\x00\xc0\x0e\x01\x80\x0e\x03\x00\x0e\x06\x00\x0e\x0c\x00\x0e\x18'\
b'\x00\x0e\x30\x00\x0e\x60\x00\x0f\xe0\x00\x0f\xf0\x00\x0f\xf8\x00'\
b'\x0f\x3c\x00\x0e\x1e\x00\x0e\x0f\x00\x0e\x07\x80\x0e\x03\xc0\x0e'\
b'\x01\xe0\x0e\x00\xf0\x0e\x00\x78\x1f\x00\x7c\x7f\xe3\xff\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x7f\xc0\x00\x1f\x00\x00\x0e\x00'\
b'\x00\x0e\x00\x00\x0e\x00\x00\x0e\x00\x00\x0e\x00\x00\x0e\x00\x00'\
b'\x0e\x00\x00\x0e\x00\x00\x0e\x00\x00\x0e\x00\x00\x0e\x00\x00\x0e'\
b'\x00\x00\x0e\x00\x00\x0e\x00\x00\x0e\x00\x00\x0e\x00\x10\x0e\x00'\
b'\x10\x0e\x00\x30\x0e\x00\x60\x1f\x01\xe0\x7f\xff\xe0\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7e\x00\x03\xf8\x1f\x00\x03'\
b'\xe0\x0f\x00\x07\xc0\x0f\x80\x07\xc0\x0f\x80\x05\xc0\x0b\x80\x0d'\
b'\xc0\x0b\xc0\x0d\xc0\x09\xc0\x19\xc0\x09\xe0\x19\xc0\x09\xe0\x11'\
b'\xc0\x08\xf0\x31\xc0\x08\xf0\x31\xc0\x08\x70\x61\xc0\x08\x78\x61'\
b'\xc0\x08\x38\x41\xc0\x08\x3c\xc1\xc0\x08\x3c\x81\xc0\x08\x1e\x81'\
b'\xc0\x08\x1f\x81\xc0\x08\x0f\x01\xc0\x08\x0f\x01\xc0\x1c\x06\x03'\
b'\xe0\x7f\x06\x0f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00'\
b'\x00\x00\x00\x00\x00\x7c\x00\xfe\x1e\x00\x38\x0f\x00\x10\x0f\x80'\
b'\x10\x0f\x80\x10\x0b\xc0\x10\x09\xe0\x10\x09\xe0\x10\x08\xf0\x10'\
b'\x08\x78\x10\x08\x7c\x10\x08\x3c\x10\x08\x1e\x10\x08\x0f\x10\x08'\
b'\x0f\x90\x08\x07\x90\x08\x03\xd0\x08\x01\xf0\x08\x00\xf0\x08\x00'\
b'\xf0\x08\x00\x70\x1c\x00\x30\x7f\x00\x10\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\xff\x00\x03\xc3\xc0\x07\x00\xe0\x0e\x00\x70'\
b'\x1c\x00\x38\x1c\x00\x38\x38\x00\x1c\x38\x00\x1c\x78\x00\x1e\x78'\
b'\x00\x1e\x78\x00\x1e\x78\x00\x1e\x78\x00\x1e\x78\x00\x1e\x78\x00'\
b'\x1e\x38\x00\x1c\x38\x00\x1c\x1c\x00\x38\x1c\x00\x38\x0e\x00\x70'\
b'\x07\x00\xe0\x03\xc3\xc0\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00'\
b'\x00\x00\x00\x7f\xfc\x00\x1e\x1f\x00\x0e\x07\x80\x0e\x03\x80\x0e'\
b'\x03\xc0\x0e\x01\xc0\x0e\x01\xc0\x0e\x01\xc0\x0e\x03\xc0\x0e\x03'\
b'\x80\x0e\x07\x80\x0e\x1f\x00\x0f\xf8\x00\x0e\x00\x00\x0e\x00\x00'\
b'\x0e\x00\x00\x0e\x00\x00\x0e\x00\x00\x0e\x00\x00\x0e\x00\x00\x0e'\
b'\x00\x00\x1f\x00\x00\x7f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\xff\x00\x03\xc3\xc0\x07\x00\xe0\x0e\x00\x70\x1c\x00'\
b'\x38\x1c\x00\x38\x38\x00\x1c\x38\x00\x1c\x78\x00\x1e\x78\x00\x1e'\
b'\x78\x00\x1e\x78\x00\x1e\x78\x00\x1e\x78\x00\x1e\x78\x00\x1e\x38'\
b'\x00\x1c\x38\x00\x1c\x1c\x00\x38\x1c\x00\x38\x0e\x00\x70\x07\x00'\
b'\xe0\x03\xc3\xc0\x00\xff\x00\x00\x3e\x00\x00\x1f\x00\x00\x0f\x80'\
b'\x00\x07\xc0\x00\x01\xf0\x00\x00\x3e\x16\x00\x00\x00\x00\x00\x00'\
b'\x00\x7f\xfc\x00\x1e\x1f\x00\x0e\x07\x80\x0e\x03\xc0\x0e\x03\xc0'\
b'\x0e\x01\xc0\x0e\x01\xc0\x0e\x01\xc0\x0e\x03\xc0\x0e\x03\x80\x0e'\
b'\x0f\x00\x0f\xfc\x00\x0e\x78\x00\x0e\x3c\x00\x0e\x1e\x00\x0e\x1e'\
b'\x00\x0e\x0f\x00\x0e\x07\x80\x0e\x07\xc0\x0e\x03\xc0\x0e\x01\xe0'\
b'\x1f\x00\xf0\x7f\xc0\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\xf2\x00\x0e\x1e\x00\x1c\x0e\x00\x38\x06\x00\x38\x02\x00\x38'\
b'\x03\x00\x3c\x00\x00\x3e\x00\x00\x1f\x00\x00\x0f\xc0\x00\x07\xf0'\
b'\x00\x03\xf8\x00\x00\xfc\x00\x00\x3e\x00\x00\x1f\x00\x00\x0f\x00'\
b'\x40\x07\x00\x40\x07\x00\x60\x07\x00\x70\x06\x00\x38\x0e\x00\x3e'\
b'\x3c\x00\x33\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x7f'\
b'\xff\xf0\x78\x70\xf0\x60\x70\x30\x60\x70\x30\x40\x70\x10\x40\x70'\
b'\x10\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00'\
b'\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00'\
b'\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\xf8'\
b'\x00\x03\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x7f\xc0'\
b'\xfe\x1f\x00\x38\x0e\x00\x10\x0e\x00\x10\x0e\x00\x10\x0e\x00\x10'\
b'\x0e\x00\x10\x0e\x00\x10\x0e\x00\x10\x0e\x00\x10\x0e\x00\x10\x0e'\
b'\x00\x10\x0e\x00\x10\x0e\x00\x10\x0e\x00\x10\x0e\x00\x10\x0e\x00'\
b'\x10\x0e\x00\x10\x0f\x00\x30\x07\x00\x20\x07\x80\x60\x03\xe1\xc0'\
b'\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00\x7f\x80\xfe'\
b'\x3e\x00\x38\x1e\x00\x30\x0f\x00\x20\x0f\x00\x60\x07\x00\x60\x07'\
b'\x80\x40\x07\x80\xc0\x03\x80\xc0\x03\xc0\x80\x01\xc1\x80\x01\xe1'\
b'\x80\x01\xe1\x00\x00\xe3\x00\x00\xf3\x00\x00\x72\x00\x00\x76\x00'\
b'\x00\x3e\x00\x00\x3c\x00\x00\x3c\x00\x00\x1c\x00\x00\x18\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x9f'\
b'\xf0\x7f\x3e\x07\xc0\x3c\x1e\x03\x80\x18\x0e\x03\xc0\x18\x0f\x03'\
b'\xc0\x30\x0f\x01\xc0\x30\x07\x01\xe0\x30\x07\x81\xe0\x60\x03\x81'\
b'\xf0\x60\x03\xc3\xf0\x60\x03\xc3\x70\xc0\x01\xc2\x78\xc0\x01\xe6'\
b'\x78\xc0\x01\xe6\x39\x80\x00\xec\x3d\x80\x00\xec\x1d\x80\x00\xfc'\
b'\x1f\x00\x00\x78\x1f\x00\x00\x78\x0e\x00\x00\x70\x0e\x00\x00\x30'\
b'\x0e\x00\x00\x30\x04\x00\x00\x20\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x7f\xe1\xfe\x1f\x80\x78'\
b'\x0f\x80\x70\x07\x80\x60\x03\xc0\xc0\x03\xc1\x80\x01\xe3\x00\x00'\
b'\xf3\x00\x00\xf6\x00\x00\x7c\x00\x00\x3c\x00\x00\x3c\x00\x00\x3e'\
b'\x00\x00\x6f\x00\x00\xcf\x00\x00\xc7\x80\x01\x87\xc0\x03\x03\xc0'\
b'\x07\x01\xe0\x06\x01\xf0\x0c\x00\xf0\x1c\x00\xf8\x7f\x03\xfe\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x18\x00\x00\x00\x00\x00\x00\x00\x7f\xe0\x7e\x1f\x80\x1c\x0f'\
b'\x00\x18\x07\x80\x30\x07\xc0\x60\x03\xc0\x40\x01\xe0\xc0\x01\xe1'\
b'\x80\x00\xf1\x80\x00\x7b\x00\x00\x7e\x00\x00\x3e\x00\x00\x1c\x00'\
b'\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00'\
b'\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x3e\x00\x00\xff\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x1f\xff\xf0\x1c\x01\xe0\x30\x03'\
b'\xc0\x30\x03\xc0\x20\x07\x80\x20\x0f\x00\x00\x0f\x00\x00\x1e\x00'\
b'\x00\x3c\x00\x00\x3c\x00\x00\x78\x00\x00\xf0\x00\x00\xf0\x00\x01'\
b'\xe0\x00\x01\xe0\x00\x03\xc0\x00\x07\x80\x00\x07\x80\x10\x0f\x00'\
b'\x10\x1e\x00\x30\x1e\x00\x30\x3c\x00\xe0\x7f\xff\xe0\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b'\
b'\x00\x00\x00\x00\x00\x1f\xc0\x1e\x00\x1c\x00\x1c\x00\x1c\x00\x1c'\
b'\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c'\
b'\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c'\
b'\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1e\x00\x1f\xc0\x00\x00\x0d'\
b'\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\x60\x00\x70\x00\x30\x00\x38'\
b'\x00\x18\x00\x1c\x00\x0c\x00\x0e\x00\x06\x00\x07\x00\x03\x00\x03'\
b'\x80\x01\x80\x01\xc0\x00\xc0\x00\xe0\x00\x60\x00\x70\x00\x30\x00'\
b'\x38\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b'\
b'\x00\x00\x00\x00\x00\x7f\x00\x0f\x00\x07\x00\x07\x00\x07\x00\x07'\
b'\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07'\
b'\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07'\
b'\x00\x07\x00\x07\x00\x07\x00\x07\x00\x0f\x00\x7f\x00\x00\x00\x10'\
b'\x00\x00\x00\x00\x00\x03\x80\x03\x80\x07\xc0\x06\xc0\x0c\x60\x0c'\
b'\x60\x18\x30\x18\x30\x38\x38\x30\x18\x70\x1c\x60\x0c\x60\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x80\xff'\
b'\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

_index =\
b'\x00\x00\x21\x00\x42\x00\x82\x00\xc2\x00\x21\x01\x61\x01\xdf\x01'\
b'\x5d\x02\x7e\x02\xbe\x02\xfe\x02\x5d\x03\xbc\x03\xdd\x03\x1d\x04'\
b'\x3e\x04\x7e\x04\xbe\x04\xfe\x04\x3e\x05\x7e\x05\xbe\x05\xfe\x05'\
b'\x3e\x06\x7e\x06\xbe\x06\xfe\x06\x3e\x07\x7e\x07\xdd\x07\x3c\x08'\
b'\x9b\x08\xdb\x08\x59\x09\xb8\x09\x17\x0a\x76\x0a\xd5\x0a\x34\x0b'\
b'\x93\x0b\xf2\x0b\x51\x0c\x91\x0c\xd1\x0c\x30\x0d\x8f\x0d\x0d\x0e'\
b'\x6c\x0e\xcb\x0e\x2a\x0f\x89\x0f\xe8\x0f\x47\x10\xa6\x10\x05\x11'\
b'\x64\x11\xe2\x11\x41\x12\xa0\x12\xff\x12\x3f\x13\x7f\x13\xbf\x13'\
b'\xff\x13\x5e\x14'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 31
    return _mvfont[doff + 2:next_offs], 31, width
 
