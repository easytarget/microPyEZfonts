'''
    mPyEZfont_u8g2_courB18_r.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original courB18.bdf font file was sourced from the U8G2 project:
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
# Font: courB18.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -l 127 -e 32 ../u8g2/tools/font/bdf/courB18.bdf 0 tmp_mPyEZfont_u8g2_courB18_r.py
version = '0.33'

def height():
    return 22

def baseline():
    return 17

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
    return 127

_font =\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x03\x00\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80'\
b'\x07\x80\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x00\x00\x03\x00'\
b'\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x1d\xc0\x1d\xc0\x1d\xc0\x1d\xc0\x08\x80\x08\x80'\
b'\x08\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x06\x60\x06\x60\x06\x60\x06\x60\x06\x60\x06\x60\x3f\xf8'\
b'\x3f\xf8\x0c\xc0\x0c\xc0\x0c\xc0\x7f\xf0\x7f\xf0\x19\x80\x19\x80'\
b'\x19\x80\x19\x80\x19\x80\x19\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x03\x00\x03\x00\x0f\x60\x1f\xe0\x30\xe0\x30\x60\x30\x00'\
b'\x38\x00\x1f\x80\x07\xe0\x00\x70\x00\x30\x30\x30\x38\x70\x3f\xe0'\
b'\x37\xc0\x03\x00\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x0f\x00\x19\x80\x30\xc0\x30\xc0\x19\x80'\
b'\x0f\x00\x00\x70\x03\xc0\x0e\x00\x39\xe0\x03\x30\x06\x18\x06\x18'\
b'\x03\x30\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x07\x80\x0f\xc0\x18\xc0\x18\x00'\
b'\x18\x00\x0c\x00\x0e\x00\x1f\x30\x1b\xf0\x31\xe0\x30\xc0\x31\xe0'\
b'\x3f\xf8\x1f\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00'\
b'\x02\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x60\x00\xe0\x00\xc0\x01\x80\x01\x80\x01\x80'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x01\x80\x01\x80\x01\x80\x00\xc0\x00\xe0\x00\x60\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x18\x00\x1c\x00\x0c\x00\x06\x00\x06\x00\x06\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x06\x00\x06\x00\x06\x00\x0c\x00\x1c\x00\x18\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x03\x00\x03\x00\x03\x00\x33\x30\x3f\xf0\x0f\xc0'\
b'\x03\x00\x0f\xc0\x0c\xc0\x1c\xe0\x18\x60\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x7f\xf8\x7f\xf8\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80'\
b'\x03\x80\x07\x00\x06\x00\x0c\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x3f\xf8\x3f\xf8\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'\
b'\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x18\x00\x18\x00\x30\x00\x30\x00\x60\x00\x60\x00\xc0'\
b'\x00\xc0\x01\x80\x01\x80\x03\x00\x03\x00\x06\x00\x06\x00\x0c\x00'\
b'\x0c\x00\x18\x00\x18\x00\x30\x00\x30\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x07\x80\x1f\xe0\x18\x60\x30\x30\x30\x30\x30\x30'\
b'\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x18\x60'\
b'\x1f\xe0\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x07\x00\x3f\x00\x3f\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x3f\xf0\x3f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x0f\xc0\x1f\xe0\x38\x70\x30\x30\x30\x30\x00\x30'\
b'\x00\x70\x00\xe0\x01\xc0\x03\x80\x07\x00\x0e\x00\x1c\x00\x38\x00'\
b'\x7f\xf0\x7f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x0f\xc0\x1f\xe0\x38\x70\x30\x30\x00\x30\x00\x70'\
b'\x00\xe0\x07\xc0\x07\xe0\x00\x70\x00\x30\x00\x30\x60\x30\x70\x70'\
b'\x3f\xe0\x1f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x01\xc0\x03\xc0\x07\xc0\x06\xc0\x0c\xc0\x0c\xc0'\
b'\x18\xc0\x18\xc0\x30\xc0\x30\xc0\x7f\xf0\x7f\xf0\x00\xc0\x00\xc0'\
b'\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x1f\xf0\x1f\xf0\x18\x00\x18\x00\x18\x00\x1b\xc0'\
b'\x1f\xf0\x1c\x70\x00\x38\x00\x18\x00\x18\x00\x18\x30\x38\x38\x70'\
b'\x1f\xf0\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x01\xf0\x07\xf0\x0f\x00\x1c\x00\x18\x00\x38\x00'\
b'\x37\xc0\x3f\xe0\x38\x70\x30\x30\x30\x30\x30\x30\x38\x30\x1c\x70'\
b'\x1f\xe0\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x3f\xf0\x3f\xf0\x30\x30\x00\x30\x00\x60\x00\x60'\
b'\x00\x60\x00\xc0\x00\xc0\x00\xc0\x01\x80\x01\x80\x01\x80\x03\x00'\
b'\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x07\x80\x1f\xe0\x38\x70\x30\x30\x30\x30\x30\x30'\
b'\x18\x60\x0f\xc0\x1f\xe0\x38\x70\x30\x30\x30\x30\x30\x30\x38\x70'\
b'\x1f\xe0\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x03\xc0\x0f\xf0\x0c\x30\x18\x18\x18\x18\x18\x18'\
b'\x18\x18\x18\x38\x1c\x78\x0f\xd8\x07\x98\x00\x18\x00\x30\x00\x70'\
b'\x1f\xe0\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'\
b'\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'\
b'\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'\
b'\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'\
b'\x07\x00\x0e\x00\x0c\x00\x18\x00\x10\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x78\x01\xe0'\
b'\x07\x80\x1e\x00\x78\x00\x78\x00\x1e\x00\x07\x80\x01\xe0\x00\x78'\
b'\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x7f\xf8\x7f\xf8\x00\x00\x00\x00\x7f\xf8\x7f\xf8\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\x00\x3c\x00\x0f\x00'\
b'\x03\xc0\x00\xf0\x00\x3c\x00\x3c\x00\xf0\x03\xc0\x0f\x00\x3c\x00'\
b'\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x0f\xc0\x1f\xe0\x18\x70\x18\x30\x18\x30'\
b'\x00\x30\x00\x70\x01\xe0\x03\x80\x03\x00\x03\x00\x00\x00\x03\x00'\
b'\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x07\x00\x1f\xc0\x18\xc0\x30\x60\x30\x60\x31\xe0'\
b'\x33\xe0\x37\x60\x36\x60\x36\x60\x37\x60\x33\xf0\x31\xf0\x30\x00'\
b'\x30\x00\x18\x60\x1f\xe0\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x3f\x00\x3f\x00\x07\x80\x07\x80\x0c\xc0'\
b'\x0c\xc0\x1c\xe0\x18\x60\x18\x60\x3f\xf0\x3f\xf0\x70\x38\x60\x18'\
b'\xfc\xfc\xfc\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x7f\xe0\x7f\xf0\x18\x38\x18\x18\x18\x18'\
b'\x18\x38\x1f\xf0\x1f\xf8\x18\x1c\x18\x0c\x18\x0c\x18\x0c\x18\x1c'\
b'\x7f\xf8\x7f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x07\xd8\x1f\xf8\x38\x38\x30\x18\x70\x18'\
b'\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x70\x00\x30\x00\x38\x18'\
b'\x1f\xf8\x07\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\xff\xc0\xff\xf0\x30\x38\x30\x18\x30\x1c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x18\x30\x38'\
b'\xff\xf0\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x7f\xf8\x7f\xf8\x18\x18\x18\x18\x18\xd8'\
b'\x18\xc0\x1f\xc0\x1f\xc0\x18\xc0\x18\xc0\x18\x0c\x18\x0c\x18\x0c'\
b'\x7f\xfc\x7f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x7f\xfc\x7f\xfc\x18\x0c\x18\x0c\x18\xcc'\
b'\x18\xc0\x1f\xc0\x1f\xc0\x18\xc0\x18\xc0\x18\x00\x18\x00\x18\x00'\
b'\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x07\xec\x1f\xfc\x38\x1c\x30\x0c\x70\x0c'\
b'\x60\x00\x60\x00\x60\x00\x60\xfc\x60\xfc\x70\x0c\x30\x0c\x38\x1c'\
b'\x1f\xf8\x07\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\xfc\xfc\xfc\xfc\x30\x30\x30\x30\x30\x30'\
b'\x30\x30\x3f\xf0\x3f\xf0\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\xfc\xfc\xfc\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x3f\xf0\x3f\xf0\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x3f\xf0\x3f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x0f\xfc\x0f\xfc\x00\x60\x00\x60\x00\x60'\
b'\x00\x60\x00\x60\x00\x60\x00\x60\x60\x60\x60\x60\x60\x60\x70\xe0'\
b'\x3f\xc0\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\xfc\xf8\xfc\xf8\x30\xe0\x31\xc0\x33\x80'\
b'\x37\x00\x3e\x00\x3f\x00\x3b\x80\x31\xc0\x30\xe0\x30\x60\x30\x70'\
b'\xfc\x3c\xfc\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x7f\x80\x7f\x80\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x18\x0c\x18\x0c\x18'\
b'\x7f\xf8\x7f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\xf0\x3c\xf0\x3c\x78\x78\x78\x78\x6c\xd8'\
b'\x6c\xd8\x6c\xd8\x67\x98\x63\x18\x63\x18\x60\x18\x60\x18\x60\x18'\
b'\xf8\x7c\xf8\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x78\x7c\x78\x7c\x3c\x18\x3c\x18\x36\x18'\
b'\x36\x18\x33\x18\x33\x18\x31\x98\x31\x98\x30\xd8\x30\xd8\x30\x78'\
b'\x7c\x78\x7c\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x07\xc0\x1f\xf0\x38\x38\x30\x18\x70\x1c'\
b'\x60\x0c\x60\x0c\x60\x0c\x60\x0c\x60\x0c\x70\x1c\x30\x18\x38\x38'\
b'\x1f\xf0\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x7f\xe0\x7f\xf8\x18\x1c\x18\x0c\x18\x0c'\
b'\x18\x0c\x18\x0c\x18\x1c\x1f\xf8\x1f\xe0\x18\x00\x18\x00\x18\x00'\
b'\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x07\xc0\x1f\xf0\x38\x38\x30\x18\x70\x1c'\
b'\x60\x0c\x60\x0c\x60\x0c\x60\x0c\x60\x0c\x70\x1c\x30\x18\x38\x38'\
b'\x1f\xf0\x07\xc0\x07\x0c\x1f\xfc\x1c\xf0\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\xff\x80\xff\xe0\x30\x70\x30\x30\x30\x30'\
b'\x30\x30\x30\x70\x3f\xe0\x3f\x80\x31\xc0\x30\xe0\x30\x60\x30\x70'\
b'\xfc\x3c\xfc\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x0f\xd8\x1f\xf8\x38\x38\x30\x18\x30\x18'\
b'\x38\x00\x1f\x00\x0f\xe0\x01\xf0\x00\x38\x60\x18\x60\x18\x70\x38'\
b'\x7f\xf0\x6f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x7f\xf8\x7f\xf8\x63\x18\x63\x18\x63\x18'\
b'\x63\x18\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x1f\xe0\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x7c\x7c\x7c\x7c\x30\x18\x30\x18\x30\x18'\
b'\x30\x18\x30\x18\x30\x18\x30\x18\x30\x18\x30\x18\x30\x18\x18\x30'\
b'\x1f\xf0\x0f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\xf8\x7c\xf8\x7c\x60\x18\x60\x18\x30\x30'\
b'\x30\x30\x30\x30\x18\x60\x18\x60\x18\x60\x0c\xc0\x0c\xc0\x07\x80'\
b'\x07\x80\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\xf8\x7c\xf8\x7c\x60\x18\x63\x18\x63\x18'\
b'\x67\x98\x67\x98\x6f\xd8\x6c\xd8\x6c\xd8\x3c\xf0\x38\x70\x38\x70'\
b'\x38\x70\x38\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\xfc\xfc\xfc\xfc\x70\x38\x38\x70\x1c\xe0'\
b'\x0f\xc0\x07\x80\x03\x00\x07\x80\x0c\xc0\x1c\xe0\x38\x70\x70\x38'\
b'\xfc\xfc\xfc\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\xfc\xfc\xfc\xfc\x70\x38\x38\x70\x18\x60'\
b'\x0c\xc0\x0f\xc0\x07\x80\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x1f\xe0\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x3f\xf8\x3f\xf8\x30\x38\x30\x70\x30\xe0'\
b'\x00\xc0\x01\xc0\x03\x80\x07\x00\x06\x00\x0e\x18\x1c\x18\x38\x18'\
b'\x3f\xf8\x3f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x03\xe0\x03\xe0\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\xe0\x03\xe0\x00\x00\x00\x00'\
b'\x0f\x00\x30\x00\x30\x00\x18\x00\x18\x00\x0c\x00\x0c\x00\x06\x00'\
b'\x06\x00\x03\x00\x03\x00\x01\x80\x01\x80\x00\xc0\x00\xc0\x00\x60'\
b'\x00\x60\x00\x30\x00\x30\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x1f\x00\x1f\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x1f\x00\x1f\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x03\x00\x03\x00\x07\x80\x07\x80\x0c\xc0\x0c\xc0'\
b'\x18\x60\x18\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\xff\xfe\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x0c\x00\x06\x00\x03\x00\x01\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80'\
b'\x3f\xc0\x30\xe0\x00\x60\x0f\xe0\x3f\xe0\x70\x60\x60\x60\x60\xe0'\
b'\x7f\xf8\x3f\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x78\x00\x78\x00\x18\x00\x18\x00\x18\x00\x1b\xe0'\
b'\x1f\xf8\x1e\x38\x1c\x1c\x18\x0c\x18\x0c\x18\x0c\x1c\x1c\x1e\x38'\
b'\x7f\xf8\x7b\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xd8'\
b'\x3f\xf8\x38\x78\x70\x38\x60\x18\x60\x00\x60\x00\x70\x00\x38\x38'\
b'\x3f\xf8\x0f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\xf0\x00\xf0\x00\x30\x00\x30\x00\x30\x0f\xb0'\
b'\x3f\xf0\x38\xf0\x70\x70\x60\x30\x60\x30\x60\x30\x70\x70\x38\xf0'\
b'\x3f\xfc\x0f\xbc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xc0'\
b'\x3f\xf0\x38\x70\x70\x38\x60\x18\x7f\xf8\x7f\xf8\x70\x00\x38\x38'\
b'\x3f\xf8\x0f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x01\xf8\x03\xf8\x07\x00\x06\x00\x06\x00\x3f\xf0'\
b'\x3f\xf0\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x3f\xf0\x3f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xbc'\
b'\x3f\xfc\x38\xf0\x70\x70\x60\x30\x60\x30\x60\x30\x70\x70\x38\xf0'\
b'\x3f\xf0\x0f\xb0\x00\x30\x00\x30\x00\x70\x1f\xe0\x1f\xc0\x00\x00'\
b'\x0f\x00\x00\x00\xf0\x00\xf0\x00\x30\x00\x30\x00\x30\x00\x37\xc0'\
b'\x3f\xe0\x3c\x70\x38\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\xfc\xfc\xfc\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x07\x00\x07\x00\x07\x00\x00\x00\x00\x00\x1f\x00'\
b'\x1f\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x3f\xf0\x3f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x3f\xc0'\
b'\x3f\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0'\
b'\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x01\xc0\x3f\x80\x3f\x00\x00\x00'\
b'\x0f\x00\x00\x00\x78\x00\x78\x00\x18\x00\x18\x00\x18\x00\x18\xf0'\
b'\x18\xf0\x19\xc0\x1b\x80\x1f\x00\x1f\x00\x1b\x80\x19\xc0\x18\xe0'\
b'\x78\xfc\x78\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x1f\x00\x1f\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x3f\xf0\x3f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xef\x78'\
b'\xff\xfc\x39\xcc\x31\x8c\x31\x8c\x31\x8c\x31\x8c\x31\x8c\x31\x8c'\
b'\xf9\xef\xf9\xef\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf3\xc0'\
b'\xf7\xe0\x3c\x70\x38\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\xfc\xfc\xfc\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xc0'\
b'\x3f\xf0\x38\x70\x70\x38\x60\x18\x60\x18\x60\x18\x70\x38\x38\x70'\
b'\x3f\xf0\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\xc0'\
b'\xff\xf0\x3c\x70\x38\x38\x30\x18\x30\x18\x30\x18\x38\x38\x3c\x70'\
b'\x3f\xf0\x37\xc0\x30\x00\x30\x00\x30\x00\xfe\x00\xfe\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xbc'\
b'\x3f\xfc\x38\xf0\x70\x70\x60\x30\x60\x30\x60\x30\x70\x70\x38\xf0'\
b'\x3f\xf0\x0f\xb0\x00\x30\x00\x30\x00\x30\x01\xfc\x01\xfc\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\xf0'\
b'\x3f\xf8\x0f\x18\x0e\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x7f\xe0\x7f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xb0'\
b'\x1f\xf0\x38\x70\x38\x30\x1f\x00\x07\xc0\x01\xf0\x30\x38\x38\x38'\
b'\x3f\xf0\x37\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x18\x00\x18\x00\x18\x00\x18\x00\x7f\xe0'\
b'\x7f\xe0\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x1c\x70'\
b'\x0f\xf0\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0'\
b'\xf0\xf0\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x38\x70'\
b'\x1f\xfc\x0f\xbc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xfc'\
b'\xfc\xfc\x30\x30\x30\x30\x18\x60\x18\x60\x0c\xc0\x0c\xc0\x07\x80'\
b'\x07\x80\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x7c'\
b'\xf8\x7c\x63\x18\x63\x18\x33\x30\x37\xb0\x37\xb0\x3c\xf0\x1c\xe0'\
b'\x18\x60\x18\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7c\xf8'\
b'\x7c\xf8\x18\x60\x0c\xc0\x07\x80\x03\x00\x07\x80\x0c\xc0\x18\x60'\
b'\x7c\xf8\x7c\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7c\xf8'\
b'\x7c\xf8\x30\x30\x38\x70\x18\x60\x1c\xe0\x0c\xc0\x0d\xc0\x07\x80'\
b'\x07\x80\x03\x00\x07\x00\x06\x00\x0e\x00\x7f\x00\x7f\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xf0'\
b'\x3f\xf0\x30\xe0\x31\xc0\x03\x80\x07\x00\x0e\x00\x1c\x30\x38\x30'\
b'\x3f\xf0\x3f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\xe0\x01\x80\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x07\x00\x0e\x00\x07\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x01\x80\x00\xe0\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x1c\x00\x06\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x80\x01\xc0\x03\x80\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x06\x00\x1c\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1e\x18\x3f\x38\x73\xf0\x61\xe0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00'

_sparse =\
b'\x20\x00\x06\x00\x21\x00\x0c\x00\x22\x00\x12\x00\x23\x00\x18\x00'\
b'\x24\x00\x1e\x00\x25\x00\x24\x00\x26\x00\x2a\x00\x27\x00\x30\x00'\
b'\x28\x00\x36\x00\x29\x00\x3c\x00\x2a\x00\x42\x00\x2b\x00\x48\x00'\
b'\x2c\x00\x4e\x00\x2d\x00\x54\x00\x2e\x00\x5a\x00\x2f\x00\x60\x00'\
b'\x30\x00\x66\x00\x31\x00\x6c\x00\x32\x00\x72\x00\x33\x00\x78\x00'\
b'\x34\x00\x7e\x00\x35\x00\x84\x00\x36\x00\x8a\x00\x37\x00\x90\x00'\
b'\x38\x00\x96\x00\x39\x00\x9c\x00\x3a\x00\xa2\x00\x3b\x00\xa8\x00'\
b'\x3c\x00\xae\x00\x3d\x00\xb4\x00\x3e\x00\xba\x00\x3f\x00\xc0\x00'\
b'\x40\x00\xc6\x00\x41\x00\xcc\x00\x42\x00\xd2\x00\x43\x00\xd8\x00'\
b'\x44\x00\xde\x00\x45\x00\xe4\x00\x46\x00\xea\x00\x47\x00\xf0\x00'\
b'\x48\x00\xf6\x00\x49\x00\xfc\x00\x4a\x00\x02\x01\x4b\x00\x08\x01'\
b'\x4c\x00\x0e\x01\x4d\x00\x14\x01\x4e\x00\x1a\x01\x4f\x00\x20\x01'\
b'\x50\x00\x26\x01\x51\x00\x2c\x01\x52\x00\x32\x01\x53\x00\x38\x01'\
b'\x54\x00\x3e\x01\x55\x00\x44\x01\x56\x00\x4a\x01\x57\x00\x50\x01'\
b'\x58\x00\x56\x01\x59\x00\x5c\x01\x5a\x00\x62\x01\x5b\x00\x68\x01'\
b'\x5c\x00\x6e\x01\x5d\x00\x74\x01\x5e\x00\x7a\x01\x5f\x00\x80\x01'\
b'\x60\x00\x86\x01\x61\x00\x8c\x01\x62\x00\x92\x01\x63\x00\x98\x01'\
b'\x64\x00\x9e\x01\x65\x00\xa4\x01\x66\x00\xaa\x01\x67\x00\xb0\x01'\
b'\x68\x00\xb6\x01\x69\x00\xbc\x01\x6a\x00\xc2\x01\x6b\x00\xc8\x01'\
b'\x6c\x00\xce\x01\x6d\x00\xd4\x01\x6e\x00\xda\x01\x6f\x00\xe0\x01'\
b'\x70\x00\xe6\x01\x71\x00\xec\x01\x72\x00\xf2\x01\x73\x00\xf8\x01'\
b'\x74\x00\xfe\x01\x75\x00\x04\x02\x76\x00\x0a\x02\x77\x00\x10\x02'\
b'\x78\x00\x16\x02\x79\x00\x1c\x02\x7a\x00\x22\x02\x7b\x00\x28\x02'\
b'\x7c\x00\x2e\x02\x7d\x00\x34\x02\x7e\x00\x3a\x02\x7f\x00\x40\x02'\

_mvfont = memoryview(_font)
_mvsp = memoryview(_sparse)
ifb = lambda l : l[0] | (l[1] << 8)

def bs(lst, val):
    while True:
        m = (len(lst) & ~ 7) >> 1
        v = ifb(lst[m:])
        if v == val:
            return ifb(lst[m + 2:])
        if not m:
            return 0
        lst = lst[m:] if v < val else lst[:m]

def get_ch(ch):
    doff = bs(_mvsp, ord(ch)) << 3
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 22
    return _mvfont[doff + 2:next_offs], 22, width
 
