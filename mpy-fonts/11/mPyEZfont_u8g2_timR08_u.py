'''
    mPyEZfont_u8g2_timR08_u.py : generated as part of the microPyEZfonts repository
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
# Font: timR08.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/u-char.set u8g2/tools/font/bdf/timR08.bdf 0 tmp_mPyEZfont_u8g2_timR08_u.py
version = '0.33'

def height():
    return 11

def baseline():
    return 8

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
b'\x04\x00\x00\xe0\xa0\x20\x40\x40\x00\x40\x00\x00\x00\x02\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x40\x40\x40'\
b'\x40\x40\x00\x40\x00\x00\x00\x04\x00\x00\xa0\xa0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x05\x00\x00\x50\x50\xf8\x50\xf8\x50\x50\x00\x00'\
b'\x00\x05\x00\x20\x70\x90\x80\x60\x10\x90\xe0\x20\x00\x00\x08\x00'\
b'\x00\x7e\xa4\xa8\x56\x2a\x2a\x44\x00\x00\x00\x08\x00\x00\x30\x50'\
b'\x6e\x74\x98\x8d\x76\x00\x00\x00\x02\x00\x00\x80\x80\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x04\x00\x00\x20\x40\x40\x80\x80\x80\x40\x40'\
b'\x20\x00\x04\x00\x00\x80\x40\x40\x20\x20\x20\x40\x40\x80\x00\x05'\
b'\x00\x00\x50\x20\x50\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00'\
b'\x00\x20\x20\xf8\x20\x20\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xc0\x40\x00\x00\x04\x00\x00\x00\x00\x00\x00\xe0\x00\x00'\
b'\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x00'\
b'\x03\x00\x00\x20\x20\x40\x40\x40\x80\x80\x00\x00\x00\x05\x00\x00'\
b'\x60\x90\x90\x90\x90\x90\x60\x00\x00\x00\x05\x00\x00\x20\x60\x20'\
b'\x20\x20\x20\x70\x00\x00\x00\x05\x00\x00\x60\x90\x10\x20\x20\x40'\
b'\xf0\x00\x00\x00\x05\x00\x00\x60\x90\x10\x60\x10\x10\xe0\x00\x00'\
b'\x00\x05\x00\x00\x10\x30\x50\x90\xf8\x10\x10\x00\x00\x00\x05\x00'\
b'\x00\x70\x40\xe0\x10\x10\x10\xe0\x00\x00\x00\x05\x00\x00\x30\x40'\
b'\xe0\x90\x90\x90\x60\x00\x00\x00\x05\x00\x00\xf0\x90\x20\x20\x40'\
b'\x40\x40\x00\x00\x00\x05\x00\x00\x60\x90\x90\x60\x90\x90\x60\x00'\
b'\x00\x00\x05\x00\x00\x60\x90\x90\x90\x70\x20\xc0\x00\x00\x00\x03'\
b'\x00\x00\x00\x00\x40\x00\x00\x00\x40\x00\x00\x00\x03\x00\x00\x00'\
b'\x00\x40\x00\x00\x00\xc0\x40\x00\x00\x05\x00\x00\x00\x00\x10\x20'\
b'\x40\x20\x10\x00\x00\x00\x06\x00\x00\x00\x00\x00\xf8\x00\xf8\x00'\
b'\x00\x00\x00\x05\x00\x00\x00\x00\x80\x40\x20\x40\x80\x00\x00\x00'\
b'\x04\x00\x00\xe0\xa0\x20\x40\x40\x00\x40\x00\x00\x00\x09\x00\x00'\
b'\x00\x3c\x00\x42\x00\x9d\x00\xa5\x00\xa5\x00\xad\x00\x92\x00\x40'\
b'\x00\x3e\x00\x00\x00\x08\x00\x00\x10\x38\x28\x28\x7c\x44\xee\x00'\
b'\x00\x00\x06\x00\x00\xf0\x48\x48\x70\x48\x48\xf0\x00\x00\x00\x07'\
b'\x00\x00\x7c\xc4\x80\x80\x80\xc4\x78\x00\x00\x00\x07\x00\x00\xf8'\
b'\x4c\x44\x44\x44\x4c\xf8\x00\x00\x00\x06\x00\x00\xf8\x48\x40\x70'\
b'\x40\x48\xf8\x00\x00\x00\x06\x00\x00\xf8\x48\x40\x70\x40\x40\xe0'\
b'\x00\x00\x00\x07\x00\x00\x7c\xc4\x80\x9c\x84\xc4\x78\x00\x00\x00'\
b'\x08\x00\x00\xee\x44\x44\x7c\x44\x44\xee\x00\x00\x00\x04\x00\x00'\
b'\xe0\x40\x40\x40\x40\x40\xe0\x00\x00\x00\x04\x00\x00\x70\x20\x20'\
b'\x20\x20\xa0\xc0\x00\x00\x00\x07\x00\x00\xec\x48\x50\x60\x50\x48'\
b'\xec\x00\x00\x00\x06\x00\x00\xe0\x40\x40\x40\x40\x48\xf8\x00\x00'\
b'\x00\x0a\x00\x00\x00\xe3\x80\x63\x00\x55\x00\x55\x00\x5d\x00\x49'\
b'\x00\xeb\x80\x00\x00\x00\x00\x00\x00\x08\x00\x00\xee\x64\x54\x54'\
b'\x4c\x4c\xe4\x00\x00\x00\x07\x00\x00\x78\xcc\x84\x84\x84\xcc\x78'\
b'\x00\x00\x00\x06\x00\x00\xf0\x48\x48\x70\x40\x40\xe0\x00\x00\x00'\
b'\x07\x00\x00\x78\xcc\x84\x84\x84\xcc\x70\x18\x0c\x00\x07\x00\x00'\
b'\xf0\x48\x48\x70\x50\x48\xec\x00\x00\x00\x05\x00\x00\x70\x90\xc0'\
b'\x60\x10\x90\xe0\x00\x00\x00\x06\x00\x00\xf8\xa8\x20\x20\x20\x20'\
b'\x70\x00\x00\x00\x08\x00\x00\xee\x44\x44\x44\x44\x6c\x38\x00\x00'\
b'\x00\x08\x00\x00\xee\x44\x6c\x28\x28\x10\x10\x00\x00\x00\x0b\x00'\
b'\x00\x00\xee\xe0\x44\x40\x64\xc0\x2e\x80\x2a\x80\x11\x00\x11\x00'\
b'\x00\x00\x00\x00\x00\x00\x08\x00\x00\xee\x44\x28\x10\x28\x44\xee'\
b'\x00\x00\x00\x08\x00\x00\xee\x44\x28\x38\x10\x10\x38\x00\x00\x00'\
b'\x06\x00\x00\xf8\x88\x10\x20\x40\x88\xf8\x00\x00\x00\x03\x00\x00'\
b'\xc0\x80\x80\x80\x80\x80\x80\x80\xc0\x00\x03\x00\x00\x80\x80\x40'\
b'\x40\x40\x20\x20\x00\x00\x00\x03\x00\x00\xc0\x40\x40\x40\x40\x40'\
b'\x40\x40\xc0\x00\x05\x00\x00\x20\x50\x50\x00\x00\x00\x00\x00\x00'\
b'\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00'

_index =\
b'\x00\x00\x0d\x00\x1a\x00\x27\x00\x34\x00\x41\x00\x4e\x00\x5b\x00'\
b'\x68\x00\x75\x00\x82\x00\x8f\x00\x9c\x00\xa9\x00\xb6\x00\xc3\x00'\
b'\xd0\x00\xdd\x00\xea\x00\xf7\x00\x04\x01\x11\x01\x1e\x01\x2b\x01'\
b'\x38\x01\x45\x01\x52\x01\x5f\x01\x6c\x01\x79\x01\x86\x01\x93\x01'\
b'\xa0\x01\xad\x01\xc5\x01\xd2\x01\xdf\x01\xec\x01\xf9\x01\x06\x02'\
b'\x13\x02\x20\x02\x2d\x02\x3a\x02\x47\x02\x54\x02\x61\x02\x79\x02'\
b'\x86\x02\x93\x02\xa0\x02\xad\x02\xba\x02\xc7\x02\xd4\x02\xe1\x02'\
b'\xee\x02\x06\x03\x13\x03\x20\x03\x2d\x03\x3a\x03\x47\x03\x54\x03'\
b'\x61\x03\x6e\x03'

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
 
