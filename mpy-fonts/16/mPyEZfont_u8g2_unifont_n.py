'''
    mPyEZfont_u8g2_unifont_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original unifont.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "Copyright (C) 1998-2019 Roman Czyborra, Paul Hardy,  Qianqian Fang, Andrew Miller, Johnnie Weaver, David Corbett, et al.  License GPLv2+: GNU GPL version 2 or later <http://gnu.org/licenses/gpl.html>  with the GNU Font Embedding Exception."

    Original Comments from source (may include copyright info):

    None found:
'''

# Code generated by font_to_py.py.
# Font: unifont.bdf Char set:  %()*+,-./0123456789:°
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./n-char.set -e 32 ../u8g2/tools/font/bdf/unifont.bdf 0 tmp_mPyEZfont_u8g2_unifont_n.py
version = '0.33'

def height():
    return 16

def baseline():
    return 14

def max_width():
    return 8

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
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x31\x4a\x4a\x34\x08\x08\x16\x29\x29\x46'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x04\x08\x08'\
b'\x10\x10\x10\x10\x10\x10\x08\x08\x04\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x20\x10\x10\x08\x08\x08\x08\x08\x08\x10\x10'\
b'\x20\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x49\x2a\x1c\x2a\x49\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x08\x08\x08\x7f\x08\x08\x08\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x18\x08\x08\x10\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x02\x02\x04\x08\x08\x10\x10\x20\x40\x40'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x18\x24'\
b'\x42\x46\x4a\x52\x62\x42\x24\x18\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x08\x18\x28\x08\x08\x08\x08\x08\x08\x3e'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x3c\x42'\
b'\x42\x02\x0c\x10\x20\x40\x40\x7e\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x3c\x42\x42\x02\x1c\x02\x02\x42\x42\x3c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x04\x0c'\
b'\x14\x24\x44\x44\x7e\x04\x04\x04\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x7e\x40\x40\x40\x7c\x02\x02\x02\x42\x3c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x1c\x20'\
b'\x40\x40\x7c\x42\x42\x42\x42\x3c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x7e\x02\x02\x04\x04\x04\x08\x08\x08\x08'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x3c\x42'\
b'\x42\x42\x3c\x42\x42\x42\x42\x3c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x3c\x42\x42\x42\x3e\x02\x02\x02\x04\x38'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x18\x18\x00\x00\x00\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x18\x24\x24\x18\x00\x00\x00\x00\x00\x00'\
b'\x00\x00'

_sparse =\
b'\x20\x00\x03\x00\x25\x00\x06\x00\x28\x00\x09\x00\x29\x00\x0c\x00'\
b'\x2a\x00\x0f\x00\x2b\x00\x12\x00\x2c\x00\x15\x00\x2d\x00\x18\x00'\
b'\x2e\x00\x1b\x00\x2f\x00\x1e\x00\x30\x00\x21\x00\x31\x00\x24\x00'\
b'\x32\x00\x27\x00\x33\x00\x2a\x00\x34\x00\x2d\x00\x35\x00\x30\x00'\
b'\x36\x00\x33\x00\x37\x00\x36\x00\x38\x00\x39\x00\x39\x00\x3c\x00'\
b'\x3a\x00\x3f\x00\xb0\x00\x42\x00'

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

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 16
    return _mvfont[doff + 2:next_offs], 16, width
 
