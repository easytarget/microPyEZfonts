'''
    ezFBfont_25_ncenB18_ascii : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original ncenB18.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Copyright (c) 1984, 1987 Adobe Systems Incorporated. All Rights Reserved. Copyright (c) 1988, 1991 Digital Equipment Corporation. All Rights Reserved."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
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
    NOTICE "New Century Schoolbook is a trademark of Linotype-Hell AG and/or its subsidiaries."
'''
# Code generated by bdf2dict.py
# Font: ncenB18
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/ncenB18.bdf', '_', './ascii-char.set']
# Date: 2024-06-12 20:08:38

version = '0.33'
name = '-Adobe-New Century Schoolbook-Bold-R-Normal--25-180-100-100-P-149-ISO10646-1'
family = 'new century schoolbook'
weight = 'bold'
size = 25

def height():
    return 25

def baseline():
    return 20

def max_width():
    return 26

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

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'7'],
 33:[b'\x00\x00p\xf8\xf8\xf8pppppp  \x00\x00p\xf8\xf8p\x00\x00\x00\x00\x00',b'7'],
 34:[b'\x00\x00\xcc\xcc\xcc\xcc\xcc\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'8'],
 35:[b'\x00\x00\x00\x00\x0c\xc0\x0c\xc0\x0c\xc0\x0c\xc0\x0c\xc0\x7f\xf0\x7f\xf0\x19\x80\x19\x80\x19\x80\x19\x80\xff\xe0\xff\xe03\x003\x003\x003\x003\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 36:[b'\x04\x00\x04\x00\x1f\xc0t`d\xf0\xe4\xf0\xe4\xf0\xf4`\xfc\x00\xff\x00\x7f\xc0\x1f\xe0\x07\xf0\x05\xf0d\xf0\xf4p\xf4p\xf4`d\xe0?\x80\x04\x00\x04\x00\x04\x00\x00\x00\x00\x00',b'14'],
 37:[b'\x00\x00\x00\x00\x00\x00\x1e\x0e\x00{6\x00q\xcc\x00\xf1\x0c\x00\xe1\x18\x00\xe2\x18\x00\xe20\x00d0\x008`\x00\x00c\xc0\x00\xcf`\x00\xce \x01\x9e \x01\x9c \x03\x1c@\x03\x1c@\x06\x0c\x80\x06\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'21'],
 38:[b'\x00\x00\x00\x00\x00\x00\x01\xf0\x00\x078\x00\x0e\x18\x00\x0e\x18\x00\x0e\x18\x00\x0f0\x00\x0f\xe0\x00\x07\xc0\x00\x0f\xc0\x009\xe3\xf0q\xf1\xc0\xf0\xf1\x80\xf0y\x00\xf0\x7f\x00\xf0>\x10x\x1f\x10|?\xe0\x1f\xc7\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'22'],
 39:[b'\x00\x00\xc0\xc0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'6'],
 40:[b'\x00\x00\x04\x0c\x1800``\xe0\xe0\xe0\xe0\xe0\xe0\xe0``00\x18\x0c\x04\x00\x00',b'8'],
 41:[b'\x00\x00\x80\xc0`00\x18\x18\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x18\x1800`\xc0\x80\x00\x00',b'8'],
 42:[b'\x00\x00\x00\x00\x1c\x00\x1c\x00\xc9\x80\xeb\x80>\x00>\x00\xeb\x80\xc9\x80\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'11'],
 43:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\xff\xf0\xff\xf0\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 44:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\xf8\xf8x0 @\x80\x00',b'7'],
 45:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xfc\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'8'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\xf8\xf8p\x00\x00\x00\x00\x00',b'7'],
 47:[b'\x00\x00\x00\x00\x06\x00\x06\x00\x06\x00\x0c\x00\x0c\x00\x0c\x00\x18\x00\x18\x00\x18\x000\x000\x000\x00`\x00`\x00`\x00\xc0\x00\xc0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 48:[b'\x00\x00\x00\x00\x0f\x009\xc0p\xe0p\xe0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0p\xe0p\xe09\xc0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 49:[b'\x00\x00\x00\x00\x1e\x00\xfe\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00?\x00\xff\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 50:[b'\x00\x00\x00\x00\x1f\x00c\xc0\xe1\xe0\xf1\xe0\xf1\xe0\xf1\xe0a\xe0\x01\xc0\x03\xc0\x03\x80\x07\x00\x0e\x00\x18 0 p`\xff\xe0\xff\xe0\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 51:[b'\x00\x00\x00\x00\x0f\x801\xe0p\xe0x\xf0x\xf0x\xf00\xe0\x01\xc0\x0f\x00\x01\xc0\x00\xe0`\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xe0\xe0a\xe0\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 52:[b'\x00\x00\x00\x00\x00\xc0\x01\xc0\x03\xc0\x07\xc0\x07\xc0\x0f\xc0\x1b\xc0\x13\xc03\xc0c\xc0c\xc0\xc3\xc0\xff\xf0\xff\xf0\x03\xc0\x03\xc0\x03\xc0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 53:[b'\x00\x00\x00\x00\x7f\xf0\x7f\xe0\x7f\xc0@\x00@\x00@\x00_\x00q\xc0`\xe0\x00\xf0\x00\xf0\x00\xf0`\xf0\xf0\xf0\xf0\xf0\xf0\xe0a\xc0?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 54:[b'\x00\x00\x00\x00\x0f\x808\xc0q\xe0q\xe0\xf1\xe0\xf0\xc0\xf0\x00\xf7\x80\xf9\xe0\xf0\xe0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0p\xe0y\xe0\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 55:[b'\x00\x00\x00\x00\xff\xf0\xff\xf0\xff\xe0\xc0`\x80\xc0\x81\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x0f\x00\x0f\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x1e\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 56:[b'\x00\x00\x00\x00\x0f\x009\xc0p\xe0p\xe0p\xe0x\xe0|\xc0?\x80\x1f\x80?\xc0w\xe0\xe1\xf0\xe0\xf0\xe0p\xe0p\xe0`p\xc0\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 57:[b'\x00\x00\x00\x00\x1f\x80y\xe0p\xe0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0p\xf0y\xf0\x1e\xf0\x00\xf00\xf0x\xf0x\xe0x\xe01\xc0\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 58:[b'\x00\x00\x00\x00\x00\x00\x00\x00p\xf8\xf8p\x00\x00\x00\x00p\xf8\xf8p\x00\x00\x00\x00\x00',b'7'],
 59:[b'\x00\x00\x00\x00\x00\x00\x00\x00p\xf8\xf8p\x00\x00\x00\x00p\xf8\xf8x0 @\x80\x00',b'7'],
 60:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\xf0\x03\xc0\x0f\x00<\x00\xf0\x00\xf0\x00<\x00\x0f\x00\x03\xc0\x00\xf0\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 61:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xf0\xff\xf0\x00\x00\x00\x00\xff\xf0\xff\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 62:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x00<\x00\x0f\x00\x03\xc0\x00\xf0\x00\xf0\x03\xc0\x0f\x00<\x00\xf0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 63:[b'\x00\x00\x00\x00?\x00c\xc0\xf1\xe0\xf1\xe0a\xe0\x01\xe0\x01\xc0\x03\x80\x07\x00\x0c\x00\x18\x00\x18\x00\x00\x00\x00\x00\x1c\x00>\x00>\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'13'],
 64:[b'\x00\x00\x00\x00\x00\x00\x01\xfc\x00\x0f\x06\x00\x0c\x01\x800\x00\xc00\xdc\xc0c\xbc`g\x1c`\xc7\x1c`\xce\x1c`\xce8`\xce8@\xce8\xc0\xcey\x80g\xbf\x00`\x00\x008\x01\x00\x1c\x07\x00\x07\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'20'],
 65:[b'\x00\x00\x00\x00\x00\x00\x00`\x00\x00`\x00\x00\xf0\x00\x00\xf0\x00\x01x\x00\x01x\x00\x03<\x00\x02<\x00\x02<\x00\x06\x1e\x00\x04\x1e\x00\x07\xfe\x00\x0c\x0f\x00\x08\x0f\x00\x08\x0f\x00\x18\x07\x808\x07\x80\xfe\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'19'],
 66:[b'\x00\x00\x00\x00\x00\x00\xff\xf8\x00<>\x00<\x1f\x00<\x1f\x00<\x1f\x00<\x1f\x00<\x1e\x00<<\x00?\xf8\x00<\x1e\x00<\x0f\x00<\x0f\x80<\x0f\x80<\x0f\x80<\x0f\x80<\x0f\x80<\x1f\x00\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'19'],
 67:[b'\x00\x00\x00\x00\x00\x00\x03\xf9\x80\x0f\x0f\x80<\x03\x80<\x01\x80x\x01\x80x\x00\x80\xf8\x00\x80\xf8\x00\x00\xf8\x00\x00\xf8\x00\x00\xf8\x00\x00\xf8\x00\x00x\x00\x80x\x00\x80<\x01\x00<\x01\x00\x0f\x06\x00\x03\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'19'],
 68:[b'\x00\x00\x00\x00\x00\x00\xff\xf0\x00<<\x00<\x0f\x00<\x0f\x00<\x07\x80<\x07\x80<\x07\xc0<\x07\xc0<\x07\xc0<\x07\xc0<\x07\xc0<\x07\xc0<\x07\x80<\x07\x80<\x0f\x00<\x0f\x00<<\x00\xff\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'20'],
 69:[b'\x00\x00\x00\x00\x00\x00\xff\xfe\x00<\x1e\x00<\x06\x00<\x02\x00<\x02\x00<"\x00< \x00<`\x00?\xe0\x00<`\x00< \x00< \x00<\x02\x00<\x02\x00<\x02\x00<\x06\x00<\x1e\x00\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'18'],
 70:[b'\x00\x00\x00\x00\x00\x00\xff\xfe\x00<\x1e\x00<\x06\x00<\x02\x00<\x02\x00<"\x00< \x00<`\x00?\xe0\x00<`\x00< \x00< \x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'17'],
 71:[b'\x00\x00\x00\x00\x00\x00\x03\xf9\x80\x0f\x0f\x80<\x03\x80<\x01\x80x\x01\x80x\x00\x80\xf8\x00\x80\xf8\x00\x00\xf8\x00\x00\xf8\x00\x00\xf8\x0f\xc0\xf8\x07\x80x\x07\x80x\x07\x80<\x07\x80<\x07\x80\x0f\r\x80\x03\xf8\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'20'],
 72:[b'\x00\x00\x00\x00\x00\x00\xff\x1f\xe0<\x07\x80<\x07\x80<\x07\x80<\x07\x80<\x07\x80<\x07\x80<\x07\x80?\xff\x80<\x07\x80<\x07\x80<\x07\x80<\x07\x80<\x07\x80<\x07\x80<\x07\x80<\x07\x80\xff\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'21'],
 73:[b'\x00\x00\x00\x00\xff\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 74:[b'\x00\x00\x00\x00\x03\xfc\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0`\xf0\xf0\xf0\xf0\xf0\xe0\xf0\xc0\xe0a\xe0?\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'16'],
 75:[b'\x00\x00\x00\x00\x00\x00\xff\x0f\xc0<\x03\x00<\x06\x00<\x0c\x00<\x18\x00<0\x00<`\x00<\xe0\x00=\xf0\x00?\xf8\x00>\xf8\x00<|\x00<>\x00<\x1f\x00<\x1f\x00<\x0f\x80<\x07\xc0\xff\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'21'],
 76:[b'\x00\x00\x00\x00\x00\x00\xff\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x02\x00<\x02\x00<\x02\x00<\x06\x00<\x1e\x00\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'17'],
 77:[b"\x00\x00\x00\x00\x00\x00\xfc\x01\xfc<\x01\xf0>\x03\xf0>\x02\xf0.\x02\xf0/\x06\xf0'\x04\xf0'\x84\xf0'\x8c\xf0#\x88\xf0#\xc8\xf0#\xd8\xf0!\xd0\xf0!\xf0\xf0 \xe0\xf0 \xe0\xf0p`\xf0\xf8C\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",b'24'],
 78:[b'\x00\x00\x00\x00\x00\x00\xfc\x07\xf0>\x01\xc0\x1f\x00\x80\x1f\x80\x80\x1f\xc0\x80\x17\xe0\x80\x13\xf0\x80\x11\xf0\x80\x10\xf8\x80\x10|\x80\x10~\x80\x10?\x80\x10\x1f\x80\x10\x0f\x80\x10\x07\x80\x10\x03\x808\x01\x80\xfe\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'22'],
 79:[b'\x00\x00\x00\x00\x00\x00\x03\xf8\x00\x0f\x1e\x00<\x07\x80<\x07\x80x\x03\xc0x\x03\xc0\xf8\x03\xe0\xf8\x03\xe0\xf8\x03\xe0\xf8\x03\xe0\xf8\x03\xe0\xf8\x03\xe0x\x03\xc0x\x03\xc0<\x07\x80<\x07\x80\x0f\x1e\x00\x03\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'21'],
 80:[b'\x00\x00\x00\x00\x00\x00\xff\xfc\x00<\x1f\x00<\x0f\x00<\x0f\x80<\x0f\x80<\x0f\x80<\x0f\x80<\x0f\x00<\x1f\x00?\xf8\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'18'],
 81:[b'\x00\x00\x00\x00\x00\x00\x03\xf8\x00\x0f\x1e\x00<\x07\x80<\x07\x80x\x03\xc0x\x03\xc0\xf8\x03\xe0\xf8\x03\xe0\xf8\x03\xe0\xf8\x03\xe0\xf8\x03\xe0\xfb\xe3\xe0~s\xc0|3\xc0<3\x80<\x1b\x80\x0f\x1e\x00\x03\xfe\x00\x00\x0e\x00\x00\x0f \x00\x07\xc0\x00\x07\xc0\x00\x03\x80',b'21'],
 82:[b'\x00\x00\x00\x00\x00\x00\xff\xf8\x00<>\x00<\x1f\x00<\x1f\x00<\x1f\x00<\x1f\x00<\x1e\x00<<\x00?\xe0\x00<x\x00<<\x00<<\x00<>\x00<\x1e\x00<\x1f <\x0f <\x0f\xc0\xff\x87\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'21'],
 83:[b'\x00\x00\x00\x00\x0f\xc88x`\x18\xe0\x18\xe0\x08\xf0\x08\xfe\x00\xff\xc0\x7f\xf0?\xf8\x0f\xfc\x01\xfc\x80<\x80\x1c\xc0\x1c\xc0\x18\xf0p\x9f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'16'],
 84:[b'\x00\x00\x00\x00\x00\x00\xff\xff\x00\xe3\xc7\x00\xc3\xc3\x00\x83\xc1\x00\x83\xc1\x00\x83\xc1\x00\x03\xc0\x00\x03\xc0\x00\x03\xc0\x00\x03\xc0\x00\x03\xc0\x00\x03\xc0\x00\x03\xc0\x00\x03\xc0\x00\x03\xc0\x00\x03\xc0\x00\x03\xc0\x00\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'18'],
 85:[b'\x00\x00\x00\x00\x00\x00\xff\x0f\xe0<\x03\x80<\x01\x00<\x01\x00<\x01\x00<\x01\x00<\x01\x00<\x01\x00<\x01\x00<\x01\x00<\x01\x00<\x01\x00<\x01\x00<\x01\x00<\x02\x00\x1e\x02\x00\x1f\x8c\x00\x07\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'21'],
 86:[b'\x00\x00\x00\x00\x00\x00\xff\x0f\xe0<\x03\x80<\x03\x00\x1e\x02\x00\x1e\x02\x00\x1e\x06\x00\x0f\x04\x00\x0f\x04\x00\x0f\x0c\x00\x07\x88\x00\x07\x88\x00\x07\x98\x00\x03\xd0\x00\x03\xd0\x00\x01\xe0\x00\x01\xe0\x00\x00\xc0\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'19'],
 87:[b'\x00\x00\x00\x00\x00\x00\x00\x00\xff\x7f\x9f\xc0<\x1e\x07\x00<\x1e\x06\x00\x1e\x0f\x04\x00\x1e\x0f\x04\x00\x1e\x0f\x0c\x00\x0f\x1f\x88\x00\x0f\x17\x88\x00\x0f\x17\x98\x00\x07\xb3\xd0\x00\x07\xa3\xd0\x00\x07\xa3\xf0\x00\x03\xe1\xe0\x00\x03\xc1\xe0\x00\x03\xc1\xe0\x00\x01\xc0\xc0\x00\x01\x80\xc0\x00\x01\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'26'],
 88:[b'\x00\x00\x00\x00\x00\x00\xff\x87\xe0>\x01\x80\x1f\x03\x00\x1f\x86\x00\x0f\x8c\x00\x07\xd8\x00\x03\xf0\x00\x03\xe0\x00\x01\xf0\x00\x00\xf8\x00\x01\xf8\x00\x03|\x00\x06>\x00\x04\x1f\x00\x0c\x1f\x00\x18\x0f\x800\x07\xc0\xfc\x1f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'20'],
 89:[b'\x00\x00\x00\x00\x00\x00\xff\x0f\xc0<\x03\x00\x1e\x02\x00\x1e\x06\x00\x0f\x04\x00\x0f\x0c\x00\x07\x88\x00\x07\x98\x00\x03\xd0\x00\x03\xf0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x01\xe0\x00\x07\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'18'],
 90:[b'\x00\x00\x00\x00\x00\x00\x7f\xfe\x00p>\x00`|\x00@x\x00@\xf8\x00\x00\xf0\x00\x01\xe0\x00\x03\xe0\x00\x03\xc0\x00\x07\x80\x00\x0f\x80\x00\x0f\x00\x00\x1e\x00\x00>\x02\x00<\x02\x00x\x06\x00\xf8\x0e\x00\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'17'],
 91:[b'\x00\x00\xfc\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xfc\x00\x00',b'8'],
 92:[b'\x00\x00\x00\x00\xc0\x00\xe0\x00\xe0\x00p\x00p\x008\x008\x00\x1c\x00\x1c\x00\x0e\x00\x0e\x00\x07\x00\x07\x00\x03\x80\x03\x80\x01\xc0\x01\xc0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'12'],
 93:[b'\x00\x00\xfc\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\xfc\x00\x00',b'8'],
 94:[b'\x00\x00\x00\x00\x0c\x00\x0c\x00\x1e\x00\x1e\x003\x003\x00a\x80a\x80\xc0\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'15'],
 95:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xf0\xff\xf0\x00\x00',b'12'],
 96:[b'\x00\x00\xe0\xe0p0\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'7'],
 97:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\xf1\xe0\xf0\xf0`\xf0\x01\xf0\x0e\xf0x\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf9\xfc~8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'15'],
 98:[b"\x00\x00\x00\x00\xfc\x00<\x00<\x00<\x00<\x00<\x00=\xf0?\x1c>\x1e<\x0e<\x0f<\x0f<\x0f<\x0f<\x0e<\x1e>\x1c'\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",b'16'],
 99:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf08xxxp0\xf0\x00\xf0\x00\xf0\x00\xf0\x00x\x08x\x08<0\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 100:[b'\x00\x00\x00\x00\x00\x00\x00\xfc\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x0f\xbc\x008\xfc\x00x|\x00p<\x00\xf0<\x00\xf0<\x00\xf0<\x00\xf0<\x00p<\x00x|\x008\xfc\x00\x0f\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'17'],
 101:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xc08pxxp8\xf0<\xff\xfc\xf0\x00\xf0\x00x\x08x\x08<0\x0f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'15'],
 102:[b'\x00\x00\x00\x00\x07\xc0\x1c\xc0\x1c\xc0<@<\x00<\x00\xff\x80<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 103:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x1f\xf8y\xe0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0y\xe0?\x80`\x00\xe0\x00\xff\xc0\x7f\xf0\x7f\xf8`8\xc0\x18\xe00\x7f\xe0',b'15'],
 104:[b'\x00\x00\x00\x00\x00\x00\xfc\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\xf8\x00=\xfc\x00>>\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00\xfe?\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'18'],
 105:[b'\x00\x00\x00\x00\x18\x00<\x00<\x00\x18\x00\x00\x00\x00\x00\xfc\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 106:[b'\x00\x00\x06\x0e\x0e\x06\x00\x00>\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\xce\xcex',b'7'],
 107:[b'\x00\x00\x00\x00\x00\x00\xfc\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\x00\x00<\xfe\x00<8\x00<0\x00<`\x00<\xc0\x00?\xc0\x00?\xe0\x00<\xf0\x00<x\x00<<\x00<\x1e\x00\xff\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'17'],
 108:[b'\x00\x00\x00\x00\xfc\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00<\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 109:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xf0\xf0\x00=\xf9\xf8\x00>~|\x00<<<\x00<<<\x00<<<\x00<<<\x00<<<\x00<<<\x00<<<\x00<<<\x00\xfe~\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'25'],
 110:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xf8\x00=\xfc\x00>>\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00\xfe?\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'18'],
 111:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xc08pxxp8\xf0<\xf0<\xf0<\xf0<p8xx8p\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'15'],
 112:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfd\xf0?\x1c<\x1e<\x0e<\x0f<\x0f<\x0f<\x0f<\x0e>\x1e?\x1c=\xf0<\x00<\x00<\x00<\x00\xff\x00',b'16'],
 113:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x84<\xecx<p<\xf0<\xf0<\xf0<\xf0<p<x|8\xfc\x0f\xbc\x00<\x00<\x00<\x00<\x00\xff',b'16'],
 114:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xe0=\xf0>\xf0<`<\x00<\x00<\x00<\x00<\x00<\x00<\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'12'],
 115:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x80c\x80\xc1\x80\xe0\x80\xfc\x00\xff\x80\x7f\xc0\x0f\xc0\x81\xc0\xc0\xc0\xe1\x80\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'11'],
 116:[b'\x00\x00\x00\x00\x00\x00\x04\x00\x0c\x00\x0c\x00\x1c\x00<\x00\xff\x80<\x00<\x00<\x00<\x00<\x00<\x00<\x00<@<@\x1f\x80\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 117:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe~\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00<\x1e\x00>>\x00\x1f\xde\x00\x0f\x9f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'18'],
 118:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x1e<\x04\x1e\x0c\x1e\x08\x0f\x18\x0f\x10\x07\xb0\x07\xa0\x03\xe0\x03\xc0\x01\xc0\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'15'],
 119:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff?<<\x1e\x08<\x1e\x08\x1e?\x18\x1e/\x10\x1e/\x10\x0fg\xb0\x0fG\xa0\x07\xc3\xe0\x07\x83\xc0\x03\x81\xc0\x03\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'22'],
 120:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x1f>\x0c\x1f\x18\x0f\xb0\x07\xe0\x03\xc0\x01\xe0\x03\xf0\x06\xf8\x0c|\x18>|\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'16'],
 121:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe><\x0c\x1e\x08\x1e\x18\x0f\x10\x0f0\x07\xa0\x07\xe0\x03\xc0\x03\xc0\x01\xc0\x01\x80\x01\x80a\x00\xf3\x00\xfe\x00x\x00',b'15'],
 122:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xe0\xe1\xe0\xc3\xe0\x87\xc0\x8f\x80\x0f\x00\x1e\x00> | \xf8`\xf0\xe0\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'12'],
 123:[b'\x00\x00\x1c0ppppppp`\xc0`ppppppp0\x1c\x00\x00',b'8'],
 124:[b'\x00\x00\x00\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'15'],
 125:[b'\x00\x00\xe008888888\x18\x0c\x1888888880\xe0\x00\x00',b'8'],
 126:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008 ~p\xff\xf0\xe7\xe0A\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'15'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 25, int(_g[c][1])

