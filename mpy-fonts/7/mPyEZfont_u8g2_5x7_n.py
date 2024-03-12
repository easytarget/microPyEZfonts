'''
    mPyEZfont_u8g2_5x7_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original 5x7.bdf font file was sourced from the U8G2 project:
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
# Font: 5x7.bdf Char set:  *+,-./0123456789:
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/5x7.bdf 0 tmp_mPyEZfont_u8g2_5x7_n.py
version = '0.33'

def height():
    return 7

def baseline():
    return 6

def max_width():
    return 5

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
b'\x05\x00\x20\x50\x10\x20\x00\x20\x00\x05\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x05\x00\x00\x50\x20\x70\x20\x50\x00\x05\x00\x00\x20\x20'\
b'\xf8\x20\x20\x00\x05\x00\x00\x00\x00\x00\x30\x20\x40\x05\x00\x00'\
b'\x00\x00\xf0\x00\x00\x00\x05\x00\x00\x00\x00\x00\x60\x60\x00\x05'\
b'\x00\x00\x10\x20\x40\x80\x00\x00\x05\x00\x20\x50\x50\x50\x50\x20'\
b'\x00\x05\x00\x20\x60\x20\x20\x20\x70\x00\x05\x00\x60\x90\x10\x20'\
b'\x40\xf0\x00\x05\x00\xf0\x10\x60\x10\x90\x60\x00\x05\x00\x20\x60'\
b'\xa0\xf0\x20\x20\x00\x05\x00\xf0\x80\xe0\x10\x90\x60\x00\x05\x00'\
b'\x60\x80\xe0\x90\x90\x60\x00\x05\x00\xf0\x10\x20\x20\x40\x40\x00'\
b'\x05\x00\x60\x90\x60\x90\x90\x60\x00\x05\x00\x60\x90\x90\x70\x10'\
b'\x60\x00\x05\x00\x00\x60\x60\x00\x60\x60\x00'

_index =\
b'\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x12\x00\x1b\x00\x24\x00\x2d\x00\x36\x00'\
b'\x3f\x00\x48\x00\x51\x00\x5a\x00\x63\x00\x6c\x00\x75\x00\x7e\x00'\
b'\x87\x00\x90\x00\x99\x00\xa2\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xab\x00'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 63 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 7
    return _mvfont[doff + 2:next_offs], 7, width
 
