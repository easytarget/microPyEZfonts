'''
    mPyEZfont_u8g2_ncenR18_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenR18.bdf font file was sourced from the U8G2 project:
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
# Font: ncenR18.bdf Char set:  %()*+,-./0123456789:°
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./n-char.set -e 32 ../u8g2/tools/font/bdf/ncenR18.bdf 0 tmp_mPyEZfont_u8g2_ncenR18_n.py
version = '0.33'

def height():
    return 22

def baseline():
    return 18

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
    return 176

_font =\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x0f\x0c\x00\x19\x94\x00\x30\xec\x00\x30\x88\x00\x60\x98'\
b'\x00\x60\x90\x00\x61\x30\x00\x61\x20\x00\x62\x63\xc0\x3c\x46\x60'\
b'\x00\xcc\x20\x00\x8c\x20\x01\x98\x20\x01\x18\x20\x03\x18\x40\x02'\
b'\x18\x40\x06\x18\x80\x04\x0f\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x01\x00\x06\x00\x0c\x00'\
b'\x18\x00\x18\x00\x30\x00\x30\x00\x60\x00\x60\x00\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x60\x00\x30\x00\x30\x00\x18\x00\x18\x00\x0c\x00'\
b'\x06\x00\x01\x00\x00\x00\x00\x00\x08\x00\x80\x60\x30\x18\x18\x0c'\
b'\x0c\x06\x06\x06\x06\x06\x06\x06\x0c\x0c\x18\x18\x30\x60\x80\x00'\
b'\x09\x00\x08\x00\x1c\x00\x49\x00\x6b\x00\x1c\x00\x6b\x00\x49\x00'\
b'\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x7f\xf8\x7f\xf8\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x30\x78\x78\x18\x10\x20\x40\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x7e\x7e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x38\x38\x38\x00\x00\x00\x00\x08\x00\x06\x06\x06\x0c\x0c\x0c'\
b'\x18\x18\x18\x30\x30\x30\x60\x60\x60\xc0\xc0\xc0\x00\x00\x00\x00'\
b'\x0d\x00\x07\x00\x08\x80\x18\xc0\x10\x40\x30\x60\x30\x60\x70\x70'\
b'\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x30\x60\x30\x60\x10\x40'\
b'\x18\xc0\x08\x80\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x01\x00\x07\x00\x1f\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x0f\x80\x38\xe0\x20\x60\x70\x70\x70\x70\x20\x70\x00\x60'\
b'\x00\xe0\x00\xc0\x01\x80\x03\x00\x06\x00\x0c\x00\x18\x10\x30\x10'\
b'\x60\x30\x7f\xf0\x7f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x0f\x80\x31\xc0\x60\xe0\x70\xe0\x70\xe0\x20\xc0\x00\xc0'\
b'\x01\x80\x0f\x80\x00\xc0\x00\x60\x00\x70\x20\x70\x70\x70\x70\x60'\
b'\x60\xe0\x30\xc0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x40\x00\xc0\x01\xc0\x03\xc0\x06\xc0\x0c\xc0\x08\xc0'\
b'\x18\xc0\x30\xc0\x60\xc0\x40\xc0\xc0\xc0\x80\xc0\xff\xf0\x00\xc0'\
b'\x00\xc0\x00\xc0\x03\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x3f\xe0\x3f\xc0\x20\x00\x20\x00\x20\x00\x20\x00\x20\x00'\
b'\x2f\x80\x31\xc0\x00\x60\x00\x60\x00\x70\x30\x70\x70\x70\x70\x60'\
b'\x20\x60\x30\xc0\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x07\xc0\x1c\x70\x10\x70\x30\x30\x30\x00\x30\x00\x70\x00'\
b'\x77\x80\x78\xc0\x70\x60\x70\x60\x70\x70\x70\x70\x30\x70\x30\x60'\
b'\x30\x60\x18\xc0\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x3f\xf0\x3f\xf0\x20\x20\x20\x60\x00\x40\x00\xc0\x00\xc0'\
b'\x00\x80\x01\x80\x01\x80\x01\x00\x03\x00\x03\x00\x03\x00\x07\x00'\
b'\x07\x00\x07\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x0f\x80\x18\xc0\x10\x40\x30\x60\x30\x60\x38\x60\x1c\xc0'\
b'\x1f\x80\x0f\x80\x1b\xc0\x30\xe0\x60\x70\x60\x30\x60\x30\x60\x30'\
b'\x30\x60\x38\xe0\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x0f\x80\x18\xc0\x38\x60\x30\x60\x70\x70\x70\x70\x70\x70'\
b'\x30\x70\x38\x70\x18\xf0\x0f\x70\x00\x70\x00\x60\x00\x60\x60\xe0'\
b'\x70\xc0\x71\xc0\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x38\x38\x38\x00\x00\x00\x00\x00'\
b'\x00\x38\x38\x38\x00\x00\x00\x00\x09\x00\x3c\x00\x66\x00\xc3\x00'\
b'\xc3\x00\xc3\x00\x66\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00'

_sparse =\
b'\x20\x00\x03\x00\x25\x00\x06\x00\x28\x00\x0f\x00\x29\x00\x15\x00'\
b'\x2a\x00\x18\x00\x2b\x00\x1e\x00\x2c\x00\x24\x00\x2d\x00\x27\x00'\
b'\x2e\x00\x2a\x00\x2f\x00\x2d\x00\x30\x00\x30\x00\x31\x00\x36\x00'\
b'\x32\x00\x3c\x00\x33\x00\x42\x00\x34\x00\x48\x00\x35\x00\x4e\x00'\
b'\x36\x00\x54\x00\x37\x00\x5a\x00\x38\x00\x60\x00\x39\x00\x66\x00'\
b'\x3a\x00\x6c\x00\xb0\x00\x6f\x00'

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
 
