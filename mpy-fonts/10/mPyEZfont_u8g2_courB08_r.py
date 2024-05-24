'''
    mPyEZfont_u8g2_courB08_r.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original courB08.bdf font file was sourced from the U8G2 project:
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
# Font: courB08.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -l 127 -e 32 ../u8g2/tools/font/bdf/courB08.bdf 0 tmp_mPyEZfont_u8g2_courB08_r.py
version = '0.33'

def height():
    return 10

def baseline():
    return 8

def max_width():
    return 7

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 127

_font =\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x60\x60\x60\x60\x00\x60\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x50\x50\x50\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x50\x50\xf8\x50\x50\xf8\x50\x50\x00\x00\x00\x00\x00'\
b'\x06\x00\x20\x78\xc8\xf0\x78\x18\xd8\xf0\x20\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\xe0\xa8\xf0\x20\x78\xa8\x38\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x38\x60\x30\x7c\xd8\x7c\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x20\x20\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x10\x20\x60\x60\x60\x60\x20\x10\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x40\x20\x30\x30\x30\x30\x20\x40\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x20\xf0\x60\x90\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x20\x20\xf8\x20\x20\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x30\x20\x40\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x08\x08\x10\x10\x20\x20\x40\x40\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\xd8\xd8\xd8\xd8\xd8\x70\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x30\xf0\x30\x30\x30\x30\xfc\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\xd8\x18\x30\x60\xd8\xf8\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\xd8\x18\x70\x18\xd8\x70\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x18\x38\x58\xd8\xfc\x18\x18\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\xf8\xc0\xf0\xd8\x18\x98\xf0\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\xd8\xc0\xf0\xd8\xd8\x70\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\xf8\xd8\x18\x30\x30\x60\x60\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\xd8\xd8\x70\xd8\xd8\x70\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\xd8\xd8\x78\x18\xd8\x70\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x60\x00\x00\x60\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x60\x00\x00\x60\x40\x80\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x30\x60\xc0\x60\x30\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\xf0\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x60\x30\x18\x30\x60\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x70\x98\x30\x60\x00\x60\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\xc8\x98\xa8\xa8\x9c\xc0\x70\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x78\x38\x28\x7c\x6c\xee\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xf8\x6c\x78\x6c\x6c\xf8\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x78\xd8\xc0\xc0\xd8\x70\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xf8\x6c\x6c\x6c\x6c\xf8\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xfc\x60\x78\x60\x6c\xfc\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xfc\x60\x78\x60\x60\xf0\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x70\xd8\xc0\xf8\xd8\x78\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xee\x6c\x7c\x6c\x6c\xee\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\xf0\x60\x60\x60\x60\xf0\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x3c\x18\x18\xd8\xd8\x70\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xec\x68\x70\x78\x6c\xf6\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xf0\x60\x60\x60\x6c\xfc\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xc4\x6c\x6c\x7c\x54\xd4\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xee\x74\x74\x6c\x6c\xe4\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x70\xd8\xd8\xd8\xd8\x70\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xf8\x6c\x6c\x78\x60\xf0\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x70\xd8\xd8\xd8\xd8\x70\x18\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xf8\x6c\x6c\x78\x6c\xf6\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x78\xc8\xf0\x38\x98\xf0\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xfc\xb4\x30\x30\x30\x78\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xee\x6c\x6c\x6c\x6c\x38\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xee\x6c\x28\x38\x38\x10\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xd6\x54\x54\x7c\x38\x28\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\xcc\x78\x30\x30\x78\xcc\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\xe6\x66\x3c\x18\x18\x3c\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\xf8\xd8\x30\x60\xd8\xf8\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x60\x60\x60\x60\x60\x60\x70\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x80\x80\x40\x40\x20\x20\x10\x10\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x30\x30\x30\x30\x30\x30\x70\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x20\x70\xd8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x00\x00\x00\x00\x00'\
b'\x06\x00\x20\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x70\xd8\x78\xd8\xfc\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\xe0\x60\x78\x6c\x6c\x6c\xf8\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x70\xd8\xc0\xd8\x70\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x38\x18\x78\xd8\xd8\xd8\x7c\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x70\xd8\xf8\xc0\x78\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x38\x60\xf8\x60\x60\x60\xf8\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x6c\xd8\xd8\xd8\x78\x18\xf0\x00\x00\x00\x00'\
b'\x07\x00\x00\xe0\x60\x78\x6c\x6c\x6c\x6c\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x30\x00\xf0\x30\x30\x30\xfc\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x30\x00\xf0\x30\x30\x30\x30\x30\xe0\x00\x00\x00\x00'\
b'\x07\x00\x00\xe0\x60\x6c\x78\x70\x78\x6e\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\xf0\x30\x30\x30\x30\x30\xfc\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xf8\x7c\x54\x54\x54\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xd8\x6c\x6c\x6c\x6c\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x70\xd8\xd8\xd8\x70\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xf8\x6c\x6c\x6c\x78\x60\xf0\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x6c\xd8\xd8\xd8\x78\x18\x3c\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\xdc\x74\x60\x60\xf0\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x78\xe0\x78\x1c\xf8\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x60\x60\xf8\x60\x60\x6c\x38\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xec\x6c\x6c\x6c\x3e\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xec\x6c\x38\x38\x10\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xd6\x54\x7c\x3c\x28\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\xec\x78\x30\x78\xdc\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xee\x6c\x6c\x28\x38\x30\xe0\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\xf8\xb0\x60\xd8\xf8\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x18\x30\x30\x60\x30\x30\x30\x18\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x20\x20\x20\x20\x20\x20\x20\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\xc0\x60\x60\x30\x60\x60\x60\xc0\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x68\xb0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00'

_sparse =\
b'\x20\x00\x02\x00\x21\x00\x04\x00\x22\x00\x06\x00\x23\x00\x08\x00'\
b'\x24\x00\x0a\x00\x25\x00\x0c\x00\x26\x00\x0e\x00\x27\x00\x10\x00'\
b'\x28\x00\x12\x00\x29\x00\x14\x00\x2a\x00\x16\x00\x2b\x00\x18\x00'\
b'\x2c\x00\x1a\x00\x2d\x00\x1c\x00\x2e\x00\x1e\x00\x2f\x00\x20\x00'\
b'\x30\x00\x22\x00\x31\x00\x24\x00\x32\x00\x26\x00\x33\x00\x28\x00'\
b'\x34\x00\x2a\x00\x35\x00\x2c\x00\x36\x00\x2e\x00\x37\x00\x30\x00'\
b'\x38\x00\x32\x00\x39\x00\x34\x00\x3a\x00\x36\x00\x3b\x00\x38\x00'\
b'\x3c\x00\x3a\x00\x3d\x00\x3c\x00\x3e\x00\x3e\x00\x3f\x00\x40\x00'\
b'\x40\x00\x42\x00\x41\x00\x44\x00\x42\x00\x46\x00\x43\x00\x48\x00'\
b'\x44\x00\x4a\x00\x45\x00\x4c\x00\x46\x00\x4e\x00\x47\x00\x50\x00'\
b'\x48\x00\x52\x00\x49\x00\x54\x00\x4a\x00\x56\x00\x4b\x00\x58\x00'\
b'\x4c\x00\x5a\x00\x4d\x00\x5c\x00\x4e\x00\x5e\x00\x4f\x00\x60\x00'\
b'\x50\x00\x62\x00\x51\x00\x64\x00\x52\x00\x66\x00\x53\x00\x68\x00'\
b'\x54\x00\x6a\x00\x55\x00\x6c\x00\x56\x00\x6e\x00\x57\x00\x70\x00'\
b'\x58\x00\x72\x00\x59\x00\x74\x00\x5a\x00\x76\x00\x5b\x00\x78\x00'\
b'\x5c\x00\x7a\x00\x5d\x00\x7c\x00\x5e\x00\x7e\x00\x5f\x00\x80\x00'\
b'\x60\x00\x82\x00\x61\x00\x84\x00\x62\x00\x86\x00\x63\x00\x88\x00'\
b'\x64\x00\x8a\x00\x65\x00\x8c\x00\x66\x00\x8e\x00\x67\x00\x90\x00'\
b'\x68\x00\x92\x00\x69\x00\x94\x00\x6a\x00\x96\x00\x6b\x00\x98\x00'\
b'\x6c\x00\x9a\x00\x6d\x00\x9c\x00\x6e\x00\x9e\x00\x6f\x00\xa0\x00'\
b'\x70\x00\xa2\x00\x71\x00\xa4\x00\x72\x00\xa6\x00\x73\x00\xa8\x00'\
b'\x74\x00\xaa\x00\x75\x00\xac\x00\x76\x00\xae\x00\x77\x00\xb0\x00'\
b'\x78\x00\xb2\x00\x79\x00\xb4\x00\x7a\x00\xb6\x00\x7b\x00\xb8\x00'\
b'\x7c\x00\xba\x00\x7d\x00\xbc\x00\x7e\x00\xbe\x00\x7f\x00\xc0\x00'\

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

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 10
    return _mvfont[doff + 2:next_offs], 10, width
 
