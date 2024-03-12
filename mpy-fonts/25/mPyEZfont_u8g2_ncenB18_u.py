'''
    mPyEZfont_u8g2_ncenB18_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenB18.bdf font file was sourced from the U8G2 project:
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
# Font: ncenB18.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/u-char.set u8g2/tools/font/bdf/ncenB18.bdf 0 tmp_mPyEZfont_u8g2_ncenB18_u.py
version = '0.33'

def height():
    return 25

def baseline():
    return 20

def max_width():
    return 26

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
b'\x0d\x00\x00\x00\x00\x00\x1f\x80\x31\xe0\x78\xf0\x78\xf0\x30\xf0'\
b'\x00\xf0\x00\xe0\x01\xc0\x03\x80\x06\x00\x0c\x00\x0c\x00\x00\x00'\
b'\x00\x00\x0e\x00\x1f\x00\x1f\x00\x0e\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07'\
b'\x00\x00\x00\x38\x7c\x7c\x7c\x38\x38\x38\x38\x38\x38\x10\x10\x00'\
b'\x00\x38\x7c\x7c\x38\x00\x00\x00\x00\x00\x08\x00\x00\x00\x66\x66'\
b'\x66\x66\x66\x44\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x06\x60\x06\x60\x06'\
b'\x60\x06\x60\x06\x60\x3f\xf8\x3f\xf8\x0c\xc0\x0c\xc0\x0c\xc0\x0c'\
b'\xc0\x7f\xf0\x7f\xf0\x19\x80\x19\x80\x19\x80\x19\x80\x19\x80\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x02\x00\x02\x00\x0f'\
b'\xe0\x3a\x30\x32\x78\x72\x78\x72\x78\x7a\x30\x7e\x00\x7f\x80\x3f'\
b'\xe0\x0f\xf0\x03\xf8\x02\xf8\x32\x78\x7a\x38\x7a\x38\x7a\x30\x32'\
b'\x70\x1f\xc0\x02\x00\x02\x00\x02\x00\x00\x00\x00\x00\x15\x00\x00'\
b'\x00\x00\x00\x00\x00\x0f\x07\x00\x3d\x9b\x00\x38\xe6\x00\x78\x86'\
b'\x00\x70\x8c\x00\x71\x0c\x00\x71\x18\x00\x32\x18\x00\x1c\x30\x00'\
b'\x00\x31\xe0\x00\x67\xb0\x00\x67\x10\x00\xcf\x10\x00\xce\x10\x01'\
b'\x8e\x20\x01\x8e\x20\x03\x06\x40\x03\x03\x80\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\xf8\x00\x03\x9c\x00\x07\x0c\x00\x07\x0c\x00\x07\x0c'\
b'\x00\x07\x98\x00\x07\xf0\x00\x03\xe0\x00\x07\xe0\x00\x1c\xf1\xf8'\
b'\x38\xf8\xe0\x78\x78\xc0\x78\x3c\x80\x78\x3f\x80\x78\x1f\x08\x3c'\
b'\x0f\x88\x3e\x1f\xf0\x0f\xe3\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x30\x30\x30\x30\x30'\
b'\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x00\x00\x02\x06\x0c\x18\x18\x30\x30\x70\x70\x70'\
b'\x70\x70\x70\x70\x30\x30\x18\x18\x0c\x06\x02\x00\x00\x08\x00\x00'\
b'\x00\x40\x60\x30\x18\x18\x0c\x0c\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0c'\
b'\x0c\x18\x18\x30\x60\x40\x00\x00\x0b\x00\x00\x00\x00\x00\x0e\x00'\
b'\x0e\x00\x64\xc0\x75\xc0\x1f\x00\x1f\x00\x75\xc0\x64\xc0\x0e\x00'\
b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x7f\xf8\x7f\xf8\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x38\x7c\x7c\x3c\x18\x10\x20\x40\x00\x08\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7e\x7e\x7e\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x7c\x7c\x38\x00\x00\x00\x00'\
b'\x00\x09\x00\x00\x00\x00\x00\x03\x00\x03\x00\x03\x00\x06\x00\x06'\
b'\x00\x06\x00\x0c\x00\x0c\x00\x0c\x00\x18\x00\x18\x00\x18\x00\x30'\
b'\x00\x30\x00\x30\x00\x60\x00\x60\x00\x60\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x07\x80\x1c\xe0\x38'\
b'\x70\x38\x70\x78\x78\x78\x78\x78\x78\x78\x78\x78\x78\x78\x78\x78'\
b'\x78\x78\x78\x78\x78\x78\x78\x38\x70\x38\x70\x1c\xe0\x07\x80\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x07'\
b'\x80\x3f\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07'\
b'\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x0f'\
b'\xc0\x3f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00'\
b'\x00\x00\x00\x0f\x80\x31\xe0\x70\xf0\x78\xf0\x78\xf0\x78\xf0\x30'\
b'\xf0\x00\xe0\x01\xe0\x01\xc0\x03\x80\x07\x00\x0c\x10\x18\x10\x38'\
b'\x30\x7f\xf0\x7f\xf0\x7f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x0e\x00\x00\x00\x00\x00\x07\xc0\x18\xf0\x38\x70\x3c\x78\x3c'\
b'\x78\x3c\x78\x18\x70\x00\xe0\x07\x80\x00\xe0\x00\x70\x30\x78\x78'\
b'\x78\x78\x78\x78\x78\x70\x70\x30\xf0\x0f\xc0\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x60\x00\xe0\x01'\
b'\xe0\x03\xe0\x03\xe0\x07\xe0\x0d\xe0\x09\xe0\x19\xe0\x31\xe0\x31'\
b'\xe0\x61\xe0\x7f\xf8\x7f\xf8\x01\xe0\x01\xe0\x01\xe0\x07\xf8\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x3f'\
b'\xf8\x3f\xf0\x3f\xe0\x20\x00\x20\x00\x20\x00\x2f\x80\x38\xe0\x30'\
b'\x70\x00\x78\x00\x78\x00\x78\x30\x78\x78\x78\x78\x78\x78\x70\x30'\
b'\xe0\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00'\
b'\x00\x00\x00\x07\xc0\x1c\x60\x38\xf0\x38\xf0\x78\xf0\x78\x60\x78'\
b'\x00\x7b\xc0\x7c\xf0\x78\x70\x78\x78\x78\x78\x78\x78\x78\x78\x78'\
b'\x78\x38\x70\x3c\xf0\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x0e\x00\x00\x00\x00\x00\x7f\xf8\x7f\xf8\x7f\xf0\x60\x30\x40'\
b'\x60\x40\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x80\x07\x80\x0f'\
b'\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x06\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x07\x80\x1c\xe0\x38'\
b'\x70\x38\x70\x38\x70\x3c\x70\x3e\x60\x1f\xc0\x0f\xc0\x1f\xe0\x3b'\
b'\xf0\x70\xf8\x70\x78\x70\x38\x70\x38\x70\x30\x38\x60\x0f\xc0\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x0f'\
b'\xc0\x3c\xf0\x38\x70\x78\x78\x78\x78\x78\x78\x78\x78\x78\x78\x38'\
b'\x78\x3c\xf8\x0f\x78\x00\x78\x18\x78\x3c\x78\x3c\x70\x3c\x70\x18'\
b'\xe0\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x38\x7c\x7c\x38\x00\x00\x00\x00\x38'\
b'\x7c\x7c\x38\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x38\x7c\x7c\x38\x00\x00\x00\x00\x38\x7c\x7c\x3c\x18\x10'\
b'\x20\x40\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x18\x00\x78\x01\xe0\x07\x80\x1e\x00\x78\x00\x78'\
b'\x00\x1e\x00\x07\x80\x01\xe0\x00\x78\x00\x18\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf8\x7f'\
b'\xf8\x00\x00\x00\x00\x7f\xf8\x7f\xf8\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00\x78\x00\x1e'\
b'\x00\x07\x80\x01\xe0\x00\x78\x00\x78\x01\xe0\x07\x80\x1e\x00\x78'\
b'\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d'\
b'\x00\x00\x00\x00\x00\x1f\x80\x31\xe0\x78\xf0\x78\xf0\x30\xf0\x00'\
b'\xf0\x00\xe0\x01\xc0\x03\x80\x06\x00\x0c\x00\x0c\x00\x00\x00\x00'\
b'\x00\x0e\x00\x1f\x00\x1f\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\xfe\x00\x07\x83'\
b'\x00\x06\x00\xc0\x18\x00\x60\x18\x6e\x60\x31\xde\x30\x33\x8e\x30'\
b'\x63\x8e\x30\x67\x0e\x30\x67\x1c\x30\x67\x1c\x20\x67\x1c\x60\x67'\
b'\x3c\xc0\x33\xdf\x80\x30\x00\x00\x1c\x00\x80\x0e\x03\x80\x03\xfe'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00\x00\x60\x00\x00\xf0'\
b'\x00\x00\xf0\x00\x01\x78\x00\x01\x78\x00\x03\x3c\x00\x02\x3c\x00'\
b'\x02\x3c\x00\x06\x1e\x00\x04\x1e\x00\x07\xfe\x00\x0c\x0f\x00\x08'\
b'\x0f\x00\x08\x0f\x00\x18\x07\x80\x38\x07\x80\xfe\x1f\xe0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00'\
b'\x00\x00\x00\x00\x00\x7f\xfc\x00\x1e\x1f\x00\x1e\x0f\x80\x1e\x0f'\
b'\x80\x1e\x0f\x80\x1e\x0f\x80\x1e\x0f\x00\x1e\x1e\x00\x1f\xfc\x00'\
b'\x1e\x0f\x00\x1e\x07\x80\x1e\x07\xc0\x1e\x07\xc0\x1e\x07\xc0\x1e'\
b'\x07\xc0\x1e\x07\xc0\x1e\x0f\x80\x7f\xfe\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x00\x00'\
b'\x00\x00\x01\xfc\xc0\x07\x87\xc0\x1e\x01\xc0\x1e\x00\xc0\x3c\x00'\
b'\xc0\x3c\x00\x40\x7c\x00\x40\x7c\x00\x00\x7c\x00\x00\x7c\x00\x00'\
b'\x7c\x00\x00\x7c\x00\x00\x3c\x00\x40\x3c\x00\x40\x1e\x00\x80\x1e'\
b'\x00\x80\x07\x83\x00\x01\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x7f'\
b'\xf8\x00\x1e\x1e\x00\x1e\x07\x80\x1e\x07\x80\x1e\x03\xc0\x1e\x03'\
b'\xc0\x1e\x03\xe0\x1e\x03\xe0\x1e\x03\xe0\x1e\x03\xe0\x1e\x03\xe0'\
b'\x1e\x03\xe0\x1e\x03\xc0\x1e\x03\xc0\x1e\x07\x80\x1e\x07\x80\x1e'\
b'\x1e\x00\x7f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x7f\xff\x00\x1e'\
b'\x0f\x00\x1e\x03\x00\x1e\x01\x00\x1e\x01\x00\x1e\x11\x00\x1e\x10'\
b'\x00\x1e\x30\x00\x1f\xf0\x00\x1e\x30\x00\x1e\x10\x00\x1e\x10\x00'\
b'\x1e\x01\x00\x1e\x01\x00\x1e\x01\x00\x1e\x03\x00\x1e\x0f\x00\x7f'\
b'\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x11\x00\x00\x00\x00\x00\x00\x00\x7f\xff\x00\x1e\x0f\x00\x1e'\
b'\x03\x00\x1e\x01\x00\x1e\x01\x00\x1e\x11\x00\x1e\x10\x00\x1e\x30'\
b'\x00\x1f\xf0\x00\x1e\x30\x00\x1e\x10\x00\x1e\x10\x00\x1e\x00\x00'\
b'\x1e\x00\x00\x1e\x00\x00\x1e\x00\x00\x1e\x00\x00\x7f\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00'\
b'\x00\x00\x00\x00\x00\x00\x01\xfc\xc0\x07\x87\xc0\x1e\x01\xc0\x1e'\
b'\x00\xc0\x3c\x00\xc0\x3c\x00\x40\x7c\x00\x40\x7c\x00\x00\x7c\x00'\
b'\x00\x7c\x00\x00\x7c\x07\xe0\x7c\x03\xc0\x3c\x03\xc0\x3c\x03\xc0'\
b'\x1e\x03\xc0\x1e\x03\xc0\x07\x86\xc0\x01\xfc\x40\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x00\x00\x00\x00'\
b'\x00\x00\x00\x7f\x8f\xf0\x1e\x03\xc0\x1e\x03\xc0\x1e\x03\xc0\x1e'\
b'\x03\xc0\x1e\x03\xc0\x1e\x03\xc0\x1e\x03\xc0\x1f\xff\xc0\x1e\x03'\
b'\xc0\x1e\x03\xc0\x1e\x03\xc0\x1e\x03\xc0\x1e\x03\xc0\x1e\x03\xc0'\
b'\x1e\x03\xc0\x1e\x03\xc0\x7f\x8f\xf0\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x7f\x80'\
b'\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00'\
b'\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00'\
b'\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\x00\x00\x03\xfc\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0'\
b'\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x60\xf0\xf0\xf0\xf0\xf0\xe0\xf0'\
b'\xc0\xe0\x61\xe0\x3f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x15\x00\x00\x00\x00\x00\x00\x00\x7f\x87\xe0\x1e\x01\x80\x1e\x03'\
b'\x00\x1e\x06\x00\x1e\x0c\x00\x1e\x18\x00\x1e\x30\x00\x1e\x70\x00'\
b'\x1e\xf8\x00\x1f\xfc\x00\x1f\x7c\x00\x1e\x3e\x00\x1e\x1f\x00\x1e'\
b'\x0f\x80\x1e\x0f\x80\x1e\x07\xc0\x1e\x03\xe0\x7f\x87\xf8\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00'\
b'\x00\x00\x00\x00\x00\x7f\x80\x00\x1e\x00\x00\x1e\x00\x00\x1e\x00'\
b'\x00\x1e\x00\x00\x1e\x00\x00\x1e\x00\x00\x1e\x00\x00\x1e\x00\x00'\
b'\x1e\x00\x00\x1e\x00\x00\x1e\x00\x00\x1e\x01\x00\x1e\x01\x00\x1e'\
b'\x01\x00\x1e\x03\x00\x1e\x0f\x00\x7f\xff\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00'\
b'\x00\x00\x7e\x00\xfe\x1e\x00\xf8\x1f\x01\xf8\x1f\x01\x78\x17\x01'\
b'\x78\x17\x83\x78\x13\x82\x78\x13\xc2\x78\x13\xc6\x78\x11\xc4\x78'\
b'\x11\xe4\x78\x11\xec\x78\x10\xe8\x78\x10\xf8\x78\x10\x70\x78\x10'\
b'\x70\x78\x38\x30\x78\x7c\x21\xfe\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00\x7e'\
b'\x03\xf8\x1f\x00\xe0\x0f\x80\x40\x0f\xc0\x40\x0f\xe0\x40\x0b\xf0'\
b'\x40\x09\xf8\x40\x08\xf8\x40\x08\x7c\x40\x08\x3e\x40\x08\x3f\x40'\
b'\x08\x1f\xc0\x08\x0f\xc0\x08\x07\xc0\x08\x03\xc0\x08\x01\xc0\x1c'\
b'\x00\xc0\x7f\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x15\x00\x00\x00\x00\x00\x00\x00\x01\xfc\x00\x07'\
b'\x8f\x00\x1e\x03\xc0\x1e\x03\xc0\x3c\x01\xe0\x3c\x01\xe0\x7c\x01'\
b'\xf0\x7c\x01\xf0\x7c\x01\xf0\x7c\x01\xf0\x7c\x01\xf0\x7c\x01\xf0'\
b'\x3c\x01\xe0\x3c\x01\xe0\x1e\x03\xc0\x1e\x03\xc0\x07\x8f\x00\x01'\
b'\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x12\x00\x00\x00\x00\x00\x00\x00\x7f\xfe\x00\x1e\x0f\x80\x1e'\
b'\x07\x80\x1e\x07\xc0\x1e\x07\xc0\x1e\x07\xc0\x1e\x07\xc0\x1e\x07'\
b'\x80\x1e\x0f\x80\x1f\xfc\x00\x1e\x00\x00\x1e\x00\x00\x1e\x00\x00'\
b'\x1e\x00\x00\x1e\x00\x00\x1e\x00\x00\x1e\x00\x00\x7f\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x00'\
b'\x00\x00\x00\x00\x00\x00\x01\xfc\x00\x07\x8f\x00\x1e\x03\xc0\x1e'\
b'\x03\xc0\x3c\x01\xe0\x3c\x01\xe0\x7c\x01\xf0\x7c\x01\xf0\x7c\x01'\
b'\xf0\x7c\x01\xf0\x7c\x01\xf0\x7d\xf1\xf0\x3f\x39\xe0\x3e\x19\xe0'\
b'\x1e\x19\xc0\x1e\x0d\xc0\x07\x8f\x00\x01\xff\x00\x00\x07\x00\x00'\
b'\x07\x90\x00\x03\xe0\x00\x03\xe0\x00\x01\xc0\x15\x00\x00\x00\x00'\
b'\x00\x00\x00\x7f\xfc\x00\x1e\x1f\x00\x1e\x0f\x80\x1e\x0f\x80\x1e'\
b'\x0f\x80\x1e\x0f\x80\x1e\x0f\x00\x1e\x1e\x00\x1f\xf0\x00\x1e\x3c'\
b'\x00\x1e\x1e\x00\x1e\x1e\x00\x1e\x1f\x00\x1e\x0f\x00\x1e\x0f\x90'\
b'\x1e\x07\x90\x1e\x07\xe0\x7f\xc3\xc0\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x07\xe4'\
b'\x1c\x3c\x30\x0c\x70\x0c\x70\x04\x78\x04\x7f\x00\x7f\xe0\x3f\xf8'\
b'\x1f\xfc\x07\xfe\x00\xfe\x40\x1e\x40\x0e\x60\x0e\x60\x0c\x78\x38'\
b'\x4f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00'\
b'\x00\x00\x00\x00\x7f\xff\x80\x71\xe3\x80\x61\xe1\x80\x41\xe0\x80'\
b'\x41\xe0\x80\x41\xe0\x80\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01'\
b'\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0'\
b'\x00\x01\xe0\x00\x01\xe0\x00\x07\xf8\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x00\x00\x00\x00\x00\x00'\
b'\x00\x7f\x87\xf0\x1e\x01\xc0\x1e\x00\x80\x1e\x00\x80\x1e\x00\x80'\
b'\x1e\x00\x80\x1e\x00\x80\x1e\x00\x80\x1e\x00\x80\x1e\x00\x80\x1e'\
b'\x00\x80\x1e\x00\x80\x1e\x00\x80\x1e\x00\x80\x1e\x01\x00\x0f\x01'\
b'\x00\x0f\xc6\x00\x03\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\xff\x0f'\
b'\xe0\x3c\x03\x80\x3c\x03\x00\x1e\x02\x00\x1e\x02\x00\x1e\x06\x00'\
b'\x0f\x04\x00\x0f\x04\x00\x0f\x0c\x00\x07\x88\x00\x07\x88\x00\x07'\
b'\x98\x00\x03\xd0\x00\x03\xd0\x00\x01\xe0\x00\x01\xe0\x00\x00\xc0'\
b'\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x7f\x9f'\
b'\xc0\x3c\x1e\x07\x00\x3c\x1e\x06\x00\x1e\x0f\x04\x00\x1e\x0f\x04'\
b'\x00\x1e\x0f\x0c\x00\x0f\x1f\x88\x00\x0f\x17\x88\x00\x0f\x17\x98'\
b'\x00\x07\xb3\xd0\x00\x07\xa3\xd0\x00\x07\xa3\xf0\x00\x03\xe1\xe0'\
b'\x00\x03\xc1\xe0\x00\x03\xc1\xe0\x00\x01\xc0\xc0\x00\x01\x80\xc0'\
b'\x00\x01\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00'\
b'\x00\xff\x87\xe0\x3e\x01\x80\x1f\x03\x00\x1f\x86\x00\x0f\x8c\x00'\
b'\x07\xd8\x00\x03\xf0\x00\x03\xe0\x00\x01\xf0\x00\x00\xf8\x00\x01'\
b'\xf8\x00\x03\x7c\x00\x06\x3e\x00\x04\x1f\x00\x0c\x1f\x00\x18\x0f'\
b'\x80\x30\x07\xc0\xfc\x1f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\xff\x0f'\
b'\xc0\x3c\x03\x00\x1e\x02\x00\x1e\x06\x00\x0f\x04\x00\x0f\x0c\x00'\
b'\x07\x88\x00\x07\x98\x00\x03\xd0\x00\x03\xf0\x00\x01\xe0\x00\x01'\
b'\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0'\
b'\x00\x07\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x3f\xff\x00\x38\x1f'\
b'\x00\x30\x3e\x00\x20\x3c\x00\x20\x7c\x00\x00\x78\x00\x00\xf0\x00'\
b'\x01\xf0\x00\x01\xe0\x00\x03\xc0\x00\x07\xc0\x00\x07\x80\x00\x0f'\
b'\x00\x00\x1f\x01\x00\x1e\x01\x00\x3c\x03\x00\x7c\x07\x00\x7f\xff'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x7e\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70'\
b'\x70\x70\x70\x70\x70\x70\x70\x70\x7e\x00\x00\x0c\x00\x00\x00\x00'\
b'\x00\x60\x00\x70\x00\x70\x00\x38\x00\x38\x00\x1c\x00\x1c\x00\x0e'\
b'\x00\x0e\x00\x07\x00\x07\x00\x03\x80\x03\x80\x01\xc0\x01\xc0\x00'\
b'\xe0\x00\xe0\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08'\
b'\x00\x00\x00\x7e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'\
b'\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x7e\x00\x00\x0f\x00\x00\x00\x00\x00'\
b'\x03\x00\x03\x00\x07\x80\x07\x80\x0c\xc0\x0c\xc0\x18\x60\x18\x60'\
b'\x30\x30\x30\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\xff\xf0\xff\xf0\x00\x00\x00\x00'\
b'\x00\x00'

_index =\
b'\x00\x00\x34\x00\x4f\x00\x6a\x00\x85\x00\xb9\x00\xed\x00\x3a\x01'\
b'\x87\x01\xa2\x01\xbd\x01\xd8\x01\x0c\x02\x40\x02\x5b\x02\x76\x02'\
b'\x91\x02\xc5\x02\xf9\x02\x2d\x03\x61\x03\x95\x03\xc9\x03\xfd\x03'\
b'\x31\x04\x65\x04\x99\x04\xcd\x04\xe8\x04\x03\x05\x37\x05\x6b\x05'\
b'\x9f\x05\xd3\x05\x20\x06\x6d\x06\xba\x06\x07\x07\x54\x07\xa1\x07'\
b'\xee\x07\x3b\x08\x88\x08\xbc\x08\xf0\x08\x3d\x09\x8a\x09\xd7\x09'\
b'\x24\x0a\x71\x0a\xbe\x0a\x0b\x0b\x58\x0b\x8c\x0b\xd9\x0b\x26\x0c'\
b'\x73\x0c\xd9\x0c\x26\x0d\x73\x0d\xc0\x0d\xdb\x0d\x0f\x0e\x2a\x0e'\
b'\x5e\x0e\x92\x0e'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 25
    return _mvfont[doff + 2:next_offs], 25, width
 
