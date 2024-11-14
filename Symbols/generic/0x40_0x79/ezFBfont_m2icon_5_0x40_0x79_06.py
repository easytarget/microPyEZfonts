'''
    ezFBfont_m2icon_5_0x40_0x79_06 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original m2icon_5.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: m2icon_5
# Cmd: ['bdf2dict.py'], ['Symbols-bdf-sources/m2icon_5.bdf', '_', './0x40_0x79-char.set']
# Date: 2024-07-31 15:36:10
'''
    Original Copyright, Comments and Notices from source:

    COPYRIGHT http://code.google.com/p/u8glib/

    COMMENT "public domain"
'''
version = '0.33'
name = 'm2icon5'
family = ''
weight = 'medium'
size = None

def height():
    return 6

def baseline():
    return 5

def max_width():
    return 9

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 65

def max_ch():
    return 104

_g = {
  65:b'\x1c\x00\xfe\x00\x82\x00\x82\x00\xfe\x00\x00\x00\t',
  66:b'p\xd0\x90\x90\xf0\x00\x08',
  67:b'\x00\xd8pp\xd8\x00\x06',
  68:b'\x06\x0c\xd8p \x00\x08',
  69:b'\x00\xf0\x90\x90\xf0\x00\x05',
  70:b'\x00\xf0\x90\xd0\xf0\x00\x05',
  71:b'\x00\xf0\xf0\xf0\xf0\x00\x05',
  72:b'\xf8\x88\x88\x88\xf8\x00\x06',
  73:b'\xf8\x88\xa8\x88\xf8\x00\x06',
  74:b'\xf8\xf8\xf8\xf8\xf8\x00\x06',
  75:b'\x00\xe0\xb0\xf0p\x00\x05',
  76:b'\x00\xe0\xb0\xf0p\x00\x05',
  77:b'\x00\xe0\xf0\xf0p\x00\x05',
  78:b'\xf0\x98\x98\xf8x\x00\x06',
  79:b'\xf0\x98\xd8\xf8x\x00\x06',
  80:b'\xf0\xf8\xf8\xf8x\x00\x06',
  81:b'\x00`\x90\x90`\x00\x05',
  82:b'\x00`\x90\xd0`\x00\x05',
  83:b'\x00`\xf0\xf0`\x00\x05',
  97:b' @\xfe@ \x00\x08',
  98:b' p\xa8  \x00\x06',
  102:b'\x1c\x00\xfe\x00\x82\x00\xbf\x80\xff\x00\x00\x00\t',
  103:b'\x80\x80\x80\x80\x80\x80\x02',
  104:b'  \xf8  \x00\x06',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 6, int(_g[c][-1])