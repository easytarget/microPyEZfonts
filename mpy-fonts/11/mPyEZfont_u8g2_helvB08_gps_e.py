'''
    mPyEZfont_u8g2_helvB08_gps_e.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original helvB08_gps.bdf font file was sourced from the U8G2 project:
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
    COMMENT 
    COMMENT Degree symbol updated and moved to position 127 
    COMMENT for the gps tracker project (olikraus@gmail.com)
    COMMENT -
'''

# Code generated by font_to_py.py.
# Font: helvB08_gps.bdf
# Cmd: micropython-font-to-py/font_to_py.py -x u8g2/tools/font/bdf/helvB08_gps.bdf 0 tmp_mPyEZfont_u8g2_helvB08_gps_e.py
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
    return 126

_font =\
b'\x06\x00\x00\x70\xd8\x18\x30\x60\x60\x00\x60\x00\x00\x03\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x60\x60\x60'\
b'\x60\x40\x40\x00\x60\x00\x00\x05\x00\x00\x50\x50\x50\x00\x00\x00'\
b'\x00\x00\x00\x00\x07\x00\x00\x00\x28\x28\x7e\x28\xfc\x50\x50\x00'\
b'\x00\x06\x00\x20\x70\xa8\xe0\x70\x38\x28\xa8\x70\x20\x00\x08\x00'\
b'\x00\x62\xb4\x68\x10\x10\x2c\x56\x8c\x00\x00\x08\x00\x00\x70\xd8'\
b'\xd8\x70\xde\xcc\xdc\x76\x00\x00\x03\x00\x00\x40\x40\x40\x00\x00'\
b'\x00\x00\x00\x00\x00\x04\x00\x00\x20\x60\x40\xc0\xc0\xc0\xc0\x40'\
b'\x60\x20\x04\x00\x00\x80\xc0\x40\x60\x60\x60\x60\x40\xc0\x80\x04'\
b'\x00\x00\xa0\x40\xa0\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00'\
b'\x00\x30\x30\xfc\x30\x30\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xc0\xc0\x40\x80\x05\x00\x00\x00\x00\x00\x00\xf0\x00\x00'\
b'\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\x00\x00'\
b'\x04\x00\x00\x10\x10\x20\x20\x40\x40\x80\x80\x00\x00\x06\x00\x00'\
b'\x70\xd8\xd8\xd8\xd8\xd8\xd8\x70\x00\x00\x06\x00\x00\x30\x70\x30'\
b'\x30\x30\x30\x30\x30\x00\x00\x06\x00\x00\x70\xd8\x18\x18\x30\x60'\
b'\xc0\xf8\x00\x00\x06\x00\x00\x70\xd8\x18\x30\x18\x18\xd8\x70\x00'\
b'\x00\x06\x00\x00\x08\x18\x38\x58\x98\xfc\x18\x18\x00\x00\x06\x00'\
b'\x00\xf8\xc0\xc0\xf0\x18\x98\xd8\x70\x00\x00\x06\x00\x00\x70\xd8'\
b'\xc0\xf0\xd8\xd8\xd8\x70\x00\x00\x06\x00\x00\xf8\x18\x18\x30\x30'\
b'\x60\x60\x60\x00\x00\x06\x00\x00\x70\xd8\xd8\x70\xd8\xd8\xd8\x70'\
b'\x00\x00\x06\x00\x00\x70\xd8\xd8\xd8\x78\x18\xd8\x70\x00\x00\x03'\
b'\x00\x00\x00\x00\xc0\xc0\x00\x00\xc0\xc0\x00\x00\x03\x00\x00\x00'\
b'\x00\xc0\xc0\x00\x00\xc0\xc0\x40\x80\x05\x00\x00\x00\x00\x30\x60'\
b'\xc0\x60\x30\x00\x00\x00\x06\x00\x00\x00\x00\x00\xf8\x00\xf8\x00'\
b'\x00\x00\x00\x05\x00\x00\x00\x00\xc0\x60\x30\x60\xc0\x00\x00\x00'\
b'\x06\x00\x00\x70\xd8\x18\x30\x60\x60\x00\x60\x00\x00\x0b\x00\x00'\
b'\x00\x1f\x00\x60\x80\x4d\x40\x92\x40\xa2\x40\xa4\x80\x9b\x00\x40'\
b'\x00\x3e\x00\x00\x00\x08\x00\x00\x38\x38\x6c\x6c\x6c\xfe\xc6\xc6'\
b'\x00\x00\x07\x00\x00\xf8\xcc\xcc\xf8\xcc\xcc\xcc\xf8\x00\x00\x08'\
b'\x00\x00\x3c\x66\xc2\xc0\xc0\xc2\x66\x3c\x00\x00\x07\x00\x00\xf0'\
b'\xd8\xcc\xcc\xcc\xcc\xd8\xf0\x00\x00\x06\x00\x00\xf8\xc0\xc0\xf8'\
b'\xc0\xc0\xc0\xf8\x00\x00\x06\x00\x00\xf8\xc0\xc0\xf0\xc0\xc0\xc0'\
b'\xc0\x00\x00\x08\x00\x00\x3c\x66\xc2\xc0\xce\xc6\x66\x3a\x00\x00'\
b'\x07\x00\x00\xcc\xcc\xcc\xfc\xcc\xcc\xcc\xcc\x00\x00\x03\x00\x00'\
b'\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\x00\x00\x06\x00\x00\x18\x18\x18'\
b'\x18\x18\x18\xd8\x70\x00\x00\x07\x00\x00\xcc\xd8\xf0\xe0\xf0\xd8'\
b'\xcc\xc6\x00\x00\x06\x00\x00\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xf8\x00'\
b'\x00\x0a\x00\x00\x00\xc1\x80\xe3\x80\xe3\x80\xf7\x80\xd5\x80\xdd'\
b'\x80\xc9\x80\xc9\x80\x00\x00\x00\x00\x08\x00\x00\xc6\xe6\xe6\xd6'\
b'\xd6\xce\xce\xc6\x00\x00\x08\x00\x00\x38\x6c\xc6\xc6\xc6\xc6\x6c'\
b'\x38\x00\x00\x07\x00\x00\xf8\xcc\xcc\xcc\xf8\xc0\xc0\xc0\x00\x00'\
b'\x08\x00\x00\x38\x6c\xc6\xc6\xc6\xd6\x6c\x3c\x02\x00\x07\x00\x00'\
b'\xf8\xcc\xcc\xcc\xf8\xcc\xcc\xcc\x00\x00\x07\x00\x00\x78\xcc\xe0'\
b'\x78\x1c\x8c\xcc\x78\x00\x00\x07\x00\x00\xfc\x30\x30\x30\x30\x30'\
b'\x30\x30\x00\x00\x07\x00\x00\xcc\xcc\xcc\xcc\xcc\xcc\xcc\x78\x00'\
b'\x00\x08\x00\x00\xc6\xc6\x6c\x6c\x6c\x38\x38\x10\x00\x00\x0b\x00'\
b'\x00\x00\xcc\xc0\xcc\xc0\xcc\xc0\x6d\x80\x6d\x80\x7f\x80\x33\x00'\
b'\x33\x00\x00\x00\x00\x00\x08\x00\x00\xc6\xc6\x6c\x38\x38\x6c\xc6'\
b'\xc6\x00\x00\x09\x00\x00\x00\xc3\x00\xc3\x00\x66\x00\x66\x00\x3c'\
b'\x00\x18\x00\x18\x00\x18\x00\x00\x00\x00\x00\x07\x00\x00\xfc\x0c'\
b'\x18\x30\x70\x60\xc0\xfc\x00\x00\x04\x00\x00\xe0\xc0\xc0\xc0\xc0'\
b'\xc0\xc0\xc0\xc0\xe0\x04\x00\x00\x80\x80\x40\x40\x20\x20\x10\x10'\
b'\x00\x00\x04\x00\x00\xe0\x60\x60\x60\x60\x60\x60\x60\x60\xe0\x05'\
b'\x00\x00\x60\xf0\x90\x90\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\xfc\x00\x03\x00\x80\x40\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x70\x98\x78\xd8\xd8'\
b'\x6c\x00\x00\x06\x00\x00\xc0\xc0\xf0\xd8\xd8\xd8\xd8\xf0\x00\x00'\
b'\x05\x00\x00\x00\x00\x70\xd0\xc0\xc0\xd0\x70\x00\x00\x06\x00\x00'\
b'\x18\x18\x78\xd8\xd8\xd8\xd8\x78\x00\x00\x06\x00\x00\x00\x00\x70'\
b'\xd8\xf8\xc0\xd8\x70\x00\x00\x05\x00\x00\x38\x60\xf0\x60\x60\x60'\
b'\x60\x60\x00\x00\x06\x00\x00\x00\x00\x68\xd8\xd8\xd8\xd8\x78\x18'\
b'\x70\x06\x00\x00\xc0\xc0\xf0\xd8\xd8\xd8\xd8\xd8\x00\x00\x03\x00'\
b'\x00\xc0\x00\xc0\xc0\xc0\xc0\xc0\xc0\x00\x00\x04\x00\x00\x60\x00'\
b'\x60\x60\x60\x60\x60\x60\x60\xc0\x06\x00\x00\xc0\xc0\xd8\xf0\xe0'\
b'\xf0\xd8\xcc\x00\x00\x03\x00\x00\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0'\
b'\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\xb6\x00\xdb\x00\xdb\x00'\
b'\xdb\x00\xdb\x00\xdb\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\xb0'\
b'\xd8\xd8\xd8\xd8\xd8\x00\x00\x06\x00\x00\x00\x00\x70\xd8\xd8\xd8'\
b'\xd8\x70\x00\x00\x06\x00\x00\x00\x00\xb0\xd8\xd8\xd8\xd8\xf0\xc0'\
b'\xc0\x06\x00\x00\x00\x00\x68\xd8\xd8\xd8\xd8\x78\x18\x18\x04\x00'\
b'\x00\x00\x00\xb0\xe0\xc0\xc0\xc0\xc0\x00\x00\x06\x00\x00\x00\x00'\
b'\x70\xd8\x70\x18\xd8\x70\x00\x00\x05\x00\x00\x60\x60\xf0\x60\x60'\
b'\x60\x60\x30\x00\x00\x06\x00\x00\x00\x00\xd8\xd8\xd8\xd8\xd8\x68'\
b'\x00\x00\x06\x00\x00\x00\x00\xd8\xd8\xd8\x50\x70\x20\x00\x00\x08'\
b'\x00\x00\x00\x00\xd6\xd6\xd6\x6c\x6c\x6c\x00\x00\x07\x00\x00\x00'\
b'\x00\xcc\x78\x30\x78\xcc\xcc\x00\x00\x06\x00\x00\x00\x00\xd8\xd8'\
b'\xd8\xd8\x78\x30\x30\x60\x06\x00\x00\x00\x00\xf8\x18\x30\x60\xc0'\
b'\xf8\x00\x00\x05\x00\x00\x30\x60\x60\x60\xc0\x60\x60\x60\x60\x30'\
b'\x03\x00\x00\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x05\x00\x00'\
b'\xc0\x60\x60\x60\x30\x60\x60\x60\x60\xc0\x06\x00\x00\x00\x00\x00'\
b'\x68\xb0\x00\x00\x00\x00\x00'

