'''
    mPyEZfont_u8g2_6x12_n.py : generated as part of the microPyEZfonts repository
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
# Font: 6x12.bdf Char set:  %*+,-./0123456789:ø
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/6x12.bdf 0 tmp_mPyEZfont_u8g2_6x12_n.py
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
    return 248

_font =\
b'\x06\x00\x00\x00\x00\x70\x88\x10\x20\x20\x00\x20\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\xc8\xc8\x10\x20\x40\x98\x98\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x20\xa8\x70\x20\x70\xa8\x20\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x20\x20\xf8\x20\x20\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\xc0\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x08\x10\x10\x20\x40\x40\x80\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x30\x48\x48\x48\x48\x48\x30\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x20\x60\x20\x20\x20\x20\x70\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x70\x88\x08\x10\x20\x40\xf8\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\xf8\x08\x10\x30\x08\x88\x70\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x10\x30\x50\x90\xf8\x10\x10\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\xf8\x80\xf0\x08\x08\x88\x70\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x30\x40\x80\xf0\x88\x88\x70\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\xf8\x08\x10\x10\x20\x20\x20\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x70\x88\x88\x70\x88\x88\x70\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x70\x88\x88\x78\x08\x10\x60\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x60\x60\x00\x60\x60\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x70\x88\x10\x20\x20\x00\x20\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x78\x98\xa8\xc8\xf0\x00\x00'

_sparse =\
b'\x20\x00\x02\x00\x25\x00\x04\x00\x2a\x00\x06\x00\x2b\x00\x08\x00'\
b'\x2c\x00\x0a\x00\x2d\x00\x0c\x00\x2e\x00\x0e\x00\x2f\x00\x10\x00'\
b'\x30\x00\x12\x00\x31\x00\x14\x00\x32\x00\x16\x00\x33\x00\x18\x00'\
b'\x34\x00\x1a\x00\x35\x00\x1c\x00\x36\x00\x1e\x00\x37\x00\x20\x00'\
b'\x38\x00\x22\x00\x39\x00\x24\x00\x3a\x00\x26\x00\x3f\x00\x28\x00'\
b'\xf8\x00\x2a\x00'

_mvfont = memoryview(_font)
_mvsp = memoryview(_sparse)
ifb = lambda l : l[0] | (l[1] << 8)

def bs(lst, val):
    while True:
        m = (len(lst) & ~ 7) >> 1
        v = ifb(lst[m:])
        if v == val:
            return ifb(lst[m + 2:])
        if not m:
            return 0
        lst = lst[m:] if v < val else lst[:m]

def get_ch(ch):
    doff = bs(_mvsp, ord(ch)) << 3
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 12
    return _mvfont[doff + 2:next_offs], 12, width
 
