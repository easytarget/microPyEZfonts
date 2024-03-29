'''
    mPyEZfont_u8g2_timR10_f.py : generated as part of the microPyEZfonts repository
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
# Font: timR10.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/f-char.set u8g2/tools/font/bdf/timR10.bdf 0 tmp_mPyEZfont_u8g2_timR10_f.py
version = '0.33'

def height():
    return 17

def baseline():
    return 14

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
    return 255

_font =\
b'\x06\x00\x00\x00\x00\x00\x70\x88\x88\x08\x10\x20\x20\x00\x20\x20'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x20\x20\x20\x20\x20\x20\x20\x00\x20\x20'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x50\x50'\
b'\x50\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x14\x14\x7e\x28\x28\x28\xfc\x50\x50\x50'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x10\x3c\x54'\
b'\x50\x50\x38\x14\x14\x14\x54\x78\x10\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\xc0\x6f\x80\x49\x00'\
b'\x4a\x00\x34\x00\x05\x80\x0b\x40\x12\x40\x22\x40\x21\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x12\x00\x12\x00\x1c\x00\x09\xc0\x3c\x80\x65\x00'\
b'\x42\x00\x67\x20\x39\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\x00\x40\x40\x40\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x10\x10'\
b'\x20\x20\x40\x40\x40\x40\x40\x20\x20\x10\x10\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x40\x40\x20\x20\x10\x10\x10\x10\x10\x20'\
b'\x20\x40\x40\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x10\x54'\
b'\x38\x38\x54\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x10\x10\x10\xfe\x10\x10\x10'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x60\x20\x40\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x10\x10\x10\x20\x20\x20\x40\x40\x40\x80'\
b'\x80\x80\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x3c\x66'\
b'\x42\x42\x42\x42\x42\x42\x66\x3c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x10\x70\x10\x10\x10\x10\x10\x10\x10\x7c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x38\x6c'\
b'\x44\x04\x0c\x08\x10\x20\x44\x7c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x78\x8c\x04\x08\x30\x38\x04\x04\xcc\x78'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x08\x18'\
b'\x18\x28\x68\x48\x88\xfc\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x3c\x20\x40\x70\x18\x0c\x04\x04\x48\x70'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x0c\x10'\
b'\x20\x40\x78\xcc\x84\x84\xcc\x78\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\xfc\x84\x08\x08\x10\x10\x20\x20\x40\x40'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x38\x4c'\
b'\x44\x64\x38\x4c\x44\x44\x44\x38\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x3c\x66\x42\x42\x66\x3c\x04\x08\x10\x60'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x60\x00\x00\x00\x00\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00\x00\x00\x00\x00\x60'\
b'\x20\x40\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x06\x18\x60\xc0\x60\x18\x06\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\x00\xfe\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xc0\x30\x0c\x06\x0c\x30\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x70\x88\x88\x08\x10\x20\x20\x00\x20\x20'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0f\x80\x30\x60\x60\x20\x46\x90\x89\x10\x91\x10\x91\x10'\
b'\x93\x20\xcd\xc0\x40\x00\x30\xc0\x0f\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x04\x00\x0a\x00'\
b'\x0a\x00\x11\x00\x11\x00\x1f\x00\x20\x80\x20\x80\x71\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7e\x00\x23\x00\x21\x00\x23\x00\x3e\x00\x23\x00\x21\x00'\
b'\x21\x00\x23\x00\x7e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x80\x31\x80\x20\x80'\
b'\x40\x80\x40\x00\x40\x00\x40\x00\x60\x80\x31\x00\x1e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xfe\x00\x23\x00\x21\x00\x20\x80\x20\x80\x20\x80\x20\x80'\
b'\x21\x00\x23\x00\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x21\x00\x20\x00'\
b'\x22\x00\x3e\x00\x22\x00\x20\x00\x21\x00\x21\x00\x7f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x7f\x21'\
b'\x20\x22\x3e\x22\x20\x20\x20\x70\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x80\x31\x80\x20\x80'\
b'\x40\x80\x40\x00\x43\xc0\x40\x80\x60\x80\x31\x80\x1f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x73\x80\x21\x00\x21\x00\x21\x00\x3f\x00\x21\x00\x21\x00'\
b'\x21\x00\x21\x00\x73\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x70\x20\x20\x20\x20\x20\x20\x20\x20\x70'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x38\x10'\
b'\x10\x10\x10\x10\x10\x10\x50\x60\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x77\x00\x22\x00\x24\x00'\
b'\x28\x00\x38\x00\x28\x00\x24\x00\x22\x00\x23\x00\x73\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x70\x00\x20\x00\x20\x00\x20\x00\x20\x00\x20\x00\x20\x00'\
b'\x20\x00\x21\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\x70\x30\x60\x28\xa0'\
b'\x28\xa0\x2d\xa0\x25\x20\x25\x20\x27\x20\x22\x20\x72\x70\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x71\xc0\x30\x80\x28\x80\x2c\x80\x24\x80\x26\x80\x22\x80'\
b'\x22\x80\x21\x80\x71\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x33\x00\x21\x00'\
b'\x40\x80\x40\x80\x40\x80\x40\x80\x21\x00\x33\x00\x1e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x7c\x26'\
b'\x22\x22\x26\x3c\x20\x20\x20\x70\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x33\x00\x21\x00'\
b'\x40\x80\x40\x80\x40\x80\x40\x80\x21\x00\x33\x00\x1e\x00\x04\x00'\
b'\x03\x00\x01\x80\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xfc\x00\x26\x00\x22\x00\x22\x00\x26\x00\x3c\x00\x24\x00'\
b'\x22\x00\x23\x00\xf1\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x3a\x66\x42\x60\x38\x0c\x02\x42\x66\x5c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7f\x00\x49\x00\x49\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x73\x80\x21\x00\x21\x00'\
b'\x21\x00\x21\x00\x21\x00\x21\x00\x21\x00\x33\x00\x1e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xe3\x80\x41\x00\x63\x00\x22\x00\x22\x00\x36\x00\x14\x00'\
b'\x1c\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe7\x38\x42\x10\x62\x30'\
b'\x22\x20\x25\x20\x35\x60\x15\x40\x18\xc0\x08\x80\x08\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x73\x80\x21\x00\x12\x00\x12\x00\x0c\x00\x0c\x00\x12\x00'\
b'\x21\x00\x61\x80\xf3\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe3\x80\x41\x00\x22\x00'\
b'\x22\x00\x14\x00\x08\x00\x08\x00\x08\x00\x08\x00\x1c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x7f\x43'\
b'\x02\x04\x08\x10\x20\x40\xc1\xff\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x70\x40\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x40\x70\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x80\x80'\
b'\x40\x40\x40\x20\x20\x20\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x70\x10\x10\x10\x10\x10\x10\x10\x10\x10'\
b'\x10\x10\x70\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x10\x28'\
b'\x28\x44\x44\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\xfe\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x40\x60\x10'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x38\x64\x0c\x34\x44\x64\x3a'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\xc0\x40'\
b'\x40\x58\x6c\x44\x44\x44\x4c\x78\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x66\x40\x40\x40\x62\x3c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x0c\x04'\
b'\x04\x3c\x64\x44\x44\x44\x6c\x3a\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x38\x44\x7c\x40\x40\x62\x3c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x38\x60'\
b'\x40\xf8\x40\x40\x40\x40\x40\xf0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x68\x44\x64\x38\x20\x3c'\
b'\x42\x66\x38\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\xc0\x40'\
b'\x40\x58\x6c\x44\x44\x44\x44\xee\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\x00\x40\x40\x00\xc0\x40\x40\x40\x40\x40\xe0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x20\x20'\
b'\x00\x60\x20\x20\x20\x20\x20\x20\x20\xa0\xc0\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\xc0\x40\x40\x4c\x48\x70\x50\x48\x4c\xe6'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\xc0\x40'\
b'\x40\x40\x40\x40\x40\x40\x40\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\xdb\x80\x6e\xc0\x44\x40\x44\x40\x44\x40\x44\x40\xee\xe0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xd8\x6c\x44\x44\x44\x44\xee\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x38\x6c\x44\x44\x44\x6c\x38'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xd8\x6c\x44\x44\x44\x6c\x58\x40\x40\xe0\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x64\x44\x44\x44\x6c\x34'\
b'\x04\x04\x0e\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xb8\x60\x40\x40\x40\x40\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x38\x48\x60\x30\x18\x48\x70'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x40\xf0\x40\x40\x40\x40\x40\x30\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\xcc\x44\x44\x44\x44\x6c\x36'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xee\x44\x44\x28\x28\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\xee\xe0\x44\x40\x44\x40\x24\x80\x3b\x80\x11\x00\x11\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xee\x44\x38\x10\x38\x44\xee\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\xee\x44\x44\x28\x28\x10\x30'\
b'\x20\xa0\xc0\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xfc\x88\x18\x30\x60\xc4\xfc\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x0c\x10\x10\x10\x10\x20\x40\x20\x10\x10'\
b'\x10\x10\x0c\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x40\x40'\
b'\x40\x40\x40\x40\x40\x40\x40\x40\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x60\x10\x10\x10\x10\x08\x04\x08\x10\x10'\
b'\x10\x10\x60\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x62\x9c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x20\x20\x00\x20\x20\x20\x20'\
b'\x20\x20\x20\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x7c\xcc\x90\x90\xa0\xe4\x78\x80\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x1c\x34\x20\x20\xf8\x20\x20\x20\xe2\xbc'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x44\x38\x44\x44\x44\x38\x44\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\xee\x44\x6c\x28\x7c\x10\x7c\x10\x10\x38'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x40\x40'\
b'\x40\x40\x00\x00\x40\x40\x40\x40\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x1c\x2c\x20\x30\x38\x4c\x44\x64\x38\x18'\
b'\x08\x68\x70\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x50\x50'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x30\xc0\x27\x40'\
b'\x49\x20\x48\x20\x48\x20\x49\x20\x26\x40\x30\xc0\x0f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\xe0\x20'\
b'\xa0\xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x24\x48\x90\x90\x48\x24'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x01\x00\x01\x00'\
b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x30\xc0\x2e\x40'\
b'\x49\x20\x4e\x20\x4a\x20\x49\x20\x29\x40\x30\xc0\x0f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\xf0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x30\x48\x48\x30\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x10\xfe\x10\x10\x00\xfe\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x60\x90\x10\x20\x40\xf0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x60\x90'\
b'\x20\x10\x90\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x10\x30\x40\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xcc\x44\x44\x44\x44\x6c\x76\x40\x40\x60\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x3e\x74\xf4\xf4\xf4\x74\x34\x14\x14\x14'\
b'\x14\x14\x14\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x20\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x20\x10\x60\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x40\xc0'\
b'\x40\x40\x40\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x60\x90\x90\x60\x00\xf0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x48\x24\x12\x12\x24\x48\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x41\x00\xc2\x00\x42\x00'\
b'\x44\x00\x44\x80\xe9\x80\x0a\x80\x14\x80\x17\xc0\x20\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x41\x00\xc2\x00\x42\x00\x44\x00\x45\x80\xea\x40\x08\x40'\
b'\x10\x80\x11\x00\x23\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x61\x00\x92\x00\x22\x00'\
b'\x14\x00\x94\x80\x69\x80\x0a\x80\x14\x80\x17\xc0\x20\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x20\x20\x00\x20\x20\x40\x80\x88\x88\x70\x00\x00\x00\x00\x00'\
b'\x0b\x00\x08\x00\x0c\x00\x02\x00\x00\x00\x04\x00\x04\x00\x0a\x00'\
b'\x0a\x00\x11\x00\x11\x00\x1f\x00\x20\x80\x20\x80\x71\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x02\x00\x06\x00\x08\x00'\
b'\x00\x00\x04\x00\x04\x00\x0a\x00\x0a\x00\x11\x00\x11\x00\x1f\x00'\
b'\x20\x80\x20\x80\x71\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x04\x00\x0e\x00\x11\x00\x00\x00\x04\x00\x04\x00\x0a\x00'\
b'\x0a\x00\x11\x00\x11\x00\x1f\x00\x20\x80\x20\x80\x71\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x09\x00\x15\x00\x12\x00'\
b'\x00\x00\x04\x00\x04\x00\x0a\x00\x0a\x00\x11\x00\x11\x00\x1f\x00'\
b'\x20\x80\x20\x80\x71\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x12\x00\x12\x00\x00\x00\x04\x00\x04\x00\x0a\x00'\
b'\x0a\x00\x11\x00\x11\x00\x1f\x00\x20\x80\x20\x80\x71\xc0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x0c\x00\x12\x00\x0c\x00'\
b'\x00\x00\x04\x00\x04\x00\x0a\x00\x0a\x00\x11\x00\x11\x00\x1f\x00'\
b'\x20\x80\x20\x80\x71\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf0\x06\x10\x0a\x00'\
b'\x0a\x20\x13\xe0\x12\x20\x1e\x00\x22\x10\x22\x10\x77\xf0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1e\x80\x31\x80\x20\x80\x40\x80\x40\x00\x40\x00\x40\x00'\
b'\x60\x80\x31\x00\x1e\x00\x04\x00\x02\x00\x0c\x00\x00\x00\x00\x00'\
b'\x09\x00\x10\x00\x18\x00\x04\x00\x00\x00\x7f\x00\x21\x00\x20\x00'\
b'\x22\x00\x3e\x00\x22\x00\x20\x00\x21\x00\x21\x00\x7f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x02\x00\x06\x00\x08\x00'\
b'\x00\x00\x7f\x00\x21\x00\x20\x00\x22\x00\x3e\x00\x22\x00\x20\x00'\
b'\x21\x00\x21\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x08\x00\x1c\x00\x22\x00\x00\x00\x7f\x00\x21\x00\x20\x00'\
b'\x22\x00\x3e\x00\x22\x00\x20\x00\x21\x00\x21\x00\x7f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x12\x00\x12\x00'\
b'\x00\x00\x7f\x00\x21\x00\x20\x00\x22\x00\x3e\x00\x22\x00\x20\x00'\
b'\x21\x00\x21\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x40\x60\x10\x00\x70\x20\x20\x20\x20\x20\x20\x20\x20\x70'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x10\x30\x40\x00\x70\x20'\
b'\x20\x20\x20\x20\x20\x20\x20\x70\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x20\x70\x88\x00\x70\x20\x20\x20\x20\x20\x20\x20\x20\x70'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x50\x50\x00\x70\x20'\
b'\x20\x20\x20\x20\x20\x20\x20\x70\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\x00\x23\x00\x21\x00'\
b'\x20\x80\xf8\x80\x20\x80\x20\x80\x21\x00\x23\x00\xfe\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x09\x00\x15\x00\x12\x00'\
b'\x00\x00\x71\xc0\x30\x80\x28\x80\x2c\x80\x24\x80\x26\x80\x22\x80'\
b'\x22\x80\x21\x80\x71\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x10\x00\x18\x00\x04\x00\x00\x00\x1e\x00\x33\x00\x21\x00'\
b'\x40\x80\x40\x80\x40\x80\x40\x80\x21\x00\x33\x00\x1e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x02\x00\x06\x00\x08\x00'\
b'\x00\x00\x1e\x00\x33\x00\x21\x00\x40\x80\x40\x80\x40\x80\x40\x80'\
b'\x21\x00\x33\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x08\x00\x1c\x00\x22\x00\x00\x00\x1e\x00\x33\x00\x21\x00'\
b'\x40\x80\x40\x80\x40\x80\x40\x80\x21\x00\x33\x00\x1e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x12\x00\x2a\x00\x24\x00'\
b'\x00\x00\x1e\x00\x33\x00\x21\x00\x40\x80\x40\x80\x40\x80\x40\x80'\
b'\x21\x00\x33\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x12\x00\x12\x00\x00\x00\x1e\x00\x33\x00\x21\x00'\
b'\x40\x80\x40\x80\x40\x80\x40\x80\x21\x00\x33\x00\x1e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x41\x22\x14\x08\x14\x22\x41\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x80\x1f\x00\x31\x00\x23\x00'\
b'\x44\x80\x4c\x80\x48\x80\x50\x80\x31\x00\x63\x00\x5e\x00\x80\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x10\x00\x18\x00\x04\x00'\
b'\x00\x00\x73\x80\x21\x00\x21\x00\x21\x00\x21\x00\x21\x00\x21\x00'\
b'\x21\x00\x33\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x02\x00\x06\x00\x08\x00\x00\x00\x73\x80\x21\x00\x21\x00'\
b'\x21\x00\x21\x00\x21\x00\x21\x00\x21\x00\x33\x00\x1e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x08\x00\x1c\x00\x22\x00'\
b'\x00\x00\x73\x80\x21\x00\x21\x00\x21\x00\x21\x00\x21\x00\x21\x00'\
b'\x21\x00\x33\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x12\x00\x12\x00\x00\x00\x73\x80\x21\x00\x21\x00'\
b'\x21\x00\x21\x00\x21\x00\x21\x00\x21\x00\x33\x00\x1e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x02\x00\x06\x00\x08\x00'\
b'\x00\x00\xe3\x80\x41\x00\x22\x00\x22\x00\x14\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x70\x20\x3c\x26\x22\x22\x26\x3c\x20\x70'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x38\x6c'\
b'\x44\x48\x70\x58\x4c\x44\x54\xd8\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x20\x30\x08\x00\x38\x64\x0c\x34\x44\x64\x3a'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x04\x0c\x10'\
b'\x00\x38\x64\x0c\x34\x44\x64\x3a\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x10\x38\x44\x00\x38\x64\x0c\x34\x44\x64\x3a'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x24\x54\x48'\
b'\x00\x38\x64\x0c\x34\x44\x64\x3a\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x28\x28\x00\x38\x64\x0c\x34\x44\x64\x3a'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x18\x24\x18'\
b'\x00\x38\x64\x0c\x34\x44\x64\x3a\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x3f\x80\x64\xc0\x0f\x80\x34\x00\x44\x00\x66\x40\x3b\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x38\x64\x40\x40\x40\x62\x3c\x10\x08\x30\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x20\x30\x08\x00\x38\x44\x7c\x40\x40\x62\x3c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x04\x0c\x10'\
b'\x00\x38\x44\x7c\x40\x40\x62\x3c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x10\x38\x44\x00\x38\x44\x7c\x40\x40\x62\x3c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x28\x28'\
b'\x00\x38\x44\x7c\x40\x40\x62\x3c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\x80\xc0\x20\x00\xc0\x40\x40\x40\x40\x40\xe0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x20\x60\x80'\
b'\x00\xc0\x40\x40\x40\x40\x40\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x20\x70\x88\x00\x60\x20\x20\x20\x20\x20\x70'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\xa0\xa0'\
b'\x00\xc0\x40\x40\x40\x40\x40\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x6c\x30\x48\x3c\x6c\x44\x44\x44\x6c\x38'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x24\x54\x48'\
b'\x00\xd8\x6c\x44\x44\x44\x44\xee\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x20\x30\x08\x00\x38\x6c\x44\x44\x44\x6c\x38'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x08\x18\x20'\
b'\x00\x38\x6c\x44\x44\x44\x6c\x38\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x10\x38\x44\x00\x38\x6c\x44\x44\x44\x6c\x38'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x24\x54\x48'\
b'\x00\x38\x6c\x44\x44\x44\x6c\x38\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x28\x28\x00\x38\x6c\x44\x44\x44\x6c\x38'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x08\x08\x00\x7f\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x02\x3c\x6c\x44\x44\x44\x6c\x78'\
b'\x80\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x20\x30\x08'\
b'\x00\xcc\x44\x44\x44\x44\x6c\x36\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x08\x18\x20\x00\xcc\x44\x44\x44\x44\x6c\x36'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x10\x38\x44'\
b'\x00\xcc\x44\x44\x44\x44\x6c\x36\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x28\x28\x00\xcc\x44\x44\x44\x44\x6c\x36'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x04\x0c\x10'\
b'\x00\xee\x44\x44\x28\x28\x10\x30\x20\xa0\xc0\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\xc0\x40\x40\x58\x6c\x44\x44\x44\x6c\x58'\
b'\x40\x40\xe0\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x28\x28'\
b'\x00\xee\x44\x44\x28\x28\x10\x30\x20\xa0\xc0'

_sparse =\
b'\x20\x00\x03\x00\x21\x00\x06\x00\x22\x00\x09\x00\x23\x00\x0c\x00'\
b'\x24\x00\x0f\x00\x25\x00\x12\x00\x26\x00\x17\x00\x27\x00\x1c\x00'\
b'\x28\x00\x1f\x00\x29\x00\x22\x00\x2a\x00\x25\x00\x2b\x00\x28\x00'\
b'\x2c\x00\x2b\x00\x2d\x00\x2e\x00\x2e\x00\x31\x00\x2f\x00\x34\x00'\
b'\x30\x00\x37\x00\x31\x00\x3a\x00\x32\x00\x3d\x00\x33\x00\x40\x00'\
b'\x34\x00\x43\x00\x35\x00\x46\x00\x36\x00\x49\x00\x37\x00\x4c\x00'\
b'\x38\x00\x4f\x00\x39\x00\x52\x00\x3a\x00\x55\x00\x3b\x00\x58\x00'\
b'\x3c\x00\x5b\x00\x3d\x00\x5e\x00\x3e\x00\x61\x00\x3f\x00\x64\x00'\
b'\x40\x00\x67\x00\x41\x00\x6c\x00\x42\x00\x71\x00\x43\x00\x76\x00'\
b'\x44\x00\x7b\x00\x45\x00\x80\x00\x46\x00\x85\x00\x47\x00\x88\x00'\
b'\x48\x00\x8d\x00\x49\x00\x92\x00\x4a\x00\x95\x00\x4b\x00\x98\x00'\
b'\x4c\x00\x9d\x00\x4d\x00\xa2\x00\x4e\x00\xa7\x00\x4f\x00\xac\x00'\
b'\x50\x00\xb1\x00\x51\x00\xb4\x00\x52\x00\xb9\x00\x53\x00\xbe\x00'\
b'\x54\x00\xc1\x00\x55\x00\xc6\x00\x56\x00\xcb\x00\x57\x00\xd0\x00'\
b'\x58\x00\xd5\x00\x59\x00\xda\x00\x5a\x00\xdf\x00\x5b\x00\xe2\x00'\
b'\x5c\x00\xe5\x00\x5d\x00\xe8\x00\x5e\x00\xeb\x00\x5f\x00\xee\x00'\
b'\x60\x00\xf1\x00\x61\x00\xf4\x00\x62\x00\xf7\x00\x63\x00\xfa\x00'\
b'\x64\x00\xfd\x00\x65\x00\x00\x01\x66\x00\x03\x01\x67\x00\x06\x01'\
b'\x68\x00\x09\x01\x69\x00\x0c\x01\x6a\x00\x0f\x01\x6b\x00\x12\x01'\
b'\x6c\x00\x15\x01\x6d\x00\x18\x01\x6e\x00\x1d\x01\x6f\x00\x20\x01'\
b'\x70\x00\x23\x01\x71\x00\x26\x01\x72\x00\x29\x01\x73\x00\x2c\x01'\
b'\x74\x00\x2f\x01\x75\x00\x32\x01\x76\x00\x35\x01\x77\x00\x38\x01'\
b'\x78\x00\x3d\x01\x79\x00\x40\x01\x7a\x00\x43\x01\x7b\x00\x46\x01'\
b'\x7c\x00\x49\x01\x7d\x00\x4c\x01\x7e\x00\x4f\x01\xa1\x00\x52\x01'\
b'\xa2\x00\x55\x01\xa3\x00\x58\x01\xa4\x00\x5b\x01\xa5\x00\x5e\x01'\
b'\xa6\x00\x61\x01\xa7\x00\x64\x01\xa8\x00\x67\x01\xa9\x00\x6a\x01'\
b'\xaa\x00\x6f\x01\xab\x00\x72\x01\xac\x00\x75\x01\xae\x00\x7a\x01'\
b'\xaf\x00\x7f\x01\xb0\x00\x82\x01\xb1\x00\x85\x01\xb2\x00\x88\x01'\
b'\xb3\x00\x8b\x01\xb4\x00\x8e\x01\xb5\x00\x91\x01\xb6\x00\x94\x01'\
b'\xb7\x00\x97\x01\xb8\x00\x9a\x01\xb9\x00\x9d\x01\xba\x00\xa0\x01'\
b'\xbb\x00\xa3\x01\xbc\x00\xa6\x01\xbd\x00\xab\x01\xbe\x00\xb0\x01'\
b'\xbf\x00\xb5\x01\xc0\x00\xb8\x01\xc1\x00\xbd\x01\xc2\x00\xc2\x01'\
b'\xc3\x00\xc7\x01\xc4\x00\xcc\x01\xc5\x00\xd1\x01\xc6\x00\xd6\x01'\
b'\xc7\x00\xdb\x01\xc8\x00\xe0\x01\xc9\x00\xe5\x01\xca\x00\xea\x01'\
b'\xcb\x00\xef\x01\xcc\x00\xf4\x01\xcd\x00\xf7\x01\xce\x00\xfa\x01'\
b'\xcf\x00\xfd\x01\xd0\x00\x00\x02\xd1\x00\x05\x02\xd2\x00\x0a\x02'\
b'\xd3\x00\x0f\x02\xd4\x00\x14\x02\xd5\x00\x19\x02\xd6\x00\x1e\x02'\
b'\xd7\x00\x23\x02\xd8\x00\x26\x02\xd9\x00\x2b\x02\xda\x00\x30\x02'\
b'\xdb\x00\x35\x02\xdc\x00\x3a\x02\xdd\x00\x3f\x02\xde\x00\x44\x02'\
b'\xdf\x00\x47\x02\xe0\x00\x4a\x02\xe1\x00\x4d\x02\xe2\x00\x50\x02'\
b'\xe3\x00\x53\x02\xe4\x00\x56\x02\xe5\x00\x59\x02\xe6\x00\x5c\x02'\
b'\xe7\x00\x61\x02\xe8\x00\x64\x02\xe9\x00\x67\x02\xea\x00\x6a\x02'\
b'\xeb\x00\x6d\x02\xec\x00\x70\x02\xed\x00\x73\x02\xee\x00\x76\x02'\
b'\xef\x00\x79\x02\xf0\x00\x7c\x02\xf1\x00\x7f\x02\xf2\x00\x82\x02'\
b'\xf3\x00\x85\x02\xf4\x00\x88\x02\xf5\x00\x8b\x02\xf6\x00\x8e\x02'\
b'\xf7\x00\x91\x02\xf8\x00\x94\x02\xf9\x00\x97\x02\xfa\x00\x9a\x02'\
b'\xfb\x00\x9d\x02\xfc\x00\xa0\x02\xfd\x00\xa3\x02\xfe\x00\xa6\x02'\
b'\xff\x00\xa9\x02'

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

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 17
    return _mvfont[doff + 2:next_offs], 17, width
 
