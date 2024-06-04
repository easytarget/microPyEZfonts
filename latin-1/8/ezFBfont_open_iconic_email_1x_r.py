'''
    ezFBfont_open_iconic_email_1x_r : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_email_1x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: open_iconic_email_1x Char set: b' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
# Cmd: ['bdf2dict.py', 'bdf-sources/open_iconic_email_1x.bdf', '../latin-1/r-char.set']
# Date: 2024-06-04 14:21:13

version = '0.33'
name = '"open_iconic_email_1x"'
family = 'None'
weight = 'None'
size = None

def height():
    return 8

def baseline():
    return 8

def max_width():
    return 8

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
 64:[b'\x00\xff~\x99\xe7\xff\xff\x00'],
 65:[b'\x18f\x81\xbd\x99\xe7\xff\xff'],
 66:[b'\xff\xff\x81\x81\x81\xc3\xff\xff'],
 67:[b'\xe0\x90\x98|>\x1e\x0c\x00'],
 68:[b'\x00\xc8\xa4r2\x00\x00\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()

