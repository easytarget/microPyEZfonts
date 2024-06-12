'''
    ezFBfont_18_timB14_ascii : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original timB14.bdf font file was sourced from the U8G2 project:
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
    NOTICE "Times is a trademark of Linotype-Hell AG and/or its subsidiaries."
'''
# Code generated by bdf2dict.py
# Font: timB14
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/timB14.bdf', '_', './ascii-char.set']
# Date: 2024-06-12 20:09:17

version = '0.33'
name = '-Adobe-Times-Bold-R-Normal--20-140-100-100-P-100-ISO10646-1'
family = 'times'
weight = 'bold'
size = 20

def height():
    return 18

def baseline():
    return 14

def max_width():
    return 19

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'5'],
 33:[b'\x00@\xe0\xe0\xe0\xe0\xe0\xe0@@\x00\xe0\xe0\xe0\x00\x00\x00\x00',b'6'],
 34:[b'\x00\x00\xcc\x00\xcc\x00\xcc\x00\xcc\x00\x88\x00\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 35:[b'\x00\x00\x00\x00\x19\x80\x19\x80\x19\x80\x7f\x80\x7f\x803\x003\x00\xff\x80\xff\x80f\x00f\x00f\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 36:[b'\x18\x00~\x00\xdb\x00\xdb\x00\xd8\x00\xf8\x00|\x00>\x00\x1f\x00\x1f\x00\x1b\x00\xdb\x00\xdb\x00~\x00\x18\x00\x18\x00\x00\x00\x00\x00',b'9'],
 37:[b'\x00\x00\x00<\x18\x00w\xf0\x00\xe2`\x00\xe2@\x00\xe4\xc0\x00\xfd\x80\x00sx\x00\x06\xec\x00\x06\xc4\x00\r\xc4\x00\x19\xc8\x001\xf8\x000\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'18'],
 38:[b'\x00\x00\x1e\x003\x003\x003\x00:\x00\x1c\xf0<`^@\xcf\x80\xc7\x80\xe3\xc0\xff\xf8x\xf0\x00\x00\x00\x00\x00\x00\x00\x00',b'16'],
 39:[b'\x00\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'5'],
 40:[b'\x00\x08\x100``\xe0\xc0\xc0\xc0\xc0\xc0\xe0``0\x10\x08',b'6'],
 41:[b'\x00\x80@`008\x18\x18\x18\x18\x1880 `@\x80',b'6'],
 42:[b'\x00\x00\x18\x00\x18\x00\xdb\x00\xff\x00<\x00\xff\x00\xdb\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 43:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\xff\xc0\xff\xc0\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'11'],
 44:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ppp0`\xc0\x00',b'5'],
 45:[b'\x00\x00\x00\x00\x00\x00\x00\xf8\xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x00',b'6'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0\xe0\x00\x00\x00\x00',b'5'],
 47:[b'\x00\x18\x18\x18000 ```\xc0\xc0\xc0\x00\x00\x00\x00',b'6'],
 48:[b'\x00\x00<\x00f\x00g\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00f\x00f\x00<\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 49:[b'\x00\x00\x1c\x00<\x00\xfc\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 50:[b'\x00\x00<\x00~\x00\xcf\x00\x87\x00\x07\x00\x07\x00\x06\x00\x0c\x00\x18\x001\x00c\x00\xff\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 51:[b'\x00\x00<\x00~\x00\x8f\x00\x07\x00\x0e\x00\x1c\x00>\x00\x0f\x00\x07\x80\x03\x80\xc3\x00\xe6\x00|\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 52:[b'\x00\x00\x0e\x00\x1e\x00\x1e\x00.\x00.\x00N\x00\xce\x00\x8e\x00\xff\x00\xff\x00\x0e\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 53:[b'\x00\x00?\x00?\x00>\x00@\x00x\x00~\x00?\x00\x07\x80\x03\x80\x03\x80\xc3\x00\xe6\x00\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 54:[b'\x00\x00\x07\x00\x1c\x008\x00p\x00`\x00\xfc\x00\xe6\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00f\x00<\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 55:[b'\x00\x00\xff\x00\xff\x00\xfe\x00\x86\x00\x0c\x00\x0c\x00\x0c\x00\x18\x00\x18\x008\x000\x000\x00p\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 56:[b'\x00\x00<\x00f\x00\xe3\x00\xe3\x00\xf6\x00|\x00<\x00~\x00\xcf\x00\xc7\x00\xc3\x00\xe7\x00~\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 57:[b'\x00\x00<\x00f\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00g\x00?\x00\x07\x00\x06\x00\x0e\x00<\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 58:[b'\x00\x00\x00\x00\x00\xe0\xe0\xe0\x00\x00\x00\xe0\xe0\xe0\x00\x00\x00\x00',b'5'],
 59:[b'\x00\x00\x00\x00\x00ppp\x00\x00\x00ppp0`\xc0\x00',b'5'],
 60:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80\x0f\x00<\x00\xf0\x00\xc0\x00\xf0\x00<\x00\x0f\x00\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00',b'11'],
 61:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x80\xff\x80\x00\x00\x00\x00\xff\x80\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'11'],
 62:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00x\x00\x1e\x00\x07\x80\x01\x80\x07\x80\x1e\x00x\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'11'],
 63:[b'\x00\x00|\x00\xce\x00\xee\x00\xee\x00N\x00\x0c\x00\x18\x00\x10\x00\x10\x00\x00\x008\x008\x008\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 64:[b'\x00\x00\x00\x03\xe0\x00\x0f8\x008\x0c\x000\x04\x00s\xb6\x00gv\x00\xe7v\x00\xeef\x00\xeef\x00\xee\xec\x00\xef\xfc\x00g\xb8\x00p\x00\x008\x00\x00\x1e\x00\x00\x07\xf0\x00\x00\x00\x00',b'17'],
 65:[b'\x00\x00\x03\x00\x03\x80\x07\x80\x05\xc0\r\xc0\x08\xc0\x18\xe0\x10`\x1f\xf00p 8`8\xf8\xfc\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 66:[b'\x00\x00\xfe\x00s\x80q\xc0q\xc0q\xc0s\x80~\x00s\x80q\xc0q\xc0q\xc0s\x80\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'13'],
 67:[b'\x00\x00\x0f\x908\xf0ppp0\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00p\x00p0<\xe0\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 68:[b'\x00\x00\xff\x00q\xc0p\xe0p`ppppppppppp`p\xe0q\xc0\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 69:[b'\x00\x00\xff\xc0p\xc0p@p\x00p\x00q\x00\x7f\x00q\x00p\x00p\x00p@p\xc0\xff\xc0\x00\x00\x00\x00\x00\x00\x00\x00',b'13'],
 70:[b'\x00\x00\xff\xc0p\xc0p@p\x00p\x00q\x00\x7f\x00q\x00p\x00p\x00p\x00p\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'12'],
 71:[b'\x00\x00\x0f\x908\xf0ppp0\xe0\x00\xe0\x00\xe0\xf8\xe0p\xe0ppppp8\xf0\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00',b'15'],
 72:[b'\x00\x00\xf8\xf8pppppppppp\x7f\xf0pppppppppp\xf9\xf8\x00\x00\x00\x00\x00\x00\x00\x00',b'15'],
 73:[b'\x00\xf8ppppppppppp\xf8\x00\x00\x00\x00',b'7'],
 74:[b'\x00\x00\x1f\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\xee\x00\xec\x00x\x00\x00\x00\x00\x00',b'9'],
 75:[b'\x00\x00\xf9\xf0p\xc0q\x80s\x00v\x00|\x00|\x00~\x00w\x00w\x80s\xc0q\xe0\xf8\xf0\x00\x00\x00\x00\x00\x00\x00\x00',b'15'],
 76:[b'\x00\x00\xf8\x00p\x00p\x00p\x00p\x00p\x00p\x00p\x00p\x00p\x00p@p\xc0\xff\xc0\x00\x00\x00\x00\x00\x00\x00\x00',b'13'],
 77:[b'\x00\x00\x00\xf0\x1e\x00p\x1c\x00x<\x00x<\x00|\\\x00\\\\\x00^\xdc\x00N\x9c\x00O\x9c\x00G\x1c\x00G\x1c\x00C\x1c\x00\xe2>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'18'],
 78:[b'\x00\x00\xf0px x | ^ N O G\xa0C\xa0C\xe0A\xe0@\xe0\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 79:[b'\x00\x00\x0f\x808\xe0pppp\xe08\xe08\xe08\xe08\xe08pppp8\xe0\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00',b'15'],
 80:[b'\x00\x00\xff\x00s\x80q\xc0q\xc0q\xc0s\x80\x7f\x00p\x00p\x00p\x00p\x00p\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'12'],
 81:[b'\x00\x00\x0f\x808\xe0pppp\xe08\xe08\xe08\xe08\xe08pppp8\xe0\x0f\x80\x0f\x00\x07\x80\x03\xe0\x00\xf8',b'15'],
 82:[b'\x00\x00\xff\x00s\x80q\xc0q\xc0q\xc0s\x80\x7f\x00w\x00s\x80q\xc0q\xc0p\xe0\xf8\xf0\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 83:[b'\x00\x00\x1e\x80c\x80\xe1\x80\xe0\x00\xf8\x00|\x00?\x00\x0f\x80\x07\x80\x03\x80\xc3\x80\xe7\x00\xbc\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'11'],
 84:[b'\x00\x00\xff\xe0\xce`\x8e \x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'13'],
 85:[b'\x00\x00\xf8\xf0p p p p p p p p p p`8\xc0\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 86:[b'\x00\x00\xfc|x\x188\x10<0\x1c \x1e`\x1e@\x0e\xc0\x0f\x80\x07\x80\x07\x00\x03\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 87:[b'\x00\x00\x00\xfd\xf7\xc0y\xe1\x808\xe1\x00<\xe3\x00<\xe2\x00\x1cr\x00\x1ev\x00\x0et\x00\x0e\xbc\x00\x0f<\x00\x07<\x00\x06\x18\x00\x06\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'19'],
 88:[b'\x00\x00\xf8xx0<`\x1c\xc0\x0f\x80\x07\x00\x07\x80\x07\xc0\r\xc0\x18\xe00p`x\xf0\xfc\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 89:[b'\x00\x00\xfcxx08`<@\x1e\xc0\x0e\x80\x0f\x80\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x1f\xc0\x00\x00\x00\x00\x00\x00\x00\x00',b'14'],
 90:[b'\x00\x00\xff\xc0\xc3\xc0\x83\x80\x07\x80\x0f\x00\x0e\x00\x1e\x00<\x008\x00x\x00\xf0@\xe0\xc0\xff\xc0\x00\x00\x00\x00\x00\x00\x00\x00',b'13'],
 91:[b'\x00\xf0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xf0\x00',b'6'],
 92:[b'\x00\xc0\xc0\xc0``` 000\x18\x18\x18\x00\x00\x00\x00',b'5'],
 93:[b'\x00\xf000000000000000\xf0\x00',b'6'],
 94:[b'\x00\x00\x18\x00\x18\x00<\x00$\x00f\x00\xc3\x00\xc3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'11'],
 95:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x80\xff\x80',b'9'],
 96:[b'\x00\xe0p\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'6'],
 97:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00\xce\x00\xce\x00\x1e\x00n\x00\xce\x00\xce\x00\xfe\x00w\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 98:[b'\x00\x00\xf0\x00p\x00p\x00p\x00v\x00\x7f\x00s\x80s\x80s\x80s\x80s\x80s\x00n\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 99:[b'\x00\x00\x00\x00\x00>v\xe6\xe0\xe0\xe0\xe0v<\x00\x00\x00\x00',b'8'],
 100:[b'\x00\x00\x0f\x00\x07\x00\x07\x00\x07\x007\x00\x7f\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00w\x00;\x80\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 101:[b'\x00\x00\x00\x00\x00<v\xe6\xfe\xe0\xe0\xe0v<\x00\x00\x00\x00',b'8'],
 102:[b'\x00<ttp\xfcppppppp\xf8\x00\x00\x00\x00',b'6'],
 103:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\x80\xe7\x00\xe7\x00\xe7\x00\xe6\x00x\x00`\x00\xfe\x00\xff\x80\xe3\x80\xc1\x80\xe3\x00~\x00',b'9'],
 104:[b'\x00\x00\xf0\x00p\x00p\x00p\x00w\x00\x7f\x80s\x80s\x80s\x80s\x80s\x80s\x80\xfb\xc0\x00\x00\x00\x00\x00\x00\x00\x00',b'11'],
 105:[b'\x00```\x00\xf0ppppppp\xf8\x00\x00\x00\x00',b'5'],
 106:[b'\x00\x18\x18\x18\x008\x18\x18\x18\x18\x18\x18\x18\x18\x18\xd8\xd8p',b'5'],
 107:[b'\x00\x00\xf0\x00p\x00p\x00p\x00s\x80s\x00v\x00|\x00|\x00~\x00w\x00s\x80\xf7\xc0\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
 108:[b'\x00\xf0ppppppppppp\xf8\x00\x00\x00\x00',b'6'],
 109:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf78{\xdcs\x9cs\x9cs\x9cs\x9cs\x9cs\x9c\xfb\xde\x00\x00\x00\x00\x00\x00\x00\x00',b'16'],
 110:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe7\x00\x7f\x80s\x80s\x80s\x80s\x80s\x80s\x80\xfb\xc0\x00\x00\x00\x00\x00\x00\x00\x00',b'11'],
 111:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00f\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00f\x00<\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 112:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe6\x00\x7f\x00s\x80s\x80s\x80s\x80s\x80{\x00v\x00p\x00p\x00p\x00\xf8\x00',b'10'],
 113:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009\x00w\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00\xe7\x00\x7f\x007\x00\x07\x00\x07\x00\x07\x00\x0f\x80',b'9'],
 114:[b'\x00\x00\x00\x00\x00\xeevpppppp\xf8\x00\x00\x00\x00',b'8'],
 115:[b'\x00\x00\x00\x00\x00|\xcc\xe4\xf0x<\x9c\xcc\xf8\x00\x00\x00\x00',b'7'],
 116:[b'\x00\x00\x00\x100\xfcppppppt8\x00\x00\x00\x00',b'7'],
 117:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\x80s\x80s\x80s\x80s\x80s\x80s\x80\x7f\x80=\xc0\x00\x00\x00\x00\x00\x00\x00\x00',b'11'],
 118:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfb\x80q\x80y\x00;\x00;\x00\x1e\x00\x1e\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 119:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\x90w\x10s\x90;\xb09\xa0\x1d\xe0\x1f\xe0\x0c\xc0\x0c\xc0\x00\x00\x00\x00\x00\x00\x00\x00',b'12'],
 120:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf3\x80s\x00z\x00<\x00\x1c\x00\x1e\x007\x00g\x80\xe3\x80\x00\x00\x00\x00\x00\x00\x00\x00',b'9'],
 121:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfb\x80q\x80y\x00;\x00:\x00\x1e\x00\x1e\x00\x0c\x00\x0c\x00\x0c\x00\xc8\x00\xd8\x00\xf0\x00',b'9'],
 122:[b'\x00\x00\x00\x00\x00\xfe\xce\x8e\x1c8pr\xe6\xfe\x00\x00\x00\x00',b'8'],
 123:[b'\x00\x1e800000`\xc0`000008\x1e',b'8'],
 124:[b'\x00\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\x00',b'4'],
 125:[b'\x00\xf08\x18\x18\x18\x18\x18\x0c\x06\x0c\x18\x18\x18\x18\x188\xf0',b'8'],
 126:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\x00\xf9\x00\x9f\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'10'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 18, int(_g[c][1])

