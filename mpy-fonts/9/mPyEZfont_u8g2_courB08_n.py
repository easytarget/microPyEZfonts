'''
    mPyEZfont_u8g2_courB08_n.py : generated as part of the microPyEZfonts repository
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
# Font: courB08.bdf Char set:  *+,-./0123456789:
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/courB08.bdf 0 tmp_mPyEZfont_u8g2_courB08_n.py
version = '0.33'

def height():
    return 9

def baseline():
    return 7

def max_width():
    return 6

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
b'\x06\x00\x00\x70\x98\x30\x60\x00\x60\x00\x00\x06\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x06\x00\x20\xf0\x60\x90\x00\x00\x00\x00'\
b'\x00\x06\x00\x00\x20\x20\xf8\x20\x20\x00\x00\x00\x06\x00\x00\x00'\
b'\x00\x00\x00\x00\x30\x20\x40\x06\x00\x00\x00\x00\xf8\x00\x00\x00'\
b'\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x60\x00\x00\x06\x00\x08'\
b'\x08\x10\x10\x20\x20\x40\x40\x00\x06\x00\x70\xd8\xd8\xd8\xd8\xd8'\
b'\x70\x00\x00\x06\x00\x30\xf0\x30\x30\x30\x30\xfc\x00\x00\x06\x00'\
b'\x70\xd8\x18\x30\x60\xd8\xf8\x00\x00\x06\x00\x70\xd8\x18\x70\x18'\
b'\xd8\x70\x00\x00\x06\x00\x18\x38\x58\xd8\xfc\x18\x18\x00\x00\x06'\
b'\x00\xf8\xc0\xf0\xd8\x18\x98\xf0\x00\x00\x06\x00\x70\xd8\xc0\xf0'\
b'\xd8\xd8\x70\x00\x00\x06\x00\xf8\xd8\x18\x30\x30\x60\x60\x00\x00'\
b'\x06\x00\x70\xd8\xd8\x70\xd8\xd8\x70\x00\x00\x06\x00\x70\xd8\xd8'\
b'\x78\x18\xd8\x70\x00\x00\x06\x00\x00\x00\x00\x60\x00\x00\x60\x00'\
b'\x00'

_index =\
b'\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x16\x00\x21\x00\x2c\x00\x37\x00\x42\x00'\
b'\x4d\x00\x58\x00\x63\x00\x6e\x00\x79\x00\x84\x00\x8f\x00\x9a\x00'\
b'\xa5\x00\xb0\x00\xbb\x00\xc6\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xd1\x00'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 63 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 9
    return _mvfont[doff + 2:next_offs], 9, width
 
