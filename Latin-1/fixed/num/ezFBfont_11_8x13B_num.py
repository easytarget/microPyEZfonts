'''
    ezFBfont_11_8x13B_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 8x13B.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: 8x13B
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/8x13B.bdf', '_', './num-char.set']
# Date: 2024-06-18 20:26:59
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain font.  Share and enjoy."
'''
version = '0.33'
name = '-misc-fixed-bold-r-normal--13-120-75-75-c-80-iso10646-1'
family = 'fixed'
weight = 'bold'
size = 13

def height():
    return 11

def baseline():
    return 10

def max_width():
    return 8

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
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  37:b'\xe6\xa6\xec\x18\x1800n\xca\xce\x00',
  40:b'\x0c\x1800```00\x18\x0c',
  41:b'`0\x18\x18\x0c\x0c\x0c\x18\x180`',
  42:b'\x00\x00\x10\x10\xfe88lD\x00\x00',
  43:b'\x00\x00\x18\x18~~\x18\x18\x00\x00\x00',
  44:b'\x00\x00\x00\x00\x00\x00<\x1c\x1c\x180',
  45:b'\x00\x00\x00\x00\x00~\x00\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x18<\x18\x00',
  47:b'\x02\x06\x06\x0c\x180`\xc0\xc0\x80\x00',
  48:b'8l\xc6\xc6\xc6\xc6\xc6\xc6l8\x00',
  49:b'\x188x\x18\x18\x18\x18\x18\x18~\x00',
  50:b'|\xc6\xc6\x06\x0c\x180`\xc0\xfe\x00',
  51:b'\xfe\x06\x0c\x18<\x06\x06\x06\xc6|\x00',
  52:b'\x0c\x1c<l\xcc\xcc\xfe\x0c\x0c\x0c\x00',
  53:b'\xfe\xc0\xc0\xfc\xe6\x06\x06\x06\xc6|\x00',
  54:b'<`\xc0\xc0\xfc\xe6\xc6\xc6\xe6|\x00',
  55:b'\xfe\x06\x06\x0c\x18\x180000\x00',
  56:b'|\xc6\xc6\xc6|\xc6\xc6\xc6\xc6|\x00',
  57:b'|\xce\xc6\xc6\xce~\x06\x06\x0cx\x00',
  58:b'\x00\x00\x18<\x18\x00\x00\x18<\x18\x00',
  176:b'<ff<\x00\x00\x00\x00\x00\x00\x00',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 11, 8
