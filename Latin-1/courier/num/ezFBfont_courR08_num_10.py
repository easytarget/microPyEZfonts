'''
    ezFBfont_courR08_num_10 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original courR08.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: courR08
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/courR08.bdf', '_', './num-char.set']
# Date: 2024-07-31 14:57:08
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
name = '-adobe-courier-medium-r-normal--11-80-100-100-m-60-iso10646-1'
family = 'courier'
weight = 'medium'
size = 11

def height():
    return 10

def baseline():
    return 8

def max_width():
    return 6

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 176

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  37:b'\x00\xe0\xa4\xc80\\\x94\x18\x00\x00',
  40:b'\x00\x08\x10\x10   \x10\x10\x08',
  41:b'\x00@  \x10\x10\x10  @',
  42:b'\x00 \xd8 P\x00\x00\x00\x00\x00',
  43:b'\x00\x00  \xf8  \x00\x00\x00',
  44:b'\x00\x00\x00\x00\x00\x00\x00  @',
  45:b'\x00\x00\x00\x00x\x00\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00\x00  \x00\x00',
  47:b'\x04\x08\x10\x10  @@\x80\x00',
  48:b'\x000HHHHH0\x00\x00',
  49:b'\x00\x10p\x10\x10\x10\x10x\x00\x00',
  50:b'\x000H\x08\x10 @x\x00\x00',
  51:b'\x000H\x080\x08H0\x00\x00',
  52:b'\x00\x100P\x90\xf8\x10\x10\x00\x00',
  53:b'\x00x@@p\x08\x08p\x00\x00',
  54:b'\x008@@pHH0\x00\x00',
  55:b'\x00xH\x08\x10\x10  \x00\x00',
  56:b'\x000HH0HH0\x00\x00',
  57:b'\x000HH8\x08\x08p\x00\x00',
  58:b'\x00\x00\x00  \x00  \x00\x00',
  176:b'\x000H0\x00\x00\x00\x00\x00\x00',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 10, 6