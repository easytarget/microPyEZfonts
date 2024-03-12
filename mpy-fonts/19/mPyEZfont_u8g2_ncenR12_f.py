'''
    mPyEZfont_u8g2_ncenR12_f.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenR12.bdf font file was sourced from the U8G2 project:
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
# Font: ncenR12.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/f-char.set u8g2/tools/font/bdf/ncenR12.bdf 0 tmp_mPyEZfont_u8g2_ncenR12_f.py
version = '0.33'

def height():
    return 19

def baseline():
    return 16

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
    return 255

_font =\
b'\x07\x00\x00\x00\x00\x00\x38\x4c\xe6\x46\x06\x0c\x18\x10\x10\x00'\
b'\x30\x30\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x60\x60\x60\x60\x60\x40\x40\x40\x40\x00'\
b'\x60\x60\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x48\x48'\
b'\x48\x48\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x12\x00\x12\x00'\
b'\x12\x00\x7f\x00\x24\x00\x24\x00\xfe\x00\x48\x00\x48\x00\x48\x00'\
b'\x48\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x08\x00\x1e\x00\x29\x00\x4b\x00\x4b\x00\x78\x00\x3e\x00'\
b'\x0f\x00\x69\x00\x69\x00\x4a\x00\x3c\x00\x08\x00\x08\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x40\x33\xc0\x22\x80'\
b'\x62\x80\x45\x00\x45\x70\x3a\xc8\x02\x88\x05\x88\x05\x10\x09\x10'\
b'\x08\xe0\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1e\x00\x33\x00\x31\x00\x33\x00\x1a\x00\x1c\xf0\x2c\x60'\
b'\x66\x40\xc6\x80\xc3\x90\xe7\x90\x7c\xe0\x00\x00\x00\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\x00\x40\x40\x40\x40\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x08\x10'\
b'\x20\x20\x40\x40\x40\x40\x40\x40\x20\x20\x10\x08\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x80\x40\x20\x20\x10\x10\x10\x10\x10\x10'\
b'\x20\x20\x40\x80\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x10\x54'\
b'\xd6\x38\xd6\x54\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x20\x20\x40\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x08\x08\x10\x10\x10\x20\x20\x40\x40\x40'\
b'\x80\x80\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x3c\x00\x66\x00\x42\x00\xc3\x00\xc3\x00\xc3\x00\xc3\x00'\
b'\xc3\x00\xc3\x00\x42\x00\x66\x00\x3c\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x78\x00\x18\x00'\
b'\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00'\
b'\x7e\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1c\x00\x22\x00\x43\x00\x63\x00\x63\x00\x06\x00\x04\x00'\
b'\x08\x00\x11\x00\x21\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x46\x00\x63\x00'\
b'\x63\x00\x06\x00\x1c\x00\x06\x00\x03\x00\x63\x00\x63\x00\x46\x00'\
b'\x3c\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x04\x00\x0c\x00\x1c\x00\x2c\x00\x2c\x00\x4c\x00\x4c\x00'\
b'\x8c\x00\xff\x00\x0c\x00\x0c\x00\x3f\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\x00\x3c\x00\x20\x00'\
b'\x20\x00\x3c\x00\x66\x00\x43\x00\x03\x00\x63\x00\x63\x00\x46\x00'\
b'\x3c\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x3c\x00\x66\x00\x46\x00\xc0\x00\xc0\x00\xfc\x00\xe6\x00'\
b'\xc3\x00\xc3\x00\xc3\x00\x66\x00\x3c\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x7f\x00\x42\x00'\
b'\x42\x00\x04\x00\x04\x00\x08\x00\x08\x00\x08\x00\x18\x00\x18\x00'\
b'\x18\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x3c\x00\x66\x00\x42\x00\x62\x00\x76\x00\x3c\x00\x6e\x00'\
b'\xc7\x00\xc3\x00\xc3\x00\x66\x00\x3c\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x66\x00\xc3\x00'\
b'\xc3\x00\xc3\x00\x67\x00\x3f\x00\x03\x00\x03\x00\x62\x00\x66\x00'\
b'\x38\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x60\x60\x00\x00\x00\x00\x60\x60\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x00\x00\x00\x00'\
b'\x60\x60\x20\x20\x40\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80\x06\x00\x18\x00'\
b'\x60\x00\x60\x00\x18\x00\x06\x00\x01\x80\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x7f\x80\x00\x00\x00\x00\x7f\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x30\x00\x0c\x00'\
b'\x03\x00\x03\x00\x0c\x00\x30\x00\xc0\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x38\x4c\xe6\x46\x06\x0c\x18\x10\x10\x00'\
b'\x30\x30\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x07\x80\x18\x60\x20\x10\x46\xd0\x4d\x90\x98\x90\x99\x90'\
b'\x91\x20\x9b\x20\x4c\xc8\x40\x10\x30\x60\x0f\x80\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x04\x00\x0e\x00'\
b'\x0e\x00\x16\x00\x13\x00\x13\x00\x3f\x80\x21\x80\x41\x80\x40\xc0'\
b'\xf3\xe0\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\x80\x31\xc0\x30\xc0\x30\xc0\x31\x80\x3f\xc0\x30\xe0'\
b'\x30\x60\x30\x60\x30\x60\x30\xc0\xff\x80\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xa0\x38\x60\x30\x20'\
b'\x70\x20\x60\x20\x60\x00\x60\x00\x60\x00\x70\x20\x30\x20\x38\x40'\
b'\x0f\x80\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\x00\x31\xc0\x30\x60\x30\x60\x30\x30\x30\x30\x30\x30'\
b'\x30\x30\x30\x60\x30\x60\x31\xc0\xff\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xc0\x30\xc0\x30\x40'\
b'\x32\x40\x32\x00\x3e\x00\x36\x00\x32\x00\x32\x40\x30\x40\x30\xc0'\
b'\xff\xc0\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\xc0\x30\xc0\x30\x40\x32\x40\x32\x00\x3e\x00\x36\x00'\
b'\x32\x00\x32\x00\x30\x00\x30\x00\xfc\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xa0\x38\x60\x30\x20'\
b'\x70\x20\x60\x20\x60\x00\x61\xf0\x60\x60\x70\x60\x30\x60\x38\xe0'\
b'\x0f\x20\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xfd\xf8\x30\x60\x30\x60\x30\x60\x30\x60\x3f\xe0\x30\x60'\
b'\x30\x60\x30\x60\x30\x60\x30\x60\xfd\xf8\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\xfc\x30\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\x30\xfc\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1f\x80\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x46\x00\xe6\x00\xc6\x00\x84\x00\x78\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfd\xf0\x30\xc0\x30\x80'\
b'\x31\x00\x32\x00\x36\x00\x3b\x00\x33\x80\x31\x80\x30\xc0\x30\xe0'\
b'\xfd\xf0\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xfc\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00'\
b'\x30\x40\x30\x40\x30\x40\x30\xc0\xff\xc0\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x3e\x38\x38\x38\x38'\
b'\x2c\x58\x2c\x58\x2e\x58\x26\x98\x26\x98\x23\x98\x23\x18\x23\x18'\
b'\xf9\x3e\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xf0\xf8\x38\x20\x3c\x20\x2c\x20\x2e\x20\x27\x20\x23\xa0'\
b'\x21\xa0\x20\xe0\x20\xe0\x20\x60\xf8\x20\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x18\xc0\x30\x60'\
b'\x30\x60\x60\x30\x60\x30\x60\x30\x60\x30\x30\x60\x30\x60\x18\xc0'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\x80\x30\xc0\x30\x60\x30\x60\x30\x60\x30\xc0\x3f\x80'\
b'\x30\x00\x30\x00\x30\x00\x30\x00\xfc\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x18\xc0\x30\x60'\
b'\x30\x60\x60\x30\x60\x30\x60\x30\x66\x30\x29\x20\x39\xe0\x19\xc0'\
b'\x07\x80\x01\xa0\x01\xa0\x00\xc0\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\x00\x30\xc0\x30\x60\x30\x60\x30\xc0\x3f\x00\x33\x80'\
b'\x30\xc0\x30\xc0\x30\xd0\x30\xd0\xfc\x60\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x80\x31\x80\x60\x80'\
b'\x60\x80\x70\x00\x3e\x00\x1f\x00\x43\x80\x41\x80\x41\x80\x63\x00'\
b'\x5e\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\xc0\xcc\xc0\x8c\x40\x8c\x40\x8c\x40\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x3f\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xf8\x30\x20\x30\x20'\
b'\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20\x18\x40'\
b'\x0f\x80\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xf8\xe0\x70\x40\x30\x40\x30\x80\x18\x80\x19\x00\x19\x00'\
b'\x0d\x00\x0e\x00\x0e\x00\x04\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\xce\x63\x04\x63\x04'\
b'\x31\x88\x31\x88\x39\xc8\x1a\xd0\x1a\xd0\x0a\x50\x0c\x60\x04\x20'\
b'\x04\x20\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xf1\xe0\x60\xc0\x30\x80\x19\x00\x1e\x00\x0c\x00\x06\x00'\
b'\x0f\x00\x13\x00\x21\x80\x60\xc0\xf1\xe0\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xf0\x30\x40\x18\x80'\
b'\x18\x80\x0d\x00\x0d\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x1f\x80\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7f\x80\x61\x80\x43\x00\x43\x00\x06\x00\x0c\x00\x0c\x00'\
b'\x18\x80\x30\x80\x30\x80\x61\x80\xff\x80\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x70\x40\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x40\x40\x70\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x20\x00\x20\x00\x10\x00\x10\x00\x08\x00\x08\x00\x04\x00'\
b'\x04\x00\x02\x00\x02\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x70\x10\x10\x10\x10\x10\x10\x10\x10\x10'\
b'\x10\x10\x10\x70\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x0c\x00\x1e\x00\x12\x00\x33\x00\x21\x00\x61\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x80\x40'\
b'\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x3c\x00\x66\x00\x66\x00\x0e\x00\x36\x00\x66\x00\x66\x00'\
b'\x3b\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xe0\x00\x60\x00\x60\x00\x60\x00\x7c\x00\x66\x00\x63\x00'\
b'\x63\x00\x63\x00\x63\x00\x66\x00\x5c\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x6c\xcc\xc0\xc0\xc0'\
b'\x6c\x38\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x07\x00\x03\x00\x03\x00\x03\x00\x1f\x00\x33\x00\x63\x00'\
b'\x63\x00\x63\x00\x63\x00\x33\x00\x1d\x80\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x44\xc6\xfe\xc0\xc0'\
b'\x66\x3c\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x38\x6c'\
b'\x60\x60\xf8\x60\x60\x60\x60\x60\x60\xf8\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x3d\x80\x66\x80\x66\x00\x66\x00\x66\x00\x3c\x00\x40\x00'\
b'\x7e\x00\xc3\x00\xc3\x00\x7e\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xe0\x00\x60\x00\x60\x00\x60\x00\x6e\x00\x77\x00\x63\x00'\
b'\x63\x00\x63\x00\x63\x00\x63\x00\xf7\x80\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x60\x60\x00\x00\xe0\x60\x60\x60\x60\x60'\
b'\x60\xf0\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x30\x30'\
b'\x00\x00\x70\x30\x30\x30\x30\x30\x30\x30\x30\xb0\xe0\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x60\x00\x60\x00'\
b'\x60\x00\x6f\x80\x66\x00\x6c\x00\x78\x00\x7c\x00\x66\x00\x63\x00'\
b'\xf7\x80\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\xe0\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\xf0\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xee\x70\x73\x98\x63\x18\x63\x18\x63\x18\x63\x18\x63\x18'\
b'\xf7\xbc\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xee\x00\x73\x00\x63\x00'\
b'\x63\x00\x63\x00\x63\x00\x63\x00\xf7\x80\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x6c\xc6\xc6\xc6\xc6'\
b'\x6c\x38\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xdc\x00\x66\x00\x63\x00'\
b'\x63\x00\x63\x00\x63\x00\x66\x00\x7c\x00\x60\x00\x60\x00\xf0\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x39\x00\x66\x00\xc6\x00\xc6\x00\xc6\x00\xc6\x00\x66\x00'\
b'\x3e\x00\x06\x00\x06\x00\x0f\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xec\x76\x66\x60\x60\x60\x60\xf0\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x74\xcc\xc4\x70\x38\x8c'\
b'\xcc\xb8\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x20'\
b'\x20\x60\xf8\x60\x60\x60\x60\x64\x64\x38\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xe7\x00\x63\x00\x63\x00\x63\x00\x63\x00\x63\x00\x63\x00'\
b'\x3d\x80\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\x80\x63\x00\x32\x00'\
b'\x36\x00\x1c\x00\x1c\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xef\x78\x66\x30\x33\x20\x33\x60\x1d\xc0\x1d\xc0\x08\x80'\
b'\x08\x80\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\x00\x62\x00\x34\x00'\
b'\x38\x00\x1c\x00\x2c\x00\x46\x00\xef\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xf7\x00\x62\x00\x36\x00\x34\x00\x1c\x00\x1c\x00\x08\x00'\
b'\x08\x00\x18\x00\xd0\x00\xe0\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7e\x46\x4c\x18\x18\x32\x62\x7e\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x10\x20\x20\x20\x20\x20\x40\x20\x20\x20'\
b'\x20\x20\x20\x10\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x40\x20\x20\x20\x20\x20\x10\x20\x20\x20'\
b'\x20\x20\x20\x40\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x39\x80\x67\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x00\x20\x20\x20\x20'\
b'\x60\x60\x60\x60\x60\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00\x1c\x00\x26\x00\x66\x00'\
b'\x48\x00\x48\x00\x72\x00\x32\x00\x1c\x00\x20\x00\x20\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x31\x00\x23\x00'\
b'\x23\x00\x30\x00\x10\x00\xfe\x00\x10\x00\x10\x00\x70\x80\xbf\x00'\
b'\x4e\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x5d\x00\x36\x00\x63\x00\x41\x00\x41\x00'\
b'\x63\x00\x36\x00\x5d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf3\x80\x61\x00\x22\x00'\
b'\x32\x00\x14\x00\x14\x00\x3e\x00\x08\x00\x3e\x00\x08\x00\x08\x00'\
b'\x3e\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x1c\x24\x20\x30\x18\x2c\x46\x42\x62\x34'\
b'\x18\x0c\x04\x24\x38\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\xd8'\
b'\xd8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80\x30\xc0\x47\x20'\
b'\xcd\xb0\x98\x90\x90\x10\x90\x10\x98\x90\xcd\xb0\x47\x20\x30\xc0'\
b'\x1f\x80\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\xe0\x90'\
b'\x70\x90\xe8\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x24\x48\xd8\x48'\
b'\x24\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80'\
b'\x00\x80\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80\x30\xc0\x5f\x20'\
b'\xc9\xb0\x89\x90\x8f\x10\x89\x10\x89\x90\xc8\xb0\x5c\xe0\x30\xc0'\
b'\x1f\x80\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00'\
b'\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x38\x44\x44\x44\x38\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x7f\x00'\
b'\x08\x00\x08\x00\x08\x00\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x70\xd8\x88\x10\x20\x48\xf8\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x70\xd8'\
b'\x88\x30\x88\xd8\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x20\x60\x80\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe7\x00\x63\x00\x63\x00'\
b'\x63\x00\x63\x00\x63\x00\x63\x00\x7d\xc0\x60\x00\x60\x00\x60\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\xea\x00\xca\x00'\
b'\xca\x00\xca\x00\xea\x00\x7a\x00\x0a\x00\x0a\x00\x0a\x00\x0a\x00'\
b'\x0a\x00\x0a\x00\x0a\x00\x1f\x00\x05\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x60\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x20\x20\x10\x60\x00\x00\x00\x06\x00\x00\x00\x00\x00\x20\x60'\
b'\x20\x20\x20\x20\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x60\x90\x90\x90\x60\x00\xf0\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x90\x48\x6c\x48\x90\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x20\x60\x60\x20\xc0'\
b'\x20\x80\x21\x00\x23\x20\x76\x60\x04\xa0\x09\x20\x19\xf0\x30\x20'\
b'\x20\x70\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x20\x40\x60\xc0\x21\x80\x21\x00\x22\x00\x26\xe0\x7d\xb0'\
b'\x09\x10\x10\x60\x30\x80\x61\x90\x41\xf0\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\x18\xd8\x30\x88\x60'\
b'\x30\xc0\x88\x80\xd9\x90\x73\x30\x06\x50\x04\x90\x0c\xf8\x18\x10'\
b'\x30\x38\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x18\x18\x00\x10\x10\x30\x60\xc0\xc4\xce\x64\x38\x00\x00\x00'\
b'\x0c\x00\x18\x00\x0c\x00\x02\x00\x00\x00\x04\x00\x04\x00\x0e\x00'\
b'\x0e\x00\x16\x00\x13\x00\x13\x00\x3f\x80\x21\x80\x41\x80\x40\xc0'\
b'\xf3\xe0\x00\x00\x00\x00\x00\x00\x0c\x00\x03\x00\x06\x00\x08\x00'\
b'\x00\x00\x04\x00\x04\x00\x0e\x00\x0e\x00\x16\x00\x13\x00\x13\x00'\
b'\x3f\x80\x21\x80\x41\x80\x40\xc0\xf3\xe0\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x04\x00\x0e\x00\x11\x00\x00\x00\x04\x00\x04\x00\x0e\x00'\
b'\x0e\x00\x16\x00\x13\x00\x13\x00\x3f\x80\x21\x80\x41\x80\x40\xc0'\
b'\xf3\xe0\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x1d\x00\x2e\x00'\
b'\x00\x00\x04\x00\x04\x00\x0e\x00\x0e\x00\x16\x00\x13\x00\x13\x00'\
b'\x3f\x80\x21\x80\x41\x80\x40\xc0\xf3\xe0\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x12\x00\x12\x00\x00\x00\x04\x00\x04\x00\x0e\x00'\
b'\x0e\x00\x16\x00\x13\x00\x13\x00\x3f\x80\x21\x80\x41\x80\x40\xc0'\
b'\xf3\xe0\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x12\x00\x0c\x00'\
b'\x00\x00\x04\x00\x04\x00\x0e\x00\x0e\x00\x16\x00\x13\x00\x13\x00'\
b'\x3f\x80\x21\x80\x41\x80\x40\xc0\xf3\xe0\x00\x00\x00\x00\x00\x00'\
b'\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xff'\
b'\x00\x02\xc3\x00\x02\xc1\x00\x04\xc1\x00\x04\xc8\x00\x08\xf8\x00'\
b'\x08\xd8\x00\x1f\xc9\x00\x10\xc1\x00\x20\xc1\x00\x20\xc3\x00\xfb'\
b'\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xa0\x38\x60\x30\x20'\
b'\x70\x20\x60\x20\x60\x00\x60\x00\x60\x00\x70\x20\x30\x20\x38\x40'\
b'\x0f\x80\x04\x00\x02\x00\x0c\x00\x0c\x00\x18\x00\x0c\x00\x02\x00'\
b'\x00\x00\xff\xc0\x30\xc0\x30\x40\x30\x40\x32\x00\x3e\x00\x36\x00'\
b'\x32\x00\x30\x40\x30\x40\x30\xc0\xff\xc0\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x03\x00\x06\x00\x08\x00\x00\x00\xff\xc0\x30\xc0\x30\x40'\
b'\x30\x40\x32\x00\x3e\x00\x36\x00\x32\x00\x30\x40\x30\x40\x30\xc0'\
b'\xff\xc0\x00\x00\x00\x00\x00\x00\x0c\x00\x04\x00\x0e\x00\x11\x00'\
b'\x00\x00\xff\xc0\x30\xc0\x30\x40\x30\x40\x32\x00\x3e\x00\x36\x00'\
b'\x32\x00\x30\x40\x30\x40\x30\xc0\xff\xc0\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x11\x00\x11\x00\x00\x00\xff\xc0\x30\xc0\x30\x40'\
b'\x30\x40\x32\x00\x3e\x00\x36\x00\x32\x00\x30\x40\x30\x40\x30\xc0'\
b'\xff\xc0\x00\x00\x00\x00\x00\x00\x07\x00\xc0\x60\x10\x00\xfc\x30'\
b'\x30\x30\x30\x30\x30\x30\x30\x30\x30\xfc\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x0c\x18\x20\x00\xfc\x30\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\x30\xfc\x00\x00\x00\x00\x00\x00\x07\x00\x20\x70\x88\x00\xfc\x30'\
b'\x30\x30\x30\x30\x30\x30\x30\x30\x30\xfc\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x48\x48\x00\xfc\x30\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\x30\xfc\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xff\x00\x31\xc0\x30\x60\x30\x60\x30\x30\x7c\x30\x30\x30'\
b'\x30\x30\x30\x60\x30\x60\x31\xc0\xff\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x0e\x40\x13\x80\x00\x00\xf0\xf8\x38\x20\x3c\x20'\
b'\x2c\x20\x2e\x20\x27\x20\x23\xa0\x21\xa0\x20\xe0\x20\xe0\x20\x60'\
b'\xf8\x20\x00\x00\x00\x00\x00\x00\x0d\x00\x0c\x00\x06\x00\x01\x00'\
b'\x00\x00\x07\x00\x18\xc0\x30\x60\x30\x60\x60\x30\x60\x30\x60\x30'\
b'\x60\x30\x30\x60\x30\x60\x18\xc0\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\xc0\x01\x80\x02\x00\x00\x00\x07\x00\x18\xc0\x30\x60'\
b'\x30\x60\x60\x30\x60\x30\x60\x30\x60\x30\x30\x60\x30\x60\x18\xc0'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x02\x00\x07\x00\x08\x80'\
b'\x00\x00\x07\x00\x18\xc0\x30\x60\x30\x60\x60\x30\x60\x30\x60\x30'\
b'\x60\x30\x30\x60\x30\x60\x18\xc0\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x07\x40\x0b\x80\x00\x00\x07\x00\x18\xc0\x30\x60'\
b'\x30\x60\x60\x30\x60\x30\x60\x30\x60\x30\x30\x60\x30\x60\x18\xc0'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x08\x80\x08\x80'\
b'\x00\x00\x07\x00\x18\xc0\x30\x60\x30\x60\x60\x30\x60\x30\x60\x30'\
b'\x60\x30\x30\x60\x30\x60\x18\xc0\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x40\x80\x21\x00\x12\x00\x0c\x00\x0c\x00\x12\x00\x21\x00'\
b'\x40\x80\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x07\x20\x18\xc0\x30\xe0\x30\xa0\x61\x30\x62\x30\x62\x30'\
b'\x64\x30\x28\x60\x38\x60\x18\xc0\x27\x00\x40\x00\x00\x00\x00\x00'\
b'\x0d\x00\x0c\x00\x06\x00\x01\x00\x00\x00\xfc\xf8\x30\x20\x30\x20'\
b'\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20\x18\x40'\
b'\x0f\x80\x00\x00\x00\x00\x00\x00\x0d\x00\x00\xc0\x01\x80\x02\x00'\
b'\x00\x00\xfc\xf8\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20'\
b'\x30\x20\x30\x20\x30\x20\x18\x40\x0f\x80\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x02\x00\x07\x00\x08\x80\x00\x00\xfc\xf8\x30\x20\x30\x20'\
b'\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20\x18\x40'\
b'\x0f\x80\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x08\x80\x08\x80'\
b'\x00\x00\xfc\xf8\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20\x30\x20'\
b'\x30\x20\x30\x20\x30\x20\x18\x40\x0f\x80\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x01\x80\x03\x00\x04\x00\x00\x00\xfc\xf0\x30\x40\x18\x80'\
b'\x18\x80\x0d\x00\x0d\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x1f\x80\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xfc\x00\x30\x00\x30\x00\x3f\x80\x30\xc0\x30\x60\x30\x60'\
b'\x30\xc0\x3f\x80\x30\x00\x30\x00\xfc\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x33\x00\x31\x80'\
b'\x31\x80\x33\x00\x3e\x00\x33\x00\x31\x80\x31\x80\x31\x80\x3b\x00'\
b'\x76\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x20\x00\x30\x00\x08\x00\x00\x00\x3c\x00\x66\x00\x66\x00'\
b'\x0e\x00\x36\x00\x66\x00\x66\x00\x3b\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x06\x00\x08\x00'\
b'\x00\x00\x3c\x00\x66\x00\x66\x00\x0e\x00\x36\x00\x66\x00\x66\x00'\
b'\x3b\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x1c\x00\x22\x00\x00\x00\x3c\x00\x66\x00\x66\x00'\
b'\x0e\x00\x36\x00\x66\x00\x66\x00\x3b\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x2c\x00'\
b'\x00\x00\x3c\x00\x66\x00\x66\x00\x0e\x00\x36\x00\x66\x00\x66\x00'\
b'\x3b\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x24\x00\x24\x00\x00\x00\x3c\x00\x66\x00\x66\x00'\
b'\x0e\x00\x36\x00\x66\x00\x66\x00\x3b\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x18\x00\x24\x00\x24\x00\x18\x00'\
b'\x00\x00\x3c\x00\x66\x00\x66\x00\x0e\x00\x36\x00\x66\x00\x66\x00'\
b'\x3b\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x79\xc0\xce\x20\xc6\x30'\
b'\x1f\xf0\x66\x00\xc6\x10\xcf\x20\x79\xc0\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x6c\xcc\xc0\xc0\xc4'\
b'\x6c\x38\x20\x10\x60\x00\x00\x00\x08\x00\x00\x00\x00\x00\x20\x30'\
b'\x08\x00\x38\x44\xc6\xfe\xc0\xc0\x66\x3c\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x04\x0c\x10\x00\x38\x44\xc6\xfe\xc0\xc0'\
b'\x66\x3c\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x10\x38'\
b'\x44\x00\x38\x44\xc6\xfe\xc0\xc0\x66\x3c\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x24\x24\x00\x38\x44\xc6\xfe\xc0\xc0'\
b'\x66\x3c\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x80\xc0'\
b'\x20\x00\xe0\x60\x60\x60\x60\x60\x60\xf0\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x10\x30\x40\x00\xe0\x60\x60\x60\x60\x60'\
b'\x60\xf0\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x20\x70'\
b'\x88\x00\x70\x30\x30\x30\x30\x30\x30\x78\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x90\x90\x00\xe0\x60\x60\x60\x60\x60'\
b'\x60\xf0\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x40\x26\x18'\
b'\x68\x0c\x3c\x6e\xc6\xc6\xc6\xc6\x6c\x38\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x2c\x00'\
b'\x00\x00\xee\x00\x73\x00\x63\x00\x63\x00\x63\x00\x63\x00\x63\x00'\
b'\xf7\x80\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x40\x60'\
b'\x10\x00\x38\x6c\xc6\xc6\xc6\xc6\x6c\x38\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x04\x0c\x10\x00\x38\x6c\xc6\xc6\xc6\xc6'\
b'\x6c\x38\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x10\x38'\
b'\x44\x00\x38\x6c\xc6\xc6\xc6\xc6\x6c\x38\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x34\x58\x00\x38\x6c\xc6\xc6\xc6\xc6'\
b'\x6c\x38\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x48'\
b'\x48\x00\x38\x6c\xc6\xc6\xc6\xc6\x6c\x38\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x0c\x00\x00\x00\x7f\x80\x00\x00\x0c\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x02\x3c\x64\xce\xd6\xd6\xe6\x4c\x78\x80\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x30\x00\x08\x00'\
b'\x00\x00\xe7\x00\x63\x00\x63\x00\x63\x00\x63\x00\x63\x00\x63\x00'\
b'\x3d\x80\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x02\x00\x06\x00\x08\x00\x00\x00\xe7\x00\x63\x00\x63\x00'\
b'\x63\x00\x63\x00\x63\x00\x63\x00\x3d\x80\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x22\x00'\
b'\x00\x00\xe7\x00\x63\x00\x63\x00\x63\x00\x63\x00\x63\x00\x63\x00'\
b'\x3d\x80\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x24\x00\x24\x00\x00\x00\xe7\x00\x63\x00\x63\x00'\
b'\x63\x00\x63\x00\x63\x00\x63\x00\x3d\x80\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x06\x00\x08\x00'\
b'\x00\x00\xf7\x00\x62\x00\x36\x00\x34\x00\x1c\x00\x18\x00\x08\x00'\
b'\x18\x00\x10\x00\xd0\x00\xe0\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\xe0\x00\x60\x00\x60\x00\x7c\x00\x66\x00\x63\x00'\
b'\x63\x00\x63\x00\x63\x00\x66\x00\x7c\x00\x60\x00\x60\x00\xf0\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x24\x00\x24\x00'\
b'\x00\x00\xf7\x00\x62\x00\x36\x00\x34\x00\x1c\x00\x18\x00\x08\x00'\
b'\x18\x00\x10\x00\xd0\x00\xe0\x00'

_sparse =\
b'\x20\x00\x03\x00\x21\x00\x06\x00\x22\x00\x09\x00\x23\x00\x0c\x00'\
b'\x24\x00\x11\x00\x25\x00\x16\x00\x26\x00\x1b\x00\x27\x00\x20\x00'\
b'\x28\x00\x23\x00\x29\x00\x26\x00\x2a\x00\x29\x00\x2b\x00\x2c\x00'\
b'\x2c\x00\x31\x00\x2d\x00\x34\x00\x2e\x00\x37\x00\x2f\x00\x3a\x00'\
b'\x30\x00\x3d\x00\x31\x00\x42\x00\x32\x00\x47\x00\x33\x00\x4c\x00'\
b'\x34\x00\x51\x00\x35\x00\x56\x00\x36\x00\x5b\x00\x37\x00\x60\x00'\
b'\x38\x00\x65\x00\x39\x00\x6a\x00\x3a\x00\x6f\x00\x3b\x00\x72\x00'\
b'\x3c\x00\x75\x00\x3d\x00\x7a\x00\x3e\x00\x7f\x00\x3f\x00\x84\x00'\
b'\x40\x00\x87\x00\x41\x00\x8c\x00\x42\x00\x91\x00\x43\x00\x96\x00'\
b'\x44\x00\x9b\x00\x45\x00\xa0\x00\x46\x00\xa5\x00\x47\x00\xaa\x00'\
b'\x48\x00\xaf\x00\x49\x00\xb4\x00\x4a\x00\xb7\x00\x4b\x00\xbc\x00'\
b'\x4c\x00\xc1\x00\x4d\x00\xc6\x00\x4e\x00\xcb\x00\x4f\x00\xd0\x00'\
b'\x50\x00\xd5\x00\x51\x00\xda\x00\x52\x00\xdf\x00\x53\x00\xe4\x00'\
b'\x54\x00\xe9\x00\x55\x00\xee\x00\x56\x00\xf3\x00\x57\x00\xf8\x00'\
b'\x58\x00\xfd\x00\x59\x00\x02\x01\x5a\x00\x07\x01\x5b\x00\x0c\x01'\
b'\x5c\x00\x0f\x01\x5d\x00\x14\x01\x5e\x00\x17\x01\x5f\x00\x1c\x01'\
b'\x60\x00\x1f\x01\x61\x00\x22\x01\x62\x00\x27\x01\x63\x00\x2c\x01'\
b'\x64\x00\x2f\x01\x65\x00\x34\x01\x66\x00\x37\x01\x67\x00\x3a\x01'\
b'\x68\x00\x3f\x01\x69\x00\x44\x01\x6a\x00\x47\x01\x6b\x00\x4a\x01'\
b'\x6c\x00\x4f\x01\x6d\x00\x52\x01\x6e\x00\x57\x01\x6f\x00\x5c\x01'\
b'\x70\x00\x5f\x01\x71\x00\x64\x01\x72\x00\x69\x01\x73\x00\x6c\x01'\
b'\x74\x00\x6f\x01\x75\x00\x72\x01\x76\x00\x77\x01\x77\x00\x7c\x01'\
b'\x78\x00\x81\x01\x79\x00\x86\x01\x7a\x00\x8b\x01\x7b\x00\x8e\x01'\
b'\x7c\x00\x91\x01\x7d\x00\x96\x01\x7e\x00\x99\x01\xa1\x00\x9e\x01'\
b'\xa2\x00\xa1\x01\xa3\x00\xa6\x01\xa4\x00\xab\x01\xa5\x00\xb0\x01'\
b'\xa6\x00\xb5\x01\xa7\x00\xba\x01\xa8\x00\xbd\x01\xa9\x00\xc0\x01'\
b'\xaa\x00\xc5\x01\xab\x00\xc8\x01\xac\x00\xcb\x01\xae\x00\xd0\x01'\
b'\xaf\x00\xd5\x01\xb0\x00\xd8\x01\xb1\x00\xdb\x01\xb2\x00\xe0\x01'\
b'\xb3\x00\xe3\x01\xb4\x00\xe6\x01\xb5\x00\xe9\x01\xb6\x00\xee\x01'\
b'\xb7\x00\xf3\x01\xb8\x00\xf6\x01\xb9\x00\xf9\x01\xba\x00\xfc\x01'\
b'\xbb\x00\xff\x01\xbc\x00\x02\x02\xbd\x00\x07\x02\xbe\x00\x0c\x02'\
b'\xbf\x00\x11\x02\xc0\x00\x14\x02\xc1\x00\x19\x02\xc2\x00\x1e\x02'\
b'\xc3\x00\x23\x02\xc4\x00\x28\x02\xc5\x00\x2d\x02\xc6\x00\x32\x02'\
b'\xc7\x00\x3a\x02\xc8\x00\x3f\x02\xc9\x00\x44\x02\xca\x00\x49\x02'\
b'\xcb\x00\x4e\x02\xcc\x00\x53\x02\xcd\x00\x56\x02\xce\x00\x59\x02'\
b'\xcf\x00\x5c\x02\xd0\x00\x5f\x02\xd1\x00\x64\x02\xd2\x00\x69\x02'\
b'\xd3\x00\x6e\x02\xd4\x00\x73\x02\xd5\x00\x78\x02\xd6\x00\x7d\x02'\
b'\xd7\x00\x82\x02\xd8\x00\x87\x02\xd9\x00\x8c\x02\xda\x00\x91\x02'\
b'\xdb\x00\x96\x02\xdc\x00\x9b\x02\xdd\x00\xa0\x02\xde\x00\xa5\x02'\
b'\xdf\x00\xaa\x02\xe0\x00\xaf\x02\xe1\x00\xb4\x02\xe2\x00\xb9\x02'\
b'\xe3\x00\xbe\x02\xe4\x00\xc3\x02\xe5\x00\xc8\x02\xe6\x00\xcd\x02'\
b'\xe7\x00\xd2\x02\xe8\x00\xd5\x02\xe9\x00\xd8\x02\xea\x00\xdb\x02'\
b'\xeb\x00\xde\x02\xec\x00\xe1\x02\xed\x00\xe4\x02\xee\x00\xe7\x02'\
b'\xef\x00\xea\x02\xf0\x00\xed\x02\xf1\x00\xf0\x02\xf2\x00\xf5\x02'\
b'\xf3\x00\xf8\x02\xf4\x00\xfb\x02\xf5\x00\xfe\x02\xf6\x00\x01\x03'\
b'\xf7\x00\x04\x03\xf8\x00\x09\x03\xf9\x00\x0c\x03\xfa\x00\x11\x03'\
b'\xfb\x00\x16\x03\xfc\x00\x1b\x03\xfd\x00\x20\x03\xfe\x00\x25\x03'\
b'\xff\x00\x2a\x03'

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
 
