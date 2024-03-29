'''
    mPyEZfont_u8g2_ncenB12_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenB12.bdf font file was sourced from the U8G2 project:
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
# Font: ncenB12.bdf Char set:  *+,-./0123456789:
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/ncenB12.bdf 0 tmp_mPyEZfont_u8g2_ncenB12_n.py
version = '0.33'

def height():
    return 15

def baseline():
    return 12

def max_width():
    return 10

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
b'\x08\x00\x3c\x66\xf7\x67\x0e\x0c\x10\x00\x10\x38\x38\x10\x00\x00'\
b'\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x10\x54\xd6\x38\xd6\x54\x10\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c'\
b'\x00\x0c\x00\x7f\x80\x7f\x80\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00'\
b'\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\xf0'\
b'\x70\x20\x60\x80\x05\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\x00'\
b'\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x60\xf0\x60\x00\x00\x00\x05\x00\x08\x08\x10\x10\x10\x20\x20\x40'\
b'\x40\x40\x80\x80\x00\x00\x00\x0a\x00\x1c\x00\x36\x00\x63\x00\x63'\
b'\x00\xe3\x80\xe3\x80\xe3\x80\xe3\x80\x63\x00\x63\x00\x36\x00\x1c'\
b'\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x0c\x00\x7c\x00\x1c\x00\x1c'\
b'\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x7f'\
b'\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x1e\x00\x23\x00\x73\x80\x73'\
b'\x80\x23\x80\x07\x00\x06\x00\x0c\x00\x18\x80\x30\x80\x7f\x80\x7f'\
b'\x80\x00\x00\x00\x00\x00\x00\x0a\x00\x3e\x00\x67\x00\x73\x00\x23'\
b'\x00\x06\x00\x1f\x00\x07\x00\x03\x80\x63\x80\xf3\x80\x67\x00\x3e'\
b'\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x02\x00\x06\x00\x0e\x00\x1e'\
b'\x00\x2e\x00\x2e\x00\x4e\x00\x8e\x00\xff\x80\x0e\x00\x0e\x00\x3f'\
b'\x80\x00\x00\x00\x00\x00\x00\x0a\x00\x3f\x80\x3f\x00\x20\x00\x20'\
b'\x00\x3e\x00\x27\x00\x03\x80\x23\x80\x73\x80\x73\x80\x67\x00\x3e'\
b'\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x1f\x00\x33\x80\x67\x80\x63'\
b'\x00\xe0\x00\xee\x00\xf7\x00\xe3\x80\xe3\x80\x63\x80\x77\x00\x1e'\
b'\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x7f\x80\x7f\x00\x43\x00\x43'\
b'\x00\x42\x00\x06\x00\x06\x00\x0c\x00\x0c\x00\x1c\x00\x1c\x00\x08'\
b'\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x1e\x00\x33\x00\x73\x80\x73'\
b'\x80\x33\x00\x1e\x00\x33\x00\x73\x80\x73\x80\x73\x80\x33\x00\x1e'\
b'\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x3c\x00\x77\x00\xe3\x00\xe3'\
b'\x80\xe3\x80\x77\x80\x3b\x80\x03\x80\x63\x00\xf3\x00\xe6\x00\x7c'\
b'\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x60\xf0\x60'\
b'\x00\x00\x60\xf0\x60\x00\x00\x00'

_index =\
b'\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x22\x00\x33\x00\x53\x00\x64\x00\x75\x00'\
b'\x86\x00\x97\x00\xb7\x00\xd7\x00\xf7\x00\x17\x01\x37\x01\x57\x01'\
b'\x77\x01\x97\x01\xb7\x01\xd7\x01\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xe8\x01'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 63 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 15
    return _mvfont[doff + 2:next_offs], 15, width
 
