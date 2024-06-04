'''
    ezFBfont_open_iconic_app_2x_e : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_app_2x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: open_iconic_app_2x Char set: b' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
# Cmd: ['bdf2dict.py', 'bdf-sources/open_iconic_app_2x.bdf', '../latin-1/e-char.set']
# Date: 2024-06-04 14:21:11

version = '0.33'
name = '"open_iconic_app_2x"'
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
    return 72

_g = {
 64:[b'\x07\xe0\x07\xf0#\xf0p\xe6|f\xfc\x07\xf0\x0f\xe0\x0f\x80\x0f\x00\x1f8\x00x\x00x\xfe<\xfc\x1c\xf8\x04`'],
 65:[b'\xff\xfc\xff\xfc\xc0\x0c\xc0\x0c\xc0\x0c\xc0\x0c\xff\xfc\xff\xfc\xcc\xcc\xcc\xcc\xff\xcc\xff\xcc\xcc\xcc\xcc\xcc\xff\xfc\xff\xfc'],
 66:[b'\xff\xfc\xff\xfc\xff\xfc\xff\xfc\x00\x00\x00\x00\xff\xfc\xff\xfc\xcc\xcc\xcc\xcc\xff\xfc\xff\xfc\xcc\xfc\xcc\xfc\xff\xfc\xff\xfc'],
 67:[b'\x00\xf0\x01\xf8\x01\xf8\x03\xfc\x7f\xff\xff\xff\xcf\x0f\xce\x07\xfcc\xfc\xf3\xfc\xf3\xfcc\xfe\x07\xff\x0f\xff\xff\xff\xff'],
 68:[b'\xff\xc0\xff\xc0\xf0\x00\xf0\x00\xf3\xff\xf3\xff\xf3\xff\xf3\xff\x83\xff\x03\xff\x03\xff\x03\xff\x00\x01\x00\x00\x00\x00\x00\x00'],
 69:[b'\x07\xe0\x1f\xf8<<p\x0ea\x86\xe1\x87\xc1\x83\xc1\x83\xc1\xc3\xc0\xc3\xe0\x07`\x06p\x0e<<\x1f\xf8\x07\xe0'],
 70:[b'\x07\xe0\x1f\xf8<<p\x0e`\x16\xe0\xe7\xc3\xe3\xc2c\xc6C\xc7\xc3\xe7\x07h\x06p\x0e<<\x1f\xf8\x07\xe0'],
 71:[b'\x01\x80\x0f\xf0>\xfc\xf8\xff\xc0\xff\xc0\xff\xc0\xff`\xfe`\xfe`\xfe0\xfc8\xfc\x1c\xf8\x0e\xf0\x07\xe0\x03\xc0'],
 72:[b'\x0f\xc0\x0f\xc0\x0f\x80\x1f\x808\x10` \xe0@\xc1\xcc\xc3\x8c\xc3\x0c\xc0\x0c\xe0\x1c`\x188p\x1f\xe0\x0f\xc0'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()

