'''
    mPyEZfont_u8g2_ncenB24_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenB24.bdf font file was sourced from the U8G2 project:
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
# Font: ncenB24.bdf Char set:  %*+,-./0123456789:ø
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/ncenB24.bdf 0 tmp_mPyEZfont_u8g2_ncenB24_n.py
version = '0.33'

def height():
    return 30

def baseline():
    return 25

def max_width():
    return 27

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 248

_font =\
b'\x10\x00\x07\xe0\x1f\xf8\x38\xfc\x78\x7c\x7c\x7e\x7c\x7e\x7c\x7e'\
b'\x38\x7e\x00\x7c\x00\xfc\x00\xf8\x01\xf0\x01\xc0\x03\x80\x03\x80'\
b'\x03\x00\x03\x00\x00\x00\x00\x00\x07\x80\x0f\xc0\x0f\xc0\x0f\xc0'\
b'\x0f\xc0\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x1b\x00\x00\x00\x00\x00\x00\x00\x18\x00\x07\xc0\x30\x00\x0f\x60'\
b'\x70\x00\x1e\x39\xe0\x00\x3c\x1f\x60\x00\x3c\x10\xc0\x00\x78\x10'\
b'\x80\x00\x78\x11\x80\x00\xf0\x31\x00\x00\xf0\x23\x00\x00\xf0\x62'\
b'\x00\x00\xf0\xc6\x1f\x00\x7b\x8c\x3d\x80\x3f\x0c\x78\xc0\x00\x18'\
b'\xf0\x40\x00\x11\xf0\x40\x00\x31\xe0\x40\x00\x21\xe0\xc0\x00\x63'\
b'\xe0\xc0\x00\xc3\xc1\x80\x00\xc3\xc1\x80\x01\x83\xc3\x00\x01\x81'\
b'\xe6\x00\x03\x00\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x11\x00\x01\x80\x00\x03\x80\x00\x03\x80\x00\x39\x9c\x00\x39\x9c'\
b'\x00\x3d\xbc\x00\x0f\xf0\x00\x03\xc0\x00\x1f\xf8\x00\x3d\xbc\x00'\
b'\x39\x9c\x00\x39\x9c\x00\x01\xc0\x00\x01\xc0\x00\x01\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x00\xf0\x00'\
b'\x00\xf0\x00\x00\xf0\x00\x00\xf0\x00\x00\xf0\x00\x3f\xff\xc0\x3f'\
b'\xff\xc0\x3f\xff\xc0\x3f\xff\xc0\x00\xf0\x00\x00\xf0\x00\x00\xf0'\
b'\x00\x00\xf0\x00\x00\xf0\x00\x00\xf0\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x3e\x00\x3f\x00\x3f\x00'\
b'\x3f\x00\x1f\x00\x07\x00\x06\x00\x0c\x00\x1c\x00\x38\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x7f\x80\x7f\x80\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x7e\x00\x7e\x00\x7e\x00'\
b'\x7e\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\xc0\x01\xc0\x01\xc0\x01\x80\x03\x80\x03\x80\x03\x00'\
b'\x07\x00\x07\x00\x06\x00\x0e\x00\x0e\x00\x0c\x00\x1c\x00\x1c\x00'\
b'\x18\x00\x38\x00\x38\x00\x30\x00\x70\x00\x70\x00\x60\x00\xe0\x00'\
b'\xe0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x01\xe0\x00\x07\xf8\x00\x0f\x3c\x00\x1e\x1e'\
b'\x00\x3e\x1f\x00\x3c\x0f\x00\x7c\x0f\x80\x7c\x0f\x80\x7c\x0f\x80'\
b'\x7c\x0f\x80\x7c\x0f\x80\x7c\x0f\x80\x7c\x0f\x80\x7c\x0f\x80\x7c'\
b'\x0f\x80\x7c\x0f\x80\x7c\x0f\x80\x3c\x0f\x00\x3c\x0f\x00\x3e\x1f'\
b'\x00\x1e\x1e\x00\x0f\x3c\x00\x07\xf8\x00\x01\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x00\x30\x00\x00\xf0\x00\x1f\xf0\x00\x1f\xf0'\
b'\x00\x01\xf0\x00\x01\xf0\x00\x01\xf0\x00\x01\xf0\x00\x01\xf0\x00'\
b'\x01\xf0\x00\x01\xf0\x00\x01\xf0\x00\x01\xf0\x00\x01\xf0\x00\x01'\
b'\xf0\x00\x01\xf0\x00\x01\xf0\x00\x01\xf0\x00\x01\xf0\x00\x01\xf0'\
b'\x00\x01\xf0\x00\x01\xf0\x00\x1f\xff\x00\x1f\xff\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x07\xf8\x00\x1f\xfe\x00\x3c\x3f\x00\x78\x1f'\
b'\x80\x7c\x0f\x80\x7e\x0f\x80\x7e\x0f\x80\x7e\x0f\x80\x3e\x1f\x80'\
b'\x1c\x1f\x00\x00\x3e\x00\x00\x7c\x00\x00\x78\x00\x00\xf0\x00\x01'\
b'\xe0\x00\x01\xc0\xc0\x03\x80\xc0\x07\x00\xc0\x0e\x01\xc0\x1f\xff'\
b'\xc0\x3f\xff\x80\x3f\xff\x80\x7f\xff\x80\x7f\xff\x80\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x07\xf0\x00\x1f\xfc\x00\x3c\x3e\x00\x7c\x1f'\
b'\x00\x7e\x1f\x00\x7e\x1f\x00\x7e\x1f\x00\x3c\x1f\x00\x00\x3e\x00'\
b'\x00\x38\x00\x03\xf0\x00\x03\xe0\x00\x00\x7c\x00\x00\x3f\x00\x00'\
b'\x1f\x00\x00\x1f\x80\x3c\x0f\x80\x7e\x0f\x80\x7e\x0f\x80\x7e\x1f'\
b'\x80\x7c\x1f\x00\x3c\x3f\x00\x1f\xfc\x00\x03\xf0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x00\x04\x00\x00\x0c\x00\x00\x1c\x00\x00\x3c'\
b'\x00\x00\x7c\x00\x00\xfc\x00\x01\xfc\x00\x01\xfc\x00\x03\x7c\x00'\
b'\x06\x7c\x00\x0c\x7c\x00\x1c\x7c\x00\x38\x7c\x00\x70\x7c\x00\xe0'\
b'\x7c\x00\xc0\x7c\x00\xff\xff\x80\xff\xff\x80\x00\x7c\x00\x00\x7c'\
b'\x00\x00\x7c\x00\x00\x7c\x00\x03\xff\x80\x03\xff\x80\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x0f\xff\x80\x1f\xff\x00\x1f\xff\x00\x1f\xfe'\
b'\x00\x1f\xf8\x00\x18\x00\x00\x18\x00\x00\x18\x00\x00\x18\x00\x00'\
b'\x1b\xf0\x00\x1f\xfc\x00\x1c\x3e\x00\x18\x1f\x00\x10\x1f\x00\x00'\
b'\x0f\x80\x00\x0f\x80\x1c\x0f\x80\x3e\x0f\x80\x7e\x0f\x80\x7e\x1f'\
b'\x00\x3c\x1f\x00\x38\x7e\x00\x1f\xf8\x00\x07\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x01\xf8\x00\x07\xfe\x00\x0f\x8f\x00\x1f\x1f'\
b'\x00\x1e\x1f\x00\x3e\x1f\x00\x3c\x0e\x00\x7c\x00\x00\x7c\x00\x00'\
b'\x7c\x00\x00\x7c\xfc\x00\x7f\xff\x00\x7f\xbf\x80\x7e\x0f\x80\x7c'\
b'\x0f\xc0\x7c\x07\xc0\x7c\x07\xc0\x7c\x07\xc0\x7c\x07\xc0\x3e\x0f'\
b'\x80\x3e\x0f\x80\x1f\x1f\x00\x0f\xfe\x00\x03\xf8\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x3f\xff\xc0\x3f\xff\x80\x3f\xff\x80\x3f\xff'\
b'\x00\x3f\xff\x00\x30\x06\x00\x30\x06\x00\x30\x0e\x00\x20\x1c\x00'\
b'\x00\x1c\x00\x00\x3c\x00\x00\x38\x00\x00\x78\x00\x00\x78\x00\x00'\
b'\xf8\x00\x00\xf0\x00\x01\xf0\x00\x01\xf0\x00\x03\xf0\x00\x03\xf0'\
b'\x00\x03\xf0\x00\x03\xf0\x00\x03\xf0\x00\x01\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x03\xf8\x00\x07\xfe\x00\x1e\x1f\x00\x1c\x0f'\
b'\x80\x3c\x07\x80\x3c\x07\x80\x3c\x07\x80\x3e\x07\x80\x3f\x0f\x00'\
b'\x3f\xfe\x00\x1f\xf8\x00\x0f\xfe\x00\x07\xff\x00\x1f\xff\x80\x3c'\
b'\x3f\x80\x7c\x0f\xc0\x78\x07\xc0\x78\x07\xc0\x78\x07\x80\x78\x07'\
b'\x80\x7c\x0f\x00\x3e\x1e\x00\x1f\xf8\x00\x03\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x01\xe0\x00\x0f\xfc\x00\x1f\x3e\x00\x3e\x1f'\
b'\x00\x7e\x0f\x80\x7c\x0f\x80\x7c\x07\xc0\x7c\x07\xc0\x7c\x07\xc0'\
b'\x7e\x0f\xc0\x7e\x1f\xc0\x3f\xb7\xc0\x1f\xe7\xc0\x0f\xc7\xc0\x00'\
b'\x07\xc0\x00\x07\xc0\x38\x07\x80\x7c\x0f\x80\x7e\x0f\x80\x7c\x0f'\
b'\x00\x7c\x1f\x00\x38\x7e\x00\x1f\xf8\x00\x07\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x1e\x00\x3f\x00\x3f\x00\x3f\x00\x3f\x00\x1e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x3f\x00\x3f\x00\x3f\x00'\
b'\x3f\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x07\xe0\x1f\xf8\x38\xfc\x78\x7c\x7c\x7e\x7c\x7e\x7c\x7e'\
b'\x38\x7e\x00\x7c\x00\xfc\x00\xf8\x01\xf0\x01\xc0\x03\x80\x03\x80'\
b'\x03\x00\x03\x00\x00\x00\x00\x00\x07\x80\x0f\xc0\x0f\xc0\x0f\xc0'\
b'\x0f\xc0\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x01\x00\x00\x03\x00\x00\x06\x00\x01\xf6\x00'\
b'\x07\xfc\x00\x1f\x1f\x00\x3e\x1f\x80\x3e\x37\x80\x7c\x27\xc0\x7c'\
b'\x67\xc0\x7c\x47\xc0\x7c\xc7\xc0\x7d\x87\xc0\x7d\x07\xc0\x3f\x0f'\
b'\x80\x3e\x0f\x80\x1f\x1f\x00\x0f\xfc\x00\x0d\xf0\x00\x18\x00\x00'\
b'\x18\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00'

_sparse =\
b'\x20\x00\x08\x00\x25\x00\x10\x00\x2a\x00\x20\x00\x2b\x00\x2c\x00'\
b'\x2c\x00\x38\x00\x2d\x00\x40\x00\x2e\x00\x48\x00\x2f\x00\x50\x00'\
b'\x30\x00\x58\x00\x31\x00\x64\x00\x32\x00\x70\x00\x33\x00\x7c\x00'\
b'\x34\x00\x88\x00\x35\x00\x94\x00\x36\x00\xa0\x00\x37\x00\xac\x00'\
b'\x38\x00\xb8\x00\x39\x00\xc4\x00\x3a\x00\xd0\x00\x3f\x00\xd8\x00'\
b'\xf8\x00\xe0\x00'

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

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 30
    return _mvfont[doff + 2:next_offs], 30, width
 
