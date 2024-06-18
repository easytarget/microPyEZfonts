'''
    ezFBfont_17_ncenR14_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original ncenR14.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: ncenR14
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/ncenR14.bdf', '_', './num-char.set']
# Date: 2024-06-18 20:27:36
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
name = '-adobe-new century schoolbook-medium-r-normal--20-140-100-100-p-103-iso10646-1'
family = 'new century schoolbook'
weight = 'medium'
size = 20

def height():
    return 17

def baseline():
    return 14

def max_width():
    return 16

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
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05',
  37:b'\x1c 2 c\xc0b@\xc4\x80\xc4\x80\xc9\x1cq2\x02b\x02b\x04\xc4\x04\xc4\x08\xc8\x08p\x00\x00\x00\x00\x00\x00\x10',
  40:b'\x04\x180``\xc0\xc0\xc0\xc0\xc0\xc0\xc0``0\x18\x04\x07',
  41:b'\x80`0\x18\x18\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x18\x180`\x80\x07',
  42:b'\x08\x00I\x00k\x00\x1c\x00k\x00I\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n',
  43:b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x08\x00\xff\x80\x08\x00\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\n',
  44:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`` @\x80\x05',
  45:b'\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x06',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00``\x00\x00\x00\x05',
  47:b'\x08\x08\x08\x10\x10\x10   @@@\x80\x80\x00\x00\x00\x06',
  48:b'\x1c\x00c\x00c\x00\xc1\x80\xc1\x80\xc1\x80\xc1\x80\xc1\x80\xc1\x80\xc1\x80\xc1\x80c\x00c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\n',
  49:b'\x0c\x00|\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80\x00\x00\x00\x00\x00\x00\n',
  50:b'\x1e\x00c\x00\xc1\x80\xc1\x80\x01\x80\x01\x80\x03\x00\x06\x00\x0c\x00\x18\x000\x80`\x80\xff\x80\xff\x80\x00\x00\x00\x00\x00\x00\n',
  51:b'>\x00c\x00a\x80\x01\x80\x01\x80\x03\x00\x1e\x00\x03\x00\x01\x80\x01\x80\x01\x80\xc1\x80\xc3\x00~\x00\x00\x00\x00\x00\x00\x00\n',
  52:b'\x03\x00\x07\x00\x0b\x00\x0b\x00\x13\x00\x13\x00#\x00#\x00C\x00C\x00\xff\xc0\x03\x00\x03\x00\x0f\x80\x00\x00\x00\x00\x00\x00\n',
  53:b'\x7f\x80\x7f\x00@\x00@\x00@\x00^\x00c\x00A\x80\x01\x80\x01\x80\x01\x80\xc1\x80\xc3\x00~\x00\x00\x00\x00\x00\x00\x00\n',
  54:b'\x0f\x001\x80a\x80`\x00\xc0\x00\xce\x00\xdf\x00\xe3\x80\xc1\x80\xc1\x80\xc1\x80\xc1\x80c\x00>\x00\x00\x00\x00\x00\x00\x00\n',
  55:b'\xff\x80\xff\x80\x81\x00\x83\x00\x02\x00\x06\x00\x06\x00\x0c\x00\x0c\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00\n',
  56:b'>\x00c\x00A\x00A\x00a\x00r\x00>\x00/\x00C\x80\xc1\x80\xc1\x80\xc1\x80c\x00>\x00\x00\x00\x00\x00\x00\x00\n',
  57:b'>\x00c\x00\xc1\x80\xc1\x80\xc1\x80\xc1\x80\xe3\x80}\x809\x80\x01\x80\x03\x00\xc3\x00\xc6\x00x\x00\x00\x00\x00\x00\x00\x00\n',
  58:b'\x00\x00\x00\x00\x00``\x00\x00\x00\x00\x00``\x00\x00\x00\x05',
  176:b'x\xcc\x84\x84\xccx\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 17, int(_g[c][-1])
