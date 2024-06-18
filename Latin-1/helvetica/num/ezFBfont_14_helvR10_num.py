'''
    ezFBfont_14_helvR10_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original helvR10.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: helvR10
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/helvR10.bdf', '_', './num-char.set']
# Date: 2024-06-18 20:27:24
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
name = '-adobe-helvetica-medium-r-normal--14-100-100-100-p-76-iso10646-1'
family = 'helvetica'
weight = 'medium'
size = 14

def height():
    return 14

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
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04',
  37:b'p\x80\x89\x00\x89\x00r\x00\x02\x00\x04\x00\x08\x00\t\xc0\x12 \x12 !\xc0\x00\x00\x00\x00\x00\x00\x0c',
  40:b'\x10  @@@@@@@@  \x10\x05',
  41:b'@  \x10\x10\x10\x10\x10\x10\x10\x10  @\x05',
  42:b'\x10T8T\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07',
  43:b'\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\t',
  44:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00@@@\x80\x00\x03',
  45:b'\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x04',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00@@\x00\x00\x00\x03',
  47:b'\x10\x10   @@@\x80\x80\x80\x00\x00\x00\x04',
  48:b'<BBBBBBBBB<\x00\x00\x00\x08',
  49:b'\x088\x08\x08\x08\x08\x08\x08\x08\x08\x08\x00\x00\x00\x08',
  50:b'<BB\x02\x04\x08\x10 @@~\x00\x00\x00\x08',
  51:b'<BB\x02\x02\x1c\x02\x02BB<\x00\x00\x00\x08',
  52:b'\x02\x06\n\x12"BB\x7f\x02\x02\x02\x00\x00\x00\x08',
  53:b'~@@@|\x02\x02\x02BB<\x00\x00\x00\x08',
  54:b'<B@@\\bBBBB<\x00\x00\x00\x08',
  55:b'~\x02\x04\x04\x08\x08\x10\x10   \x00\x00\x00\x08',
  56:b'<BBBB<BBBB<\x00\x00\x00\x08',
  57:b'<BBBB>\x02\x02BB<\x00\x00\x00\x08',
  58:b'\x00\x00\x00@@\x00\x00\x00\x00@@\x00\x00\x00\x03',
  176:b'0HH0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 14, int(_g[c][-1])
