'''
    mPyEZfont_u8g2_ncenR14_r.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenR14.bdf font file was sourced from the U8G2 project:
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
# Font: ncenR14.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/r-char.set u8g2/tools/font/bdf/ncenR14.bdf 0 tmp_mPyEZfont_u8g2_ncenR14_r.py
version = '0.33'

def height():
    return 19

def baseline():
    return 15

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
    return 126

_font =\
b'\x08\x00\x00\x3c\xce\xc6\x06\x06\x04\x08\x08\x10\x10\x00\x00\x30'\
b'\x30\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x60\x60\x60'\
b'\x60\x60\x60\x60\x40\x40\x40\x00\x00\x60\x60\x00\x00\x00\x00\x07'\
b'\x00\x00\x48\x48\x48\x48\x48\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x09\x00\x09\x00\x09\x00'\
b'\x09\x00\x7f\xc0\x12\x00\x12\x00\x12\x00\xff\x80\x24\x00\x24\x00'\
b'\x24\x00\x24\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x08\x00'\
b'\x08\x00\x3f\x00\x69\x80\xc9\x80\xc8\x00\xe8\x00\x78\x00\x1e\x00'\
b'\x0f\x00\x0b\x80\x09\x80\xc9\x80\xcb\x00\x7e\x00\x08\x00\x08\x00'\
b'\x00\x00\x00\x00\x10\x00\x00\x00\x1c\x20\x32\x20\x63\xc0\x62\x40'\
b'\xc4\x80\xc4\x80\xc9\x1c\x71\x32\x02\x62\x02\x62\x04\xc4\x04\xc4'\
b'\x08\xc8\x08\x70\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00'\
b'\x1e\x00\x33\x00\x21\x00\x23\x00\x36\x00\x1c\x00\x39\xf8\x7c\x60'\
b'\xee\x40\xc7\x80\xc3\x80\xc1\xc8\xe3\xf0\x7c\x60\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x04\x00\x00\x40\x40\x40\x40\x40\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x04\x18\x30\x60'\
b'\x60\xc0\xc0\xc0\xc0\xc0\xc0\xc0\x60\x60\x30\x18\x04\x00\x07\x00'\
b'\x00\x80\x60\x30\x18\x18\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x18\x18\x30'\
b'\x60\x80\x00\x0a\x00\x00\x00\x08\x00\x49\x00\x6b\x00\x1c\x00\x6b'\
b'\x00\x49\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x08\x00\xff'\
b'\x80\x08\x00\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x60\x60\x20\x40\x80\x00\x06\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x00\x00'\
b'\x00\x00\x06\x00\x00\x08\x08\x08\x10\x10\x10\x20\x20\x20\x40\x40'\
b'\x40\x80\x80\x00\x00\x00\x00\x0a\x00\x00\x00\x1c\x00\x63\x00\x63'\
b'\x00\xc1\x80\xc1\x80\xc1\x80\xc1\x80\xc1\x80\xc1\x80\xc1\x80\xc1'\
b'\x80\x63\x00\x63\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a'\
b'\x00\x00\x00\x0c\x00\x7c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c'\
b'\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x1e\x00\x63\x00\xc1'\
b'\x80\xc1\x80\x01\x80\x01\x80\x03\x00\x06\x00\x0c\x00\x18\x00\x30'\
b'\x80\x60\x80\xff\x80\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0a'\
b'\x00\x00\x00\x3e\x00\x63\x00\x61\x80\x01\x80\x01\x80\x03\x00\x1e'\
b'\x00\x03\x00\x01\x80\x01\x80\x01\x80\xc1\x80\xc3\x00\x7e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x03\x00\x07\x00\x0b'\
b'\x00\x0b\x00\x13\x00\x13\x00\x23\x00\x23\x00\x43\x00\x43\x00\xff'\
b'\xc0\x03\x00\x03\x00\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0a'\
b'\x00\x00\x00\x7f\x80\x7f\x00\x40\x00\x40\x00\x40\x00\x5e\x00\x63'\
b'\x00\x41\x80\x01\x80\x01\x80\x01\x80\xc1\x80\xc3\x00\x7e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x0f\x00\x31\x80\x61'\
b'\x80\x60\x00\xc0\x00\xce\x00\xdf\x00\xe3\x80\xc1\x80\xc1\x80\xc1'\
b'\x80\xc1\x80\x63\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a'\
b'\x00\x00\x00\xff\x80\xff\x80\x81\x00\x83\x00\x02\x00\x06\x00\x06'\
b'\x00\x0c\x00\x0c\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x3e\x00\x63\x00\x41'\
b'\x00\x41\x00\x61\x00\x72\x00\x3e\x00\x2f\x00\x43\x80\xc1\x80\xc1'\
b'\x80\xc1\x80\x63\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a'\
b'\x00\x00\x00\x3e\x00\x63\x00\xc1\x80\xc1\x80\xc1\x80\xc1\x80\xe3'\
b'\x80\x7d\x80\x39\x80\x01\x80\x03\x00\xc3\x00\xc6\x00\x78\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x60'\
b'\x60\x00\x00\x00\x00\x00\x60\x60\x00\x00\x00\x00\x05\x00\x00\x00'\
b'\x00\x00\x00\x00\x60\x60\x00\x00\x00\x00\x00\x60\x60\x20\x40\x80'\
b'\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x03'\
b'\x80\x0e\x00\x38\x00\xe0\x00\x38\x00\x0e\x00\x03\x80\x00\x80\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x80\x00\x00\x00\x00\xff'\
b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0'\
b'\x00\x38\x00\x0e\x00\x03\x80\x0e\x00\x38\x00\xe0\x00\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x3c\xce\xc6\x06'\
b'\x06\x04\x08\x08\x10\x10\x00\x00\x30\x30\x00\x00\x00\x00\x0e\x00'\
b'\x00\x00\x07\x80\x18\x60\x20\x10\x46\xd0\x4d\xc8\x8c\xc8\x98\xc8'\
b'\x99\x90\x99\x90\x9b\xa0\x4c\xc0\x40\x10\x20\x60\x1f\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x03\x00\x03\x00\x03\x00'\
b'\x05\x80\x05\x80\x05\x80\x08\xc0\x08\xc0\x1f\xe0\x10\x60\x10\x60'\
b'\x20\x30\x20\x30\xf8\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00'\
b'\x00\x00\xff\x80\x30\xc0\x30\x60\x30\x60\x30\x60\x30\xc0\x3f\x80'\
b'\x30\x60\x30\x30\x30\x30\x30\x30\x30\x30\x30\x60\xff\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x0f\x90\x38\x70\x60\x30'\
b'\x60\x10\xc0\x10\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\x60\x10'\
b'\x60\x10\x38\x60\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00'\
b'\x00\x00\xff\xc0\x30\x70\x30\x18\x30\x18\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x18\x30\x18\x30\x70\xff\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\xff\xe0\x30\x60\x30\x20'\
b'\x30\x20\x31\x20\x31\x00\x3f\x00\x31\x00\x31\x00\x30\x20\x30\x20'\
b'\x30\x20\x30\x60\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\xff\xe0\x30\x60\x30\x20\x30\x20\x31\x20\x31\x00\x3f\x00'\
b'\x31\x00\x31\x00\x30\x00\x30\x00\x30\x00\x30\x00\xfc\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x0f\xc8\x38\x78\x60\x18'\
b'\x60\x08\xc0\x08\xc0\x00\xc0\x00\xc0\x00\xc0\x7c\xc0\x18\x60\x18'\
b'\x60\x18\x38\x78\x0f\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\xfc\x7e\x30\x18\x30\x18\x30\x18\x30\x18\x30\x18\x3f\xf8'\
b'\x30\x18\x30\x18\x30\x18\x30\x18\x30\x18\x30\x18\xfc\x7e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x07\x00\x00\xfc\x30\x30\x30\x30\x30\x30'\
b'\x30\x30\x30\x30\x30\x30\xfc\x00\x00\x00\x00\x0a\x00\x00\x00\x1f'\
b'\x80\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06'\
b'\x00\x06\x00\xc6\x00\xc6\x00\x84\x00\x78\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x0f\x00\x00\x00\xfc\xf8\x30\x60\x30\x40\x30\x80\x31'\
b'\x00\x32\x00\x36\x00\x3f\x00\x33\x80\x31\xc0\x30\xe0\x30\x70\x30'\
b'\x38\xfc\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\xfc'\
b'\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30'\
b'\x00\x30\x20\x30\x20\x30\x20\x30\x60\xff\xe0\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x12\x00\x00\x00\x00\xf8\x0f\x80\x38\x0e\x00\x2c\x16'\
b'\x00\x2c\x16\x00\x2c\x16\x00\x26\x26\x00\x26\x26\x00\x26\x26\x00'\
b'\x23\x46\x00\x23\x46\x00\x23\x46\x00\x21\x86\x00\x21\x86\x00\xf9'\
b'\x9f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00'\
b'\x00\x00\xf0\x7c\x30\x10\x38\x10\x3c\x10\x2e\x10\x26\x10\x23\x10'\
b'\x23\x90\x21\x90\x20\xd0\x20\xf0\x20\x70\x20\x30\xf8\x10\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x0f\xc0\x38\x70\x60\x18'\
b'\x60\x18\xc0\x0c\xc0\x0c\xc0\x0c\xc0\x0c\xc0\x0c\xc0\x0c\x60\x18'\
b'\x60\x18\x38\x70\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\xff\x80\x30\xc0\x30\x60\x30\x60\x30\x60\x30\x60\x30\xc0'\
b'\x3f\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\xfc\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x0f\xc0\x38\x70\x60\x18'\
b'\x60\x18\xc0\x0c\xc0\x0c\xc0\x0c\xc0\x0c\xc0\x0c\xcf\x0c\x71\x98'\
b'\x60\x98\x38\xf0\x0f\xe0\x00\x60\x00\x72\x00\x3e\x00\x1c\x0e\x00'\
b'\x00\x00\xff\x80\x30\xc0\x30\x60\x30\x60\x30\x60\x30\xc0\x3f\x00'\
b'\x31\x80\x30\xc0\x30\xc0\x30\xe0\x30\x60\x30\x74\xf8\x38\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x3e\x80\x61\x80\xc0\x80'\
b'\xc0\x80\xc0\x00\xf0\x00\x7e\x00\x1f\x80\x03\xc0\x80\xc0\x80\xc0'\
b'\xc0\xc0\xe1\x80\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00'\
b'\x00\x00\xff\xf0\xc6\x30\x86\x10\x86\x10\x86\x10\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x1f\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\xfc\x7c\x30\x10\x30\x10'\
b'\x30\x10\x30\x10\x30\x10\x30\x10\x30\x10\x30\x10\x30\x10\x30\x10'\
b'\x30\x10\x18\x20\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00'\
b'\x00\x00\xfc\x7c\x30\x10\x30\x10\x18\x20\x18\x20\x18\x20\x0c\x40'\
b'\x0c\x40\x0c\x40\x06\x80\x06\x80\x06\x80\x03\x00\x03\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\xfd\xf9\xf0\x30\x60'\
b'\x40\x30\x60\x40\x18\x70\x80\x18\x70\x80\x18\x70\x80\x0c\x99\x00'\
b'\x0c\x99\x00\x0c\x99\x00\x05\x09\x00\x07\x0e\x00\x07\x0e\x00\x03'\
b'\x06\x00\x03\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x0e\x00\x00\x00\x7c\x78\x18\x20\x1c\x60\x0c\x40\x06\xc0\x07'\
b'\x80\x03\x00\x03\x80\x07\xc0\x04\xc0\x08\x60\x18\x70\x10\x30\x7c'\
b'\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\xfc\x7c\x30'\
b'\x10\x18\x20\x18\x20\x0c\x40\x0c\x40\x06\x80\x07\x80\x03\x00\x03'\
b'\x00\x03\x00\x03\x00\x03\x00\x0f\xc0\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x0b\x00\x00\x00\xff\xc0\xc0\xc0\x81\x80\x83\x80\x83\x00\x06'\
b'\x00\x0e\x00\x1c\x00\x18\x00\x30\x40\x70\x40\x60\x40\xc0\xc0\xff'\
b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x78\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x78\x00\x0a\x00'\
b'\x00\x00\x40\x00\x40\x00\x60\x00\x20\x00\x30\x00\x10\x00\x18\x00'\
b'\x08\x00\x0c\x00\x04\x00\x06\x00\x02\x00\x03\x00\x01\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x06\x00\x00\xf0\x30\x30\x30\x30\x30\x30'\
b'\x30\x30\x30\x30\x30\x30\x30\x30\x30\xf0\x00\x0a\x00\x00\x00\x08'\
b'\x00\x08\x00\x1c\x00\x14\x00\x36\x00\x22\x00\x63\x00\x41\x00\xc1'\
b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\xff\x80\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x60'\
b'\x30\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00'\
b'\x62\x00\x63\x00\x03\x00\x1f\x00\x63\x00\xc3\x00\xc7\x00\x79\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\xe0\x00\x60\x00'\
b'\x60\x00\x60\x00\x60\x00\x6f\x00\x71\x80\x60\xc0\x60\xc0\x60\xc0'\
b'\x60\xc0\x60\xc0\x71\x80\x4f\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00'\
b'\x63\x00\xc3\x00\xc0\x00\xc0\x00\xc0\x00\xc1\x00\x63\x00\x3e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x03\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x3d\x80\x63\x80\xc1\x80\xc1\x80\xc1\x80'\
b'\xc1\x80\xc1\x80\x63\x80\x3d\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00'\
b'\x66\x00\xc3\x00\xc3\x00\xff\x00\xc0\x00\xc1\x00\x63\x00\x3e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x0e\x1b\x33\x30\x30'\
b'\xfc\x30\x30\x30\x30\x30\x30\x30\x78\x00\x00\x00\x00\x0b\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x1f\xc0\x33\x00\x61'\
b'\x80\x61\x80\x33\x00\x3e\x00\x40\x00\x7f\x00\x3f\x80\x41\xc0\x80'\
b'\xc0\xc1\x80\x7f\x00\x0b\x00\x00\x00\xe0\x00\x60\x00\x60\x00\x60'\
b'\x00\x60\x00\x6f\x00\x73\x80\x61\x80\x61\x80\x61\x80\x61\x80\x61'\
b'\x80\x61\x80\xf3\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00'\
b'\x00\x60\x60\x00\x00\xe0\x60\x60\x60\x60\x60\x60\x60\xf0\x00\x00'\
b'\x00\x00\x08\x00\x00\x00\x0c\x0c\x00\x00\x1c\x0c\x0c\x0c\x0c\x0c'\
b'\x0c\x0c\x0c\x0c\xcc\xc8\x70\x0a\x00\x00\x00\xe0\x00\x60\x00\x60'\
b'\x00\x60\x00\x60\x00\x67\x80\x62\x00\x64\x00\x68\x00\x78\x00\x6c'\
b'\x00\x66\x00\x63\x00\xf7\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x05'\
b'\x00\x00\xe0\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\xf0'\
b'\x00\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\xef\x3c\x00\x73\xce\x00\x61\x86'\
b'\x00\x61\x86\x00\x61\x86\x00\x61\x86\x00\x61\x86\x00\x61\x86\x00'\
b'\xf3\xcf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xef\x00\x73'\
b'\x80\x61\x80\x61\x80\x61\x80\x61\x80\x61\x80\x61\x80\xf3\xc0\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x3e\x00\x63\x00\xc1\x80\xc1\x80\xc1\x80\xc1'\
b'\x80\xc1\x80\x63\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xef\x00\x71'\
b'\x80\x60\xc0\x60\xc0\x60\xc0\x60\xc0\x60\xc0\x71\x80\x6f\x00\x60'\
b'\x00\x60\x00\x60\x00\xf0\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x3c\x80\x63\x80\xc1\x80\xc1\x80\xc1\x80\xc1'\
b'\x80\xc1\x80\x63\x80\x3d\x80\x01\x80\x01\x80\x01\x80\x03\xc0\x08'\
b'\x00\x00\x00\x00\x00\x00\x00\xe6\x6e\x72\x60\x60\x60\x60\x60\xf0'\
b'\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x7a\xc6\x82\xe0'\
b'\x7c\x0e\x82\xc6\xbc\x00\x00\x00\x00\x06\x00\x00\x00\x00\x60\x60'\
b'\x60\xf8\x60\x60\x60\x60\x60\x60\x64\x38\x00\x00\x00\x00\x0b\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe3\x80\x61\x80'\
b'\x61\x80\x61\x80\x61\x80\x61\x80\x61\x80\x73\x80\x3d\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\xf1\xc0\x60\x80\x60\x80\x31\x00\x31\x00\x1a\x00'\
b'\x1e\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\xde\x61\x84'\
b'\x61\x84\x32\xc8\x32\xc8\x34\xd0\x1c\x70\x1c\x70\x08\x20\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\xf3\x80\x61\x00\x32\x00\x1c\x00\x08\x00\x1c\x00'\
b'\x26\x00\x43\x00\xe7\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf1\xc0\x60\x80'\
b'\x31\x00\x31\x00\x1a\x00\x1a\x00\x0c\x00\x0c\x00\x08\x00\x08\x00'\
b'\x10\x00\xd0\x00\xe0\x00\x08\x00\x00\x00\x00\x00\x00\x00\xfe\x86'\
b'\x8c\x18\x18\x30\x62\xc6\xfe\x00\x00\x00\x00\x06\x00\x00\x18\x20'\
b'\x60\x60\x60\x60\x60\x40\x80\x40\x60\x60\x60\x60\x60\x20\x18\x00'\
b'\x0b\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\xc0\x20\x30\x30\x30'\
b'\x30\x30\x10\x08\x10\x30\x30\x30\x30\x30\x20\xc0\x00\x0b\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38'\
b'\xc0\x6d\x80\xc7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00'

_index =\
b'\x00\x00\x15\x00\x2a\x00\x3f\x00\x54\x00\x7c\x00\xa4\x00\xcc\x00'\
b'\xf4\x00\x09\x01\x1e\x01\x33\x01\x5b\x01\x83\x01\x98\x01\xad\x01'\
b'\xc2\x01\xd7\x01\xff\x01\x27\x02\x4f\x02\x77\x02\x9f\x02\xc7\x02'\
b'\xef\x02\x17\x03\x3f\x03\x67\x03\x7c\x03\x91\x03\xb9\x03\xe1\x03'\
b'\x09\x04\x1e\x04\x46\x04\x6e\x04\x96\x04\xbe\x04\xe6\x04\x0e\x05'\
b'\x36\x05\x5e\x05\x86\x05\x9b\x05\xc3\x05\xeb\x05\x13\x06\x4e\x06'\
b'\x76\x06\x9e\x06\xc6\x06\xee\x06\x16\x07\x3e\x07\x66\x07\x8e\x07'\
b'\xb6\x07\xf1\x07\x19\x08\x41\x08\x69\x08\x7e\x08\xa6\x08\xbb\x08'\
b'\xe3\x08\x0b\x09\x20\x09\x48\x09\x70\x09\x98\x09\xc0\x09\xe8\x09'\
b'\xfd\x09\x25\x0a\x4d\x0a\x62\x0a\x77\x0a\x9f\x0a\xb4\x0a\xef\x0a'\
b'\x17\x0b\x3f\x0b\x67\x0b\x8f\x0b\xa4\x0b\xb9\x0b\xce\x0b\xf6\x0b'\
b'\x1e\x0c\x46\x0c\x6e\x0c\x96\x0c\xab\x0c\xc0\x0c\xe8\x0c\xfd\x0c'\
b'\x25\x0d'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 126 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 19
    return _mvfont[doff + 2:next_offs], 19, width
 
