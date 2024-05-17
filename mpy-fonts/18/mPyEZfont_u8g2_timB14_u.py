'''
    mPyEZfont_u8g2_timB14_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original timB14.bdf font file was sourced from the U8G2 project:
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
# Font: timB14.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./u-char.set -e 32 ../u8g2/tools/font/bdf/timB14.bdf 0 tmp_mPyEZfont_u8g2_timB14_u.py
version = '0.33'

def height():
    return 18

def baseline():
    return 14

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
    return 95

_font =\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x20\x70\x70\x70\x70'\
b'\x70\x70\x20\x20\x00\x70\x70\x70\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x33\x00\x33\x00\x33\x00\x33\x00\x22\x00\x22\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0a\x00\x00\x00\x00\x00\x19\x80\x19\x80\x19\x80\x7f\xc0'\
b'\x7f\xc0\x33\x00\x33\x00\xff\x80\xff\x80\x66\x00\x66\x00\x66\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x18\x00\x7e\x00\xdb\x00'\
b'\xdb\x00\xd8\x00\xf8\x00\x7c\x00\x3e\x00\x1f\x00\x1f\x00\x1b\x00'\
b'\xdb\x00\xdb\x00\x7e\x00\x18\x00\x18\x00\x00\x00\x00\x00\x12\x00'\
b'\x00\x00\x00\x1e\x0c\x00\x3b\xf8\x00\x71\x30\x00\x71\x20\x00\x72'\
b'\x60\x00\x7e\xc0\x00\x39\xbc\x00\x03\x76\x00\x03\x62\x00\x06\xe2'\
b'\x00\x0c\xe4\x00\x18\xfc\x00\x18\x70\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x07\x80\x0c\xc0\x0c\xc0'\
b'\x0c\xc0\x0e\x80\x07\x3c\x0f\x18\x17\x90\x33\xe0\x31\xe0\x38\xf0'\
b'\x3f\xfe\x1e\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x60'\
b'\x60\x60\x60\x40\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x04\x08\x18\x30\x30\x70\x60\x60\x60\x60\x60\x70\x30'\
b'\x30\x18\x08\x04\x06\x00\x00\x80\x40\x60\x30\x30\x38\x18\x18\x18'\
b'\x18\x18\x38\x30\x20\x60\x40\x80\x09\x00\x00\x00\x18\x00\x18\x00'\
b'\xdb\x00\xff\x00\x3c\x00\xff\x00\xdb\x00\x18\x00\x18\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\xff\xc0\xff\xc0\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x70\x70\x70\x30\x60\xc0\x00\x06\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xf8\xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\x70\x70\x00\x00\x00\x00'\
b'\x06\x00\x00\x18\x18\x18\x30\x30\x30\x20\x60\x60\x60\xc0\xc0\xc0'\
b'\x00\x00\x00\x00\x09\x00\x00\x00\x3c\x00\x66\x00\x67\x00\xe7\x00'\
b'\xe7\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00\x66\x00\x66\x00'\
b'\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x1c\x00'\
b'\x3c\x00\xfc\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00'\
b'\x1c\x00\x1c\x00\x1c\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x3c\x00\x7e\x00\xcf\x00\x87\x00\x07\x00\x07\x00'\
b'\x06\x00\x0c\x00\x18\x00\x31\x00\x63\x00\xff\x00\xff\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x3c\x00\x7e\x00\x8f\x00'\
b'\x07\x00\x0e\x00\x1c\x00\x3e\x00\x0f\x00\x07\x80\x03\x80\xc3\x00'\
b'\xe6\x00\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00'\
b'\x0e\x00\x1e\x00\x1e\x00\x2e\x00\x2e\x00\x4e\x00\xce\x00\x8e\x00'\
b'\xff\x00\xff\x00\x0e\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x09\x00\x00\x00\x3f\x00\x3f\x00\x3e\x00\x40\x00\x78\x00'\
b'\x7e\x00\x3f\x00\x07\x80\x03\x80\x03\x80\xc3\x00\xe6\x00\xfc\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x07\x00\x1c\x00'\
b'\x38\x00\x70\x00\x60\x00\xfc\x00\xe6\x00\xe7\x00\xe7\x00\xe7\x00'\
b'\xe7\x00\x66\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00'\
b'\x00\x00\xff\x00\xff\x00\xfe\x00\x86\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x18\x00\x18\x00\x38\x00\x30\x00\x30\x00\x70\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x00\x00\x3c\x00\x66\x00\xe3\x00\xe3\x00'\
b'\xf6\x00\x7c\x00\x3c\x00\x7e\x00\xcf\x00\xc7\x00\xc3\x00\xe7\x00'\
b'\x7e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x3c\x00'\
b'\x66\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00\x67\x00\x3f\x00\x07\x00'\
b'\x06\x00\x0e\x00\x3c\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x70\x70\x70\x00\x00\x00\x70\x70\x70'\
b'\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x70\x70\x70\x00\x00'\
b'\x00\x70\x70\x70\x30\x60\xc0\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x01\xc0\x07\x80\x1e\x00\x78\x00\x60\x00\x78\x00'\
b'\x1e\x00\x07\x80\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xc0\x7f\xc0'\
b'\x00\x00\x00\x00\x7f\xc0\x7f\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x70\x00\x3c\x00\x0f\x00\x03\xc0\x00\xc0\x03\xc0\x0f\x00\x3c\x00'\
b'\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x3e\x00'\
b'\x67\x00\x77\x00\x77\x00\x27\x00\x06\x00\x0c\x00\x08\x00\x08\x00'\
b'\x00\x00\x1c\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x11\x00\x00\x00\x00\x01\xf0\x00\x07\x9c\x00\x1c\x06\x00\x18\x02'\
b'\x00\x39\xdb\x00\x33\xbb\x00\x73\xbb\x00\x77\x33\x00\x77\x33\x00'\
b'\x77\x76\x00\x77\xfe\x00\x33\xdc\x00\x38\x00\x00\x1c\x00\x00\x0f'\
b'\x00\x00\x03\xf8\x00\x00\x00\x00\x0e\x00\x00\x00\x03\x00\x03\x80'\
b'\x07\x80\x05\xc0\x0d\xc0\x08\xc0\x18\xe0\x10\x60\x1f\xf0\x30\x70'\
b'\x20\x38\x60\x38\xf8\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00'\
b'\x00\x00\x7f\x00\x39\xc0\x38\xe0\x38\xe0\x38\xe0\x39\xc0\x3f\x00'\
b'\x39\xc0\x38\xe0\x38\xe0\x38\xe0\x39\xc0\x7f\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0e\x00\x00\x00\x07\xc8\x1c\x78\x38\x38\x38\x18'\
b'\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x38\x00\x38\x18\x1e\x70'\
b'\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x7f\x80'\
b'\x38\xe0\x38\x70\x38\x30\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\x30\x38\x70\x38\xe0\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x3f\xf0\x1c\x30\x1c\x10\x1c\x00\x1c\x00\x1c\x40'\
b'\x1f\xc0\x1c\x40\x1c\x00\x1c\x00\x1c\x10\x1c\x30\x3f\xf0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x3f\xf0\x1c\x30\x1c\x10'\
b'\x1c\x00\x1c\x00\x1c\x40\x1f\xc0\x1c\x40\x1c\x00\x1c\x00\x1c\x00'\
b'\x1c\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00'\
b'\x07\xc8\x1c\x78\x38\x38\x38\x18\x70\x00\x70\x00\x70\x7c\x70\x38'\
b'\x70\x38\x38\x38\x38\x38\x1c\x78\x07\xe0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0f\x00\x00\x00\x7c\x7c\x38\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\x38\x3f\xf8\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x7c\xfc'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x7c\x38\x38\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\x38\x7c\x00\x00\x00\x00\x09\x00\x00\x00'\
b'\x1f\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00'\
b'\x0e\x00\x0e\x00\x0e\x00\x0e\x00\xee\x00\xec\x00\x78\x00\x00\x00'\
b'\x00\x00\x0f\x00\x00\x00\x3e\x7c\x1c\x30\x1c\x60\x1c\xc0\x1d\x80'\
b'\x1f\x00\x1f\x00\x1f\x80\x1d\xc0\x1d\xe0\x1c\xf0\x1c\x78\x3e\x3c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x3e\x00\x1c\x00'\
b'\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00'\
b'\x1c\x10\x1c\x30\x3f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00'\
b'\x00\x00\x00\x3c\x07\x80\x1c\x07\x00\x1e\x0f\x00\x1e\x0f\x00\x1f'\
b'\x17\x00\x17\x17\x00\x17\xb7\x00\x13\xa7\x00\x13\xe7\x00\x11\xc7'\
b'\x00\x11\xc7\x00\x10\xc7\x00\x38\x8f\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x78\x38\x3c\x10\x3c\x10'\
b'\x3e\x10\x2f\x10\x27\x10\x27\x90\x23\xd0\x21\xd0\x21\xf0\x20\xf0'\
b'\x20\x70\x70\x70\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00'\
b'\x07\xc0\x1c\x70\x38\x38\x38\x38\x70\x1c\x70\x1c\x70\x1c\x70\x1c'\
b'\x70\x1c\x38\x38\x38\x38\x1c\x70\x07\xc0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x00\x00\x7f\x80\x39\xc0\x38\xe0\x38\xe0\x38\xe0'\
b'\x39\xc0\x3f\x80\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x7c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x07\xc0\x1c\x70'\
b'\x38\x38\x38\x38\x70\x1c\x70\x1c\x70\x1c\x70\x1c\x70\x1c\x38\x38'\
b'\x38\x38\x1c\x70\x07\xc0\x07\x80\x03\xc0\x01\xf0\x00\x7c\x0e\x00'\
b'\x00\x00\x7f\x80\x39\xc0\x38\xe0\x38\xe0\x38\xe0\x39\xc0\x3f\x80'\
b'\x3b\x80\x39\xc0\x38\xe0\x38\xe0\x38\x70\x7c\x78\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x0f\x40\x31\xc0\x70\xc0\x70\x00'\
b'\x7c\x00\x3e\x00\x1f\x80\x07\xc0\x03\xc0\x01\xc0\x61\xc0\x73\x80'\
b'\x5e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x7f\xf0'\
b'\x67\x30\x47\x10\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00'\
b'\x07\x00\x07\x00\x07\x00\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x7c\x78\x38\x10\x38\x10\x38\x10\x38\x10\x38\x10'\
b'\x38\x10\x38\x10\x38\x10\x38\x10\x38\x30\x1c\x60\x0f\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\xfc\x7c\x78\x18\x38\x10'\
b'\x3c\x30\x1c\x20\x1e\x60\x1e\x40\x0e\xc0\x0f\x80\x07\x80\x07\x00'\
b'\x03\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00'\
b'\x00\x7e\xfb\xe0\x3c\xf0\xc0\x1c\x70\x80\x1e\x71\x80\x1e\x71\x00'\
b'\x0e\x39\x00\x0f\x3b\x00\x07\x3a\x00\x07\x5e\x00\x07\x9e\x00\x03'\
b'\x9e\x00\x03\x0c\x00\x03\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0e\x00\x00\x00\xf8\x78\x78\x30\x3c\x60\x1c\xc0'\
b'\x0f\x80\x07\x00\x07\x80\x07\xc0\x0d\xc0\x18\xe0\x30\x70\x60\x78'\
b'\xf0\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x7e\x3c'\
b'\x3c\x18\x1c\x30\x1e\x20\x0f\x60\x07\x40\x07\xc0\x03\x80\x03\x80'\
b'\x03\x80\x03\x80\x03\x80\x0f\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x3f\xf0\x30\xf0\x20\xe0\x01\xe0\x03\xc0\x03\x80'\
b'\x07\x80\x0f\x00\x0e\x00\x1e\x00\x3c\x10\x38\x30\x3f\xf0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x06\x00\x00\x78\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x78\x00\x05\x00\x00\xc0\xc0\xc0'\
b'\x60\x60\x60\x20\x30\x30\x30\x18\x18\x18\x00\x00\x00\x00\x06\x00'\
b'\x00\x78\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18'\
b'\x78\x00\x0b\x00\x00\x00\x0c\x00\x0c\x00\x1e\x00\x12\x00\x33\x00'\
b'\x61\x80\x61\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\xff\x80\xff\x80\x00\x00\x00\x00'

_index =\
b'\x00\x00\x14\x00\x28\x00\x3c\x00\x62\x00\x88\x00\xae\x00\xe6\x00'\
b'\x0c\x01\x20\x01\x34\x01\x48\x01\x6e\x01\x94\x01\xa8\x01\xbc\x01'\
b'\xd0\x01\xe4\x01\x0a\x02\x30\x02\x56\x02\x7c\x02\xa2\x02\xc8\x02'\
b'\xee\x02\x14\x03\x3a\x03\x60\x03\x74\x03\x88\x03\xae\x03\xd4\x03'\
b'\xfa\x03\x20\x04\x58\x04\x7e\x04\xa4\x04\xca\x04\xf0\x04\x16\x05'\
b'\x3c\x05\x62\x05\x88\x05\x9c\x05\xc2\x05\xe8\x05\x0e\x06\x46\x06'\
b'\x6c\x06\x92\x06\xb8\x06\xde\x06\x04\x07\x2a\x07\x50\x07\x76\x07'\
b'\x9c\x07\xd4\x07\xfa\x07\x20\x08\x46\x08\x5a\x08\x6e\x08\x82\x08'\
b'\xa8\x08\xce\x08'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 18
    return _mvfont[doff + 2:next_offs], 18, width
 
