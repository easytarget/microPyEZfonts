'''
    mPyEZfont_u8g2_ncenB14_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenB14.bdf font file was sourced from the U8G2 project:
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
# Font: ncenB14.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./u-char.set -e 32 ../u8g2/tools/font/bdf/ncenB14.bdf 0 tmp_mPyEZfont_u8g2_ncenB14_u.py
version = '0.33'

def height():
    return 20

def baseline():
    return 16

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
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00'\
b'\x30\x78\x78\x78\x78\x78\x30\x30\x30\x00\x30\x78\x78\x30\x00\x00'\
b'\x00\x00\x08\x00\x00\x00\x6c\x6c\x6c\x6c\x6c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x80\x0d\x80\x0d\x80\x7f\xe0\x7f\xe0\x1b\x00\x1b\x00\xff\xc0'\
b'\xff\xc0\x36\x00\x36\x00\x36\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0b\x00\x04\x00\x04\x00\x1f\x00\x35\xc0\x65\xc0\x64\xc0'\
b'\x74\x00\x7e\x00\x7f\x80\x3f\xc0\x0f\xc0\x05\xc0\x64\xc0\x74\xc0'\
b'\x75\x80\x1f\x00\x04\x00\x04\x00\x00\x00\x00\x00\x0f\x00\x00\x00'\
b'\x00\x00\x38\xc0\x67\x40\xc4\xc0\xc4\x80\xc5\x80\xc9\x00\x73\x00'\
b'\x02\x38\x06\x64\x04\xc4\x0c\xc4\x08\xc4\x18\xc8\x10\x70\x10\x00'\
b'\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x03\xc0'\
b'\x00\x06\x60\x00\x0c\x60\x00\x0c\x60\x00\x0e\xc0\x00\x0f\x80\x00'\
b'\x07\x1f\x00\x1f\x8c\x00\x3b\xc8\x00\x71\xf0\x00\x70\xf0\x00\x70'\
b'\x78\x80\x78\xff\x00\x3f\x8e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x05\x00\x00\x00\x60\x60\x60\x60\x60\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x18\x30'\
b'\x70\x60\xe0\xc0\xc0\xc0\xc0\xc0\xc0\xe0\x60\x70\x30\x18\x00\x00'\
b'\x06\x00\x00\x00\xc0\x60\x70\x30\x38\x18\x18\x18\x18\x18\x18\x38'\
b'\x30\x70\x60\xc0\x00\x00\x08\x00\x00\x00\x38\x92\xd6\x38\xd6\x92'\
b'\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\xff\xc0\xff\xc0\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x60\xf0\xf0\x70\x20\x40\x80\x00\x06\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf8\xf8\x00\x00\x00\x00\x00'\
b'\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x60\xf0\xf0\x60\x00\x00\x00\x00\x07\x00\x00\x00\x0c\x0c\x08\x18'\
b'\x18\x10\x30\x30\x20\x60\x60\x40\xc0\xc0\x00\x00\x00\x00\x0b\x00'\
b'\x00\x00\x00\x00\x0e\x00\x3b\x80\x31\x80\x71\xc0\x71\xc0\x71\xc0'\
b'\x71\xc0\x71\xc0\x71\xc0\x71\xc0\x71\xc0\x31\x80\x3b\x80\x0e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x06\x00'\
b'\x0e\x00\x3e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00'\
b'\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x3f\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0b\x00\x00\x00\x00\x00\x0f\x00\x33\x80\x71\xc0\x71\xc0'\
b'\x31\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x0c\x00\x18\x00\x30\x40'\
b'\x7f\xc0\x7f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x0f\x00\x33\x80\x71\xc0\x71\xc0\x31\xc0\x01\x80\x0e\x00'\
b'\x01\x80\x01\xc0\x31\xc0\x71\xc0\x71\xc0\x33\x80\x1f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x80\x01\x80'\
b'\x03\x80\x07\x80\x07\x80\x0b\x80\x13\x80\x23\x80\x23\x80\x43\x80'\
b'\x7f\xc0\x03\x80\x03\x80\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x3f\xc0\x3f\x80\x20\x00\x20\x00\x20\x00'\
b'\x3f\x00\x23\x80\x01\xc0\x01\xc0\x31\xc0\x71\xc0\x71\xc0\x33\x80'\
b'\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00'\
b'\x0f\x80\x39\xc0\x31\xc0\x71\x80\x70\x00\x77\x00\x7b\x80\x71\xc0'\
b'\x71\xc0\x71\xc0\x71\xc0\x31\xc0\x39\x80\x0e\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x7f\xc0\x7f\xc0\x40\xc0'\
b'\x41\x80\x03\x00\x03\x00\x06\x00\x06\x00\x0e\x00\x0e\x00\x1c\x00'\
b'\x1c\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00'\
b'\x00\x00\x00\x00\x0e\x00\x31\x80\x60\xc0\x60\xc0\x70\xc0\x7d\x80'\
b'\x3f\x00\x1f\x80\x27\xc0\x61\xc0\x60\xc0\x60\xc0\x71\x80\x1e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x0e\x00'\
b'\x33\x80\x71\x80\x71\xc0\x71\xc0\x71\xc0\x71\xc0\x3b\xc0\x1d\xc0'\
b'\x01\xc0\x31\xc0\x71\x80\x73\x80\x3e\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x30\x78\x78\x30\x00'\
b'\x30\x78\x78\x30\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x30\x78\x78\x30\x00\x30\x78\x78\x38\x10\x20\x40\x00\x0b\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x03\xc0'\
b'\x0f\x00\x3c\x00\xf0\x00\xf0\x00\x3c\x00\x0f\x00\x03\xc0\x00\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xc0\x7f\xc0\x00\x00'\
b'\x00\x00\x7f\xc0\x7f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\xc0\x00\xf0\x00\x3c\x00\x0f\x00\x03\xc0\x03\xc0\x0f\x00\x3c\x00'\
b'\xf0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x00\x00\x1f\x00\x67\x80\xe3\x80\xe3\x80\x63\x80\x03\x00\x06\x00'\
b'\x0c\x00\x18\x00\x00\x00\x18\x00\x3c\x00\x3c\x00\x18\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x07\xf0\x1c\x0c'\
b'\x30\x04\x63\xe6\x66\x66\xcc\x66\xcc\x66\xd8\xcc\xd8\xcc\xd9\xd8'\
b'\xce\xf0\x60\x08\x70\x30\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x01\x00\x01\x80\x03\x80\x03\xc0\x05\xc0'\
b'\x04\xc0\x08\xe0\x08\xe0\x10\x70\x1f\xf0\x20\x70\x20\x38\x60\x38'\
b'\xf0\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00'\
b'\xff\xc0\x71\xe0\x70\xe0\x70\xe0\x70\xe0\x71\xc0\x7f\x80\x70\xe0'\
b'\x70\x70\x70\x70\x70\x70\x70\x70\x70\xe0\xff\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x0f\x90\x3c\xf0\x70\x30'\
b'\x70\x30\xe0\x10\xe0\x10\xe0\x00\xe0\x00\xe0\x00\xe0\x10\x70\x10'\
b'\x70\x20\x3c\x60\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\xff\xc0\x70\xf0\x70\x38\x70\x38\x70\x1c\x70\x1c'\
b'\x70\x1c\x70\x1c\x70\x1c\x70\x1c\x70\x38\x70\x38\x70\xf0\xff\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\xff\xe0'\
b'\x70\xe0\x70\x60\x71\x20\x71\x20\x73\x00\x7f\x00\x73\x00\x71\x00'\
b'\x71\x20\x70\x20\x70\x60\x70\xe0\xff\xe0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0d\x00\x00\x00\x00\x00\xff\xe0\x70\xe0\x70\x60\x71\x20'\
b'\x71\x20\x73\x00\x7f\x00\x73\x00\x71\x00\x71\x00\x70\x00\x70\x00'\
b'\x70\x00\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00'\
b'\x00\x00\x0f\x90\x3c\xf0\x70\x30\x70\x30\xe0\x10\xe0\x10\xe0\x00'\
b'\xe0\x00\xe0\xf8\xe0\x70\x70\x70\x70\x70\x3c\xf0\x0f\x90\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\xf8\x7c\x70\x38'\
b'\x70\x38\x70\x38\x70\x38\x70\x38\x7f\xf8\x70\x38\x70\x38\x70\x38'\
b'\x70\x38\x70\x38\x70\x38\xf8\x7c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x7c\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
b'\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00'\
b'\x07\xc0\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80'\
b'\x63\x80\xf3\x80\xf3\x80\xc3\x80\x67\x00\x3c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\xf8\xf8\x70\x60\x70\xc0'\
b'\x71\x80\x73\x00\x76\x00\x7e\x00\x7f\x00\x77\x80\x73\xc0\x71\xe0'\
b'\x70\xf0\x70\x78\xf8\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\xf8\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00'\
b'\x70\x00\x70\x00\x70\x00\x70\x40\x70\x40\x70\xc0\x71\xc0\xff\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00'\
b'\xfc\x0f\x80\x3c\x0f\x00\x3e\x0f\x00\x2e\x17\x00\x27\x17\x00\x27'\
b'\x17\x00\x27\x27\x00\x23\xa7\x00\x23\xa7\x00\x23\xc7\x00\x21\xc7'\
b'\x00\x21\xc7\x00\x70\x87\x00\xf8\x8f\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\xf0\x7c\x78\x38'\
b'\x3c\x10\x3c\x10\x3e\x10\x2f\x10\x27\x90\x23\xd0\x21\xf0\x20\xf0'\
b'\x20\xf0\x20\x70\x70\x30\xf8\x10\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\x0f\xc0\x3c\xf0\x70\x38\x70\x38\xe0\x1c'\
b'\xe0\x1c\xe0\x1c\xe0\x1c\xe0\x1c\xe0\x1c\x70\x38\x70\x38\x3c\xf0'\
b'\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00'\
b'\xff\x80\x71\xe0\x70\xf0\x70\xf0\x70\xf0\x70\xf0\x71\xe0\x7f\x80'\
b'\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\xf8\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x0f\xc0\x3c\xf0\x70\x38'\
b'\x70\x38\xe0\x1c\xe0\x1c\xe0\x1c\xe0\x1c\xe0\x1c\xef\x1c\x73\x98'\
b'\x71\xb8\x3d\xf0\x0f\xc0\x00\xc0\x00\xe8\x00\xf8\x00\x70\x10\x00'\
b'\x00\x00\x00\x00\xff\xe0\x70\xf0\x70\x70\x70\x70\x70\x70\x70\xe0'\
b'\x7f\x80\x71\xc0\x71\xc0\x71\xe0\x70\xe0\x70\xe0\x70\xe8\xf8\x70'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x1e\x80'\
b'\x73\x80\xe1\x80\xe0\x80\xf0\x00\xfc\x00\x7f\x00\x1f\x80\x07\xc0'\
b'\x83\xc0\x81\xc0\xc1\xc0\xf3\x80\x9f\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0d\x00\x00\x00\x00\x00\xff\xe0\xce\x60\x8e\x20\x8e\x20'\
b'\x8e\x20\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00'\
b'\x0e\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\x00\x00\xf8\x7c\x70\x38\x70\x10\x70\x10\x70\x10\x70\x10\x70\x10'\
b'\x70\x10\x70\x10\x70\x10\x70\x10\x70\x10\x38\x60\x0f\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\xfc\x3e\x78\x1c'\
b'\x38\x08\x3c\x10\x1c\x10\x1c\x10\x0e\x20\x0e\x20\x07\x40\x07\x40'\
b'\x03\x80\x03\x80\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\xfd\xf9\xf0\x78\xf0\xe0\x38\x70'\
b'\x40\x3c\x78\x80\x1c\x78\x80\x1c\x78\x80\x1e\xbd\x00\x0e\x9d\x00'\
b'\x0e\x9d\x00\x0f\x1e\x00\x07\x0e\x00\x07\x0e\x00\x02\x04\x00\x02'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00'\
b'\x00\x00\x00\x00\x00\x00\x7e\x7c\x00\x3c\x38\x00\x1e\x30\x00\x0e'\
b'\x60\x00\x0f\xc0\x00\x07\x80\x00\x03\xc0\x00\x07\xc0\x00\x07\xe0'\
b'\x00\x0c\xf0\x00\x18\x70\x00\x38\x78\x00\x70\x3c\x00\xf8\x7e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00'\
b'\x00\x00\xfc\x78\x78\x30\x38\x20\x3c\x60\x1c\x40\x1e\x80\x0f\x80'\
b'\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x1f\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\xff\xf0\xe0\x70'\
b'\xc0\xe0\x81\xe0\x83\xc0\x07\x80\x07\x00\x0f\x00\x1e\x00\x3c\x10'\
b'\x78\x10\x70\x30\xe0\x70\xff\xf0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x78\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x78\x00\x00\x09\x00\x00\x00\x00\x00\xc0\x00\xc0\x00'\
b'\x60\x00\x60\x00\x30\x00\x30\x00\x18\x00\x18\x00\x0c\x00\x0c\x00'\
b'\x06\x00\x06\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\xf0\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\x30\x30\x30\xf0\x00\x00\x09\x00\x00\x00\x00\x00\x18\x00\x18\x00'\
b'\x3c\x00\x3c\x00\x66\x00\x66\x00\xc3\x00\xc3\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\x80\xff\x80\x00\x00\x00\x00'

_index =\
b'\x00\x00\x16\x00\x2c\x00\x42\x00\x58\x00\x82\x00\xac\x00\xd6\x00'\
b'\x14\x01\x2a\x01\x40\x01\x56\x01\x6c\x01\x96\x01\xac\x01\xc2\x01'\
b'\xd8\x01\xee\x01\x18\x02\x42\x02\x6c\x02\x96\x02\xc0\x02\xea\x02'\
b'\x14\x03\x3e\x03\x68\x03\x92\x03\xa8\x03\xbe\x03\xe8\x03\x12\x04'\
b'\x3c\x04\x66\x04\x90\x04\xba\x04\xe4\x04\x0e\x05\x38\x05\x62\x05'\
b'\x8c\x05\xb6\x05\xe0\x05\x0a\x06\x34\x06\x5e\x06\x88\x06\xc6\x06'\
b'\xf0\x06\x1a\x07\x44\x07\x6e\x07\x98\x07\xc2\x07\xec\x07\x16\x08'\
b'\x40\x08\x7e\x08\xbc\x08\xe6\x08\x10\x09\x26\x09\x50\x09\x66\x09'\
b'\x90\x09\xba\x09'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 20
    return _mvfont[doff + 2:next_offs], 20, width
 
