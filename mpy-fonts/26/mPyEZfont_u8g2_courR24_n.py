'''
    mPyEZfont_u8g2_courR24_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original courR24.bdf font file was sourced from the U8G2 project:
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
# Font: courR24.bdf Char set:  %()*+,-./0123456789:°
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./n-char.set -e 32 ../u8g2/tools/font/bdf/courR24.bdf 0 tmp_mPyEZfont_u8g2_courR24_n.py
version = '0.33'

def height():
    return 26

def baseline():
    return 22

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
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x00\x06\x60\x00\x0c\x30'\
b'\x00\x08\x10\x00\x08\x10\x00\x0c\x30\x00\x06\x60\x00\x03\xc1\xc0'\
b'\x00\x0e\x00\x00\x70\x00\x03\x80\x00\x1c\x00\x00\x00\x3c\x00\x00'\
b'\x66\x00\x00\xc3\x00\x00\x81\x00\x00\x81\x00\x00\xc3\x00\x00\x66'\
b'\x00\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x04\x00\x00\x0c\x00\x00\x08\x00\x00\x18'\
b'\x00\x00\x10\x00\x00\x30\x00\x00\x30\x00\x00\x20\x00\x00\x20\x00'\
b'\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00\x60\x00\x00'\
b'\x60\x00\x00\x60\x00\x00\x20\x00\x00\x20\x00\x00\x30\x00\x00\x30'\
b'\x00\x00\x10\x00\x00\x18\x00\x00\x08\x00\x00\x0c\x00\x00\x04\x00'\
b'\x14\x00\x00\x00\x00\x04\x00\x00\x06\x00\x00\x02\x00\x00\x03\x00'\
b'\x00\x01\x00\x00\x01\x80\x00\x01\x80\x00\x00\x80\x00\x00\x80\x00'\
b'\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00\x00\xc0\x00\x00'\
b'\xc0\x00\x00\xc0\x00\x00\x80\x00\x00\x80\x00\x01\x80\x00\x01\x80'\
b'\x00\x01\x00\x00\x03\x00\x00\x02\x00\x00\x06\x00\x00\x04\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40'\
b'\x00\x08\x42\x00\x0f\x5e\x00\x01\xf0\x00\x00\xe0\x00\x00\xa0\x00'\
b'\x01\xb0\x00\x03\x18\x00\x02\x08\x00\x06\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40'\
b'\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00'\
b'\x00\x40\x00\x00\x40\x00\x3f\xff\x80\x00\x40\x00\x00\x40\x00\x00'\
b'\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x01\xe0\x00\x01\xe0\x00\x03\xc0\x00\x03\xc0'\
b'\x00\x03\x00\x00\x07\x00\x00\x06\x00\x00\x06\x00\x00\x04\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x3f\xff\x80\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x01\xf0\x00\x01\xf0'\
b'\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x02\x00\x00\x06\x00\x00\x04\x00\x00\x04\x00\x00\x0c'\
b'\x00\x00\x08\x00\x00\x18\x00\x00\x10\x00\x00\x30\x00\x00\x20\x00'\
b'\x00\x20\x00\x00\x60\x00\x00\x40\x00\x00\xc0\x00\x00\x80\x00\x00'\
b'\x80\x00\x01\x80\x00\x01\x00\x00\x03\x00\x00\x02\x00\x00\x06\x00'\
b'\x00\x04\x00\x00\x04\x00\x00\x0c\x00\x00\x08\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x01\xf0\x00\x03\x18\x00\x06\x0c'\
b'\x00\x04\x04\x00\x04\x04\x00\x08\x02\x00\x08\x02\x00\x08\x02\x00'\
b'\x08\x02\x00\x08\x02\x00\x08\x02\x00\x08\x02\x00\x08\x02\x00\x08'\
b'\x02\x00\x0c\x06\x00\x04\x04\x00\x04\x04\x00\x06\x0c\x00\x03\x18'\
b'\x00\x01\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x03\xc0\x00\x0e\x40'\
b'\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00'\
b'\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00'\
b'\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40\x00\x00\x40'\
b'\x00\x0f\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x01\xf8\x00\x06\x0c\x00\x0c\x02'\
b'\x00\x08\x02\x00\x08\x02\x00\x00\x02\x00\x00\x06\x00\x00\x04\x00'\
b'\x00\x0c\x00\x00\x18\x00\x00\x30\x00\x00\x60\x00\x00\xc0\x00\x01'\
b'\x80\x00\x03\x00\x00\x06\x00\x00\x0c\x00\x00\x18\x00\x00\x10\x01'\
b'\x00\x1f\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x01\xf0\x00\x07\x1c\x00\x0c\x06'\
b'\x00\x00\x02\x00\x00\x02\x00\x00\x02\x00\x00\x02\x00\x00\x04\x00'\
b'\x00\x08\x00\x00\xf0\x00\x00\x0c\x00\x00\x02\x00\x00\x01\x00\x00'\
b'\x01\x00\x00\x01\x00\x00\x01\x00\x00\x03\x00\x18\x06\x00\x0e\x1c'\
b'\x00\x03\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x28\x00\x00\x28'\
b'\x00\x00\x48\x00\x00\xc8\x00\x00\x88\x00\x01\x08\x00\x03\x08\x00'\
b'\x02\x08\x00\x04\x08\x00\x0c\x08\x00\x08\x08\x00\x10\x08\x00\x1f'\
b'\xff\x00\x00\x08\x00\x00\x08\x00\x00\x08\x00\x00\x08\x00\x00\x08'\
b'\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x07\xfe\x00\x04\x00\x00\x04\x00'\
b'\x00\x04\x00\x00\x04\x00\x00\x04\x00\x00\x04\x00\x00\x04\xf0\x00'\
b'\x07\x9c\x00\x04\x06\x00\x00\x02\x00\x00\x03\x00\x00\x01\x00\x00'\
b'\x01\x00\x00\x01\x00\x00\x03\x00\x18\x02\x00\x0c\x06\x00\x07\x1c'\
b'\x00\x01\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x7c\x00\x01\xc2\x00\x03\x00'\
b'\x00\x02\x00\x00\x06\x00\x00\x04\x00\x00\x0c\x00\x00\x08\xf8\x00'\
b'\x0b\x8e\x00\x0a\x02\x00\x0c\x03\x00\x0c\x01\x00\x0c\x01\x00\x0c'\
b'\x01\x00\x0c\x01\x00\x04\x01\x00\x06\x03\x00\x02\x02\x00\x03\x8e'\
b'\x00\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x0f\xfe\x00\x08\x02\x00\x08\x02'\
b'\x00\x00\x06\x00\x00\x04\x00\x00\x04\x00\x00\x0c\x00\x00\x08\x00'\
b'\x00\x08\x00\x00\x18\x00\x00\x10\x00\x00\x10\x00\x00\x30\x00\x00'\
b'\x20\x00\x00\x20\x00\x00\x20\x00\x00\x60\x00\x00\x40\x00\x00\x40'\
b'\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x01\xf0\x00\x06\x0c\x00\x04\x04'\
b'\x00\x0c\x06\x00\x08\x02\x00\x08\x02\x00\x0c\x06\x00\x04\x04\x00'\
b'\x03\x18\x00\x01\xf0\x00\x07\x1c\x00\x04\x04\x00\x0c\x06\x00\x08'\
b'\x02\x00\x08\x02\x00\x08\x02\x00\x0c\x06\x00\x04\x04\x00\x07\x1c'\
b'\x00\x01\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x01\xf0\x00\x07\x0c\x00\x04\x06'\
b'\x00\x0c\x02\x00\x08\x03\x00\x08\x03\x00\x08\x03\x00\x08\x03\x00'\
b'\x0c\x05\x00\x04\x0d\x00\x07\x39\x00\x01\xe1\x00\x00\x02\x00\x00'\
b'\x02\x00\x00\x02\x00\x00\x04\x00\x00\x0c\x00\x00\x18\x00\x00\xe0'\
b'\x00\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x01\xf0\x00'\
b'\x01\xf0\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x01\xf0\x00\x01\xf0'\
b'\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x01\xf0\x00\x03\x18\x00\x02\x08\x00\x06\x0c'\
b'\x00\x04\x04\x00\x04\x04\x00\x06\x0c\x00\x02\x08\x00\x03\x18\x00'\
b'\x01\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

_sparse =\
b'\x20\x00\x0a\x00\x25\x00\x14\x00\x28\x00\x1e\x00\x29\x00\x28\x00'\
b'\x2a\x00\x32\x00\x2b\x00\x3c\x00\x2c\x00\x46\x00\x2d\x00\x50\x00'\
b'\x2e\x00\x5a\x00\x2f\x00\x64\x00\x30\x00\x6e\x00\x31\x00\x78\x00'\
b'\x32\x00\x82\x00\x33\x00\x8c\x00\x34\x00\x96\x00\x35\x00\xa0\x00'\
b'\x36\x00\xaa\x00\x37\x00\xb4\x00\x38\x00\xbe\x00\x39\x00\xc8\x00'\
b'\x3a\x00\xd2\x00\xb0\x00\xdc\x00'

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

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 26
    return _mvfont[doff + 2:next_offs], 26, width
 
