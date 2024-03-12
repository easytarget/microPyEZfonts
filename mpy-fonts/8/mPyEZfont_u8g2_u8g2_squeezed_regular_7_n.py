'''
    mPyEZfont_u8g2_u8g2_squeezed_regular_7_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original u8g2_squeezed_regular_7.bdf font file was sourced from the U8G2 project:
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
# Font: u8g2_squeezed_regular_7.bdf Char set:  *+,-./0123456789:
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/u8g2_squeezed_regular_7.bdf 0 tmp_mPyEZfont_u8g2_u8g2_squeezed_regular_7_n.py
version = '0.33'

def height():
    return 8

def baseline():
    return 7

def max_width():
    return 4

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 63

_font =\
b'\x03\x00\x80\x40\x40\x80\x80\x00\x80\x00\x02\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x04\x00\x00\xa0\x40\xe0\x40\xa0\x00\x00\x04\x00'\
b'\x00\x00\x40\xe0\x40\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00'\
b'\x80\x80\x03\x00\x00\x00\x00\xc0\x00\x00\x00\x00\x02\x00\x00\x00'\
b'\x00\x00\x00\x00\x80\x00\x04\x00\x20\x20\x40\x40\x40\x80\x80\x00'\
b'\x04\x00\x40\xa0\xa0\xa0\xa0\xa0\x40\x00\x03\x00\x40\xc0\x40\x40'\
b'\x40\x40\x40\x00\x03\x00\x80\x40\x40\x40\x80\x80\xc0\x00\x03\x00'\
b'\xc0\x40\x40\x80\x40\x40\x80\x00\x04\x00\xa0\xa0\xa0\xe0\x20\x20'\
b'\x20\x00\x03\x00\xc0\x80\x80\x40\x40\x40\x80\x00\x04\x00\x40\x80'\
b'\x80\xc0\xa0\xa0\x40\x00\x04\x00\xe0\x20\x20\x40\x40\x40\x40\x00'\
b'\x04\x00\x40\xa0\xa0\x40\xa0\xa0\x40\x00\x04\x00\x40\xa0\xa0\x60'\
b'\x20\x20\x40\x00\x02\x00\x00\x00\x80\x00\x00\x80\x00\x00'

_index =\
b'\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x14\x00\x1e\x00\x28\x00\x32\x00\x3c\x00'\
b'\x46\x00\x50\x00\x5a\x00\x64\x00\x6e\x00\x78\x00\x82\x00\x8c\x00'\
b'\x96\x00\xa0\x00\xaa\x00\xb4\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xbe\x00'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 63 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 8
    return _mvfont[doff + 2:next_offs], 8, width
 
