'''
    ezFBfont_08_open_iconic_gui_1x_lower : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_gui_1x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: open_iconic_gui_1x
# Cmd: [bdf2dict.py], ['Symbols-bdf-sources/open_iconic_gui_1x.bdf', '_', './lower-char.set']
# Date: 2024-06-13 11:38:34

version = '0.33'
name = '"open_iconic_gui_1x"'
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
    return 93

_g = {
 64:[b'\x1f\x01\t\xfd\t\x01\x1f\x00'],
 65:[b'\x1f\x01A\xfdA\x01\x1f\x00'],
 66:[b'\x008\x0c\x06\x06\x06\x00\x00'],
 67:[b'\x00\x1c0```\x00\x00'],
 68:[b'\xff\xff\x00\x18\x00\x00\x00\xff'],
 69:[b'\x83\x83\x83\x8b\x8b\x83\x83\x83'],
 70:[b'\xc1\xc1\xc1\xd1\xd1\xc1\xc1\xc1'],
 71:[b'\xff\x00\x00\x00\x18\x00\xff\xff'],
 72:[b'A\xfeFJRb\x7f\x02'],
 73:[b'<B\x81\xa5\x99\x99B<'],
 74:[b'\x00\x18<\x00\x00<\x18\x00'],
 75:[b'\xff\x00\x18\x00\x00\x00\xff\xff'],
 76:[b'\x83\x83\x83\xa3\xa3\x83\x83\x83'],
 77:[b'\xc1\xc1\xc1\xc5\xc5\xc1\xc1\xc1'],
 78:[b'\xff\xff\x00\x00\x00\x18\x00\xff'],
 79:[b'\xe0\xe0\xe0\x00\x00\x07\x07\x07'],
 80:[b'\x00ppp\x0e\x0e\x0e\x00'],
 81:[b'\xf0\xf0\xf4\xf4\x05=\x01\x0f'],
 82:[b'\xbf\x00\xbf\x00\xbf\x00\xbf\x00'],
 83:[b'\xef\xe0\xee\x00\xef\xe0\xee\x00'],
 84:[b'\x00\xff\x00\x00\xff\x00\x00\xff'],
 85:[b'\x10\x10\x10\xfe\x10\x10\x10\x00'],
 86:[b'<<\x00\xff\x81\xbd<<'],
 87:[b'\x07\x07\x07\x08\x90\xe0\xe0\xe0'],
 88:[b'\x108|\x10\x10|8\x10'],
 89:[b'\x00$f\xfff$\x00\x00'],
 90:[b', . / p '],
 91:[b'/ . , p '],
 92:[b'8D\x92\xba\x92F?\x03'],
 93:[b'8D\x82\xba\x82F?\x03'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 8, 8

