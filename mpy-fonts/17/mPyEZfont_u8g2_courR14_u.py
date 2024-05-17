'''
    mPyEZfont_u8g2_courR14_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original courR14.bdf font file was sourced from the U8G2 project:
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
# Font: courR14.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./u-char.set -e 32 ../u8g2/tools/font/bdf/courR14.bdf 0 tmp_mPyEZfont_u8g2_courR14_u.py
version = '0.33'

def height():
    return 17

def baseline():
    return 13

def max_width():
    return 11

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
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x04\x00\x04\x00\x00\x00\x00\x00'\
b'\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x19\x80\x19\x80\x19\x80\x08\x80\x08\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x09\x00\x09\x00\x09\x00\x09\x00\x09\x00\x3f\x80\x12\x00'\
b'\x12\x00\x12\x00\x7f\x00\x12\x00\x12\x00\x12\x00\x12\x00\x12\x00'\
b'\x00\x00\x00\x00\x0b\x00\x04\x00\x04\x00\x1d\x00\x23\x00\x21\x00'\
b'\x20\x00\x18\x00\x06\x00\x01\x00\x21\x00\x31\x00\x2e\x00\x04\x00'\
b'\x04\x00\x04\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x1c\x00\x22\x00'\
b'\x22\x00\x22\x00\x1c\xc0\x07\x00\x18\x00\x67\x00\x08\x80\x08\x80'\
b'\x08\x80\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x00\x00\x0e\x00\x10\x00\x10\x00\x10\x00\x08\x00\x1d\x00'\
b'\x22\x00\x22\x00\x26\x00\x19\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x04\x00\x04\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x01\x00\x02\x00\x02\x00\x04\x00'\
b'\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x02\x00'\
b'\x02\x00\x01\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x10\x00\x08\x00'\
b'\x08\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00'\
b'\x04\x00\x08\x00\x08\x00\x10\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x04\x00\x04\x00\x04\x00\x3f\x80\x04\x00\x0a\x00\x11\x00\x11\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x04\x00\x04\x00\x04\x00\x04\x00'\
b'\x7f\xc0\x04\x00\x04\x00\x04\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x06\x00'\
b'\x0c\x00\x08\x00\x10\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x80\x00\x80\x01\x00\x01\x00\x02\x00\x02\x00\x04\x00'\
b'\x04\x00\x08\x00\x08\x00\x10\x00\x10\x00\x20\x00\x20\x00\x40\x00'\
b'\x40\x00\x00\x00\x0b\x00\x00\x00\x0e\x00\x11\x00\x20\x80\x20\x80'\
b'\x20\x80\x20\x80\x20\x80\x20\x80\x20\x80\x20\x80\x11\x00\x0e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x34\x00'\
b'\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00'\
b'\x04\x00\x3f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x0e\x00\x11\x00\x20\x80\x20\x80\x00\x80\x01\x00\x02\x00\x04\x00'\
b'\x08\x00\x10\x80\x20\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x1e\x00\x21\x00\x00\x80\x00\x80\x01\x00\x0e\x00'\
b'\x01\x00\x00\x80\x00\x80\x00\x80\x21\x00\x1e\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x03\x00\x05\x00\x05\x00\x09\x00'\
b'\x09\x00\x11\x00\x11\x00\x21\x00\x3f\x80\x01\x00\x01\x00\x07\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x3f\x00\x20\x00'\
b'\x20\x00\x20\x00\x2e\x00\x31\x00\x00\x80\x00\x80\x00\x80\x00\x80'\
b'\x61\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x07\x00\x18\x00\x10\x00\x20\x00\x20\x00\x2e\x00\x31\x00\x20\x80'\
b'\x20\x80\x20\x80\x11\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x3f\x80\x20\x80\x00\x80\x00\x80\x01\x00\x01\x00'\
b'\x01\x00\x01\x00\x02\x00\x02\x00\x02\x00\x02\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x0e\x00\x11\x00\x20\x80\x20\x80'\
b'\x11\x00\x0e\x00\x11\x00\x20\x80\x20\x80\x20\x80\x11\x00\x0e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x0e\x00\x11\x00'\
b'\x20\x80\x20\x80\x20\x80\x11\x80\x0e\x80\x00\x80\x00\x80\x01\x00'\
b'\x03\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x18\x00\x10\x00'\
b'\x20\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x03\x00'\
b'\x0c\x00\x30\x00\xc0\x00\x30\x00\x0c\x00\x03\x00\x00\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x7f\xc0\x00\x00\x00\x00\x7f\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x00\x00\xc0\x00\x30\x00\x0c\x00\x03\x00\x00\xc0\x03\x00'\
b'\x0c\x00\x30\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x1f\x00\x20\x80\x20\x80\x00\x80\x00\x80'\
b'\x07\x00\x04\x00\x04\x00\x00\x00\x06\x00\x06\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x0e\x00\x11\x00\x20\x80\x20\x80'\
b'\x23\x80\x24\x80\x24\x80\x24\x80\x23\xc0\x20\x00\x20\x00\x10\xc0'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x3c\x00'\
b'\x04\x00\x0a\x00\x0a\x00\x11\x00\x11\x00\x20\x80\x3f\x80\x40\x40'\
b'\x40\x40\xf1\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x7e\x00\x21\x00\x20\x80\x20\x80\x21\x00\x3f\x00\x20\x80'\
b'\x20\x40\x20\x40\x20\x80\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x0f\x40\x30\xc0\x20\x40\x40\x00\x40\x00'\
b'\x40\x00\x40\x00\x40\x00\x20\x40\x30\x80\x0f\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x7e\x00\x21\x80\x20\x80'\
b'\x20\x40\x20\x40\x20\x40\x20\x40\x20\x40\x20\x80\x21\x80\x7e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x7f\x80'\
b'\x20\x80\x20\x80\x20\x80\x24\x00\x3c\x00\x24\x00\x20\x80\x20\x80'\
b'\x20\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x7f\x80\x20\x80\x20\x80\x20\x80\x24\x00\x3c\x00\x24\x00'\
b'\x20\x00\x20\x00\x20\x00\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x0f\x40\x30\xc0\x20\x40\x40\x00\x40\x00'\
b'\x40\x00\x41\xe0\x40\x40\x20\x40\x30\x80\x0f\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x71\xc0\x20\x80\x20\x80'\
b'\x20\x80\x20\x80\x3f\x80\x20\x80\x20\x80\x20\x80\x20\x80\x71\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x3f\x80'\
b'\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00'\
b'\x04\x00\x3f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x0f\xc0\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x41\x00'\
b'\x41\x00\x41\x00\x22\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x79\xe0\x20\x80\x21\x00\x22\x00\x24\x00'\
b'\x2c\x00\x32\x00\x21\x00\x21\x00\x20\x80\x78\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x7c\x00\x10\x00\x10\x00'\
b'\x10\x00\x10\x00\x10\x00\x10\x00\x10\x40\x10\x40\x10\x40\x7f\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\xe0\xe0'\
b'\x60\xc0\x51\x40\x51\x40\x4a\x40\x4a\x40\x44\x40\x44\x40\x40\x40'\
b'\x40\x40\xf1\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x73\xc0\x30\x80\x28\x80\x28\x80\x24\x80\x24\x80\x22\x80'\
b'\x22\x80\x21\x80\x21\x80\x78\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x0e\x00\x31\x80\x20\x80\x40\x40\x40\x40'\
b'\x40\x40\x40\x40\x40\x40\x20\x80\x31\x80\x0e\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x7f\x00\x20\x80\x20\x40'\
b'\x20\x40\x20\x80\x3f\x00\x20\x00\x20\x00\x20\x00\x20\x00\x7c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x0e\x00'\
b'\x31\x80\x20\x80\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x20\x80'\
b'\x31\x80\x0e\x00\x1c\x40\x23\x80\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x7f\x00\x20\x80\x20\x40\x20\x40\x20\x80\x3f\x00\x22\x00'\
b'\x21\x00\x21\x00\x20\x80\x78\x60\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x1e\x80\x21\x80\x40\x80\x40\x00\x20\x00'\
b'\x1e\x00\x01\x00\x00\x80\x40\x80\x61\x00\x5e\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x7f\xc0\x44\x40\x44\x40'\
b'\x44\x40\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x1f\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\xf3\xc0'\
b'\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80'\
b'\x21\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\xf1\xe0\x40\x40\x40\x40\x20\x80\x20\x80\x11\x00\x11\x00'\
b'\x0a\x00\x0a\x00\x04\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\xf1\xe0\x40\x40\x44\x40\x44\x40\x44\x40'\
b'\x2a\x80\x2a\x80\x2a\x80\x2a\x80\x11\x00\x11\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x71\xc0\x20\x80\x11\x00'\
b'\x11\x00\x0a\x00\x04\x00\x0a\x00\x11\x00\x11\x00\x20\x80\x71\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x71\xc0'\
b'\x20\x80\x11\x00\x11\x00\x0a\x00\x0a\x00\x04\x00\x04\x00\x04\x00'\
b'\x04\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x3f\x80\x20\x80\x20\x80\x01\x00\x02\x00\x04\x00\x08\x00'\
b'\x10\x00\x20\x80\x20\x80\x3f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x07\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00'\
b'\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00'\
b'\x07\x00\x00\x00\x0b\x00\x20\x00\x20\x00\x10\x00\x10\x00\x08\x00'\
b'\x08\x00\x04\x00\x04\x00\x02\x00\x02\x00\x01\x00\x01\x00\x00\x80'\
b'\x00\x80\x00\x40\x00\x40\x00\x00\x0b\x00\x00\x00\x1c\x00\x04\x00'\
b'\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00'\
b'\x04\x00\x04\x00\x04\x00\x04\x00\x1c\x00\x00\x00\x0b\x00\x00\x00'\
b'\x04\x00\x0a\x00\x11\x00\x20\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xe0\x00\x00'\
b'\x00\x00\x00\x00'

_index =\
b'\x00\x00\x24\x00\x48\x00\x6c\x00\x90\x00\xb4\x00\xd8\x00\xfc\x00'\
b'\x20\x01\x44\x01\x68\x01\x8c\x01\xb0\x01\xd4\x01\xf8\x01\x1c\x02'\
b'\x40\x02\x64\x02\x88\x02\xac\x02\xd0\x02\xf4\x02\x18\x03\x3c\x03'\
b'\x60\x03\x84\x03\xa8\x03\xcc\x03\xf0\x03\x14\x04\x38\x04\x5c\x04'\
b'\x80\x04\xa4\x04\xc8\x04\xec\x04\x10\x05\x34\x05\x58\x05\x7c\x05'\
b'\xa0\x05\xc4\x05\xe8\x05\x0c\x06\x30\x06\x54\x06\x78\x06\x9c\x06'\
b'\xc0\x06\xe4\x06\x08\x07\x2c\x07\x50\x07\x74\x07\x98\x07\xbc\x07'\
b'\xe0\x07\x04\x08\x28\x08\x4c\x08\x70\x08\x94\x08\xb8\x08\xdc\x08'\
b'\x00\x09\x24\x09'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 17
    return _mvfont[doff + 2:next_offs], 17, width
 
