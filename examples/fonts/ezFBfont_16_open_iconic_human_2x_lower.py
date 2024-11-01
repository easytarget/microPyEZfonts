'''
    ezFBfont_16_open_iconic_human_2x_lower : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_human_2x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: open_iconic_human_2x
# Cmd: ['bdf2dict.py'], ['Symbols-bdf-sources/open_iconic_human_2x.bdf', '_', './lower-char.set']
# Date: 2024-06-18 17:10:01
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"
'''
version = '0.33'
name = 'open_iconic_human_2x'
family = 'iconic'
weight = 'none'
size = None

def height():
    return 16

def baseline():
    return 16

def max_width():
    return 16

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 64

def max_ch():
    return 68

_g = {
  64:b'\x00\x00\x00\x00\x03\xc0\x0f\xf0\x1c88\x1cq\x0e\xf3\x0f\xf3\xcfq\x8e8\x1c\x1c8\x0f\xf0\x03\xc0\x00\x00\x00\x00',
  65:b'\x03\x1e\x03\xbf\x01\xff\x01\xff\x03\xff\x07>\x0e\x1c\x1c\x1e8?ps\xe0\xe0\xe1\xc0\xf3\x80\xff\x00\xfe\x00\xfc\x00',
  66:b'\x00\x00\x00\x00<<~~\xff\xff\xff\xff\xff\xff\xff\xff\x7f\xfe?\xfc\x1f\xf8\x0f\xf0\x07\xe0\x03\xc0\x01\x80\x00\x00',
  67:b'\x000\x00x\x0c|\x1e<?<?<?8?0\x1e\x00\x0c\x07\x00\x1f\xe1\xcf\xff\xcf\xff\xcf\xff\xc0\xff\xc0',
  68:b'\x03\xc0\x07\xe0\x07\xe0\x0f\xf0\x0f\xf0\x0f\xf0\x0f\xf0\x07\xe0\x07\xe0\x03\xc00\x0c|>\xff\xff\xff\xff\xff\xff\xff\xff',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 16, 16
