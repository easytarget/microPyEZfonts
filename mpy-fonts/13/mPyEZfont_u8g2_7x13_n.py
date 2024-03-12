'''
    mPyEZfont_u8g2_7x13_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original 7x13.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "Public domain font.  Share and enjoy."

    Original Comments from source (may include copyright info):

    None found:
'''

# Code generated by font_to_py.py.
# Font: 7x13.bdf Char set:  *+,-./0123456789:
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/7x13.bdf 0 tmp_mPyEZfont_u8g2_7x13_n.py
version = '0.33'

def height():
    return 13

def baseline():
    return 11

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
    return 63

_font =\
b'\x07\x00\x00\x00\x78\x84\x84\x04\x08\x10\x10\x00\x10\x00\x00\x07'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'\
b'\x00\x00\x00\x00\x48\x30\xfc\x30\x48\x00\x00\x00\x00\x07\x00\x00'\
b'\x00\x00\x00\x10\x10\x7c\x10\x10\x00\x00\x00\x00\x07\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x38\x30\x40\x00\x07\x00\x00\x00\x00'\
b'\x00\x00\x00\x7c\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x10\x38\x10\x00\x07\x00\x00\x00\x04\x04\x08'\
b'\x08\x10\x20\x20\x40\x40\x00\x00\x07\x00\x00\x00\x30\x48\x84\x84'\
b'\x84\x84\x84\x48\x30\x00\x00\x07\x00\x00\x00\x10\x30\x50\x10\x10'\
b'\x10\x10\x10\x7c\x00\x00\x07\x00\x00\x00\x78\x84\x84\x04\x08\x30'\
b'\x40\x80\xfc\x00\x00\x07\x00\x00\x00\xfc\x04\x08\x10\x38\x04\x04'\
b'\x84\x78\x00\x00\x07\x00\x00\x00\x08\x18\x28\x48\x88\x88\xfc\x08'\
b'\x08\x00\x00\x07\x00\x00\x00\xfc\x80\x80\xb8\xc4\x04\x04\x84\x78'\
b'\x00\x00\x07\x00\x00\x00\x38\x40\x80\x80\xb8\xc4\x84\x84\x78\x00'\
b'\x00\x07\x00\x00\x00\xfc\x04\x08\x10\x10\x20\x20\x40\x40\x00\x00'\
b'\x07\x00\x00\x00\x78\x84\x84\x84\x78\x84\x84\x84\x78\x00\x00\x07'\
b'\x00\x00\x00\x78\x84\x84\x8c\x74\x04\x04\x08\x70\x00\x00\x07\x00'\
b'\x00\x00\x00\x00\x10\x38\x10\x00\x00\x10\x38\x10\x00'

_index =\
b'\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x1e\x00\x2d\x00\x3c\x00\x4b\x00\x5a\x00'\
b'\x69\x00\x78\x00\x87\x00\x96\x00\xa5\x00\xb4\x00\xc3\x00\xd2\x00'\
b'\xe1\x00\xf0\x00\xff\x00\x0e\x01\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1d\x01'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 63 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 13
    return _mvfont[doff + 2:next_offs], 13, width
 
