'''
    mPyEZfont_u8g2_ncenB12_e.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenB12.bdf font file was sourced from the U8G2 project:
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
# Font: ncenB12.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -e 32 ../u8g2/tools/font/bdf/ncenB12.bdf 0 tmp_mPyEZfont_u8g2_ncenB12_e.py
version = '0.33'

def height():
    return 17

def baseline():
    return 14

def max_width():
    return 16

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
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x20\x70\x70\x70\x70\x20'\
b'\x20\x00\x20\x70\x70\x20\x00\x00\x00\x06\x00\x00\x00\xd8\xd8\xd8'\
b'\x90\x90\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x00\x00\x19\x80\x19\x80\x19\x80\x7f\xc0\x7f\xc0\x33\x00\x33\x00'\
b'\xff\x80\xff\x80\x66\x00\x66\x00\x66\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x08\x00\x08\x00\x3e\x00\x69\x00\xcb\x80\xc9\x00\xfc\x00'\
b'\x7f\x00\x1f\x80\x49\x80\xe9\x80\xc9\x80\x6b\x00\x3e\x00\x08\x00'\
b'\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x1c\x40\x3b\xc0\x32\x80'\
b'\x62\x80\x65\x00\x65\x70\x3a\xe8\x02\xc8\x05\x88\x05\x90\x09\x90'\
b'\x08\xe0\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x07\x80'\
b'\x0c\xc0\x0c\xc0\x0c\x80\x0f\x00\x1e\x78\x37\x30\x73\xa0\x63\xc0'\
b'\x71\xc8\x79\xf8\x3e\x70\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00'\
b'\x60\x60\x60\x40\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06'\
b'\x00\x00\x00\x08\x10\x30\x30\x60\x60\x60\x60\x60\x60\x30\x30\x10'\
b'\x08\x00\x06\x00\x00\x00\x80\x40\x60\x60\x30\x30\x30\x30\x30\x30'\
b'\x60\x60\x40\x80\x00\x08\x00\x00\x00\x10\x54\xd6\x38\xd6\x54\x10'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80\x7f\x80'\
b'\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\xf0\x70\x20\x60\x80\x05'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\x00\x00\x00\x00'\
b'\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60'\
b'\xf0\x60\x00\x00\x00\x05\x00\x00\x00\x08\x08\x10\x10\x10\x20\x20'\
b'\x40\x40\x40\x80\x80\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x1c\x00'\
b'\x36\x00\x63\x00\x63\x00\xe3\x80\xe3\x80\xe3\x80\xe3\x80\x63\x00'\
b'\x63\x00\x36\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x00\x00\x0c\x00\x7c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00'\
b'\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x7f\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x1e\x00\x23\x00\x73\x80\x73\x80\x23\x80'\
b'\x07\x00\x06\x00\x0c\x00\x18\x80\x30\x80\x7f\x80\x7f\x80\x00\x00'\
b'\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x3e\x00\x67\x00\x73\x00'\
b'\x23\x00\x06\x00\x1f\x00\x07\x00\x03\x80\x63\x80\xf3\x80\x67\x00'\
b'\x3e\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x02\x00'\
b'\x06\x00\x0e\x00\x1e\x00\x2e\x00\x2e\x00\x4e\x00\x8e\x00\xff\x80'\
b'\x0e\x00\x0e\x00\x3f\x80\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x00\x00\x3f\x80\x3f\x00\x20\x00\x20\x00\x3e\x00\x27\x00\x03\x80'\
b'\x23\x80\x73\x80\x73\x80\x67\x00\x3e\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x1f\x00\x33\x80\x67\x80\x63\x00\xe0\x00'\
b'\xee\x00\xf7\x00\xe3\x80\xe3\x80\x63\x80\x77\x00\x1e\x00\x00\x00'\
b'\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x7f\x80\x7f\x00\x43\x00'\
b'\x43\x00\x42\x00\x06\x00\x06\x00\x0c\x00\x0c\x00\x1c\x00\x1c\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x1e\x00'\
b'\x33\x00\x73\x80\x73\x80\x33\x00\x1e\x00\x33\x00\x73\x80\x73\x80'\
b'\x73\x80\x33\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x00\x00\x3c\x00\x77\x00\xe3\x00\xe3\x80\xe3\x80\x77\x80\x3b\x80'\
b'\x03\x80\x63\x00\xf3\x00\xe6\x00\x7c\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x60\xf0\x60\x00\x00\x60\xf0\x60'\
b'\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x60\xf0\x60\x00\x00'\
b'\x60\xf0\x70\x20\x60\x80\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x01\x80\x07\x80\x1e\x00\x78\x00\x78\x00\x1e\x00\x07\x80'\
b'\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x7f\x80\x00\x00'\
b'\x00\x00\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00\x78\x00\x1e\x00'\
b'\x07\x80\x07\x80\x1e\x00\x78\x00\x60\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x00\x00\x3c\x66\xf7\x67\x0e\x0c\x10\x00\x10\x38'\
b'\x38\x10\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x0f\x80\x38\xe0\x60'\
b'\x20\x46\xb0\xcd\x90\x99\x90\x99\x90\x99\xb0\xdb\xa0\x4c\x40\x60'\
b'\x30\x38\xe0\x0f\x80\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x06'\
b'\x00\x07\x00\x07\x00\x0f\x00\x0b\x80\x1b\x80\x11\xc0\x3f\xc0\x31'\
b'\xc0\x20\xe0\x60\xe0\xf1\xf8\x00\x00\x00\x00\x00\x00\x0d\x00\x00'\
b'\x00\x00\x00\xff\xc0\x38\xe0\x38\x70\x38\x70\x38\xe0\x3f\xc0\x38'\
b'\xe0\x38\x70\x38\x70\x38\x70\x38\xe0\xff\xc0\x00\x00\x00\x00\x00'\
b'\x00\x0d\x00\x00\x00\x00\x00\x07\xd0\x1c\x70\x38\x30\x38\x10\x70'\
b'\x10\x70\x00\x70\x00\x70\x10\x38\x10\x38\x20\x1c\x60\x07\x80\x00'\
b'\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\xff\x80\x38\xe0\x38'\
b'\x70\x38\x70\x38\x38\x38\x38\x38\x38\x38\x38\x38\x70\x38\x70\x38'\
b'\xe0\xff\x80\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\xff'\
b'\xe0\x38\x60\x38\x60\x39\x20\x3b\x00\x3f\x00\x3b\x00\x39\x20\x38'\
b'\x20\x38\x60\x38\x60\xff\xe0\x00\x00\x00\x00\x00\x00\x0c\x00\x00'\
b'\x00\x00\x00\xff\xe0\x38\x60\x38\x60\x39\x20\x3b\x00\x3f\x00\x3b'\
b'\x00\x39\x00\x38\x00\x38\x00\x38\x00\xfe\x00\x00\x00\x00\x00\x00'\
b'\x00\x0e\x00\x00\x00\x00\x00\x07\xd0\x1c\x70\x38\x30\x38\x10\x70'\
b'\x10\x70\x00\x71\xfc\x70\x70\x38\x70\x38\x70\x1c\xf0\x07\x90\x00'\
b'\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\xfe\xfc\x38\x70\x38'\
b'\x70\x38\x70\x38\x70\x3f\xf0\x38\x70\x38\x70\x38\x70\x38\x70\x38'\
b'\x70\xfe\xfc\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\xfe\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\x38\x38\xfe\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x1f\xc0\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x67\x00'\
b'\xf7\x00\xe7\x00\x87\x00\xce\x00\x7c\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\xfe\xf8\x38\x60\x38\xc0\x39\x80\x3b\x00'\
b'\x3f\x80\x3f\x80\x3b\xc0\x39\xe0\x38\xf0\x38\x78\xfe\xfc\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\xfe\x00\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x20\x38\x20\x38\x60\x38\x60'\
b'\xff\xe0\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\xfc\x3f'\
b'\x3c\x3c\x2e\x3c\x2e\x5c\x2e\x5c\x27\x5c\x27\x9c\x27\x9c\x23\x9c'\
b'\x23\x1c\x21\x1c\xf9\x3f\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00'\
b'\x00\x00\xf0\x7c\x38\x10\x3c\x10\x3e\x10\x2f\x10\x27\x90\x23\xd0'\
b'\x21\xf0\x20\xf0\x20\x70\x20\x30\xf8\x10\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x07\x80\x1c\xe0\x38\x70\x38\x70\x70\x38'\
b'\x70\x38\x70\x38\x70\x38\x38\x70\x38\x70\x1c\xe0\x07\x80\x00\x00'\
b'\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\xff\xc0\x38\xe0\x38\x70'\
b'\x38\x70\x38\x70\x38\xe0\x3f\xc0\x38\x00\x38\x00\x38\x00\x38\x00'\
b'\xfe\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x07\x80'\
b'\x1c\xe0\x38\x70\x38\x70\x70\x38\x70\x38\x70\x38\x73\x38\x34\xb0'\
b'\x3c\xf0\x1c\xe0\x07\xc0\x00\xe8\x00\xf8\x00\x70\x0e\x00\x00\x00'\
b'\x00\x00\xff\xc0\x38\xe0\x38\x70\x38\x70\x38\xe0\x3f\xc0\x39\x80'\
b'\x39\xc0\x38\xe0\x38\xe8\x38\xf8\xfc\x70\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x1f\x40\x21\xc0\x60\xc0\x60\x40\x7c\x40'\
b'\x3f\x00\x1f\x80\x47\xc0\x40\xc0\x60\xc0\x70\x80\x5f\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\xff\xe0\xce\x60\x8e\x20'\
b'\x8e\x20\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00'\
b'\x3f\x80\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\xfe\x7c'\
b'\x38\x10\x38\x10\x38\x10\x38\x10\x38\x10\x38\x10\x38\x10\x38\x10'\
b'\x1c\x20\x1e\x60\x07\x80\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00'\
b'\x00\x00\xfe\x78\x38\x30\x3c\x20\x1c\x20\x1c\x40\x0e\x40\x0e\x80'\
b'\x0f\x80\x07\x80\x07\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\xfb\xde\x71\x8c\x31\x88\x39\xc8\x39\xd8'\
b'\x3b\xd0\x1a\xd0\x1e\xf0\x1c\xe0\x0c\x60\x0c\x60\x0c\x60\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\xf9\xf0\x70\x60\x38\x40'\
b'\x1c\x80\x1f\x00\x0f\x00\x0f\x00\x0f\x80\x13\xc0\x21\xc0\x60\xe0'\
b'\xf9\xf0\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\xfe\xf8'\
b'\x38\x60\x1c\x40\x1c\x80\x0e\x80\x0f\x00\x07\x00\x07\x00\x07\x00'\
b'\x07\x00\x07\x00\x1f\xc0\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x7f\xc0\x61\xc0\x43\x80\x43\x80\x07\x00\x0e\x00\x0e\x00'\
b'\x1c\x40\x38\x40\x38\xc0\x71\xc0\x7f\xc0\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x78\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x78\x00\x0a\x00\x00\x00\x00\x00\x60\x00\x60\x00\x30\x00\x30'\
b'\x00\x18\x00\x18\x00\x0c\x00\x0c\x00\x06\x00\x06\x00\x03\x00\x03'\
b'\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x78\x18\x18\x18\x18'\
b'\x18\x18\x18\x18\x18\x18\x18\x18\x78\x00\x0a\x00\x00\x00\x00\x00'\
b'\x0c\x00\x0c\x00\x1e\x00\x33\x00\x33\x00\x61\x80\x61\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff'\
b'\x00\x06\x00\x00\x00\xc0\xe0\x30\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7e\x00\xe7\x00\xc7\x00\x1f\x00\x67\x00\xe7\x00\xef\x00'\
b'\x77\x80\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\xf8\x00'\
b'\x38\x00\x38\x00\x38\x00\x3b\x80\x3d\xc0\x38\xe0\x38\xe0\x38\xe0'\
b'\x38\xe0\x3d\xc0\x2b\x80\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3e\x00\x73\x00\xe7\x00'\
b'\xe0\x00\xe0\x00\xe3\x00\x76\x00\x3c\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x07\x80\x03\x80\x03\x80\x03\x80\x3b\x80'\
b'\x77\x80\xe3\x80\xe3\x80\xe3\x80\xe3\x80\x77\x80\x3a\xe0\x00\x00'\
b'\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x3e\x00\x77\x00\xe3\x80\xff\x80\xe0\x00\xe1\x80\x73\x00'\
b'\x3e\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x0f\x00'\
b'\x1b\x80\x3b\x00\x38\x00\xfe\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\xfe\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80\x3f\x80\x77\x00\xe3\x80'\
b'\xe3\x80\xf7\x00\x7c\x00\x60\x00\x7f\x00\xff\x80\xc3\x80\xff\x00'\
b'\x0c\x00\x00\x00\x00\x00\xf0\x00\x70\x00\x70\x00\x70\x00\x77\x80'\
b'\x79\xc0\x79\xc0\x71\xc0\x71\xc0\x71\xc0\x71\xc0\xfb\xe0\x00\x00'\
b'\x00\x00\x00\x00\x06\x00\x00\x00\x60\xf0\x60\x00\xf0\x70\x70\x70'\
b'\x70\x70\x70\xf8\x00\x00\x00\x08\x00\x00\x00\x18\x3c\x18\x00\x7c'\
b'\x1c\x1c\x1c\x1c\x1c\x1c\x1c\xdc\xd8\x70\x0b\x00\x00\x00\x00\x00'\
b'\xf0\x00\x70\x00\x70\x00\x70\x00\x77\xc0\x73\x80\x77\x00\x7e\x00'\
b'\x7f\x00\x73\x80\x71\xc0\xfb\xe0\x00\x00\x00\x00\x00\x00\x06\x00'\
b'\x00\x00\xf0\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\xf8\x00\x00'\
b'\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7'\
b'\x38\x7b\xdc\x73\x9c\x73\x9c\x73\x9c\x73\x9c\x73\x9c\xfb\xbe\x00'\
b'\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\xf7\x80\x79\xc0\x71\xc0\x71\xc0\x71\xc0\x71\xc0\x71'\
b'\xc0\xfb\xe0\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x73\x80\xe1\xc0\xe1\xc0\xe1'\
b'\xc0\xe1\xc0\x73\x80\x1e\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\x00\x7b\x80\x71'\
b'\xc0\x71\xc0\x71\xc0\x71\xc0\x7b\x80\x77\x00\x70\x00\x70\x00\xf8'\
b'\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3e'\
b'\x80\x73\x80\xe3\x80\xe3\x80\xe3\x80\xe3\x80\x73\x80\x3f\x80\x03'\
b'\x80\x03\x80\x07\xc0\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\xf7\x00\x7b\x80\x73\x00\x70\x00\x70\x00\x70\x00\x70'\
b'\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00'\
b'\x00\x7a\xc6\xe2\xfc\x7e\x8e\xc6\xbc\x00\x00\x00\x07\x00\x00\x00'\
b'\x00\x10\x10\x30\xfc\x70\x70\x70\x70\x74\x7c\x38\x00\x00\x00\x0c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf3\xc0\x71'\
b'\xc0\x71\xc0\x71\xc0\x71\xc0\x71\xc0\x7b\xc0\x3e\xe0\x00\x00\x00'\
b'\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xfb\xc0\x71\x80\x73\x00\x3b\x00\x3a\x00\x1e\x00\x1c\x00\x0c'\
b'\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\xfb\xde\x71\x8c\x39\xc8\x3b\xd8\x1e\xf0\x1e'\
b'\xf0\x0c\x60\x0c\x60\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfb\x80\x71\x00\x3e\x00\x1c'\
b'\x00\x1c\x00\x3e\x00\x47\x00\xef\x80\x00\x00\x00\x00\x00\x00\x0b'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfb\xc0\x71'\
b'\x80\x39\x80\x39\x00\x1f\x00\x0e\x00\x0e\x00\x06\x00\x34\x00\x74'\
b'\x00\x38\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xfe\x00\xcc\x00\x9c\x00\x38\x00\x30\x00\x72\x00\xe6\x00\xfe'\
b'\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x18\x30\x30\x30\x30'\
b'\x30\x60\x30\x30\x30\x30\x30\x30\x18\x00\x0a\x00\x00\x00\x00\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x06\x00'\
b'\x00\x00\xc0\x60\x60\x60\x60\x60\x30\x60\x60\x60\x60\x60\x60\xc0'\
b'\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x39\x00\x7f\x80\x27\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00'

_index =\
b'\x00\x00\x13\x00\x26\x00\x39\x00\x4c\x00\x70\x00\x94\x00\xb8\x00'\
b'\xdc\x00\xef\x00\x02\x01\x15\x01\x28\x01\x4c\x01\x5f\x01\x72\x01'\
b'\x85\x01\x98\x01\xbc\x01\xe0\x01\x04\x02\x28\x02\x4c\x02\x70\x02'\
b'\x94\x02\xb8\x02\xdc\x02\x00\x03\x13\x03\x26\x03\x4a\x03\x6e\x03'\
b'\x92\x03\xa5\x03\xc9\x03\xed\x03\x11\x04\x35\x04\x59\x04\x7d\x04'\
b'\xa1\x04\xc5\x04\xe9\x04\xfc\x04\x20\x05\x44\x05\x68\x05\x8c\x05'\
b'\xb0\x05\xd4\x05\xf8\x05\x1c\x06\x40\x06\x64\x06\x88\x06\xac\x06'\
b'\xd0\x06\xf4\x06\x18\x07\x3c\x07\x60\x07\x73\x07\x97\x07\xaa\x07'\
b'\xce\x07\xe1\x07\xf4\x07\x18\x08\x3c\x08\x60\x08\x84\x08\xa8\x08'\
b'\xcc\x08\xf0\x08\x14\x09\x27\x09\x3a\x09\x5e\x09\x71\x09\x95\x09'\
b'\xb9\x09\xdd\x09\x01\x0a\x25\x0a\x49\x0a\x5c\x0a\x6f\x0a\x93\x0a'\
b'\xb7\x0a\xdb\x0a\xff\x0a\x23\x0b\x47\x0b\x5a\x0b\x7e\x0b\x91\x0b'\
b'\xb5\x0b'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 126 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 17
    return _mvfont[doff + 2:next_offs], 17, width
 
