'''
    ezFBfont_18_helvB18_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original helvB18.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: helvB18
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/helvB18.bdf', '_', './time-char.set']
# Date: 2024-06-18 20:27:22
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

    NOTICE "Helvetica is a trademark of Linotype-Hell AG and/or its subsidiaries.  "
'''
version = '0.33'
name = '-adobe-helvetica-bold-r-normal--25-180-100-100-p-138-iso10646-1'
family = 'helvetica'
weight = 'bold'
size = 25

def height():
    return 18

def baseline():
    return 18

def max_width():
    return 15

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
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06',
  43:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x7f\xf8\x7f\xf8\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x00\x00\x0f',
  45:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xfe\xfe\x00\x00\x00\x00\x00\x00\x08',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00888\x07',
  48:b'\x1f\x80?\xc0y\xe0p\xe0p\xe0\xe0p\xe0p\xe0p\xe0p\xe0p\xe0p\xe0p\xe0pp\xe0p\xe0y\xe0?\xc0\x1f\x80\r',
  49:b'\x03\x80\x03\x80\x07\x80?\x80?\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\r',
  50:b'\x1f\x00\x7f\xc0q\xe0\xe0\xe0\xe0p\xe0p\x00p\x00\xe0\x01\xe0\x03\xc0\x07\x80\x1f\x00<\x00x\x00\xf0\x00\xe0\x00\xff\xf0\xff\xf0\r',
  51:b'\x1f\x00\x7f\xc0q\xc0\xe0\xe0\xe0\xe0\xe0\xe0\x00\xe0\x01\xc0\x0f\x80\x0f\xe0\x00\xe0\x00p\x00p\xe0p\xe0\xf0q\xe0\x7f\xe0\x1f\x80\r',
  52:b'\x01\xc0\x03\xc0\x03\xc0\x07\xc0\x07\xc0\r\xc0\x1d\xc0\x19\xc01\xc0q\xc0a\xc0\xe1\xc0\xff\xf0\xff\xf0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\r',
  53:b'\x7f\xe0\x7f\xe0p\x00p\x00p\x00p\x00\x7f\x80\x7f\xc0q\xe0\x00\xe0\x00p\x00p\x00p\xe0p\xe0\xf0\xf1\xe0\x7f\xc0\x1f\x80\r',
  54:b'\x0f\x80?\xe0x\xe0pp\xe0p\xe0\x00\xe0\x00\xef\x00\xff\xc0\xf9\xe0\xf0\xe0\xe0p\xe0p\xe0pp\xe0y\xe0?\xc0\x1f\x80\r',
  55:b'\xff\xf0\xff\xf0\x00\xf0\x00\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x0e\x00\x0e\x00\x1e\x00\x1c\x00\x1c\x00<\x008\x008\x00\r',
  56:b'\x0f\x00?\xc09\xc0p\xe0p\xe0p\xe0p\xe09\xc0\x1f\x80?\xc0p\xe0\xe0p\xe0p\xe0p\xe0pp\xe0\x7f\xe0\x1f\x80\r',
  57:b'\x1f\x80\x7f\xc0y\xe0\xf0\xe0\xe0p\xe0p\xe0p\xe0p\xf0\xf0y\xf0\x7f\xf0\x1fp\x00p\x00p\xe0\xe0\xf3\xe0\x7f\xc0\x1f\x00\r',
  58:b'\x00\x00\x00\x00888\x00\x00\x00\x00\x00\x00\x00\x00888\x07',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 18, int(_g[c][-1])
