'''
    mPyEZfont_u8g2_u8glib_4_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original u8glib_4.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "public domain"

    Original Comments from source (may include copyright info):

    COMMENT Exported by Fony v1.4.6
'''

# Code generated by font_to_py.py.
# Font: u8glib_4.bdf Char set:  %()*+,-./0123456789:°
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./n-char.set -e 32 ../u8g2/tools/font/bdf/u8glib_4.bdf 0 tmp_mPyEZfont_u8g2_u8glib_4_n.py
version = '0.33'

def height():
    return 6

def baseline():
    return 5

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
    return 176

_font =\
b'\x02\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x90\x20\x40\x90\x00\x03\x00\x40\x80\x80\x80\x80\x40'\
b'\x03\x00\x80\x40\x40\x40\x40\x80\x03\x00\x00\x00\xc0\xc0\x00\x00'\
b'\x04\x00\x00\x00\x40\xe0\x40\x00\x02\x00\x00\x00\x00\x00\x80\x80'\
b'\x04\x00\x00\x00\x00\xe0\x00\x00\x02\x00\x00\x00\x00\x00\x80\x00'\
b'\x05\x00\x00\x10\x20\x40\x80\x00\x04\x00\x00\xe0\xa0\xa0\xe0\x00'\
b'\x03\x00\x00\x40\xc0\x40\x40\x00\x04\x00\x00\xe0\x20\x40\xe0\x00'\
b'\x04\x00\x00\xe0\x40\x20\xe0\x00\x04\x00\x00\x80\xa0\xe0\x20\x00'\
b'\x04\x00\x00\xe0\xc0\x20\xe0\x00\x04\x00\x00\xe0\x80\xe0\xe0\x00'\
b'\x04\x00\x00\xe0\x20\x40\x80\x00\x04\x00\x00\xe0\xe0\xa0\xe0\x00'\
b'\x04\x00\x00\xe0\xe0\x20\xe0\x00\x02\x00\x00\x00\x80\x00\x80\x00'\
b'\x04\x00\xe0\xa0\xe0\x00\x00\x00'

_sparse =\
b'\x20\x00\x01\x00\x25\x00\x02\x00\x28\x00\x03\x00\x29\x00\x04\x00'\
b'\x2a\x00\x05\x00\x2b\x00\x06\x00\x2c\x00\x07\x00\x2d\x00\x08\x00'\
b'\x2e\x00\x09\x00\x2f\x00\x0a\x00\x30\x00\x0b\x00\x31\x00\x0c\x00'\
b'\x32\x00\x0d\x00\x33\x00\x0e\x00\x34\x00\x0f\x00\x35\x00\x10\x00'\
b'\x36\x00\x11\x00\x37\x00\x12\x00\x38\x00\x13\x00\x39\x00\x14\x00'\
b'\x3a\x00\x15\x00\xb0\x00\x16\x00'

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

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 6
    return _mvfont[doff + 2:next_offs], 6, width
 