_index =\
b'\x00\x00\x0d\x00\x1a\x00\x27\x00\x34\x00\x41\x00\x4e\x00\x5b\x00'\
b'\x68\x00\x75\x00\x82\x00\x8f\x00\x9c\x00\xa9\x00\xb6\x00\xc3\x00'\
b'\xd0\x00\xdd\x00\xea\x00\xf7\x00\x04\x01\x11\x01\x1e\x01\x2b\x01'\
b'\x38\x01\x45\x01\x52\x01\x5f\x01\x6c\x01\x79\x01\x86\x01\x93\x01'\
b'\xa0\x01\xad\x01\xc5\x01\xd2\x01\xdf\x01\xec\x01\xf9\x01\x06\x02'\
b'\x13\x02\x20\x02\x2d\x02\x3a\x02\x47\x02\x54\x02\x61\x02\x79\x02'\
b'\x86\x02\x93\x02\xa0\x02\xad\x02\xba\x02\xc7\x02\xd4\x02\xe1\x02'\
b'\xee\x02\x06\x03\x13\x03\x2b\x03\x38\x03\x45\x03\x52\x03\x5f\x03'\
b'\x6c\x03\x79\x03\x86\x03\x93\x03\xa0\x03\xad\x03\xba\x03\xc7\x03'\
b'\xd4\x03\xe1\x03\xee\x03\xfb\x03\x08\x04\x15\x04\x22\x04\x3a\x04'\
b'\x47\x04\x54\x04\x61\x04\x6e\x04\x7b\x04\x88\x04\x95\x04\xa2\x04'\
b'\xaf\x04\xbc\x04\xc9\x04\xd6\x04\xe3\x04\xf0\x04\xfd\x04\x0a\x05'\
b'\x17\x05'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 126 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 11
    return _mvfont[doff + 2:next_offs], 11, width
 
