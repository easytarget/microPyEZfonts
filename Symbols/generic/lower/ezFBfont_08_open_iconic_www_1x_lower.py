'''
    ezFBfont_08_open_iconic_www_1x_lower : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_www_1x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: open_iconic_www_1x
# Cmd: [bdf2dict.py], ['Symbols-bdf-sources/open_iconic_www_1x.bdf', '_', './lower-char.set']
# Date: 2024-06-13 11:39:02

version = '0.33'
name = '"open_iconic_www_1x"'
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
    return 83

_g = {
 64:[b'\x18<<\x18\x00\x18\x18\x00'],
 65:[b'<<<<<<$\x00'],
 66:[b'\x00\xe0?\x1e\x1e\x00\x12\x00'],
 67:[b'\x1c>~\xf7\xe3\x08\x1c\x08'],
 68:[b'\xb8\xbe\xbc\xbc\x8e\x80\x80\x80'],
 69:[b'&i\x01"D\x80\x96d'],
 70:[b'\x00\x06\x1e|<\x18\x08\x00'],
 71:[b'<fBBf<\x18\x00'],
 72:[b'\xe0\xf8<\xce\xf67\x9b\xdb'],
 73:[b'\x08\x18\x18\xbe\xbe\xbc\xbc\x00'],
 74:[b'<F\x87\x89\x91\xe1b<'],
 75:[b'\xff\xa1\xff\x81\x81\x81\x81\xff'],
 76:[b'\x1c>~\xe3\xeb\x08\x1c\x08'],
 77:[b'\xc7\x87\x87\x88\x80\x80\x81\xff'],
 78:[b'<f\xc7\x87\x8f\xc3b<'],
 79:[b'\x06\x01\x19"D\x98\x80`'],
 80:[b'\xff\x81\xb9\xa9\xb9\x97\x81\xff'],
 81:[b'p\x18d\x1ak5\xd5\xc0'],
 82:[b'\xbc\xbc\xbe\xbe\x18\x18\x08\x00'],
 83:[b'\x02\xff\x02\x00@\xff@\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 8, 8

