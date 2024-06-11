'''
    ezFBfont_24_battery24_lower : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original battery24.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Created with Fony 1.4.7"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    COMMENT Exported by Fony v1.4.7
'''
# Code generated by bdf2dict.py
# Font: battery24
# Cmd: [bdf2dict.py], ['Symbols-bdf-sources/battery24.bdf', './lower-char.set', 'True']
# Date: 2024-06-11 17:20:49

version = '0.33'
name = 'Battery24'
family = 'None'
weight = 'None'
size = None

def height():
    return 24

def baseline():
    return 24

def max_width():
    return 20

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 64

def max_ch():
    return 70

_g = {
 64:[b'\x01\xf8\x00\x01\xf8\x00\x01\xf8\x00\x7f\xff\xe0\xff\xff\xf0\xff\xff\xf0\xff\xdf\xf0\xff\x9f\xf0\xff?\xf0\xff\x7f\xf0\xfeq\xf0\xfcA\xf0\xfc\x03\xf0\xf8#\xf0\xf8\xe7\xf0\xff\xe7\xf0\xff\xcf\xf0\xff\xcf\xf0\xff\x9f\xf0\xff?\xf0\xff\x7f\xf0\xff\xff\xf0\xff\xff\xf0\x7f\xff\xe0'],
 65:[b'\x01\xf8\x00\x01\xf8\x00\x01\xf8\x00\x7f\xff\xe0\xff\xff\xf0\xe0\x00p\xc3\xfc0\xc4\x020\xc4\x020\xc3\xfc0\xc0\x000\xc0\x000\xc3\xfc0\xc4\x020\xc4\x020\xc3\xfc0\xc0\x000\xc0\x000\xc7\xfe0\xc2\x000\xc0\x000\xe0\x00p\xff\xff\xf0\x7f\xff\xe0'],
 66:[b'\x01\xf8\x00\x01\xf8\x00\x01\xf8\x00\x7f\xff\xe0\xff\xff\xf0\xe0\x00p\xcf\xff0\xc0\x000\xdf\xff\xb0\xc0\x000\xdf\xff\xb0\xc0\x000\xdf\xff\xb0\xc0\x000\xdf\xff\xb0\xc0\x000\xdf\xff\xb0\xc0\x000\xdf\xff\xb0\xc0\x000\xcf\xff0\xe0\x00p\xff\xff\xf0\x7f\xff\xe0'],
 67:[b'\x01\xf8\x00\x01\xf8\x00\x01\xf8\x00\x7f\xff\xe0\xff\xff\xf0\xe0\x00p\xc0\x000\xc0\x000\xc0\x000\xc0\x000\xc0\x000\xc0\x000\xc0\x000\xc0\x000\xc0\x000\xc0\x000\xc0\x000\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xcf\xff0\xe0\x00p\xff\xff\xf0\x7f\xff\xe0'],
 68:[b'\x01\xf8\x00\x01\xf8\x00\x01\xf8\x00\x7f\xff\xe0\xff\xff\xf0\xe0\x00p\xc0\x000\xc0\x000\xc0\x000\xc0\x000\xc0\x000\xc0\x000\xc0\x000\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xcf\xff0\xe0\x00p\xff\xff\xf0\x7f\xff\xe0'],
 69:[b'\x01\xf8\x00\x01\xf8\x00\x01\xf8\x00\x7f\xff\xe0\xff\xff\xf0\xe0\x00p\xc0\x000\xc0\x000\xc0\x000\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xcf\xff0\xe0\x00p\xff\xff\xf0\x7f\xff\xe0'],
 70:[b'\x01\xf8\x00\x01\xf8\x00\x01\xf8\x00\x7f\xff\xe0\xff\xff\xf0\xe0\x00p\xcf\xff0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xdf\xff\xb0\xcf\xff0\xe0\x00p\xff\xff\xf0\x7f\xff\xe0'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 24, 20
