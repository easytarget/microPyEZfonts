'''
    mPyEZfont_u8g2_courB12_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original courB12.bdf font file was sourced from the U8G2 project:
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
# Font: courB12.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/u-char.set u8g2/tools/font/bdf/courB12.bdf 0 tmp_mPyEZfont_u8g2_courB12_u.py
version = '0.33'

def height():
    return 15

def baseline():
    return 12

def max_width():
    return 10

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
b'\x0a\x00\x00\x00\x00\x00\x3e\x00\x63\x00\x63\x00\x03\x00\x0e\x00'\
b'\x18\x00\x18\x00\x00\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00'\
b'\x18\x00\x18\x00\x00\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x33\x00\x33\x00\x33\x00\x33\x00\x33\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x36\x00\x36\x00\x36\x00\x36\x00\xff\x80\x36\x00'\
b'\x36\x00\xff\x80\x36\x00\x36\x00\x36\x00\x36\x00\x00\x00\x00\x00'\
b'\x0a\x00\x0c\x00\x0c\x00\x3f\x00\x63\x00\x60\x00\x70\x00\x3e\x00'\
b'\x07\x00\x03\x00\x63\x00\x7e\x00\x18\x00\x18\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x3c\x00\x66\x00\x66\x00\x3c\x00\x03\x80\x1e\x00'\
b'\x70\x00\x0f\x00\x19\x80\x19\x80\x0f\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x36\x00\x30\x00\x18\x00'\
b'\x3b\x00\x6f\x00\x66\x00\x66\x00\x3f\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x06\x00\x0c\x00\x0c\x00\x0c\x00\x18\x00\x18\x00'\
b'\x18\x00\x18\x00\x18\x00\x0c\x00\x0c\x00\x0c\x00\x06\x00\x00\x00'\
b'\x0a\x00\x00\x00\x30\x00\x18\x00\x18\x00\x18\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x18\x00\x18\x00\x18\x00\x30\x00\x00\x00'\
b'\x0a\x00\x00\x00\x0c\x00\x0c\x00\x7f\x80\x1e\x00\x1e\x00\x33\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80'\
b'\x7f\x80\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00\x0c\x00\x18\x00\x10\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00'\
b'\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x03\x00\x03\x00\x06\x00\x06\x00\x06\x00\x0c\x00\x0c\x00'\
b'\x18\x00\x18\x00\x18\x00\x30\x00\x30\x00\x60\x00\x60\x00\x00\x00'\
b'\x0a\x00\x00\x00\x1e\x00\x33\x00\x33\x00\x61\x80\x61\x80\x61\x80'\
b'\x61\x80\x61\x80\x33\x00\x33\x00\x1e\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x0c\x00\x3c\x00\x6c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x3c\x00\x66\x00\x43\x00\x03\x00\x03\x00\x06\x00'\
b'\x0c\x00\x18\x00\x30\x00\x63\x00\x7f\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x3c\x00\x66\x00\x43\x00\x06\x00\x1c\x00\x06\x00'\
b'\x03\x00\x03\x00\x43\x00\x66\x00\x3c\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x03\x00\x07\x00\x0f\x00\x1b\x00\x33\x00\x23\x00'\
b'\x63\x00\x7f\x80\x03\x00\x03\x00\x0f\x80\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x7f\x00\x60\x00\x60\x00\x60\x00\x7e\x00\x63\x00'\
b'\x03\x00\x03\x00\x03\x00\x66\x00\x7c\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x0f\x00\x38\x00\x30\x00\x60\x00\x6e\x00\x73\x00'\
b'\x61\x80\x61\x80\x61\x80\x33\x00\x1e\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x7f\x00\x63\x00\x03\x00\x06\x00\x06\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x18\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x1c\x00\x36\x00\x63\x00\x22\x00\x1c\x00\x36\x00'\
b'\x63\x00\x63\x00\x63\x00\x36\x00\x1c\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x1e\x00\x33\x00\x61\x80\x61\x80\x33\x80\x1d\x80'\
b'\x01\x80\x01\x80\x03\x00\x07\x00\x3c\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00'\
b'\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00'\
b'\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00\x0c\x00\x18\x00\x10\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x03\xc0\x0f\x00\x3c\x00'\
b'\x70\x00\x3c\x00\x0f\x00\x03\xc0\x00\xc0\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x80\xff\x80'\
b'\x00\x00\xff\x80\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x00\x3c\x00\x0f\x00'\
b'\x03\x80\x0f\x00\x3c\x00\xf0\x00\xc0\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x3e\x00\x63\x00\x63\x00\x03\x00\x0e\x00'\
b'\x18\x00\x18\x00\x00\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x3e\x00\x63\x00\xc1\x80\xdd\x80\xb2\x80\xb2\x80'\
b'\xb2\x80\xb2\x80\xdf\x00\xc0\x00\x63\x00\x3e\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x3c\x00\x0c\x00\x1e\x00\x12\x00\x33\x00'\
b'\x33\x00\x3f\x00\x61\x80\x61\x80\xf3\xc0\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xfe\x00\x63\x00\x61\x80\x63\x00\x7e\x00'\
b'\x63\x00\x61\x80\x61\x80\x63\x00\xfe\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x1e\x80\x73\x80\x61\x80\xc0\x00\xc0\x00'\
b'\xc0\x00\xc0\x00\x61\x80\x73\x80\x1e\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xfc\x00\x67\x00\x63\x00\x61\x80\x61\x80'\
b'\x61\x80\x61\x80\x63\x00\x67\x00\xfc\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x7f\x80\x31\x80\x30\x00\x32\x00\x3e\x00'\
b'\x32\x00\x30\x00\x31\x80\x31\x80\x7f\x80\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x7f\x80\x31\x80\x30\x00\x32\x00\x3e\x00'\
b'\x32\x00\x30\x00\x30\x00\x30\x00\x7c\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x1e\x80\x73\x80\x61\x80\xc0\x00\xc0\x00'\
b'\xc7\xc0\xc1\x80\x61\x80\x71\x80\x1f\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xf7\x80\x63\x00\x63\x00\x63\x00\x7f\x00'\
b'\x63\x00\x63\x00\x63\x00\x63\x00\xf7\x80\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x7f\x80\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x3f\x80\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\xc6\x00\xc6\x00\xc6\x00\x7c\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xf7\x80\x63\x00\x66\x00\x6c\x00\x78\x00'\
b'\x7c\x00\x66\x00\x66\x00\x63\x00\xfb\x80\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xfc\x00\x30\x00\x30\x00\x30\x00\x30\x00'\
b'\x30\x00\x31\x80\x31\x80\x31\x80\xff\x80\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xe1\xc0\x61\x80\x73\x80\x73\x80\x7f\x80'\
b'\x6d\x80\x6d\x80\x61\x80\x61\x80\xf3\xc0\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xf7\xc0\x71\x80\x79\x80\x69\x80\x6d\x80'\
b'\x6d\x80\x65\x80\x67\x80\x63\x80\xfb\x80\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x3e\x00\x63\x00\x63\x00\xc1\x80\xc1\x80'\
b'\xc1\x80\xc1\x80\x63\x00\x63\x00\x3e\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xfe\x00\x63\x00\x61\x80\x61\x80\x63\x00'\
b'\x7e\x00\x60\x00\x60\x00\x60\x00\xfc\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x3e\x00\x63\x00\x63\x00\xc1\x80\xc1\x80'\
b'\xc1\x80\xc1\x80\x63\x00\x63\x00\x3e\x00\x19\x80\x3f\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xfc\x00\x66\x00\x63\x00\x63\x00\x66\x00'\
b'\x7c\x00\x66\x00\x63\x00\x63\x00\xfb\x80\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x1e\x80\x33\x80\x61\x80\x70\x00\x3c\x00'\
b'\x0f\x00\x03\x80\x61\x80\x73\x00\x5e\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x7f\x80\x4c\x80\x4c\x80\x4c\x80\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x3f\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xf3\xc0\x61\x80\x61\x80\x61\x80\x61\x80'\
b'\x61\x80\x61\x80\x61\x80\x33\x00\x1e\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xf3\xc0\x61\x80\x61\x80\x33\x00\x33\x00'\
b'\x33\x00\x1e\x00\x1e\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xf3\xc0\x61\x80\x6d\x80\x6d\x80\x6d\x80'\
b'\x3f\x00\x33\x00\x33\x00\x33\x00\x33\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xf3\xc0\x61\x80\x33\x00\x1e\x00\x0c\x00'\
b'\x0c\x00\x1e\x00\x33\x00\x61\x80\xf3\xc0\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\xf3\xc0\x61\x80\x33\x00\x33\x00\x1e\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x3f\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x7f\x00\x63\x00\x66\x00\x0e\x00\x0c\x00'\
b'\x18\x00\x38\x00\x33\x00\x63\x00\x7f\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x1e\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00'\
b'\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x1e\x00\x00\x00'\
b'\x0a\x00\x60\x00\x60\x00\x30\x00\x30\x00\x30\x00\x18\x00\x18\x00'\
b'\x1c\x00\x0c\x00\x0c\x00\x06\x00\x06\x00\x03\x00\x03\x00\x00\x00'\
b'\x0a\x00\x00\x00\x3c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x3c\x00\x00\x00'\
b'\x0a\x00\x00\x00\x0c\x00\x1e\x00\x33\x00\x61\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xc0\xff\xc0\x00\x00'\

_index =\
b'\x00\x00\x20\x00\x40\x00\x60\x00\x80\x00\xa0\x00\xc0\x00\xe0\x00'\
b'\x00\x01\x20\x01\x40\x01\x60\x01\x80\x01\xa0\x01\xc0\x01\xe0\x01'\
b'\x00\x02\x20\x02\x40\x02\x60\x02\x80\x02\xa0\x02\xc0\x02\xe0\x02'\
b'\x00\x03\x20\x03\x40\x03\x60\x03\x80\x03\xa0\x03\xc0\x03\xe0\x03'\
b'\x00\x04\x20\x04\x40\x04\x60\x04\x80\x04\xa0\x04\xc0\x04\xe0\x04'\
b'\x00\x05\x20\x05\x40\x05\x60\x05\x80\x05\xa0\x05\xc0\x05\xe0\x05'\
b'\x00\x06\x20\x06\x40\x06\x60\x06\x80\x06\xa0\x06\xc0\x06\xe0\x06'\
b'\x00\x07\x20\x07\x40\x07\x60\x07\x80\x07\xa0\x07\xc0\x07\xe0\x07'\
b'\x00\x08\x20\x08'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 15
    return _mvfont[doff + 2:next_offs], 15, width
 
