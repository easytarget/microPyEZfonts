'''
    ezFBfont_06_font_tiny5_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original font_tiny5.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "(CC) Gissio 2022-2023 Creative Commons Zero v1.0 Universal"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    COMMENT Exported by Fony v1.4.7
'''
# Code generated by bdf2dict.py
# Font: font_tiny5
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/font_tiny5.bdf', './num-char.set', 'True']
# Date: 2024-06-11 17:34:04

version = '0.33'
name = 'font_tiny5'
family = 'None'
weight = 'None'
size = None

def height():
    return 6

def baseline():
    return 5

def max_width():
    return 5

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 176

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00',b'2'],
 37:[b'\x90 @\x90\x00\x00',b'5'],
 40:[b'@\x80\x80\x80@\x00',b'3'],
 41:[b'\x80@@@\x80\x00',b'3'],
 42:[b'@\xe0@\xa0\x00\x00',b'4'],
 43:[b'\x00@\xe0@\x00\x00',b'4'],
 44:[b'\x00\x00\x00\x00@\x80',b'3'],
 45:[b'\x00\x00\xe0\x00\x00\x00',b'4'],
 46:[b'\x00\x00\x00\x00\x80\x00',b'2'],
 47:[b'@@\x80\x80\x80\x00',b'3'],
 48:[b'@\xa0\xa0\xa0@\x00',b'4'],
 49:[b'@\xc0@@@\x00',b'4'],
 50:[b'\xc0 @\x80\xe0\x00',b'4'],
 51:[b'\xc0 @ \xc0\x00',b'4'],
 52:[b' `\xa0\xe0 \x00',b'4'],
 53:[b'\xe0\x80\xc0 \xc0\x00',b'4'],
 54:[b'`\x80\xc0\xa0@\x00',b'4'],
 55:[b'\xe0 @@@\x00',b'4'],
 56:[b'@\xa0@\xa0@\x00',b'4'],
 57:[b'@\xa0` \xc0\x00',b'4'],
 58:[b'\x00\x80\x00\x00\x80\x00',b'2'],
 176:[b'@\xa0@\x00\x00\x00',b'4'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 6, int(_g[c][1])

