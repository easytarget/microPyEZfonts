'''
    ezFBfont_open_iconic_email_2x_e : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_email_2x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: open_iconic_email_2x Char set: b' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
# Cmd: ['bdf2dict.py', 'bdf-sources/open_iconic_email_2x.bdf', '../latin-1/e-char.set']
# Date: 2024-06-04 14:21:14

version = '0.33'
name = '"open_iconic_email_2x"'
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
    return 68

_g = {
 64:[b'\x00\x00\x00\x00\xff\xff\xff\xff\x7f\xfe\x1f\xf8\x87\xe1\xe1\x87\xf8\x1f\xfe\x7f\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00'],
 65:[b'\x01\x80\x07\xe0\x1exx\x1e\xe0\x07\xc0\x03\xcf\xf3\xcf\xf3\xc7\xe3\xe1\x87\xf8\x1f\xfe\x7f\xff\xff\xff\xff\xff\xff\xff\xff'],
 66:[b'\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\xf0\x0f\xf8\x1f\xff\xff\xff\xff\xff\xff\xff\xff'],
 67:[b'\xfc\x00\xfe\x00\xe7\x00\xc3\x80\xc3\xc0\xe7\xe0\x7f\xf0?\xf8\x1f\xfc\x0f\xfe\x07\xfe\x03\xfc\x01\xf8\x00\xf0\x00`\x00\x00'],
 68:[b'\x00\x00\x00\x00\xf1\xc0\xf8\xe0\xccp\xce8\x7f\x1c?\x8e\x1f\x8e\x0f\x1c\x06\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()
