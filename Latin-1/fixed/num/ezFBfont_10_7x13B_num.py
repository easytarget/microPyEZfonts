'''
    ezFBfont_10_7x13B_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 7x13B.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: 7x13B
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/7x13B.bdf', '_', './num-char.set']
# Date: 2024-06-18 20:26:53
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain font.  Share and enjoy."
'''
version = '0.33'
name = '-misc-fixed-bold-r-normal--13-120-75-75-c-70-iso10646-1'
family = 'fixed'
weight = 'bold'
size = 13

def height():
    return 10

def baseline():
    return 9

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
    return 176

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  37:b'\xe4\xac\xe8\x180`\\\xd4\x9c\x00',
  40:b'\x1800```00\x18\x00',
  41:b'`00\x18\x18\x1800`\x00',
  42:b'\x00\x00H0\xfc\xfc0H\x00\x00',
  43:b'\x00\x0000\xfc\xfc00\x00\x00',
  44:b'\x00\x00\x00\x00\x00\x00880`',
  45:b'\x00\x00\x00\x00\x00\xfc\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00\x00\x000x0',
  47:b'\x0c\x0c\x18\x180``\xc0\xc0\x00',
  48:b'0H\xcc\xcc\xcc\xcc\xccH0\x00',
  49:b'0p\xb000000\xfc\x00',
  50:b'x\xcc\xcc\x0c8`\xc0\xc0\xfc\x00',
  51:b'\xfc\x0c\x180x\x0c\x0c\xccx\x00',
  52:b'\x0c\x1c<l\xcc\xcc\xfc\x0c\x0c\x00',
  53:b'\xfc\xc0\xc0\xf8\xcc\x0c\x0c\xccx\x00',
  54:b'x\xcc\xc0\xc0\xf8\xcc\xcc\xccx\x00',
  55:b'\xfc\x0c\x0c\x18\x1800``\x00',
  56:b'x\xcc\xcc\xccx\xcc\xcc\xccx\x00',
  57:b'x\xcc\xcc\xcc|\x0c\x0c\xccx\x00',
  58:b'\x00\x000x0\x00\x000x0',
  176:b'x\xcc\xccx\x00\x00\x00\x00\x00\x00',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 10, 7
