'''
    mPyEZfont_u8g2_ncenB10_n.py : generated as part of the microPyEZfonts repository
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
# Font: ncenB10.bdf Char set:  %()*+,-./0123456789:°
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./n-char.set -e 32 ../u8g2/tools/font/bdf/ncenB10.bdf 0 tmp_mPyEZfont_u8g2_ncenB10_n.py
version = '0.33'

def height():
    return 13

def baseline():
    return 11

def max_width():
    return 13

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
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x30\x80\x6f\x00\xc9\x00\xca\x00\xd2\x00\x64\x60\x04\xd0'\
b'\x09\x90\x09\x90\x11\xa0\x10\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x10\x20\x60\x40\xc0\xc0\xc0\xc0\xc0\x40\x60\x20\x10\x00'\
b'\x05\x00\x80\x40\x60\x20\x30\x30\x30\x30\x30\x20\x60\x40\x80\x00'\
b'\x06\x00\x20\xa8\x70\xa8\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x10\x10\x10\xfe\x10\x10\x10\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x60\x20\x40\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x60\x00\x00\x00'\
b'\x05\x00\x10\x10\x10\x20\x20\x20\x40\x40\x40\x80\x80\x00\x00\x00'\
b'\x08\x00\x38\x6c\xc6\xc6\xc6\xc6\xc6\xc6\xc6\x6c\x38\x00\x00\x00'\
b'\x08\x00\x18\x78\x18\x18\x18\x18\x18\x18\x18\x18\x3c\x00\x00\x00'\
b'\x08\x00\x78\xce\xc6\x06\x06\x0c\x18\x30\x62\xfe\xfe\x00\x00\x00'\
b'\x08\x00\x78\xce\xc6\x06\x0c\x3c\x06\x06\xc6\xce\x78\x00\x00\x00'\
b'\x08\x00\x0c\x1c\x1c\x2c\x2c\x4c\x4c\xfe\x0c\x0c\x1e\x00\x00\x00'\
b'\x08\x00\x7e\x7c\x40\x40\x5c\x6e\x06\x06\xc6\xce\x78\x00\x00\x00'\
b'\x08\x00\x3c\x66\xc6\xc0\xdc\xee\xc6\xc6\xc6\xe6\x78\x00\x00\x00'\
b'\x08\x00\xfe\xfe\x84\x8c\x0c\x18\x18\x18\x30\x30\x30\x00\x00\x00'\
b'\x08\x00\x78\xe6\xc6\xc6\xf4\x3c\x5e\xc6\xc6\xce\x3c\x00\x00\x00'\
b'\x08\x00\x3c\xce\xc6\xc6\xc6\xee\x76\x06\xc6\xcc\x78\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x60\x60\x60\x00\x60\x60\x60\x00\x00\x00'\
b'\x06\x00\x30\x48\x48\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00'

_sparse =\
b'\x20\x00\x02\x00\x25\x00\x04\x00\x28\x00\x08\x00\x29\x00\x0a\x00'\
b'\x2a\x00\x0c\x00\x2b\x00\x0e\x00\x2c\x00\x10\x00\x2d\x00\x12\x00'\
b'\x2e\x00\x14\x00\x2f\x00\x16\x00\x30\x00\x18\x00\x31\x00\x1a\x00'\
b'\x32\x00\x1c\x00\x33\x00\x1e\x00\x34\x00\x20\x00\x35\x00\x22\x00'\
b'\x36\x00\x24\x00\x37\x00\x26\x00\x38\x00\x28\x00\x39\x00\x2a\x00'\
b'\x3a\x00\x2c\x00\xb0\x00\x2e\x00'

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

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 13
    return _mvfont[doff + 2:next_offs], 13, width
 
