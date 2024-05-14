'''
    mPyEZfont_u8g2_ncenR24_t.py : generated as part of the microPyEZfonts repository
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
# Font: ncenR24.bdf Char set:  +-.0123456789:
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./t-char.set -e 32 ../u8g2/tools/font/bdf/ncenR24.bdf 0 tmp_mPyEZfont_u8g2_ncenR24_t.py
version = '0.33'

def height():
    return 25

def baseline():
    return 24

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
    return 58

_font =\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00\x60'\
b'\x00\x00\x60\x00\x00\x60\x00\x3f\xff\xc0\x3f\xff\xc0\x00\x60\x00'\
b'\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00'\
b'\x60\x00\x00\x60\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x7f\x80\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x18\x00\x3c\x00\x3c\x00\x18\x00\x00\x00\x12\x00\x00'\
b'\xf0\x00\x03\xfc\x00\x07\x0e\x00\x06\x06\x00\x0e\x07\x00\x1e\x07'\
b'\x80\x1c\x03\x80\x3c\x03\xc0\x3c\x03\xc0\x3c\x03\xc0\x3c\x03\xc0'\
b'\x3c\x03\xc0\x3c\x03\xc0\x3c\x03\xc0\x3c\x03\xc0\x3c\x03\xc0\x3c'\
b'\x03\xc0\x1c\x03\x80\x1e\x07\x80\x0e\x07\x00\x06\x06\x00\x07\x0e'\
b'\x00\x03\xfc\x00\x00\xf0\x00\x00\x00\x00\x12\x00\x00\x60\x00\x00'\
b'\xe0\x00\x1f\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0'\
b'\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00'\
b'\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00'\
b'\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x01\xf0'\
b'\x00\x1f\xff\x00\x00\x00\x00\x12\x00\x03\xf0\x00\x0f\xfc\x00\x1c'\
b'\x0e\x00\x30\x0f\x00\x38\x07\x00\x3c\x07\x00\x3c\x07\x00\x3c\x07'\
b'\x00\x18\x0f\x00\x00\x0e\x00\x00\x0e\x00\x00\x1c\x00\x00\x3c\x00'\
b'\x00\x38\x00\x00\x70\x00\x00\xe0\x00\x01\xc0\x00\x03\x81\x00\x07'\
b'\x01\x00\x0e\x03\x00\x1c\x03\x00\x3f\xff\x00\x7f\xff\x00\x7f\xff'\
b'\x00\x00\x00\x00\x12\x00\x03\xf0\x00\x0f\xfc\x00\x1c\x1c\x00\x38'\
b'\x0e\x00\x3c\x0e\x00\x3c\x0e\x00\x18\x0e\x00\x00\x0e\x00\x00\x1c'\
b'\x00\x00\x38\x00\x00\xf0\x00\x07\xf8\x00\x00\x7c\x00\x00\x1e\x00'\
b'\x00\x0e\x00\x00\x0f\x00\x30\x07\x00\x78\x07\x00\x78\x07\x00\x78'\
b'\x0f\x00\x70\x0e\x00\x3c\x3e\x00\x1f\xf8\x00\x07\xe0\x00\x00\x00'\
b'\x00\x12\x00\x00\x18\x00\x00\x18\x00\x00\x38\x00\x00\x78\x00\x00'\
b'\xf8\x00\x00\xf8\x00\x01\xb8\x00\x03\x38\x00\x03\x38\x00\x06\x38'\
b'\x00\x0c\x38\x00\x0c\x38\x00\x18\x38\x00\x30\x38\x00\x30\x38\x00'\
b'\x60\x38\x00\x7f\xff\x80\x7f\xff\x80\x00\x38\x00\x00\x38\x00\x00'\
b'\x38\x00\x00\x38\x00\x00\x7c\x00\x01\xff\x00\x00\x00\x00\x12\x00'\
b'\x0e\x02\x00\x0f\xfe\x00\x0f\xfc\x00\x0f\xf8\x00\x0c\x00\x00\x0c'\
b'\x00\x00\x08\x00\x00\x18\x00\x00\x18\xf0\x00\x1b\xfc\x00\x1f\x1e'\
b'\x00\x1c\x0e\x00\x18\x0f\x00\x00\x07\x00\x00\x07\x00\x00\x07\x00'\
b'\x18\x07\x00\x3c\x07\x00\x3c\x07\x00\x3c\x0f\x00\x38\x0e\x00\x1c'\
b'\x1e\x00\x1f\xfc\x00\x07\xe0\x00\x00\x00\x00\x12\x00\x01\xf8\x00'\
b'\x07\xfe\x00\x0e\x1f\x00\x1c\x0f\x00\x1c\x0f\x00\x18\x06\x00\x38'\
b'\x00\x00\x38\x00\x00\x38\x00\x00\x78\xf0\x00\x7b\xfc\x00\x7f\x1e'\
b'\x00\x7e\x0e\x00\x7c\x0f\x00\x78\x07\x00\x78\x07\x00\x78\x07\x00'\
b'\x38\x07\x00\x38\x07\x00\x38\x0f\x00\x1c\x0e\x00\x1c\x1e\x00\x0f'\
b'\xf8\x00\x03\xe0\x00\x00\x00\x00\x12\x00\x1f\xff\x00\x1f\xff\x00'\
b'\x1f\xff\x00\x18\x02\x00\x18\x06\x00\x10\x04\x00\x10\x0c\x00\x10'\
b'\x08\x00\x00\x18\x00\x00\x18\x00\x00\x30\x00\x00\x30\x00\x00\x30'\
b'\x00\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00\xe0\x00\x00\xe0\x00'\
b'\x00\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x00'\
b'\xc0\x00\x00\x00\x00\x12\x00\x03\xf0\x00\x0f\xfc\x00\x1e\x1c\x00'\
b'\x1c\x0e\x00\x38\x0e\x00\x38\x06\x00\x38\x06\x00\x3c\x0c\x00\x1e'\
b'\x1c\x00\x1f\xb8\x00\x0f\xf0\x00\x03\xf8\x00\x03\xfc\x00\x0e\xfe'\
b'\x00\x1c\x3e\x00\x38\x0f\x00\x38\x0f\x00\x70\x07\x00\x70\x07\x00'\
b'\x70\x07\x00\x38\x0e\x00\x3c\x1e\x00\x1f\xfc\x00\x07\xf0\x00\x00'\
b'\x00\x00\x12\x00\x07\xe0\x00\x1f\xf8\x00\x3c\x3c\x00\x38\x1c\x00'\
b'\x78\x1e\x00\x70\x0e\x00\x70\x0e\x00\x70\x0f\x00\x70\x0f\x00\x78'\
b'\x0f\x00\x78\x1f\x00\x3c\x3f\x00\x3c\x3f\x00\x1f\xef\x00\x0f\xcf'\
b'\x00\x00\x0f\x00\x00\x0e\x00\x00\x0e\x00\x30\x1c\x00\x78\x1c\x00'\
b'\x78\x38\x00\x78\xf0\x00\x3f\xe0\x00\x1f\x80\x00\x00\x00\x00\x09'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x0c\x00\x1e\x00\x1e\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1e\x00\x1e\x00\x0c'\
b'\x00\x00\x00'

_index =\
b'\x00\x00\x34\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x68\x00\x00\x00\xb5\x00\xe9\x00'\
b'\x00\x00\x1d\x01\x6a\x01\xb7\x01\x04\x02\x51\x02\x9e\x02\xeb\x02'\
b'\x38\x03\x85\x03\xd2\x03\x1f\x04\x53\x04'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 58 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 25
    return _mvfont[doff + 2:next_offs], 25, width
 