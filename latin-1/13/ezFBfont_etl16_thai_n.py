'''
    ezFBfont_etl16_thai_n : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original etl16-thai.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Public domain font.  Share and enjoy."

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    COMMENT 94.8.25 7-bit part (ASCII) taken from etl16-latin1.bdf
    COMMENT         8-bit part (Thai) created by Manop Wongsaisuwan
    COMMENT 2000/04/18 some glyphs modified by Theppitak Karoonboonyanan
'''
# Code generated by bdf2dict.py
# Font: etl16-thai Char set: b' %()*+,-./0123456789:\xb0'
# Cmd: ['bdf2dict.py', 'bdf-sources/etl16-thai.bdf', '../latin-1/n-char.set']
# Date: 2024-06-04 14:20:56

version = '0.33'
name = '-etl-fixed-medium-r-normal--16-160-72-72-m-80-tis620-0'
family = 'fixed'
weight = 'medium'
size = 16

def height():
    return 13

def baseline():
    return 11

def max_width():
    return 8

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 37

def max_ch():
    return 176

_g = {
 37:[b'\x00b\x94\x94h\x10\x10,RR\x8c\x00\x00'],
 40:[b'\x08\x10\x10      \x10\x10\x08\x00'],
 41:[b' \x10\x10\x08\x08\x08\x08\x08\x08\x10\x10 \x00'],
 42:[b'\x00\x00\x00\x10\x92T8T\x92\x10\x00\x00\x00'],
 43:[b'\x00\x00\x00\x10\x10\x10\xfe\x10\x10\x10\x00\x00\x00'],
 44:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x08\x08\x10'],
 45:[b'\x00\x00\x00\x00\x00\x00~\x00\x00\x00\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x18\x00\x00'],
 47:[b'\x00\x02\x02\x04\x08\x08\x10\x10 @@\x00\x00'],
 48:[b'\x00\x18$BBBBBB$\x18\x00\x00'],
 49:[b'\x00\x100P\x10\x10\x10\x10\x10\x10|\x00\x00'],
 50:[b'\x00<BB\x02\x0c\x10 @@~\x00\x00'],
 51:[b'\x00<BB\x02\x1c\x02\x02BB<\x00\x00'],
 52:[b'\x00\x04\x0c\x14$DD~\x04\x04\x04\x00\x00'],
 53:[b'\x00~@@@|\x02\x02\x02B<\x00\x00'],
 54:[b'\x00\x1c @@|BBBB<\x00\x00'],
 55:[b'\x00~\x02\x02\x04\x04\x04\x08\x08\x08\x08\x00\x00'],
 56:[b'\x00<BBB<BBBB<\x00\x00'],
 57:[b'\x00<BBB>\x02\x02\x02\x048\x00\x00'],
 58:[b'\x00\x00\x00\x18\x18\x00\x00\x00\x18\x18\x00\x00\x00'],
 176:[b'\x00\x00\x00<@8\x0444\x0c\x04T,'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()

