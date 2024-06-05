'''
    ezFBfont_m2icon_5_e : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original m2icon_5.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "public domain"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    COMMENT http://code.google.com/p/u8glib/
'''
# Code generated by bdf2dict.py
# Font: m2icon_5 Char set: b' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
# Cmd: ['bdf2dict.py', 'bdf-sources/m2icon_5.bdf', '../latin-1/e-char.set']
# Date: 2024-06-04 14:21:02

version = '0.33'
name = 'm2icon5'
family = ''
weight = 'Medium'
size = None

def height():
    return 6

def baseline():
    return 5

def max_width():
    return 10

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 65

def max_ch():
    return 104

_g = {
 65:[b'\x1c\x00\xfe\x00\x82\x00\x82\x00\xfe\x00\x00\x00',9],
 66:[b'p\xd0\x90\x90\xf0\x00',8],
 67:[b'\x00\xd8pp\xd8\x00',6],
 68:[b'\x06\x0c\xd8p \x00',8],
 69:[b'\x00\xf0\x90\x90\xf0\x00',5],
 70:[b'\x00\xf0\x90\xd0\xf0\x00',5],
 71:[b'\x00\xf0\xf0\xf0\xf0\x00',5],
 72:[b'\xf8\x88\x88\x88\xf8\x00',6],
 73:[b'\xf8\x88\xa8\x88\xf8\x00',6],
 74:[b'\xf8\xf8\xf8\xf8\xf8\x00',6],
 75:[b'\x00\xe0\xb0\xf0p\x00',5],
 76:[b'\x00\xe0\xb0\xf0p\x00',5],
 77:[b'\x00\xe0\xf0\xf0p\x00',5],
 78:[b'\xf0\x98\x98\xf8x\x00',6],
 79:[b'\xf0\x98\xd8\xf8x\x00',6],
 80:[b'\xf0\xf8\xf8\xf8x\x00',6],
 81:[b'\x00`\x90\x90`\x00',5],
 82:[b'\x00`\x90\xd0`\x00',5],
 83:[b'\x00`\xf0\xf0`\x00',5],
 97:[b' @\xfe@ \x00',8],
 98:[b' p\xa8  \x00',6],
 102:[b'\x1c\x00\xfe\x00\x82\x00\xbf\x80\xff\x00\x00\x00',10],
 103:[b'\x80\x80\x80\x80\x80\x80',2],
 104:[b'  \xf8  \x00',6],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), _g[c][1]

