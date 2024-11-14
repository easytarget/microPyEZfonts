'''
    ezFBfont_ncenR10_num_13 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original ncenR10.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: ncenR10
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/ncenR10.bdf', '_', './num-char.set']
# Date: 2024-07-31 14:57:29
'''
    Original Copyright, Comments and Notices from source:

    COPYRIGHT ISO10646-1 extension by Markus Kuhn <mkuhn@acm.org>, 2001-03-20
    COPYRIGHT 
    COPYRIGHT +
    COPYRIGHT Copyright 1984-1989, 1994 Adobe Systems Incorporated.
    COPYRIGHT Copyright 1988, 1994 Digital Equipment Corporation.
    COPYRIGHT 
    COPYRIGHT Adobe is a trademark of Adobe Systems Incorporated which may be
    COPYRIGHT registered in certain jurisdictions.
    COPYRIGHT Permission to use these trademarks is hereby granted only in
    COPYRIGHT association with the images described in this file.
    COPYRIGHT 
    COPYRIGHT Permission to use, copy, modify, distribute and sell this software
    COPYRIGHT and its documentation for any purpose and without fee is hereby
    COPYRIGHT granted, provided that the above copyright notices appear in all
    COPYRIGHT copies and that both those copyright notices and this permission
    COPYRIGHT notice appear in supporting documentation, and that the names of
    COPYRIGHT Adobe Systems and Digital Equipment Corporation not be used in
    COPYRIGHT advertising or publicity pertaining to distribution of the software
    COPYRIGHT without specific, written prior permission.  Adobe Systems and
    COPYRIGHT Digital Equipment Corporation make no representations about the
    COPYRIGHT suitability of this software for any purpose.  It is provided "as
    COPYRIGHT is" without express or implied warranty.
    COPYRIGHT -

    COMMENT "Copyright (c) 1984, 1987 Adobe Systems Incorporated. All Rights Reserved. Copyright (c) 1988, 1991 Digital Equipment Corporation. All Rights Reserved."

    NOTICE "New Century Schoolbook is a trademark of Linotype-Hell AG and/or its subsidiaries."
'''
version = '0.33'
name = '-adobe-new century schoolbook-medium-r-normal--14-100-100-100-p-82-iso10646-1'
family = 'new century schoolbook'
weight = 'medium'
size = 14

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
    return 176

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04',
  37:b'3\x00M\x00\x8a\x00\x8a\x00\x94\x00d\xc0\t \n \x12 \x12@!\x80\x00\x00\x00\x00\x0c',
  40:b'\x10 @@\x80\x80\x80\x80\x80@@ \x10\x05',
  41:b'@ \x10\x10\x08\x08\x08\x08\x08\x10\x10 @\x06',
  42:b'\x10T8T\x10\x00\x00\x00\x00\x00\x00\x00\x00\x07',
  43:b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00\t',
  44:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0@@\x80\x04',
  45:b'\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x00\x00\x05',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00@@\x00\x00\x04',
  47:b'\x10\x10\x10   @@@\x80\x80\x00\x00\x04',
  48:b'<fBBBBBBBf<\x00\x00\x08',
  49:b'\x10p\x10\x10\x10\x10\x10\x10\x10\x10|\x00\x00\x08',
  50:b'<Fb\x02\x02\x04\x08\x10"B~\x00\x00\x08',
  51:b'<Fb\x02\x04\x1c\x06\x02bF<\x00\x00\x08',
  52:b'\x0c\x1c\x14$DD\x84\xfe\x04\x04\x0e\x00\x00\x08',
  53:b'~@@\\fB\x02\x02bF<\x00\x00\x08',
  54:b'\x1c"F@\\fBBBf<\x00\x00\x08',
  55:b'~BD\x04\x08\x08\x08\x10\x10\x10\x10\x00\x00\x08',
  56:b'<fBb4<FBBf<\x00\x00\x08',
  57:b'<fBBBf:\x02bD8\x00\x00\x08',
  58:b'\x00\x00\x00\x00@@\x00\x00\x00@@\x00\x00\x04',
  176:b'0HH0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 13, int(_g[c][-1])