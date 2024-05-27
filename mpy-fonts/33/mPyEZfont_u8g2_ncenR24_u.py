'''
    mPyEZfont_u8g2_ncenR24_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenR24.bdf font file was sourced from the U8G2 project:
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
# Font: ncenR24.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -l 95 -e 32 ../u8g2/tools/font/bdf/ncenR24.bdf 0 tmp_mPyEZfont_u8g2_ncenR24_u.py
version = '0.33'

def height():
    return 33

def baseline():
    return 27

def max_width():
    return 31

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
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x0c\x00'\
b'\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1e\x00\x1e\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00'\
b'\x00\x00\x38\xe0\x38\xe0\x38\xe0\x38\xe0\x10\x40\x10\x40\x10\x40'\
b'\x10\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc3'\
b'\x00\x00\xc3\x00\x00\xc3\x00\x01\xc7\x00\x01\x86\x00\x01\x86\x00'\
b'\x01\x86\x00\x1f\xff\xc0\x1f\xff\xc0\x01\x86\x00\x03\x8e\x00\x03'\
b'\x0e\x00\x03\x0c\x00\x3f\xff\x80\x3f\xff\x80\x03\x0c\x00\x03\x0c'\
b'\x00\x07\x1c\x00\x07\x1c\x00\x06\x18\x00\x06\x18\x00\x06\x18\x00'\
b'\x06\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x12\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00'\
b'\x03\xf0\x00\x0f\xfc\x00\x1c\x9c\x00\x38\x8e\x00\x30\x9e\x00\x30'\
b'\x9e\x00\x30\x8c\x00\x30\x80\x00\x38\x80\x00\x3e\x80\x00\x1f\xc0'\
b'\x00\x0f\xf0\x00\x07\xfc\x00\x00\xfe\x00\x00\x9f\x00\x00\x8f\x00'\
b'\x18\x87\x00\x3c\x83\x00\x3c\x83\x00\x38\x87\x00\x30\x86\x00\x38'\
b'\x9e\x00\x1f\xfc\x00\x07\xf0\x00\x00\x80\x00\x00\x80\x00\x00\x80'\
b'\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x1b\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x10\x00\x07\xe0\x70\x00'\
b'\x0e\x71\xe0\x00\x1c\x3f\xe0\x00\x1c\x30\xc0\x00\x38\x30\xc0\x00'\
b'\x38\x31\x80\x00\x78\x31\x80\x00\x70\x33\x00\x00\x70\x62\x00\x00'\
b'\x70\x66\x00\x00\x70\xc4\x0e\x00\x39\x8c\x3f\x00\x1f\x08\x71\x80'\
b'\x00\x18\xe1\x80\x00\x31\xe1\x80\x00\x31\xc1\x80\x00\x63\xc1\x80'\
b'\x00\x63\x81\x80\x00\xc3\x83\x00\x00\xc3\x83\x00\x01\x83\x86\x00'\
b'\x01\x01\xcc\x00\x03\x00\xf8\x00\x02\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x1b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7e\x00\x00\x01\xef'\
b'\x00\x00\x01\x87\x00\x00\x03\x83\x80\x00\x03\x83\x80\x00\x03\x83'\
b'\x80\x00\x03\x83\x00\x00\x03\x87\x00\x00\x03\xce\x00\x00\x03\xdc'\
b'\x00\x00\x01\xf8\x00\x00\x01\xe0\x00\x00\x03\xf1\xff\x00\x0e\xf0'\
b'\x7c\x00\x1c\x78\x38\x00\x1c\x7c\x30\x00\x38\x3c\x30\x00\x38\x3e'\
b'\x60\x00\x38\x1f\x60\x00\x3c\x0f\xc1\x00\x3c\x07\x81\x00\x3e\x03'\
b'\xc3\x00\x1f\x8f\xfe\x00\x0f\xfc\xfe\x00\x07\xf0\x78\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x38\x38\x38\x38\x10\x10'\
b'\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00'\
b'\x40\x01\xc0\x01\x80\x03\x00\x06\x00\x0c\x00\x0c\x00\x0c\x00\x18'\
b'\x00\x18\x00\x18\x00\x18\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38'\
b'\x00\x18\x00\x18\x00\x18\x00\x18\x00\x0c\x00\x0c\x00\x04\x00\x06'\
b'\x00\x03\x00\x01\x80\x01\xc0\x00\xc0\x00\x00\x00\x00\x0b\x00\x00'\
b'\x00\x00\x00\x30\x00\x38\x00\x18\x00\x0c\x00\x06\x00\x02\x00\x03'\
b'\x00\x03\x00\x01\x80\x01\x80\x01\x80\x01\x80\x01\xc0\x01\xc0\x01'\
b'\xc0\x01\xc0\x01\xc0\x01\x80\x01\x80\x01\x80\x01\x80\x03\x00\x03'\
b'\x00\x07\x00\x06\x00\x0c\x00\x18\x00\x30\x00\x30\x00\x00\x00\x00'\
b'\x00\x11\x00\x00\x00\x00\x00\x00\x00\x01\x80\x00\x01\x80\x00\x01'\
b'\x80\x00\x31\x9c\x00\x39\x9c\x00\x1f\xf8\x00\x07\xe0\x00\x07\xc0'\
b'\x00\x1f\xf0\x00\x39\x9c\x00\x31\x9c\x00\x01\x80\x00\x01\x80\x00'\
b'\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00\x00\x60\x00\x00'\
b'\x60\x00\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00\x60\x00\x3f\xff'\
b'\xc0\x3f\xff\xc0\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00\x60\x00'\
b'\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x3e\x00\x3e'\
b'\x00\x1e\x00\x06\x00\x06\x00\x0c\x00\x18\x00\x38\x00\x20\x00\x0b'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x7f\x80\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x18\x00\x3c\x00\x3c\x00\x18\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\xc0\x00'\
b'\xc0\x00\xc0\x01\x80\x01\x80\x01\x80\x03\x00\x03\x00\x03\x00\x06'\
b'\x00\x06\x00\x06\x00\x0c\x00\x0c\x00\x0c\x00\x18\x00\x18\x00\x18'\
b'\x00\x30\x00\x30\x00\x30\x00\x60\x00\x60\x00\x60\x00\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x03\xfc\x00\x07\x0e\x00\x06'\
b'\x06\x00\x0e\x07\x00\x1e\x07\x80\x1c\x03\x80\x3c\x03\xc0\x3c\x03'\
b'\xc0\x3c\x03\xc0\x3c\x03\xc0\x3c\x03\xc0\x3c\x03\xc0\x3c\x03\xc0'\
b'\x3c\x03\xc0\x3c\x03\xc0\x3c\x03\xc0\x1c\x03\x80\x1e\x07\x80\x0e'\
b'\x07\x00\x06\x06\x00\x07\x0e\x00\x03\xfc\x00\x00\xf0\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00\x00\xe0'\
b'\x00\x1f\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00'\
b'\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00'\
b'\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0'\
b'\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x01\xf0\x00'\
b'\x1f\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\xf0\x00\x0f\xfc\x00\x1c\x0e\x00\x30\x0f\x00\x38\x07\x00\x3c'\
b'\x07\x00\x3c\x07\x00\x3c\x07\x00\x18\x0f\x00\x00\x0e\x00\x00\x0e'\
b'\x00\x00\x1c\x00\x00\x3c\x00\x00\x38\x00\x00\x70\x00\x00\xe0\x00'\
b'\x01\xc0\x00\x03\x81\x00\x07\x01\x00\x0e\x03\x00\x1c\x03\x00\x3f'\
b'\xff\x00\x7f\xff\x00\x7f\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x03\xf0\x00\x0f\xfc\x00\x1c\x1c\x00\x38\x0e'\
b'\x00\x3c\x0e\x00\x3c\x0e\x00\x18\x0e\x00\x00\x0e\x00\x00\x1c\x00'\
b'\x00\x38\x00\x00\xf0\x00\x07\xf8\x00\x00\x7c\x00\x00\x1e\x00\x00'\
b'\x0e\x00\x00\x0f\x00\x30\x07\x00\x78\x07\x00\x78\x07\x00\x78\x0f'\
b'\x00\x70\x0e\x00\x3c\x3e\x00\x1f\xf8\x00\x07\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x18\x00'\
b'\x00\x38\x00\x00\x78\x00\x00\xf8\x00\x00\xf8\x00\x01\xb8\x00\x03'\
b'\x38\x00\x03\x38\x00\x06\x38\x00\x0c\x38\x00\x0c\x38\x00\x18\x38'\
b'\x00\x30\x38\x00\x30\x38\x00\x60\x38\x00\x7f\xff\x80\x7f\xff\x80'\
b'\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00\x7c\x00\x01'\
b'\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e'\
b'\x02\x00\x0f\xfe\x00\x0f\xfc\x00\x0f\xf8\x00\x0c\x00\x00\x0c\x00'\
b'\x00\x08\x00\x00\x18\x00\x00\x18\xf0\x00\x1b\xfc\x00\x1f\x1e\x00'\
b'\x1c\x0e\x00\x18\x0f\x00\x00\x07\x00\x00\x07\x00\x00\x07\x00\x18'\
b'\x07\x00\x3c\x07\x00\x3c\x07\x00\x3c\x0f\x00\x38\x0e\x00\x1c\x1e'\
b'\x00\x1f\xfc\x00\x07\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x01\xf8\x00\x07\xfe\x00\x0e\x1f\x00\x1c\x0f\x00'\
b'\x1c\x0f\x00\x18\x06\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00\x78'\
b'\xf0\x00\x7b\xfc\x00\x7f\x1e\x00\x7e\x0e\x00\x7c\x0f\x00\x78\x07'\
b'\x00\x78\x07\x00\x78\x07\x00\x38\x07\x00\x38\x07\x00\x38\x0f\x00'\
b'\x1c\x0e\x00\x1c\x1e\x00\x0f\xf8\x00\x03\xe0\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xff\x00\x1f\xff\x00\x1f'\
b'\xff\x00\x18\x02\x00\x18\x06\x00\x10\x04\x00\x10\x0c\x00\x10\x08'\
b'\x00\x00\x18\x00\x00\x18\x00\x00\x30\x00\x00\x30\x00\x00\x30\x00'\
b'\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00\xe0\x00\x00\xe0\x00\x00'\
b'\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x00\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf0'\
b'\x00\x0f\xfc\x00\x1e\x1c\x00\x1c\x0e\x00\x38\x0e\x00\x38\x06\x00'\
b'\x38\x06\x00\x3c\x0c\x00\x1e\x1c\x00\x1f\xb8\x00\x0f\xf0\x00\x03'\
b'\xf8\x00\x03\xfc\x00\x0e\xfe\x00\x1c\x3e\x00\x38\x0f\x00\x38\x0f'\
b'\x00\x70\x07\x00\x70\x07\x00\x70\x07\x00\x38\x0e\x00\x3c\x1e\x00'\
b'\x1f\xfc\x00\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x07\xe0\x00\x1f\xf8\x00\x3c\x3c\x00\x38\x1c\x00\x78'\
b'\x1e\x00\x70\x0e\x00\x70\x0e\x00\x70\x0f\x00\x70\x0f\x00\x78\x0f'\
b'\x00\x78\x1f\x00\x3c\x3f\x00\x3c\x3f\x00\x1f\xef\x00\x0f\xcf\x00'\
b'\x00\x0f\x00\x00\x0e\x00\x00\x0e\x00\x30\x1c\x00\x78\x1c\x00\x78'\
b'\x38\x00\x78\xf0\x00\x3f\xe0\x00\x1f\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x0c\x00\x1e\x00\x1e\x00\x0c\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1e'\
b'\x00\x1e\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x3c\x00\x3c\x00\x18'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x18\x00\x3c\x00\x3c\x00\x1c\x00\x0c\x00\x08\x00\x18\x00\x30'\
b'\x00\x60\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x40\x00\x01\xc0\x00\x07\xc0\x00\x1f'\
b'\x00\x00\x7c\x00\x01\xf0\x00\x07\xc0\x00\x1f\x00\x00\x3c\x00\x00'\
b'\x3c\x00\x00\x1f\x00\x00\x07\xc0\x00\x01\xf0\x00\x00\x7c\x00\x00'\
b'\x1f\x00\x00\x07\xc0\x00\x01\xc0\x00\x00\x40\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xff\xc0\x3f\xff\xc0\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xff\xc0\x3f\xff'\
b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20'\
b'\x00\x00\x38\x00\x00\x3e\x00\x00\x0f\x80\x00\x03\xe0\x00\x00\xf8'\
b'\x00\x00\x3e\x00\x00\x0f\x80\x00\x03\xc0\x00\x03\xc0\x00\x0f\x80'\
b'\x00\x3e\x00\x00\xf8\x00\x03\xe0\x00\x0f\x80\x00\x3e\x00\x00\x38'\
b'\x00\x00\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x1f\xc0\x39\xf0\x60\x70'\
b'\x60\x78\x70\x38\x70\x38\x70\x38\x00\x78\x00\x78\x00\xf0\x00\xe0'\
b'\x01\xc0\x01\x80\x03\x00\x02\x00\x02\x00\x06\x00\x06\x00\x00\x00'\
b'\x00\x00\x00\x00\x06\x00\x0f\x00\x0f\x00\x06\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x7f\x00\x00\x01\xff\xc0\x00\x07\xc3\xe0\x00\x0f\x00'\
b'\x70\x00\x0e\x00\x38\x00\x18\x00\x1c\x00\x18\x00\x0c\x00\x30\x7d'\
b'\xcc\x00\x30\xe7\xc6\x00\x71\xc7\xc6\x00\x63\xc3\xc6\x00\x63\x83'\
b'\x86\x00\x67\x83\x86\x00\x67\x87\x84\x00\x67\x07\x8c\x00\x67\x07'\
b'\x0c\x00\x67\x0f\x18\x00\x33\x1f\x30\x00\x33\xbf\x60\x00\x19\xf3'\
b'\xcc\x00\x1c\x00\x1c\x00\x0e\x00\x38\x00\x07\xc0\xf0\x00\x03\xff'\
b'\xc0\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x38\x00\x00\x38\x00\x00'\
b'\x78\x00\x00\x7c\x00\x00\x7c\x00\x00\xdc\x00\x00\xde\x00\x01\x9e'\
b'\x00\x01\x8e\x00\x01\x8f\x00\x03\x07\x00\x03\x07\x80\x03\x07\x80'\
b'\x06\x03\x80\x07\xff\xc0\x07\xff\xc0\x0c\x01\xc0\x0c\x01\xe0\x0c'\
b'\x01\xe0\x18\x00\xf0\x18\x00\xf0\x38\x00\xf8\x7c\x01\xfc\xfe\x03'\
b'\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00\x7f\xff\x00\x1f\xff'\
b'\xc0\x07\x03\xe0\x07\x00\xe0\x07\x00\xf0\x07\x00\xf0\x07\x00\xf0'\
b'\x07\x00\xf0\x07\x00\xe0\x07\x00\xe0\x07\x01\xc0\x07\xff\x80\x07'\
b'\xfe\x00\x07\x07\xc0\x07\x01\xe0\x07\x00\xf0\x07\x00\x78\x07\x00'\
b'\x78\x07\x00\x78\x07\x00\x78\x07\x00\x78\x07\x00\xf0\x07\x01\xf0'\
b'\x1f\xff\xe0\x7f\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xfe\x30\x03\xff\xb0\x07\x01\xf0\x0e\x00\xf0\x1e\x00\x70\x1c'\
b'\x00\x70\x3c\x00\x30\x3c\x00\x30\x78\x00\x10\x78\x00\x10\x78\x00'\
b'\x00\x78\x00\x00\x78\x00\x00\x78\x00\x00\x78\x00\x00\x78\x00\x00'\
b'\x78\x00\x18\x3c\x00\x18\x3c\x00\x18\x3c\x00\x30\x1e\x00\x30\x0e'\
b'\x00\x60\x07\x81\xc0\x03\xff\x80\x00\xfe\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x7f\xff\x00\x00\x1f\xff\xe0\x00\x07'\
b'\x01\xf0\x00\x07\x00\x78\x00\x07\x00\x38\x00\x07\x00\x3c\x00\x07'\
b'\x00\x3c\x00\x07\x00\x1e\x00\x07\x00\x1e\x00\x07\x00\x1e\x00\x07'\
b'\x00\x1e\x00\x07\x00\x1e\x00\x07\x00\x1e\x00\x07\x00\x1e\x00\x07'\
b'\x00\x1e\x00\x07\x00\x1e\x00\x07\x00\x1e\x00\x07\x00\x1e\x00\x07'\
b'\x00\x1c\x00\x07\x00\x3c\x00\x07\x00\x38\x00\x07\x00\x70\x00\x07'\
b'\x01\xf0\x00\x1f\xff\xe0\x00\x7f\xff\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x7f\xff\xf8\x1f\xff'\
b'\xf8\x07\x00\xf8\x07\x00\x38\x07\x00\x38\x07\x00\x18\x07\x02\x18'\
b'\x07\x02\x08\x07\x02\x08\x07\x06\x00\x07\x1e\x00\x07\xfe\x00\x07'\
b'\xfe\x00\x07\x1e\x00\x07\x06\x00\x07\x06\x00\x07\x02\x08\x07\x02'\
b'\x08\x07\x00\x08\x07\x00\x18\x07\x00\x18\x07\x00\x38\x07\x00\xf8'\
b'\x1f\xff\xf8\x7f\xff\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00'\
b'\x7f\xff\xf8\x1f\xff\xf8\x07\x00\xf8\x07\x00\x38\x07\x00\x18\x07'\
b'\x00\x18\x07\x00\x08\x07\x02\x08\x07\x02\x08\x07\x06\x00\x07\x06'\
b'\x00\x07\x1e\x00\x07\xfe\x00\x07\xfe\x00\x07\x0e\x00\x07\x06\x00'\
b'\x07\x02\x00\x07\x02\x00\x07\x02\x00\x07\x00\x00\x07\x00\x00\x07'\
b'\x00\x00\x07\x00\x00\x1f\xc0\x00\x7f\xf0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\xff\x18\x00\x03\xff\xd8\x00\x07'\
b'\x81\xf8\x00\x0f\x00\x78\x00\x1e\x00\x38\x00\x1c\x00\x38\x00\x3c'\
b'\x00\x18\x00\x38\x00\x18\x00\x38\x00\x08\x00\x78\x00\x08\x00\x78'\
b'\x00\x00\x00\x78\x00\x00\x00\x78\x00\x00\x00\x78\x00\x00\x00\x78'\
b'\x03\xff\x80\x78\x00\x7c\x00\x78\x00\x38\x00\x38\x00\x38\x00\x38'\
b'\x00\x38\x00\x3c\x00\x38\x00\x1c\x00\x78\x00\x0e\x00\x78\x00\x07'\
b'\x80\xd8\x00\x03\xff\x98\x00\x00\xff\x08\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x1b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf1\xff'\
b'\xc0\x1f\xc0\x7f\x00\x07\x00\x1c\x00\x07\x00\x1c\x00\x07\x00\x1c'\
b'\x00\x07\x00\x1c\x00\x07\x00\x1c\x00\x07\x00\x1c\x00\x07\x00\x1c'\
b'\x00\x07\x00\x1c\x00\x07\x00\x1c\x00\x07\xff\xfc\x00\x07\xff\xfc'\
b'\x00\x07\x00\x1c\x00\x07\x00\x1c\x00\x07\x00\x1c\x00\x07\x00\x1c'\
b'\x00\x07\x00\x1c\x00\x07\x00\x1c\x00\x07\x00\x1c\x00\x07\x00\x1c'\
b'\x00\x07\x00\x1c\x00\x07\x00\x1c\x00\x1f\xc0\x7f\x00\x7f\xf1\xff'\
b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x7f'\
b'\xf0\x1f\xc0\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07'\
b'\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07'\
b'\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x1f\xc0\x7f'\
b'\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00'\
b'\x00\x00\x00\x00\x00\x03\xff\x80\x00\x7c\x00\x00\x38\x00\x00\x38'\
b'\x00\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00\x38\x00'\
b'\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00'\
b'\x38\x00\x00\x38\x00\x70\x38\x00\xf8\x38\x00\xf8\x38\x00\xf8\x38'\
b'\x00\xf0\x38\x00\xc0\x78\x00\xe0\x70\x00\x7f\xf0\x00\x1f\xc0\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf1\xff\x80'\
b'\x1f\xc0\xfe\x00\x07\x00\x78\x00\x07\x00\x70\x00\x07\x00\xe0\x00'\
b'\x07\x00\xc0\x00\x07\x01\x80\x00\x07\x03\x00\x00\x07\x07\x00\x00'\
b'\x07\x0e\x00\x00\x07\x1c\x00\x00\x07\x3e\x00\x00\x07\x7f\x00\x00'\
b'\x07\xef\x00\x00\x07\xc7\x80\x00\x07\x83\xc0\x00\x07\x03\xe0\x00'\
b'\x07\x01\xe0\x00\x07\x00\xf0\x00\x07\x00\xf8\x00\x07\x00\x78\x00'\
b'\x07\x00\x3c\x00\x07\x00\x3e\x00\x1f\x80\x1f\x00\x7f\xe0\x7f\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00'\
b'\x7f\xf0\x00\x1f\xc0\x00\x07\x00\x00\x07\x00\x00\x07\x00\x00\x07'\
b'\x00\x00\x07\x00\x00\x07\x00\x00\x07\x00\x00\x07\x00\x00\x07\x00'\
b'\x00\x07\x00\x00\x07\x00\x00\x07\x00\x00\x07\x00\x00\x07\x00\x00'\
b'\x07\x00\x08\x07\x00\x08\x07\x00\x08\x07\x00\x18\x07\x00\x18\x07'\
b'\x00\x38\x07\x00\xf8\x1f\xff\xf0\x7f\xff\xf0\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x0f\xf8\x1f\x80\x0f\xc0\x0f'\
b'\x80\x0f\x80\x0f\xc0\x0f\x80\x0d\xc0\x1b\x80\x0d\xc0\x1b\x80\x0d'\
b'\xe0\x13\x80\x0c\xe0\x33\x80\x0c\xe0\x33\x80\x0c\xf0\x23\x80\x0c'\
b'\x70\x63\x80\x0c\x70\x63\x80\x0c\x78\x63\x80\x0c\x38\xc3\x80\x0c'\
b'\x38\xc3\x80\x0c\x3c\xc3\x80\x0c\x1c\x83\x80\x0c\x1d\x83\x80\x0c'\
b'\x1f\x83\x80\x0c\x1f\x03\x80\x0c\x0f\x03\x80\x0c\x0f\x03\x80\x0c'\
b'\x0e\x03\x80\x3f\x06\x0f\xe0\xff\xc6\x3f\xf8\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x7f'\
b'\xe0\x0f\x80\x1f\x80\x07\xc0\x06\x00\x07\xe0\x06\x00\x07\xe0\x06'\
b'\x00\x06\xf0\x06\x00\x06\xf8\x06\x00\x06\x7c\x06\x00\x06\x3c\x06'\
b'\x00\x06\x3e\x06\x00\x06\x1f\x06\x00\x06\x0f\x06\x00\x06\x0f\x86'\
b'\x00\x06\x07\xc6\x00\x06\x03\xc6\x00\x06\x03\xe6\x00\x06\x01\xe6'\
b'\x00\x06\x00\xf6\x00\x06\x00\x76\x00\x06\x00\x7e\x00\x06\x00\x3e'\
b'\x00\x06\x00\x1e\x00\x06\x00\x1e\x00\x1f\x80\x0e\x00\x7f\xe0\x06'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\x00\x03\xff\xc0\x07\x81\xe0\x0e\x00\x70\x1e\x00\x78'\
b'\x1c\x00\x38\x3c\x00\x3c\x38\x00\x1c\x78\x00\x1e\x78\x00\x1e\x70'\
b'\x00\x0e\x70\x00\x0e\x70\x00\x0e\x70\x00\x0e\x70\x00\x0e\x78\x00'\
b'\x1e\x78\x00\x1c\x38\x00\x1c\x3c\x00\x3c\x1c\x00\x38\x1e\x00\x78'\
b'\x0e\x00\x70\x07\x81\xe0\x03\xff\xc0\x00\xff\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00'\
b'\x00\x00\x00\x00\x00\x00\x7f\xff\x00\x1f\xff\xc0\x07\x03\xe0\x07'\
b'\x00\xf0\x07\x00\x78\x07\x00\x78\x07\x00\x38\x07\x00\x38\x07\x00'\
b'\x78\x07\x00\x78\x07\x00\xf0\x07\x03\xe0\x07\xff\xc0\x07\xff\x00'\
b'\x07\x00\x00\x07\x00\x00\x07\x00\x00\x07\x00\x00\x07\x00\x00\x07'\
b'\x00\x00\x07\x00\x00\x07\x00\x00\x07\x00\x00\x1f\xc0\x00\x7f\xf0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x01\xff'\
b'\xc0\x07\x80\xf0\x0f\x00\x78\x1e\x00\x3c\x1c\x00\x1c\x3c\x00\x1e'\
b'\x38\x00\x0e\x78\x00\x0f\x78\x00\x0f\x70\x00\x07\x70\x00\x07\x70'\
b'\x00\x07\x70\x00\x07\x78\x00\x0f\x78\x00\x0f\x38\x3e\x0e\x3c\xef'\
b'\x1e\x3c\xc3\x9c\x1e\x81\xb8\x0e\x81\xb8\x0f\x81\xf0\x07\xc1\xe0'\
b'\x01\xff\xc0\x00\x7f\xe0\x00\x01\xe3\x00\x00\xe3\x00\x00\xf2\x00'\
b'\x00\xfe\x00\x00\x7c\x00\x00\x38\x17\x00\x00\x00\x00\x00\x00\x00'\
b'\x7f\xff\x00\x1f\xff\xc0\x07\x03\xe0\x07\x00\xe0\x07\x00\xf0\x07'\
b'\x00\x70\x07\x00\x70\x07\x00\xf0\x07\x00\xf0\x07\x00\xe0\x07\x01'\
b'\xe0\x07\x07\x80\x07\xfe\x00\x07\xff\x00\x07\x07\x80\x07\x03\x80'\
b'\x07\x03\xc0\x07\x01\xc0\x07\x01\xc0\x07\x01\xc4\x07\x01\xc4\x07'\
b'\x01\xc4\x07\x01\xec\x1f\xc0\xf8\x7f\xf0\xf0\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00'\
b'\x00\x00\x00\x00\x00\x03\xfc\x40\x0f\xfe\xc0\x1c\x07\xc0\x18\x01'\
b'\xc0\x38\x01\xc0\x38\x00\xc0\x38\x00\x40\x3c\x00\x40\x3c\x00\x00'\
b'\x1f\x80\x00\x1f\xf8\x00\x07\xff\x00\x01\xff\x80\x00\x1f\xc0\x00'\
b'\x03\xe0\x20\x01\xe0\x20\x00\xe0\x30\x00\xe0\x30\x00\xe0\x30\x00'\
b'\xe0\x38\x01\xe0\x3c\x01\xc0\x3e\x03\x80\x37\xff\x00\x21\xfc\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x15\x00\x00\x00\x00\x00\x00\x00\x7f\xff\xf0\x7f\xff\xf0'\
b'\x78\x71\xf0\x70\x70\x70\x60\x70\x30\x60\x70\x30\x40\x70\x10\x40'\
b'\x70\x10\x40\x70\x10\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70'\
b'\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00'\
b'\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x00\x70\x00\x01'\
b'\xfc\x00\x07\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xff\xe0\xff\xc0\x3f\x80\x3f\x00\x0e\x00\x0c\x00\x0e\x00\x0c'\
b'\x00\x0e\x00\x0c\x00\x0e\x00\x0c\x00\x0e\x00\x0c\x00\x0e\x00\x0c'\
b'\x00\x0e\x00\x0c\x00\x0e\x00\x0c\x00\x0e\x00\x0c\x00\x0e\x00\x0c'\
b'\x00\x0e\x00\x0c\x00\x0e\x00\x0c\x00\x0e\x00\x0c\x00\x0e\x00\x0c'\
b'\x00\x0e\x00\x0c\x00\x0e\x00\x0c\x00\x0e\x00\x0c\x00\x0f\x00\x18'\
b'\x00\x07\x00\x18\x00\x07\x80\x30\x00\x03\xe0\xf0\x00\x01\xff\xc0'\
b'\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00\x00'\
b'\x00\x00\x00\x00\x00\xff\xc3\xfe\x3e\x00\xf8\x1e\x00\x70\x1e\x00'\
b'\x70\x0e\x00\x60\x0f\x00\x60\x0f\x00\x40\x07\x00\xc0\x07\x80\xc0'\
b'\x07\x80\x80\x03\x81\x80\x03\xc1\x80\x03\xc1\x00\x01\xc3\x00\x01'\
b'\xe3\x00\x01\xe2\x00\x00\xe6\x00\x00\xf6\x00\x00\xf4\x00\x00\x7c'\
b'\x00\x00\x7c\x00\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x1f\xf1\xfe'\
b'\x7e\x07\xc0\x7c\x3c\x03\x80\x38\x1c\x03\x80\x30\x1e\x03\xc0\x30'\
b'\x1e\x03\xc0\x60\x0e\x03\xc0\x60\x0e\x03\xe0\x60\x0f\x03\xe0\x60'\
b'\x07\x06\xe0\xc0\x07\x06\xe0\xc0\x07\x84\xf0\xc0\x07\x8c\x70\xc0'\
b'\x03\x8c\x71\x80\x03\x8c\x79\x80\x03\xc8\x39\x80\x01\xd8\x39\x00'\
b'\x01\xf8\x3f\x00\x01\xf8\x1f\x00\x00\xf0\x1f\x00\x00\xf0\x1e\x00'\
b'\x00\xf0\x1e\x00\x00\xe0\x0e\x00\x00\x60\x0c\x00\x00\x60\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00'\
b'\xff\xc7\xfc\x3f\x01\xf0\x1f\x00\xe0\x0f\x01\xc0\x0f\x81\x80\x07'\
b'\x83\x80\x03\xc3\x00\x03\xe6\x00\x01\xee\x00\x00\xfc\x00\x00\xf8'\
b'\x00\x00\x78\x00\x00\x7c\x00\x00\x7c\x00\x00\xfe\x00\x01\xdf\x00'\
b'\x01\x8f\x00\x03\x87\x80\x03\x07\x80\x06\x03\xc0\x0e\x03\xe0\x0c'\
b'\x01\xe0\x1c\x00\xf0\x3e\x00\xf8\xff\x87\xfe\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00\x00'\
b'\x00\x00\x00\x00\x00\xff\x83\xfe\x7e\x00\xf8\x3e\x00\x70\x1e\x00'\
b'\x60\x0f\x00\xe0\x0f\x00\xc0\x07\x81\x80\x07\xc1\x80\x03\xc3\x00'\
b'\x03\xe3\x00\x01\xe6\x00\x00\xf6\x00\x00\xfc\x00\x00\x7c\x00\x00'\
b'\x78\x00\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00\x38'\
b'\x00\x00\x38\x00\x00\x38\x00\x00\x38\x00\x00\xfe\x00\x03\xff\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x3f\xff\xc0\x3f\xff\xc0'\
b'\x3c\x07\x80\x38\x07\x80\x30\x0f\x00\x30\x1f\x00\x30\x1e\x00\x20'\
b'\x3e\x00\x20\x3c\x00\x00\x78\x00\x00\x78\x00\x00\xf0\x00\x01\xf0'\
b'\x00\x01\xe0\x00\x03\xc0\x00\x03\xc0\x40\x07\x80\x40\x0f\x80\x40'\
b'\x0f\x00\xc0\x1f\x00\xc0\x1e\x00\xc0\x3c\x01\xc0\x3c\x03\xc0\x7f'\
b'\xff\xc0\x7f\xff\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x1f\xc0\x18'\
b'\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18'\
b'\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18'\
b'\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18'\
b'\x00\x18\x00\x18\x00\x1f\xc0\x00\x00\x00\x00\x14\x00\x00\x00\x00'\
b'\x00\x00\x00\x38\x00\x00\x1c\x00\x00\x1c\x00\x00\x0e\x00\x00\x0e'\
b'\x00\x00\x07\x00\x00\x07\x00\x00\x03\x80\x00\x03\x80\x00\x01\xc0'\
b'\x00\x01\xc0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\x70\x00'\
b'\x00\x70\x00\x00\x38\x00\x00\x38\x00\x00\x1c\x00\x00\x1c\x00\x00'\
b'\x0e\x00\x00\x0e\x00\x00\x07\x00\x00\x07\x00\x00\x03\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x7f\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x7f\x00'\
b'\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x00'\
b'\xf0\x00\x01\xf8\x00\x01\xf8\x00\x03\x9c\x00\x03\x9c\x00\x07\x0e'\
b'\x00\x07\x0e\x00\x0e\x07\x00\x0e\x07\x00\x1c\x03\x80\x1c\x03\x80'\
b'\x38\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00'

_index =\
b'\x00\x00\x44\x00\x88\x00\xcc\x00\x10\x01\x75\x01\xda\x01\x60\x02'\
b'\xe6\x02\x09\x03\x4d\x03\x91\x03\xf6\x03\x5b\x04\x9f\x04\xe3\x04'\
b'\x27\x05\x6b\x05\xd0\x05\x35\x06\x9a\x06\xff\x06\x64\x07\xc9\x07'\
b'\x2e\x08\x93\x08\xf8\x08\x5d\x09\xa1\x09\xe5\x09\x4a\x0a\xaf\x0a'\
b'\x14\x0b\x58\x0b\xde\x0b\x43\x0c\xa8\x0c\x0d\x0d\x93\x0d\xf8\x0d'\
b'\x5d\x0e\xe3\x0e\x69\x0f\xad\x0f\x12\x10\x98\x10\xfd\x10\x83\x11'\
b'\x09\x12\x6e\x12\xd3\x12\x38\x13\x9d\x13\x02\x14\x67\x14\xed\x14'\
b'\x52\x15\xd8\x15\x3d\x16\xa2\x16\x07\x17\x4b\x17\xb0\x17\xf4\x17'\
b'\x59\x18\x9d\x18'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 33
    return _mvfont[doff + 2:next_offs], 33, width
 