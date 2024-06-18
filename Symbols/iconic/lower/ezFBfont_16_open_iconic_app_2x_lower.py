'''
    ezFBfont_16_open_iconic_app_2x_lower : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_app_2x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: open_iconic_app_2x
# Cmd: ['bdf2dict.py'], ['Symbols-bdf-sources/open_iconic_app_2x.bdf', '_', './lower-char.set']
# Date: 2024-06-18 20:28:25
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"
'''
version = '0.33'
name = 'open_iconic_app_2x'
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
    return 72

_g = {
  64:b'\x07\xe0\x07\xf0#\xf0p\xe6|f\xfc\x07\xf0\x0f\xe0\x0f\x80\x0f\x00\x1f8\x00x\x00x\xfe<\xfc\x1c\xf8\x04`',
  65:b'\xff\xfc\xff\xfc\xc0\x0c\xc0\x0c\xc0\x0c\xc0\x0c\xff\xfc\xff\xfc\xcc\xcc\xcc\xcc\xff\xcc\xff\xcc\xcc\xcc\xcc\xcc\xff\xfc\xff\xfc',
  66:b'\xff\xfc\xff\xfc\xff\xfc\xff\xfc\x00\x00\x00\x00\xff\xfc\xff\xfc\xcc\xcc\xcc\xcc\xff\xfc\xff\xfc\xcc\xfc\xcc\xfc\xff\xfc\xff\xfc',
  67:b'\x00\xf0\x01\xf8\x01\xf8\x03\xfc\x7f\xff\xff\xff\xcf\x0f\xce\x07\xfcc\xfc\xf3\xfc\xf3\xfcc\xfe\x07\xff\x0f\xff\xff\xff\xff',
  68:b'\xff\xc0\xff\xc0\xf0\x00\xf0\x00\xf3\xff\xf3\xff\xf3\xff\xf3\xff\x83\xff\x03\xff\x03\xff\x03\xff\x00\x01\x00\x00\x00\x00\x00\x00',
  69:b'\x07\xe0\x1f\xf8<<p\x0ea\x86\xe1\x87\xc1\x83\xc1\x83\xc1\xc3\xc0\xc3\xe0\x07`\x06p\x0e<<\x1f\xf8\x07\xe0',
  70:b'\x07\xe0\x1f\xf8<<p\x0e`\x16\xe0\xe7\xc3\xe3\xc2c\xc6C\xc7\xc3\xe7\x07h\x06p\x0e<<\x1f\xf8\x07\xe0',
  71:b'\x01\x80\x0f\xf0>\xfc\xf8\xff\xc0\xff\xc0\xff\xc0\xff`\xfe`\xfe`\xfe0\xfc8\xfc\x1c\xf8\x0e\xf0\x07\xe0\x03\xc0',
  72:b'\x0f\xc0\x0f\xc0\x0f\x80\x1f\x808\x10` \xe0@\xc1\xcc\xc3\x8c\xc3\x0c\xc0\x0c\xe0\x1c`\x188p\x1f\xe0\x0f\xc0',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 16, 16
