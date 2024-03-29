'''
    mPyEZfont_u8g2_timB24_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original timB24.bdf font file was sourced from the U8G2 project:
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
# Font: timB24.bdf Char set:  *+,-./0123456789:
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/timB24.bdf 0 tmp_mPyEZfont_u8g2_timB24_n.py
version = '0.33'

def height():
    return 31

def baseline():
    return 25

def max_width():
    return 19

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
b'\x10\x00\x00\x00\x00\x00\x0f\xc0\x1c\xf0\x38\x78\x38\x7c\x3c\x7c'\
b'\x3c\x7c\x18\x7c\x00\x78\x00\x78\x00\xf0\x00\xe0\x00\xc0\x01\x80'\
b'\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x03\x80\x07\xc0\x07\xc0'\
b'\x07\xc0\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x11\x00\x00\x00\x00\x00\x00\x00\x01\x80\x00\x03\x80\x00\x03'\
b'\x80\x00\x73\x9c\x00\x79\x3c\x00\x3d\x78\x00\x07\xc0\x00\x07\xc0'\
b'\x00\x3d\x78\x00\x79\x3c\x00\x73\x9c\x00\x03\x80\x00\x03\x80\x00'\
b'\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00'\
b'\xe0\x00\x3f\xff\x80\x3f\xff\x80\x3f\xff\x80\x00\xe0\x00\x00\xe0'\
b'\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x1c\x3e\x3e\x3e\x1e\x06\x04\x0c\x18\x30\x60'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x7f\x80\x7f\x80\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x38\x7c\x7c\x7c\x38\x00\x00\x00\x00\x00'\
b'\x00\x09\x00\x01\x80\x01\x80\x01\x00\x03\x00\x03\x00\x03\x00\x06'\
b'\x00\x06\x00\x06\x00\x04\x00\x0c\x00\x0c\x00\x0c\x00\x18\x00\x18'\
b'\x00\x18\x00\x30\x00\x30\x00\x30\x00\x30\x00\x60\x00\x60\x00\x60'\
b'\x00\xc0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x00\x00\x00\x00\x00\x03\xc0\x0f\xf0\x0e\x70\x1c\x38\x3c'\
b'\x38\x3c\x3c\x3c\x3c\x7c\x3e\x7c\x3e\x7c\x3e\x7c\x3e\x7c\x3e\x7c'\
b'\x3e\x7c\x3e\x7c\x3e\x7c\x3e\x3c\x3c\x3c\x3c\x3c\x3c\x1c\x38\x0e'\
b'\x70\x07\xe0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x00\x00\x00\x00\x00\x00\x60\x01\xe0\x07\xe0\x3f\xe0\x03'\
b'\xe0\x03\xe0\x03\xe0\x03\xe0\x03\xe0\x03\xe0\x03\xe0\x03\xe0\x03'\
b'\xe0\x03\xe0\x03\xe0\x03\xe0\x03\xe0\x03\xe0\x03\xe0\x03\xe0\x03'\
b'\xe0\x07\xf0\x3f\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x00\x00\x00\x00\x00\x03\xc0\x0f\xf0\x1f\xf8\x3f\xf8\x30'\
b'\xfc\x60\x7c\x40\x7c\x00\x7c\x00\x78\x00\x78\x00\x78\x00\xf0\x00'\
b'\xe0\x01\xc0\x01\x80\x03\x00\x07\x01\x0e\x03\x1c\x06\x3f\xfe\x7f'\
b'\xfe\xff\xfc\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x00\x00\x00\x00\x00\x03\xe0\x0f\xf8\x1f\xf8\x18\x7c\x30'\
b'\x3c\x20\x3c\x00\x3c\x00\x38\x00\x60\x01\xf0\x07\xf8\x07\xfc\x01'\
b'\xfc\x00\x7e\x00\x3e\x00\x1e\x00\x1e\x00\x1e\x30\x1c\x78\x1c\x7c'\
b'\x38\x3f\xe0\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x00\x00\x00\x00\x00\x00\x38\x00\x78\x00\x78\x00\xf8\x01'\
b'\xf8\x03\x78\x03\x78\x06\x78\x0c\x78\x0c\x78\x18\x78\x30\x78\x30'\
b'\x78\x60\x78\x7f\xfe\x7f\xfe\x7f\xfe\x7f\xfe\x00\x78\x00\x78\x00'\
b'\x78\x00\x78\x00\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x00\x00\x00\x00\x00\x0f\xfc\x0f\xfc\x0f\xfc\x0f\xfc\x18'\
b'\x00\x18\x00\x10\x00\x1f\x00\x3f\xc0\x3f\xf0\x3f\xf8\x3f\xf8\x01'\
b'\xfc\x00\x7c\x00\x3c\x00\x1c\x00\x1c\x00\x1c\x30\x18\x78\x18\x7c'\
b'\x30\x3f\xe0\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x00\x00\x00\x00\x00\x00\x0e\x00\x78\x01\xe0\x03\xc0\x07'\
b'\x80\x0f\x00\x1f\x00\x1e\x00\x3e\x00\x3f\xf0\x7e\xf8\x7c\x7c\x7c'\
b'\x3c\x7c\x3e\x7c\x3e\x7c\x3e\x7c\x3e\x3c\x3e\x3c\x3c\x3c\x3c\x1c'\
b'\x38\x0e\x70\x07\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x00\x00\x00\x00\x00\x1f\xfe\x1f\xfe\x3f\xfe\x3f\xfe\x30'\
b'\x0c\x20\x1c\x20\x1c\x00\x18\x00\x38\x00\x38\x00\x30\x00\x70\x00'\
b'\x70\x00\xe0\x00\xe0\x00\xe0\x01\xc0\x01\xc0\x01\xc0\x03\x80\x03'\
b'\x80\x03\x80\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x00\x00\x00\x00\x00\x07\xf0\x1f\x78\x1e\x3c\x3c\x3c\x3c'\
b'\x1c\x3c\x1c\x3e\x1c\x3f\x38\x1f\xf0\x1f\xc0\x0f\xe0\x07\xf0\x1f'\
b'\xf8\x38\xfc\x38\x7e\x70\x3e\x70\x1e\x70\x1e\x70\x1e\x78\x1c\x3c'\
b'\x3c\x3f\xf8\x0f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x00\x00\x00\x00\x00\x07\xe0\x0e\x70\x1c\x38\x3c\x3c\x3c'\
b'\x3c\x7c\x3c\x7c\x3e\x7c\x3e\x7c\x3e\x7c\x3e\x3c\x3e\x3e\x3e\x1f'\
b'\x7e\x0f\xfc\x00\x7c\x00\x78\x00\xf8\x00\xf0\x01\xe0\x03\xc0\x07'\
b'\x80\x1e\x00\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x0e\x00\x1f\x00\x1f\x00\x1f\x00\x0e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x1f\x00\x1f'\
b'\x00\x1f\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00'

_index =\
b'\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x61\x00\xc0\x00\x1f\x01\x40\x01\x80\x01'\
b'\xa1\x01\xe1\x01\x21\x02\x61\x02\xa1\x02\xe1\x02\x21\x03\x61\x03'\
b'\xa1\x03\xe1\x03\x21\x04\x61\x04\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xa1\x04'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 63 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 31
    return _mvfont[doff + 2:next_offs], 31, width
 
