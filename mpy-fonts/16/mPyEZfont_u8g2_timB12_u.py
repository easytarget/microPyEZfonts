'''
    mPyEZfont_u8g2_timB12_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original timB12.bdf font file was sourced from the U8G2 project:
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
# Font: timB12.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/u-char.set u8g2/tools/font/bdf/timB12.bdf 0 tmp_mPyEZfont_u8g2_timB12_u.py
version = '0.33'

def height():
    return 16

def baseline():
    return 12

def max_width():
    return 17

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
b'\x08\x00\x00\x1c\x66\x66\x06\x06\x04\x08\x10\x00\x30\x30\x00\x00'\
b'\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x06\x00\x00\x30\x30\x30\x30\x30\x20\x20\x00\x00'\
b'\x30\x30\x00\x00\x00\x00\x09\x00\x00\x00\x6c\x00\x6c\x00\x6c\x00'\
b'\x48\x00\x48\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x12\x12\x12\x7f\x24'\
b'\x24\x24\xfe\x48\x48\x48\x00\x00\x00\x00\x08\x00\x10\x7a\x96\xd2'\
b'\xf0\x78\x3c\x1e\x16\x92\xd2\xbc\x10\x00\x00\x00\x10\x00\x0c\x20'\
b'\x1b\xc0\x32\x40\x32\x40\x32\x80\x34\x98\x19\x34\x02\x64\x02\x64'\
b'\x04\x64\x04\x68\x08\x30\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00'\
b'\x00\x00\x07\x00\x09\x80\x09\x80\x0d\x00\x0e\x70\x1e\x20\x27\x20'\
b'\x23\x40\x31\x90\x39\xf0\x1e\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x30\x30\x30\x20\x20\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x06\x00\x00\x08\x10\x30\x20\x60\x60\x60\x60\x60\x60\x20'\
b'\x30\x10\x08\x00\x06\x00\x00\x80\x40\x60\x20\x30\x30\x30\x30\x30'\
b'\x30\x20\x60\x40\x80\x00\x08\x00\x00\x10\x54\x7c\x38\x7c\x54\x10'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x7f\x00\x08\x00\x08\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x60\x60\x20\x20\x40\x00\x05\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\xf0\xf0\x00\x00\x00\x00\x00\x00\x00\x04\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x00\x00\x00\x00'\
b'\x05\x00\x00\x10\x30\x20\x20\x60\x40\x40\x40\xc0\x80\x80\x00\x00'\
b'\x00\x00\x08\x00\x00\x18\x24\x66\x66\x66\x66\x66\x66\x66\x24\x18'\
b'\x00\x00\x00\x00\x08\x00\x00\x08\x78\x18\x18\x18\x18\x18\x18\x18'\
b'\x18\x7e\x00\x00\x00\x00\x08\x00\x00\x38\x7c\x9c\x0c\x0c\x08\x18'\
b'\x10\x22\x7c\xfc\x00\x00\x00\x00\x08\x00\x00\x38\x7c\x8c\x08\x10'\
b'\x3c\x0e\x06\xc6\xcc\x78\x00\x00\x00\x00\x08\x00\x00\x04\x0c\x1c'\
b'\x2c\x2c\x4c\x8c\xfe\xfe\x0c\x0c\x00\x00\x00\x00\x08\x00\x00\x1f'\
b'\x3e\x20\x38\x7c\x0e\x06\x06\xc6\xcc\x70\x00\x00\x00\x00\x08\x00'\
b'\x00\x06\x18\x30\x30\x78\x66\x66\x66\x66\x24\x18\x00\x00\x00\x00'\
b'\x08\x00\x00\x7e\x7e\x84\x04\x0c\x08\x08\x18\x10\x30\x20\x00\x00'\
b'\x00\x00\x08\x00\x00\x38\x44\xc6\xe4\x78\x3c\x4e\xc6\xc6\x44\x38'\
b'\x00\x00\x00\x00\x08\x00\x00\x18\x24\x66\x66\x66\x66\x3e\x0c\x0c'\
b'\x18\x60\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x60\x60\x00'\
b'\x00\x00\x60\x60\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x60'\
b'\x60\x00\x00\x00\x60\x60\x20\x20\x40\x00\x09\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x03\x00\x0e\x00\x38\x00\xc0\x00\xc0\x00\x38\x00'\
b'\x0e\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x7f\x00\x00\x00\x7f\x00'\
b'\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x70\x00\x1c\x00\x03\x00'\
b'\x03\x00\x1c\x00\x70\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x1c\x66\x66\x06\x06\x04\x08\x10\x00\x30\x30\x00\x00'\
b'\x00\x00\x10\x00\x00\x00\x03\xc0\x0e\x30\x18\x08\x33\xa8\x66\x64'\
b'\x6c\x64\x6c\x44\x6c\xc8\x6c\xd8\x27\x70\x10\x00\x0c\x30\x03\xc0'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x04\x00\x0e\x00\x0e\x00\x1b\x00'\
b'\x13\x00\x33\x00\x21\x80\x7f\x80\x40\xc0\xc0\xc0\xe1\xe0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x7e\x00\x33\x00\x31\x80'\
b'\x31\x80\x33\x00\x3f\x00\x31\x80\x30\xc0\x30\xc0\x31\x80\x7f\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x0f\x40\x31\xc0'\
b'\x20\xc0\x60\x40\x60\x00\x60\x00\x60\x00\x60\x00\x30\x40\x39\x80'\
b'\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x7e\x00'\
b'\x33\x00\x31\x80\x30\xc0\x30\xc0\x30\xc0\x30\xc0\x30\xc0\x31\x80'\
b'\x33\x00\x7e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x7f\x80\x31\x80\x30\x80\x30\x00\x31\x00\x3f\x00\x31\x00\x30\x00'\
b'\x30\x80\x31\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00'\
b'\x00\x00\x7f\x80\x31\x80\x30\x80\x30\x00\x31\x00\x3f\x00\x31\x00'\
b'\x30\x00\x30\x00\x30\x00\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x0f\x40\x31\xc0\x20\xc0\x60\x40\x60\x00\x60\x00'\
b'\x63\xe0\x60\xc0\x60\xc0\x30\xc0\x1f\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x00\x00\x79\xe0\x30\xc0\x30\xc0\x30\xc0\x30\xc0'\
b'\x3f\xc0\x30\xc0\x30\xc0\x30\xc0\x30\xc0\x79\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x06\x00\x00\x78\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\x30\x78\x00\x00\x00\x00\x08\x00\x00\x1e\x0c\x0c\x0c\x0c\x0c\x0c'\
b'\x0c\x0c\x0c\x6c\x68\x30\x00\x00\x0d\x00\x00\x00\x7d\xe0\x30\x80'\
b'\x31\x00\x32\x00\x34\x00\x3c\x00\x36\x00\x33\x00\x31\x80\x30\xc0'\
b'\x7d\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x78\x00'\
b'\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x40\x30\x40'\
b'\x30\xc0\x7f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00'\
b'\xe0\x1c\x70\x18\x70\x38\x78\x38\x58\x58\x4c\x58\x4c\x98\x46\x98'\
b'\x47\x18\x43\x18\xe2\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x78\xe0\x38\x40\x2c\x40\x2c\x40\x26\x40\x23\x40\x23\xc0'\
b'\x21\xc0\x20\xc0\x20\xc0\x70\x40\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x0f\x00\x30\xc0\x20\x40\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x20\x40\x30\xc0\x0f\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0a\x00\x00\x00\x7f\x00\x33\x80\x31\x80\x31\x80\x33\x00'\
b'\x3e\x00\x30\x00\x30\x00\x30\x00\x30\x00\x78\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x0f\x00\x30\xc0\x20\x40\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x20\x40\x30\xc0\x1f\x80\x07\x00'\
b'\x03\x00\x00\xc0\x00\x00\x0c\x00\x00\x00\x7f\x00\x33\x80\x31\x80'\
b'\x31\x80\x33\x00\x3e\x00\x36\x00\x33\x00\x31\x80\x30\xc0\x79\xe0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x3d\x00\x43\x00'\
b'\xc1\x00\xe0\x00\x78\x00\x3c\x00\x0e\x00\x07\x00\x83\x00\xc2\x00'\
b'\xbc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x7f\xe0'\
b'\x66\x60\x46\x20\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x78\xe0\x30\x40\x30\x40\x30\x40\x30\x40\x30\x40\x30\x40\x30\x40'\
b'\x30\x40\x10\x80\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\xf8\xe0\x30\x40\x30\x40\x18\x80\x18\x80\x0d\x00\x0d\x00'\
b'\x07\x00\x06\x00\x02\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x11\x00\x00\x00\x00\xfb\xef\x80\x70\xc3\x00\x30\xc2\x00\x38\xe2'\
b'\x00\x19\xe6\x00\x1d\x64\x00\x0d\x7c\x00\x0f\x38\x00\x06\x38\x00'\
b'\x06\x10\x00\x02\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x00\x00\x7d\xe0\x38\x80\x1d\x00\x1d\x00\x0e\x00'\
b'\x07\x00\x0f\x00\x0b\x80\x11\x80\x21\xc0\x73\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\xf8\xe0\x70\x40\x38\x80\x18\x80'\
b'\x1d\x00\x0f\x00\x06\x00\x06\x00\x06\x00\x06\x00\x0f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\xff\xc0\xc1\xc0\x83\x80'\
b'\x07\x00\x0e\x00\x0e\x00\x1c\x00\x38\x00\x70\x40\xf0\xc0\xff\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x70\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x70\x00\x05\x00\x00\x80\xc0\x40'\
b'\x40\x60\x20\x20\x20\x30\x10\x10\x00\x00\x00\x00\x06\x00\x00\x70'\
b'\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x70\x00\x09\x00'\
b'\x00\x00\x08\x00\x1c\x00\x14\x00\x36\x00\x22\x00\x63\x00\x41\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00'\
b'\x00\x00'

_index =\
b'\x00\x00\x12\x00\x24\x00\x36\x00\x58\x00\x6a\x00\x7c\x00\x9e\x00'\
b'\xc0\x00\xd2\x00\xe4\x00\xf6\x00\x08\x01\x2a\x01\x3c\x01\x4e\x01'\
b'\x60\x01\x72\x01\x84\x01\x96\x01\xa8\x01\xba\x01\xcc\x01\xde\x01'\
b'\xf0\x01\x02\x02\x14\x02\x26\x02\x38\x02\x4a\x02\x6c\x02\x8e\x02'\
b'\xb0\x02\xc2\x02\xe4\x02\x06\x03\x28\x03\x4a\x03\x6c\x03\x8e\x03'\
b'\xb0\x03\xd2\x03\xf4\x03\x06\x04\x18\x04\x3a\x04\x5c\x04\x7e\x04'\
b'\xa0\x04\xc2\x04\xe4\x04\x06\x05\x28\x05\x4a\x05\x6c\x05\x8e\x05'\
b'\xb0\x05\xe2\x05\x04\x06\x26\x06\x48\x06\x5a\x06\x6c\x06\x7e\x06'\
b'\xa0\x06\xb2\x06'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 16
    return _mvfont[doff + 2:next_offs], 16, width
 
