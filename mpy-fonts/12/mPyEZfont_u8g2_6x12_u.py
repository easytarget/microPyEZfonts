'''
    mPyEZfont_u8g2_6x12_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original 6x12.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "Public domain terminal emulator font.  Share and enjoy."

    Original Comments from source (may include copyright info):

    None found:
'''

# Code generated by font_to_py.py.
# Font: 6x12.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/u-char.set u8g2/tools/font/bdf/6x12.bdf 0 tmp_mPyEZfont_u8g2_6x12_u.py
version = '0.33'

def height():
    return 12

def baseline():
    return 10

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
b'\x06\x00\x00\x00\x00\x70\x88\x10\x20\x20\x00\x20\x00\x00\x06\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00'\
b'\x00\x20\x20\x20\x20\x20\x00\x20\x00\x00\x06\x00\x00\x00\x50\x50'\
b'\x50\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x50\xf8'\
b'\x50\x50\xf8\x50\x00\x00\x06\x00\x00\x00\x20\x70\xa8\xa0\x70\x28'\
b'\xa8\x70\x20\x00\x06\x00\x00\x00\x00\xc8\xc8\x10\x20\x40\x98\x98'\
b'\x00\x00\x06\x00\x00\x00\x00\x40\xa0\xa0\x40\xa8\x90\x68\x00\x00'\
b'\x06\x00\x00\x00\x20\x20\x20\x00\x00\x00\x00\x00\x00\x00\x06\x00'\
b'\x00\x00\x10\x20\x20\x40\x40\x40\x20\x20\x10\x00\x06\x00\x00\x00'\
b'\x40\x20\x20\x10\x10\x10\x20\x20\x40\x00\x06\x00\x00\x00\x00\x20'\
b'\xa8\x70\x20\x70\xa8\x20\x00\x00\x06\x00\x00\x00\x00\x00\x20\x20'\
b'\xf8\x20\x20\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x60\x60\xc0\x00\x06\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00'\
b'\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x00\x00'\
b'\x06\x00\x00\x00\x00\x08\x10\x10\x20\x40\x40\x80\x00\x00\x06\x00'\
b'\x00\x00\x00\x30\x48\x48\x48\x48\x48\x30\x00\x00\x06\x00\x00\x00'\
b'\x00\x20\x60\x20\x20\x20\x20\x70\x00\x00\x06\x00\x00\x00\x00\x70'\
b'\x88\x08\x10\x20\x40\xf8\x00\x00\x06\x00\x00\x00\x00\xf8\x08\x10'\
b'\x30\x08\x88\x70\x00\x00\x06\x00\x00\x00\x00\x10\x30\x50\x90\xf8'\
b'\x10\x10\x00\x00\x06\x00\x00\x00\x00\xf8\x80\xf0\x08\x08\x88\x70'\
b'\x00\x00\x06\x00\x00\x00\x00\x30\x40\x80\xf0\x88\x88\x70\x00\x00'\
b'\x06\x00\x00\x00\x00\xf8\x08\x10\x10\x20\x20\x20\x00\x00\x06\x00'\
b'\x00\x00\x00\x70\x88\x88\x70\x88\x88\x70\x00\x00\x06\x00\x00\x00'\
b'\x00\x70\x88\x88\x78\x08\x10\x60\x00\x00\x06\x00\x00\x00\x00\x00'\
b'\x00\x60\x60\x00\x60\x60\x00\x00\x06\x00\x00\x00\x00\x00\x00\x60'\
b'\x60\x00\x60\x60\xc0\x00\x06\x00\x00\x00\x00\x00\x10\x20\x40\x20'\
b'\x10\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\x00'\
b'\x00\x00\x06\x00\x00\x00\x00\x00\x40\x20\x10\x20\x40\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x70\x88\x10\x20\x20\x00\x20\x00\x00\x06\x00'\
b'\x00\x00\x00\x70\x88\xb8\xa8\xb8\x80\x70\x00\x00\x06\x00\x00\x00'\
b'\x00\x70\x88\x88\xf8\x88\x88\x88\x00\x00\x06\x00\x00\x00\x00\xf0'\
b'\x48\x48\x70\x48\x48\xf0\x00\x00\x06\x00\x00\x00\x00\x70\x88\x80'\
b'\x80\x80\x88\x70\x00\x00\x06\x00\x00\x00\x00\xf0\x48\x48\x48\x48'\
b'\x48\xf0\x00\x00\x06\x00\x00\x00\x00\xf8\x80\x80\xf0\x80\x80\xf8'\
b'\x00\x00\x06\x00\x00\x00\x00\xf8\x80\x80\xf0\x80\x80\x80\x00\x00'\
b'\x06\x00\x00\x00\x00\x70\x88\x80\x80\x98\x88\x70\x00\x00\x06\x00'\
b'\x00\x00\x00\x88\x88\x88\xf8\x88\x88\x88\x00\x00\x06\x00\x00\x00'\
b'\x00\x70\x20\x20\x20\x20\x20\x70\x00\x00\x06\x00\x00\x00\x00\x38'\
b'\x10\x10\x10\x10\x90\x60\x00\x00\x06\x00\x00\x00\x00\x88\x90\xa0'\
b'\xc0\xa0\x90\x88\x00\x00\x06\x00\x00\x00\x00\x80\x80\x80\x80\x80'\
b'\x80\xf8\x00\x00\x06\x00\x00\x00\x00\x88\xd8\xa8\x88\x88\x88\x88'\
b'\x00\x00\x06\x00\x00\x00\x00\x88\x88\xc8\xa8\x98\x88\x88\x00\x00'\
b'\x06\x00\x00\x00\x00\x70\x88\x88\x88\x88\x88\x70\x00\x00\x06\x00'\
b'\x00\x00\x00\xf0\x88\x88\xf0\x80\x80\x80\x00\x00\x06\x00\x00\x00'\
b'\x00\x70\x88\x88\x88\xa8\x90\x68\x00\x00\x06\x00\x00\x00\x00\xf0'\
b'\x88\x88\xf0\xa0\x90\x88\x00\x00\x06\x00\x00\x00\x00\x70\x88\x80'\
b'\x70\x08\x88\x70\x00\x00\x06\x00\x00\x00\x00\xf8\x20\x20\x20\x20'\
b'\x20\x20\x00\x00\x06\x00\x00\x00\x00\x88\x88\x88\x88\x88\x88\x70'\
b'\x00\x00\x06\x00\x00\x00\x00\x88\x88\x88\x88\x50\x50\x20\x00\x00'\
b'\x06\x00\x00\x00\x00\x88\x88\x88\x88\xa8\xa8\x50\x00\x00\x06\x00'\
b'\x00\x00\x00\x88\x88\x50\x20\x50\x88\x88\x00\x00\x06\x00\x00\x00'\
b'\x00\x88\x88\x50\x20\x20\x20\x20\x00\x00\x06\x00\x00\x00\x00\xf8'\
b'\x08\x10\x20\x40\x80\xf8\x00\x00\x06\x00\x00\x00\x70\x40\x40\x40'\
b'\x40\x40\x40\x40\x70\x00\x06\x00\x00\x00\x00\x80\x40\x40\x20\x10'\
b'\x10\x08\x00\x00\x06\x00\x00\x00\x70\x10\x10\x10\x10\x10\x10\x10'\
b'\x70\x00\x06\x00\x00\x00\x20\x50\x88\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8'

_index =\
b'\x00\x00\x0e\x00\x1c\x00\x2a\x00\x38\x00\x46\x00\x54\x00\x62\x00'\
b'\x70\x00\x7e\x00\x8c\x00\x9a\x00\xa8\x00\xb6\x00\xc4\x00\xd2\x00'\
b'\xe0\x00\xee\x00\xfc\x00\x0a\x01\x18\x01\x26\x01\x34\x01\x42\x01'\
b'\x50\x01\x5e\x01\x6c\x01\x7a\x01\x88\x01\x96\x01\xa4\x01\xb2\x01'\
b'\xc0\x01\xce\x01\xdc\x01\xea\x01\xf8\x01\x06\x02\x14\x02\x22\x02'\
b'\x30\x02\x3e\x02\x4c\x02\x5a\x02\x68\x02\x76\x02\x84\x02\x92\x02'\
b'\xa0\x02\xae\x02\xbc\x02\xca\x02\xd8\x02\xe6\x02\xf4\x02\x02\x03'\
b'\x10\x03\x1e\x03\x2c\x03\x3a\x03\x48\x03\x56\x03\x64\x03\x72\x03'\
b'\x80\x03\x8e\x03'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 12
    return _mvfont[doff + 2:next_offs], 12, width
 
