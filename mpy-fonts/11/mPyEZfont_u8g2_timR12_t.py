'''
    mPyEZfont_u8g2_timR12_t.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original timR12.bdf font file was sourced from the U8G2 project:
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
# Font: timR12.bdf Char set:  +-.0123456789:
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./t-char.set -e 32 ../u8g2/tools/font/bdf/timR12.bdf 0 tmp_mPyEZfont_u8g2_timR12_t.py
version = '0.33'

def height():
    return 11

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
    return 58

_font =\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00'\
b'\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x00\x04'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x40\x08\x00\x38\x44'\
b'\x44\x82\x82\x82\x82\x82\x44\x44\x38\x08\x00\x10\x30\x50\x10\x10'\
b'\x10\x10\x10\x10\x10\x38\x08\x00\x38\x44\x82\x02\x02\x04\x08\x10'\
b'\x20\x42\xfc\x08\x00\x38\x44\x84\x08\x10\x38\x04\x02\x02\xc4\x78'\
b'\x09\x00\x02\x00\x06\x00\x0a\x00\x0a\x00\x12\x00\x22\x00\x22\x00'\
b'\x42\x00\xff\x00\x02\x00\x02\x00\x08\x00\x3e\x20\x20\x40\x78\x04'\
b'\x02\x02\x02\x8c\x70\x08\x00\x0e\x30\x40\x40\x98\xe4\x82\x82\x82'\
b'\x44\x38\x08\x00\xfe\x82\x84\x04\x08\x08\x10\x10\x10\x20\x20\x08'\
b'\x00\x30\x48\x84\x84\x48\x30\x48\x84\x84\x48\x30\x08\x00\x38\x44'\
b'\x82\x82\x82\x46\x3a\x04\x04\x18\xe0\x04\x00\x00\x00\x00\x40\x40'\
b'\x00\x00\x00\x00\x40\x40'

_index =\
b'\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00\x32\x00\x3f\x00'\
b'\x00\x00\x4c\x00\x59\x00\x66\x00\x73\x00\x80\x00\x98\x00\xa5\x00'\
b'\xb2\x00\xbf\x00\xcc\x00\xd9\x00\xe6\x00'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 58 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 11
    return _mvfont[doff + 2:next_offs], 11, width
 
