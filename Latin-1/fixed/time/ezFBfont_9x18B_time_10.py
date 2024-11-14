'''
    ezFBfont_9x18B_time_10 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 9x18B.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: 9x18B
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/9x18B.bdf', '_', './time-char.set']
# Date: 2024-07-31 14:57:01
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain font.  Share and enjoy."
'''
version = '0.33'
name = '-misc-fixed-bold-r-normal--18-120-100-100-c-90-iso10646-1'
family = 'fixed'
weight = 'bold'
size = 18

def height():
    return 10

def baseline():
    return 10

def max_width():
    return 9

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 58

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  43:b'\x00\x00\x00\x00\x18\x00\x18\x00\x18\x00\xff\x00\x18\x00\x18\x00\x18\x00\x00\x00',
  45:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00',
  48:b'\x1c\x006\x00c\x00c\x00c\x00c\x00c\x00c\x006\x00\x1c\x00',
  49:b'\x18\x008\x00x\x00\xd8\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\xff\x00',
  50:b'\x1c\x006\x00c\x00\x03\x00\x03\x00\x06\x00\x0c\x00\x18\x000\x00\x7f\x00',
  51:b'\x7f\x00\x03\x00\x06\x00\x0c\x00\x1c\x00\x06\x00\x03\x00\x03\x00f\x00<\x00',
  52:b'\x06\x00\x0e\x00\x1e\x006\x00f\x00f\x00\x7f\x00\x06\x00\x06\x00\x06\x00',
  53:b'\x7f\x00`\x00`\x00`\x00|\x00\x06\x00\x03\x00\x03\x00f\x00<\x00',
  54:b'\x1e\x000\x00`\x00`\x00|\x00f\x00c\x00c\x006\x00\x1c\x00',
  55:b'\x7f\x00\x03\x00\x06\x00\x06\x00\x0c\x00\x0c\x00\x18\x00\x18\x00\x18\x00\x18\x00',
  56:b'\x1c\x006\x00c\x006\x00\x1c\x006\x00c\x00c\x006\x00\x1c\x00',
  57:b'\x1c\x006\x00c\x00c\x007\x00\x1f\x00\x03\x00\x03\x00\x06\x00<\x00',
  58:b'\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 10, 9