'''
    ezFBfont_08_open_iconic_mime_1x_lower : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_mime_1x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: open_iconic_mime_1x
# Cmd: [bdf2dict.py], ['Symbols-bdf-sources/open_iconic_mime_1x.bdf', '_', './lower-char.set']
# Date: 2024-06-13 11:38:41

version = '0.33'
name = '"open_iconic_mime_1x"'
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
    return 77

_g = {
 64:[b'\x00B\x81\xa5\xa5\xc3\x00\x00'],
 65:[b'\xf2\xf2\xf2\xfe\xfe\xfe\x80\xfe'],
 66:[b'\xe0\xe8\xac\xe0\xbe\xfe\x86\xfe'],
 67:[b'\xe0\xff\x00\xff\xff\xff\xff\xff'],
 68:[b'\xff\x81\x81\x81\xe3\xf1\xf9\xff'],
 69:[b'\x81\xb1\x81\x99\x81\x8d\x81\x00'],
 70:[b'\xff\xa1\xff\xa1\xff\xa1\xff\x00'],
 71:[b'\x00\xfc\xfd\xff\xfd\xfc\x00\x00'],
 72:[b'\x10\xba\x82\xfe\xfe\xfe\xfe\xfe'],
 73:[b'\xe0\xe8\xec\xe0\xfe\xfe\xfe\xfe'],
 74:[b'\x00\x02\x048@\x80\x00\xff'],
 75:[b'04\x16\xc7\xe7\xcf\x1e\x1c'],
 76:[b'?// >\xbe\xbe\xfe'],
 77:[b'8\xfe\x00TTTT|'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 8, 8

