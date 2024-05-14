'''
    mPyEZfont_u8g2_timR24_t.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original timR24.bdf font file was sourced from the U8G2 project:
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
# Font: timR24.bdf Char set:  +-.0123456789:
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./t-char.set -e 32 ../u8g2/tools/font/bdf/timR24.bdf 0 tmp_mPyEZfont_u8g2_timR24_t.py
version = '0.33'

def height():
    return 23

def baseline():
    return 23

def max_width():
    return 19

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
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00\x00'\
b'\xc0\x00\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00\x7f\xff\x80\x7f\xff'\
b'\x80\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00'\
b'\x00\xc0\x00\x00\xc0\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x7f\x80\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x3c'\
b'\x3c\x18\x10\x00\x03\xc0\x0e\x70\x1c\x38\x18\x18\x38\x1c\x38\x1c'\
b'\x30\x0c\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e'\
b'\x70\x0e\x70\x0e\x70\x0c\x38\x1c\x38\x1c\x18\x18\x1c\x38\x0e\x70'\
b'\x03\xc0\x10\x00\x00\xc0\x01\xc0\x07\xc0\x0d\xc0\x01\xc0\x01\xc0'\
b'\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0'\
b'\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x03\xe0'\
b'\x0f\xf8\x10\x00\x07\xe0\x0f\xf0\x1c\xf8\x30\x3c\x20\x3c\x60\x1c'\
b'\x40\x1c\x00\x1c\x00\x1c\x00\x18\x00\x38\x00\x30\x00\x60\x00\x60'\
b'\x00\xc0\x01\x80\x03\x00\x06\x00\x0c\x02\x18\x06\x3f\xfc\x7f\xf8'\
b'\xff\xf8\x10\x00\x03\xe0\x0f\xf0\x18\x78\x30\x38\x20\x38\x00\x38'\
b'\x00\x30\x00\x30\x00\x60\x00\xc0\x01\xf0\x07\xf8\x00\x7c\x00\x1c'\
b'\x00\x1c\x00\x0c\x00\x0c\x00\x0c\x00\x1c\x00\x18\x38\x30\x3c\xe0'\
b'\x1f\xc0\x10\x00\x00\x30\x00\x70\x00\x70\x00\xf0\x00\xb0\x01\xb0'\
b'\x03\x30\x02\x30\x06\x30\x0c\x30\x08\x30\x18\x30\x30\x30\x20\x30'\
b'\x7f\xfe\x7f\xfe\x7f\xfe\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30'\
b'\x00\x30\x10\x00\x07\xfc\x0f\xf8\x0f\xf0\x08\x00\x18\x00\x10\x00'\
b'\x3f\x00\x3f\xc0\x3f\xe0\x03\xf0\x00\xf0\x00\x78\x00\x38\x00\x38'\
b'\x00\x18\x00\x18\x00\x18\x00\x18\x00\x30\x00\x30\x70\x60\x79\xc0'\
b'\x3f\x00\x10\x00\x00\x3c\x00\xe0\x01\xc0\x07\x80\x0f\x00\x0e\x00'\
b'\x1c\x00\x3c\x00\x38\x00\x39\xe0\x7b\xf8\x7c\x3c\x70\x1c\x70\x1e'\
b'\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x38\x0e\x38\x0c\x1c\x1c\x0e\x30'\
b'\x03\xe0\x10\x00\x1f\xfe\x3f\xfe\x30\x0c\x60\x0c\x40\x1c\x00\x18'\
b'\x00\x18\x00\x18\x00\x30\x00\x30\x00\x30\x00\x70\x00\x60\x00\x60'\
b'\x00\xe0\x00\xc0\x00\xc0\x00\xc0\x01\x80\x01\x80\x01\x80\x03\x80'\
b'\x03\x00\x10\x00\x07\xe0\x0e\x38\x1c\x1c\x38\x0c\x38\x0c\x38\x0c'\
b'\x38\x1c\x3c\x18\x1f\x30\x0f\xc0\x07\xe0\x03\xf0\x06\xf8\x1c\x7c'\
b'\x18\x3c\x38\x1e\x30\x1e\x30\x0e\x30\x0e\x38\x0e\x18\x1c\x1c\x38'\
b'\x07\xf0\x10\x00\x03\xc0\x0c\x70\x18\x38\x38\x1c\x30\x1c\x70\x0e'\
b'\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x78\x0e\x38\x0e\x3c\x1e\x1f\x7e'\
b'\x07\xdc\x00\x1c\x00\x38\x00\x38\x00\x70\x00\xe0\x01\xc0\x07\x80'\
b'\x3c\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x18\x00\x3c\x00\x3c\x00\x18\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x3c\x00\x3c\x00'\
b'\x18\x00'

_index =\
b'\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x32\x00\x00\x00\x79\x00\xa9\x00'\
b'\x00\x00\xc2\x00\xf2\x00\x22\x01\x52\x01\x82\x01\xb2\x01\xe2\x01'\
b'\x12\x02\x42\x02\x72\x02\xa2\x02\xd2\x02'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 58 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 23
    return _mvfont[doff + 2:next_offs], 23, width
 