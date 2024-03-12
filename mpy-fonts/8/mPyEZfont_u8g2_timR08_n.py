'''
    mPyEZfont_u8g2_timR08_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original timR08.bdf font file was sourced from the U8G2 project:
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
# Font: timR08.bdf Char set:  *+,-./0123456789:
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/timR08.bdf 0 tmp_mPyEZfont_u8g2_timR08_n.py
version = '0.33'

def height():
    return 8

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
b'\x04\x00\xe0\xa0\x20\x40\x40\x00\x40\x00\x02\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x05\x00\x50\x20\x50\x00\x00\x00\x00\x00\x06\x00'\
b'\x00\x00\x20\x20\xf8\x20\x20\x00\x03\x00\x00\x00\x00\x00\x00\x00'\
b'\xc0\x40\x04\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x03\x00\x00\x00'\
b'\x00\x00\x00\x00\x40\x00\x03\x00\x20\x20\x40\x40\x40\x80\x80\x00'\
b'\x05\x00\x60\x90\x90\x90\x90\x90\x60\x00\x05\x00\x20\x60\x20\x20'\
b'\x20\x20\x70\x00\x05\x00\x60\x90\x10\x20\x20\x40\xf0\x00\x05\x00'\
b'\x60\x90\x10\x60\x10\x10\xe0\x00\x05\x00\x10\x30\x50\x90\xf8\x10'\
b'\x10\x00\x05\x00\x70\x40\xe0\x10\x10\x10\xe0\x00\x05\x00\x30\x40'\
b'\xe0\x90\x90\x90\x60\x00\x05\x00\xf0\x90\x20\x20\x40\x40\x40\x00'\
b'\x05\x00\x60\x90\x90\x60\x90\x90\x60\x00\x05\x00\x60\x90\x90\x90'\
b'\x70\x20\xc0\x00\x03\x00\x00\x00\x40\x00\x00\x00\x40\x00'

_index =\
b'\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x14\x00\x1e\x00\x28\x00\x32\x00\x3c\x00'\
b'\x46\x00\x50\x00\x5a\x00\x64\x00\x6e\x00\x78\x00\x82\x00\x8c\x00'\
b'\x96\x00\xa0\x00\xaa\x00\xb4\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xbe\x00'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 63 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 8
    return _mvfont[doff + 2:next_offs], 8, width
 
