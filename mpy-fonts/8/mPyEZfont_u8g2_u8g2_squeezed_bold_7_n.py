'''
    mPyEZfont_u8g2_u8g2_squeezed_bold_7_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original u8g2_squeezed_bold_7.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "public domain"

    Original Comments from source (may include copyright info):

    COMMENT Exported by Fony v1.4.7
'''

# Code generated by font_to_py.py.
# Font: u8g2_squeezed_bold_7.bdf Char set:  %()*+,-./0123456789:°
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./n-char.set -e 32 ../u8g2/tools/font/bdf/u8g2_squeezed_bold_7.bdf 0 tmp_mPyEZfont_u8g2_u8g2_squeezed_bold_7_n.py
version = '0.33'

def height():
    return 8

def baseline():
    return 7

def max_width():
    return 7

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 58

_font =\
b'\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x07\x00\xcc\xd8\x18\x30\x60\x6c\xcc\x00\x04\x00'\
b'\x60\xc0\xc0\xc0\xc0\xc0\x60\x00\x04\x00\xc0\x60\x60\x60\x60\x60'\
b'\xc0\x00\x06\x00\x00\xd8\x70\xf8\x70\xd8\x00\x00\x05\x00\x00\x00'\
b'\x60\xf0\x60\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xc0\xc0'\
b'\x04\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00'\
b'\x00\xc0\xc0\x00\x05\x00\x30\x30\x60\x60\x60\xc0\xc0\x00\x05\x00'\
b'\x70\xd8\xd8\xd8\xd8\xd8\x70\x00\x04\x00\x60\xe0\x60\x60\x60\x60'\
b'\x60\x00\x05\x00\xe0\x30\x30\x60\xc0\xc0\xf0\x00\x05\x00\xe0\x30'\
b'\x30\xe0\x30\x30\xe0\x00\x06\x00\xd8\xd8\xd8\xf8\x18\x18\x18\x00'\
b'\x05\x00\xf0\xc0\xe0\x30\x30\x30\xe0\x00\x06\x00\x70\xc0\xc0\xf0'\
b'\xd8\xd8\x70\x00\x05\x00\xf0\x30\x30\x60\x60\x60\x60\x00\x06\x00'\
b'\x70\xd8\xd8\x70\xd8\xd8\x70\x00\x06\x00\x70\xd8\xd8\x78\x18\xd8'\
b'\x70\x00\x03\x00\x00\x00\xc0\x00\x00\xc0\x00\x00'

_index =\
b'\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00'\
b'\x00\x00\x1e\x00\x28\x00\x32\x00\x3c\x00\x46\x00\x50\x00\x5a\x00'\
b'\x64\x00\x6e\x00\x78\x00\x82\x00\x8c\x00\x96\x00\xa0\x00\xaa\x00'\
b'\xb4\x00\xbe\x00\xc8\x00\xd2\x00\xdc\x00'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 58 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 8
    return _mvfont[doff + 2:next_offs], 8, width
 
