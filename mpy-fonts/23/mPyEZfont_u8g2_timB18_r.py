'''
    mPyEZfont_u8g2_timB18_r.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original timB18.bdf font file was sourced from the U8G2 project:
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
# Font: timB18.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -l 127 -e 32 ../u8g2/tools/font/bdf/timB18.bdf 0 tmp_mPyEZfont_u8g2_timB18_r.py
version = '0.33'

def height():
    return 23

def baseline():
    return 18

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
    return 127

_font =\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x18\x3c\x3c\x3c\x3c\x3c\x18\x18\x18\x18\x18\x00\x00'\
b'\x18\x3c\x3c\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x39\xc0\x39\xc0\x39\xc0\x39\xc0\x39\xc0\x39\xc0'\
b'\x10\x80\x10\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x0c\xc0\x0c\xc0\x0c\xc0\x0c\xc0\x7f\xf0\x7f\xf0'\
b'\x19\x80\x19\x80\x19\x80\x19\x80\xff\xe0\xff\xe0\x33\x00\x33\x00'\
b'\x33\x00\x33\x00\x33\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x04\x00\x04\x00\x1f\x80\x35\xc0\x74\xc0\x74\xc0\x7c\x40'\
b'\x3e\x00\x3f\x00\x1f\x80\x0f\xc0\x07\xc0\x05\xe0\x44\xe0\x64\xe0'\
b'\x64\xc0\x75\xc0\x1f\x00\x04\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x0f\x06\x00\x1d\xfe\x00\x38\x8c\x00\x70\x98'\
b'\x00\x71\x18\x00\x71\x30\x00\x7a\x30\x00\x3c\x60\x00\x00\x60\x00'\
b'\x00\xc7\x80\x00\xce\xc0\x01\x9c\x40\x01\xb8\x40\x03\x38\x80\x03'\
b'\x38\x80\x06\x3d\x00\x06\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x15\x00\x00\x00\x00\x01\xf0\x00'\
b'\x03\x38\x00\x07\x18\x00\x07\x18\x00\x07\x38\x00\x03\xf0\x00\x07'\
b'\x87\xc0\x0f\xc3\x80\x19\xe1\x00\x30\xf3\x00\x70\xfe\x00\x70\x7c'\
b'\x00\x70\x3c\x00\x78\x3e\x00\x7c\x7f\xc0\x3f\xcf\x80\x1f\x87\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x38\x38\x38\x38\x38\x38\x10\x10\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x04\x0c\x18\x18\x38\x30\x30\x70\x70\x70\x70\x70\x70'\
b'\x70\x30\x30\x38\x18\x18\x0c\x04\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x40\x60\x30\x30\x18\x18\x18\x1c\x1c\x1c\x1c\x1c\x1c'\
b'\x1c\x18\x18\x18\x30\x30\x60\x40\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x06\x00\x06\x00\x26\x40\x76\xe0\x3f\xc0\x0f\x00'\
b'\x3f\xc0\x76\xe0\x26\x40\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x7f\xf8\x7f\xf8\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x30\x78\x78\x38\x18\x30\x30\x60\x40\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7e\x7e\x7e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x30\x78\x78\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x06\x06\x04\x0c\x0c\x08\x18\x18\x10\x30\x30\x20\x60'\
b'\x60\x40\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x0e\x00\x3b\x80\x31\x80\x71\xc0\x71\xc0\xf1\xe0'\
b'\xf1\xe0\xf1\xe0\xf1\xe0\xf1\xe0\xf1\xe0\x71\xc0\x71\xc0\x71\xc0'\
b'\x31\x80\x3b\x80\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x03\x00\x0f\x00\x3f\x00\x07\x00\x07\x00\x07\x00'\
b'\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00'\
b'\x07\x00\x0f\x80\x3f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x0f\x00\x1f\x80\x3f\xc0\x63\xc0\x41\xc0\x01\xc0'\
b'\x01\xc0\x01\x80\x03\x80\x03\x00\x06\x00\x06\x00\x0c\x20\x18\x20'\
b'\x3f\xe0\x7f\xe0\x7f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x0f\x00\x3f\x80\x63\xc0\x41\xc0\x01\xc0\x03\x80'\
b'\x07\x00\x1f\x00\x07\xc0\x01\xe0\x01\xe0\x00\xe0\x00\xe0\x60\xe0'\
b'\xf1\xc0\xfb\x80\x7e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x01\x80\x03\x80\x07\x80\x07\x80\x0f\x80\x1b\x80'\
b'\x33\x80\x33\x80\x63\x80\xc3\x80\xff\xe0\xff\xe0\xff\xe0\x03\x80'\
b'\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x1f\xe0\x1f\xc0\x3f\xc0\x30\x00\x20\x00\x70\x00'\
b'\x7f\x00\x7f\x80\x7f\xc0\x07\xc0\x01\xc0\x00\xc0\x00\xc0\x60\xc0'\
b'\xf1\x80\xfb\x80\x7e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\xf0\x03\xc0\x0f\x00\x1e\x00\x1c\x00\x3c\x00'\
b'\x3b\x80\x3d\xc0\x78\xe0\x78\xf0\x78\xf0\x78\xf0\x78\xf0\x38\xe0'\
b'\x38\xe0\x1d\xc0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x3f\xe0\x7f\xe0\x7f\xc0\xc0\xc0\x81\x80\x01\x80'\
b'\x03\x80\x03\x00\x03\x00\x07\x00\x06\x00\x06\x00\x0e\x00\x0e\x00'\
b'\x0c\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x1f\x00\x3b\x80\x71\xc0\x71\xc0\x71\xc0\x79\x80'\
b'\x3b\x00\x3f\x00\x1f\x80\x37\xc0\x63\xc0\xe1\xe0\xe1\xe0\xe1\xe0'\
b'\xf1\xc0\x7b\x80\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x0e\x00\x3b\x80\x71\xc0\x71\xc0\xf1\xe0\xf1\xe0'\
b'\xf1\xe0\xf1\xe0\x71\xe0\x3b\xc0\x1f\xc0\x03\xc0\x03\x80\x07\x80'\
b'\x0f\x00\x3c\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x18\x3c\x3c\x18\x00\x00\x00\x00'\
b'\x18\x3c\x3c\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x18\x3c\x3c\x18\x00\x00\x00\x00'\
b'\x18\x3c\x3c\x1c\x0c\x18\x18\x30\x20\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30'\
b'\x00\xf0\x03\xe0\x0f\x80\x1e\x00\x70\x00\x70\x00\x1e\x00\x0f\x80'\
b'\x03\xe0\x00\xf0\x00\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x7f\xf0\x7f\xf0\x00\x00\x00\x00\x7f\xf0\x7f\xf0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00'\
b'\x78\x00\x3e\x00\x0f\x80\x03\xc0\x00\x70\x00\x70\x03\xc0\x0f\x80'\
b'\x3e\x00\x78\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x1f\x00\x37\x80\x73\xc0\x73\xc0\x23\xc0\x03\xc0'\
b'\x07\x80\x07\x00\x0e\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x0c\x00'\
b'\x1e\x00\x1e\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x17\x00\x00\x00\x00\x00\x3e\x00\x01\xfb\xc0\x07\xc0\x60\x0f\x00'\
b'\x30\x1e\x00\x10\x1c\x1d\x98\x38\x7f\x88\x38\xf3\x88\x78\xe3\x88'\
b'\x71\xe3\x08\x71\xc7\x08\x71\xc7\x18\x71\xc7\x10\x79\xcf\x30\x78'\
b'\xff\x60\x38\x79\xc0\x3c\x00\x00\x1c\x00\x00\x0f\x00\x00\x03\xc1'\
b'\x80\x00\xfe\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00\x01\x80\x00'\
b'\x01\xc0\x00\x03\xc0\x00\x03\xe0\x00\x03\xe0\x00\x06\xe0\x00\x06'\
b'\xf0\x00\x04\x70\x00\x0c\x70\x00\x08\x78\x00\x08\x38\x00\x1f\xf8'\
b'\x00\x10\x3c\x00\x30\x3c\x00\x30\x1e\x00\x70\x1e\x00\xf8\x7f\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\xff\xc0\x3c\xf0\x3c\x78\x3c\x78\x3c\x78\x3c\x78'\
b'\x3c\x70\x3c\xc0\x3f\xe0\x3c\x78\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c'\
b'\x3c\x38\x3c\x78\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x12\x00\x00\x00\x00\x01\xf9\x00\x0f\x1f\x00\x1e\x07\x00\x3c\x03'\
b'\x00\x3c\x01\x00\x78\x01\x00\x78\x00\x00\x78\x00\x00\x78\x00\x00'\
b'\x78\x00\x00\x78\x00\x00\x78\x00\x00\x3c\x00\x00\x3c\x01\x00\x1e'\
b'\x07\x00\x0f\x9e\x00\x03\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00\x7f\xf0\x00'\
b'\x1e\x3c\x00\x1e\x1e\x00\x1e\x0f\x00\x1e\x0f\x00\x1e\x07\x80\x1e'\
b'\x07\x80\x1e\x07\x80\x1e\x07\x80\x1e\x07\x80\x1e\x07\x80\x1e\x07'\
b'\x00\x1e\x0f\x00\x1e\x0e\x00\x1e\x1e\x00\x1e\x3c\x00\x7f\xf0\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x11\x00\x00\x00\x00\x7f\xfe\x00\x1e\x0e\x00\x1e\x06\x00\x1e\x02'\
b'\x00\x1e\x02\x00\x1e\x10\x00\x1e\x10\x00\x1e\x30\x00\x1f\xf0\x00'\
b'\x1e\x30\x00\x1e\x10\x00\x1e\x10\x00\x1e\x01\x00\x1e\x01\x00\x1e'\
b'\x03\x00\x1e\x07\x00\x7f\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\xff\xfc\x3c\x1c'\
b'\x3c\x0c\x3c\x04\x3c\x04\x3c\x20\x3c\x20\x3c\x60\x3f\xe0\x3c\x60'\
b'\x3c\x20\x3c\x20\x3c\x00\x3c\x00\x3c\x00\x3c\x00\xff\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x00\x01\xf9\x00'\
b'\x0f\x1f\x00\x1e\x07\x00\x3c\x03\x00\x3c\x01\x00\x78\x01\x00\x78'\
b'\x00\x00\x78\x00\x00\x78\x00\x00\x78\x3f\xc0\x78\x0f\x00\x78\x0f'\
b'\x00\x3c\x0f\x00\x3c\x0f\x00\x1c\x0f\x00\x0f\x0f\x00\x03\xfc\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\xff\x3f\xc0\x3c\x0f\x00\x3c\x0f\x00\x3c\x0f'\
b'\x00\x3c\x0f\x00\x3c\x0f\x00\x3c\x0f\x00\x3c\x0f\x00\x3f\xff\x00'\
b'\x3c\x0f\x00\x3c\x0f\x00\x3c\x0f\x00\x3c\x0f\x00\x3c\x0f\x00\x3c'\
b'\x0f\x00\x3c\x0f\x00\xff\x3f\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\xff\x00\x3c\x00'\
b'\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00'\
b'\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\xff\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x1f\xe0\x07\x80'\
b'\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80'\
b'\x07\x80\x07\x80\x07\x80\x07\x80\xe7\x80\xe7\x80\xe7\x00\xe7\x00'\
b'\x3c\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x00\xff\x3f\x80'\
b'\x3c\x1e\x00\x3c\x18\x00\x3c\x30\x00\x3c\x60\x00\x3c\xc0\x00\x3d'\
b'\x80\x00\x3f\xc0\x00\x3f\xc0\x00\x3d\xe0\x00\x3c\xf0\x00\x3c\xf8'\
b'\x00\x3c\x7c\x00\x3c\x3e\x00\x3c\x1f\x00\x3c\x0f\x80\xff\x1f\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\xff\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00'\
b'\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x02\x3c\x06'\
b'\x3c\x0c\x3c\x1c\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x18\x00\x00\x00\x00\x7e\x00\xfc\x1e\x01\xf0\x1f\x01\xf0\x1f\x03'\
b'\xf0\x17\x82\xf0\x17\x86\xf0\x13\x84\xf0\x13\xc4\xf0\x13\xcc\xf0'\
b'\x11\xc8\xf0\x11\xf8\xf0\x11\xf8\xf0\x10\xf0\xf0\x10\xf0\xf0\x10'\
b'\x60\xf0\x10\x60\xf0\x7c\x03\xfc\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00\xf8\x0f\x80'\
b'\x7c\x07\x00\x3e\x02\x00\x3f\x02\x00\x3f\x82\x00\x2f\xc2\x00\x27'\
b'\xe2\x00\x23\xe2\x00\x21\xf2\x00\x20\xfa\x00\x20\x7e\x00\x20\x3e'\
b'\x00\x20\x1e\x00\x20\x1e\x00\x20\x0e\x00\x60\x06\x00\xf8\x02\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x03\xf0\x00\x0e\x1c\x00\x1c\x0e\x00\x3c\x0f'\
b'\x00\x38\x07\x00\x78\x07\x80\x78\x07\x80\x78\x07\x80\x78\x07\x80'\
b'\x78\x07\x80\x78\x07\x80\x78\x07\x80\x38\x07\x00\x3c\x0f\x00\x1c'\
b'\x0e\x00\x0e\x1c\x00\x03\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\xff\xe0\x3c\x78'\
b'\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x78\x3f\xe0\x3c\x00'\
b'\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\x3c\x00\xff\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x00\x03\xf0\x00'\
b'\x0e\x1c\x00\x1c\x0e\x00\x3c\x0f\x00\x38\x07\x00\x78\x07\x80\x78'\
b'\x07\x80\x78\x07\x80\x78\x07\x80\x78\x07\x80\x78\x07\x80\x78\x07'\
b'\x80\x78\x07\x00\x3c\x0f\x00\x3c\x0e\x00\x1e\x1c\x00\x0f\xf0\x00'\
b'\x03\xe0\x00\x00\xf0\x00\x00\xf8\x00\x00\x7e\x00\x00\x1f\xc0\x00'\
b'\x12\x00\x00\x00\x00\x7f\xf0\x00\x1e\x3c\x00\x1e\x1c\x00\x1e\x1e'\
b'\x00\x1e\x1e\x00\x1e\x1e\x00\x1e\x1c\x00\x1e\x38\x00\x1f\xe0\x00'\
b'\x1e\xf0\x00\x1e\x78\x00\x1e\x78\x00\x1e\x3c\x00\x1e\x3e\x00\x1e'\
b'\x1e\x00\x1e\x0f\x00\x7f\x8f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x1f\xd0\x38\xf0'\
b'\x70\x70\x70\x30\x70\x10\x7c\x00\x3f\x00\x3f\xc0\x1f\xe0\x07\xf0'\
b'\x03\xf0\x40\xf8\x40\x78\x60\x78\x70\x70\x7c\xf0\x5f\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x7f\xfe\x73\xce'\
b'\x63\xc6\x43\xc2\x43\xc2\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0'\
b'\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x0f\xf0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00\xff\x0f\x80'\
b'\x7e\x07\x00\x3c\x02\x00\x3c\x02\x00\x3c\x02\x00\x3c\x02\x00\x3c'\
b'\x02\x00\x3c\x02\x00\x3c\x02\x00\x3c\x02\x00\x3c\x02\x00\x3c\x02'\
b'\x00\x3c\x02\x00\x3c\x06\x00\x1e\x04\x00\x1f\x0c\x00\x07\xf8\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x12\x00\x00\x00\x00\xff\x1f\x80\x3c\x06\x00\x3c\x04\x00\x1e\x04'\
b'\x00\x1e\x0c\x00\x0f\x08\x00\x0f\x18\x00\x0f\x18\x00\x07\x90\x00'\
b'\x07\xb0\x00\x03\xe0\x00\x03\xe0\x00\x03\xe0\x00\x01\xc0\x00\x01'\
b'\xc0\x00\x00\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x19\x00\x00\x00\x00\x00\xff\x7f'\
b'\x9f\x00\x3c\x1e\x06\x00\x3c\x1e\x04\x00\x1e\x0f\x0c\x00\x1e\x1f'\
b'\x08\x00\x1e\x1f\x18\x00\x0f\x17\x98\x00\x0f\x37\x90\x00\x0f\x27'\
b'\xb0\x00\x07\xe3\xb0\x00\x07\xc3\xe0\x00\x07\xc3\xe0\x00\x03\xc1'\
b'\xe0\x00\x03\x81\xc0\x00\x03\x81\xc0\x00\x01\x00\x80\x00\x01\x00'\
b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00\x7f\x9f\x80'\
b'\x1f\x06\x00\x0f\x04\x00\x0f\x8c\x00\x07\x98\x00\x07\xd0\x00\x03'\
b'\xf0\x00\x01\xe0\x00\x01\xf0\x00\x01\xf0\x00\x01\xf8\x00\x03\x78'\
b'\x00\x06\x3c\x00\x04\x3e\x00\x0c\x1e\x00\x1c\x1f\x00\x7e\x7f\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x12\x00\x00\x00\x00\xff\x8f\xc0\x3e\x03\x00\x1e\x02\x00\x0f\x06'\
b'\x00\x0f\x0c\x00\x07\x8c\x00\x07\x98\x00\x03\xd0\x00\x03\xf0\x00'\
b'\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01'\
b'\xe0\x00\x01\xe0\x00\x07\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00\x00\x7f\xfc\x00'\
b'\x70\x7c\x00\x60\xf8\x00\x60\xf8\x00\x41\xf0\x00\x01\xe0\x00\x03'\
b'\xe0\x00\x03\xc0\x00\x07\xc0\x00\x07\x80\x00\x0f\x00\x00\x1f\x02'\
b'\x00\x1e\x02\x00\x3e\x06\x00\x3c\x0e\x00\x7c\x1e\x00\x7f\xfc\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x7c\x70\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x70\x7c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\xc0\xc0\x40\x60\x60\x20\x30\x30\x10\x18\x18\x08\x0c'\
b'\x0c\x04\x06\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x7c\x1c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'\
b'\x0c\x0c\x0c\x0c\x0c\x0c\x1c\x7c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x03\x00\x03\x00\x07\x80\x04\x80\x0c\xc0\x0c\xc0'\
b'\x0c\xc0\x18\x60\x18\x60\x10\x20\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\xff\xf0\xff\xf0\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x70\x38\x18\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x00'\
b'\x3b\x80\x71\xc0\x71\xc0\x21\xc0\x07\xc0\x39\xc0\x71\xc0\x71\xc0'\
b'\x73\xc0\x7f\xe0\x38\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x78\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3b\x80'\
b'\x3f\xe0\x38\xe0\x38\x70\x38\x70\x38\x70\x38\x70\x38\x70\x38\x70'\
b'\x38\xe0\x3d\xe0\x33\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00'\
b'\x39\x80\x39\xc0\x71\xc0\x70\x80\x70\x00\x70\x00\x70\x00\x78\x00'\
b'\x3c\x40\x3f\x80\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\xf0\x00\x70\x00\x70\x00\x70\x00\x70\x0f\x70'\
b'\x3f\xf0\x38\xf0\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x78\x70'\
b'\x38\xf0\x3f\x70\x0e\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00'\
b'\x39\x80\x39\xc0\x71\xc0\x71\xc0\x7f\xc0\x70\x00\x70\x00\x78\x00'\
b'\x3c\x40\x3f\x80\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x0f\x00\x19\x80\x39\x80\x38\x00\x38\x00\x7e\x00'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x60'\
b'\x3b\xe0\x71\xc0\x71\xc0\x71\xc0\x71\xc0\x39\x80\x1f\x00\x30\x00'\
b'\x70\x00\x7f\xc0\x7f\xe0\x3f\xe0\x60\xe0\x60\x60\x70\xc0\x3f\x80'\
b'\x0e\x00\x00\x00\x78\x00\x38\x00\x38\x00\x38\x00\x38\x00\x39\xe0'\
b'\x3f\xf0\x3c\x70\x38\x70\x38\x70\x38\x70\x38\x70\x38\x70\x38\x70'\
b'\x38\x70\x38\x70\x7c\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x38\x38\x38\x00\x00\x78\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\x38\x38\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x0e\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x1e\x00'\
b'\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00'\
b'\x0e\x00\x0e\x00\x0e\x00\x0e\x00\xce\x00\xce\x00\xcc\x00\x78\x00'\
b'\x0f\x00\x00\x00\x78\x00\x38\x00\x38\x00\x38\x00\x38\x00\x39\xf8'\
b'\x38\x60\x38\xc0\x39\x80\x3b\x00\x3f\x00\x3f\x80\x3b\xc0\x39\xe0'\
b'\x38\xf0\x38\x78\x7d\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x78\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\x38\x38\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x79\xe3\xc0\x3b\xef\xe0\x3c\x78\xe0\x38\x70\xe0'\
b'\x38\x70\xe0\x38\x70\xe0\x38\x70\xe0\x38\x70\xe0\x38\x70\xe0\x38'\
b'\x70\xe0\x38\x70\xe0\x7c\xf9\xf0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x79\xe0\x3b\xf0\x3c\x70\x38\x70\x38\x70'\
b'\x38\x70\x38\x70\x38\x70\x38\x70\x38\x70\x38\x70\x7c\xf8\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0f\x80\x38\xe0\x38\xe0\x70\x70\x70\x70'\
b'\x70\x70\x70\x70\x70\x70\x70\x70\x38\xe0\x38\xe0\x0f\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x71\xe0\x3b\xf0\x3c\x70\x38\x38\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\x38\x38\x3c\x70\x3b\xf0\x39\xc0\x38\x00'\
b'\x38\x00\x38\x00\x38\x00\x7e\x00\x0e\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x07\x30\x1f\xf0\x38\xf0\x38\x70\x70\x70'\
b'\x70\x70\x70\x70\x70\x70\x70\x70\x38\xf0\x3f\x70\x0e\x70\x00\x70'\
b'\x00\x70\x00\x70\x00\x70\x00\xf8\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x77\x80\x3f\xc0\x39\xc0\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x7c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x1f\x00\x33\x00\x71\x00\x70\x00\x7c\x00'\
b'\x3e\x00\x1f\x00\x0f\x80\x43\x80\x43\x80\x63\x00\x7e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x08\x18\x38\x78'\
b'\xff\x38\x38\x38\x38\x38\x38\x38\x38\x39\x3e\x1c\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x78\xf0\x38\x70\x38\x70\x38\x70\x38\x70'\
b'\x38\x70\x38\x70\x38\x70\x38\x70\x38\xf0\x3f\x78\x1e\x70\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\xfc\xf0\x70\x60\x78\x40\x38\xc0\x38\x80'\
b'\x1c\x80\x1d\x80\x1f\x00\x0f\x00\x0f\x00\x06\x00\x06\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfd\xf7\x80\x78'\
b'\xe3\x00\x38\xe3\x00\x38\xe2\x00\x3c\xe6\x00\x1d\x76\x00\x1d\x74'\
b'\x00\x1f\x3c\x00\x0e\x38\x00\x0e\x38\x00\x04\x10\x00\x04\x10\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xf0'\
b'\x78\x60\x3c\xc0\x1d\x80\x1f\x00\x0f\x00\x0f\x00\x1f\x80\x1b\xc0'\
b'\x31\xc0\x61\xe0\xf3\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfd\xf0'\
b'\x78\x60\x38\x40\x38\xc0\x3c\x80\x1c\x80\x1d\x80\x1f\x00\x0f\x00'\
b'\x0f\x00\x06\x00\x06\x00\x06\x00\x64\x00\xec\x00\xf8\x00\x70\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xc0'\
b'\x63\x80\x47\x80\x47\x00\x0f\x00\x0e\x00\x1e\x00\x1c\x00\x3c\x40'\
b'\x38\xc0\x78\xc0\x7f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x07\x00\x0c\x00\x18\x00\x18\x00\x18\x00\x18\x00'\
b'\x18\x00\x18\x00\x18\x00\x30\x00\x60\x00\x30\x00\x18\x00\x18\x00'\
b'\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x0c\x00\x07\x00\x00\x00'\
b'\x06\x00\x00\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\x30\x30\x30\x30\x30\x30\x30\x30\x30\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x70\x00\x18\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x06\x00\x03\x00\x06\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x18\x00\x70\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00'\
b'\x7e\x10\xff\x10\x8f\xf0\x87\xe0\x01\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00'

_sparse =\
b'\x20\x00\x04\x00\x21\x00\x08\x00\x22\x00\x0c\x00\x23\x00\x12\x00'\
b'\x24\x00\x18\x00\x25\x00\x1e\x00\x26\x00\x27\x00\x27\x00\x30\x00'\
b'\x28\x00\x34\x00\x29\x00\x38\x00\x2a\x00\x3c\x00\x2b\x00\x42\x00'\
b'\x2c\x00\x48\x00\x2d\x00\x4c\x00\x2e\x00\x50\x00\x2f\x00\x54\x00'\
b'\x30\x00\x58\x00\x31\x00\x5e\x00\x32\x00\x64\x00\x33\x00\x6a\x00'\
b'\x34\x00\x70\x00\x35\x00\x76\x00\x36\x00\x7c\x00\x37\x00\x82\x00'\
b'\x38\x00\x88\x00\x39\x00\x8e\x00\x3a\x00\x94\x00\x3b\x00\x98\x00'\
b'\x3c\x00\x9c\x00\x3d\x00\xa2\x00\x3e\x00\xa8\x00\x3f\x00\xae\x00'\
b'\x40\x00\xb4\x00\x41\x00\xbd\x00\x42\x00\xc6\x00\x43\x00\xcc\x00'\
b'\x44\x00\xd5\x00\x45\x00\xde\x00\x46\x00\xe7\x00\x47\x00\xed\x00'\
b'\x48\x00\xf6\x00\x49\x00\xff\x00\x4a\x00\x05\x01\x4b\x00\x0b\x01'\
b'\x4c\x00\x14\x01\x4d\x00\x1a\x01\x4e\x00\x23\x01\x4f\x00\x2c\x01'\
b'\x50\x00\x35\x01\x51\x00\x3b\x01\x52\x00\x44\x01\x53\x00\x4d\x01'\
b'\x54\x00\x53\x01\x55\x00\x59\x01\x56\x00\x62\x01\x57\x00\x6b\x01'\
b'\x58\x00\x77\x01\x59\x00\x80\x01\x5a\x00\x89\x01\x5b\x00\x92\x01'\
b'\x5c\x00\x96\x01\x5d\x00\x9a\x01\x5e\x00\x9e\x01\x5f\x00\xa4\x01'\
b'\x60\x00\xaa\x01\x61\x00\xae\x01\x62\x00\xb4\x01\x63\x00\xba\x01'\
b'\x64\x00\xc0\x01\x65\x00\xc6\x01\x66\x00\xcc\x01\x67\x00\xd2\x01'\
b'\x68\x00\xd8\x01\x69\x00\xde\x01\x6a\x00\xe2\x01\x6b\x00\xe8\x01'\
b'\x6c\x00\xee\x01\x6d\x00\xf2\x01\x6e\x00\xfb\x01\x6f\x00\x01\x02'\
b'\x70\x00\x07\x02\x71\x00\x0d\x02\x72\x00\x13\x02\x73\x00\x19\x02'\
b'\x74\x00\x1f\x02\x75\x00\x23\x02\x76\x00\x29\x02\x77\x00\x2f\x02'\
b'\x78\x00\x38\x02\x79\x00\x3e\x02\x7a\x00\x44\x02\x7b\x00\x4a\x02'\
b'\x7c\x00\x50\x02\x7d\x00\x54\x02\x7e\x00\x5a\x02\x7f\x00\x60\x02'\

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

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 23
    return _mvfont[doff + 2:next_offs], 23, width
 
