'''
    mPyEZfont_u8g2_helvB18_r.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original helvB18.bdf font file was sourced from the U8G2 project:
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
# Font: helvB18.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/r-char.set u8g2/tools/font/bdf/helvB18.bdf 0 tmp_mPyEZfont_u8g2_helvB18_r.py
version = '0.33'

def height():
    return 24

def baseline():
    return 19

def max_width():
    return 24

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 126

_font =\
b'\x0f\x00\x07\xe0\x1f\xf0\x1e\x78\x3c\x38\x38\x38\x38\x78\x00\x70'\
b'\x00\xf0\x01\xe0\x01\xc0\x03\x80\x03\x80\x03\x80\x03\x80\x00\x00'\
b'\x00\x00\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\x38\x38\x38\x30\x30\x30\x00\x00\x38\x38'\
b'\x38\x00\x00\x00\x00\x00\x09\x00\x36\x00\x36\x00\x36\x00\x36\x00'\
b'\x36\x00\x24\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x06\x60\x06\x60'\
b'\x06\x60\x06\x60\x06\x60\x3f\xf8\x3f\xf8\x0c\xc0\x0c\xc0\x0c\xc0'\
b'\x0c\xc0\x7f\xf0\x7f\xf0\x19\x80\x19\x80\x19\x80\x19\x80\x19\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x06\x00\x3f\x80'\
b'\x7f\xe0\xf6\xe0\xe6\x70\xe6\x70\xf6\x00\x7e\x00\x3e\x00\x0f\x00'\
b'\x07\xc0\x07\xe0\x06\xf0\xe6\x70\xe6\x70\xe6\x70\xf6\xf0\x7f\xe0'\
b'\x1f\xc0\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00'\
b'\x00\x00\x07\x00\x3e\x07\x00\x7f\x0e\x00\xe3\x8e\x00\xc1\x9c\x00'\
b'\xc1\x9c\x00\xe3\xb8\x00\x7f\x38\x00\x3e\x70\x00\x00\x70\x00\x00'\
b'\xe3\xe0\x00\xe7\xf0\x01\xce\x38\x01\xcc\x18\x03\x8c\x18\x03\x8e'\
b'\x38\x07\x07\xf0\x07\x03\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00\x07\xc0\x00\x0f\xe0'\
b'\x00\x1e\xf0\x00\x1c\x70\x00\x1c\x70\x00\x1c\x70\x00\x0e\xe0\x00'\
b'\x07\xc0\x00\x0f\x80\x00\x1f\xce\x00\x3d\xee\x00\x38\xfe\x00\x70'\
b'\x7c\x00\x70\x38\x00\x70\x7c\x00\x78\xfe\x00\x3f\xe7\x00\x0f\xc3'\
b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x30\x30\x30\x30\x30\x20\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x06\x0e\x1c\x1c'\
b'\x38\x38\x30\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x30\x38\x38'\
b'\x1c\x1c\x0e\x06\x08\x00\x60\x70\x38\x38\x1c\x1c\x0c\x0e\x0e\x0e'\
b'\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0c\x1c\x1c\x38\x38\x70\x60\x0a\x00'\
b'\x0c\x00\x0c\x00\x6d\x80\x7f\x80\x1e\x00\x33\x00\x33\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x7f\xf8\x7f\xf8\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x38\x38\x38\x18\x18\x30\x00\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xfe\xfe\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x38\x38\x00\x00\x00\x00\x00'\
b'\x08\x00\x03\x03\x03\x06\x06\x06\x0c\x0c\x0c\x0c\x18\x18\x18\x30'\
b'\x30\x30\x60\x60\x60\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x1f\x80'\
b'\x3f\xc0\x79\xe0\x70\xe0\x70\xe0\xe0\x70\xe0\x70\xe0\x70\xe0\x70'\
b'\xe0\x70\xe0\x70\xe0\x70\xe0\x70\x70\xe0\x70\xe0\x79\xe0\x3f\xc0'\
b'\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00'\
b'\x03\x80\x03\x80\x07\x80\x3f\x80\x3f\x80\x03\x80\x03\x80\x03\x80'\
b'\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80'\
b'\x03\x80\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00'\
b'\x00\x00\x1f\x00\x7f\xc0\x71\xe0\xe0\xe0\xe0\x70\xe0\x70\x00\x70'\
b'\x00\xe0\x01\xe0\x03\xc0\x07\x80\x1f\x00\x3c\x00\x78\x00\xf0\x00'\
b'\xe0\x00\xff\xf0\xff\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x1f\x00\x7f\xc0\x71\xc0\xe0\xe0\xe0\xe0\xe0\xe0'\
b'\x00\xe0\x01\xc0\x0f\x80\x0f\xe0\x00\xe0\x00\x70\x00\x70\xe0\x70'\
b'\xe0\xf0\x71\xe0\x7f\xe0\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0d\x00\x00\x00\x01\xc0\x03\xc0\x03\xc0\x07\xc0\x07\xc0'\
b'\x0d\xc0\x1d\xc0\x19\xc0\x31\xc0\x71\xc0\x61\xc0\xe1\xc0\xff\xf0'\
b'\xff\xf0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0d\x00\x00\x00\x7f\xe0\x7f\xe0\x70\x00\x70\x00'\
b'\x70\x00\x70\x00\x7f\x80\x7f\xc0\x71\xe0\x00\xe0\x00\x70\x00\x70'\
b'\x00\x70\xe0\x70\xe0\xf0\xf1\xe0\x7f\xc0\x1f\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x0f\x80\x3f\xe0\x78\xe0'\
b'\x70\x70\xe0\x70\xe0\x00\xe0\x00\xef\x00\xff\xc0\xf9\xe0\xf0\xe0'\
b'\xe0\x70\xe0\x70\xe0\x70\x70\xe0\x79\xe0\x3f\xc0\x1f\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\xff\xf0\xff\xf0'\
b'\x00\xf0\x00\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x07\x00'\
b'\x0e\x00\x0e\x00\x1e\x00\x1c\x00\x1c\x00\x3c\x00\x38\x00\x38\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x0f\x00'\
b'\x3f\xc0\x39\xc0\x70\xe0\x70\xe0\x70\xe0\x70\xe0\x39\xc0\x1f\x80'\
b'\x3f\xc0\x70\xe0\xe0\x70\xe0\x70\xe0\x70\xe0\x70\x70\xe0\x7f\xe0'\
b'\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00'\
b'\x1f\x80\x7f\xc0\x79\xe0\xf0\xe0\xe0\x70\xe0\x70\xe0\x70\xe0\x70'\
b'\xf0\xf0\x79\xf0\x7f\xf0\x1f\x70\x00\x70\x00\x70\xe0\xe0\xf3\xe0'\
b'\x7f\xc0\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'\
b'\x00\x00\x00\x00\x00\x38\x38\x38\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x38\x38\x38\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x38'\
b'\x38\x38\x00\x00\x00\x00\x00\x00\x00\x00\x38\x38\x38\x18\x18\x30'\
b'\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x38\x00\xf8\x03\xe0\x0f\x80\x3e\x00\xf0\x00\xf0\x00\x3e\x00'\
b'\x0f\x80\x03\xe0\x00\xf8\x00\x38\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xf0\x3f\xf0\x00\x00\x3f\xf0'\
b'\x3f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x70\x00\x7c\x00\x1f\x00\x07\xc0\x01\xf0\x00\x3c'\
b'\x00\x3c\x01\xf0\x07\xc0\x1f\x00\x7c\x00\x70\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x07\xe0\x1f\xf0\x1e\x78'\
b'\x3c\x38\x38\x38\x38\x78\x00\x70\x00\xf0\x01\xe0\x01\xc0\x03\x80'\
b'\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x03\x80\x03\x80\x03\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00'\
b'\xff\x80\x03\xff\xe0\x07\xc0\xf8\x0f\x00\x3c\x1e\x00\x1c\x3c\x3e'\
b'\xce\x38\x7f\xce\x78\xe3\x8e\x71\xc3\x8e\x71\x87\x0e\x73\x87\x1c'\
b'\x73\x86\x1c\x73\x8e\x38\x73\x8e\x38\x71\xce\xf0\x79\xff\xe0\x38'\
b'\xfb\x80\x3c\x00\x00\x1e\x00\x00\x0f\x83\x80\x07\xff\x80\x01\xfe'\
b'\x00\x00\x00\x00\x12\x00\x01\xe0\x00\x01\xe0\x00\x03\xf0\x00\x03'\
b'\xf0\x00\x07\x30\x00\x07\x38\x00\x07\x38\x00\x0e\x1c\x00\x0e\x1c'\
b'\x00\x0e\x1c\x00\x1c\x0e\x00\x1c\x0e\x00\x1f\xfe\x00\x3f\xff\x00'\
b'\x38\x07\x00\x38\x07\x00\x70\x03\x80\x70\x03\x80\x70\x03\x80\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00'\
b'\x3f\xf8\x00\x3f\xfe\x00\x38\x1e\x00\x38\x07\x00\x38\x07\x00\x38'\
b'\x07\x00\x38\x07\x00\x38\x0e\x00\x3f\xfc\x00\x3f\xfe\x00\x38\x07'\
b'\x00\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38\x07\x80'\
b'\x38\x1f\x00\x3f\xfe\x00\x3f\xf8\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x03\xf8\x00\x0f\xfe\x00'\
b'\x1f\x1f\x00\x3c\x07\x80\x38\x03\x80\x78\x00\x00\x70\x00\x00\x70'\
b'\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00'\
b'\x00\x78\x03\x80\x38\x03\x80\x3c\x07\x80\x1f\x1f\x00\x0f\xfe\x00'\
b'\x03\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x13\x00\x3f\xf8\x00\x3f\xfe\x00\x38\x1f\x00\x38\x07\x80'\
b'\x38\x03\x80\x38\x03\xc0\x38\x01\xc0\x38\x01\xc0\x38\x01\xc0\x38'\
b'\x01\xc0\x38\x01\xc0\x38\x01\xc0\x38\x01\xc0\x38\x03\xc0\x38\x03'\
b'\x80\x38\x07\x80\x38\x1f\x00\x3f\xfe\x00\x3f\xf8\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x3f\xfc'\
b'\x3f\xfc\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xf8'\
b'\x3f\xf8\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
b'\x3f\xfe\x3f\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00'\
b'\x3f\xfc\x3f\xfc\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
b'\x3f\xf8\x3f\xf8\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x03\xf8\x00\x0f\xfe\x00\x1f\x1f\x00\x3c\x07\x80\x38\x03'\
b'\x80\x78\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x3f\xc0'\
b'\x70\x3f\xc0\x70\x01\xc0\x70\x01\xc0\x78\x01\xc0\x38\x03\xc0\x3c'\
b'\x07\xc0\x1f\x1f\xc0\x0f\xfd\xc0\x03\xf9\xc0\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x38\x03\x80\x38'\
b'\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03'\
b'\x80\x38\x03\x80\x3f\xff\x80\x3f\xff\x80\x38\x03\x80\x38\x03\x80'\
b'\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38'\
b'\x03\x80\x38\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x07\x00\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\x38\x38\x38\x00\x00\x00\x00\x00\x0e\x00'\
b'\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70'\
b'\x00\x70\x00\x70\x00\x70\x00\x70\x70\x70\x70\x70\x70\x70\x70\x70'\
b'\x38\xf0\x3f\xe0\x1f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x12\x00\x38\x0f\x00\x38\x1e\x00\x38\x3c\x00\x38\x78\x00\x38\xf0'\
b'\x00\x39\xe0\x00\x3b\xc0\x00\x3f\x80\x00\x3f\x80\x00\x3f\xc0\x00'\
b'\x3d\xe0\x00\x38\xe0\x00\x38\x70\x00\x38\x78\x00\x38\x38\x00\x38'\
b'\x1c\x00\x38\x1e\x00\x38\x0e\x00\x38\x0f\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xfc'\
b'\x3f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00\x38\x00'\
b'\x38\x3c\x00\x78\x3c\x00\x78\x3e\x00\xf8\x3e\x00\xf8\x3f\x01\xf8'\
b'\x3b\x01\xb8\x3b\x83\xb8\x39\x83\x38\x39\xc7\x38\x39\xc7\x38\x38'\
b'\xc6\x38\x38\xee\x38\x38\xee\x38\x38\x7c\x38\x38\x7c\x38\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x13\x00\x38\x03\x80\x3c\x03\x80\x3c\x03'\
b'\x80\x3e\x03\x80\x3e\x03\x80\x3f\x03\x80\x3b\x83\x80\x3b\x83\x80'\
b'\x39\xc3\x80\x38\xe3\x80\x38\xe3\x80\x38\x73\x80\x38\x33\x80\x38'\
b'\x3b\x80\x38\x1f\x80\x38\x0f\x80\x38\x0f\x80\x38\x07\x80\x38\x03'\
b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x03\xf8\x00\x0f\xfe\x00\x1f\x1f\x00\x3c\x07\x80\x38\x03'\
b'\x80\x78\x03\xc0\x70\x01\xc0\x70\x01\xc0\x70\x01\xc0\x70\x01\xc0'\
b'\x70\x01\xc0\x70\x01\xc0\x70\x01\xc0\x78\x03\xc0\x38\x03\x80\x3c'\
b'\x07\x80\x1f\x1f\x00\x0f\xfe\x00\x03\xf8\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x3f\xf8\x00\x3f'\
b'\xfe\x00\x38\x0e\x00\x38\x07\x00\x38\x07\x00\x38\x07\x00\x38\x07'\
b'\x00\x38\x0e\x00\x3f\xfe\x00\x3f\xfc\x00\x38\x00\x00\x38\x00\x00'\
b'\x38\x00\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00\x38'\
b'\x00\x00\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x13\x00\x03\xf8\x00\x0f\xfe\x00\x1f\x1f\x00\x3c'\
b'\x07\x80\x38\x03\x80\x78\x03\xc0\x70\x01\xc0\x70\x01\xc0\x70\x01'\
b'\xc0\x70\x01\xc0\x70\x01\xc0\x70\x01\xc0\x70\x01\xc0\x78\x13\xc0'\
b'\x38\x3b\x80\x3c\x1f\x80\x1f\x0f\x00\x0f\xff\x00\x03\xfb\x80\x00'\
b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00'\
b'\x3f\xf8\x00\x3f\xfe\x00\x38\x0e\x00\x38\x07\x00\x38\x07\x00\x38'\
b'\x07\x00\x38\x07\x00\x38\x0e\x00\x3f\xfe\x00\x3f\xfc\x00\x38\x1e'\
b'\x00\x38\x0e\x00\x38\x07\x00\x38\x07\x00\x38\x07\x00\x38\x07\x00'\
b'\x38\x07\x00\x38\x07\x00\x38\x07\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x03\xf0\x00\x0f\xfc\x00'\
b'\x1e\x3e\x00\x3c\x0e\x00\x38\x0e\x00\x38\x00\x00\x3c\x00\x00\x1f'\
b'\x00\x00\x0f\xf0\x00\x01\xfc\x00\x00\x3e\x00\x00\x0f\x00\x00\x07'\
b'\x00\x38\x07\x00\x38\x07\x00\x38\x0f\x00\x3e\x3e\x00\x1f\xfc\x00'\
b'\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0f\x00\xff\xfe\xff\xfe\x03\x80\x03\x80\x03\x80\x03\x80'\
b'\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80'\
b'\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x13\x00\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38'\
b'\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03'\
b'\x80\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03\x80'\
b'\x3c\x07\x80\x1c\x07\x00\x1f\x1f\x00\x0f\xfe\x00\x03\xf8\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00'\
b'\x70\x03\x80\x70\x03\x80\x78\x07\x80\x38\x07\x00\x3c\x0f\x00\x1c'\
b'\x0e\x00\x1c\x0e\x00\x1e\x1e\x00\x0e\x1c\x00\x0e\x1c\x00\x0f\x3c'\
b'\x00\x07\x38\x00\x07\x38\x00\x07\x38\x00\x03\xf0\x00\x03\xf0\x00'\
b'\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00\x70\x38\x1c\x70\x38\x1c'\
b'\x70\x38\x1c\x70\x38\x1c\x38\x7c\x38\x38\x7c\x38\x38\x6c\x38\x38'\
b'\xee\x38\x18\xee\x30\x1c\xee\x70\x1c\xc6\x70\x1d\xc7\x70\x0d\xc7'\
b'\x60\x0d\xc7\x60\x0f\x83\xe0\x0f\x83\xe0\x07\x01\xc0\x07\x01\xc0'\
b'\x07\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x12\x00\x70\x03\x80\x78\x07\x80\x3c\x0f\x00\x1c\x0e\x00'\
b'\x0e\x1c\x00\x07\x38\x00\x07\xf8\x00\x03\xf0\x00\x01\xe0\x00\x01'\
b'\xe0\x00\x03\xf0\x00\x07\xf8\x00\x07\x38\x00\x0e\x1c\x00\x1e\x1e'\
b'\x00\x1c\x0e\x00\x38\x07\x00\x78\x07\x80\x70\x03\x80\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x70\x07'\
b'\x00\x78\x07\x00\x38\x0e\x00\x3c\x0e\x00\x1c\x1c\x00\x1e\x1c\x00'\
b'\x0e\x38\x00\x0e\x38\x00\x07\x70\x00\x07\x70\x00\x03\xe0\x00\x03'\
b'\xe0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0'\
b'\x00\x01\xc0\x00\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x10\x00\x7f\xfe\x7f\xfe\x00\x1e\x00\x3c'\
b'\x00\x78\x00\xf0\x00\xf0\x01\xe0\x03\xc0\x03\xc0\x07\x80\x0f\x00'\
b'\x0f\x00\x1e\x00\x1c\x00\x3c\x00\x78\x00\x7f\xfe\x7f\xfe\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x7c\x7c\x70\x70\x70\x70'\
b'\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70'\
b'\x7c\x7c\x08\x00\xc0\xc0\xc0\x60\x60\x60\x30\x30\x30\x30\x18\x18'\
b'\x18\x0c\x0c\x0c\x06\x06\x06\x00\x00\x00\x00\x00\x08\x00\x3e\x3e'\
b'\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'\
b'\x0e\x0e\x0e\x0e\x3e\x3e\x0e\x00\x07\x00\x07\x00\x0f\x80\x0d\x80'\
b'\x1d\xc0\x38\xe0\x38\xe0\x70\x70\x70\x70\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\xff\xfc\xff\xfc\x00\x00\x00\x00\x00\x00\x08\x00\x70\x38\x1c\x0e'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\xc0\x1f\xe0\x38\xf0\x38\x70\x00\x70\x03\xf0\x1f\xf0\x3e\x70'\
b'\x78\x70\x70\x70\x70\xf0\x79\xf0\x3f\xf8\x1f\x38\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0f\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
b'\x38\x00\x3b\xe0\x3f\xf0\x3e\x78\x3c\x38\x38\x1c\x38\x1c\x38\x1c'\
b'\x38\x1c\x38\x1c\x38\x1c\x3c\x38\x3e\x78\x3f\xf0\x3b\xe0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0f\xc0\x1f\xe0\x3c\xf0\x38\x70\x70\x00\x70\x00'\
b'\x70\x00\x70\x00\x70\x00\x70\x00\x38\x70\x3c\xf0\x1f\xe0\x0f\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x38\x00\x38'\
b'\x00\x38\x00\x38\x00\x38\x0f\xb8\x1f\xf8\x3c\xf8\x38\x78\x70\x38'\
b'\x70\x38\x70\x38\x70\x38\x70\x38\x70\x38\x38\x78\x3c\xf8\x1f\xf8'\
b'\x0f\xb8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\x1f\xe0\x3c\xf0\x38\x70'\
b'\x70\x38\x70\x38\x7f\xf8\x7f\xf8\x70\x00\x70\x00\x38\x38\x3c\x78'\
b'\x1f\xf0\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00'\
b'\x0f\x00\x1f\x00\x1c\x00\x1c\x00\x1c\x00\x7f\x00\x7f\x00\x1c\x00'\
b'\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00'\
b'\x1c\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xb8\x1f\xf8'\
b'\x3c\xf8\x38\x78\x70\x38\x70\x38\x70\x38\x70\x38\x70\x38\x70\x38'\
b'\x38\x78\x3c\xf8\x1f\xf8\x0f\xb8\x00\x38\x70\x38\x78\x70\x3f\xf0'\
b'\x0f\xc0\x0f\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3b\xc0'\
b'\x3f\xf0\x3c\x70\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x07\x00\x38\x38\x38\x00\x00\x38\x38\x38\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\x38\x38\x38\x00\x00\x00\x00\x00\x07\x00'\
b'\x38\x38\x38\x00\x00\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\xf8\xf0\x0e\x00\x38\x00\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\x38\x70\x38\xf0\x39\xe0\x3b\xc0\x3f\x80\x3f\x00'\
b'\x3f\x80\x3b\xc0\x39\xc0\x39\xe0\x38\xf0\x38\x70\x38\x78\x38\x38'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x38\x38\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x00'\
b'\x00\x00\x00\x00\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x3b\xcf\x80\x3f\xff\xc0\x3c\xf9\xe0\x38\x70'\
b'\xe0\x38\x70\xe0\x38\x70\xe0\x38\x70\xe0\x38\x70\xe0\x38\x70\xe0'\
b'\x38\x70\xe0\x38\x70\xe0\x38\x70\xe0\x38\x70\xe0\x38\x70\xe0\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3b\xe0\x3f\xf0\x3c\x70'\
b'\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\x1f\xe0'\
b'\x3c\xf0\x38\x70\x70\x38\x70\x38\x70\x38\x70\x38\x70\x38\x70\x38'\
b'\x38\x70\x3c\xf0\x1f\xe0\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3b\xe0'\
b'\x3f\xf0\x3e\x78\x3c\x38\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c'\
b'\x38\x1c\x3c\x38\x3e\x78\x3f\xf0\x3b\xe0\x38\x00\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\xb8\x1f\xf8\x3c\xf8\x38\x78\x70\x38\x70\x38\x70\x38\x70\x38'\
b'\x70\x38\x70\x38\x38\x78\x3c\xf8\x1f\xf8\x0f\xb8\x00\x38\x00\x38'\
b'\x00\x38\x00\x38\x00\x38\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x3b\x80\x3f\x80\x3f\x80\x3c\x00\x38\x00\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x1f\x80\x3f\xc0\x79\xe0\x70\xe0\x70\x00\x7e\x00'\
b'\x3f\xc0\x07\xe0\x00\xf0\x70\x70\x70\x70\x78\xf0\x3f\xe0\x1f\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x1c\x00'\
b'\x1c\x00\x1c\x00\x1c\x00\x7f\x00\x7f\x00\x1c\x00\x1c\x00\x1c\x00'\
b'\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1f\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x78\x1c\xf8'\
b'\x1f\xb8\x07\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\x38\x70\x38\x70\x38'\
b'\x38\x70\x38\x70\x38\x70\x1c\xe0\x1c\xe0\x1c\xe0\x0f\xc0\x0f\xc0'\
b'\x07\x80\x07\x80\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xe0\xe0\xe0\xe0\xe0\xe0\x60\xe0\xc0\x71\xf1\xc0\x71\xf1\xc0'\
b'\x31\xb1\x80\x33\xb9\x80\x3b\xbb\x80\x1b\x1b\x00\x1f\x1f\x00\x1f'\
b'\x1f\x00\x0e\x0e\x00\x0e\x0e\x00\x0e\x0e\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x70\x70\x78\xf0\x38\xe0\x1d\xc0\x1f\xc0'\
b'\x0f\x80\x07\x00\x0f\x80\x0f\x80\x1d\xc0\x3d\xe0\x38\xe0\x78\xf0'\
b'\x70\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x70\x1c\x70\x1c\x38\x1c\x3c\x38'\
b'\x1c\x38\x1e\x78\x0e\x70\x0e\x70\x07\xe0\x07\xe0\x03\xe0\x03\xc0'\
b'\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x1f\x00\x1e\x00\x0d\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf0\x7f\xf0\x00\xe0'\
b'\x01\xc0\x03\xc0\x07\x80\x07\x00\x0f\x00\x1e\x00\x1c\x00\x38\x00'\
b'\x78\x00\x7f\xf0\x7f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x07\x00\x0e\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00'\
b'\x1c\x00\x1c\x00\x1c\x00\x38\x00\x70\x00\x70\x00\x38\x00\x1c\x00'\
b'\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x0e\x00'\
b'\x07\x00\x07\x00\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18'\
b'\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x0a\x00\x38\x00'\
b'\x1c\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00'\
b'\x0e\x00\x07\x00\x03\x80\x03\x80\x07\x00\x0e\x00\x0e\x00\x0e\x00'\
b'\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x1c\x00\x38\x00\x0e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x3c\x70\x7f\x70\x77\xf0\x71\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

_index =\
b'\x00\x00\x32\x00\x4c\x00\x66\x00\x98\x00\xca\x00\xfc\x00\x46\x01'\
b'\x90\x01\xaa\x01\xc4\x01\xde\x01\x10\x02\x42\x02\x5c\x02\x76\x02'\
b'\x90\x02\xaa\x02\xdc\x02\x0e\x03\x40\x03\x72\x03\xa4\x03\xd6\x03'\
b'\x08\x04\x3a\x04\x6c\x04\x9e\x04\xb8\x04\xd2\x04\x04\x05\x36\x05'\
b'\x68\x05\x9a\x05\xe4\x05\x2e\x06\x78\x06\xc2\x06\x0c\x07\x3e\x07'\
b'\x70\x07\xba\x07\x04\x08\x1e\x08\x50\x08\x9a\x08\xcc\x08\x16\x09'\
b'\x60\x09\xaa\x09\xf4\x09\x3e\x0a\x88\x0a\xd2\x0a\x04\x0b\x4e\x0b'\
b'\x98\x0b\xe2\x0b\x2c\x0c\x76\x0c\xa8\x0c\xc2\x0c\xdc\x0c\xf6\x0c'\
b'\x28\x0d\x5a\x0d\x74\x0d\xa6\x0d\xd8\x0d\x0a\x0e\x3c\x0e\x6e\x0e'\
b'\xa0\x0e\xd2\x0e\x04\x0f\x1e\x0f\x38\x0f\x6a\x0f\x84\x0f\xce\x0f'\
b'\x00\x10\x32\x10\x64\x10\x96\x10\xc8\x10\xfa\x10\x2c\x11\x5e\x11'\
b'\x90\x11\xda\x11\x0c\x12\x3e\x12\x70\x12\xa2\x12\xbc\x12\xee\x12'\
b'\x20\x13'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 126 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 24
    return _mvfont[doff + 2:next_offs], 24, width
 
