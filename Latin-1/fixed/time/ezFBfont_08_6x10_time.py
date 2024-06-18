'''
    ezFBfont_08_6x10_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 6x10.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: 6x10
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/6x10.bdf', '_', './time-char.set']
# Date: 2024-06-18 20:26:44
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain terminal emulator font.  Share and enjoy."
'''
version = '0.33'
name = '-misc-fixed-medium-r-normal--10-100-75-75-c-60-iso10646-1'
family = 'fixed'
weight = 'medium'
size = 10

def height():
    return 8

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
    return 58

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00',
  43:b'\x00  \xf8  \x00\x00',
  45:b'\x00\x00\x00\xf8\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00 p ',
  48:b' P\x88\x88\x88P \x00',
  49:b' `\xa0   \xf8\x00',
  50:b'p\x88\x080@\x80\xf8\x00',
  51:b'\xf8\x08\x100\x08\x88p\x00',
  52:b'\x100P\x90\xf8\x10\x10\x00',
  53:b'\xf8\x80\xb0\xc8\x08\x88p\x00',
  54:b'0@\x80\xb0\xc8\x88p\x00',
  55:b'\xf8\x08\x10\x10 @@\x00',
  56:b'p\x88\x88p\x88\x88p\x00',
  57:b'p\x88\x98h\x08\x10`\x00',
  58:b'\x00 p \x00 p ',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 8, 6
