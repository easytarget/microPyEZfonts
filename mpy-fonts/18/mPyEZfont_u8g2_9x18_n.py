'''
    mPyEZfont_u8g2_9x18_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original 9x18.bdf font file was sourced from the U8G2 project:
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
# Font: 9x18.bdf Char set:  *+,-./0123456789:
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/n-char.set u8g2/tools/font/bdf/9x18.bdf 0 tmp_mPyEZfont_u8g2_9x18_n.py
version = '0.33'

def height():
    return 18

def baseline():
    return 14

def max_width():
    return 9

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
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x22\x00\x41\x00'\
b'\x01\x00\x02\x00\x04\x00\x08\x00\x08\x00\x00\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x08\x00\x49\x00\x2a\x00\x1c\x00\x2a\x00'\
b'\x49\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x0c\x00\x04\x00\x08\x00\x00\x00\x00\x00\x09\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x01\x00\x02\x00\x02\x00\x04\x00\x08\x00\x08\x00'\
b'\x10\x00\x20\x00\x20\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x22\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x22\x00\x1c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x18\x00\x28\x00\x48\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x1c\x00\x22\x00\x41\x00\x01\x00\x02\x00'\
b'\x04\x00\x08\x00\x10\x00\x20\x00\x7f\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x01\x00'\
b'\x02\x00\x04\x00\x0c\x00\x02\x00\x01\x00\x01\x00\x42\x00\x3c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x02\x00\x06\x00\x0a\x00\x12\x00\x22\x00\x42\x00\x7f\x00'\
b'\x02\x00\x02\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x40\x00\x40\x00\x40\x00'\
b'\x7c\x00\x02\x00\x01\x00\x01\x00\x42\x00\x3c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00'\
b'\x20\x00\x40\x00\x40\x00\x5c\x00\x62\x00\x41\x00\x41\x00\x22\x00'\
b'\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x7f\x00\x01\x00\x02\x00\x02\x00\x04\x00\x04\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x22\x00\x41\x00'\
b'\x22\x00\x1c\x00\x22\x00\x41\x00\x41\x00\x22\x00\x1c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x1c\x00\x22\x00\x41\x00\x41\x00\x23\x00\x1d\x00\x01\x00\x01\x00'\
b'\x02\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00'

_index =\
b'\x00\x00\x26\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x4c\x00\x72\x00\x98\x00\xbe\x00\xe4\x00'\
b'\x0a\x01\x30\x01\x56\x01\x7c\x01\xa2\x01\xc8\x01\xee\x01\x14\x02'\
b'\x3a\x02\x60\x02\x86\x02\xac\x02\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\xd2\x02'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 63 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 18
    return _mvfont[doff + 2:next_offs], 18, width
 
