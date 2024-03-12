'''
    mPyEZfont_u8g2_ncenR12_e.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenR12.bdf font file was sourced from the U8G2 project:
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
# Font: ncenR12.bdf
# Cmd: micropython-font-to-py/font_to_py.py -x u8g2/tools/font/bdf/ncenR12.bdf 0 tmp_mPyEZfont_u8g2_ncenR12_e.py
version = '0.33'

def height():
    return 16

def baseline():
    return 13

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
b'\x07\x00\x00\x38\x4c\xe6\x46\x06\x0c\x18\x10\x10\x00\x30\x30\x00'\
b'\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x05\x00\x00\x60\x60\x60\x60\x60\x40\x40\x40\x40'\
b'\x00\x60\x60\x00\x00\x00\x06\x00\x00\x48\x48\x48\x48\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x12\x00\x12\x00'\
b'\x12\x00\x12\x00\x7f\x00\x24\x00\x24\x00\xfe\x00\x48\x00\x48\x00'\
b'\x48\x00\x48\x00\x00\x00\x00\x00\x00\x00\x09\x00\x08\x00\x08\x00'\
b'\x1e\x00\x29\x00\x4b\x00\x4b\x00\x78\x00\x3e\x00\x0f\x00\x69\x00'\
b'\x69\x00\x4a\x00\x3c\x00\x08\x00\x08\x00\x00\x00\x0e\x00\x00\x00'\
b'\x1c\x40\x33\xc0\x22\x80\x62\x80\x45\x00\x45\x70\x3a\xc8\x02\x88'\
b'\x05\x88\x05\x10\x09\x10\x08\xe0\x00\x00\x00\x00\x00\x00\x0d\x00'\
b'\x00\x00\x1e\x00\x33\x00\x31\x00\x33\x00\x1a\x00\x1c\xf0\x2c\x60'\
b'\x66\x40\xc6\x80\xc3\x90\xe7\x90\x7c\xe0\x00\x00\x00\x00\x00\x00'\
b'\x03\x00\x00\x40\x40\x40\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x06\x00\x00\x08\x10\x20\x20\x40\x40\x40\x40\x40\x40\x20'\
b'\x20\x10\x08\x00\x06\x00\x00\x80\x40\x20\x20\x10\x10\x10\x10\x10'\
b'\x10\x20\x20\x40\x80\x00\x08\x00\x00\x10\x54\xd6\x38\xd6\x54\x10'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x60\x60\x20\x20\x40\x05\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x00\x00\x00\x04\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x00\x00\x00'\
b'\x05\x00\x00\x08\x08\x10\x10\x10\x20\x20\x40\x40\x40\x80\x80\x00'\
b'\x00\x00\x09\x00\x00\x00\x3c\x00\x66\x00\x42\x00\xc3\x00\xc3\x00'\
b'\xc3\x00\xc3\x00\xc3\x00\xc3\x00\x42\x00\x66\x00\x3c\x00\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x00\x00\x08\x00\x78\x00\x18\x00\x18\x00'\
b'\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x7e\x00'\
b'\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x1c\x00\x22\x00\x43\x00'\
b'\x63\x00\x63\x00\x06\x00\x04\x00\x08\x00\x11\x00\x21\x00\x7f\x00'\
b'\x7f\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x3c\x00\x46\x00'\
b'\x63\x00\x63\x00\x06\x00\x1c\x00\x06\x00\x03\x00\x63\x00\x63\x00'\
b'\x46\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x04\x00'\
b'\x0c\x00\x1c\x00\x2c\x00\x2c\x00\x4c\x00\x4c\x00\x8c\x00\xff\x00'\
b'\x0c\x00\x0c\x00\x3f\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00'\
b'\x3f\x00\x3c\x00\x20\x00\x20\x00\x3c\x00\x66\x00\x43\x00\x03\x00'\
b'\x63\x00\x63\x00\x46\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x09\x00'\
b'\x00\x00\x3c\x00\x66\x00\x46\x00\xc0\x00\xc0\x00\xfc\x00\xe6\x00'\
b'\xc3\x00\xc3\x00\xc3\x00\x66\x00\x3c\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x7f\x00\x7f\x00\x42\x00\x42\x00\x04\x00\x04\x00'\
b'\x08\x00\x08\x00\x08\x00\x18\x00\x18\x00\x18\x00\x00\x00\x00\x00'\
b'\x00\x00\x09\x00\x00\x00\x3c\x00\x66\x00\x42\x00\x62\x00\x76\x00'\
b'\x3c\x00\x6e\x00\xc7\x00\xc3\x00\xc3\x00\x66\x00\x3c\x00\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x00\x00\x3c\x00\x66\x00\xc3\x00\xc3\x00'\
b'\xc3\x00\x67\x00\x3f\x00\x03\x00\x03\x00\x62\x00\x66\x00\x38\x00'\
b'\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x60\x60\x00'\
b'\x00\x00\x00\x60\x60\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x60'\
b'\x60\x00\x00\x00\x00\x60\x60\x20\x20\x40\x0a\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x01\x80\x06\x00\x18\x00\x60\x00\x60\x00'\
b'\x18\x00\x06\x00\x01\x80\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x00\x00'\
b'\x00\x00\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x30\x00\x0c\x00'\
b'\x03\x00\x03\x00\x0c\x00\x30\x00\xc0\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x38\x4c\xe6\x46\x06\x0c\x18\x10\x10\x00\x30\x30\x00'\
b'\x00\x00\x0d\x00\x00\x00\x07\x80\x18\x60\x20\x10\x46\xd0\x4d\x90'\
b'\x98\x90\x99\x90\x91\x20\x9b\x20\x4c\xc8\x40\x10\x30\x60\x0f\x80'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x04\x00\x04\x00\x0e\x00\x0e\x00'\
b'\x16\x00\x13\x00\x13\x00\x3f\x80\x21\x80\x41\x80\x40\xc0\xf3\xe0'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\xff\x80\x31\xc0\x30\xc0'\
b'\x30\xc0\x31\x80\x3f\xc0\x30\xe0\x30\x60\x30\x60\x30\x60\x30\xc0'\
b'\xff\x80\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x0f\xa0\x38\x60'\
b'\x30\x20\x70\x20\x60\x20\x60\x00\x60\x00\x60\x00\x70\x20\x30\x20'\
b'\x38\x40\x0f\x80\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\xff\x00'\
b'\x31\xc0\x30\x60\x30\x60\x30\x30\x30\x30\x30\x30\x30\x30\x30\x60'\
b'\x30\x60\x31\xc0\xff\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\xff\xc0\x30\xc0\x30\x40\x32\x40\x32\x00\x3e\x00\x36\x00\x32\x00'\
b'\x32\x40\x30\x40\x30\xc0\xff\xc0\x00\x00\x00\x00\x00\x00\x0b\x00'\
b'\x00\x00\xff\xc0\x30\xc0\x30\x40\x32\x40\x32\x00\x3e\x00\x36\x00'\
b'\x32\x00\x32\x00\x30\x00\x30\x00\xfc\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x0f\xa0\x38\x60\x30\x20\x70\x20\x60\x20\x60\x00'\
b'\x61\xf0\x60\x60\x70\x60\x30\x60\x38\xe0\x0f\x20\x00\x00\x00\x00'\
b'\x00\x00\x0e\x00\x00\x00\xfd\xf8\x30\x60\x30\x60\x30\x60\x30\x60'\
b'\x3f\xe0\x30\x60\x30\x60\x30\x60\x30\x60\x30\x60\xfd\xf8\x00\x00'\
b'\x00\x00\x00\x00\x07\x00\x00\xfc\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\x30\x30\xfc\x00\x00\x00\x09\x00\x00\x00\x1f\x80\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x06\x00\x06\x00\x46\x00\xe6\x00\xc6\x00\x84\x00'\
b'\x78\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\xfd\xf0\x30\xc0'\
b'\x30\x80\x31\x00\x32\x00\x36\x00\x3b\x00\x33\x80\x31\x80\x30\xc0'\
b'\x30\xe0\xfd\xf0\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\xfc\x00'\
b'\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x40\x30\x40'\
b'\x30\x40\x30\xc0\xff\xc0\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\xf8\x3e\x38\x38\x38\x38\x2c\x58\x2c\x58\x2e\x58\x26\x98\x26\x98'\
b'\x23\x98\x23\x18\x23\x18\xf9\x3e\x00\x00\x00\x00\x00\x00\x0d\x00'\
b'\x00\x00\xf0\xf8\x38\x20\x3c\x20\x2c\x20\x2e\x20\x27\x20\x23\xa0'\
b'\x21\xa0\x20\xe0\x20\xe0\x20\x60\xf8\x20\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x07\x00\x18\xc0\x30\x60\x30\x60\x60\x30\x60\x30'\
b'\x60\x30\x60\x30\x30\x60\x30\x60\x18\xc0\x07\x00\x00\x00\x00\x00'\
b'\x00\x00\x0b\x00\x00\x00\xff\x80\x30\xc0\x30\x60\x30\x60\x30\x60'\
b'\x30\xc0\x3f\x80\x30\x00\x30\x00\x30\x00\x30\x00\xfc\x00\x00\x00'\
b'\x00\x00\x00\x00\x0d\x00\x00\x00\x07\x00\x18\xc0\x30\x60\x30\x60'\
b'\x60\x30\x60\x30\x60\x30\x66\x30\x29\x20\x39\xe0\x19\xc0\x07\x80'\
b'\x01\xa0\x01\xa0\x00\xc0\x0c\x00\x00\x00\xff\x00\x30\xc0\x30\x60'\
b'\x30\x60\x30\xc0\x3f\x00\x33\x80\x30\xc0\x30\xc0\x30\xd0\x30\xd0'\
b'\xfc\x60\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x1e\x80\x31\x80'\
b'\x60\x80\x60\x80\x70\x00\x3e\x00\x1f\x00\x43\x80\x41\x80\x41\x80'\
b'\x63\x00\x5e\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\xff\xc0'\
b'\xcc\xc0\x8c\x40\x8c\x40\x8c\x40\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x3f\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00'\
b'\xfc\xf8\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20'\
b'\x30\x20\x30\x20\x18\x40\x0f\x80\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\xf8\xe0\x70\x40\x30\x40\x30\x80\x18\x80\x19\x00\x19\x00'\
b'\x0d\x00\x0e\x00\x0e\x00\x04\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\xf7\xce\x63\x04\x63\x04\x31\x88\x31\x88\x39\xc8'\
b'\x1a\xd0\x1a\xd0\x0a\x50\x0c\x60\x04\x20\x04\x20\x00\x00\x00\x00'\
b'\x00\x00\x0b\x00\x00\x00\xf1\xe0\x60\xc0\x30\x80\x19\x00\x1e\x00'\
b'\x0c\x00\x06\x00\x0f\x00\x13\x00\x21\x80\x60\xc0\xf1\xe0\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\xfc\xf0\x30\x40\x18\x80\x18\x80'\
b'\x0d\x00\x0d\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x1f\x80'\
b'\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x7f\x80\x61\x80\x43\x00'\
b'\x43\x00\x06\x00\x0c\x00\x0c\x00\x18\x80\x30\x80\x30\x80\x61\x80'\
b'\xff\x80\x00\x00\x00\x00\x00\x00\x06\x00\x00\x70\x40\x40\x40\x40'\
b'\x40\x40\x40\x40\x40\x40\x40\x40\x70\x00\x0a\x00\x00\x00\x20\x00'\
b'\x20\x00\x10\x00\x10\x00\x08\x00\x08\x00\x04\x00\x04\x00\x02\x00'\
b'\x02\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x70'\
b'\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x70\x00\x0a\x00'\
b'\x00\x00\x0c\x00\x0c\x00\x1e\x00\x12\x00\x33\x00\x21\x00\x61\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff'\
b'\x00\x00\x05\x00\x00\x80\x40\x20\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x3c\x00\x66\x00\x66\x00\x0e\x00\x36\x00\x66\x00\x66\x00\x3b\x00'\
b'\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\xe0\x00\x60\x00\x60\x00'\
b'\x60\x00\x7c\x00\x66\x00\x63\x00\x63\x00\x63\x00\x63\x00\x66\x00'\
b'\x5c\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x38'\
b'\x6c\xcc\xc0\xc0\xc0\x6c\x38\x00\x00\x00\x0a\x00\x00\x00\x07\x00'\
b'\x03\x00\x03\x00\x03\x00\x1f\x00\x33\x00\x63\x00\x63\x00\x63\x00'\
b'\x63\x00\x33\x00\x1d\x80\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x38\x44\xc6\xfe\xc0\xc0\x66\x3c\x00\x00\x00\x06\x00'\
b'\x00\x38\x6c\x60\x60\xf8\x60\x60\x60\x60\x60\x60\xf8\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3d\x80\x66\x80'\
b'\x66\x00\x66\x00\x66\x00\x3c\x00\x40\x00\x7e\x00\xc3\x00\xc3\x00'\
b'\x7e\x00\x0a\x00\x00\x00\xe0\x00\x60\x00\x60\x00\x60\x00\x6e\x00'\
b'\x77\x00\x63\x00\x63\x00\x63\x00\x63\x00\x63\x00\xf7\x80\x00\x00'\
b'\x00\x00\x00\x00\x05\x00\x00\x60\x60\x00\x00\xe0\x60\x60\x60\x60'\
b'\x60\x60\xf0\x00\x00\x00\x06\x00\x00\x30\x30\x00\x00\x70\x30\x30'\
b'\x30\x30\x30\x30\x30\x30\xb0\xe0\x0a\x00\x00\x00\xe0\x00\x60\x00'\
b'\x60\x00\x60\x00\x6f\x80\x66\x00\x6c\x00\x78\x00\x7c\x00\x66\x00'\
b'\x63\x00\xf7\x80\x00\x00\x00\x00\x00\x00\x05\x00\x00\xe0\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\xf0\x00\x00\x00\x0f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\xee\x70\x73\x98\x63\x18\x63\x18'\
b'\x63\x18\x63\x18\x63\x18\xf7\xbc\x00\x00\x00\x00\x00\x00\x0a\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xee\x00\x73\x00\x63\x00'\
b'\x63\x00\x63\x00\x63\x00\x63\x00\xf7\x80\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x38\x6c\xc6\xc6\xc6\xc6\x6c\x38\x00'\
b'\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xdc\x00'\
b'\x66\x00\x63\x00\x63\x00\x63\x00\x63\x00\x66\x00\x7c\x00\x60\x00'\
b'\x60\x00\xf0\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x39\x00\x66\x00\xc6\x00\xc6\x00\xc6\x00\xc6\x00\x66\x00\x3e\x00'\
b'\x06\x00\x06\x00\x0f\x00\x07\x00\x00\x00\x00\x00\x00\xec\x76\x66'\
b'\x60\x60\x60\x60\xf0\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x74'\
b'\xcc\xc4\x70\x38\x8c\xcc\xb8\x00\x00\x00\x07\x00\x00\x00\x20\x20'\
b'\x60\xf8\x60\x60\x60\x60\x64\x64\x38\x00\x00\x00\x0a\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\xe7\x00\x63\x00\x63\x00\x63\x00'\
b'\x63\x00\x63\x00\x63\x00\x3d\x80\x00\x00\x00\x00\x00\x00\x09\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\x80\x63\x00\x32\x00'\
b'\x36\x00\x1c\x00\x1c\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xef\x78\x66\x30'\
b'\x33\x20\x33\x60\x1d\xc0\x1d\xc0\x08\x80\x08\x80\x00\x00\x00\x00'\
b'\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\x00'\
b'\x62\x00\x34\x00\x38\x00\x1c\x00\x2c\x00\x46\x00\xef\x00\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\xf7\x00\x62\x00\x36\x00\x34\x00\x1c\x00\x1c\x00\x08\x00\x08\x00'\
b'\x18\x00\xd0\x00\xe0\x00\x08\x00\x00\x00\x00\x00\x00\x7e\x46\x4c'\
b'\x18\x18\x32\x62\x7e\x00\x00\x00\x06\x00\x00\x10\x20\x20\x20\x20'\
b'\x20\x40\x20\x20\x20\x20\x20\x20\x10\x00\x0a\x00\x00\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x40'\
b'\x20\x20\x20\x20\x20\x10\x20\x20\x20\x20\x20\x20\x40\x00\x0a\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x39\x80\x67\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

_index =\
b'\x00\x00\x12\x00\x24\x00\x36\x00\x48\x00\x6a\x00\x8c\x00\xae\x00'\
b'\xd0\x00\xe2\x00\xf4\x00\x06\x01\x18\x01\x3a\x01\x4c\x01\x5e\x01'\
b'\x70\x01\x82\x01\xa4\x01\xc6\x01\xe8\x01\x0a\x02\x2c\x02\x4e\x02'\
b'\x70\x02\x92\x02\xb4\x02\xd6\x02\xe8\x02\xfa\x02\x1c\x03\x3e\x03'\
b'\x60\x03\x72\x03\x94\x03\xb6\x03\xd8\x03\xfa\x03\x1c\x04\x3e\x04'\
b'\x60\x04\x82\x04\xa4\x04\xb6\x04\xd8\x04\xfa\x04\x1c\x05\x3e\x05'\
b'\x60\x05\x82\x05\xa4\x05\xc6\x05\xe8\x05\x0a\x06\x2c\x06\x4e\x06'\
b'\x70\x06\x92\x06\xb4\x06\xd6\x06\xf8\x06\x0a\x07\x2c\x07\x3e\x07'\
b'\x60\x07\x72\x07\x84\x07\xa6\x07\xc8\x07\xda\x07\xfc\x07\x0e\x08'\
b'\x20\x08\x42\x08\x64\x08\x76\x08\x88\x08\xaa\x08\xbc\x08\xde\x08'\
b'\x00\x09\x12\x09\x34\x09\x56\x09\x68\x09\x7a\x09\x8c\x09\xae\x09'\
b'\xd0\x09\xf2\x09\x14\x0a\x36\x0a\x48\x0a\x5a\x0a\x7c\x0a\x8e\x0a'\
b'\xb0\x0a'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 126 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 16
    return _mvfont[doff + 2:next_offs], 16, width
 
