'''
    ezFBfont_symb08_0x0_0x39_09 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original symb08.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: symb08
# Cmd: ['bdf2dict.py'], ['Symbols-bdf-sources/symb08.bdf', '_', './0x0_0x39-char.set']
# Date: 2024-07-31 15:36:50
'''
    Original Copyright, Comments and Notices from source:

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
name = '-adobe-symbol-medium-r-normal--11-80-100-100-p-61-adobe-fontspecific'
family = 'symbol'
weight = 'medium'
size = 11

def height():
    return 9

def baseline():
    return 7

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
    return 63

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03',
  33:b'@@@@@\x00@\x00\x00\x03',
  34:b'\x82D|((\x10\x10\x00\x00\x07',
  35:b'PP\xf8P\xf8PP\x00\x00\x05',
  36:b'\xf8\x08\x08x\x08\x08\xf8\x00\x00\x06',
  37:b'd\xbc\xa8V**D\x00\x00\x08',
  38:b' PPl\x98\x98l\x00\x00\x07',
  39:b'\x00\x00\xe0\x10p\x10\xe0\x00\x00\x05',
  40:b' @@\x80\x80\x80@@ \x04',
  41:b'@  \x10\x10\x10  @\x04',
  42:b'\x00\x00P P\x00\x00\x00\x00\x05',
  43:b'\x00\x00  \xf8  \x00\x00\x06',
  44:b'\x00\x00\x00\x00\x00\x00@@\x80\x02',
  45:b'\x00\x00\x00\x00\xf8\x00\x00\x00\x00\x06',
  46:b'\x00\x00\x00\x00\x00\x00@\x00\x00\x02',
  47:b'  @@@\x80\x80\x00\x00\x03',
  48:b'`\x90\x90\x90\x90\x90`\x00\x00\x05',
  49:b' `    p\x00\x00\x05',
  50:b'`\x90\x10  @\xf0\x00\x00\x05',
  51:b'`\x90\x10`\x10\x10\xe0\x00\x00\x05',
  52:b'\x100P\x90\xf8\x10\x10\x00\x00\x05',
  53:b'p@\xe0\x10\x10\x10\xe0\x00\x00\x05',
  54:b'p\x80\xe0\x90\x90\x90`\x00\x00\x05',
  55:b'\xf0\x90  @@@\x00\x00\x05',
  56:b'`\x90\x90`\x90\x90`\x00\x00\x05',
  57:b'`\x90\x90\x90p \xc0\x00\x00\x05',
  58:b'\x00\x00@\x00\x00\x00@\x00\x00\x02',
  59:b'\x00\x00@\x00\x00\x00@@\x80\x02',
  60:b'\x00\x00\x0c0\xc00\x0c\x00\x00\x07',
  61:b'\x00\x00\x00\xf8\x00\xf8\x00\x00\x00\x06',
  62:b'\x00\x00\xc00\x0c0\xc0\x00\x00\x06',
  63:b' P\x10  \x00 \x00\x00\x05',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 9, int(_g[c][-1])