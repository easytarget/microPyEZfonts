'''
    mPyEZfont_u8g2_helvR08_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original helvR08.bdf font file was sourced from the U8G2 project:
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
# Font: helvR08.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/u-char.set u8g2/tools/font/bdf/helvR08.bdf 0 tmp_mPyEZfont_u8g2_helvR08_u.py
version = '0.33'

def height():
    return 11

def baseline():
    return 9

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
    return 95

_font =\
b'\x06\x00\x00\x30\x48\x08\x10\x20\x20\x00\x20\x00\x00\x03\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x40\x40\x40'\
b'\x40\x40\x40\x00\x40\x00\x00\x04\x00\x00\x50\x50\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x06\x00\x00\x00\x28\x28\x7c\x28\xf8\x50\x50\x00'\
b'\x00\x06\x00\x20\x70\xa8\xa0\x70\x28\x28\xa8\x70\x20\x00\x09\x00'\
b'\x00\x00\x64\x00\x94\x00\x68\x00\x08\x00\x10\x00\x16\x00\x29\x00'\
b'\x26\x00\x00\x00\x00\x00\x08\x00\x00\x30\x48\x48\x30\x4a\x44\x4c'\
b'\x32\x00\x00\x02\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x20\x40\x40\x80\x80\x80\x80\x40\x40\x20\x04\x00\x00'\
b'\x40\x20\x20\x10\x10\x10\x10\x20\x20\x40\x04\x00\x00\xa0\x40\xa0'\
b'\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x20\x20\xf8\x20'\
b'\x20\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x40'\
b'\x80\x04\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x03\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x03\x00\x00\x20\x20'\
b'\x40\x40\x40\x40\x80\x80\x00\x00\x06\x00\x00\x70\x88\x88\x88\x88'\
b'\x88\x88\x70\x00\x00\x06\x00\x00\x20\x60\x20\x20\x20\x20\x20\x20'\
b'\x00\x00\x06\x00\x00\x70\x88\x08\x08\x30\x40\x80\xf8\x00\x00\x06'\
b'\x00\x00\x70\x88\x08\x30\x08\x08\x88\x70\x00\x00\x06\x00\x00\x10'\
b'\x30\x50\x50\x90\xf8\x10\x10\x00\x00\x06\x00\x00\x78\x40\x40\x70'\
b'\x08\x08\x88\x70\x00\x00\x06\x00\x00\x70\x88\x80\xf0\x88\x88\x88'\
b'\x70\x00\x00\x06\x00\x00\xf8\x08\x10\x20\x20\x40\x40\x40\x00\x00'\
b'\x06\x00\x00\x70\x88\x88\x70\x88\x88\x88\x70\x00\x00\x06\x00\x00'\
b'\x70\x88\x88\x88\x78\x08\x88\x70\x00\x00\x03\x00\x00\x00\x00\x40'\
b'\x00\x00\x00\x00\x40\x00\x00\x03\x00\x00\x00\x00\x40\x00\x00\x00'\
b'\x00\x40\x40\x80\x06\x00\x00\x00\x00\x10\x20\x40\x20\x10\x00\x00'\
b'\x00\x05\x00\x00\x00\x00\x00\xf0\x00\xf0\x00\x00\x00\x00\x06\x00'\
b'\x00\x00\x00\x40\x20\x10\x20\x40\x00\x00\x00\x06\x00\x00\x30\x48'\
b'\x08\x10\x20\x20\x00\x20\x00\x00\x0b\x00\x00\x00\x1f\x00\x20\x80'\
b'\x4d\x40\x92\x40\xa2\x40\xa4\x80\x9b\x00\x40\x00\x3e\x00\x00\x00'\
b'\x07\x00\x00\x10\x10\x28\x28\x44\x7c\x82\x82\x00\x00\x07\x00\x00'\
b'\x78\x44\x44\x78\x44\x44\x44\x78\x00\x00\x08\x00\x00\x3c\x42\x40'\
b'\x40\x40\x40\x42\x3c\x00\x00\x08\x00\x00\x78\x44\x42\x42\x42\x42'\
b'\x44\x78\x00\x00\x07\x00\x00\x7c\x40\x40\x7c\x40\x40\x40\x7c\x00'\
b'\x00\x06\x00\x00\x7c\x40\x40\x78\x40\x40\x40\x40\x00\x00\x08\x00'\
b'\x00\x3c\x42\x40\x40\x46\x42\x42\x3e\x00\x00\x08\x00\x00\x42\x42'\
b'\x42\x7e\x42\x42\x42\x42\x00\x00\x03\x00\x00\x40\x40\x40\x40\x40'\
b'\x40\x40\x40\x00\x00\x05\x00\x00\x10\x10\x10\x10\x10\x10\x90\x60'\
b'\x00\x00\x07\x00\x00\x44\x48\x50\x70\x48\x48\x44\x44\x00\x00\x06'\
b'\x00\x00\x40\x40\x40\x40\x40\x40\x40\x78\x00\x00\x09\x00\x00\x00'\
b'\x41\x00\x63\x00\x63\x00\x55\x00\x55\x00\x49\x00\x49\x00\x49\x00'\
b'\x00\x00\x00\x00\x08\x00\x00\x62\x62\x52\x52\x4a\x4a\x46\x46\x00'\
b'\x00\x08\x00\x00\x3c\x42\x42\x42\x42\x42\x42\x3c\x00\x00\x07\x00'\
b'\x00\x78\x44\x44\x78\x40\x40\x40\x40\x00\x00\x08\x00\x00\x3c\x42'\
b'\x42\x42\x42\x4a\x46\x3e\x01\x00\x07\x00\x00\x78\x44\x44\x78\x44'\
b'\x44\x44\x44\x00\x00\x07\x00\x00\x38\x44\x40\x38\x04\x44\x44\x38'\
b'\x00\x00\x05\x00\x00\xf8\x20\x20\x20\x20\x20\x20\x20\x00\x00\x08'\
b'\x00\x00\x42\x42\x42\x42\x42\x42\x42\x3c\x00\x00\x07\x00\x00\x82'\
b'\x82\x44\x44\x44\x28\x28\x10\x00\x00\x09\x00\x00\x00\x88\x80\x88'\
b'\x80\x49\x00\x49\x00\x55\x00\x22\x00\x22\x00\x22\x00\x00\x00\x00'\
b'\x00\x07\x00\x00\x44\x44\x28\x10\x28\x28\x44\x44\x00\x00\x07\x00'\
b'\x00\x82\x44\x44\x28\x28\x10\x10\x10\x00\x00\x07\x00\x00\x7c\x04'\
b'\x08\x10\x10\x20\x40\x7c\x00\x00\x03\x00\x00\x60\x40\x40\x40\x40'\
b'\x40\x40\x40\x40\x60\x03\x00\x00\x80\x80\x40\x40\x40\x40\x20\x20'\
b'\x00\x00\x03\x00\x00\xc0\x40\x40\x40\x40\x40\x40\x40\x40\xc0\x06'\
b'\x00\x00\x20\x20\x50\x50\x88\x00\x00\x00\x00\x00\x06\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\xfc\x00'

_index =\
b'\x00\x00\x0d\x00\x1a\x00\x27\x00\x34\x00\x41\x00\x4e\x00\x66\x00'\
b'\x73\x00\x80\x00\x8d\x00\x9a\x00\xa7\x00\xb4\x00\xc1\x00\xce\x00'\
b'\xdb\x00\xe8\x00\xf5\x00\x02\x01\x0f\x01\x1c\x01\x29\x01\x36\x01'\
b'\x43\x01\x50\x01\x5d\x01\x6a\x01\x77\x01\x84\x01\x91\x01\x9e\x01'\
b'\xab\x01\xb8\x01\xd0\x01\xdd\x01\xea\x01\xf7\x01\x04\x02\x11\x02'\
b'\x1e\x02\x2b\x02\x38\x02\x45\x02\x52\x02\x5f\x02\x6c\x02\x84\x02'\
b'\x91\x02\x9e\x02\xab\x02\xb8\x02\xc5\x02\xd2\x02\xdf\x02\xec\x02'\
b'\xf9\x02\x11\x03\x1e\x03\x2b\x03\x38\x03\x45\x03\x52\x03\x5f\x03'\
b'\x6c\x03\x79\x03'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 11
    return _mvfont[doff + 2:next_offs], 11, width
 
