'''
    ezFBfont_open_iconic_other_1x_u : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_other_1x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: open_iconic_other_1x Char set: b' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_'
# Cmd: ['bdf2dict.py', 'bdf-sources/open_iconic_other_1x.bdf', '../latin-1/u-char.set']
# Date: 2024-06-04 14:21:18

version = '0.33'
name = '"open_iconic_other_1x"'
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
    return 71

_g = {
 64:[b'\x00\x10\x10<x\x10\x10\x00'],
 65:[b'\x00<B\x99\xbd<\x18\x00'],
 66:[b'\xee\xee\xeeD|\xe0\xe0\xe0'],
 67:[b'\xaa\x00\xaa\x00\xaa\x00\xaa\x00'],
 68:[b'\xdb\xdb\x00\xdb\xdb\x00\xdb\xdb'],
 69:[b'\xe7\xe7\xe7\x00\x00\xe7\xe7\xe7'],
 70:[b'\x02\n\n**\xaa\xaa\xaa'],
 71:[b'<B\x99\xa5\xa5\x99B<'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()
