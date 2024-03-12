'''
    mPyEZfont_u8g2_helvR12_r.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original helvR12.bdf font file was sourced from the U8G2 project:
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
# Font: helvR12.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/r-char.set u8g2/tools/font/bdf/helvR12.bdf 0 tmp_mPyEZfont_u8g2_helvR12_r.py
version = '0.33'

def height():
    return 17

def baseline():
    return 13

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
    return 126

_font =\
b'\x09\x00\x00\x00\x1c\x00\x22\x00\x41\x00\x41\x00\x01\x00\x02\x00'\
b'\x04\x00\x08\x00\x08\x00\x00\x00\x08\x00\x08\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x20\x20\x20\x20\x20\x20'\
b'\x20\x20\x20\x00\x20\x20\x00\x00\x00\x00\x06\x00\x00\x48\x48\x48'\
b'\x48\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00'\
b'\x00\x00\x00\x12\x00\x12\x00\x12\x00\x7f\x00\x24\x00\x24\x00\x24'\
b'\x00\xfe\x00\x48\x00\x48\x00\x48\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x09\x00\x08\x00\x3e\x00\x49\x00\x49\x00\x48\x00\x28\x00\x18'\
b'\x00\x0c\x00\x0a\x00\x09\x00\x49\x00\x49\x00\x3e\x00\x08\x00\x08'\
b'\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x70\x40\x88\x80\x88\x80\x89'\
b'\x00\x72\x00\x02\x00\x04\x00\x04\xe0\x09\x10\x11\x10\x11\x10\x20'\
b'\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x18\x00\x24'\
b'\x00\x42\x00\x42\x00\x24\x00\x18\x00\x29\x00\x45\x00\x82\x00\x83'\
b'\x00\x44\x80\x38\x40\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00'\
b'\xc0\xc0\x40\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x10\x20\x20\x20\x40\x40\x40\x40\x40\x40\x40\x40\x20'\
b'\x20\x20\x10\x06\x00\x00\x40\x20\x20\x20\x10\x10\x10\x10\x10\x10'\
b'\x10\x10\x20\x20\x20\x40\x06\x00\x00\x20\xa8\x70\x50\x88\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x08\x00\x08\x00\x08\x00\x08\x00\xff\x80\x08\x00\x08'\
b'\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x20\x20\x40\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x20\x20\x00\x00\x00\x00\x05\x00\x00\x10\x10\x20\x20\x20\x20\x40'\
b'\x40\x40\x80\x80\x80\x00\x00\x00\x00\x09\x00\x00\x00\x1c\x00\x22'\
b'\x00\x22\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x22'\
b'\x00\x22\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00'\
b'\x00\x04\x00\x04\x00\x0c\x00\x14\x00\x04\x00\x04\x00\x04\x00\x04'\
b'\x00\x04\x00\x04\x00\x04\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x09\x00\x00\x00\x1c\x00\x22\x00\x41\x00\x41\x00\x01\x00\x02'\
b'\x00\x04\x00\x18\x00\x20\x00\x40\x00\x40\x00\x7f\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x09\x00\x00\x00\x1c\x00\x22\x00\x41\x00\x41'\
b'\x00\x02\x00\x1c\x00\x02\x00\x01\x00\x41\x00\x41\x00\x22\x00\x1c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x0c\x00\x14'\
b'\x00\x14\x00\x24\x00\x24\x00\x44\x00\x44\x00\x84\x00\xff\x00\x04'\
b'\x00\x04\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00'\
b'\x00\x1f\x00\x10\x00\x10\x00\x20\x00\x3c\x00\x22\x00\x01\x00\x01'\
b'\x00\x01\x00\x41\x00\x22\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x09\x00\x00\x00\x1e\x00\x21\x00\x41\x00\x40\x00\x5c\x00\x62'\
b'\x00\x41\x00\x41\x00\x41\x00\x41\x00\x22\x00\x1c\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x09\x00\x00\x00\xff\x00\x01\x00\x02\x00\x04'\
b'\x00\x04\x00\x08\x00\x08\x00\x10\x00\x10\x00\x10\x00\x20\x00\x20'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x1c\x00\x22'\
b'\x00\x41\x00\x41\x00\x22\x00\x1c\x00\x22\x00\x41\x00\x41\x00\x41'\
b'\x00\x22\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00'\
b'\x00\x1c\x00\x22\x00\x41\x00\x41\x00\x41\x00\x41\x00\x23\x00\x1d'\
b'\x00\x01\x00\x41\x00\x42\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x04\x00\x00\x00\x00\x00\x20\x20\x00\x00\x00\x00\x00\x20\x20'\
b'\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x20\x20\x00\x00\x00\x00'\
b'\x00\x20\x20\x20\x40\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x01\x80\x06\x00\x18\x00\x60\x00\x80\x00\x60\x00\x18\x00\x06'\
b'\x00\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00'\
b'\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00\x18\x00\x06\x00\x01'\
b'\x80\x00\x40\x01\x80\x06\x00\x18\x00\x60\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x09\x00\x00\x00\x1c\x00\x22\x00\x41\x00\x41\x00\x01'\
b'\x00\x02\x00\x04\x00\x08\x00\x08\x00\x00\x00\x08\x00\x08\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00\x00\x03\xc0\x00\x0c'\
b'\x30\x00\x10\x08\x00\x21\xe8\x00\x26\x24\x00\x44\x24\x00\x48\x44'\
b'\x00\x48\x44\x00\x48\x48\x00\x4c\xc8\x00\x27\x30\x00\x20\x00\x00'\
b'\x18\x30\x00\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x0c\x00\x0c\x00\x12\x00\x12\x00\x12\x00\x21\x00\x21\x00\x7f\x80'\
b'\x40\x80\x40\x80\x80\x40\x80\x40\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x7e\x00\x41\x00\x40\x80\x40\x80\x41\x00\x7f\x00'\
b'\x40\x80\x40\x40\x40\x40\x40\x40\x40\x80\x7f\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x07\x80\x18\x40\x20\x20\x20\x00'\
b'\x40\x00\x40\x00\x40\x00\x40\x00\x20\x00\x20\x20\x18\x40\x07\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x7e\x00\x41\x80'\
b'\x40\x40\x40\x40\x40\x20\x40\x20\x40\x20\x40\x20\x40\x40\x40\x40'\
b'\x41\x80\x7e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x7f\x80\x40\x00\x40\x00\x40\x00\x40\x00\x7f\x80\x40\x00\x40\x00'\
b'\x40\x00\x40\x00\x40\x00\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x7f\x00\x40\x00\x40\x00\x40\x00\x40\x00\x7f\x00'\
b'\x40\x00\x40\x00\x40\x00\x40\x00\x40\x00\x40\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0d\x00\x00\x00\x07\x00\x18\xc0\x20\x20\x20\x00'\
b'\x40\x00\x40\x00\x43\xe0\x40\x20\x20\x20\x20\x60\x18\xa0\x07\x20'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x40\x40\x40\x40'\
b'\x40\x40\x40\x40\x40\x40\x7f\xc0\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x40\x40\x40\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x40'\
b'\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x00\x00\x00\x00\x08'\
b'\x00\x00\x04\x04\x04\x04\x04\x04\x04\x04\x84\x84\x84\x78\x00\x00'\
b'\x00\x00\x0b\x00\x00\x00\x40\x80\x41\x00\x42\x00\x44\x00\x48\x00'\
b'\x58\x00\x64\x00\x44\x00\x42\x00\x41\x00\x41\x00\x40\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x40\x00\x40\x00\x40\x00'\
b'\x40\x00\x40\x00\x40\x00\x40\x00\x40\x00\x40\x00\x40\x00\x40\x00'\
b'\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x40\x10'\
b'\x60\x30\x60\x30\x50\x50\x50\x50\x50\x50\x48\x90\x48\x90\x48\x90'\
b'\x45\x10\x45\x10\x42\x10\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x40\x40\x60\x40\x50\x40\x50\x40\x48\x40\x44\x40\x44\x40'\
b'\x42\x40\x41\x40\x41\x40\x40\xc0\x40\x40\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0d\x00\x00\x00\x07\x00\x18\xc0\x20\x20\x20\x20\x40\x10'\
b'\x40\x10\x40\x10\x40\x10\x20\x20\x20\x20\x18\xc0\x07\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x3f\x00\x20\x80\x20\x40'\
b'\x20\x40\x20\x80\x3f\x00\x20\x00\x20\x00\x20\x00\x20\x00\x20\x00'\
b'\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x07\x00'\
b'\x18\xc0\x20\x20\x20\x20\x40\x10\x40\x10\x40\x10\x40\x10\x20\x20'\
b'\x21\x20\x18\xc0\x07\x40\x00\x20\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x3f\x00\x20\x80\x20\x40\x20\x40\x20\x80\x3f\x00\x20\x80'\
b'\x20\x40\x20\x40\x20\x40\x20\x40\x20\x20\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0b\x00\x00\x00\x1f\x00\x20\x80\x40\x40\x40\x40\x20\x00'\
b'\x18\x00\x07\x00\x00\x80\x40\x40\x40\x40\x20\x80\x1f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\xff\x80\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x40\x40'\
b'\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x40\x20\x80\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00'\
b'\x00\x00\x80\x40\x80\x40\x40\x80\x40\x80\x40\x80\x21\x00\x21\x00'\
b'\x12\x00\x12\x00\x12\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0f\x00\x00\x00\x41\x04\x41\x04\x41\x04\x22\x88\x22\x88'\
b'\x22\x88\x14\x50\x14\x50\x14\x50\x08\x20\x08\x20\x08\x20\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x40\x80\x21\x00\x21\x00'\
b'\x12\x00\x12\x00\x0c\x00\x0c\x00\x12\x00\x12\x00\x21\x00\x21\x00'\
b'\x40\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x40\x40'\
b'\x20\x80\x20\x80\x11\x00\x11\x00\x0a\x00\x0e\x00\x04\x00\x04\x00'\
b'\x04\x00\x04\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00'\
b'\x00\x00\x7f\x80\x01\x00\x03\x00\x02\x00\x04\x00\x0c\x00\x08\x00'\
b'\x10\x00\x30\x00\x20\x00\x40\x00\xff\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x05\x00\x00\x70\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x40\x40\x70\x00\x05\x00\x00\x80\x80\x40\x40\x40\x40\x20\x20'\
b'\x20\x10\x10\x10\x00\x00\x00\x00\x05\x00\x00\xe0\x20\x20\x20\x20'\
b'\x20\x20\x20\x20\x20\x20\x20\x20\x20\xe0\x00\x08\x00\x00\x10\x28'\
b'\x28\x44\x44\x82\x82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x80\x00\x00\x00\x00'\
b'\x00\x00\x06\x00\x80\xc0\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3e'\
b'\x00\x41\x00\x01\x00\x03\x00\x3d\x00\x41\x00\x41\x00\x43\x00\x3d'\
b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x40\x00\x40'\
b'\x00\x40\x00\x5c\x00\x62\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41'\
b'\x00\x62\x00\x5c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00'\
b'\x00\x00\x00\x1c\x22\x41\x40\x40\x40\x41\x22\x1c\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x01\x00\x01\x00\x01\x00\x1d\x00\x23\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x41\x00\x23\x00\x1d\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00'\
b'\x22\x00\x41\x00\x41\x00\x7f\x00\x40\x00\x41\x00\x22\x00\x1c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x18\x20\x20\x78\x20'\
b'\x20\x20\x20\x20\x20\x20\x20\x00\x00\x00\x00\x09\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x1d\x00\x23\x00\x41\x00\x41\x00\x41\x00\x41'\
b'\x00\x41\x00\x23\x00\x1d\x00\x01\x00\x41\x00\x42\x00\x3c\x00\x09'\
b'\x00\x00\x00\x40\x00\x40\x00\x40\x00\x5e\x00\x61\x00\x41\x00\x41'\
b'\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x03\x00\x00\x40\x40\x00\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x40\x00\x00\x00\x00\x05\x00\x00\x20\x20\x00\x20\x20\x20\x20'\
b'\x20\x20\x20\x20\x20\x20\x20\x20\xc0\x08\x00\x00\x80\x80\x80\x84'\
b'\x88\x90\xa0\xe0\x90\x88\x84\x82\x00\x00\x00\x00\x03\x00\x00\x40'\
b'\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x00\x00\x00\x00\x0e'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x2e\x70\x31\x88\x21\x08\x21'\
b'\x08\x21\x08\x21\x08\x21\x08\x21\x08\x21\x08\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x5e\x00\x61'\
b'\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x1c\x00\x22\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x22'\
b'\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x5c\x00\x62\x00\x41\x00\x41\x00\x41\x00\x41'\
b'\x00\x41\x00\x62\x00\x5c\x00\x40\x00\x40\x00\x40\x00\x40\x00\x09'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1d\x00\x23\x00\x41\x00\x41'\
b'\x00\x41\x00\x41\x00\x41\x00\x23\x00\x1d\x00\x01\x00\x01\x00\x01'\
b'\x00\x01\x00\x05\x00\x00\x00\x00\x00\x58\x60\x40\x40\x40\x40\x40'\
b'\x40\x40\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x3c\x42\x42\x60'\
b'\x18\x06\x42\x42\x3c\x00\x00\x00\x00\x05\x00\x00\x00\x20\x20\x78'\
b'\x20\x20\x20\x20\x20\x20\x20\x18\x00\x00\x00\x00\x09\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x43\x00\x3d\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x82\x82\x44\x44\x44\x28\x28\x38\x10\x00'\
b'\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x20\x84'\
b'\x20\x44\x40\x4e\x40\x4a\x40\x2a\x80\x2a\x80\x11\x00\x11\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x82\x44\x44'\
b'\x28\x10\x28\x44\x44\x82\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00'\
b'\x82\x82\x44\x44\x28\x28\x38\x10\x10\x20\x20\xc0\x00\x08\x00\x00'\
b'\x00\x00\x00\x7e\x02\x04\x08\x10\x10\x20\x40\x7e\x00\x00\x00\x00'\
b'\x06\x00\x00\x10\x20\x20\x20\x20\x20\x20\x40\x20\x20\x20\x20\x20'\
b'\x20\x20\x10\x04\x00\x00\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x40\x40\x40\x40\x40\x06\x00\x00\x40\x20\x20\x20\x20\x20\x20'\
b'\x10\x20\x20\x20\x20\x20\x20\x20\x40\x0a\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x80\x47\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

_index =\
b'\x00\x00\x24\x00\x37\x00\x4a\x00\x5d\x00\x81\x00\xa5\x00\xc9\x00'\
b'\xed\x00\x00\x01\x13\x01\x26\x01\x39\x01\x5d\x01\x70\x01\x83\x01'\
b'\x96\x01\xa9\x01\xcd\x01\xf1\x01\x15\x02\x39\x02\x5d\x02\x81\x02'\
b'\xa5\x02\xc9\x02\xed\x02\x11\x03\x24\x03\x37\x03\x5b\x03\x7f\x03'\
b'\xa3\x03\xc7\x03\xfc\x03\x20\x04\x44\x04\x68\x04\x8c\x04\xb0\x04'\
b'\xd4\x04\xf8\x04\x1c\x05\x2f\x05\x42\x05\x66\x05\x8a\x05\xae\x05'\
b'\xd2\x05\xf6\x05\x1a\x06\x3e\x06\x62\x06\x86\x06\xaa\x06\xce\x06'\
b'\xf2\x06\x16\x07\x3a\x07\x5e\x07\x82\x07\x95\x07\xa8\x07\xbb\x07'\
b'\xce\x07\xf2\x07\x05\x08\x29\x08\x4d\x08\x60\x08\x84\x08\xa8\x08'\
b'\xbb\x08\xdf\x08\x03\x09\x16\x09\x29\x09\x3c\x09\x4f\x09\x73\x09'\
b'\x97\x09\xbb\x09\xdf\x09\x03\x0a\x16\x0a\x29\x0a\x3c\x0a\x60\x0a'\
b'\x73\x0a\x97\x0a\xaa\x0a\xbd\x0a\xd0\x0a\xe3\x0a\xf6\x0a\x09\x0b'\
b'\x2d\x0b'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 126 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 17
    return _mvfont[doff + 2:next_offs], 17, width
 
