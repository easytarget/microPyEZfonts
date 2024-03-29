'''
    mPyEZfont_u8g2_ncenR10_e.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenR10.bdf font file was sourced from the U8G2 project:
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
# Font: ncenR10.bdf
# Cmd: micropython-font-to-py/font_to_py.py -x u8g2/tools/font/bdf/ncenR10.bdf 0 tmp_mPyEZfont_u8g2_ncenR10_e.py
version = '0.33'

def height():
    return 15

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
    return 126

_font =\
b'\x06\x00\x00\x70\x98\x88\x08\x10\x20\x20\x20\x00\x20\x20\x00\x00'\
b'\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x03\x00\x00\x40\x40\x40\x40\x40\x40\x40\x40\x00\x40\x40'\
b'\x00\x00\x00\x05\x00\x00\x50\x50\x50\x50\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x08\x00\x00\x12\x12\x12\x7f\x24\x24\x24\xfe\x48'\
b'\x48\x48\x00\x00\x00\x08\x00\x10\x3c\x52\x56\x50\x70\x3c\x0e\x0a'\
b'\x6a\x4a\x3c\x08\x08\x00\x0c\x00\x00\x00\x33\x00\x4d\x00\x8a\x00'\
b'\x8a\x00\x94\x00\x64\xc0\x09\x20\x0a\x20\x12\x20\x12\x40\x21\x80'\
b'\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x0e\x00\x19\x00\x11\x00'\
b'\x1a\x00\x0c\x00\x1c\xf0\x26\x40\x43\x80\x41\x90\x62\xe0\x3c\x60'\
b'\x00\x00\x00\x00\x00\x00\x03\x00\x00\x40\x40\x40\x40\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x10\x20\x40\x40\x80\x80'\
b'\x80\x80\x80\x40\x40\x20\x10\x00\x06\x00\x00\x40\x20\x10\x10\x08'\
b'\x08\x08\x08\x08\x10\x10\x20\x40\x00\x07\x00\x00\x10\x54\x38\x54'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00'\
b'\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\xc0\x40\x40\x80\x00\x05\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x40\x40\x00\x00\x00\x04\x00\x00'\
b'\x10\x10\x10\x20\x20\x20\x40\x40\x40\x80\x80\x00\x00\x00\x08\x00'\
b'\x00\x3c\x66\x42\x42\x42\x42\x42\x42\x42\x66\x3c\x00\x00\x00\x08'\
b'\x00\x00\x10\x70\x10\x10\x10\x10\x10\x10\x10\x10\x7c\x00\x00\x00'\
b'\x08\x00\x00\x3c\x46\x62\x02\x02\x04\x08\x10\x22\x42\x7e\x00\x00'\
b'\x00\x08\x00\x00\x3c\x46\x62\x02\x04\x1c\x06\x02\x62\x46\x3c\x00'\
b'\x00\x00\x08\x00\x00\x0c\x1c\x14\x24\x44\x44\x84\xfe\x04\x04\x0e'\
b'\x00\x00\x00\x08\x00\x00\x7e\x40\x40\x5c\x66\x42\x02\x02\x62\x46'\
b'\x3c\x00\x00\x00\x08\x00\x00\x1c\x22\x46\x40\x5c\x66\x42\x42\x42'\
b'\x66\x3c\x00\x00\x00\x08\x00\x00\x7e\x42\x44\x04\x08\x08\x08\x10'\
b'\x10\x10\x10\x00\x00\x00\x08\x00\x00\x3c\x66\x42\x62\x34\x3c\x46'\
b'\x42\x42\x66\x3c\x00\x00\x00\x08\x00\x00\x3c\x66\x42\x42\x42\x66'\
b'\x3a\x02\x62\x44\x38\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x40'\
b'\x40\x00\x00\x00\x40\x40\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00'\
b'\x40\x40\x00\x00\x00\xc0\x40\x40\x80\x00\x0a\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x01\x80\x06\x00\x18\x00\x60\x00\x18\x00'\
b'\x06\x00\x01\x80\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x00\x00\x00\x00\x7f\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x60\x00\x18\x00\x06\x00\x01\x80\x06\x00'\
b'\x18\x00\x60\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x70\x98\x88'\
b'\x08\x10\x20\x20\x20\x00\x20\x20\x00\x00\x00\x0d\x00\x00\x00\x1f'\
b'\xe0\x20\x10\x46\x90\x89\x90\x90\x90\x91\x10\x91\x10\x93\x30\x8d'\
b'\xc0\x40\x10\x3f\xe0\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x04'\
b'\x00\x04\x00\x0a\x00\x0a\x00\x0a\x00\x11\x00\x11\x00\x3f\x80\x20'\
b'\x80\x20\x80\xfb\xe0\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\xfe'\
b'\x00\x23\x00\x21\x00\x21\x00\x22\x00\x3f\x00\x21\x80\x20\x80\x20'\
b'\x80\x21\x80\xff\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x0f'\
b'\x40\x30\xc0\x20\x40\x60\x40\x40\x00\x40\x00\x40\x00\x60\x40\x20'\
b'\x40\x30\x80\x0f\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\xff'\
b'\x00\x20\x80\x20\xc0\x20\x40\x20\x40\x20\x40\x20\x40\x20\x40\x20'\
b'\xc0\x20\x80\xff\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\xff'\
b'\x80\x20\x80\x20\x80\x24\x00\x24\x00\x3c\x00\x24\x00\x24\x00\x20'\
b'\x80\x20\x80\xff\x80\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\xff'\
b'\x80\x20\x80\x20\x80\x24\x00\x24\x00\x3c\x00\x24\x00\x24\x00\x20'\
b'\x00\x20\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x1e'\
b'\x80\x61\x80\x40\x80\xc0\x80\x80\x00\x80\x00\x87\xc0\xc0\x80\x40'\
b'\x80\x61\x80\x1e\x80\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\xfb'\
b'\xe0\x20\x80\x20\x80\x20\x80\x20\x80\x3f\x80\x20\x80\x20\x80\x20'\
b'\x80\x20\x80\xfb\xe0\x00\x00\x00\x00\x00\x00\x06\x00\x00\xf8\x20'\
b'\x20\x20\x20\x20\x20\x20\x20\x20\xf8\x00\x00\x00\x07\x00\x00\x3e'\
b'\x08\x08\x08\x08\x08\x08\xc8\x88\x88\x70\x00\x00\x00\x0b\x00\x00'\
b'\x00\xfb\xc0\x21\x00\x22\x00\x24\x00\x28\x00\x38\x00\x34\x00\x26'\
b'\x00\x23\x00\x21\x80\xfb\xe0\x00\x00\x00\x00\x00\x00\x0a\x00\x00'\
b'\x00\xf8\x00\x20\x00\x20\x00\x20\x00\x20\x00\x20\x00\x20\x00\x20'\
b'\x00\x20\x80\x20\x80\xff\x80\x00\x00\x00\x00\x00\x00\x10\x00\x00'\
b'\x00\xf0\x1e\x30\x18\x28\x28\x28\x28\x2c\x48\x24\x48\x26\x88\x22'\
b'\x88\x23\x88\x21\x08\xf9\x3e\x00\x00\x00\x00\x00\x00\x0d\x00\x00'\
b'\x00\xe1\xf0\x30\x40\x38\x40\x28\x40\x2c\x40\x26\x40\x23\x40\x21'\
b'\x40\x21\xc0\x20\xc0\xf8\x40\x00\x00\x00\x00\x00\x00\x0b\x00\x00'\
b'\x00\x1e\x00\x61\x80\x40\x80\xc0\xc0\x80\x40\x80\x40\x80\x40\xc0'\
b'\xc0\x40\x80\x61\x80\x1e\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00'\
b'\x00\xff\x00\x21\x80\x20\x80\x20\x80\x21\x00\x3e\x00\x20\x00\x20'\
b'\x00\x20\x00\x20\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00'\
b'\x00\x1e\x00\x61\x80\x40\x80\xc0\xc0\x80\x40\x80\x40\x80\x40\xdc'\
b'\xc0\x62\x80\x63\x80\x1f\x00\x01\x20\x00\xc0\x00\x00\x0b\x00\x00'\
b'\x00\xff\x00\x21\x80\x20\x80\x20\x80\x21\x00\x3e\x00\x23\x00\x21'\
b'\x00\x21\x20\x21\xa0\xf8\xc0\x00\x00\x00\x00\x00\x00\x08\x00\x00'\
b'\x7a\xc6\x82\x82\xe0\x38\x0e\x82\x82\xc6\xbc\x00\x00\x00\x0a\x00'\
b'\x00\x00\xff\x80\x88\x80\x88\x80\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x0d\x00'\
b'\x00\x00\xf9\xf0\x20\x40\x20\x40\x20\x40\x20\x40\x20\x40\x20\x40'\
b'\x20\x40\x20\x40\x30\x80\x1f\x00\x00\x00\x00\x00\x00\x00\x0b\x00'\
b'\x00\x00\xfb\xe0\x20\x80\x30\x80\x11\x00\x11\x00\x19\x00\x0a\x00'\
b'\x0a\x00\x0a\x00\x04\x00\x04\x00\x00\x00\x00\x00\x00\x00\x11\x00'\
b'\x00\x00\x00\xfb\xef\x80\x20\x83\x00\x30\xc2\x00\x11\xc2\x00\x11'\
b'\x44\x00\x19\x64\x00\x0b\x28\x00\x0a\x28\x00\x0e\x38\x00\x06\x10'\
b'\x00\x04\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00'\
b'\x00\xfd\xf0\x30\x40\x18\x80\x0d\x00\x05\x00\x06\x00\x0b\x00\x09'\
b'\x00\x11\x80\x20\xc0\xfb\xf0\x00\x00\x00\x00\x00\x00\x0b\x00\x00'\
b'\x00\xfb\xe0\x60\x80\x31\x00\x11\x00\x1a\x00\x0a\x00\x04\x00\x04'\
b'\x00\x04\x00\x04\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00'\
b'\x00\xff\x00\x83\x00\x86\x00\x0c\x00\x08\x00\x18\x00\x30\x00\x20'\
b'\x00\x61\x00\xc1\x00\xff\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00'\
b'\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xe0\x00\x08\x00'\
b'\x00\x40\x40\x20\x20\x10\x10\x08\x08\x04\x04\x02\x00\x00\x00\x04'\
b'\x00\x00\xe0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\xe0\x00'\
b'\x07\x00\x00\x10\x10\x28\x28\x44\x44\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe'\
b'\x00\x00\x05\x00\x00\x40\x20\x10\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x38\x4c\x04\x3c\xc4\x8c'\
b'\x76\x00\x00\x00\x08\x00\x00\xc0\x40\x40\x40\x5c\x66\x42\x42\x42'\
b'\x66\x5c\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x78\xcc\x80\x80'\
b'\x80\xc4\x78\x00\x00\x00\x08\x00\x00\x0c\x04\x04\x04\x74\xcc\x84'\
b'\x84\x84\xcc\x76\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x78\xcc'\
b'\x84\xfc\x80\xc4\x78\x00\x00\x00\x05\x00\x00\x38\x48\x40\x40\xf0'\
b'\x40\x40\x40\x40\x40\xe0\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00'\
b'\x76\xcc\x84\xcc\x78\x80\x7c\xc6\x82\x7c\x09\x00\x00\x00\xc0\x00'\
b'\x40\x00\x40\x00\x40\x00\x5c\x00\x66\x00\x42\x00\x42\x00\x42\x00'\
b'\x42\x00\xe7\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x40\x40'\
b'\x00\xc0\x40\x40\x40\x40\x40\xe0\x00\x00\x00\x05\x00\x00\x00\x20'\
b'\x20\x00\x60\x20\x20\x20\x20\x20\x20\x20\xa0\xc0\x09\x00\x00\x00'\
b'\xc0\x00\x40\x00\x40\x00\x40\x00\x5e\x00\x48\x00\x50\x00\x78\x00'\
b'\x4c\x00\x46\x00\xef\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\xc0'\
b'\x40\x40\x40\x40\x40\x40\x40\x40\x40\xe0\x00\x00\x00\x0e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xdc\xe0\x67\x30\x42\x10\x42'\
b'\x10\x42\x10\x42\x10\xe7\x38\x00\x00\x00\x00\x00\x00\x09\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xdc\x00\x66\x00\x42\x00\x42'\
b'\x00\x42\x00\x42\x00\xe7\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00'\
b'\x00\x00\x00\x00\x78\xcc\x84\x84\x84\xcc\x78\x00\x00\x00\x08\x00'\
b'\x00\x00\x00\x00\x00\xdc\x66\x42\x42\x42\x66\x5c\x40\x40\xe0\x07'\
b'\x00\x00\x00\x00\x00\x00\x74\xcc\x84\x84\x84\xcc\x74\x04\x04\x0e'\
b'\x07\x00\x00\x00\x00\x00\x00\xdc\x64\x40\x40\x40\x40\xe0\x00\x00'\
b'\x00\x06\x00\x00\x00\x00\x00\x00\x78\x88\xc0\x70\x18\x88\xf0\x00'\
b'\x00\x00\x05\x00\x00\x00\x00\x40\x40\xf0\x40\x40\x40\x40\x48\x30'\
b'\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe7'\
b'\x00\x42\x00\x42\x00\x42\x00\x42\x00\x66\x00\x3b\x00\x00\x00\x00'\
b'\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\xee\x44\x44\x28\x28\x10'\
b'\x10\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\xee\xe0\x44\x40\x44\x40\x2a\x80\x2a\x80\x11\x00\x11\x00\x00\x00'\
b'\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\xce\x64\x38\x10\x38'\
b'\x4c\xe6\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\xee\x44\x44\x28'\
b'\x28\x10\x10\x20\xa0\xc0\x07\x00\x00\x00\x00\x00\x00\xfc\x8c\x98'\
b'\x30\x64\xc4\xfc\x00\x00\x00\x04\x00\x00\x20\x40\x40\x40\x40\x40'\
b'\x80\x40\x40\x40\x40\x40\x20\x00\x09\x00\x00\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x40\x20\x20\x20\x20'\
b'\x20\x10\x20\x20\x20\x20\x20\x40\x00\x09\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x39\x00\x46\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'

_index =\
b'\x00\x00\x11\x00\x22\x00\x33\x00\x44\x00\x55\x00\x66\x00\x86\x00'\
b'\xa6\x00\xb7\x00\xc8\x00\xd9\x00\xea\x00\x0a\x01\x1b\x01\x2c\x01'\
b'\x3d\x01\x4e\x01\x5f\x01\x70\x01\x81\x01\x92\x01\xa3\x01\xb4\x01'\
b'\xc5\x01\xd6\x01\xe7\x01\xf8\x01\x09\x02\x1a\x02\x3a\x02\x5a\x02'\
b'\x7a\x02\x8b\x02\xab\x02\xcb\x02\xeb\x02\x0b\x03\x2b\x03\x4b\x03'\
b'\x6b\x03\x8b\x03\xab\x03\xbc\x03\xcd\x03\xed\x03\x0d\x04\x2d\x04'\
b'\x4d\x04\x6d\x04\x8d\x04\xad\x04\xcd\x04\xde\x04\xfe\x04\x1e\x05'\
b'\x3e\x05\x6d\x05\x8d\x05\xad\x05\xcd\x05\xde\x05\xef\x05\x00\x06'\
b'\x11\x06\x22\x06\x33\x06\x44\x06\x55\x06\x66\x06\x77\x06\x88\x06'\
b'\x99\x06\xaa\x06\xca\x06\xdb\x06\xec\x06\x0c\x07\x1d\x07\x3d\x07'\
b'\x5d\x07\x6e\x07\x7f\x07\x90\x07\xa1\x07\xb2\x07\xc3\x07\xe3\x07'\
b'\xf4\x07\x14\x08\x25\x08\x36\x08\x47\x08\x58\x08\x78\x08\x89\x08'\
b'\xa9\x08'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 126 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 15
    return _mvfont[doff + 2:next_offs], 15, width
 
