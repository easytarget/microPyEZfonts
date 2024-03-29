'''
    mPyEZfont_u8g2_10x20_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original 10x20.bdf font file was sourced from the U8G2 project:
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
# Font: 10x20.bdf Char set:  *+,-./0123456789:
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/10x20.bdf 0 tmp_mPyEZfont_u8g2_10x20_n.py
version = '0.33'

def height():
    return 20

def baseline():
    return 16

def max_width():
    return 10

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
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x33\x00\x61\x80\x61\x80'\
b'\x61\x80\x03\x00\x06\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x0c\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x33\x00\x33\x00\x1e\x00\x7f\x80\x1e\x00\x33\x00\x33\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x7f\x80\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x1c\x00\x00\x00\x00\x00'\
b'\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x0e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x01\x80\x01\x80\x03\x00\x03\x00\x06\x00\x06\x00\x0c\x00\x0c\x00'\
b'\x18\x00\x18\x00\x30\x00\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1e\x00\x33\x00\x33\x00'\
b'\x61\x80\x61\x80\x61\x80\x61\x80\x61\x80\x33\x00\x33\x00\x1e\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x1c\x00\x3c\x00\x6c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x33\x00'\
b'\x61\x80\x61\x80\x01\x80\x01\x80\x03\x00\x0e\x00\x18\x00\x30\x00'\
b'\x60\x00\x60\x00\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00'\
b'\x00\x00\x00\x00\x00\x00\x1e\x00\x33\x00\x61\x80\x61\x80\x01\x80'\
b'\x03\x00\x0e\x00\x03\x00\x01\x80\x61\x80\x61\x80\x33\x00\x1e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00'\
b'\x01\x00\x03\x00\x07\x00\x0f\x00\x1b\x00\x33\x00\x63\x00\x63\x00'\
b'\x7f\x80\x03\x00\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x6e\x00\x73\x00\x01\x80\x01\x80\x01\x80\x61\x80'\
b'\x33\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00'\
b'\x00\x00\x00\x00\x1e\x00\x33\x00\x61\x00\x60\x00\x60\x00\x6e\x00'\
b'\x73\x00\x61\x80\x61\x80\x61\x80\x61\x80\x33\x00\x1e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x7f\x80'\
b'\x01\x80\x01\x80\x03\x00\x03\x00\x06\x00\x06\x00\x0c\x00\x0c\x00'\
b'\x18\x00\x18\x00\x30\x00\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x33\x00\x61\x80\x61\x80'\
b'\x61\x80\x33\x00\x1e\x00\x33\x00\x61\x80\x61\x80\x61\x80\x33\x00'\
b'\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00'\
b'\x00\x00\x1e\x00\x33\x00\x61\x80\x61\x80\x61\x80\x61\x80\x33\x80'\
b'\x1d\x80\x01\x80\x01\x80\x21\x80\x33\x00\x1e\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00'

_index =\
b'\x00\x00\x2a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x54\x00\x7e\x00\xa8\x00\xd2\x00\xfc\x00'\
b'\x26\x01\x50\x01\x7a\x01\xa4\x01\xce\x01\xf8\x01\x22\x02\x4c\x02'\
b'\x76\x02\xa0\x02\xca\x02\xf4\x02\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1e\x03'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 63 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 20
    return _mvfont[doff + 2:next_offs], 20, width
 
