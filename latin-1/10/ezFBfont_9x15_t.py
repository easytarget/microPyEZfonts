'''
    ezFBfont_9x15_t : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 9x15.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Public domain font.  Share and enjoy."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: 9x15 Char set: b' +-.0123456789:'
# Cmd: ['bdf2dict.py', 'bdf-sources/9x15.bdf', '../latin-1/t-char.set']
# Date: 2024-06-04 14:19:51

version = '0.33'
name = '-Misc-Fixed-Medium-R-Normal--15-140-75-75-C-90-ISO10646-1'
family = 'Fixed'
weight = 'Medium'
size = 15

def height():
    return 10

def baseline():
    return 10

def max_width():
    return 9

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 43:[b'\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00\x00\x00'],
 45:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00'],
 48:[b'\x1c\x00"\x00A\x00A\x00A\x00A\x00A\x00A\x00"\x00\x1c\x00'],
 49:[b'\x08\x00\x18\x00(\x00H\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x7f\x00'],
 50:[b'>\x00A\x00A\x00\x02\x00\x04\x00\x08\x00\x10\x00 \x00@\x00\x7f\x00'],
 51:[b'\x7f\x00\x01\x00\x02\x00\x04\x00\x0e\x00\x01\x00\x01\x00\x01\x00A\x00>\x00'],
 52:[b'\x02\x00\x06\x00\n\x00\x12\x00"\x00B\x00\x7f\x00\x02\x00\x02\x00\x02\x00'],
 53:[b'\x7f\x00@\x00@\x00^\x00a\x00\x01\x00\x01\x00\x01\x00A\x00>\x00'],
 54:[b'\x1e\x00 \x00@\x00@\x00^\x00a\x00A\x00A\x00A\x00>\x00'],
 55:[b'\x7f\x00\x01\x00\x02\x00\x02\x00\x04\x00\x04\x00\x08\x00\x08\x00\x10\x00\x10\x00'],
 56:[b'\x1c\x00"\x00A\x00"\x00\x1c\x00"\x00A\x00A\x00"\x00\x1c\x00'],
 57:[b'>\x00A\x00A\x00A\x00C\x00=\x00\x01\x00\x01\x00\x02\x00<\x00'],
 58:[b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()

