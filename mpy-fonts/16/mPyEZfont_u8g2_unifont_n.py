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
# Font: unifont.bdf Char set:  *+,-./0123456789:
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/unifont.bdf 0 tmp_mPyEZfont_u8g2_unifont_n.py
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
    return 63

_font =\
b'\x08\x00\x00\x00\x00\x00\x3c\x42\x42\x02\x04\x08\x08\x00\x08\x08'\
b'\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x08\x49\x2a\x1c'\
b'\x2a\x49\x08\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x08\x08'\
b'\x08\x7f\x08\x08\x08\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x18\x08\x08\x10\x08\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x3c\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x18\x00\x00\x08\x00'\
b'\x00\x00\x00\x00\x02\x02\x04\x08\x08\x10\x10\x20\x40\x40\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x18\x24\x42\x46\x4a\x52\x62\x42\x24\x18'\
b'\x00\x00\x08\x00\x00\x00\x00\x00\x08\x18\x28\x08\x08\x08\x08\x08'\
b'\x08\x3e\x00\x00\x08\x00\x00\x00\x00\x00\x3c\x42\x42\x02\x0c\x10'\
b'\x20\x40\x40\x7e\x00\x00\x08\x00\x00\x00\x00\x00\x3c\x42\x42\x02'\
b'\x1c\x02\x02\x42\x42\x3c\x00\x00\x08\x00\x00\x00\x00\x00\x04\x0c'\
b'\x14\x24\x44\x44\x7e\x04\x04\x04\x00\x00\x08\x00\x00\x00\x00\x00'\
b'\x7e\x40\x40\x40\x7c\x02\x02\x02\x42\x3c\x00\x00\x08\x00\x00\x00'\
b'\x00\x00\x1c\x20\x40\x40\x7c\x42\x42\x42\x42\x3c\x00\x00\x08\x00'\
b'\x00\x00\x00\x00\x7e\x02\x02\x04\x04\x04\x08\x08\x08\x08\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x3c\x42\x42\x42\x3c\x42\x42\x42\x42\x3c'\
b'\x00\x00\x08\x00\x00\x00\x00\x00\x3c\x42\x42\x42\x3e\x02\x02\x02'\
b'\x04\x38\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x18\x18\x00\x00'\
b'\x00\x18\x18\x00\x00\x00'

_index =\
b'\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x24\x00\x36\x00\x48\x00\x5a\x00\x6c\x00'\
b'\x7e\x00\x90\x00\xa2\x00\xb4\x00\xc6\x00\xd8\x00\xea\x00\xfc\x00'\
b'\x0e\x01\x20\x01\x32\x01\x44\x01\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x56\x01'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 63 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 16
    return _mvfont[doff + 2:next_offs], 16, width
 
