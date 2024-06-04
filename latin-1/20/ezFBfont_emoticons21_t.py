'''
    ezFBfont_emoticons21_t : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original emoticons21.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "public domain,

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    COMMENT Exported by Fony v1.4.7
'''
# Code generated by bdf2dict.py
# Font: emoticons21 Char set: b' +-.0123456789:'
# Cmd: ['bdf2dict.py', 'bdf-sources/emoticons21.bdf', '../latin-1/t-char.set']
# Date: 2024-06-04 14:20:55

version = '0.33'
name = 'Emoticons21'
family = 'None'
weight = 'None'
size = None

def height():
    return 20

def baseline():
    return 20

def max_width():
    return 22

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 55

_g = {
 32:[b'\x06\x03\x00\x08\x00\x80\x10\x00@ \x00 A\x8c\x10A\x8c\x10\x81\x8c\x08\x81\x8c\x08\x80\x00\x08\x80\x00\x08\x8f\xff\x88\x88\x00\x88\x84\x01\x08C\x06\x10@\xf8\x10 \x00 \x10\x00@\x08\x00\x80\x06\x03\x00\x01\xfc\x00'],
 48:[b'\x06\x03\x00\x08\x00\x80\x10\x00@ \x00 @\x0c\x10A\x8c\x10\x83\xcc\x08\x80\x0c\x08\x80\x00\x08\x80\x00\x08\x88\x00\x88\x84\x01\x08\x83\x06\x08@\xfa\x10@"\x10 " \x10\x1c@\x08\x00\x80\x06\x03\x00\x01\xfc\x00'],
 49:[b'\x06\x03\x00\x08\x00\x80\x10\x00@ \x00 @\x0c\x10A\x8c\x10\x81\x8c\x08\x81\x8c\x08\x81\x80\x08\x80\x00\x08\x88\x00\x88\x84\x01\x08\x83\x07\x08@\xfa\x10@!\x10 \x11 \x10\x0e@\x08\x00\x80\x06\x03\x00\x01\xfc\x00'],
 50:[b'\x06\x03\x00\x08\x00\x80\x10\x00@ \x00 @\x0c\x10A\x8c\x10\x83\xcc\x08\x80\x0c\x08\x80\x00\x08\x88\x00\x08\x88\x00\x08\x84\x01\x08\x83\x06\x08@\xf8\x10@\x00\x10 \x00 \x10\x00@\x08\x00\x80\x06\x03\x00\x01\xfc\x00'],
 51:[b'\x06\x03\x00\x08\x00\x80\x10\x00@#\x8e E\xd7\x10E\xd7\x10\x84Q\x08\x83\x8e\x08\x80\x00\x08\x80\x00\x08\x88\x00\x88\x84\x01\x08\x83\x06\x08@\xf8\x10@\x00\x10 \x00 \x10\x00@\x08\x00\x80\x06\x03\x00\x01\xfc\x00'],
 52:[b'\x06\x03\x00\x08\x00\x80\x10\x00@#\x8e E\xd7\x10E\xd7\x10\x84Q\x08\x83\x8e\x08\x80\x00\x08\x80\x00\x08\x80\x00\x08\x80\x00\x08\x87\xff\x08@\x00\x10@\x00\x10 \x00 \x10\x00@\x08\x00\x80\x06\x03\x00\x01\xfc\x00'],
 53:[b'\x06\x03\x00\x08\x00\x80\x10\x00@ \x00 A\x8c\x10A\x8c\x10\x81\x8c\x08\x81\x8c\x08\x80\x00\x08\x80\x00\x08\x80p\x08\x80\x88\x08\x80\x88\x08@\x88\x10@\x88\x10 p \x10\x00@\x08\x00\x80\x06\x03\x00\x01\xfc\x00'],
 54:[b'\x06\x03\x00\x08\x00\x80\x10\x00@\x7f\xdf\xf0\x7f\xff\xf0\x7f\xff\xf0\x9f\xdf\xc8\x9f\xdf\xc8\x8f\x8f\x88\x80\x00\x08\x80\x00\x08\x88\x00\x88\x84\x01\x08C\x06\x10@\xf8\x10 \x00 \x10\x00@\x08\x00\x80\x06\x03\x00\x01\xfc\x00'],
 55:[b'\x06\x03\x00\x08\x00\x80\x10\x00@!\x8c C\xde\x10@\x00\x10\x80\x00\x08\x9f\xff\xc8\x92"H\x92"H\x92"H\x8a"\x88\x86#\x08C&\x10@\xf8\x10 \x00 \x10\x01@\x08\x00\x80\x06\x03\x00\x01\xfc\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()

