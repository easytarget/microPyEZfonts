'''
    mPyEZfont_u8g2_ncenR12_n.py : generated as part of the microPyEZfonts repository
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
# Font: ncenR12.bdf Char set:  %*+,-./0123456789:°
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/ncenR12.bdf 0 tmp_mPyEZfont_u8g2_ncenR12_n.py
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
    return 176

_font =\
b'\x07\x00\x38\x4c\xe6\x46\x06\x0c\x18\x10\x10\x00\x30\x30\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x1c\x40\x33\xc0\x22\x80\x62\x80\x45\x00\x45\x70\x3a\xc8'\
b'\x02\x88\x05\x88\x05\x10\x09\x10\x08\xe0\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x10\x54\xd6\x38\xd6\x54\x10\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x60\x60\x20\x20\x40\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x60\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x08\x08\x10\x10\x10\x20\x20\x40\x40\x40\x80\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x3c\x00\x66\x00\x42\x00'\
b'\xc3\x00\xc3\x00\xc3\x00\xc3\x00\xc3\x00\xc3\x00\x42\x00\x66\x00'\
b'\x3c\x00\x00\x00\x00\x00\x00\x00\x09\x00\x08\x00\x78\x00\x18\x00'\
b'\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00'\
b'\x7e\x00\x00\x00\x00\x00\x00\x00\x09\x00\x1c\x00\x22\x00\x43\x00'\
b'\x63\x00\x63\x00\x06\x00\x04\x00\x08\x00\x11\x00\x21\x00\x7f\x00'\
b'\x7f\x00\x00\x00\x00\x00\x00\x00\x09\x00\x3c\x00\x46\x00\x63\x00'\
b'\x63\x00\x06\x00\x1c\x00\x06\x00\x03\x00\x63\x00\x63\x00\x46\x00'\
b'\x3c\x00\x00\x00\x00\x00\x00\x00\x09\x00\x04\x00\x0c\x00\x1c\x00'\
b'\x2c\x00\x2c\x00\x4c\x00\x4c\x00\x8c\x00\xff\x00\x0c\x00\x0c\x00'\
b'\x3f\x00\x00\x00\x00\x00\x00\x00\x09\x00\x3f\x00\x3c\x00\x20\x00'\
b'\x20\x00\x3c\x00\x66\x00\x43\x00\x03\x00\x63\x00\x63\x00\x46\x00'\
b'\x3c\x00\x00\x00\x00\x00\x00\x00\x09\x00\x3c\x00\x66\x00\x46\x00'\
b'\xc0\x00\xc0\x00\xfc\x00\xe6\x00\xc3\x00\xc3\x00\xc3\x00\x66\x00'\
b'\x3c\x00\x00\x00\x00\x00\x00\x00\x09\x00\x7f\x00\x7f\x00\x42\x00'\
b'\x42\x00\x04\x00\x04\x00\x08\x00\x08\x00\x08\x00\x18\x00\x18\x00'\
b'\x18\x00\x00\x00\x00\x00\x00\x00\x09\x00\x3c\x00\x66\x00\x42\x00'\
b'\x62\x00\x76\x00\x3c\x00\x6e\x00\xc7\x00\xc3\x00\xc3\x00\x66\x00'\
b'\x3c\x00\x00\x00\x00\x00\x00\x00\x09\x00\x3c\x00\x66\x00\xc3\x00'\
b'\xc3\x00\xc3\x00\x67\x00\x3f\x00\x03\x00\x03\x00\x62\x00\x66\x00'\
b'\x38\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x60\x60'\
b'\x00\x00\x00\x00\x60\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x38\x4c\xe6\x46\x06\x0c\x18\x10\x10\x00\x30\x30\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x38\x44\x44\x44\x38\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'

_sparse =\
b'\x20\x00\x03\x00\x25\x00\x06\x00\x2a\x00\x0a\x00\x2b\x00\x0d\x00'\
b'\x2c\x00\x11\x00\x2d\x00\x14\x00\x2e\x00\x17\x00\x2f\x00\x1a\x00'\
b'\x30\x00\x1d\x00\x31\x00\x21\x00\x32\x00\x25\x00\x33\x00\x29\x00'\
b'\x34\x00\x2d\x00\x35\x00\x31\x00\x36\x00\x35\x00\x37\x00\x39\x00'\
b'\x38\x00\x3d\x00\x39\x00\x41\x00\x3a\x00\x45\x00\x3f\x00\x48\x00'\
b'\xb0\x00\x4b\x00'

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
 
