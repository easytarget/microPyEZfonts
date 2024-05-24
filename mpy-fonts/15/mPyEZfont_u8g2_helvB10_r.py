'''
    mPyEZfont_u8g2_helvB10_r.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original helvB10.bdf font file was sourced from the U8G2 project:
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
# Font: helvB10.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -l 127 -e 32 ../u8g2/tools/font/bdf/helvB10.bdf 0 tmp_mPyEZfont_u8g2_helvB10_r.py
version = '0.33'

def height():
    return 15

def baseline():
    return 12

def max_width():
    return 14

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
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x60\x60\x60\x60\x60\x60\x40\x40\x00\x60\x60\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x6c\x6c\x48\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x1b\x00\x1b\x00\x1b\x00\x7f\x80\x36\x00'\
b'\x36\x00\xff\x00\x6c\x00\x6c\x00\x6c\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x10\x7c\xd6\xd6\xd0\xf0\x78\x1c\x16\xd6\xd6\x7c\x10\x10'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x78\x40\xcc\xc0'\
b'\xcd\x80\x79\x00\x03\x00\x06\x00\x04\x00\x0d\xe0\x0b\x30\x1b\x30'\
b'\x11\xe0\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x1c\x00'\
b'\x36\x00\x36\x00\x1c\x00\x39\x80\x7d\x80\x67\x00\x63\x00\x67\x80'\
b'\x3e\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x00\x60\x60\x40\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x18\x30\x30\x60\x60\x60\x60\x60\x60\x60\x60\x30\x30'\
b'\x18\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\xc0\x60\x60\x30\x30'\
b'\x30\x30\x30\x30\x30\x30\x60\x60\xc0\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x20\xf8\x70\xd8\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x18\x00\x18\x00\x18\x00\xff\x00\x18\x00\x18\x00\x18\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x60\x60\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x60\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x10\x10\x30\x20\x20\x60\x40\x40\xc0\x80\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x38\x6c\xc6\xc6\xc6'\
b'\xc6\xc6\xc6\xc6\x6c\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x18\x78\x18\x18\x18\x18\x18\x18\x18\x18\x18\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x7c\xc6\xc6\x06\x0e'\
b'\x0c\x18\x30\x60\xc0\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x7c\xc6\xc6\x06\x06\x3c\x06\x06\xc6\xc6\x7c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x06\x0e\x1e\x36\x66'\
b'\xc6\xc6\xff\x06\x06\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x7e\x60\x60\xc0\xfc\x0e\x06\x06\xc6\xcc\x78\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x3c\x66\x66\xc0\xdc'\
b'\xe6\xc6\xc6\xc6\xc6\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\xfe\x06\x0c\x0c\x18\x18\x30\x30\x60\x60\x60\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x7c\xc6\xc6\xc6\xc6'\
b'\x7c\xc6\xc6\xc6\xc6\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x7c\xc6\xc6\xc6\xc6\xc6\x7e\x06\xc6\xcc\x78\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x30\x30'\
b'\x00\x00\x00\x00\x30\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x30\x30\x00\x00\x00\x00\x30\x30\x60\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x0e'\
b'\x38\x60\x38\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00'\
b'\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x70\x1c\x06\x1c\x70\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x3e\x00\x63\x00'\
b'\x63\x00\x03\x00\x06\x00\x0c\x00\x18\x00\x18\x00\x00\x00\x18\x00'\
b'\x18\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x0f\x80\x38\xe0'\
b'\x70\x70\x66\xb0\xcd\x98\xd9\x98\xdb\x18\xdb\x30\xce\xe0\x60\x00'\
b'\x31\x80\x1f\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x0c\x00\x0c\x00'\
b'\x1e\x00\x12\x00\x33\x00\x33\x00\x61\x80\x7f\x80\x61\x80\xc0\xc0'\
b'\xc0\xc0\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x7f\x00\x63\x80'\
b'\x61\x80\x61\x80\x63\x00\x7e\x00\x63\x00\x61\x80\x61\x80\x63\x80'\
b'\x7f\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x0f\x80\x3d\xc0'\
b'\x30\x40\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x30\x40\x3d\xc0'\
b'\x0f\x80\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x7e\x00\x63\x80'\
b'\x61\x80\x60\xc0\x60\xc0\x60\xc0\x60\xc0\x60\xc0\x61\x80\x63\x80'\
b'\x7e\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x7f\x00\x60\x00'\
b'\x60\x00\x60\x00\x60\x00\x7f\x00\x60\x00\x60\x00\x60\x00\x60\x00'\
b'\x7f\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x7f\x00\x60\x00'\
b'\x60\x00\x60\x00\x60\x00\x7e\x00\x60\x00\x60\x00\x60\x00\x60\x00'\
b'\x60\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x0f\x80\x3d\xc0'\
b'\x30\x40\x60\x00\x60\x00\x63\xc0\x60\xc0\x60\xc0\x30\xc0\x3d\xc0'\
b'\x0f\x40\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x61\x80\x61\x80'\
b'\x61\x80\x61\x80\x61\x80\x7f\x80\x61\x80\x61\x80\x61\x80\x61\x80'\
b'\x61\x80\x00\x00\x00\x00\x00\x00\x04\x00\x00\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x06\x06\x06\x06\x06\x06\x06\xc6\xc6\xee\x7c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x61\x80\x63\x00'\
b'\x66\x00\x6c\x00\x78\x00\x78\x00\x6c\x00\x66\x00\x63\x00\x61\x80'\
b'\x60\xc0\x00\x00\x00\x00\x00\x00\x08\x00\x00\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x60\x30\x60\x30\x70\x70\x70\x70\x78\xf0\x68\xb0'\
b'\x68\xb0\x6d\xb0\x65\x30\x67\x30\x62\x30\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x60\xc0\x70\xc0\x70\xc0\x68\xc0\x6c\xc0\x64\xc0'\
b'\x66\xc0\x62\xc0\x61\xc0\x61\xc0\x60\xc0\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x0f\x00\x39\xc0\x30\xc0\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x30\xc0\x39\xc0\x0f\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x7f\x00\x63\x80\x61\x80\x61\x80\x63\x80\x7f\x00'\
b'\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x0f\x00\x39\xc0\x30\xc0\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x63\x60\x31\xc0\x39\xc0\x0f\x60\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x7f\x00\x63\x80\x61\x80\x61\x80\x63\x00\x7f\x00'\
b'\x63\x80\x61\x80\x61\x80\x61\x80\x60\xc0\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x3f\x00\x73\x80\x61\x80\x70\x00\x3c\x00\x0f\x00'\
b'\x03\x80\x01\x80\x61\x80\x77\x00\x3e\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\xff\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x60\xc0\x60\xc0'\
b'\x60\xc0\x60\xc0\x60\xc0\x60\xc0\x60\xc0\x60\xc0\x60\xc0\x31\x80'\
b'\x1f\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\xc0\xc0\xc0\xc0'\
b'\x61\x80\x61\x80\x73\x80\x33\x00\x33\x00\x1e\x00\x1e\x00\x0c\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\xc3\x0c\xc3\x0c'\
b'\xc3\x0c\x67\x98\x64\x98\x64\x98\x6c\xd8\x2c\xd0\x38\x70\x18\x60'\
b'\x18\x60\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\xc1\x80\xc1\x80'\
b'\x63\x00\x36\x00\x1c\x00\x1c\x00\x36\x00\x63\x00\x63\x00\xc1\x80'\
b'\xc1\x80\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\xc0\xc0\x61\x80'\
b'\x61\x80\x33\x00\x33\x00\x1e\x00\x1e\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\xff\x00\x03\x00'\
b'\x06\x00\x0c\x00\x1c\x00\x18\x00\x30\x00\x70\x00\x60\x00\xc0\x00'\
b'\xff\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x78\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x78\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x80\x80\xc0\x40\x40\x60\x20\x20\x30\x10\x10\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\xf0\x30\x30\x30\x30'\
b'\x30\x30\x30\x30\x30\x30\x30\x30\xf0\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x18\x3c\x24\x66\x66\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x60\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x3c\x66'\
b'\x06\x3e\x66\x66\x6e\x3b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x60\x00\x60\x00\x60\x00\x6c\x00\x76\x00\x63\x00'\
b'\x63\x00\x63\x00\x63\x00\x76\x00\x6c\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x1c\x36\x66\x60\x60\x66\x36\x1c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x03\x00\x03\x00'\
b'\x03\x00\x1b\x00\x37\x00\x63\x00\x63\x00\x63\x00\x63\x00\x37\x00'\
b'\x1b\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x3c\x66'\
b'\x66\x7e\x60\x60\x76\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x38\x60\x60\xf0\x60\x60\x60\x60\x60\x60\x60\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1d\x00\x37\x00\x63\x00\x63\x00\x63\x00\x63\x00\x37\x00'\
b'\x1b\x00\x03\x00\x67\x00\x3e\x00\x09\x00\x00\x00\x60\x00\x60\x00'\
b'\x60\x00\x6e\x00\x77\x00\x63\x00\x63\x00\x63\x00\x63\x00\x63\x00'\
b'\x63\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x60\x60\x00\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x60\x60\x00\x60\x60\x60\x60\x60\x60\x60\x60\x60\xe0'\
b'\xc0\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x60\x60\x60\x66\x6c'\
b'\x78\x78\x6c\x6c\x66\x66\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x6d\xc0\x77\x60\x66\x60\x66\x60\x66\x60\x66\x60\x66\x60'\
b'\x66\x60\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x6e\x00\x77\x00\x63\x00\x63\x00\x63\x00\x63\x00\x63\x00'\
b'\x63\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1c\x00\x36\x00\x63\x00\x63\x00\x63\x00\x63\x00\x36\x00'\
b'\x1c\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x6c\x00\x76\x00\x63\x00\x63\x00\x63\x00\x63\x00\x76\x00'\
b'\x6c\x00\x60\x00\x60\x00\x60\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1b\x00\x37\x00\x63\x00\x63\x00\x63\x00\x63\x00\x37\x00'\
b'\x1b\x00\x03\x00\x03\x00\x03\x00\x06\x00\x00\x00\x00\x00\x6c\x7c'\
b'\x60\x60\x60\x60\x60\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x3c\x66\x70\x3c\x0e\x06\x76\x3c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x60\x60\xf8\x60'\
b'\x60\x60\x60\x60\x68\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x63\x00\x63\x00\x63\x00'\
b'\x63\x00\x63\x00\x63\x00\x77\x00\x3b\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\xc3\xc3\x66\x66\x24\x3c\x18\x18\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xcc\xc0\xcc\xc0\xcc\xc0\x6d\x80\x6d\x80\x33\x00\x33\x00'\
b'\x33\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\xc6\xc6'\
b'\x6c\x38\x38\x6c\xc6\xc6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\xc3\xc3\x66\x66\x24\x3c\x18\x18\x18\x30'\
b'\x70\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\xfc\x0c'\
b'\x18\x30\x30\x60\xc0\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x18\x30\x30\x30\x30\x60\xc0\x60\x30\x30\x30\x30\x30'\
b'\x18\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x20\x20\x20\x20\x20'\
b'\x20\x20\x20\x20\x20\x20\x20\x20\x20\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x60\x30\x30\x30\x30\x18\x0c\x18\x30\x30\x30\x30\x30'\
b'\x60\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x39\x00\x6f\x00\x46\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

_sparse =\
b'\x20\x00\x03\x00\x21\x00\x06\x00\x22\x00\x09\x00\x23\x00\x0c\x00'\
b'\x24\x00\x10\x00\x25\x00\x13\x00\x26\x00\x17\x00\x27\x00\x1b\x00'\
b'\x28\x00\x1e\x00\x29\x00\x21\x00\x2a\x00\x24\x00\x2b\x00\x27\x00'\
b'\x2c\x00\x2b\x00\x2d\x00\x2e\x00\x2e\x00\x31\x00\x2f\x00\x34\x00'\
b'\x30\x00\x37\x00\x31\x00\x3a\x00\x32\x00\x3d\x00\x33\x00\x40\x00'\
b'\x34\x00\x43\x00\x35\x00\x46\x00\x36\x00\x49\x00\x37\x00\x4c\x00'\
b'\x38\x00\x4f\x00\x39\x00\x52\x00\x3a\x00\x55\x00\x3b\x00\x58\x00'\
b'\x3c\x00\x5b\x00\x3d\x00\x5e\x00\x3e\x00\x62\x00\x3f\x00\x65\x00'\
b'\x40\x00\x69\x00\x41\x00\x6d\x00\x42\x00\x71\x00\x43\x00\x75\x00'\
b'\x44\x00\x79\x00\x45\x00\x7d\x00\x46\x00\x81\x00\x47\x00\x85\x00'\
b'\x48\x00\x89\x00\x49\x00\x8d\x00\x4a\x00\x90\x00\x4b\x00\x93\x00'\
b'\x4c\x00\x97\x00\x4d\x00\x9a\x00\x4e\x00\x9e\x00\x4f\x00\xa2\x00'\
b'\x50\x00\xa6\x00\x51\x00\xaa\x00\x52\x00\xae\x00\x53\x00\xb2\x00'\
b'\x54\x00\xb6\x00\x55\x00\xb9\x00\x56\x00\xbd\x00\x57\x00\xc1\x00'\
b'\x58\x00\xc5\x00\x59\x00\xc9\x00\x5a\x00\xcd\x00\x5b\x00\xd1\x00'\
b'\x5c\x00\xd4\x00\x5d\x00\xd7\x00\x5e\x00\xda\x00\x5f\x00\xdd\x00'\
b'\x60\x00\xe0\x00\x61\x00\xe3\x00\x62\x00\xe6\x00\x63\x00\xea\x00'\
b'\x64\x00\xed\x00\x65\x00\xf1\x00\x66\x00\xf4\x00\x67\x00\xf7\x00'\
b'\x68\x00\xfb\x00\x69\x00\xff\x00\x6a\x00\x02\x01\x6b\x00\x05\x01'\
b'\x6c\x00\x08\x01\x6d\x00\x0b\x01\x6e\x00\x0f\x01\x6f\x00\x13\x01'\
b'\x70\x00\x17\x01\x71\x00\x1b\x01\x72\x00\x1f\x01\x73\x00\x22\x01'\
b'\x74\x00\x25\x01\x75\x00\x28\x01\x76\x00\x2c\x01\x77\x00\x2f\x01'\
b'\x78\x00\x33\x01\x79\x00\x36\x01\x7a\x00\x39\x01\x7b\x00\x3c\x01'\
b'\x7c\x00\x3f\x01\x7d\x00\x42\x01\x7e\x00\x45\x01\x7f\x00\x49\x01'\

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

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 15
    return _mvfont[doff + 2:next_offs], 15, width
 
