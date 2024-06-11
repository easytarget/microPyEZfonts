'''
    ezFBfont_08_open_iconic_text_1x_lower : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_text_1x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: open_iconic_text_1x
# Cmd: [bdf2dict.py], ['Symbols-bdf-sources/open_iconic_text_1x.bdf', './lower-char.set', 'True']
# Date: 2024-06-11 17:21:34

version = '0.33'
name = '"open_iconic_text_1x"'
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
    return 95

_g = {
 64:[b'\xff\x00~\x00\xff\x00~\x00'],
 65:[b'\xff\x00\xfc\x00\xff\x00\xfc\x00'],
 66:[b'\xff\x00?\x00\xff\x00?\x00'],
 67:[b'\xfcff~ccc\xfe'],
 68:[b'\x00\x04J\x89\x91R \x00'],
 69:[b'\xee\xaa\xfe(\xfe\xaa\xee\x00'],
 70:[b'\xff\xff\xff\xff\xff\xff\x01\x00'],
 71:[b'\xff\x00\xf8\x00\x00\xff\x00\xfd'],
 72:[b'\x00?m\xf3\xf3m?\x00'],
 73:[b'\x00\xe7\xe7\xe7\xc6\x84\x00\x00'],
 74:[b'\x00\x00!c\xe7\xe7\xe7\x00'],
 75:[b'\x00c\xc6\x84\xe7\xe7\xe7\x00'],
 76:[b'\x00\xe7\xe7\xe7!c\xc6\x00'],
 77:[b'\x00\x00\x00\xdb\xdb\x00\x00\x00'],
 78:[b'\xfe\x00\xf8\x00\xff\x00\xa8\x00'],
 79:[b'\xeeDD|DD\xee\x00'],
 80:[b'\x00\x00f\x99\x99f\x00\x00'],
 81:[b'\x0c\x0c\x008\x08\x10\x10\x1c'],
 82:[b'>\x1c\x18\x1800p\xf8'],
 83:[b'\xff\x00\xff\x00\xff\x00~\x00'],
 84:[b'\xff\x00\xff\x00\xff\x00\xfc\x00'],
 85:[b'\xff\x00\xff\x00\xff\x00?\x00'],
 86:[b'<<\xff\xff\xff\xff<<'],
 87:[b'\x00\x00\x00\xff\xff\x00\x00\x00'],
 88:[b'\x18\x18\x18\xff\xff\x18\x18\x18'],
 89:[b'\x1c"\x02\x04\x0c\x08\x00\x08'],
 90:[b'\xff\xbf\xdf\xb1\xff\xff\xff\xff'],
 91:[b'\xff\x99\x18\x18\x18\x18\x18<'],
 92:[b'ddddd8\x00\xfe'],
 93:[b'\xc3\xc3\xdb\xdb\xdb\x00\xff\x00'],
 94:[b'\xc3\xdb\x00\xff\x00\xdb\xc3\x00'],
 95:[b'\xff\x00\xdb\xdb\xdb\xc3\xc3\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 8, 8

