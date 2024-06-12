'''
    ezFBfont_05_tom_thumb_upper : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original tom_thumb.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT """""MIT"""""

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: tom_thumb
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/tom-thumb.bdf', '_', './upper-char.set']
# Date: 2024-06-12 20:09:36

version = '0.33'
name = '-Raccoon-Fixed4x6-Medium-R-Normal--6-60-75-75-P-40-ISO10646-1'
family = 'fixed4x6'
weight = 'medium'
size = 6

def height():
    return 5

def baseline():
    return 5

def max_width():
    return 4

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 95

_g = {
 32:[b'\x00\x00\x00\x00\x00'],
 33:[b'\x80\x80\x80\x00\x80'],
 34:[b'\xa0\xa0\x00\x00\x00'],
 35:[b'\xa0\xe0\xa0\xe0\xa0'],
 36:[b'`\xc0`\xc0@'],
 37:[b'\x80 @\x80 '],
 38:[b'\xc0\xc0\xe0\xa0`'],
 39:[b'\x80\x80\x00\x00\x00'],
 40:[b'@\x80\x80\x80@'],
 41:[b'\x80@@@\x80'],
 42:[b'\xa0@\xa0\x00\x00'],
 43:[b'\x00@\xe0@\x00'],
 44:[b'\x00\x00\x00@\x80'],
 45:[b'\x00\x00\xe0\x00\x00'],
 46:[b'\x00\x00\x00\x00\x80'],
 47:[b'  @\x80\x80'],
 48:[b'`\xa0\xa0\xa0\xc0'],
 49:[b'@\xc0@@@'],
 50:[b'\xc0 @\x80\xe0'],
 51:[b'\xc0 @ \xc0'],
 52:[b'\xa0\xa0\xe0  '],
 53:[b'\xe0\x80\xc0 \xc0'],
 54:[b'`\x80\xe0\xa0\xe0'],
 55:[b'\xe0 @\x80\x80'],
 56:[b'\xe0\xa0\xe0\xa0\xe0'],
 57:[b'\xe0\xa0\xe0 \xc0'],
 58:[b'\x00\x80\x00\x80\x00'],
 59:[b'\x00@\x00@\x80'],
 60:[b' @\x80@ '],
 61:[b'\x00\xe0\x00\xe0\x00'],
 62:[b'\x80@ @\x80'],
 63:[b'\xe0 @\x00@'],
 64:[b'@\xa0\xe0\x80`'],
 65:[b'@\xa0\xe0\xa0\xa0'],
 66:[b'\xc0\xa0\xc0\xa0\xc0'],
 67:[b'`\x80\x80\x80`'],
 68:[b'\xc0\xa0\xa0\xa0\xc0'],
 69:[b'\xe0\x80\xe0\x80\xe0'],
 70:[b'\xe0\x80\xe0\x80\x80'],
 71:[b'`\x80\xe0\xa0`'],
 72:[b'\xa0\xa0\xe0\xa0\xa0'],
 73:[b'\xe0@@@\xe0'],
 74:[b'   \xa0@'],
 75:[b'\xa0\xa0\xc0\xa0\xa0'],
 76:[b'\x80\x80\x80\x80\xe0'],
 77:[b'\xa0\xe0\xe0\xa0\xa0'],
 78:[b'\xa0\xe0\xe0\xe0\xa0'],
 79:[b'@\xa0\xa0\xa0@'],
 80:[b'\xc0\xa0\xc0\x80\x80'],
 81:[b'@\xa0\xa0\xe0`'],
 82:[b'\xc0\xa0\xe0\xc0\xa0'],
 83:[b'`\x80@ \xc0'],
 84:[b'\xe0@@@@'],
 85:[b'\xa0\xa0\xa0\xa0`'],
 86:[b'\xa0\xa0\xa0@@'],
 87:[b'\xa0\xa0\xe0\xe0\xa0'],
 88:[b'\xa0\xa0@\xa0\xa0'],
 89:[b'\xa0\xa0@@@'],
 90:[b'\xe0 @\x80\xe0'],
 91:[b'\xe0\x80\x80\x80\xe0'],
 92:[b'\x00\x80@ \x00'],
 93:[b'\xe0   \xe0'],
 94:[b'@\xa0\x00\x00\x00'],
 95:[b'\x00\x00\x00\x00\xe0'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 5, 4

