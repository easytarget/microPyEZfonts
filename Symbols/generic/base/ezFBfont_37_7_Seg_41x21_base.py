'''
    ezFBfont_37_7_Seg_41x21_base : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 7_Seg_41x21.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: 7_Seg_41x21
# Cmd: ['bdf2dict.py'], ['Symbols-bdf-sources/7_Seg_41x21.bdf', '_', './base-char.set']
# Date: 2024-06-18 20:28:17
'''
    Original Copyright, Comments and Notices from source:

    COPYRIGHT Exported by Fony v1.4.0.2

    COMMENT "Created with Fony 1.4.0.2"
'''
version = '0.33'
name = '7_seg_41x21'
family = 'generic'
weight = 'none'
size = None

def height():
    return 37

def baseline():
    return 37

def max_width():
    return 21

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 43

def max_ch():
    return 58

_g = {
  43:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x07\x00\x07\x00?\xe0?\xe0?\xe0\x07\x00\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r',
  44:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00888\x07',
  45:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\xe0?\xe0?\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00888\x07',
  48:b'\x0f\xff\x80\x17\xff@\x1b\xfe\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x18\x00\xc0\x10\x00@\x00\x00\x00\x10\x00@\x18\x00\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1b\xfe\xc0\x17\xff@\x0f\xff\x80\x15',
  49:b'\x00\x00@\x00\x00\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x00\xc0\x00\x00@\x00\x00\x00\x00\x00@\x00\x00\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x00\xc0\x00\x00@\x15',
  50:b'\x1f\xff\x80\x0f\xff@\x07\xfe\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x00\xc0\x07\xff@\x0f\xff\x80\x17\xff\x00\x18\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1b\xff\x00\x17\xff\x80\x0f\xff\xc0\x15',
  51:b'\x1f\xff\x80\x0f\xff@\x07\xfe\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x00\xc0\x07\xff@\x0f\xff\x80\x07\xff@\x00\x00\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x07\xfe\xc0\x0f\xff@\x1f\xff\x80\x15',
  52:b'\x10\x00@\x18\x00\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x18\x00\xc0\x17\xff@\x0f\xff\x80\x07\xff@\x00\x00\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x00\xc0\x00\x00@\x15',
  53:b'\x0f\xff\xc0\x17\xff\x80\x1b\xff\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x18\x00\x00\x17\xff\x00\x0f\xff\x80\x07\xff@\x00\x00\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x07\xfe\xc0\x0f\xff@\x1f\xff\x80\x15',
  54:b'\x0f\xff\xc0\x17\xff\x80\x1b\xff\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x1c\x00\x00\x18\x00\x00\x17\xff\x00\x0f\xff\x80\x17\xff@\x18\x00\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1b\xfe\xc0\x17\xff@\x0f\xff\x80\x15',
  55:b'\x1f\xff\x80\x0f\xff@\x07\xfe\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x00\xc0\x00\x00@\x00\x00\x00\x00\x00@\x00\x00\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x00\xc0\x00\x00@\x15',
  56:b'\x0f\xff\x80\x17\xff@\x1b\xfe\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x18\x00\xc0\x17\xff@\x0f\xff\x80\x17\xff@\x18\x00\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1b\xfe\xc0\x17\xff@\x0f\xff\x80\x15',
  57:b'\x0f\xff\x80\x17\xff@\x1b\xfe\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x1c\x01\xc0\x18\x00\xc0\x17\xff@\x0f\xff\x80\x07\xff@\x00\x00\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x00\x01\xc0\x07\xfe\xc0\x0f\xff@\x1f\xff\x80\x15',
  58:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00888\x00\x00\x00\x00\x00\x00\x00\x00\x00888\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 37, int(_g[c][-1])
