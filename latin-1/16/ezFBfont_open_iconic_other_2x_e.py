'''
    ezFBfont_open_iconic_other_2x_e : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_other_2x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: open_iconic_other_2x Char set: b' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
# Cmd: ['bdf2dict.py', 'bdf-sources/open_iconic_other_2x.bdf', '../latin-1/e-char.set']
# Date: 2024-06-04 14:21:18

version = '0.33'
name = '"open_iconic_other_2x"'
family = 'None'
weight = 'None'
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
    return 71

_g = {
 64:[b'\x00\x00\x01\x00\x01\x00\x03\x00\x07\x00\x07\x00\x0f\xf0\x0f\xe0\x1f\xc0?\xc0\x03\x80\x03\x80\x03\x00\x02\x00\x02\x00\x00\x00'],
 65:[b'\x00\x00\x00\x00\x07\xe0\x1f\xf8<<p\x0ebF\xe7\xe7\xcf\xf3\xcf\xf3\x0f\xf0\x0f\xf0\x07\xe0\x03\xc0\x00\x00\x00\x00'],
 66:[b'xx\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfcxx0000?\xf0?\xe0x\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00x\x00'],
 67:[b'\xcc\xcc\xcc\xcc\x00\x00\x00\x00\xcc\xcc\xcc\xcc\x00\x00\x00\x00\xcc\xcc\xcc\xcc\x00\x00\x00\x00\xcc\xcc\xcc\xcc\x00\x00\x00\x00'],
 68:[b'\xf3\xcf\xf3\xcf\xf3\xcf\xf3\xcf\x00\x00\x00\x00\xf3\xcf\xf3\xcf\xf3\xcf\xf3\xcf\x00\x00\x00\x00\xf3\xcf\xf3\xcf\xf3\xcf\xf3\xcf'],
 69:[b'\xfc?\xfc?\xfc?\xfc?\xfc?\xfc?\x00\x00\x00\x00\x00\x00\x00\x00\xfc?\xfc?\xfc?\xfc?\xfc?\xfc?'],
 70:[b'\x00\x0c\x00\x0c\x00\xcc\x00\xcc\x00\xcc\x00\xcc\x0c\xcc\x0c\xcc\x0c\xcc\x0c\xcc\xcc\xcc\xcc\xcc\xcc\xcc\xcc\xcc\xcc\xcc\xcc\xcc'],
 71:[b'\x07\xe0\x1f\xf8<<p\x0ec\xc6\xe7\xe7\xces\xcc3\xcc3\xces\xe7\xe7c\xc6p\x0e<<\x1f\xf8\x07\xe0'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()

