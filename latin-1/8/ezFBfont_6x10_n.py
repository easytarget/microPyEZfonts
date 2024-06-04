'''
    ezFBfont_6x10_n : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 6x10.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Public domain terminal emulator font.  Share and enjoy."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: 6x10 Char set: b' %()*+,-./0123456789:\xb0'
# Cmd: ['bdf2dict.py', 'bdf-sources/6x10.bdf', '../latin-1/n-char.set']
# Date: 2024-06-04 14:19:41

version = '0.33'
name = '-Misc-Fixed-Medium-R-Normal--10-100-75-75-C-60-ISO10646-1'
family = 'Fixed'
weight = 'Medium'
size = 10

def height():
    return 8

def baseline():
    return 7

def max_width():
    return 6

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
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00'],
 37:[b'H\xa8P P\xa8\x90\x00'],
 40:[b'\x10 @@@ \x10\x00'],
 41:[b'@ \x10\x10\x10 @\x00'],
 42:[b'\x00\x88P\xf8P\x88\x00\x00'],
 43:[b'\x00  \xf8  \x00\x00'],
 44:[b'\x00\x00\x00\x00\x000 @'],
 45:[b'\x00\x00\x00\xf8\x00\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00 p '],
 47:[b'\x08\x08\x10 @\x80\x80\x00'],
 48:[b' P\x88\x88\x88P \x00'],
 49:[b' `\xa0   \xf8\x00'],
 50:[b'p\x88\x080@\x80\xf8\x00'],
 51:[b'\xf8\x08\x100\x08\x88p\x00'],
 52:[b'\x100P\x90\xf8\x10\x10\x00'],
 53:[b'\xf8\x80\xb0\xc8\x08\x88p\x00'],
 54:[b'0@\x80\xb0\xc8\x88p\x00'],
 55:[b'\xf8\x08\x10\x10 @@\x00'],
 56:[b'p\x88\x88p\x88\x88p\x00'],
 57:[b'p\x88\x98h\x08\x10`\x00'],
 58:[b'\x00 p \x00 p '],
 176:[b' P \x00\x00\x00\x00\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()
