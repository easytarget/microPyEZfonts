'''
    mPyEZfont_u8g2_6x13_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original 6x13.bdf font file was sourced from the U8G2 project:
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
# Font: 6x13.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/u-char.set u8g2/tools/font/bdf/6x13.bdf 0 tmp_mPyEZfont_u8g2_6x13_u.py
version = '0.33'

def height():
    return 13

def baseline():
    return 11

def max_width():
    return 6

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 95

_font =\
b'\x06\x00\x00\x00\x70\x88\x88\x08\x10\x20\x20\x00\x20\x00\x00\x06'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'\
b'\x00\x00\x20\x20\x20\x20\x20\x20\x20\x00\x20\x00\x00\x06\x00\x00'\
b'\x00\x50\x50\x50\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00'\
b'\x00\x50\x50\xf8\x50\xf8\x50\x50\x00\x00\x00\x06\x00\x00\x00\x20'\
b'\x78\xa0\xa0\x70\x28\x28\xf0\x20\x00\x00\x06\x00\x00\x00\x48\xa8'\
b'\x50\x10\x20\x40\x50\xa8\x90\x00\x00\x06\x00\x00\x00\x00\x40\xa0'\
b'\xa0\x40\xa0\x98\x90\x68\x00\x00\x06\x00\x00\x00\x20\x20\x20\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x10\x20\x20\x40\x40\x40'\
b'\x40\x40\x20\x20\x10\x00\x06\x00\x00\x40\x20\x20\x10\x10\x10\x10'\
b'\x10\x20\x20\x40\x00\x06\x00\x00\x00\x20\xa8\x70\xa8\x20\x00\x00'\
b'\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x20\x20\xf8\x20\x20\x00'\
b'\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30\x20'\
b'\x40\x00\x06\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00\x00'\
b'\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x70\x20\x00'\
b'\x06\x00\x00\x00\x08\x08\x10\x10\x20\x40\x40\x80\x80\x00\x00\x06'\
b'\x00\x00\x00\x20\x50\x88\x88\x88\x88\x88\x50\x20\x00\x00\x06\x00'\
b'\x00\x00\x20\x60\xa0\x20\x20\x20\x20\x20\xf8\x00\x00\x06\x00\x00'\
b'\x00\x70\x88\x88\x08\x10\x20\x40\x80\xf8\x00\x00\x06\x00\x00\x00'\
b'\xf8\x08\x10\x20\x70\x08\x08\x88\x70\x00\x00\x06\x00\x00\x00\x10'\
b'\x10\x30\x50\x50\x90\xf8\x10\x10\x00\x00\x06\x00\x00\x00\xf8\x80'\
b'\x80\xb0\xc8\x08\x08\x88\x70\x00\x00\x06\x00\x00\x00\x70\x88\x80'\
b'\x80\xf0\x88\x88\x88\x70\x00\x00\x06\x00\x00\x00\xf8\x08\x10\x10'\
b'\x20\x20\x40\x40\x40\x00\x00\x06\x00\x00\x00\x70\x88\x88\x88\x70'\
b'\x88\x88\x88\x70\x00\x00\x06\x00\x00\x00\x70\x88\x88\x88\x78\x08'\
b'\x08\x88\x70\x00\x00\x06\x00\x00\x00\x00\x00\x20\x70\x20\x00\x00'\
b'\x20\x70\x20\x00\x06\x00\x00\x00\x00\x00\x20\x70\x20\x00\x00\x30'\
b'\x20\x40\x00\x06\x00\x00\x00\x08\x10\x20\x40\x80\x40\x20\x10\x08'\
b'\x00\x00\x06\x00\x00\x00\x00\x00\x00\xf8\x00\x00\xf8\x00\x00\x00'\
b'\x00\x06\x00\x00\x00\x80\x40\x20\x10\x08\x10\x20\x40\x80\x00\x00'\
b'\x06\x00\x00\x00\x70\x88\x88\x08\x10\x20\x20\x00\x20\x00\x00\x06'\
b'\x00\x00\x00\x70\x88\x88\x98\xa8\xa8\xb0\x80\x78\x00\x00\x06\x00'\
b'\x00\x00\x20\x50\x88\x88\x88\xf8\x88\x88\x88\x00\x00\x06\x00\x00'\
b'\x00\xf0\x48\x48\x48\x70\x48\x48\x48\xf0\x00\x00\x06\x00\x00\x00'\
b'\x70\x88\x80\x80\x80\x80\x80\x88\x70\x00\x00\x06\x00\x00\x00\xf0'\
b'\x48\x48\x48\x48\x48\x48\x48\xf0\x00\x00\x06\x00\x00\x00\xf8\x80'\
b'\x80\x80\xf0\x80\x80\x80\xf8\x00\x00\x06\x00\x00\x00\xf8\x80\x80'\
b'\x80\xf0\x80\x80\x80\x80\x00\x00\x06\x00\x00\x00\x70\x88\x80\x80'\
b'\x80\x98\x88\x88\x70\x00\x00\x06\x00\x00\x00\x88\x88\x88\x88\xf8'\
b'\x88\x88\x88\x88\x00\x00\x06\x00\x00\x00\x70\x20\x20\x20\x20\x20'\
b'\x20\x20\x70\x00\x00\x06\x00\x00\x00\x38\x10\x10\x10\x10\x10\x10'\
b'\x90\x60\x00\x00\x06\x00\x00\x00\x88\x88\x90\xa0\xc0\xa0\x90\x88'\
b'\x88\x00\x00\x06\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x80\xf8'\
b'\x00\x00\x06\x00\x00\x00\x88\x88\xd8\xa8\xa8\x88\x88\x88\x88\x00'\
b'\x00\x06\x00\x00\x00\x88\xc8\xc8\xa8\xa8\x98\x98\x88\x88\x00\x00'\
b'\x06\x00\x00\x00\x70\x88\x88\x88\x88\x88\x88\x88\x70\x00\x00\x06'\
b'\x00\x00\x00\xf0\x88\x88\x88\xf0\x80\x80\x80\x80\x00\x00\x06\x00'\
b'\x00\x00\x70\x88\x88\x88\x88\x88\x88\xa8\x70\x08\x00\x06\x00\x00'\
b'\x00\xf0\x88\x88\x88\xf0\xa0\x90\x88\x88\x00\x00\x06\x00\x00\x00'\
b'\x70\x88\x80\x80\x70\x08\x08\x88\x70\x00\x00\x06\x00\x00\x00\xf8'\
b'\x20\x20\x20\x20\x20\x20\x20\x20\x00\x00\x06\x00\x00\x00\x88\x88'\
b'\x88\x88\x88\x88\x88\x88\x70\x00\x00\x06\x00\x00\x00\x88\x88\x88'\
b'\x88\x50\x50\x50\x20\x20\x00\x00\x06\x00\x00\x00\x88\x88\x88\x88'\
b'\xa8\xa8\xa8\xa8\x50\x00\x00\x06\x00\x00\x00\x88\x88\x50\x50\x20'\
b'\x50\x50\x88\x88\x00\x00\x06\x00\x00\x00\x88\x88\x50\x50\x20\x20'\
b'\x20\x20\x20\x00\x00\x06\x00\x00\x00\xf8\x08\x10\x10\x20\x40\x40'\
b'\x80\xf8\x00\x00\x06\x00\x00\x70\x40\x40\x40\x40\x40\x40\x40\x40'\
b'\x40\x70\x00\x06\x00\x00\x00\x80\x80\x40\x40\x20\x10\x10\x08\x08'\
b'\x00\x00\x06\x00\x00\x70\x10\x10\x10\x10\x10\x10\x10\x10\x10\x70'\
b'\x00\x06\x00\x00\x00\x20\x50\x88\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00'

_index =\
b'\x00\x00\x0f\x00\x1e\x00\x2d\x00\x3c\x00\x4b\x00\x5a\x00\x69\x00'\
b'\x78\x00\x87\x00\x96\x00\xa5\x00\xb4\x00\xc3\x00\xd2\x00\xe1\x00'\
b'\xf0\x00\xff\x00\x0e\x01\x1d\x01\x2c\x01\x3b\x01\x4a\x01\x59\x01'\
b'\x68\x01\x77\x01\x86\x01\x95\x01\xa4\x01\xb3\x01\xc2\x01\xd1\x01'\
b'\xe0\x01\xef\x01\xfe\x01\x0d\x02\x1c\x02\x2b\x02\x3a\x02\x49\x02'\
b'\x58\x02\x67\x02\x76\x02\x85\x02\x94\x02\xa3\x02\xb2\x02\xc1\x02'\
b'\xd0\x02\xdf\x02\xee\x02\xfd\x02\x0c\x03\x1b\x03\x2a\x03\x39\x03'\
b'\x48\x03\x57\x03\x66\x03\x75\x03\x84\x03\x93\x03\xa2\x03\xb1\x03'\
b'\xc0\x03\xcf\x03'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 13
    return _mvfont[doff + 2:next_offs], 13, width
 
