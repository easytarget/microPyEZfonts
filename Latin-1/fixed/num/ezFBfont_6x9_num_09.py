'''
    ezFBfont_6x9_num_09 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 6x9.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: 6x9
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/6x9.bdf', '_', './num-char.set']
# Date: 2024-07-31 14:56:46
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain font.  Share and enjoy."
'''
version = '0.33'
name = '-misc-fixed-medium-r-normal--9-90-75-75-c-60-iso10646-1'
family = 'fixed'
weight = 'medium'
size = 9

def height():
    return 9

def baseline():
    return 7

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
    return 176

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  37:b'@\xa8H\x10 HT\x08\x00',
  40:b'\x00\x10     \x10\x00',
  41:b'\x00 \x10\x10\x10\x10\x10 \x00',
  42:b'\x00\x00\x88P\xf8P\x88\x00\x00',
  43:b'\x00\x00  \xf8  \x00\x00',
  44:b'\x00\x00\x00\x00\x000\x10\x10 ',
  45:b'\x00\x00\x00\x00\xf8\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x0000\x00\x00',
  47:b'\x00\x08\x08\x10 @@\x00\x00',
  48:b'\x000HHHH0\x00\x00',
  49:b'\x00 `   p\x00\x00',
  50:b'\x000H\x08\x10 x\x00\x00',
  51:b'\x00x\x100\x08\x08p\x00\x00',
  52:b'\x00\x100P\x90\xf8\x10\x00\x00',
  53:b'\x00x@p\x08\x08p\x00\x00',
  54:b'\x000@pHH0\x00\x00',
  55:b'\x00x\x08\x08\x10  \x00\x00',
  56:b'\x000H0HH0\x00\x00',
  57:b'\x000HH8\x080\x00\x00',
  58:b'\x00\x0000\x0000\x00\x00',
  176:b'\x00\x000H0\x00\x00\x00\x00',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 9, 6
