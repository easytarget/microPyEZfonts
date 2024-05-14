'''
    mPyEZfont_u8g2_font_tiny5_t.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original font_tiny5.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "(CC) Gissio 2022-2023 Creative Commons Zero v1.0 Universal"

    Original Comments from source (may include copyright info):

    COMMENT Exported by Fony v1.4.7
'''

# Code generated by font_to_py.py.
# Font: font_tiny5.bdf Char set:  +-.0123456789:
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./t-char.set -e 32 ../u8g2/tools/font/bdf/font_tiny5.bdf 0 tmp_mPyEZfont_u8g2_font_tiny5_t.py
version = '0.33'

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
    return False

def min_ch():
    return 32

def max_ch():
    return 58

_font =\
b'\x02\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x04\x00'\
b'\x00\x40\xe0\x40\x00\x04\x00\x00\x00\xe0\x00\x00\x02\x00\x00\x00'\
b'\x00\x00\x80\x04\x00\x40\xa0\xa0\xa0\x40\x04\x00\x40\xc0\x40\x40'\
b'\x40\x04\x00\xc0\x20\x40\x80\xe0\x04\x00\xc0\x20\x40\x20\xc0\x04'\
b'\x00\x20\x60\xa0\xe0\x20\x04\x00\xe0\x80\xc0\x20\xc0\x04\x00\x60'\
b'\x80\xc0\xa0\x40\x04\x00\xe0\x20\x40\x40\x40\x04\x00\x40\xa0\x40'\
b'\xa0\x40\x04\x00\x40\xa0\x60\x20\xc0\x02\x00\x00\x80\x00\x00\x80'\

_index =\
b'\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x15\x00\x1c\x00'\
b'\x00\x00\x23\x00\x2a\x00\x31\x00\x38\x00\x3f\x00\x46\x00\x4d\x00'\
b'\x54\x00\x5b\x00\x62\x00\x69\x00\x70\x00'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 58 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 5
    return _mvfont[doff + 2:next_offs], 5, width
 
