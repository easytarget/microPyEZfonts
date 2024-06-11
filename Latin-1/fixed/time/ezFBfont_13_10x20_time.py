'''
    ezFBfont_13_10x20_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 10x20.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Public domain font.  Share and enjoy."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: 10x20
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/10x20.bdf', './time-char.set', 'True']
# Date: 2024-06-11 17:32:19

version = '0.33'
name = '-Misc-Fixed-Medium-R-Normal--20-200-75-75-C-100-ISO10646-1'
family = 'fixed'
weight = 'medium'
size = 20

def height():
    return 13

def baseline():
    return 13

def max_width():
    return 10

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 58

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 43:[b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00'],
 45:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x0e\x00'],
 48:[b'\x0c\x00\x1e\x003\x003\x00a\x80a\x80a\x80a\x80a\x803\x003\x00\x1e\x00\x0c\x00'],
 49:[b'\x0c\x00\x1c\x00<\x00l\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80'],
 50:[b'\x1e\x003\x00a\x80a\x80\x01\x80\x01\x80\x03\x00\x0e\x00\x18\x000\x00`\x00`\x00\x7f\x80'],
 51:[b'\x1e\x003\x00a\x80a\x80\x01\x80\x03\x00\x0e\x00\x03\x00\x01\x80a\x80a\x803\x00\x1e\x00'],
 52:[b'\x01\x00\x03\x00\x07\x00\x0f\x00\x1b\x003\x00c\x00c\x00\x7f\x80\x03\x00\x03\x00\x03\x00\x03\x00'],
 53:[b'\x7f\x80`\x00`\x00`\x00`\x00n\x00s\x00\x01\x80\x01\x80\x01\x80a\x803\x00\x1e\x00'],
 54:[b'\x1e\x003\x00a\x00`\x00`\x00n\x00s\x00a\x80a\x80a\x80a\x803\x00\x1e\x00'],
 55:[b'\x7f\x80\x01\x80\x01\x80\x03\x00\x03\x00\x06\x00\x06\x00\x0c\x00\x0c\x00\x18\x00\x18\x000\x000\x00'],
 56:[b'\x1e\x003\x00a\x80a\x80a\x803\x00\x1e\x003\x00a\x80a\x80a\x803\x00\x1e\x00'],
 57:[b'\x1e\x003\x00a\x80a\x80a\x80a\x803\x80\x1d\x80\x01\x80\x01\x80!\x803\x00\x1e\x00'],
 58:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 13, 10
