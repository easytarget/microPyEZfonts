'''
    ezFBfont_13_7x14_upper : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 7x14.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: 7x14
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/7x14.bdf', '_', './upper-char.set']
# Date: 2024-06-18 20:26:55
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain font.  Share and enjoy."
'''
version = '0.33'
name = '-misc-fixed-medium-r-normal--14-130-75-75-c-70-iso10646-1'
family = 'fixed'
weight = 'medium'
size = 14

def height():
    return 13

def baseline():
    return 11

def max_width():
    return 7

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
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  33:b'\x00\x10\x10\x10\x10\x10\x10\x10\x00\x10\x10\x00\x00',
  34:b'((((\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  35:b'\x00(((|((|(((\x00\x00',
  36:b'\x00\x10x\x94\x94P8\x14\x94\x94x\x10\x00',
  37:b'\x00d\x94\x98p\x10 8d\xa4\x98\x00\x00',
  38:b'\x000HHH0d\x94\x88\x98d\x00\x00',
  39:b'\x10\x10\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  40:b'\x04\x08\x10\x10     \x10\x10\x08\x04',
  41:b'@ \x10\x10\x08\x08\x08\x08\x08\x10\x10 @',
  42:b'\x00\x00\x00\x10T8\x108T\x10\x00\x00\x00',
  43:b'\x00\x00\x00\x10\x10\x10|\x10\x10\x10\x00\x00\x00',
  44:b'\x00\x00\x00\x00\x00\x00\x00\x00\x000\x10\x10 ',
  45:b'\x00\x00\x00\x00\x00\x00|\x00\x00\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x108\x10\x00',
  47:b'\x04\x04\x08\x08\x10\x10\x10  @@\x80\x80',
  48:b'\x000H\x84\x84\x84\x84\x84\x84H0\x00\x00',
  49:b'\x00\x100P\x10\x10\x10\x10\x10\x10|\x00\x00',
  50:b'\x00x\x84\x84\x04\x08\x08\x10 @\xfc\x00\x00',
  51:b'\x00\xfc\x04\x08\x108\x04\x04\x84\x84x\x00\x00',
  52:b'\x00\x08\x18((HH\x88\xfc\x08\x08\x00\x00',
  53:b'\x00\xfc\x80\x80\xf8\x84\x04\x04\x84\x84x\x00\x00',
  54:b'\x008@\x80\x80\xb8\xc4\x84\x84\x84x\x00\x00',
  55:b'\x00\xfc\x04\x08\x08\x10\x10  @@\x00\x00',
  56:b'\x00x\x84\x84H0H\x84\x84\x84x\x00\x00',
  57:b'\x00x\x84\x84\x84\x8ct\x04\x84\x88p\x00\x00',
  58:b'\x00\x00\x00\x108\x10\x00\x00\x108\x10\x00\x00',
  59:b'\x00\x00\x00\x0000\x00\x000\x10\x10 \x00',
  60:b'\x00\x00\x04\x08\x10 @ \x10\x08\x04\x00\x00',
  61:b'\x00\x00\x00\x00\xfc\x00\x00\xfc\x00\x00\x00\x00\x00',
  62:b'\x00\x00@ \x10\x08\x04\x08\x10 @\x00\x00',
  63:b'\x00x\x84\x84\x08\x10\x10\x10\x00\x10\x10\x00\x00',
  64:b'\x008D\x9c\xa4\xa4\xa4\xa4\x9c@<\x00\x00',
  65:b'\x000H\x84\x84\x84\xfc\x84\x84\x84\x84\x00\x00',
  66:b'\x00\xf0\x88\x84\x88\xf0\x88\x84\x84\x88\xf0\x00\x00',
  67:b'\x00x\x84\x84\x80\x80\x80\x80\x84\x84x\x00\x00',
  68:b'\x00\xf0\x88\x84\x84\x84\x84\x84\x84\x88\xf0\x00\x00',
  69:b'\x00\xfc\x80\x80\x80\xf0\x80\x80\x80\x80\xfc\x00\x00',
  70:b'\x00\xfc\x80\x80\x80\xf0\x80\x80\x80\x80\x80\x00\x00',
  71:b'\x00x\x84\x84\x80\x80\x9c\x84\x84\x8ct\x00\x00',
  72:b'\x00\x84\x84\x84\x84\xfc\x84\x84\x84\x84\x84\x00\x00',
  73:b'\x00|\x10\x10\x10\x10\x10\x10\x10\x10|\x00\x00',
  74:b'\x00\x1c\x08\x08\x08\x08\x08\x08\x88\x88p\x00\x00',
  75:b'\x00\x84\x88\x90\xa0\xc0\xa0\x90\x88\x84\x84\x00\x00',
  76:b'\x00\x80\x80\x80\x80\x80\x80\x80\x80\x80\xfc\x00\x00',
  77:b'\x00\x84\xcc\xcc\xb4\xb4\x84\x84\x84\x84\x84\x00\x00',
  78:b'\x00\x84\x84\xc4\xc4\xa4\x94\x8c\x8c\x84\x84\x00\x00',
  79:b'\x00x\x84\x84\x84\x84\x84\x84\x84\x84x\x00\x00',
  80:b'\x00\xf8\x84\x84\x84\x84\xf8\x80\x80\x80\x80\x00\x00',
  81:b'\x00x\x84\x84\x84\x84\x84\xe4\x94\x8cx\x08\x04',
  82:b'\x00\xf8\x84\x84\x84\x84\xf8\x90\x88\x84\x84\x00\x00',
  83:b'\x00x\x84\x84\x80`\x18\x04\x84\x84x\x00\x00',
  84:b'\x00\xfe\x10\x10\x10\x10\x10\x10\x10\x10\x10\x00\x00',
  85:b'\x00\x84\x84\x84\x84\x84\x84\x84\x84\x84x\x00\x00',
  86:b'\x00\x84\x84\x84\x84HHH000\x00\x00',
  87:b'\x00DDDDDDTTT(\x00\x00',
  88:b'\x00\x84\x84HH00HH\x84\x84\x00\x00',
  89:b'\x00DDD((\x10\x10\x10\x10\x10\x00\x00',
  90:b'\x00\xfc\x04\x08\x10\x10 @@\x80\xfc\x00\x00',
  91:b'<           <',
  92:b'\x80\x80@@   \x10\x10\x08\x08\x04\x04',
  93:b'x\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08x',
  94:b'0H\x84\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  95:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 13, 7
