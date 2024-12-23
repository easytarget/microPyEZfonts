'''
    ezFBfont_6x13_upper_11 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 6x13.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: 6x13
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/6x13.bdf', '_', './upper-char.set']
# Date: 2024-07-31 14:56:43
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain font.  Share and enjoy."
'''
version = '0.33'
name = '-misc-fixed-medium-r-semicondensed--13-120-75-75-c-60-iso10646-1'
family = 'fixed'
weight = 'medium'
size = 13

def height():
    return 11

def baseline():
    return 10

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
    return 95

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  33:b'\x00       \x00 \x00',
  34:b'\x00PPP\x00\x00\x00\x00\x00\x00\x00',
  35:b'\x00\x00PP\xf8P\xf8PP\x00\x00',
  36:b'\x00 x\xa0\xa0p((\xf0 \x00',
  37:b'\x00H\xa8P\x10 @P\xa8\x90\x00',
  38:b'\x00\x00@\xa0\xa0@\xa0\x98\x90h\x00',
  39:b'\x00   \x00\x00\x00\x00\x00\x00\x00',
  40:b'\x10  @@@@@  \x10',
  41:b'@  \x10\x10\x10\x10\x10  @',
  42:b'\x00 \xa8p\xa8 \x00\x00\x00\x00\x00',
  43:b'\x00\x00\x00  \xf8  \x00\x00\x00',
  44:b'\x00\x00\x00\x00\x00\x00\x00\x000 @',
  45:b'\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00 p ',
  47:b'\x00\x08\x08\x10\x10 @@\x80\x80\x00',
  48:b'\x00 P\x88\x88\x88\x88\x88P \x00',
  49:b'\x00 `\xa0     \xf8\x00',
  50:b'\x00p\x88\x88\x08\x10 @\x80\xf8\x00',
  51:b'\x00\xf8\x08\x10 p\x08\x08\x88p\x00',
  52:b'\x00\x10\x100PP\x90\xf8\x10\x10\x00',
  53:b'\x00\xf8\x80\x80\xb0\xc8\x08\x08\x88p\x00',
  54:b'\x00p\x88\x80\x80\xf0\x88\x88\x88p\x00',
  55:b'\x00\xf8\x08\x10\x10  @@@\x00',
  56:b'\x00p\x88\x88\x88p\x88\x88\x88p\x00',
  57:b'\x00p\x88\x88\x88x\x08\x08\x88p\x00',
  58:b'\x00\x00\x00 p \x00\x00 p ',
  59:b'\x00\x00\x00 p \x00\x000 @',
  60:b'\x00\x08\x10 @\x80@ \x10\x08\x00',
  61:b'\x00\x00\x00\x00\xf8\x00\x00\xf8\x00\x00\x00',
  62:b'\x00\x80@ \x10\x08\x10 @\x80\x00',
  63:b'\x00p\x88\x88\x08\x10  \x00 \x00',
  64:b'\x00p\x88\x88\x98\xa8\xa8\xb0\x80x\x00',
  65:b'\x00 P\x88\x88\x88\xf8\x88\x88\x88\x00',
  66:b'\x00\xf0HHHpHHH\xf0\x00',
  67:b'\x00p\x88\x80\x80\x80\x80\x80\x88p\x00',
  68:b'\x00\xf0HHHHHHH\xf0\x00',
  69:b'\x00\xf8\x80\x80\x80\xf0\x80\x80\x80\xf8\x00',
  70:b'\x00\xf8\x80\x80\x80\xf0\x80\x80\x80\x80\x00',
  71:b'\x00p\x88\x80\x80\x80\x98\x88\x88p\x00',
  72:b'\x00\x88\x88\x88\x88\xf8\x88\x88\x88\x88\x00',
  73:b'\x00p       p\x00',
  74:b'\x008\x10\x10\x10\x10\x10\x10\x90`\x00',
  75:b'\x00\x88\x88\x90\xa0\xc0\xa0\x90\x88\x88\x00',
  76:b'\x00\x80\x80\x80\x80\x80\x80\x80\x80\xf8\x00',
  77:b'\x00\x88\x88\xd8\xa8\xa8\x88\x88\x88\x88\x00',
  78:b'\x00\x88\xc8\xc8\xa8\xa8\x98\x98\x88\x88\x00',
  79:b'\x00p\x88\x88\x88\x88\x88\x88\x88p\x00',
  80:b'\x00\xf0\x88\x88\x88\xf0\x80\x80\x80\x80\x00',
  81:b'\x00p\x88\x88\x88\x88\x88\x88\xa8p\x08',
  82:b'\x00\xf0\x88\x88\x88\xf0\xa0\x90\x88\x88\x00',
  83:b'\x00p\x88\x80\x80p\x08\x08\x88p\x00',
  84:b'\x00\xf8        \x00',
  85:b'\x00\x88\x88\x88\x88\x88\x88\x88\x88p\x00',
  86:b'\x00\x88\x88\x88\x88PPP  \x00',
  87:b'\x00\x88\x88\x88\x88\xa8\xa8\xa8\xa8P\x00',
  88:b'\x00\x88\x88PP PP\x88\x88\x00',
  89:b'\x00\x88\x88PP     \x00',
  90:b'\x00\xf8\x08\x10\x10 @@\x80\xf8\x00',
  91:b'p@@@@@@@@@p',
  92:b'\x00\x80\x80@@ \x10\x10\x08\x08\x00',
  93:b'p\x10\x10\x10\x10\x10\x10\x10\x10\x10p',
  94:b'\x00 P\x88\x00\x00\x00\x00\x00\x00\x00',
  95:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 11, 6
