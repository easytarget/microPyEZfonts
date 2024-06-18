'''
    ezFBfont_22_courR18_ascii : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original courR18.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: courR18
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/courR18.bdf', '_', './ascii-char.set']
# Date: 2024-06-18 20:27:16
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
name = '-adobe-courier-medium-r-normal--25-180-100-100-m-150-iso10646-1'
family = 'courier'
weight = 'medium'
size = 25

def height():
    return 22

def baseline():
    return 17

def max_width():
    return 15

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 126

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  33:b'\x00\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x02\x00\x02\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  34:b'\x00\x00\x1c\xe0\x1c\xe0\x1c\xe0\x1c\xe0\x08@\x08@\x08@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  35:b'\x00\x00\x02@\x02@\x02@\x02@\x02@\x02@\x1f\xf0\x04\x80\x04\x80\x04\x80?\xe0\x04\x80\x04\x80\x04\x80\x04\x80\x04\x80\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00',
  36:b'\x01\x00\x01\x00\x01\x00\x03\xd0\x040\x08\x10\x08\x00\x08\x00\x04\x00\x03\xc0\x00 \x00\x10\x00\x10\x10\x10\x18 \x17\xc0\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00',
  37:b'\x00\x00\x0e\x00\x11\x00 \x80 \x80 \x80\x11\x00\x0e8\x01\xc0\x0e\x00p\xe0\x01\x10\x02\x08\x02\x08\x02\x08\x01\x10\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  38:b'\x00\x00\x00\x00\x00\x00\x00\x00\x07@\t\x80\x08\x00\x08\x00\x04\x00\x0c\x00\x12`"@!\x80 \x80 \xc0\x11@\x0e0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  39:b'\x00\x00\x00\x00\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  40:b'\x00\x00\x00 \x00@\x00@\x00\x80\x00\x80\x00\x80\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x80\x00\x80\x00\x80\x00@\x00@\x00 \x00\x00\x00\x00',
  41:b'\x00\x00\x10\x00\x08\x00\x08\x00\x04\x00\x04\x00\x04\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x04\x00\x04\x00\x04\x00\x08\x00\x08\x00\x10\x00\x00\x00\x00\x00',
  42:b'\x00\x00\x01\x00\x01\x00\x01\x00\x190\x0f\xe0\x03\x80\x06\xc0\x0c`\x180\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  43:b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00?\xf8\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  44:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80\x03\x80\x07\x00\x06\x00\x0c\x00\x08\x00\x00\x00\x00\x00',
  45:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  47:b'\x00\x00\x00\x10\x00\x10\x00 \x00 \x00@\x00@\x00\x80\x00\x80\x01\x00\x01\x00\x02\x00\x02\x00\x04\x00\x04\x00\x08\x00\x08\x00\x10\x00\x10\x00\x00\x00\x00\x00\x00\x00',
  48:b'\x00\x00\x00\x00\x03\x80\x0c`\x08 \x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x08 \x0c`\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  49:b'\x00\x00\x00\x00\x03\x00\x1d\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x1f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  50:b'\x00\x00\x00\x00\x07\x80\x18@    \x00 \x00 \x00@\x00\x80\x01\x00\x02\x00\x04\x00\x08\x00\x10\x00 \x10?\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  51:b'\x00\x00\x00\x00\x0f\x80\x10`\x00 \x00 \x00 \x00@\x07\x80\x00`\x00\x10\x00\x10\x00\x10\x00\x10 \x10\x18`\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  52:b'\x00\x00\x00\x00\x00\xc0\x01@\x02@\x02@\x04@\x08@\x08@\x10@\x10@ @?\xf0\x00@\x00@\x00@\x03\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  53:b'\x00\x00\x00\x00\x1f\xe0\x10\x00\x10\x00\x10\x00\x10\x00\x17\x80\x18`\x00 \x00\x10\x00\x10\x00\x10\x00\x10\x00 0`\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  54:b'\x00\x00\x00\x00\x01\xe0\x06\x00\x0c\x00\x08\x00\x10\x00\x13\xc0\x14 \x18\x10\x10\x10\x10\x10\x10\x10\x10\x10\x08\x10\x0c \x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  55:b'\x00\x00\x00\x00?\xe0   @\x00@\x00@\x00\x80\x00\x80\x00\x80\x00\x80\x01\x00\x01\x00\x01\x00\x02\x00\x02\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  56:b'\x00\x00\x00\x00\x07\x80\x08@\x10 \x10 \x10 \x10 \x08@\x0f\xc0\x10  \x10 \x10 \x10\x10 \x18`\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  57:b'\x00\x00\x00\x00\x03\x80\x0c`\x180\x10\x10\x10\x10\x10\x10\x080\x0cP\x03\x90\x00\x10\x00\x10\x00 \x00 \x00\xc0\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  58:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  59:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80\x03\x80\x07\x00\x06\x00\x0c\x00\x08\x00\x00\x00\x00\x00',
  60:b'\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\xc0\x03\x00\x0c\x000\x00`\x000\x00\x0c\x00\x03\x00\x00\xc0\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  61:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf8\x00\x00\x00\x00\x7f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  62:b'\x00\x00\x00\x00\x00\x00\x00\x000\x00\x0c\x00\x03\x00\x00\xc0\x000\x00\x18\x000\x00\xc0\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  63:b'\x00\x00\x00\x00\x00\x00\x0f\x80\x10@\x10 \x00 \x00 \x00 \x00@\x01\x80\x02\x00\x02\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  64:b'\x00\x00\x07\x80\x18@\x10      \xe0! " " " " !  \xf0 \x00 \x00\x10\x00\x18`\x07\xc0\x00\x00\x00\x00\x00\x00',
  65:b'\x00\x00\x00\x00\x00\x00\x1f\x80\x02\x80\x04@\x04@\x04@\x08 \x08 \x08 \x1f\xf0\x10\x10\x10\x10 \x08 \x08x<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  66:b'\x00\x00\x00\x00\x00\x00\x7f\xe0\x10\x10\x10\x08\x10\x08\x10\x08\x10\x10\x1f\xe0\x10\x10\x10\x08\x10\x08\x10\x08\x10\x08\x10\x10\x7f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  67:b'\x00\x00\x00\x00\x00\x00\x03\xc8\x0c(\x18\x18\x10\x08 \x00 \x00 \x00 \x00 \x00 \x00\x10\x08\x18\x18\x0c0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  68:b'\x00\x00\x00\x00\x00\x00\x7f\xc0 0 \x10 \x08 \x08 \x08 \x08 \x08 \x08 \x08 \x08 \x10 0\x7f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  69:b'\x00\x00\x00\x00\x00\x00\x7f\xf0\x10\x10\x10\x10\x10\x10\x11\x00\x11\x00\x1f\x00\x11\x00\x11\x00\x10\x08\x10\x08\x10\x08\x10\x08\x7f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  70:b'\x00\x00\x00\x00\x00\x00?\xf8\x08\x08\x08\x08\x08\x08\x08\x80\x08\x80\x0f\x80\x08\x80\x08\x80\x08\x00\x08\x00\x08\x00\x08\x00?\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  71:b'\x00\x00\x00\x00\x00\x00\x07\x90\x18P00 \x10@\x00@\x00@\x00@\x00A\xf8@\x10 \x100\x10\x18 \x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  72:b'\x00\x00\x00\x00\x00\x00||\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x1f\xf0\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10||\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  73:b'\x00\x00\x00\x00\x00\x00\x1f\xf0\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x1f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  74:b'\x00\x00\x00\x00\x00\x00\x07\xfc\x00 \x00 \x00 \x00 \x00 \x00 \x00        @\x10\xc0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  75:b'\x00\x00\x00\x00\x00\x00|x\x10 \x10@\x10\x80\x11\x00\x12\x00\x16\x00\x19\x00\x10\x80\x10@\x10 \x10 \x10\x10|<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  76:b'\x00\x00\x00\x00\x00\x00\x7f\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x08\x08\x08\x08\x08\x08\x08\x7f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  77:b'\x00\x00\x00\x00\x00\x00p\x1c0\x180\x18(((($H$H"\x88#\x88 \x08 \x08 \x08 \x08x<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  78:b'\x00\x00\x00\x00\x00\x00\xf0\xfc0\x10(\x10$\x10$\x10"\x10"\x10!\x10!\x10 \x90 \x90 P 0\xfc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  79:b'\x00\x00\x00\x00\x00\x00\x07\xc0\x1800\x18 \x08@\x04@\x04@\x04@\x04@\x04@\x04 \x080\x18\x180\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  80:b'\x00\x00\x00\x00\x00\x00?\xe0\x08\x10\x08\x08\x08\x08\x08\x08\x08\x08\x08\x10\x0f\xe0\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00?\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  81:b'\x00\x00\x00\x00\x00\x00\x07\xc0\x1800\x18 \x08@\x04@\x04@\x04@\x04@\x04@\x04 \x080\x18\x180\x07\xc0\x03\x18\r\xe0\x00\x00\x00\x00\x00\x00',
  82:b'\x00\x00\x00\x00\x00\x00\x7f\xc0\x10 \x10\x10\x10\x10\x10\x10\x10\x10\x10 \x1f\xc0\x10\x80\x10@\x10 \x10 \x10\x10|\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  83:b"\x00\x00\x00\x00\x00\x00\x07\x90\x18P 0 \x10 \x00\x18\x00\x07\x80\x00`\x00\x10\x00\x10 \x100\x10( '\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
  84:b'\x00\x00\x00\x00\x00\x00?\xf8!\x08!\x08!\x08!\x08\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x0f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  85:b'\x00\x00\x00\x00\x00\x00|\xf8 \x10 \x10 \x10 \x10 \x10 \x10 \x10 \x10 \x10 \x10 \x10\x10 \x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  86:b'\x00\x00\x00\x00\x00\x00|| \x08 \x08\x10\x10\x10\x10\x08 \x08 \x08 \x04@\x04@\x04@\x02\x80\x03\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  87:b'\x00\x00\x00\x00\x00\x00|| \x08 \x08!\x08!\x08"\x88"\x88\x12\x90\x14P\x14P\x14P\x180\x180\x180\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  88:b'\x00\x00\x00\x00\x00\x00||\x10\x10\x08 \x08 \x04@\x02\x80\x01\x00\x02\x80\x04@\x04@\x08 \x10\x10\x10\x10||\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  89:b'\x00\x00\x00\x00\x00\x00x<\x10\x10\x08 \x08 \x04@\x04@\x02\x80\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x0f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  90:b'\x00\x00\x00\x00\x00\x00?\xf0 \x10   @ \x80\x00\x80\x01\x00\x02\x00\x04\x00\x04\x10\x08\x10\x10\x10 \x10?\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  91:b'\x00\x00\x01\xc0\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\xc0\x00\x00\x00\x00',
  92:b'\x00\x00\x10\x00\x10\x00\x08\x00\x08\x00\x04\x00\x04\x00\x02\x00\x02\x00\x01\x00\x01\x00\x00\x80\x00\x80\x00@\x00@\x00 \x00 \x00\x10\x00\x10\x00\x00\x00\x00\x00\x00',
  93:b'\x00\x00\x07\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x07\x00\x00\x00\x00\x00',
  94:b'\x00\x00\x01\x00\x03\x80\x04@\x08 \x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  95:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe',
  96:b'\x00\x00\x0c\x00\x06\x00\x03\x00\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  97:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x80\x10@\x00 \x00 \x0f\xa0\x10`      \x10`\x0f\xb8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  98:b'\x00\x00\x00\x00p\x00\x10\x00\x10\x00\x10\x00\x13\xe0\x14\x18\x18\x08\x10\x04\x10\x04\x10\x04\x10\x04\x10\x04\x18\x08\x14\x18s\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  99:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xd0\x180\x10\x10 \x10 \x00 \x00 \x00 \x00\x10\x18\x180\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  100:b'\x00\x00\x00\x00\x00p\x00\x10\x00\x10\x00\x10\x0f\x900P 0@\x10@\x10@\x10@\x10@\x10 00P\x0f\x9c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  101:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xc0\x180\x10\x10 \x08 \x08?\xf8 \x00 \x00\x10\x00\x18\x18\x07\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  102:b'\x00\x00\x00\x00\x01\xf0\x03\x08\x02\x00\x02\x00\x1f\xf0\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x1f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  103:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x9c0P 0@\x10@\x10@\x10@\x10@\x10 00P\x0f\x90\x00\x10\x00\x10\x00 \x00`\x1f\x80',
  104:b'\x00\x00\x00\x00p\x00\x10\x00\x10\x00\x10\x00\x13\xc0\x14 \x18\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10||\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  105:b'\x00\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x0f\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x1f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  106:b'\x00\x00\x00@\x00@\x00@\x00\x00\x00\x00\x1f\xe0\x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00@\x00\xc0\x1f\x00',
  107:b'\x00\x00\x00\x008\x00\x08\x00\x08\x00\x08\x00\x08\xf0\x08@\x08\x80\t\x00\n\x00\x0e\x00\t\x00\x08\x80\x08@\x08 8x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  108:b'\x00\x00\x00\x00\x1f\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00?\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  109:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xeep1\x88!\x08!\x08!\x08!\x08!\x08!\x08!\x08!\x08\xf9\x8c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  110:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00s\xc0\x14 \x18\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10||\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  111:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xc0\x180\x10\x10 \x08 \x08 \x08 \x08 \x08\x10\x10\x180\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  112:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00s\xe0\x14\x18\x18\x08\x10\x04\x10\x04\x10\x04\x10\x04\x10\x04\x18\x08\x14\x18\x13\xe0\x10\x00\x10\x00\x10\x00\x10\x00~\x00',
  113:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x9c0P 0@\x10@\x10@\x10@\x10@\x10 00P\x0f\x90\x00\x10\x00\x10\x00\x10\x00\x10\x00\xfc',
  114:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1cp\x05\x88\x06\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00?\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  115:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xd0\x080\x08\x10\x08\x00\x07\x00\x00\xe0\x00\x10\x00\x10\x10\x10\x18 \x17\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  116:b'\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x08\x00?\xe0\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x040\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  117:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00pp\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x100\x08P\x07\x98\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  118:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00||\x10\x10\x10\x10\x08 \x08 \x08 \x04@\x04@\x02\x80\x03\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  119:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x< \x08 \x08!\x08\x11\x10\x12\x90\x12\x90\x12\x90\n\xa0\x0c`\x0c`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  120:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<x\x10\x10\x08 \x04@\x02\x80\x01\x00\x02\x80\x04@\x08 \x10\x10<x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  121:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00xx \x10 \x10\x10 \x10 \x10@\x08@\x08\x80\x04\x80\x05\x00\x03\x00\x02\x00\x02\x00\x04\x00\x04\x00\x7f\x00',
  122:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xf0\x10\x10\x10 \x00@\x00\x80\x01\x00\x02\x00\x04\x00\x08\x10\x10\x10\x1f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  123:b'\x00\x00\x00\xc0\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x06\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\xc0\x00\x00\x00\x00',
  124:b'\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00',
  125:b'\x00\x00\x06\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\xc0\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x06\x00\x00\x00\x00\x00',
  126:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x1830a\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 22, 15
