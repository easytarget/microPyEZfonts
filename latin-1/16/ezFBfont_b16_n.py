'''
    ezFBfont_b16_n : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original b16.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "(c) Copyright 2000-2003 /efont/ The Electronic Font Open Laboratory."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: b16 Char set: b' %()*+,-./0123456789:\xb0'
# Cmd: ['bdf2dict.py', 'bdf-sources/b16.bdf', '../latin-1/n-char.set']
# Date: 2024-06-04 14:20:35

version = '0.33'
name = '-Efont-Biwidth-Medium-R-Normal--16-160-75-75-P-80-ISO10646-1'
family = 'Biwidth'
weight = 'Medium'
size = 16

def height():
    return 16

def baseline():
    return 14

def max_width():
    return 8

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 176

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 37:[b'\x00\x00\x00\x001JJ4\x08\x08\x16))F\x00\x00'],
 40:[b'\x00\x00\x00\x04\x08\x08\x10\x10\x10\x10\x10\x10\x08\x08\x04\x00'],
 41:[b'\x00\x00\x00 \x10\x10\x08\x08\x08\x08\x08\x08\x10\x10 \x00'],
 42:[b'\x00\x00\x00\x00\x00\x00\x08I*\x1c*I\x08\x00\x00\x00'],
 43:[b'\x00\x00\x00\x00\x00\x00\x08\x08\x08\x7f\x08\x08\x08\x00\x00\x00'],
 44:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x08\x08\x10'],
 45:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00~\x00\x00\x00\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x18\x00\x00'],
 47:[b'\x00\x00\x00\x00\x02\x02\x04\x08\x08\x10\x10 @@\x00\x00'],
 48:[b'\x00\x00\x00\x00\x18$BBBBBB$\x18\x00\x00'],
 49:[b'\x00\x00\x00\x00\x08\x18(\x08\x08\x08\x08\x08\x08>\x00\x00'],
 50:[b'\x00\x00\x00\x00<BB\x02\x0c\x10 @@~\x00\x00'],
 51:[b'\x00\x00\x00\x00<BB\x02\x1c\x02\x02BB<\x00\x00'],
 52:[b'\x00\x00\x00\x00\x04\x0c\x14$DD~\x04\x04\x04\x00\x00'],
 53:[b'\x00\x00\x00\x00~@@@|\x02\x02\x02B<\x00\x00'],
 54:[b'\x00\x00\x00\x00\x1c @@|BBBB<\x00\x00'],
 55:[b'\x00\x00\x00\x00~\x02\x02\x04\x04\x04\x08\x08\x08\x08\x00\x00'],
 56:[b'\x00\x00\x00\x00<BBB<BBBB<\x00\x00'],
 57:[b'\x00\x00\x00\x00<BBB>\x02\x02\x02\x048\x00\x00'],
 58:[b'\x00\x00\x00\x00\x00\x00\x18\x18\x00\x00\x00\x18\x18\x00\x00\x00'],
 176:[b'\x10((\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()

