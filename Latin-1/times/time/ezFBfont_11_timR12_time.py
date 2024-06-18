'''
    ezFBfont_11_timR12_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original timR12.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: timR12
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/timR12.bdf', '_', './time-char.set']
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
name = '-adobe-times-medium-r-normal--17-120-100-100-p-84-iso10646-1'
family = 'times'
weight = 'medium'
size = 17

def height():
    return 11

def baseline():
    return 11

def max_width():
    return 9

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
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04',
  43:b'\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00\x00\x00\t',
  45:b'\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x00\x05',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00@@\x04',
  48:b'8DD\x82\x82\x82\x82\x82DD8\x08',
  49:b'\x100P\x10\x10\x10\x10\x10\x10\x108\x08',
  50:b'8D\x82\x02\x02\x04\x08\x10 B\xfc\x08',
  51:b'8D\x84\x08\x108\x04\x02\x02\xc4x\x08',
  52:b'\x02\x06\n\n\x12""B\xff\x02\x02\x08',
  53:b'>  @x\x04\x02\x02\x02\x8cp\x08',
  54:b'\x0e0@@\x98\xe4\x82\x82\x82D8\x08',
  55:b'\xfe\x82\x84\x04\x08\x08\x10\x10\x10  \x08',
  56:b'0H\x84\x84H0H\x84\x84H0\x08',
  57:b'8D\x82\x82\x82F:\x04\x04\x18\xe0\x08',
  58:b'\x00\x00\x00@@\x00\x00\x00\x00@@\x04',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 11, int(_g[c][-1])
