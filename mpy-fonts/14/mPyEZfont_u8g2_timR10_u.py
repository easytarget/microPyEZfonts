'''
    mPyEZfont_u8g2_timR10_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original timR10.bdf font file was sourced from the U8G2 project:
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
# Font: timR10.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -l 95 -e 32 ../u8g2/tools/font/bdf/timR10.bdf 0 tmp_mPyEZfont_u8g2_timR10_u.py
version = '0.33'

def height():
    return 14

def baseline():
    return 11

def max_width():
    return 13

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
b'\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x20\x20\x20\x20\x20\x20\x20\x00\x20\x20\x00\x00\x00'\
b'\x06\x00\x00\x50\x50\x50\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x14\x14\x7e\x28\x28\x28\xfc\x50\x50\x50\x00\x00\x00'\
b'\x07\x00\x10\x3c\x54\x50\x50\x38\x14\x14\x14\x54\x78\x10\x00\x00'\
b'\x0c\x00\x00\x00\x38\xc0\x6f\x80\x49\x00\x4a\x00\x34\x00\x05\x80'\
b'\x0b\x40\x12\x40\x22\x40\x21\x80\x00\x00\x00\x00\x00\x00\x0b\x00'\
b'\x00\x00\x0c\x00\x12\x00\x12\x00\x1c\x00\x09\xc0\x3c\x80\x65\x00'\
b'\x42\x00\x67\x20\x39\xc0\x00\x00\x00\x00\x00\x00\x03\x00\x00\x40'\
b'\x40\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x10'\
b'\x10\x20\x20\x40\x40\x40\x40\x40\x20\x20\x10\x10\x05\x00\x00\x40'\
b'\x40\x20\x20\x10\x10\x10\x10\x10\x20\x20\x40\x40\x07\x00\x00\x10'\
b'\x54\x38\x38\x54\x10\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00'\
b'\x00\x00\x10\x10\x10\xfe\x10\x10\x10\x00\x00\x00\x04\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x60\x20\x40\x00\x04\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00\x00\x00\x04\x00\x00\x10'\
b'\x10\x10\x20\x20\x20\x40\x40\x40\x80\x80\x80\x00\x07\x00\x00\x3c'\
b'\x66\x42\x42\x42\x42\x42\x42\x66\x3c\x00\x00\x00\x07\x00\x00\x10'\
b'\x70\x10\x10\x10\x10\x10\x10\x10\x7c\x00\x00\x00\x07\x00\x00\x38'\
b'\x6c\x44\x04\x0c\x08\x10\x20\x44\x7c\x00\x00\x00\x07\x00\x00\x78'\
b'\x8c\x04\x08\x30\x38\x04\x04\xcc\x78\x00\x00\x00\x07\x00\x00\x08'\
b'\x18\x18\x28\x68\x48\x88\xfc\x08\x08\x00\x00\x00\x07\x00\x00\x3c'\
b'\x20\x40\x70\x18\x0c\x04\x04\x48\x70\x00\x00\x00\x07\x00\x00\x0c'\
b'\x10\x20\x40\x78\xcc\x84\x84\xcc\x78\x00\x00\x00\x07\x00\x00\xfc'\
b'\x84\x08\x08\x10\x10\x20\x20\x40\x40\x00\x00\x00\x07\x00\x00\x38'\
b'\x4c\x44\x64\x38\x4c\x44\x44\x44\x38\x00\x00\x00\x07\x00\x00\x3c'\
b'\x66\x42\x42\x66\x3c\x04\x08\x10\x60\x00\x00\x00\x04\x00\x00\x00'\
b'\x00\x00\x60\x00\x00\x00\x00\x00\x60\x00\x00\x00\x04\x00\x00\x00'\
b'\x00\x00\x60\x00\x00\x00\x00\x00\x60\x20\x40\x00\x08\x00\x00\x00'\
b'\x00\x00\x06\x18\x60\xc0\x60\x18\x06\x00\x00\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\xfe\x00\xfe\x00\x00\x00\x00\x00\x08\x00\x00\x00'\
b'\x00\x00\xc0\x30\x0c\x06\x0c\x30\xc0\x00\x00\x00\x06\x00\x00\x70'\
b'\x88\x88\x08\x10\x20\x20\x00\x20\x20\x00\x00\x00\x0d\x00\x00\x00'\
b'\x0f\x80\x30\x60\x60\x20\x46\x90\x89\x10\x91\x10\x91\x10\x93\x20'\
b'\xcd\xc0\x40\x00\x30\xc0\x0f\x00\x00\x00\x0b\x00\x00\x00\x04\x00'\
b'\x04\x00\x0a\x00\x0a\x00\x11\x00\x11\x00\x1f\x00\x20\x80\x20\x80'\
b'\x71\xc0\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x7e\x00\x23\x00'\
b'\x21\x00\x23\x00\x3e\x00\x23\x00\x21\x00\x21\x00\x23\x00\x7e\x00'\
b'\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x1e\x80\x31\x80\x20\x80'\
b'\x40\x80\x40\x00\x40\x00\x40\x00\x60\x80\x31\x00\x1e\x00\x00\x00'\
b'\x00\x00\x00\x00\x0a\x00\x00\x00\xfe\x00\x23\x00\x21\x00\x20\x80'\
b'\x20\x80\x20\x80\x20\x80\x21\x00\x23\x00\xfe\x00\x00\x00\x00\x00'\
b'\x00\x00\x09\x00\x00\x00\x7f\x00\x21\x00\x20\x00\x22\x00\x3e\x00'\
b'\x22\x00\x20\x00\x21\x00\x21\x00\x7f\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x7f\x21\x20\x22\x3e\x22\x20\x20\x20\x70\x00\x00\x00'\
b'\x0b\x00\x00\x00\x1e\x80\x31\x80\x20\x80\x40\x80\x40\x00\x43\xc0'\
b'\x40\x80\x60\x80\x31\x80\x1f\x00\x00\x00\x00\x00\x00\x00\x0a\x00'\
b'\x00\x00\x73\x80\x21\x00\x21\x00\x21\x00\x3f\x00\x21\x00\x21\x00'\
b'\x21\x00\x21\x00\x73\x80\x00\x00\x00\x00\x00\x00\x05\x00\x00\x70'\
b'\x20\x20\x20\x20\x20\x20\x20\x20\x70\x00\x00\x00\x06\x00\x00\x38'\
b'\x10\x10\x10\x10\x10\x10\x10\x50\x60\x00\x00\x00\x0a\x00\x00\x00'\
b'\x77\x00\x22\x00\x24\x00\x28\x00\x38\x00\x28\x00\x24\x00\x22\x00'\
b'\x23\x00\x73\x80\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x70\x00'\
b'\x20\x00\x20\x00\x20\x00\x20\x00\x20\x00\x20\x00\x20\x00\x21\x00'\
b'\x7f\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x70\x70\x30\x60'\
b'\x28\xa0\x28\xa0\x2d\xa0\x25\x20\x25\x20\x27\x20\x22\x20\x72\x70'\
b'\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x71\xc0\x30\x80\x28\x80'\
b'\x2c\x80\x24\x80\x26\x80\x22\x80\x22\x80\x21\x80\x71\x80\x00\x00'\
b'\x00\x00\x00\x00\x0a\x00\x00\x00\x1e\x00\x33\x00\x21\x00\x40\x80'\
b'\x40\x80\x40\x80\x40\x80\x21\x00\x33\x00\x1e\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x00\x7c\x26\x22\x22\x26\x3c\x20\x20\x20\x70\x00'\
b'\x00\x00\x0a\x00\x00\x00\x1e\x00\x33\x00\x21\x00\x40\x80\x40\x80'\
b'\x40\x80\x40\x80\x21\x00\x33\x00\x1e\x00\x04\x00\x03\x00\x01\x80'\
b'\x09\x00\x00\x00\xfc\x00\x26\x00\x22\x00\x22\x00\x26\x00\x3c\x00'\
b'\x24\x00\x22\x00\x23\x00\xf1\x80\x00\x00\x00\x00\x00\x00\x08\x00'\
b'\x00\x3a\x66\x42\x60\x38\x0c\x02\x42\x66\x5c\x00\x00\x00\x09\x00'\
b'\x00\x00\x7f\x00\x49\x00\x49\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x73\x80\x21\x00\x21\x00\x21\x00\x21\x00\x21\x00\x21\x00\x21\x00'\
b'\x33\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\xe3\x80'\
b'\x41\x00\x63\x00\x22\x00\x22\x00\x36\x00\x14\x00\x1c\x00\x08\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\xe7\x38\x42\x10'\
b'\x62\x30\x22\x20\x25\x20\x35\x60\x15\x40\x18\xc0\x08\x80\x08\x80'\
b'\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x73\x80\x21\x00\x12\x00'\
b'\x12\x00\x0c\x00\x0c\x00\x12\x00\x21\x00\x61\x80\xf3\xc0\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x00\x00\xe3\x80\x41\x00\x22\x00\x22\x00'\
b'\x14\x00\x08\x00\x08\x00\x08\x00\x08\x00\x1c\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x00\x7f\x43\x02\x04\x08\x10\x20\x40\xc1\xff\x00'\
b'\x00\x00\x05\x00\x00\x70\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x70\x04\x00\x00\x80\x80\x40\x40\x40\x20\x20\x20\x10\x10\x00'\
b'\x00\x00\x05\x00\x00\x70\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'\
b'\x10\x70\x07\x00\x00\x10\x28\x28\x44\x44\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe'\
b'\x00\x00'

_index =\
b'\x00\x00\x10\x00\x20\x00\x30\x00\x40\x00\x50\x00\x60\x00\x7e\x00'\
b'\x9c\x00\xac\x00\xbc\x00\xcc\x00\xdc\x00\xec\x00\xfc\x00\x0c\x01'\
b'\x1c\x01\x2c\x01\x3c\x01\x4c\x01\x5c\x01\x6c\x01\x7c\x01\x8c\x01'\
b'\x9c\x01\xac\x01\xbc\x01\xcc\x01\xdc\x01\xec\x01\xfc\x01\x0c\x02'\
b'\x1c\x02\x2c\x02\x4a\x02\x68\x02\x86\x02\xa4\x02\xc2\x02\xe0\x02'\
b'\xf0\x02\x0e\x03\x2c\x03\x3c\x03\x4c\x03\x6a\x03\x88\x03\xa6\x03'\
b'\xc4\x03\xe2\x03\xf2\x03\x10\x04\x2e\x04\x3e\x04\x5c\x04\x7a\x04'\
b'\x98\x04\xb6\x04\xd4\x04\xf2\x04\x02\x05\x12\x05\x22\x05\x32\x05'\
b'\x42\x05\x52\x05'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 14
    return _mvfont[doff + 2:next_offs], 14, width
 
