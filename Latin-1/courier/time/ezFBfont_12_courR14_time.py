'''
    ezFBfont_12_courR14_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original courR14.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: courR14
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/courR14.bdf', '_', './time-char.set']
# Date: 2024-06-18 20:27:15
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

    NOTICE "No mark"
'''
version = '0.33'
name = '-adobe-courier-medium-r-normal--20-140-100-100-m-110-iso10646-1'
family = 'courier'
weight = 'medium'
size = 20

def height():
    return 12

def baseline():
    return 12

def max_width():
    return 11

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 58

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  43:b'\x00\x00\x00\x00\x04\x00\x04\x00\x04\x00\x04\x00\x7f\xc0\x04\x00\x04\x00\x04\x00\x04\x00\x00\x00',
  45:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00',
  48:b'\x0e\x00\x11\x00 \x80 \x80 \x80 \x80 \x80 \x80 \x80 \x80\x11\x00\x0e\x00',
  49:b'\x0c\x004\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00?\x80',
  50:b'\x0e\x00\x11\x00 \x80 \x80\x00\x80\x01\x00\x02\x00\x04\x00\x08\x00\x10\x80 \x80\x7f\x80',
  51:b'\x1e\x00!\x00\x00\x80\x00\x80\x01\x00\x0e\x00\x01\x00\x00\x80\x00\x80\x00\x80!\x00\x1e\x00',
  52:b'\x03\x00\x05\x00\x05\x00\t\x00\t\x00\x11\x00\x11\x00!\x00?\x80\x01\x00\x01\x00\x07\x80',
  53:b'?\x00 \x00 \x00 \x00.\x001\x00\x00\x80\x00\x80\x00\x80\x00\x80a\x00\x1e\x00',
  54:b'\x07\x00\x18\x00\x10\x00 \x00 \x00.\x001\x00 \x80 \x80 \x80\x11\x00\x0e\x00',
  55:b'?\x80 \x80\x00\x80\x00\x80\x01\x00\x01\x00\x01\x00\x01\x00\x02\x00\x02\x00\x02\x00\x02\x00',
  56:b'\x0e\x00\x11\x00 \x80 \x80\x11\x00\x0e\x00\x11\x00 \x80 \x80 \x80\x11\x00\x0e\x00',
  57:b'\x0e\x00\x11\x00 \x80 \x80 \x80\x11\x80\x0e\x80\x00\x80\x00\x80\x01\x00\x03\x00\x1c\x00',
  58:b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 12, 11
