'''
    mPyEZfont_u8g2_ncenR10_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenR10.bdf font file was sourced from the U8G2 project:
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
# Font: ncenR10.bdf Char set:  *+,-./0123456789:
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/ncenR10.bdf 0 tmp_mPyEZfont_u8g2_ncenR10_n.py
version = '0.33'

def height():
    return 13

def baseline():
    return 11

def max_width():
    return 9

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 63

_font =\
b'\x06\x00\x70\x98\x88\x08\x10\x20\x20\x20\x00\x20\x20\x00\x00\x04'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'\
b'\x10\x54\x38\x54\x10\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08'\
b'\x00\x08\x00\x08\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\xc0\x40\x40\x80\x05\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xf0\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x40\x40\x00\x00\x04\x00\x10\x10\x10\x20\x20\x20\x40\x40'\
b'\x40\x80\x80\x00\x00\x08\x00\x3c\x66\x42\x42\x42\x42\x42\x42\x42'\
b'\x66\x3c\x00\x00\x08\x00\x10\x70\x10\x10\x10\x10\x10\x10\x10\x10'\
b'\x7c\x00\x00\x08\x00\x3c\x46\x62\x02\x02\x04\x08\x10\x22\x42\x7e'\
b'\x00\x00\x08\x00\x3c\x46\x62\x02\x04\x1c\x06\x02\x62\x46\x3c\x00'\
b'\x00\x08\x00\x0c\x1c\x14\x24\x44\x44\x84\xfe\x04\x04\x0e\x00\x00'\
b'\x08\x00\x7e\x40\x40\x5c\x66\x42\x02\x02\x62\x46\x3c\x00\x00\x08'\
b'\x00\x1c\x22\x46\x40\x5c\x66\x42\x42\x42\x66\x3c\x00\x00\x08\x00'\
b'\x7e\x42\x44\x04\x08\x08\x08\x10\x10\x10\x10\x00\x00\x08\x00\x3c'\
b'\x66\x42\x62\x34\x3c\x46\x42\x42\x66\x3c\x00\x00\x08\x00\x3c\x66'\
b'\x42\x42\x42\x66\x3a\x02\x62\x44\x38\x00\x00\x04\x00\x00\x00\x00'\
b'\x00\x40\x40\x00\x00\x00\x40\x40\x00\x00'

_index =\
b'\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x1e\x00\x2d\x00\x49\x00\x58\x00\x67\x00'\
b'\x76\x00\x85\x00\x94\x00\xa3\x00\xb2\x00\xc1\x00\xd0\x00\xdf\x00'\
b'\xee\x00\xfd\x00\x0c\x01\x1b\x01\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x2a\x01'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 63 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 13
    return _mvfont[doff + 2:next_offs], 13, width
 
