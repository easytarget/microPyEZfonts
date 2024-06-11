'''
    ezFBfont_08_open_iconic_all_1x_extended : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_all_1x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: open_iconic_all_1x
# Cmd: [bdf2dict.py], ['Symbols-bdf-sources/open_iconic_all_1x.bdf', './extended-char.set', 'True']
# Date: 2024-06-11 17:20:54

version = '0.33'
name = '"open_iconic_all_1x"'
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
    return 256

def max_ch():
    return 286

_g = {
 256:[b'/ . , p '],
 257:[b'\xff\xa1\xff\xa1\xff\xa1\xff\x00'],
 258:[b'\x00\x00\x18~<<$\x00'],
 259:[b'\x00B\x18<<\x18B\x00'],
 260:[b'\xfe\x82\x82\x82\x82\x82\xfe\xfe'],
 261:[b'\xe0\x90\x98|>\x1e\x0c\x00'],
 262:[b'\x00\xc8\xa4r2\x00\x00\x00'],
 263:[b'<B\x99\xa5\xa5\x99B<'],
 264:[b'\xf8\x82\x84\x98\x82\x82\xfe\x00'],
 265:[b'\xff\xbf\xdf\xb1\xff\xff\xff\xff'],
 266:[b'\xff\x99\x18\x18\x18\x18\x18<'],
 267:[b'\xbc\xbc\xbe\xbe\x18\x18\x08\x00'],
 268:[b'\x08\x18\x18\xbe\xbe\xbc\xbc\x00'],
 269:[b'88@\x8a\x92\x82D8'],
 270:[b'\x02\xff\x02\x00@\xff@\x00'],
 271:[b'8\xfe\x00TTTT|'],
 272:[b'ddddd8\x00\xfe'],
 273:[b'\xc3\xc3\xdb\xdb\xdb\x00\xff\x00'],
 274:[b'\xc3\xdb\x00\xff\x00\xdb\xc3\x00'],
 275:[b'\xff\x00\xdb\xdb\xdb\xc3\xc3\x00'],
 276:[b'\x00\xfc\xfd\xff\xfd\xfc\x00\x00'],
 277:[b'\x106\xf3\xf5\xf5\xf36\x10'],
 278:[b'\x08\x18xzzx\x18\x08'],
 279:[b'\x04\x0c<<<<\x0c\x04'],
 280:[b'\x1088hl|\xee\xfe'],
 281:[b'|\x82\x008\x00\x00\x18\x18'],
 282:[b'\x08\x18\x18\x1f>p\xe0\xc0'],
 283:[b'B\xe7~<<~\xe7B'],
 284:[b'\x82D(\xfe\x10\xfe\x10\x10'],
 285:[b'8D\x92\xba\x92F?\x03'],
 286:[b'8D\x82\xba\x82F?\x03'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 8, 8

