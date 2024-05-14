'''
    mPyEZfont_u8g2_helvR14_t.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original helvR14.bdf font file was sourced from the U8G2 project:
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
# Font: helvR14.bdf Char set:  +-.0123456789:
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./t-char.set -e 32 ../u8g2/tools/font/bdf/helvR14.bdf 0 tmp_mPyEZfont_u8g2_helvR14_t.py
version = '0.33'

def height():
    return 13

def baseline():
    return 13

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
    return 58

_font =\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80'\
b'\x7f\x80\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x06\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\xf8\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x60\x60\x0a\x00\x1e\x00\x3f\x00\x33\x00'\
b'\x61\x80\x61\x80\x61\x80\x61\x80\x61\x80\x61\x80\x61\x80\x33\x00'\
b'\x3f\x00\x1e\x00\x0a\x00\x06\x00\x3e\x00\x3e\x00\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x0a\x00\x1e\x00\x7f\x00\x61\x80\x01\x80\x03\x80\x07\x00\x0e\x00'\
b'\x1c\x00\x38\x00\x70\x00\x60\x00\x7f\x80\x7f\x80\x0a\x00\x1f\x00'\
b'\x3f\x80\x61\x80\x61\x80\x03\x00\x0e\x00\x0f\x00\x03\x80\x01\x80'\
b'\x61\x80\x63\x80\x3f\x00\x1e\x00\x0a\x00\x03\x00\x07\x00\x0f\x00'\
b'\x1b\x00\x33\x00\x33\x00\x63\x00\xc3\x00\xff\x80\xff\x80\x03\x00'\
b'\x03\x00\x03\x00\x0a\x00\x7f\x00\x7f\x00\x60\x00\x60\x00\x7e\x00'\
b'\x7f\x00\x63\x80\x01\x80\x01\x80\x61\x80\x63\x80\x7f\x00\x3e\x00'\
b'\x0a\x00\x1e\x00\x3f\x80\x31\x80\x60\x00\x60\x00\x6e\x00\x7f\x00'\
b'\x61\x80\x61\x80\x61\x80\x71\x80\x3f\x00\x1e\x00\x0a\x00\x7f\x80'\
b'\x7f\x80\x01\x80\x03\x00\x06\x00\x06\x00\x0c\x00\x0c\x00\x18\x00'\
b'\x18\x00\x30\x00\x30\x00\x30\x00\x0a\x00\x1e\x00\x3f\x00\x73\x80'\
b'\x61\x80\x61\x80\x33\x00\x3f\x00\x73\x80\x61\x80\x61\x80\x73\x80'\
b'\x3f\x00\x1e\x00\x0a\x00\x1e\x00\x3f\x00\x63\x80\x61\x80\x61\x80'\
b'\x61\x80\x3f\x80\x1d\x80\x01\x80\x01\x80\x63\x00\x7f\x00\x3e\x00'\
b'\x05\x00\x00\x00\x00\x60\x60\x00\x00\x00\x00\x00\x00\x60\x60'

_index =\
b'\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x3a\x00\x49\x00'\
b'\x00\x00\x58\x00\x74\x00\x90\x00\xac\x00\xc8\x00\xe4\x00\x00\x01'\
b'\x1c\x01\x38\x01\x54\x01\x70\x01\x7f\x01'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 58 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 13
    return _mvfont[doff + 2:next_offs], 13, width
 
