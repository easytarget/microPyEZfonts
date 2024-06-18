'''
    ezFBfont_10_timR10_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original timR10.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: timR10
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/timR10.bdf', '_', './time-char.set']
# Date: 2024-06-18 20:27:49
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

    NOTICE "Times is a trademark of Linotype-Hell AG and/or its subsidiaries."
'''
version = '0.33'
name = '-adobe-times-medium-r-normal--14-100-100-100-p-74-iso10646-1'
family = 'times'
weight = 'medium'
size = 14

def height():
    return 10

def baseline():
    return 10

def max_width():
    return 8

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 58

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03',
  43:b'\x00\x00\x00\x10\x10\x10\xfe\x10\x10\x10\x08',
  45:b'\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x04',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x04',
  48:b'<fBBBBBBf<\x07',
  49:b'\x10p\x10\x10\x10\x10\x10\x10\x10|\x07',
  50:b'8lD\x04\x0c\x08\x10 D|\x07',
  51:b'x\x8c\x04\x0808\x04\x04\xccx\x07',
  52:b'\x08\x18\x18(hH\x88\xfc\x08\x08\x07',
  53:b'< @p\x18\x0c\x04\x04Hp\x07',
  54:b'\x0c\x10 @x\xcc\x84\x84\xccx\x07',
  55:b'\xfc\x84\x08\x08\x10\x10  @@\x07',
  56:b'8LDd8LDDD8\x07',
  57:b'<fBBf<\x04\x08\x10`\x07',
  58:b'\x00\x00\x00`\x00\x00\x00\x00\x00`\x04',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 10, int(_g[c][-1])
