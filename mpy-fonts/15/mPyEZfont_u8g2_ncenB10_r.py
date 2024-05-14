'''
    mPyEZfont_u8g2_ncenB10_r.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenB10.bdf font file was sourced from the U8G2 project:
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
# Font: ncenB10.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./r-char.set -e 32 ../u8g2/tools/font/bdf/ncenB10.bdf 0 tmp_mPyEZfont_u8g2_ncenB10_r.py
version = '0.33'

def height():
    return 15

def baseline():
    return 12

def max_width():
    return 15

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
b'\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x04\x00\x00\x60\x60\x60\x60\x60\x40\x40\x00\x60\x60\x60'\
b'\x00\x00\x00\x05\x00\x00\x50\x50\x50\x50\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x08\x00\x00\x00\x14\x14\x14\x7e\x28\x28\xfc\x50'\
b'\x50\x50\x00\x00\x00\x08\x00\x10\x7c\xd6\x96\xd0\xf0\x7c\x1e\x16'\
b'\xd2\xd6\x7c\x10\x00\x00\x0d\x00\x00\x00\x30\x80\x6f\x00\xc9\x00'\
b'\xca\x00\xd2\x00\x64\x60\x04\xd0\x09\x90\x09\x90\x11\xa0\x10\xc0'\
b'\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x1e\x00\x33\x00\x33\x00'\
b'\x32\x00\x1c\x00\x3c\xe0\x4e\x40\xc7\x80\xc3\x90\xe3\xe0\x7c\xc0'\
b'\x00\x00\x00\x00\x00\x00\x03\x00\x00\x40\x40\x40\x40\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x10\x20\x60\x40\xc0\xc0'\
b'\xc0\xc0\xc0\x40\x60\x20\x10\x00\x05\x00\x00\x80\x40\x60\x20\x30'\
b'\x30\x30\x30\x30\x20\x60\x40\x80\x00\x06\x00\x00\x20\xa8\x70\xa8'\
b'\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00'\
b'\x10\x10\x10\xfe\x10\x10\x10\x00\x00\x00\x00\x04\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x60\x60\x60\x20\x40\x00\x05\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\xf0\xf0\x00\x00\x00\x00\x00\x00\x04\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x60\x00\x00\x00\x05\x00'\
b'\x00\x10\x10\x10\x20\x20\x20\x40\x40\x40\x80\x80\x00\x00\x00\x08'\
b'\x00\x00\x38\x6c\xc6\xc6\xc6\xc6\xc6\xc6\xc6\x6c\x38\x00\x00\x00'\
b'\x08\x00\x00\x18\x78\x18\x18\x18\x18\x18\x18\x18\x18\x3c\x00\x00'\
b'\x00\x08\x00\x00\x78\xce\xc6\x06\x06\x0c\x18\x30\x62\xfe\xfe\x00'\
b'\x00\x00\x08\x00\x00\x78\xce\xc6\x06\x0c\x3c\x06\x06\xc6\xce\x78'\
b'\x00\x00\x00\x08\x00\x00\x0c\x1c\x1c\x2c\x2c\x4c\x4c\xfe\x0c\x0c'\
b'\x1e\x00\x00\x00\x08\x00\x00\x7e\x7c\x40\x40\x5c\x6e\x06\x06\xc6'\
b'\xce\x78\x00\x00\x00\x08\x00\x00\x3c\x66\xc6\xc0\xdc\xee\xc6\xc6'\
b'\xc6\xe6\x78\x00\x00\x00\x08\x00\x00\xfe\xfe\x84\x8c\x0c\x18\x18'\
b'\x18\x30\x30\x30\x00\x00\x00\x08\x00\x00\x78\xe6\xc6\xc6\xf4\x3c'\
b'\x5e\xc6\xc6\xce\x3c\x00\x00\x00\x08\x00\x00\x3c\xce\xc6\xc6\xc6'\
b'\xee\x76\x06\xc6\xcc\x78\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00'\
b'\x60\x60\x60\x00\x60\x60\x60\x00\x00\x00\x04\x00\x00\x00\x00\x00'\
b'\x00\x60\x60\x60\x00\x60\x60\x60\x20\x40\x00\x08\x00\x00\x00\x00'\
b'\x00\x02\x0e\x38\xe0\x38\x0e\x02\x00\x00\x00\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\xfe\x00\xfe\x00\x00\x00\x00\x00\x00\x08\x00\x00'\
b'\x00\x00\x00\x80\xe0\x38\x0e\x38\xe0\x80\x00\x00\x00\x00\x07\x00'\
b'\x00\x78\xcc\xcc\x0c\x18\x30\x20\x00\x30\x30\x30\x00\x00\x00\x0e'\
b'\x00\x00\x00\x0f\xc0\x38\x70\x63\x98\x6c\xd8\xcc\xd8\xd9\x98\xd9'\
b'\xb0\xdb\xb0\xcd\xc0\x60\x10\x3f\xe0\x00\x00\x00\x00\x00\x00\x0b'\
b'\x00\x00\x00\x0c\x00\x0c\x00\x16\x00\x16\x00\x12\x00\x23\x00\x23'\
b'\x00\x3f\x00\x41\x80\x41\x80\xe3\xc0\x00\x00\x00\x00\x00\x00\x0a'\
b'\x00\x00\x00\xfe\x00\x63\x00\x63\x00\x63\x00\x66\x00\x7f\x00\x61'\
b'\x80\x61\x80\x61\x80\x63\x80\xfe\x00\x00\x00\x00\x00\x00\x00\x0b'\
b'\x00\x00\x00\x1f\x40\x70\xc0\x60\x40\xc0\x40\xc0\x00\xc0\x00\xc0'\
b'\x00\xc0\x00\x60\x40\x70\xc0\x1f\x00\x00\x00\x00\x00\x00\x00\x0c'\
b'\x00\x00\x00\xff\x00\x61\xc0\x60\xc0\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\xc0\x61\xc0\xff\x00\x00\x00\x00\x00\x00\x00\x0a'\
b'\x00\x00\x00\xff\x80\x61\x80\x60\x80\x64\x80\x64\x00\x7c\x00\x64'\
b'\x00\x64\x80\x60\x80\x61\x80\xff\x80\x00\x00\x00\x00\x00\x00\x0a'\
b'\x00\x00\x00\xff\x80\x61\x80\x60\x80\x64\x80\x64\x00\x7c\x00\x64'\
b'\x00\x64\x00\x60\x00\x60\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x0c'\
b'\x00\x00\x00\x1f\x40\x70\xc0\x60\x40\xc0\x40\xc0\x00\xc0\x00\xc3'\
b'\xe0\xc0\xc0\x60\xc0\x71\xc0\x1e\x40\x00\x00\x00\x00\x00\x00\x0c'\
b'\x00\x00\x00\xf1\xe0\x60\xc0\x60\xc0\x60\xc0\x60\xc0\x7f\xc0\x60'\
b'\xc0\x60\xc0\x60\xc0\x60\xc0\xf1\xe0\x00\x00\x00\x00\x00\x00\x07'\
b'\x00\x00\x78\x30\x30\x30\x30\x30\x30\x30\x30\x30\x78\x00\x00\x00'\
b'\x09\x00\x00\x00\x1e\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\xcc\x00\xcc\x00\x9c\x00\x70\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\xf3\xc0\x61\x00\x62\x00\x64\x00\x68\x00\x7c\x00'\
b'\x6e\x00\x67\x00\x63\x80\x61\xc0\xf3\xe0\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\xf0\x00\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00'\
b'\x60\x00\x60\x80\x60\x80\x61\x80\xff\x80\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\xf0\x78\x70\x70\x70\x70\x58\xb0\x58\xb0\x58\xb0'\
b'\x4d\x30\x4d\x30\x4d\x30\x46\x30\xe6\x78\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\xe0\xe0\x70\x40\x78\x40\x5c\x40\x4c\x40\x46\x40'\
b'\x47\x40\x43\xc0\x41\xc0\x40\xc0\xe0\x40\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x1f\x00\x71\xc0\x60\xc0\xc0\x60\xc0\x60\xc0\x60'\
b'\xc0\x60\xc0\x60\x60\xc0\x71\xc0\x1f\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\xff\x00\x63\x80\x61\x80\x61\x80\x63\x80\x7e\x00'\
b'\x60\x00\x60\x00\x60\x00\x60\x00\xf0\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x1f\x00\x71\xc0\x60\xc0\xc0\x60\xc0\x60\xc0\x60'\
b'\xc0\x60\xdc\x60\x66\xc0\x73\xc0\x1f\x00\x03\x20\x03\xa0\x01\xc0'\
b'\x0c\x00\x00\x00\xff\x00\x63\x80\x61\x80\x61\x80\x63\x00\x7e\x00'\
b'\x63\x00\x63\x00\x61\x80\x61\xa0\xf1\xc0\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x3d\x00\xe3\x00\xc1\x00\xc1\x00\xf0\x00\x7e\x00'\
b'\x0f\x80\x81\x80\x81\x80\xc3\x80\xbe\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\xff\xc0\xcc\xc0\x8c\x40\x8c\x40\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x1e\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\xf0\xe0\x60\x40\x60\x40\x60\x40\x60\x40\x60\x40'\
b'\x60\x40\x60\x40\x60\x40\x30\x80\x1f\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\xf1\xc0\x60\x80\x60\x80\x31\x00\x31\x00\x31\x00'\
b'\x1a\x00\x1a\x00\x1a\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\xf7\xb8\x63\x10\x63\x10\x63\x10\x35\xa0\x35\xa0'\
b'\x35\xa0\x35\xa0\x18\xc0\x18\xc0\x18\xc0\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\xf9\xe0\x70\xc0\x30\x80\x19\x00\x0d\x00\x0e\x00'\
b'\x16\x00\x13\x00\x21\x80\x61\xc0\xf3\xe0\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\xf1\xc0\x60\x80\x31\x00\x31\x00\x1a\x00\x1a\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x1e\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\xff\x00\xc3\x00\x87\x00\x8e\x00\x0c\x00\x18\x00'\
b'\x30\x00\x71\x00\xe1\x00\xc3\x00\xff\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\xf0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xf0'\
b'\x00\x07\x00\x00\x80\x80\x40\x40\x20\x20\x10\x10\x08\x08\x04\x00'\
b'\x00\x00\x05\x00\x00\xf0\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\x30\xf0\x00\x08\x00\x00\x10\x10\x38\x28\x6c\x44\xc6\x00\x00\x00'\
b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xfe\x00\x00\x06\x00\x00\x60\x30\x08\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x3c\x00\x66\x00\x06\x00\x3e\x00\xc6\x00\xce\x00\x77\x00'\
b'\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\xe0\x00\x60\x00\x60\x00'\
b'\x60\x00\x6e\x00\x73\x00\x61\x80\x61\x80\x61\x80\x63\x00\x5e\x00'\
b'\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x3c\x66\xc6'\
b'\xc0\xc2\x66\x3c\x00\x00\x00\x0a\x00\x00\x00\x07\x00\x03\x00\x03'\
b'\x00\x03\x00\x3b\x00\x67\x00\xc3\x00\xc3\x00\xc3\x00\x67\x00\x3b'\
b'\x80\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x3c\x00\x66\x00\xc3\x00\xff\x00\xc0\x00\x63\x00\x3e'\
b'\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x38\x6c\x6c\x60\xf8\x60'\
b'\x60\x60\x60\x60\xf0\x00\x00\x00\x08\x00\x00\x00\x00\x00\x06\x7c'\
b'\xc6\xc6\x7c\x80\xfc\x7e\x82\x86\x7c\x0a\x00\x00\x00\xe0\x00\x60'\
b'\x00\x60\x00\x60\x00\x6e\x00\x73\x00\x63\x00\x63\x00\x63\x00\x63'\
b'\x00\xf7\x80\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x60\x60\x00'\
b'\xe0\x60\x60\x60\x60\x60\xf0\x00\x00\x00\x07\x00\x00\x00\x18\x18'\
b'\x00\x38\x18\x18\x18\x18\x18\x18\x18\xd8\x70\x09\x00\x00\x00\xe0'\
b'\x00\x60\x00\x60\x00\x60\x00\x67\x00\x66\x00\x6c\x00\x78\x00\x6c'\
b'\x00\x66\x00\xe7\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\xe0\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\xf0\x00\x00\x00\x0f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\xee\x70\x73\x98\x63\x18\x63\x18'\
b'\x63\x18\x63\x18\xf7\xbc\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\xee\x00\x73\x00\x63\x00\x63\x00'\
b'\x63\x00\x63\x00\xf7\x80\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x66\x00\xc3\x00\xc3\x00'\
b'\xc3\x00\x66\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\xee\x00\x73\x00\x61\x80\x61\x80'\
b'\x61\x80\x73\x00\x6e\x00\x60\x00\x60\x00\xf0\x00\x09\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3d\x00\x67\x00\xc3\x00\xc3\x00'\
b'\xc3\x00\x67\x00\x3b\x00\x03\x00\x03\x00\x07\x80\x07\x00\x00\x00'\
b'\x00\x00\x00\xee\x76\x60\x60\x60\x60\xf0\x00\x00\x00\x07\x00\x00'\
b'\x00\x00\x00\x00\x7c\xc4\xe0\x78\x1c\x8c\xf8\x00\x00\x00\x06\x00'\
b'\x00\x00\x20\x20\x60\xf8\x60\x60\x60\x64\x64\x38\x00\x00\x00\x0a'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe7\x00\x63\x00\x63'\
b'\x00\x63\x00\x63\x00\x67\x00\x3b\x80\x00\x00\x00\x00\x00\x00\x08'\
b'\x00\x00\x00\x00\x00\x00\xf7\x62\x62\x34\x34\x18\x18\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\xb8\x63\x10'\
b'\x63\x10\x35\xa0\x35\xa0\x18\xc0\x18\xc0\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe7\x00\x66\x00'\
b'\x3c\x00\x18\x00\x3c\x00\x46\x00\xe7\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\xf7\x62\x62\x34\x34\x18\x18\x10\xd0'\
b'\xe0\x07\x00\x00\x00\x00\x00\x00\xfc\x8c\x18\x30\x60\xc4\xfc\x00'\
b'\x00\x00\x06\x00\x00\x18\x20\x60\x60\x60\x40\x80\x40\x60\x60\x60'\
b'\x20\x18\x00\x08\x00\x00\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'\
b'\x10\x00\x00\x00\x06\x00\x00\xc0\x20\x30\x30\x30\x10\x08\x10\x30'\
b'\x30\x30\x20\xc0\x00\x08\x00\x00\x00\x00\x00\x00\x00\x76\xdc\x00'\
b'\x00\x00\x00\x00\x00\x00'

_index =\
b'\x00\x00\x11\x00\x22\x00\x33\x00\x44\x00\x55\x00\x66\x00\x86\x00'\
b'\xa6\x00\xb7\x00\xc8\x00\xd9\x00\xea\x00\xfb\x00\x0c\x01\x1d\x01'\
b'\x2e\x01\x3f\x01\x50\x01\x61\x01\x72\x01\x83\x01\x94\x01\xa5\x01'\
b'\xb6\x01\xc7\x01\xd8\x01\xe9\x01\xfa\x01\x0b\x02\x1c\x02\x2d\x02'\
b'\x3e\x02\x4f\x02\x6f\x02\x8f\x02\xaf\x02\xcf\x02\xef\x02\x0f\x03'\
b'\x2f\x03\x4f\x03\x6f\x03\x80\x03\xa0\x03\xc0\x03\xe0\x03\x00\x04'\
b'\x20\x04\x40\x04\x60\x04\x80\x04\xa0\x04\xc0\x04\xe0\x04\x00\x05'\
b'\x20\x05\x40\x05\x60\x05\x80\x05\xa0\x05\xb1\x05\xc2\x05\xd3\x05'\
b'\xe4\x05\xf5\x05\x06\x06\x26\x06\x46\x06\x57\x06\x77\x06\x97\x06'\
b'\xa8\x06\xb9\x06\xd9\x06\xea\x06\xfb\x06\x1b\x07\x2c\x07\x4c\x07'\
b'\x6c\x07\x8c\x07\xac\x07\xcc\x07\xdd\x07\xee\x07\xff\x07\x1f\x08'\
b'\x30\x08\x50\x08\x70\x08\x81\x08\x92\x08\xa3\x08\xb4\x08\xc5\x08'\
b'\xd6\x08'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 126 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 15
    return _mvfont[doff + 2:next_offs], 15, width
 
