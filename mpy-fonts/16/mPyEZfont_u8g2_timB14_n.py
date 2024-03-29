'''
    mPyEZfont_u8g2_timB14_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original timB14.bdf font file was sourced from the U8G2 project:
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
# Font: timB14.bdf Char set:  *+,-./0123456789:
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/timB14.bdf 0 tmp_mPyEZfont_u8g2_timB14_n.py
version = '0.33'

def height():
    return 16

def baseline():
    return 13

def max_width():
    return 11

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
b'\x09\x00\x3e\x00\x67\x00\x77\x00\x77\x00\x27\x00\x06\x00\x0c\x00'\
b'\x08\x00\x08\x00\x00\x00\x1c\x00\x1c\x00\x1c\x00\x00\x00\x00\x00'\
b'\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x18\x00\x18\x00\xdb\x00\xff\x00\x3c\x00'\
b'\xff\x00\xdb\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\xff\xc0\xff\xc0\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x70\x70\x70\x30\x60\xc0\x06\x00\x00\x00\x00\x00'\
b'\x00\x00\xf8\xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x70\x70\x70\x00\x00\x00\x06\x00'\
b'\x18\x18\x18\x30\x30\x30\x20\x60\x60\x60\xc0\xc0\xc0\x00\x00\x00'\
b'\x09\x00\x3c\x00\x66\x00\x67\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00'\
b'\xe7\x00\xe7\x00\xe7\x00\x66\x00\x66\x00\x3c\x00\x00\x00\x00\x00'\
b'\x00\x00\x09\x00\x1c\x00\x3c\x00\xfc\x00\x1c\x00\x1c\x00\x1c\x00'\
b'\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x7f\x00\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x3c\x00\x7e\x00\xcf\x00\x87\x00\x07\x00'\
b'\x07\x00\x06\x00\x0c\x00\x18\x00\x31\x00\x63\x00\xff\x00\xff\x00'\
b'\x00\x00\x00\x00\x00\x00\x09\x00\x3c\x00\x7e\x00\x8f\x00\x07\x00'\
b'\x0e\x00\x1c\x00\x3e\x00\x0f\x00\x07\x80\x03\x80\xc3\x00\xe6\x00'\
b'\x7c\x00\x00\x00\x00\x00\x00\x00\x09\x00\x0e\x00\x1e\x00\x1e\x00'\
b'\x2e\x00\x2e\x00\x4e\x00\xce\x00\x8e\x00\xff\x00\xff\x00\x0e\x00'\
b'\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x09\x00\x3f\x00\x3f\x00'\
b'\x3e\x00\x40\x00\x78\x00\x7e\x00\x3f\x00\x07\x80\x03\x80\x03\x80'\
b'\xc3\x00\xe6\x00\xfc\x00\x00\x00\x00\x00\x00\x00\x09\x00\x07\x00'\
b'\x1c\x00\x38\x00\x70\x00\x60\x00\xfc\x00\xe6\x00\xe7\x00\xe7\x00'\
b'\xe7\x00\xe7\x00\x66\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x09\x00'\
b'\xff\x00\xff\x00\xfe\x00\x86\x00\x0c\x00\x0c\x00\x0c\x00\x18\x00'\
b'\x18\x00\x38\x00\x30\x00\x30\x00\x70\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x3c\x00\x66\x00\xe3\x00\xe3\x00\xf6\x00\x7c\x00\x3c\x00'\
b'\x7e\x00\xcf\x00\xc7\x00\xc3\x00\xe7\x00\x7e\x00\x00\x00\x00\x00'\
b'\x00\x00\x09\x00\x3c\x00\x66\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00'\
b'\x67\x00\x3f\x00\x07\x00\x06\x00\x0e\x00\x3c\x00\xf0\x00\x00\x00'\
b'\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x70\x70\x70\x00\x00\x00'\
b'\x70\x70\x70\x00\x00\x00'

_index =\
b'\x00\x00\x22\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x34\x00\x56\x00\x78\x00\x8a\x00\x9c\x00'\
b'\xae\x00\xc0\x00\xe2\x00\x04\x01\x26\x01\x48\x01\x6a\x01\x8c\x01'\
b'\xae\x01\xd0\x01\xf2\x01\x14\x02\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x26\x02'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 63 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 16
    return _mvfont[doff + 2:next_offs], 16, width
 
