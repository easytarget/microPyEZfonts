'''
    mPyEZfont_u8g2_timB18_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original timB18.bdf font file was sourced from the U8G2 project:
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
# Font: timB18.bdf Char set:  *+,-./0123456789:
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/timB18.bdf 0 tmp_mPyEZfont_u8g2_timB18_n.py
version = '0.33'

def height():
    return 22

def baseline():
    return 17

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
    return 63

_font =\
b'\x0c\x00\x1f\x00\x37\x80\x73\xc0\x73\xc0\x23\xc0\x03\xc0\x07\x80'\
b'\x07\x00\x0e\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x0c\x00\x1e\x00'\
b'\x1e\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0d\x00\x06\x00\x06\x00\x26\x40\x76\xe0'\
b'\x3f\xc0\x0f\x00\x3f\xc0\x76\xe0\x26\x40\x06\x00\x06\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x7f\xf8\x7f\xf8\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x30\x78\x78\x38\x18\x30\x30\x60\x40\x08\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x7e\x7e\x7e\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x30\x78\x78\x30\x00\x00\x00\x00\x00\x07\x00\x06\x06\x04\x0c'\
b'\x0c\x08\x18\x18\x10\x30\x30\x20\x60\x60\x40\xc0\xc0\x00\x00\x00'\
b'\x00\x00\x0c\x00\x0e\x00\x3b\x80\x31\x80\x71\xc0\x71\xc0\xf1\xe0'\
b'\xf1\xe0\xf1\xe0\xf1\xe0\xf1\xe0\xf1\xe0\x71\xc0\x71\xc0\x71\xc0'\
b'\x31\x80\x3b\x80\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x03\x00\x0f\x00\x3f\x00\x07\x00\x07\x00\x07\x00\x07\x00'\
b'\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00'\
b'\x0f\x80\x3f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x0f\x00\x1f\x80\x3f\xc0\x63\xc0\x41\xc0\x01\xc0\x01\xc0\x01\x80'\
b'\x03\x80\x03\x00\x06\x00\x06\x00\x0c\x20\x18\x20\x3f\xe0\x7f\xe0'\
b'\x7f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0f\x00'\
b'\x3f\x80\x63\xc0\x41\xc0\x01\xc0\x03\x80\x07\x00\x1f\x00\x07\xc0'\
b'\x01\xe0\x01\xe0\x00\xe0\x00\xe0\x60\xe0\xf1\xc0\xfb\x80\x7e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x01\x80\x03\x80'\
b'\x07\x80\x07\x80\x0f\x80\x1b\x80\x33\x80\x33\x80\x63\x80\xc3\x80'\
b'\xff\xe0\xff\xe0\xff\xe0\x03\x80\x03\x80\x03\x80\x03\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1f\xe0\x1f\xc0\x3f\xc0'\
b'\x30\x00\x20\x00\x70\x00\x7f\x00\x7f\x80\x7f\xc0\x07\xc0\x01\xc0'\
b'\x00\xc0\x00\xc0\x60\xc0\xf1\x80\xfb\x80\x7e\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x00\xf0\x03\xc0\x0f\x00\x1e\x00'\
b'\x1c\x00\x3c\x00\x3b\x80\x3d\xc0\x78\xe0\x78\xf0\x78\xf0\x78\xf0'\
b'\x78\xf0\x38\xe0\x38\xe0\x1d\xc0\x0f\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x3f\xe0\x7f\xe0\x7f\xc0\xc0\xc0\x81\x80'\
b'\x01\x80\x03\x80\x03\x00\x03\x00\x07\x00\x06\x00\x06\x00\x0e\x00'\
b'\x0e\x00\x0c\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x1f\x00\x3b\x80\x71\xc0\x71\xc0\x71\xc0\x79\x80'\
b'\x3b\x00\x3f\x00\x1f\x80\x37\xc0\x63\xc0\xe1\xe0\xe1\xe0\xe1\xe0'\
b'\xf1\xc0\x7b\x80\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x0e\x00\x3b\x80\x71\xc0\x71\xc0\xf1\xe0\xf1\xe0\xf1\xe0'\
b'\xf1\xe0\x71\xe0\x3b\xc0\x1f\xc0\x03\xc0\x03\x80\x07\x80\x0f\x00'\
b'\x3c\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'\
b'\x00\x00\x00\x00\x00\x18\x3c\x3c\x18\x00\x00\x00\x00\x18\x3c\x3c'\
b'\x18\x00\x00\x00\x00\x00'

_index =\
b'\x00\x00\x2e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x46\x00\x74\x00\xa2\x00\xba\x00\xd2\x00'\
b'\xea\x00\x02\x01\x30\x01\x5e\x01\x8c\x01\xba\x01\xe8\x01\x16\x02'\
b'\x44\x02\x72\x02\xa0\x02\xce\x02\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xe6\x02'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 63 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 22
    return _mvfont[doff + 2:next_offs], 22, width
 
