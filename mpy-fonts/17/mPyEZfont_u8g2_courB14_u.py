'''
    mPyEZfont_u8g2_courB14_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original courB14.bdf font file was sourced from the U8G2 project:
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
# Font: courB14.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/u-char.set u8g2/tools/font/bdf/courB14.bdf 0 tmp_mPyEZfont_u8g2_courB14_u.py
version = '0.33'

def height():
    return 17

def baseline():
    return 13

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
    return 95

_font =\
b'\x0b\x00\x00\x00\x00\x00\x1f\x00\x3f\x80\x31\x80\x01\x80\x03\x80'\
b'\x0f\x00\x0c\x00\x0c\x00\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x0e\x00\x0e\x00'\
b'\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00'\
b'\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x33\x00\x33\x00\x33\x00\x33\x00\x22\x00\x22\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x1b\x00\x1b\x00\x1b\x00\x1b\x00\x7f\x80\x7f\x80\x36\x00'\
b'\x36\x00\x7f\x80\x7f\x80\x36\x00\x36\x00\x36\x00\x36\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x0c\x00\x0c\x00\x1f\x80\x3f\x80\x61\x80'\
b'\x60\x00\x78\x00\x3f\x00\x07\x80\x01\x80\x63\x80\x7f\x00\x7e\x00'\
b'\x0c\x00\x0c\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x38\x00\x6c\x00'\
b'\x44\x00\x6c\x00\x39\x80\x07\x00\x3c\x00\x67\x00\x0d\x80\x08\x80'\
b'\x0d\x80\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x00\x00\x1e\x00\x3f\x00\x33\x00\x30\x00\x18\x00\x3d\x80'\
b'\x7f\x80\x67\x00\x7f\x80\x3d\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x08\x00\x08\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x03\x00\x03\x00\x06\x00\x06\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x06\x00'\
b'\x06\x00\x03\x00\x03\x00\x00\x00\x0b\x00\x00\x00\x30\x00\x30\x00'\
b'\x18\x00\x18\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x18\x00\x18\x00\x30\x00\x30\x00\x00\x00\x0b\x00\x00\x00'\
b'\x0c\x00\x0c\x00\x7f\x80\x7f\x80\x0c\x00\x3f\x00\x73\x80\x21\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\xff\xc0\xff\xc0\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00'\
b'\x18\x00\x10\x00\x20\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x7f\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x01\x80\x01\x80\x03\x00\x03\x00\x06\x00\x06\x00\x0c\x00'\
b'\x0c\x00\x18\x00\x18\x00\x30\x00\x30\x00\x60\x00\x60\x00\xc0\x00'\
b'\xc0\x00\x00\x00\x0b\x00\x00\x00\x1e\x00\x3f\x00\x33\x00\x61\x80'\
b'\x61\x80\x61\x80\x61\x80\x61\x80\x61\x80\x33\x00\x3f\x00\x1e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x7c\x00'\
b'\x7c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x1e\x00\x3f\x00\x63\x80\x61\x80\x01\x80\x03\x80\x07\x00\x0e\x00'\
b'\x1c\x00\x38\x00\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x1e\x00\x3f\x00\x33\x00\x03\x00\x07\x00\x1e\x00'\
b'\x1f\x00\x03\x80\x01\x80\x63\x80\x7f\x00\x3e\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x07\x00\x0f\x00\x1f\x00\x1b\x00'\
b'\x33\x00\x33\x00\x63\x00\x7f\x80\x7f\x80\x03\x00\x0f\x80\x0f\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x3f\x80\x3f\x80'\
b'\x30\x00\x30\x00\x3f\x00\x3f\x80\x33\x80\x01\x80\x01\x80\x63\x80'\
b'\x7f\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x07\x80\x1f\x80\x38\x00\x30\x00\x6e\x00\x7f\x00\x73\x80\x61\x80'\
b'\x61\x80\x73\x80\x3f\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x7f\x80\x7f\x80\x61\x80\x03\x00\x03\x00\x03\x00'\
b'\x06\x00\x06\x00\x06\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x1e\x00\x3f\x00\x73\x80\x61\x80'\
b'\x33\x00\x1e\x00\x3f\x00\x73\x80\x61\x80\x73\x80\x3f\x00\x1e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x1e\x00\x3f\x00'\
b'\x61\x80\x61\x80\x61\x80\x63\x80\x3f\x80\x1d\x80\x01\x80\x03\x00'\
b'\x7f\x00\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x18\x00\x10\x00'\
b'\x20\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x03\xc0'\
b'\x0f\x00\x3c\x00\x70\x00\x3c\x00\x0f\x00\x03\xc0\x00\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\xff\xc0\xff\xc0\x00\x00\x00\x00\xff\xc0\xff\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x00\x00\x60\x00\x78\x00\x1e\x00\x07\x80\x01\xc0\x07\x80'\
b'\x1e\x00\x78\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x1f\x00\x3f\x80\x31\x80\x01\x80\x03\x80'\
b'\x0f\x00\x0c\x00\x0c\x00\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x1e\x00\x33\x00\x61\x80\x67\x80'\
b'\x6d\x80\x6d\x80\x6d\x80\x6d\x80\x67\xc0\x60\x00\x60\x00\x31\x80'\
b'\x1f\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x3e\x00'\
b'\x3f\x00\x0f\x00\x19\x80\x19\x80\x19\x80\x3f\xc0\x3f\xc0\x30\xc0'\
b'\xf9\xf0\xf9\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\xfe\x00\xff\x00\x31\x80\x31\x80\x3f\x00\x3f\x80\x30\xc0'\
b'\x30\xc0\x30\xc0\xff\x80\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x1e\xc0\x7f\xc0\x71\xc0\xe0\xc0\xc0\x00'\
b'\xc0\x00\xc0\x00\xe0\x00\x70\xc0\x7f\xc0\x1f\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\xfe\x00\xff\x80\x63\x80'\
b'\x61\xc0\x60\xc0\x60\xc0\x60\xc0\x61\xc0\x63\x80\xff\x80\xfe\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\xff\xc0'\
b'\xff\xc0\x30\xc0\x36\xc0\x3e\x00\x3e\x00\x36\x00\x30\xc0\x30\xc0'\
b'\xff\xc0\xff\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\xff\xc0\xff\xc0\x30\xc0\x36\xc0\x3e\x00\x3e\x00\x36\x00'\
b'\x30\x00\x30\x00\xfe\x00\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x1e\xc0\x7f\xc0\x71\xc0\xe0\xc0\xc0\x00'\
b'\xc0\x00\xc7\xe0\xe7\xe0\x70\xc0\x7f\xc0\x1f\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\xf3\xc0\xf3\xc0\x61\x80'\
b'\x61\x80\x7f\x80\x7f\x80\x61\x80\x61\x80\x61\x80\xf3\xc0\xf3\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x7f\x80'\
b'\x7f\x80\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x1f\xc0\x1f\xc0\x03\x00\x03\x00\x03\x00\x03\x00\xc3\x00'\
b'\xc3\x00\xc3\x00\xfe\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\xf7\xc0\xf7\xc0\x63\x00\x66\x00\x6c\x00'\
b'\x7c\x00\x7e\x00\x67\x00\x63\x80\xf9\xe0\xf9\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\xfc\x00\xfc\x00\x30\x00'\
b'\x30\x00\x30\x00\x30\x00\x30\xc0\x30\xc0\x30\xc0\xff\xc0\xff\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\xe1\xc0'\
b'\xe1\xc0\x73\x80\x73\x80\x7f\x80\x6d\x80\x6d\x80\x6d\x80\x61\x80'\
b'\xf3\xc0\xf3\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\xe7\xc0\xf7\xc0\x71\x80\x79\x80\x69\x80\x6d\x80\x65\x80'\
b'\x67\x80\x63\x80\xfb\x80\xf9\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x1e\x00\x7f\x80\x73\x80\xe1\xc0\xc0\xc0'\
b'\xc0\xc0\xc0\xc0\xe1\xc0\x73\x80\x7f\x80\x1e\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\xff\x00\xff\x80\x61\xc0'\
b'\x60\xc0\x61\xc0\x7f\x80\x7f\x00\x60\x00\x60\x00\xfc\x00\xfc\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x1e\x00'\
b'\x7f\x80\x73\x80\xe1\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xe1\xc0\x73\x80'\
b'\x7f\x80\x1e\x40\x3f\xc0\x33\x80\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\xff\x00\xff\x80\x61\xc0\x60\xc0\x61\xc0\x7f\x80\x7f\x00'\
b'\x63\x80\x61\xc0\xfc\xe0\xfc\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x1e\xc0\x7f\xc0\x61\xc0\x60\xc0\x7c\x00'\
b'\x3f\x80\x07\xc0\x60\xc0\x70\xc0\x7f\x80\x6f\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\xff\xc0\xff\xc0\xcc\xc0'\
b'\xcc\xc0\xcc\xc0\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80\x7f\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\xf7\xc0'\
b'\xf7\xc0\x61\x80\x61\x80\x61\x80\x61\x80\x61\x80\x61\x80\x73\x80'\
b'\x3f\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x00\x00\xf9\xf0\xf9\xf0\x60\x60\x60\x60\x30\xc0\x30\xc0\x19\x80'\
b'\x19\x80\x0f\x00\x0f\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\xf9\xf0\xf9\xf0\x60\x60\x66\x60\x66\x60'\
b'\x6f\x60\x6f\x60\x39\xc0\x39\xc0\x30\xc0\x30\xc0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\xf3\xc0\xf3\xc0\x61\x80'\
b'\x33\x00\x1e\x00\x0c\x00\x1e\x00\x33\x00\x61\x80\xf3\xc0\xf3\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\xf3\xc0'\
b'\xf3\xc0\x61\x80\x33\x00\x3f\x00\x1e\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x3f\x00\x3f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x7f\x80\x7f\x80\x63\x80\x67\x00\x06\x00\x0c\x00\x18\x00'\
b'\x39\x80\x71\x80\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x0f\x00\x0f\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0f\x00'\
b'\x0f\x00\x00\x00\x0b\x00\x60\x00\x60\x00\x30\x00\x30\x00\x18\x00'\
b'\x18\x00\x0c\x00\x0c\x00\x06\x00\x06\x00\x03\x00\x03\x00\x01\x80'\
b'\x01\x80\x00\xc0\x00\xc0\x00\x00\x0b\x00\x00\x00\x3c\x00\x3c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x3c\x00\x3c\x00\x00\x00\x0b\x00\x00\x00'\
b'\x0c\x00\x1e\x00\x1e\x00\x33\x00\x33\x00\x61\x80\x61\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xe0\xff\xe0'\
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
 
