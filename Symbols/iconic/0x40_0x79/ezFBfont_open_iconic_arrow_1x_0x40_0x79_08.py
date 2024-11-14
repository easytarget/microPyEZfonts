'''
    ezFBfont_open_iconic_arrow_1x_0x40_0x79_08 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_arrow_1x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: open_iconic_arrow_1x
# Cmd: ['bdf2dict.py'], ['Symbols-bdf-sources/open_iconic_arrow_1x.bdf', '_', './0x40_0x79-char.set']
# Date: 2024-07-31 15:36:17
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"
'''
version = '0.33'
name = 'open_iconic_arrow_1x'
family = 'iconic'
weight = 'none'
size = None

def height():
    return 8

def baseline():
    return 8

def max_width():
    return 8

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 64

def max_ch():
    return 91

_g = {
  64:b'\x10\x10\x10\x10\x10|8\x10',
  65:b'\x00 `\xff` \x00\x00',
  66:b'\x00\x04\x06\xff\x06\x04\x00\x00',
  67:b'\x108|\x10\x10\x10\x10\x10',
  68:b'<f\xe7\xe7\x81\xc3f<',
  69:b'<n\xcf\x81\x81\xcfn<',
  70:b'<v\xf3\x81\x81\xf3v<',
  71:b'<f\xc3\x81\xe7\xe7f<',
  72:b'\x18\x18\x18\x18\x18<\x18\x08',
  73:b'\x00\x00 \x7f\xff \x00\x00',
  74:b'\x00\x00\x06\xff\xfe\x04\x00\x00',
  75:b'\x108<\x18\x18\x18\x18\x18',
  76:b'\x00\x00~<\x18\x00\x00\x00',
  77:b'\x00\x04\x0c\x1c\x1c\x0c\x04\x00',
  78:b'\x00 0880 \x00',
  79:b'\x00\x00\x00\x18<~\x00\x00',
  80:b'\x00B\xe7~<\x18\x00\x00',
  81:b'\x00\x0c\x1800\x18\x0c\x00',
  82:b' p8\x1c\x1c8p ',
  83:b'\x00\x00\x18<fB\x00\x00',
  84:b'\x18\x18\x18<\x18\x00\x00\xff',
  85:b'\xff\x00\x00\x18<\x18\x18\x18',
  86:b'\x02\xff\x82\x00A\xff@\x00',
  87:b'\x000bG\xe2F\x0c\x00',
  88:b'~B\x02G\xe2@B~',
  89:b'\x02\xc7j00j\xc7\x02',
  90:b'\x04\x06?~\xc4\x80\x00\x00',
  91:b'\xe0\x8f\x9e\x80\x80\x84\xfc\x00',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 8, 8