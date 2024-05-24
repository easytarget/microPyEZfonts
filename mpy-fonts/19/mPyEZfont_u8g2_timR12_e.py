'''
    mPyEZfont_u8g2_timR12_e.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original timR12.bdf font file was sourced from the U8G2 project:
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
# Font: timR12.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -l 255 -e 32 ../u8g2/tools/font/bdf/timR12.bdf 0 tmp_mPyEZfont_u8g2_timR12_e.py
version = '0.33'

def height():
    return 19

def baseline():
    return 15

def max_width():
    return 16

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 255

_font =\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x20\x20\x20\x20\x20\x20\x20\x00\x00\x20'\
b'\x20\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x48\x48'\
b'\x48\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x12\x12\x12\x7f\x24\x24\xfe\x48\x48\x48'\
b'\x48\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x10\x7c\x92'\
b'\x92\x90\x50\x38\x14\x12\x92\x92\x7c\x10\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x80\x27\x80\x45\x80'\
b'\x45\x00\x4b\x00\x32\x70\x06\x90\x05\x10\x0d\x10\x09\x20\x08\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x12\x00\x12\x00\x12\x00\x0c\xe0\x38\x40\x44\x80'\
b'\x83\x00\x82\x10\x45\x20\x38\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\x00\x40\x40\x40\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x10\x20'\
b'\x40\x40\x80\x80\x80\x80\x80\x80\x40\x40\x20\x10\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x80\x40\x20\x20\x10\x10\x10\x10\x10\x10'\
b'\x20\x20\x40\x80\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x10\x54'\
b'\x38\x38\x54\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x20\x20\x40\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x40\x40\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x08\x08\x08\x10\x10\x20\x20\x20\x40\x40'\
b'\x40\x80\x80\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x38\x44'\
b'\x44\x82\x82\x82\x82\x82\x44\x44\x38\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x10\x30\x50\x10\x10\x10\x10\x10\x10\x10'\
b'\x38\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x38\x44'\
b'\x82\x02\x02\x04\x08\x10\x20\x42\xfc\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x38\x44\x84\x08\x10\x38\x04\x02\x02\xc4'\
b'\x78\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x02\x00\x06\x00\x0a\x00\x0a\x00\x12\x00\x22\x00\x22\x00'\
b'\x42\x00\xff\x00\x02\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x3e\x20\x20\x40\x78\x04\x02\x02\x02\x8c'\
b'\x70\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x0e\x30'\
b'\x40\x40\x98\xe4\x82\x82\x82\x44\x38\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\xfe\x82\x84\x04\x08\x08\x10\x10\x10\x20'\
b'\x20\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x30\x48'\
b'\x84\x84\x48\x30\x48\x84\x84\x48\x30\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x38\x44\x82\x82\x82\x46\x3a\x04\x04\x18'\
b'\xe0\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x40\x40\x00\x00\x00\x00\x40\x40\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x40\x40\x00\x00\x00\x00\x40'\
b'\x40\x80\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x00\x10\x00\x60\x00\x80\x00'\
b'\x60\x00\x10\x00\x0c\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\xfe\x00\x00\x00\x00\x00\xfe\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x60\x00\x18\x00\x04\x00\x03\x00\x00\x80'\
b'\x03\x00\x04\x00\x18\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x38\x44\x44\x04\x08\x10\x10\x00\x00\x10'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x07\xc0\x18\x30\x20\x08\x41\xa8\x46\x64\x84\x44\x88\x44'\
b'\x88\x44\x88\xc8\x89\x48\x46\x30\x20\x00\x18\x30\x07\xc0\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x06\x00\x0a\x00'\
b'\x0b\x00\x11\x00\x11\x80\x20\x80\x3f\x80\x40\xc0\x40\x40\xe0\xf0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7e\x00\x23\x00\x21\x00\x21\x00\x22\x00\x3e\x00\x23\x00'\
b'\x20\x80\x20\x80\x21\x80\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x40\x60\xc0\x40\x40'\
b'\x80\x40\x80\x00\x80\x00\x80\x00\x80\x00\x40\x40\x61\x80\x1e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xfc\x00\x43\x00\x40\x80\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x40\x40\x80\x43\x00\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x41\x00\x40\x00'\
b'\x40\x00\x42\x00\x7e\x00\x42\x00\x40\x00\x40\x00\x40\x80\xff\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\x00\x41\x00\x40\x00\x40\x00\x42\x00\x7e\x00\x42\x00'\
b'\x40\x00\x40\x00\x40\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x40\x30\xc0\x40\x40'\
b'\x80\x00\x80\x00\x81\xe0\x80\x40\x80\x40\x40\x40\x30\xc0\x0f\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xe1\xc0\x40\x80\x40\x80\x40\x80\x40\x80\x7f\x80\x40\x80'\
b'\x40\x80\x40\x80\x40\x80\xe1\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\xe0\x40\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\xe0\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x38\x10'\
b'\x10\x10\x10\x10\x10\x10\x90\x90\x60\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x79\xe0\x20\x80\x21\x00'\
b'\x22\x00\x24\x00\x38\x00\x24\x00\x22\x00\x21\x00\x20\x80\x79\xe0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xe0\x00\x40\x00\x40\x00\x40\x00\x40\x00\x40\x00\x40\x00'\
b'\x40\x00\x40\x00\x41\x00\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x38\x60\x30\x50\x50'\
b'\x50\x50\x48\x90\x48\x90\x48\x90\x45\x10\x45\x10\x42\x10\xe2\x38'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xe1\xc0\x60\x80\x50\x80\x50\x80\x48\x80\x48\x80\x44\x80'\
b'\x42\x80\x42\x80\x41\x80\xf0\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x31\x80\x20\x80'\
b'\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x20\x80\x31\x80\x0e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xfc\x00\x42\x00\x41\x00\x41\x00\x42\x00\x7c\x00\x40\x00'\
b'\x40\x00\x40\x00\x40\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x31\x80\x20\x80'\
b'\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x20\x80\x31\x80\x1e\x00'\
b'\x06\x00\x03\x00\x00\xe0\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xfc\x00\x42\x00\x41\x00\x41\x00\x42\x00\x7c\x00\x48\x00'\
b'\x44\x00\x42\x00\x41\x00\xe1\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3a\x00\x46\x00\x82\x00'\
b'\x80\x00\x60\x00\x1c\x00\x02\x00\x01\x00\x81\x00\xc2\x00\xbc\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\x80\x88\x80\x88\x80\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xc0\x40\x80\x40\x80'\
b'\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80\x21\x00\x1e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xe0\xe0\x40\x40\x20\x80\x20\x80\x11\x00\x11\x00\x11\x00'\
b'\x0a\x00\x0a\x00\x04\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe7\x0e\x42\x04\x21\x08'\
b'\x21\x08\x11\x88\x12\x90\x12\x90\x0a\x50\x0a\x50\x04\x20\x04\x20'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xe0\xe0\x40\x40\x20\x80\x11\x00\x0a\x00\x04\x00\x0a\x00'\
b'\x11\x00\x20\x80\x40\x40\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0\x40\x40\x20\x80'\
b'\x11\x00\x11\x00\x0a\x00\x04\x00\x04\x00\x04\x00\x04\x00\x0e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\x80\x81\x00\x82\x00\x04\x00\x04\x00\x08\x00\x10\x00'\
b'\x20\x00\x20\x00\x40\x80\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x70\x40\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x40\x40\x70\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x80\x40'\
b'\x40\x20\x20\x10\x10\x08\x08\x04\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\xe0\x20\x20\x20\x20\x20\x20\x20\x20\x20'\
b'\x20\x20\x20\xe0\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x10\x28'\
b'\x28\x44\x44\x82\x82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xff\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x40\x20'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x38\x44\x44\x1c\x64\x44\x4d'\
b'\x36\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x40\xc0'\
b'\x40\x5c\x64\x42\x42\x42\x42\x64\x38\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x38\x44\x84\x80\x80\x80\x44'\
b'\x38\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x04\x0c'\
b'\x04\x34\x4c\x84\x84\x84\x84\x4e\x34\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x38\x44\x84\xfc\x80\x80\x44'\
b'\x38\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x18\x24'\
b'\x20\x20\x78\x20\x20\x20\x20\x20\x78\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x36\x4c\x84\x84\x48\x70\x80'\
b'\x7c\x82\x82\xc4\x78\x00\x00\x00\x08\x00\x00\x00\x00\x00\x40\xc0'\
b'\x40\x5c\x66\x42\x42\x42\x42\x42\xe7\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x20\x20\x00\x20\x60\x20\x20\x20\x20\x20'\
b'\x70\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x20\x20'\
b'\x00\x20\x60\x20\x20\x20\x20\x20\x20\x20\x20\xa0\xc0\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x20\x60\x20\x2e\x24\x28\x30\x28\x24\x22'\
b'\x77\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x20\x60'\
b'\x20\x20\x20\x20\x20\x20\x20\x20\x70\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x2c\xc0\x73\x20\x22\x20\x22\x20\x22\x20\x22\x20\x22\x20\x77\x70'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x5c\xe6\x42\x42\x42\x42\x42\xe7\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x38\x44\x82\x82\x82\x82\x44'\
b'\x38\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x5c\xe6\x42\x42\x42\x42\x62\x5c\x40\x40\x40\xe0\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x3a\x66\x42\x42\x42\x42\x66'\
b'\x3a\x02\x02\x02\x07\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x58\xe8\x40\x40\x40\x40\x40\xe0\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x78\x88\x80\x70\x08\x88\xc8'\
b'\xb0\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x40'\
b'\x40\xf0\x40\x40\x40\x40\x40\x50\x20\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\xc6\x42\x42\x42\x42\x42\x47'\
b'\x3a\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xe7\x42\x42\x24\x24\x14\x18\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\xee\x70\x44\x20\x44\x20\x22\x40\x22\x40\x15\x40\x08\x80\x08\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xee\x44\x28\x10\x28\x28\x44\xee\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\xf7\x42\x42\x24\x24\x14\x08'\
b'\x08\x10\x10\xa0\xc0\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xfc\x84\x08\x10\x20\x40\x84\xfc\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x0c\x10\x10\x10\x10\x10\x20\x10\x10\x10'\
b'\x10\x10\x10\x0c\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x80\x80'\
b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\xc0\x20\x20\x20\x20\x20\x10\x20\x20\x20'\
b'\x20\x20\x20\xc0\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x71\x00\x99\x00'\
b'\x8e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x20\x20\x00\x00\x20\x20\x20'\
b'\x20\x20\x20\x20\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x04'\
b'\x04\x3c\x4a\x8a\x88\x90\x92\x54\x38\x20\x20\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x0c\x12\x22\x20\x20\xfc\x10\x10\x71\x91'\
b'\x6e\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x99'\
b'\x66\x42\x81\x81\x81\x42\x66\x99\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe3\x80\x41\x00\x22\x00'\
b'\x14\x00\x08\x00\x3e\x00\x08\x00\x3e\x00\x08\x00\x08\x00\x1c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x80\x80'\
b'\x80\x80\x80\x00\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x38\x44\x4c\x20\x50\x88\x84\x42\x22\x14'\
b'\x08\x64\x44\x38\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x48\x48'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x31\x80\x40\x40'\
b'\x4e\x40\x91\x20\x90\x20\x90\x20\x51\x40\x4e\x40\x31\x80\x0e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x60\x10'\
b'\x70\x90\x50\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x24\x48\x90\x48\x24'\
b'\x12\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00'\
b'\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0e\x00\x31\x80\x40\x40\x4e\x40\x89\x20\x8e\x20\x8a\x20'\
b'\x4a\x40\x49\x40\x31\x80\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x38\x44'\
b'\x44\x44\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'\
b'\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00\x00\x00\x7f\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x70\x88'\
b'\x08\x10\x20\x48\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x38\x44\x04\x18\x04\x84\x78\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x08\x10'\
b'\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\xc6\x42\x42\x42\x42\x42\x47'\
b'\x7a\x40\x40\x40\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x3e\x74'\
b'\xf4\xf4\xf4\x74\x34\x14\x14\x14\x14\x14\x14\x14\x14\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x40\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x70\x10\xe0\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x20\x60\x20\x20\x20\x20\x70\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x60\x90'\
b'\x90\x90\x60\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x48\x24\x12\x24\x48'\
b'\x90\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x20\x40\x60\x80\x21\x80\x21\x00\x22\x20\x26\x60\x74\xa0'\
b'\x0c\xa0\x09\x20\x13\xf0\x20\x20\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x80\xc1\x00\x43\x00'\
b'\x42\x00\x44\xe0\x4d\x10\xe8\x10\x18\x20\x10\x40\x20\x90\x41\xf0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x38\x20\x44\x40\x04\xc0\x18\x80\x05\x10\x87\x30\x7a\x50'\
b'\x06\x50\x04\x90\x09\xf8\x08\x10\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x10\x10\x00\x00\x10\x10\x20'\
b'\x40\x44\x44\x38\x00\x00\x00\x00\x0c\x00\x08\x00\x04\x00\x02\x00'\
b'\x00\x00\x04\x00\x06\x00\x0a\x00\x0b\x00\x11\x00\x11\x80\x20\x80'\
b'\x3f\x80\x40\xc0\x40\x40\xe0\xf0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x01\x00\x02\x00\x04\x00\x00\x00\x04\x00\x06\x00\x0a\x00'\
b'\x0b\x00\x11\x00\x11\x80\x20\x80\x3f\x80\x40\xc0\x40\x40\xe0\xf0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x04\x00\x0a\x00\x11\x00'\
b'\x00\x00\x04\x00\x06\x00\x0a\x00\x0b\x00\x11\x00\x11\x80\x20\x80'\
b'\x3f\x80\x40\xc0\x40\x40\xe0\xf0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x0d\x00\x16\x00\x00\x00\x04\x00\x06\x00\x0a\x00'\
b'\x0b\x00\x11\x00\x11\x80\x20\x80\x3f\x80\x40\xc0\x40\x40\xe0\xf0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x09\x00\x09\x00'\
b'\x00\x00\x04\x00\x06\x00\x0a\x00\x0b\x00\x11\x00\x11\x80\x20\x80'\
b'\x3f\x80\x40\xc0\x40\x40\xe0\xf0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x06\x00\x09\x00\x09\x00\x06\x00\x06\x00\x0a\x00'\
b'\x0b\x00\x11\x00\x11\x80\x20\x80\x3f\x80\x40\xc0\x40\x40\xe0\xf0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x07\xf8\x03\x08\x05\x08\x09\x00\x09\x10\x11\xf0\x1f\x10'\
b'\x21\x00\x21\x00\x41\x04\xf3\xf8\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x40\x30\xc0\x40\x40'\
b'\x80\x40\x80\x00\x80\x00\x80\x00\x80\x00\x40\x40\x31\x80\x0e\x00'\
b'\x04\x00\x0e\x00\x02\x00\x1c\x00\x0a\x00\x20\x00\x10\x00\x08\x00'\
b'\x00\x00\xff\x00\x41\x00\x40\x00\x40\x00\x42\x00\x7e\x00\x42\x00'\
b'\x40\x00\x40\x00\x40\x80\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x02\x00\x04\x00\x08\x00\x00\x00\xff\x00\x41\x00\x41\x00'\
b'\x40\x00\x42\x00\x7e\x00\x42\x00\x40\x00\x40\x00\x40\x80\xff\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x08\x00\x14\x00\x22\x00'\
b'\x00\x00\xff\x00\x41\x00\x40\x00\x40\x00\x42\x00\x7e\x00\x42\x00'\
b'\x40\x00\x40\x00\x40\x80\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x24\x00\x24\x00\x00\x00\xff\x00\x41\x00\x40\x00'\
b'\x40\x00\x42\x00\x7e\x00\x42\x00\x40\x00\x40\x00\x40\x80\xff\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x80\x40\x20\x00\x70\x20'\
b'\x20\x20\x20\x20\x20\x20\x20\x20\x70\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x08\x10\x20\x00\xe0\x40\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\xe0\x00\x00\x00\x00\x00\x00\x00\x06\x00\x20\x50\x88\x00\x70\x20'\
b'\x20\x20\x20\x20\x20\x20\x20\x20\x70\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\xa0\xa0\x00\xe0\x40\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\xe0\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7e\x00\x21\x80\x20\x40\x20\x20\x20\x20\x7c\x20\x20\x20'\
b'\x20\x20\x20\x40\x21\x80\x7e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x0d\x00\x16\x00\x00\x00\xe1\xc0\x60\x80\x50\x80'\
b'\x50\x80\x48\x80\x48\x80\x44\x80\x42\x80\x42\x80\x41\x80\xf0\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x10\x00\x08\x00\x04\x00'\
b'\x00\x00\x0e\x00\x31\x80\x20\x80\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x40\x20\x80\x31\x80\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x01\x00\x02\x00\x04\x00\x00\x00\x0e\x00\x31\x80\x20\x80'\
b'\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x20\x80\x31\x80\x0e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x04\x00\x0a\x00\x11\x00'\
b'\x00\x00\x0e\x00\x31\x80\x20\x80\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x40\x20\x80\x31\x80\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x0d\x00\x16\x00\x00\x00\x0e\x00\x31\x80\x20\x80'\
b'\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x20\x80\x31\x80\x0e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x11\x00\x11\x00'\
b'\x00\x00\x0e\x00\x31\x80\x20\x80\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x40\x20\x80\x31\x80\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x41\x00\x22\x00\x14\x00\x08\x00\x14\x00\x22\x00\x41\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x40\x0e\x40\x31\x80\x41\x40\x82\x20\x84\x20\x84\x20\x88\x20'\
b'\x90\x20\x50\x40\x31\x80\x4e\x00\x40\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x10\x00\x08\x00\x04\x00\x00\x00\xe1\xc0\x40\x80\x40\x80'\
b'\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80\x21\x00\x1e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x01\x00\x02\x00\x04\x00'\
b'\x00\x00\xe1\xc0\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80'\
b'\x40\x80\x40\x80\x21\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x04\x00\x0a\x00\x11\x00\x00\x00\xe1\xc0\x40\x80\x40\x80'\
b'\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80\x21\x00\x1e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x12\x00\x12\x00'\
b'\x00\x00\xe1\xc0\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80\x40\x80'\
b'\x40\x80\x40\x80\x21\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x80\x01\x00\x02\x00\x00\x00\xe0\xe0\x40\x40\x20\x80'\
b'\x11\x00\x11\x00\x0a\x00\x04\x00\x04\x00\x04\x00\x04\x00\x0e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xe0\x00\x40\x00\x7c\x00\x42\x00\x41\x00\x41\x00\x42\x00'\
b'\x7c\x00\x40\x00\x40\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x38\x44\x44\x44\x48\x58\x44\x42\x42\x52'\
b'\xcc\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x20\x10\x08'\
b'\x00\x38\x44\x44\x1c\x64\x44\x4d\x32\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x04\x08\x10\x00\x38\x44\x44\x1c\x64\x44\x4d'\
b'\x32\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x10\x28\x44'\
b'\x00\x38\x44\x44\x1c\x64\x44\x4d\x32\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x34\x58\x00\x38\x44\x44\x1c\x64\x44\x4d'\
b'\x32\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x24\x24'\
b'\x00\x38\x44\x44\x1c\x64\x44\x4d\x32\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x10\x28\x28\x10\x38\x44\x44\x1c\x64\x44\x4d'\
b'\x32\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x39\x80\x46\x40\x44\x40\x1f\xc0'\
b'\x64\x00\x44\x00\x4e\x40\x31\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x38\x44\x84\x80\x80\x80\x44'\
b'\x38\x10\x38\x08\x70\x00\x00\x00\x07\x00\x00\x00\x00\x40\x20\x10'\
b'\x00\x38\x44\x84\xfc\x80\x80\x44\x38\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x04\x08\x10\x00\x38\x44\x84\xfc\x80\x80\x44'\
b'\x38\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x10\x28\x44'\
b'\x00\x38\x44\x84\xfc\x80\x80\x44\x38\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x48\x48\x00\x38\x44\x84\xfc\x80\x80\x44'\
b'\x38\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x80\x40\x20'\
b'\x00\x40\xc0\x40\x40\x40\x40\x40\xe0\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x20\x40\x80\x00\x40\xc0\x40\x40\x40\x40\x40'\
b'\xe0\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x20\x50\x88'\
b'\x00\x20\x60\x20\x20\x20\x20\x20\x70\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\xa0\xa0\x00\x40\xc0\x40\x40\x40\x40\x40'\
b'\xe0\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x6c\x30'\
b'\xc8\x3c\x44\x82\x82\x82\x82\x44\x38\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x34\x00\x58\x00\x00\x00'\
b'\x5c\x00\xe6\x00\x42\x00\x42\x00\x42\x00\x42\x00\x42\x00\xe7\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x20\x10\x08'\
b'\x00\x38\x44\x82\x82\x82\x82\x44\x38\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x04\x08\x10\x00\x38\x44\x82\x82\x82\x82\x44'\
b'\x38\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x10\x28\x44'\
b'\x00\x38\x44\x82\x82\x82\x82\x44\x38\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x34\x58\x00\x38\x44\x82\x82\x82\x82\x44'\
b'\x38\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x48\x48'\
b'\x00\x38\x44\x82\x82\x82\x82\x44\x38\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'\
b'\x08\x00\x00\x00\x00\x00\xff\x80\x00\x00\x00\x00\x08\x00\x08\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x02'\
b'\x02\x3c\x44\x8a\x92\x92\xa2\x64\x38\x40\x40\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x20\x00\x10\x00\x08\x00\x00\x00'\
b'\xc6\x00\x42\x00\x42\x00\x42\x00\x42\x00\x42\x00\x46\x00\x3b\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x08\x00\x10\x00\x00\x00\xc6\x00\x42\x00\x42\x00\x42\x00'\
b'\x42\x00\x42\x00\x46\x00\x3b\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x10\x00\x28\x00\x44\x00\x00\x00'\
b'\xc6\x00\x42\x00\x42\x00\x42\x00\x42\x00\x42\x00\x46\x00\x3b\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x24\x00\x24\x00\x00\x00\xc6\x00\x42\x00\x42\x00\x42\x00'\
b'\x42\x00\x42\x00\x46\x00\x3b\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x02\x00\x04\x00\x08\x00\x00\x00'\
b'\xf7\x00\x42\x00\x42\x00\x24\x00\x24\x00\x14\x00\x08\x00\x08\x00'\
b'\x10\x00\x10\x00\xa0\x00\xc0\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x40\x00\xc0\x00\x40\x00\x5c\x00\x62\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x62\x00\x5c\x00\x40\x00\x40\x00\x40\x00\xe0\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x24\x00\x24\x00\x00\x00'\
b'\xf7\x00\x42\x00\x62\x00\x24\x00\x34\x00\x14\x00\x18\x00\x08\x00'\
b'\x10\x00\x10\x00\xa0\x00\xc0\x00'

_sparse =\
b'\x20\x00\x03\x00\x21\x00\x06\x00\x22\x00\x09\x00\x23\x00\x0c\x00'\
b'\x24\x00\x0f\x00\x25\x00\x12\x00\x26\x00\x17\x00\x27\x00\x1c\x00'\
b'\x28\x00\x1f\x00\x29\x00\x22\x00\x2a\x00\x25\x00\x2b\x00\x28\x00'\
b'\x2c\x00\x2d\x00\x2d\x00\x30\x00\x2e\x00\x33\x00\x2f\x00\x36\x00'\
b'\x30\x00\x39\x00\x31\x00\x3c\x00\x32\x00\x3f\x00\x33\x00\x42\x00'\
b'\x34\x00\x45\x00\x35\x00\x4a\x00\x36\x00\x4d\x00\x37\x00\x50\x00'\
b'\x38\x00\x53\x00\x39\x00\x56\x00\x3a\x00\x59\x00\x3b\x00\x5c\x00'\
b'\x3c\x00\x5f\x00\x3d\x00\x64\x00\x3e\x00\x69\x00\x3f\x00\x6e\x00'\
b'\x40\x00\x71\x00\x41\x00\x76\x00\x42\x00\x7b\x00\x43\x00\x80\x00'\
b'\x44\x00\x85\x00\x45\x00\x8a\x00\x46\x00\x8f\x00\x47\x00\x94\x00'\
b'\x48\x00\x99\x00\x49\x00\x9e\x00\x4a\x00\xa1\x00\x4b\x00\xa4\x00'\
b'\x4c\x00\xa9\x00\x4d\x00\xae\x00\x4e\x00\xb3\x00\x4f\x00\xb8\x00'\
b'\x50\x00\xbd\x00\x51\x00\xc2\x00\x52\x00\xc7\x00\x53\x00\xcc\x00'\
b'\x54\x00\xd1\x00\x55\x00\xd6\x00\x56\x00\xdb\x00\x57\x00\xe0\x00'\
b'\x58\x00\xe5\x00\x59\x00\xea\x00\x5a\x00\xef\x00\x5b\x00\xf4\x00'\
b'\x5c\x00\xf7\x00\x5d\x00\xfa\x00\x5e\x00\xfd\x00\x5f\x00\x00\x01'\
b'\x60\x00\x03\x01\x61\x00\x06\x01\x62\x00\x09\x01\x63\x00\x0c\x01'\
b'\x64\x00\x0f\x01\x65\x00\x12\x01\x66\x00\x15\x01\x67\x00\x18\x01'\
b'\x68\x00\x1b\x01\x69\x00\x1e\x01\x6a\x00\x21\x01\x6b\x00\x24\x01'\
b'\x6c\x00\x27\x01\x6d\x00\x2a\x01\x6e\x00\x2f\x01\x6f\x00\x32\x01'\
b'\x70\x00\x35\x01\x71\x00\x38\x01\x72\x00\x3b\x01\x73\x00\x3e\x01'\
b'\x74\x00\x41\x01\x75\x00\x44\x01\x76\x00\x47\x01\x77\x00\x4a\x01'\
b'\x78\x00\x4f\x01\x79\x00\x52\x01\x7a\x00\x55\x01\x7b\x00\x58\x01'\
b'\x7c\x00\x5b\x01\x7d\x00\x5e\x01\x7e\x00\x61\x01\x7f\x00\x66\x01'\
b'\x80\x00\x67\x01\x81\x00\x68\x01\x82\x00\x69\x01\x83\x00\x6a\x01'\
b'\x84\x00\x6b\x01\x85\x00\x6c\x01\x86\x00\x6d\x01\x87\x00\x6e\x01'\
b'\x88\x00\x6f\x01\x89\x00\x70\x01\x8a\x00\x71\x01\x8b\x00\x72\x01'\
b'\x8c\x00\x73\x01\x8d\x00\x74\x01\x8e\x00\x75\x01\x8f\x00\x76\x01'\
b'\x90\x00\x77\x01\x91\x00\x78\x01\x92\x00\x79\x01\x93\x00\x7a\x01'\
b'\x94\x00\x7b\x01\x95\x00\x7c\x01\x96\x00\x7d\x01\x97\x00\x7e\x01'\
b'\x98\x00\x7f\x01\x99\x00\x80\x01\x9a\x00\x81\x01\x9b\x00\x82\x01'\
b'\x9c\x00\x83\x01\x9d\x00\x84\x01\x9e\x00\x85\x01\x9f\x00\x86\x01'\
b'\xa0\x00\x87\x01\xa1\x00\x8a\x01\xa2\x00\x8d\x01\xa3\x00\x90\x01'\
b'\xa4\x00\x93\x01\xa5\x00\x96\x01\xa6\x00\x9b\x01\xa7\x00\x9e\x01'\
b'\xa8\x00\xa1\x01\xa9\x00\xa4\x01\xaa\x00\xa9\x01\xab\x00\xac\x01'\
b'\xac\x00\xaf\x01\xad\x00\xb4\x01\xae\x00\xb7\x01\xaf\x00\xbc\x01'\
b'\xb0\x00\xbf\x01\xb1\x00\xc2\x01\xb2\x00\xc7\x01\xb3\x00\xca\x01'\
b'\xb4\x00\xcd\x01\xb5\x00\xd0\x01\xb6\x00\xd3\x01\xb7\x00\xd6\x01'\
b'\xb8\x00\xd9\x01\xb9\x00\xdc\x01\xba\x00\xdf\x01\xbb\x00\xe2\x01'\
b'\xbc\x00\xe5\x01\xbd\x00\xea\x01\xbe\x00\xef\x01\xbf\x00\xf4\x01'\
b'\xc0\x00\xf7\x01\xc1\x00\xfc\x01\xc2\x00\x01\x02\xc3\x00\x06\x02'\
b'\xc4\x00\x0b\x02\xc5\x00\x10\x02\xc6\x00\x15\x02\xc7\x00\x1a\x02'\
b'\xc8\x00\x1f\x02\xc9\x00\x24\x02\xca\x00\x29\x02\xcb\x00\x2e\x02'\
b'\xcc\x00\x33\x02\xcd\x00\x36\x02\xce\x00\x39\x02\xcf\x00\x3c\x02'\
b'\xd0\x00\x3f\x02\xd1\x00\x44\x02\xd2\x00\x49\x02\xd3\x00\x4e\x02'\
b'\xd4\x00\x53\x02\xd5\x00\x58\x02\xd6\x00\x5d\x02\xd7\x00\x62\x02'\
b'\xd8\x00\x67\x02\xd9\x00\x6c\x02\xda\x00\x71\x02\xdb\x00\x76\x02'\
b'\xdc\x00\x7b\x02\xdd\x00\x80\x02\xde\x00\x85\x02\xdf\x00\x8a\x02'\
b'\xe0\x00\x8d\x02\xe1\x00\x90\x02\xe2\x00\x93\x02\xe3\x00\x96\x02'\
b'\xe4\x00\x99\x02\xe5\x00\x9c\x02\xe6\x00\x9f\x02\xe7\x00\xa4\x02'\
b'\xe8\x00\xa7\x02\xe9\x00\xaa\x02\xea\x00\xad\x02\xeb\x00\xb0\x02'\
b'\xec\x00\xb3\x02\xed\x00\xb6\x02\xee\x00\xb9\x02\xef\x00\xbc\x02'\
b'\xf0\x00\xbf\x02\xf1\x00\xc2\x02\xf2\x00\xc7\x02\xf3\x00\xca\x02'\
b'\xf4\x00\xcd\x02\xf5\x00\xd0\x02\xf6\x00\xd3\x02\xf7\x00\xd6\x02'\
b'\xf8\x00\xdb\x02\xf9\x00\xde\x02\xfa\x00\xe3\x02\xfb\x00\xe8\x02'\
b'\xfc\x00\xed\x02\xfd\x00\xf2\x02\xfe\x00\xf7\x02\xff\x00\xfc\x02'\

_mvfont = memoryview(_font)
_mvsp = memoryview(_sparse)
ifb = lambda l : l[0] | (l[1] << 8)

def bs(lst, val):
    while True:
        m = (len(lst) & ~ 7) >> 1
        v = ifb(lst[m:])
        if v == val:
            return ifb(lst[m + 2:])
        if not m:
            return 0
        lst = lst[m:] if v < val else lst[:m]

def get_ch(ch):
    doff = bs(_mvsp, ord(ch)) << 3
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 19
    return _mvfont[doff + 2:next_offs], 19, width
 
