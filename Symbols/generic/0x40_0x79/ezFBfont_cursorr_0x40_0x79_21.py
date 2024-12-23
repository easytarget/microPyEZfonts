'''
    ezFBfont_cursorr_0x40_0x79_21 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original cursorr.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: cursorr
# Cmd: ['bdf2dict.py'], ['Symbols-bdf-sources/cursorr.bdf', '_', './0x40_0x79-char.set']
# Date: 2024-07-31 15:36:10
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "These "glyphs" are unencumbered"
'''
version = '0.33'
name = 'cursor'
family = 'generic'
weight = 'none'
size = None

def height():
    return 21

def baseline():
    return 6

def max_width():
    return 17

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 68

def max_ch():
    return 95

_g = {
  68:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\xc0\x00\x00\xe0\x00\x00\xf0\x00\x00\xf8\x00\x00\xfc\x00\x00\xfe\x00\x00\xff\x00\x00\xf8\x00\x00\xd8\x00\x00\x8c\x00\x00\x0c\x00\x00\x06\x00\x00\x06\x00\x00\x00\x00\x00',
  69:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\xe0\x00\x00\xf0\x00\x00\xf8\x00\x00\xfc\x00\x00\xfe\x00\x00\xff\x00\x00\xff\x80\x00\xff\xc0\x00\xff\xc0\x00\xfe\x00\x00\xef\x00\x00\xcf\x00\x00\x07\x80\x00\x07\x80\x00\x03\x00\x00',
  90:b'\x00\x00\x00\x0c\x00\x00\x0c\x00\x00\x0c\x00\x00\x0c\x00\x00\xff\xc0\x00\xff\xc0\x00\x0c\x00\x00\x0c\x00\x00\x0c\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  91:b'\x0f\x00\x00\x0f\x00\x00\x0f\x00\x00\x0f\x00\x00\xff\xf0\x00\xff\xf0\x00\xff\xf0\x00\xff\xf0\x00\x0f\x00\x00\x0f\x00\x00\x0f\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  94:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x00\x00\x07\x00\x00\x0f\x00\x00\x1f\x00\x00?\x00\x00\x7f\x00\x00\xff\x00\x00\x1f\x00\x00\x1b\x00\x001\x00\x000\x00\x00`\x00\x00`\x00\x00\x00\x00\x00',
  95:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x01\xc0\x00\x03\xc0\x00\x07\xc0\x00\x0f\xc0\x00\x1f\xc0\x00?\xc0\x00\x7f\xc0\x00\xff\xc0\x00\xff\xc0\x00\x1f\xc0\x00=\xc0\x00<\xc0\x00x\x00\x00x\x00\x000\x00\x00',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 21, 17
