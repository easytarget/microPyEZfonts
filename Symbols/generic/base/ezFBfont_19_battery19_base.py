'''
    ezFBfont_19_battery19_base : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original battery19.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: battery19
# Cmd: ['bdf2dict.py'], ['Symbols-bdf-sources/battery19.bdf', '_', './base-char.set']
# Date: 2024-06-18 20:28:17
'''
    Original Copyright, Comments and Notices from source:

    COPYRIGHT Exported by Fony v1.4.7

    COMMENT "Created with Fony 1.4.7"
'''
version = '0.33'
name = 'battery19'
family = 'generic'
weight = 'none'
size = None

def height():
    return 19

def baseline():
    return 19

def max_width():
    return 9

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 48

def max_ch():
    return 54

_g = {
  48:b'<\x00\xff\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\xff\x00',
  49:b'<\x00\xff\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xff\x00',
  50:b'<\x00\xff\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xff\x00',
  51:b'<\x00\xff\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xff\x00',
  52:b'<\x00\xff\x00\x81\x00\x81\x00\x81\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xff\x00',
  53:b'<\x00\xff\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xff\x00',
  54:b'<\x00\xff\x00\x81\x00\x81\x00\x81\x00\x89\x00\x89\x00\x99\x00\x99\x00\xbd\x00\xbd\x00\x99\x00\x99\x00\x91\x00\x91\x00\x81\x00\x81\x00\x81\x00\xff\x00',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 19, 9
