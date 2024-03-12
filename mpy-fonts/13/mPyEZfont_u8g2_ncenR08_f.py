'''
    mPyEZfont_u8g2_ncenR08_f.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original ncenR08.bdf font file was sourced from the U8G2 project:
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
# Font: ncenR08.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/f-char.set u8g2/tools/font/bdf/ncenR08.bdf 0 tmp_mPyEZfont_u8g2_ncenR08_f.py
version = '0.33'

def height():
    return 13

def baseline():
    return 11

def max_width():
    return 12

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
b'\x05\x00\x00\x00\x00\x60\x90\x10\x20\x40\x00\x40\x40\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x40\x40\x40\x40\x40\x00\x40\x40\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x50\x50\x50\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x14\x14\x7e\x28\x28\xfc\x50\x50\x00\x00\x00'\
b'\x05\x00\x00\x00\x20\x70\xa0\xa0\x60\x50\x50\x50\xe0\x40\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x64\x00\x94\x00\x98\x00\x68\x00'\
b'\x16\x00\x19\x00\x29\x00\x26\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x30\x00\x48\x00\x50\x00\x26\x00'\
b'\x54\x00\x88\x00\x8c\x80\x73\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x40\x40\x40\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x20\x40\x40\x80\x80\x80\x40\x40\x20\x00\x00'\
b'\x04\x00\x00\x00\x00\x80\x40\x40\x20\x20\x20\x40\x40\x80\x00\x00'\
b'\x06\x00\x00\x00\x00\x20\xa8\x70\xa8\x20\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x20\x20\xf8\x20\x20\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x40\x80\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x40\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x20\x20\x20\x40\x40\x40\x80\x80\x80\x00\x00'\
b'\x05\x00\x00\x00\x00\x60\x90\x90\x90\x90\x90\x90\x60\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x20\x60\x20\x20\x20\x20\x20\x70\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x60\x90\x90\x10\x20\x40\x90\xf0\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x60\x90\x10\x60\x10\x90\x90\x60\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x10\x30\x50\x50\x90\xf8\x10\x38\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\xf0\x80\x80\xe0\x10\x10\x90\x60\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x70\x90\x80\xe0\x90\x90\x90\x60\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\xf0\x90\x20\x20\x20\x40\x40\x40\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x60\x90\x90\x60\x90\x90\x90\x60\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x60\x90\x90\x90\x70\x10\x90\xe0\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x40\x40\x00\x40\x40\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x40\x40\x00\x40\x40\x80\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x0c\x30\xc0\x30\x0c\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\xc0\x30\x0c\x30\xc0\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x60\x90\x10\x20\x40\x00\x40\x40\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x3c\x00\x42\x00\x81\x00\x9d\x00\xa5\x00'\
b'\xad\x00\xb6\x00\x80\x00\x40\x00\x3c\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x10\x10\x28\x28\x44\x7c\x44\xee\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xf8\x44\x44\x78\x44\x44\x44\xf8\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x3c\x44\x80\x80\x80\x80\x44\x38\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\xf8\x44\x42\x42\x42\x42\x44\xf8\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xfc\x44\x54\x70\x50\x44\x44\xfc\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xfc\x44\x54\x70\x50\x40\x40\xe0\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x3c\x44\x80\x80\x8e\x84\x44\x38\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\xe7\x00\x42\x00\x42\x00\x7e\x00'\
b'\x42\x00\x42\x00\x42\x00\xe7\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\xe0\x40\x40\x40\x40\x40\x40\xe0\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x70\x20\x20\x20\x20\xa0\xa0\xc0\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\xe6\x44\x48\x50\x70\x48\x44\xee\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xe0\x40\x40\x40\x40\x44\x44\xfc\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\xc1\x80\x63\x00\x63\x00\x55\x00'\
b'\x55\x00\x55\x00\x49\x00\xeb\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\xe7\x00\x62\x00\x52\x00\x52\x00'\
b'\x4a\x00\x4a\x00\x46\x00\xe6\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x38\x44\x82\x82\x82\x82\x44\x38\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xf8\x44\x44\x44\x78\x40\x40\xe0\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x38\x44\x82\x82\x82\xb2\x4c\x38\x06\x00\x00'\
b'\x08\x00\x00\x00\x00\xf8\x44\x44\x48\x78\x44\x44\xc6\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x78\x88\x80\xe0\x18\x08\x88\xf0\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\xfe\x92\x92\x10\x10\x10\x10\x38\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\xee\x44\x44\x44\x44\x44\x44\x38\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\xee\x44\x44\x44\x28\x28\x10\x10\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\xee\xe0\x44\x40\x44\x40\x2a\x80'\
b'\x2a\x80\x2a\x80\x11\x00\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xcc\x48\x48\x30\x30\x48\x48\xcc\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\xc6\x44\x28\x28\x10\x10\x10\x38\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\xf8\x88\x90\x20\x20\x48\x88\xf8\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\xc0\x80\x80\x80\x80\x80\x80\x80\xc0\x00\x00'\
b'\x05\x00\x00\x00\x00\x80\x80\x40\x40\x20\x20\x10\x10\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\xc0\x40\x40\x40\x40\x40\x40\x40\xc0\x00\x00'\
b'\x06\x00\x00\x00\x00\x20\x20\x50\x50\x88\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x00\x00'\
b'\x03\x00\x00\x00\x00\x80\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x60\x90\x70\x90\xf8\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\xc0\x40\x40\x70\x48\x48\x48\x70\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x70\x90\x80\x90\x60\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x30\x10\x10\x70\x90\x90\x90\x78\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x60\x90\xf0\x80\x70\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x30\x50\x40\xe0\x40\x40\x40\xe0\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x78\x90\xa0\x40\x78\x88\x70\x00'\
b'\x07\x00\x00\x00\x00\xc0\x40\x40\x70\x48\x48\x48\xec\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x40\x00\xc0\x40\x40\x40\xe0\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x40\x00\xc0\x40\x40\x40\x40\x40\x80\x00'\
b'\x07\x00\x00\x00\x00\xc0\x40\x40\x58\x50\x70\x48\xec\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\xc0\x40\x40\x40\x40\x40\x40\xe0\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb6\x00'\
b'\x49\x00\x49\x00\x49\x00\xed\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\xb0\x48\x48\x48\xec\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x60\x90\x90\x90\x60\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x60\x90\x90\x90\xe0\x80\xc0\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x68\x90\x90\x90\x70\x10\x38\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\xd0\x60\x40\x40\xe0\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x70\x80\x60\x10\xe0\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\x00\x80\x80\xc0\x80\x80\x80\x60\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x90\x90\x90\x90\x68\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\xdc\x88\x50\x50\x20\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x93\xaa\xaa\x44\x44\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\xd8\x50\x20\x50\xd8\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\xdc\x88\x50\x50\x20\x20\xc0\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\xf0\x20\x40\x80\xf0\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x20\x40\x40\x40\x80\x40\x40\x40\x20\x00\x00'\
b'\x06\x00\x00\x00\x00\x20\x20\x20\x20\x20\x20\x20\x20\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x80\x40\x40\x40\x20\x40\x40\x40\x80\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x64\x98\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x40\x40\x00\x40\x40\x40\x40\x40\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x10\x78\xa8\xa0\xc8\x70\x40\x00\x00'\
b'\x07\x00\x00\x00\x00\x38\x48\x40\xf8\x20\x20\x44\xf8\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x00\x84\x78\x48\x48\x78\x84\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\xc6\x44\x28\x6c\x10\x7c\x10\x38\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x20\x20\x20\x00\x00\x20\x20\x20\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x70\x90\x80\x60\x90\x90\x60\x10\x90\xe0\x00'\
b'\x04\x00\x00\x00\x00\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x3e\x00\x41\x00\x9c\x80\xa4\x80'\
b'\xa0\x80\x9c\x80\x41\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\xe0\x20\x60\xb0\x00\xf0\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x48\x90\x48\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x08\x08\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x3e\x00\x41\x00\xbc\x80\x94\x80'\
b'\x98\x80\xb6\x80\x41\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x40\xa0\xa0\x40\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x20\xf8\x20\x00\xf8\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\x60\xa0\x40\xe0\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\xe0\x40\x20\xc0\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\x40\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x90\x90\x90\x90\xe8\x80\x80\x00'\
b'\x07\x00\x00\x00\x00\x7c\xa8\xa8\xa8\x68\x28\x28\x28\x28\x7c\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x40\x40\x00\x00\x00\x00\x00'\
b'\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x40\xc0\x00'\
b'\x03\x00\x00\x00\x00\x40\xc0\x40\xe0\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x60\x90\x90\x60\x00\xf0\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x90\x48\x90\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x48\xc8\x50\xf0\x24\x2c\x5e\x44\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x48\xc8\x50\xf0\x2c\x34\x48\x5c\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xe8\x48\x30\xd0\x24\x2c\x5e\x44\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x20\x20\x00\x20\x40\x80\x90\x60\x00'\
b'\x08\x00\x20\x10\x00\x10\x10\x28\x28\x44\x7c\x44\xee\x00\x00\x00'\
b'\x08\x00\x08\x10\x00\x10\x10\x28\x28\x44\x7c\x44\xee\x00\x00\x00'\
b'\x08\x00\x10\x28\x00\x10\x10\x28\x28\x44\x7c\x44\xee\x00\x00\x00'\
b'\x08\x00\x14\x28\x00\x10\x10\x28\x28\x44\x7c\x44\xee\x00\x00\x00'\
b'\x08\x00\x00\x28\x00\x10\x10\x28\x28\x44\x7c\x44\xee\x00\x00\x00'\
b'\x08\x00\x10\x28\x10\x10\x10\x28\x28\x44\x7c\x44\xee\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x00\x00\x1f\xc0\x0c\x40\x15\x40\x17\x00'\
b'\x3d\x00\x24\x40\x44\x40\xe7\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x3c\x44\x80\x80\x80\x80\x44\x38\x10\x30\x00'\
b'\x07\x00\x20\x10\x00\xfc\x44\x54\x70\x50\x44\x44\xfc\x00\x00\x00'\
b'\x07\x00\x08\x10\x00\xfc\x44\x54\x70\x50\x44\x44\xfc\x00\x00\x00'\
b'\x07\x00\x10\x28\x00\xfc\x44\x54\x70\x50\x44\x44\xfc\x00\x00\x00'\
b'\x07\x00\x00\x28\x00\xfc\x44\x54\x70\x50\x44\x44\xfc\x00\x00\x00'\
b'\x04\x00\x80\x40\x00\xe0\x40\x40\x40\x40\x40\x40\xe0\x00\x00\x00'\
b'\x04\x00\x20\x40\x00\xe0\x40\x40\x40\x40\x40\x40\xe0\x00\x00\x00'\
b'\x04\x00\x40\xa0\x00\xe0\x40\x40\x40\x40\x40\x40\xe0\x00\x00\x00'\
b'\x04\x00\x00\xa0\x00\xe0\x40\x40\x40\x40\x40\x40\xe0\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\xf8\x44\x42\xe2\x42\x42\x44\xf8\x00\x00\x00'\
b'\x09\x00\x14\x00\x28\x00\x00\x00\xe7\x00\x62\x00\x52\x00\x52\x00'\
b'\x4a\x00\x4a\x00\x46\x00\xe6\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x20\x10\x00\x38\x44\x82\x82\x82\x82\x44\x38\x00\x00\x00'\
b'\x08\x00\x08\x10\x00\x38\x44\x82\x82\x82\x82\x44\x38\x00\x00\x00'\
b'\x08\x00\x10\x28\x00\x38\x44\x82\x82\x82\x82\x44\x38\x00\x00\x00'\
b'\x08\x00\x14\x28\x00\x38\x44\x82\x82\x82\x82\x44\x38\x00\x00\x00'\
b'\x08\x00\x00\x28\x00\x38\x44\x82\x82\x82\x82\x44\x38\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x88\x50\x20\x50\x88\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x1d\x00\x22\x00\x45\x00\x49\x00'\
b'\x51\x00\x61\x00\x62\x00\x9c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x20\x10\x00\xee\x44\x44\x44\x44\x44\x44\x38\x00\x00\x00'\
b'\x08\x00\x08\x10\x00\xee\x44\x44\x44\x44\x44\x44\x38\x00\x00\x00'\
b'\x08\x00\x10\x28\x00\xee\x44\x44\x44\x44\x44\x44\x38\x00\x00\x00'\
b'\x08\x00\x00\x28\x00\xee\x44\x44\x44\x44\x44\x44\x38\x00\x00\x00'\
b'\x08\x00\x08\x10\x00\xc6\x44\x28\x28\x10\x10\x10\x38\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\xc0\x78\x44\x44\x44\x78\x40\xe0\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x30\x48\x48\x58\x44\x44\x54\xd8\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x40\x20\x00\x60\x90\x70\x90\xf8\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x20\x40\x00\x60\x90\x70\x90\xf8\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x20\x50\x00\x60\x90\x70\x90\xf8\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x50\xa0\x00\x60\x90\x70\x90\xf8\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x50\x00\x60\x90\x70\x90\xf8\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x20\x50\x20\x60\x90\x70\x90\xf8\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x6c\x92\x7e\x90\xee\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x70\x90\x80\x90\x60\x20\x60\x00'\
b'\x05\x00\x00\x00\x00\x40\x20\x00\x60\x90\xf0\x80\x70\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x20\x40\x00\x60\x90\xf0\x80\x70\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x20\x50\x00\x60\x90\xf0\x80\x70\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x50\x00\x60\x90\xf0\x80\x70\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x80\x40\x00\xc0\x40\x40\x40\xe0\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x20\x40\x00\xc0\x40\x40\x40\xe0\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x40\xa0\x00\xc0\x40\x40\x40\xe0\x00\x00\x00'\
b'\x04\x00\x00\x00\x00\x00\xa0\x00\xc0\x40\x40\x40\xe0\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x50\x60\xa0\x60\x90\x90\x90\x60\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x28\x50\x00\xb0\x48\x48\x48\xec\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x40\x20\x00\x60\x90\x90\x90\x60\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x20\x40\x00\x60\x90\x90\x90\x60\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x20\x50\x00\x60\x90\x90\x90\x60\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x50\xa0\x00\x60\x90\x90\x90\x60\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x50\x00\x60\x90\x90\x90\x60\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x20\x00\xf8\x00\x20\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x68\x90\xb0\xd0\x60\x80\x00\x00'\
b'\x06\x00\x00\x00\x00\x40\x20\x00\x90\x90\x90\x90\x68\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x20\x40\x00\x90\x90\x90\x90\x68\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x20\x50\x00\x90\x90\x90\x90\x68\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x50\x00\x90\x90\x90\x90\x68\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x10\x20\x00\xdc\x88\x50\x50\x20\x20\xc0\x00'\
b'\x06\x00\x00\x00\x00\xc0\x40\x40\x70\x48\x48\x48\x70\x40\xe0\x00'\
b'\x06\x00\x00\x00\x00\x00\x50\x00\xdc\x88\x50\x50\x20\x20\xc0'

_sparse =\
b'\x20\x00\x02\x00\x21\x00\x04\x00\x22\x00\x06\x00\x23\x00\x08\x00'\
b'\x24\x00\x0a\x00\x25\x00\x0c\x00\x26\x00\x10\x00\x27\x00\x14\x00'\
b'\x28\x00\x16\x00\x29\x00\x18\x00\x2a\x00\x1a\x00\x2b\x00\x1c\x00'\
b'\x2c\x00\x1e\x00\x2d\x00\x20\x00\x2e\x00\x22\x00\x2f\x00\x24\x00'\
b'\x30\x00\x26\x00\x31\x00\x28\x00\x32\x00\x2a\x00\x33\x00\x2c\x00'\
b'\x34\x00\x2e\x00\x35\x00\x30\x00\x36\x00\x32\x00\x37\x00\x34\x00'\
b'\x38\x00\x36\x00\x39\x00\x38\x00\x3a\x00\x3a\x00\x3b\x00\x3c\x00'\
b'\x3c\x00\x3e\x00\x3d\x00\x40\x00\x3e\x00\x42\x00\x3f\x00\x44\x00'\
b'\x40\x00\x46\x00\x41\x00\x4a\x00\x42\x00\x4c\x00\x43\x00\x4e\x00'\
b'\x44\x00\x50\x00\x45\x00\x52\x00\x46\x00\x54\x00\x47\x00\x56\x00'\
b'\x48\x00\x58\x00\x49\x00\x5c\x00\x4a\x00\x5e\x00\x4b\x00\x60\x00'\
b'\x4c\x00\x62\x00\x4d\x00\x64\x00\x4e\x00\x68\x00\x4f\x00\x6c\x00'\
b'\x50\x00\x6e\x00\x51\x00\x70\x00\x52\x00\x72\x00\x53\x00\x74\x00'\
b'\x54\x00\x76\x00\x55\x00\x78\x00\x56\x00\x7a\x00\x57\x00\x7c\x00'\
b'\x58\x00\x80\x00\x59\x00\x82\x00\x5a\x00\x84\x00\x5b\x00\x86\x00'\
b'\x5c\x00\x88\x00\x5d\x00\x8a\x00\x5e\x00\x8c\x00\x5f\x00\x8e\x00'\
b'\x60\x00\x90\x00\x61\x00\x92\x00\x62\x00\x94\x00\x63\x00\x96\x00'\
b'\x64\x00\x98\x00\x65\x00\x9a\x00\x66\x00\x9c\x00\x67\x00\x9e\x00'\
b'\x68\x00\xa0\x00\x69\x00\xa2\x00\x6a\x00\xa4\x00\x6b\x00\xa6\x00'\
b'\x6c\x00\xa8\x00\x6d\x00\xaa\x00\x6e\x00\xae\x00\x6f\x00\xb0\x00'\
b'\x70\x00\xb2\x00\x71\x00\xb4\x00\x72\x00\xb6\x00\x73\x00\xb8\x00'\
b'\x74\x00\xba\x00\x75\x00\xbc\x00\x76\x00\xbe\x00\x77\x00\xc0\x00'\
b'\x78\x00\xc2\x00\x79\x00\xc4\x00\x7a\x00\xc6\x00\x7b\x00\xc8\x00'\
b'\x7c\x00\xca\x00\x7d\x00\xcc\x00\x7e\x00\xce\x00\xa1\x00\xd0\x00'\
b'\xa2\x00\xd2\x00\xa3\x00\xd4\x00\xa4\x00\xd6\x00\xa5\x00\xd8\x00'\
b'\xa6\x00\xda\x00\xa7\x00\xdc\x00\xa8\x00\xde\x00\xa9\x00\xe0\x00'\
b'\xaa\x00\xe4\x00\xab\x00\xe6\x00\xac\x00\xe8\x00\xae\x00\xea\x00'\
b'\xaf\x00\xee\x00\xb0\x00\xf0\x00\xb1\x00\xf2\x00\xb2\x00\xf4\x00'\
b'\xb3\x00\xf6\x00\xb4\x00\xf8\x00\xb5\x00\xfa\x00\xb6\x00\xfc\x00'\
b'\xb7\x00\xfe\x00\xb8\x00\x00\x01\xb9\x00\x02\x01\xba\x00\x04\x01'\
b'\xbb\x00\x06\x01\xbc\x00\x08\x01\xbd\x00\x0a\x01\xbe\x00\x0c\x01'\
b'\xbf\x00\x0e\x01\xc0\x00\x10\x01\xc1\x00\x12\x01\xc2\x00\x14\x01'\
b'\xc3\x00\x16\x01\xc4\x00\x18\x01\xc5\x00\x1a\x01\xc6\x00\x1c\x01'\
b'\xc7\x00\x20\x01\xc8\x00\x22\x01\xc9\x00\x24\x01\xca\x00\x26\x01'\
b'\xcb\x00\x28\x01\xcc\x00\x2a\x01\xcd\x00\x2c\x01\xce\x00\x2e\x01'\
b'\xcf\x00\x30\x01\xd0\x00\x32\x01\xd1\x00\x34\x01\xd2\x00\x38\x01'\
b'\xd3\x00\x3a\x01\xd4\x00\x3c\x01\xd5\x00\x3e\x01\xd6\x00\x40\x01'\
b'\xd7\x00\x42\x01\xd8\x00\x44\x01\xd9\x00\x48\x01\xda\x00\x4a\x01'\
b'\xdb\x00\x4c\x01\xdc\x00\x4e\x01\xdd\x00\x50\x01\xde\x00\x52\x01'\
b'\xdf\x00\x54\x01\xe0\x00\x56\x01\xe1\x00\x58\x01\xe2\x00\x5a\x01'\
b'\xe3\x00\x5c\x01\xe4\x00\x5e\x01\xe5\x00\x60\x01\xe6\x00\x62\x01'\
b'\xe7\x00\x64\x01\xe8\x00\x66\x01\xe9\x00\x68\x01\xea\x00\x6a\x01'\
b'\xeb\x00\x6c\x01\xec\x00\x6e\x01\xed\x00\x70\x01\xee\x00\x72\x01'\
b'\xef\x00\x74\x01\xf0\x00\x76\x01\xf1\x00\x78\x01\xf2\x00\x7a\x01'\
b'\xf3\x00\x7c\x01\xf4\x00\x7e\x01\xf5\x00\x80\x01\xf6\x00\x82\x01'\
b'\xf7\x00\x84\x01\xf8\x00\x86\x01\xf9\x00\x88\x01\xfa\x00\x8a\x01'\
b'\xfb\x00\x8c\x01\xfc\x00\x8e\x01\xfd\x00\x90\x01\xfe\x00\x92\x01'\
b'\xff\x00\x94\x01'

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

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 13
    return _mvfont[doff + 2:next_offs], 13, width
 
