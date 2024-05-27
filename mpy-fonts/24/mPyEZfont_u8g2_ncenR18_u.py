'''
    mPyEZfont_u8g2_ncenR18_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenR18.bdf font file was sourced from the U8G2 project:
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
# Font: ncenR18.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -l 95 -e 32 ../u8g2/tools/font/bdf/ncenR18.bdf 0 tmp_mPyEZfont_u8g2_ncenR18_u.py
version = '0.33'

def height():
    return 24

def baseline():
    return 20

def max_width():
    return 25

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
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x07\x00\x00\x00\x10\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\x38\x38\x10\x10\x10\x00\x38\x38\x38\x00\x00\x00\x00\x0a\x00'\
b'\x00\x00\x00\x00\x33\x00\x33\x00\x33\x00\x33\x00\x33\x00\x33\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x06\x30\x06\x30\x06\x30\x06\x30'\
b'\x06\x30\x3f\xfc\x0c\x60\x0c\x60\x0c\x60\x0c\x60\x7f\xf8\x18\xc0'\
b'\x18\xc0\x18\xc0\x18\xc0\x18\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0d\x00\x02\x00\x02\x00\x0f\x80\x32\xc0\x22\x60\x62\x60'\
b'\x62\xe0\x62\xc0\x72\x00\x7e\x00\x3f\x80\x0f\xe0\x03\xe0\x02\x70'\
b'\x32\x30\x72\x30\x62\x30\x62\x20\x32\x60\x1f\x80\x02\x00\x02\x00'\
b'\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x0f\x0c\x00\x19'\
b'\x94\x00\x30\xec\x00\x30\x88\x00\x60\x98\x00\x60\x90\x00\x61\x30'\
b'\x00\x61\x20\x00\x62\x63\xc0\x3c\x46\x60\x00\xcc\x20\x00\x8c\x20'\
b'\x01\x98\x20\x01\x18\x20\x03\x18\x40\x02\x18\x40\x06\x18\x80\x04'\
b'\x0f\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00'\
b'\x00\x00\x00\x00\x00\x00\x03\xe0\x00\x06\x70\x00\x0c\x30\x00\x0c'\
b'\x30\x00\x0c\x30\x00\x0c\x60\x00\x06\xc0\x00\x07\x00\x00\x0f\x1f'\
b'\xc0\x33\x8f\x00\x31\xc6\x00\x60\xe4\x00\x60\x74\x00\x60\x38\x00'\
b'\x70\x1c\x20\x38\x3e\x20\x3f\xe7\xc0\x0f\x83\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x30\x30\x30\x30'\
b'\x30\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x09\x00\x00\x00\x00\x00\x01\x00\x06\x00\x0c\x00\x18\x00'\
b'\x18\x00\x30\x00\x30\x00\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x30\x00\x30\x00\x18\x00\x18\x00\x0c\x00\x06\x00'\
b'\x01\x00\x00\x00\x08\x00\x00\x00\x80\x60\x30\x18\x18\x0c\x0c\x06'\
b'\x06\x06\x06\x06\x06\x06\x0c\x0c\x18\x18\x30\x60\x80\x00\x09\x00'\
b'\x00\x00\x00\x00\x08\x00\x1c\x00\x49\x00\x6b\x00\x1c\x00\x6b\x00'\
b'\x49\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x7f\xf8\x7f\xf8\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x30\x78\x78\x18\x10\x20\x40\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7e\x7e\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x38\x38\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x06\x06\x06\x0c\x0c\x0c\x18\x18\x18\x30\x30\x30'\
b'\x60\x60\x60\xc0\xc0\xc0\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00'\
b'\x07\x00\x08\x80\x18\xc0\x10\x40\x30\x60\x30\x60\x70\x70\x70\x70'\
b'\x70\x70\x70\x70\x70\x70\x70\x70\x30\x60\x30\x60\x10\x40\x18\xc0'\
b'\x08\x80\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00'\
b'\x00\x00\x01\x00\x07\x00\x1f\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00'\
b'\x00\x00\x00\x00\x0f\x80\x38\xe0\x20\x60\x70\x70\x70\x70\x20\x70'\
b'\x00\x60\x00\xe0\x00\xc0\x01\x80\x03\x00\x06\x00\x0c\x00\x18\x10'\
b'\x30\x10\x60\x30\x7f\xf0\x7f\xf0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x0f\x80\x31\xc0\x60\xe0\x70\xe0\x70\xe0'\
b'\x20\xc0\x00\xc0\x01\x80\x0f\x80\x00\xc0\x00\x60\x00\x70\x20\x70'\
b'\x70\x70\x70\x60\x60\xe0\x30\xc0\x0f\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x40\x00\xc0\x01\xc0\x03\xc0'\
b'\x06\xc0\x0c\xc0\x08\xc0\x18\xc0\x30\xc0\x60\xc0\x40\xc0\xc0\xc0'\
b'\x80\xc0\xff\xf0\x00\xc0\x00\xc0\x00\xc0\x03\xf0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x3f\xe0\x3f\xc0\x20\x00'\
b'\x20\x00\x20\x00\x20\x00\x20\x00\x2f\x80\x31\xc0\x00\x60\x00\x60'\
b'\x00\x70\x30\x70\x70\x70\x70\x60\x20\x60\x30\xc0\x0f\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x07\xc0\x1c\x70'\
b'\x10\x70\x30\x30\x30\x00\x30\x00\x70\x00\x77\x80\x78\xc0\x70\x60'\
b'\x70\x60\x70\x70\x70\x70\x30\x70\x30\x60\x30\x60\x18\xc0\x0f\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x3f\xf0'\
b'\x3f\xf0\x20\x20\x20\x60\x00\x40\x00\xc0\x00\xc0\x00\x80\x01\x80'\
b'\x01\x80\x01\x00\x03\x00\x03\x00\x03\x00\x07\x00\x07\x00\x07\x00'\
b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00'\
b'\x0f\x80\x18\xc0\x10\x40\x30\x60\x30\x60\x38\x60\x1c\xc0\x1f\x80'\
b'\x0f\x80\x1b\xc0\x30\xe0\x60\x70\x60\x30\x60\x30\x60\x30\x30\x60'\
b'\x38\xe0\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00'\
b'\x00\x00\x0f\x80\x18\xc0\x38\x60\x30\x60\x70\x70\x70\x70\x70\x70'\
b'\x30\x70\x38\x70\x18\xf0\x0f\x70\x00\x70\x00\x60\x00\x60\x60\xe0'\
b'\x70\xc0\x71\xc0\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x38\x38\x00\x00\x00\x00\x00'\
b'\x00\x38\x38\x38\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x38\x38\x38\x00\x00\x00\x00\x00\x00\x18\x3c\x3c\x0c\x08'\
b'\x10\x20\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x18\x00\x78\x01\xe0\x07\x80\x1e\x00\x78\x00\x78\x00'\
b'\x1e\x00\x07\x80\x01\xe0\x00\x78\x00\x18\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf8\x7f\xf8\x00\x00'\
b'\x00\x00\x7f\xf8\x7f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x60\x00\x78\x00\x1e\x00\x07\x80\x01\xe0'\
b'\x00\x78\x00\x78\x01\xe0\x07\x80\x1e\x00\x78\x00\x60\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x0f\x00'\
b'\x31\xc0\x60\xe0\x70\xe0\x70\xe0\x00\xe0\x01\xc0\x03\x80\x07\x00'\
b'\x06\x00\x0c\x00\x08\x00\x08\x00\x00\x00\x00\x00\x1c\x00\x1c\x00'\
b'\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\xfc\x00\x03\x03\x00\x0c\x01\x80\x08\x00\xc0\x30\x6c'\
b'\x40\x31\x9c\x40\x63\x0c\x40\x63\x0c\x40\x66\x0c\x40\x66\x18\x80'\
b'\x66\x18\x80\x66\x39\x00\x62\x5a\x00\x61\x9c\x00\x30\x00\x80\x30'\
b'\x01\x00\x0c\x06\x00\x0f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00'\
b'\x60\x00\x00\xe0\x00\x00\xf0\x00\x01\x30\x00\x01\x38\x00\x02\x18'\
b'\x00\x02\x1c\x00\x04\x0c\x00\x04\x0c\x00\x08\x0e\x00\x0f\xfe\x00'\
b'\x10\x06\x00\x10\x07\x00\x20\x03\x00\x20\x03\x80\x60\x03\x80\xf8'\
b'\x0f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00'\
b'\x00\x00\x00\x00\x00\x00\x3f\xf0\x00\x0c\x1c\x00\x0c\x0c\x00\x0c'\
b'\x0e\x00\x0c\x0e\x00\x0c\x0e\x00\x0c\x0c\x00\x0c\x18\x00\x0f\xfc'\
b'\x00\x0c\x0e\x00\x0c\x06\x00\x0c\x07\x00\x0c\x07\x00\x0c\x07\x00'\
b'\x0c\x07\x00\x0c\x06\x00\x0c\x0e\x00\x3f\xf8\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\xf9\x00\x0e\x0f\x00\x1c\x03\x00\x18\x01\x00\x38\x01\x00\x30'\
b'\x01\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00'\
b'\x00\x70\x00\x00\x30\x01\x00\x38\x01\x00\x18\x03\x00\x1c\x02\x00'\
b'\x0e\x0e\x00\x03\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x3f\xf8\x00\x0c\x0e\x00'\
b'\x0c\x03\x00\x0c\x03\x00\x0c\x01\x80\x0c\x01\x80\x0c\x01\xc0\x0c'\
b'\x01\xc0\x0c\x01\xc0\x0c\x01\xc0\x0c\x01\xc0\x0c\x01\xc0\x0c\x01'\
b'\x80\x0c\x01\x80\x0c\x03\x00\x0c\x03\x00\x0c\x0e\x00\x3f\xf8\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\x00\x00\x7f\xfc\x18\x1c\x18\x0c\x18\x04\x18\x04\x18\x44\x18\x40'\
b'\x18\xc0\x1f\xc0\x18\xc0\x18\x40\x18\x40\x18\x04\x18\x04\x18\x04'\
b'\x18\x0c\x18\x1c\x7f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x7f\xfc\x18\x1c\x18\x0c\x18\x04\x18\x04\x18\x44'\
b'\x18\x40\x18\xc0\x1f\xc0\x18\xc0\x18\x40\x18\x40\x18\x00\x18\x00'\
b'\x18\x00\x18\x00\x18\x00\x7e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x12\x00\x00\x00\x00\x00\x00\x00\x03\xfd\x00\x0e\x0f\x00\x18\x03'\
b'\x00\x18\x03\x00\x38\x01\x00\x30\x01\x00\x70\x00\x00\x70\x00\x00'\
b'\x70\x00\x00\x70\x00\x00\x70\x1f\xc0\x70\x03\x00\x30\x03\x00\x38'\
b'\x03\x00\x18\x03\x00\x18\x07\x00\x0e\x0f\x00\x03\xf9\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x00\x00\x00\x00\x00'\
b'\x00\x00\x3f\x07\xe0\x0c\x01\x80\x0c\x01\x80\x0c\x01\x80\x0c\x01'\
b'\x80\x0c\x01\x80\x0c\x01\x80\x0c\x01\x80\x0f\xff\x80\x0c\x01\x80'\
b'\x0c\x01\x80\x0c\x01\x80\x0c\x01\x80\x0c\x01\x80\x0c\x01\x80\x0c'\
b'\x01\x80\x0c\x01\x80\x3f\x07\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x3f\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x3f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x03\xf0\x00\xc0'\
b'\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0'\
b'\x00\xc0\x30\xc0\x78\xc0\x70\xc0\x60\xc0\x60\xc0\x31\x80\x1f\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00'\
b'\x3f\x1f\xc0\x0c\x07\x00\x0c\x06\x00\x0c\x0c\x00\x0c\x18\x00\x0c'\
b'\x30\x00\x0c\x60\x00\x0c\xc0\x00\x0d\xc0\x00\x0f\xe0\x00\x0e\x70'\
b'\x00\x0c\x38\x00\x0c\x1c\x00\x0c\x0e\x00\x0c\x07\x00\x0c\x03\x80'\
b'\x0c\x01\xc0\x3f\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x10\x00\x00\x00\x00\x00\x3f\x80\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x02\x0c\x02\x0c\x02\x0c\x06\x0c\x0e\x3f\xfe\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00\x7e\x00\xf8\x1e'\
b'\x00\xe0\x0f\x01\xe0\x0b\x01\x60\x0b\x81\x60\x09\x81\x60\x09\x82'\
b'\x60\x09\xc2\x60\x08\xc2\x60\x08\xc4\x60\x08\xe4\x60\x08\x64\x60'\
b'\x08\x68\x60\x08\x78\x60\x08\x38\x60\x08\x30\x60\x1c\x30\x60\x7f'\
b'\x11\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x00'\
b'\x00\x00\x00\x00\x00\x00\x7c\x07\xf0\x1e\x01\xc0\x0e\x00\x80\x0f'\
b'\x00\x80\x0b\x80\x80\x09\xc0\x80\x08\xc0\x80\x08\x60\x80\x08\x70'\
b'\x80\x08\x30\x80\x08\x18\x80\x08\x1c\x80\x08\x0e\x80\x08\x07\x80'\
b'\x08\x03\x80\x08\x03\x80\x1c\x01\x80\x7f\x00\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\xf8\x00\x0e\x0e\x00\x18\x03\x00\x18\x03\x00\x38\x03\x80\x30'\
b'\x01\x80\x70\x01\xc0\x70\x01\xc0\x70\x01\xc0\x70\x01\xc0\x70\x01'\
b'\xc0\x70\x01\xc0\x30\x01\x80\x38\x03\x80\x18\x03\x00\x18\x03\x00'\
b'\x0e\x0e\x00\x03\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x10\x00\x00\x00\x00\x00\x3f\xf0\x0c\x1c\x0c\x0c\x0c\x0e'\
b'\x0c\x0e\x0c\x0e\x0c\x0e\x0c\x0c\x0c\x1c\x0f\xf0\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x3f\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x03\xf8\x00\x0e'\
b'\x0e\x00\x18\x03\x00\x18\x03\x00\x38\x03\x80\x30\x01\x80\x70\x01'\
b'\xc0\x70\x01\xc0\x70\x01\xc0\x70\x01\xc0\x70\x01\xc0\x71\xe1\xc0'\
b'\x32\x31\x80\x34\x13\x80\x1c\x1b\x00\x1c\x0b\x00\x0e\x0e\x00\x03'\
b'\xfc\x00\x00\x0c\x40\x00\x06\x40\x00\x07\x80\x00\x03\x00\x12\x00'\
b'\x00\x00\x00\x00\x00\x00\x3f\xf0\x00\x0c\x1c\x00\x0c\x0c\x00\x0c'\
b'\x0e\x00\x0c\x0e\x00\x0c\x0e\x00\x0c\x0c\x00\x0c\x18\x00\x0f\xe0'\
b'\x00\x0c\x70\x00\x0c\x38\x00\x0c\x18\x00\x0c\x1c\x00\x0c\x1c\x00'\
b'\x0c\x0c\x80\x0c\x0c\x80\x0c\x0f\x00\x3f\x07\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\xc8'\
b'\x38\x78\x20\x18\x60\x18\x60\x08\x70\x08\x3c\x00\x1f\x00\x07\xc0'\
b'\x01\xf0\x00\x78\x00\x1c\x40\x0c\x40\x0c\x60\x0c\x60\x18\x78\x38'\
b'\x4f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00\x00\x00'\
b'\x00\x00\x7f\xfe\x00\x71\x8e\x00\x61\x86\x00\x41\x82\x00\x41\x82'\
b'\x00\x41\x82\x00\x01\x80\x00\x01\x80\x00\x01\x80\x00\x01\x80\x00'\
b'\x01\x80\x00\x01\x80\x00\x01\x80\x00\x01\x80\x00\x01\x80\x00\x01'\
b'\x80\x00\x01\x80\x00\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x3f\x07\xc0\x0c'\
b'\x03\x80\x0c\x01\x00\x0c\x01\x00\x0c\x01\x00\x0c\x01\x00\x0c\x01'\
b'\x00\x0c\x01\x00\x0c\x01\x00\x0c\x01\x00\x0c\x01\x00\x0c\x01\x00'\
b'\x0c\x01\x00\x0c\x01\x00\x0e\x03\x00\x06\x02\x00\x07\x8e\x00\x01'\
b'\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00'\
b'\x00\x00\x00\x00\x00\x00\xfe\x07\xc0\x38\x01\x00\x18\x01\x00\x1c'\
b'\x02\x00\x1c\x02\x00\x0c\x02\x00\x0e\x04\x00\x06\x04\x00\x07\x08'\
b'\x00\x07\x08\x00\x03\x08\x00\x03\x90\x00\x01\x90\x00\x01\xa0\x00'\
b'\x01\xe0\x00\x00\xe0\x00\x00\xc0\x00\x00\x40\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xfe\x3f\x8f\x80\x38\x0e\x02\x00\x38\x0e\x02\x00\x18\x0e'\
b'\x02\x00\x18\x16\x04\x00\x1c\x17\x04\x00\x0c\x13\x04\x00\x0c\x13'\
b'\x04\x00\x0e\x23\x88\x00\x06\x21\x88\x00\x06\x21\x88\x00\x07\x41'\
b'\xd0\x00\x03\x40\xd0\x00\x03\xc0\xf0\x00\x03\x80\xf0\x00\x01\x80'\
b'\x60\x00\x01\x80\x60\x00\x00\x80\x20\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x00\x00'\
b'\x00\x00\x7f\x8f\x80\x1e\x06\x00\x0e\x04\x00\x07\x08\x00\x07\x10'\
b'\x00\x03\x90\x00\x01\xa0\x00\x01\xc0\x00\x00\xe0\x00\x00\xe0\x00'\
b'\x01\x70\x00\x01\x38\x00\x02\x1c\x00\x04\x1c\x00\x04\x0e\x00\x08'\
b'\x07\x00\x18\x07\x80\xfc\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\xfc\x3f\x00\x38'\
b'\x0c\x00\x18\x08\x00\x1c\x18\x00\x0c\x10\x00\x0e\x30\x00\x06\x20'\
b'\x00\x07\x60\x00\x03\x40\x00\x03\xc0\x00\x01\x80\x00\x01\x80\x00'\
b'\x01\x80\x00\x01\x80\x00\x01\x80\x00\x01\x80\x00\x01\x80\x00\x07'\
b'\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x3f\xfe\x38\x0c\x30\x1c\x20\x18\x20\x30\x00\x70'\
b'\x00\x60\x00\xc0\x01\xc0\x01\x80\x03\x00\x07\x00\x0e\x00\x0c\x02'\
b'\x18\x02\x38\x06\x30\x0e\x7f\xfe\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x3e\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\x30\x30\x30\x30\x30\x30\x30\x30\x3e\x00\x0b\x00\x00\x00\x00\x00'\
b'\xc0\x00\xc0\x00\x60\x00\x60\x00\x30\x00\x30\x00\x18\x00\x18\x00'\
b'\x0c\x00\x0c\x00\x06\x00\x06\x00\x03\x00\x03\x00\x01\x80\x01\x80'\
b'\x00\xc0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00'\
b'\xf8\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18'\
b'\x18\x18\x18\x18\xf8\x00\x0c\x00\x00\x00\x00\x00\x06\x00\x06\x00'\
b'\x0f\x00\x0f\x00\x19\x80\x19\x80\x30\xc0\x30\xc0\x60\x60\x60\x60'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\xf0\xff\xf0\x00\x00\x00\x00'

_index =\
b'\x00\x00\x1a\x00\x34\x00\x4e\x00\x80\x00\xb2\x00\xe4\x00\x2e\x01'\
b'\x78\x01\x92\x01\xc4\x01\xde\x01\x10\x02\x42\x02\x5c\x02\x76\x02'\
b'\x90\x02\xaa\x02\xdc\x02\x0e\x03\x40\x03\x72\x03\xa4\x03\xd6\x03'\
b'\x08\x04\x3a\x04\x6c\x04\x9e\x04\xb8\x04\xd2\x04\x04\x05\x36\x05'\
b'\x68\x05\x9a\x05\xe4\x05\x2e\x06\x78\x06\xc2\x06\x0c\x07\x3e\x07'\
b'\x70\x07\xba\x07\x04\x08\x36\x08\x68\x08\xb2\x08\xe4\x08\x2e\x09'\
b'\x78\x09\xc2\x09\xf4\x09\x3e\x0a\x88\x0a\xba\x0a\x04\x0b\x4e\x0b'\
b'\x98\x0b\xfa\x0b\x44\x0c\x8e\x0c\xc0\x0c\xda\x0c\x0c\x0d\x26\x0d'\
b'\x58\x0d\x8a\x0d'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 24
    return _mvfont[doff + 2:next_offs], 24, width
 