'''
    mPyEZfont_u8g2_battery19_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original battery19.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "Created with Fony 1.4.7"

    Original Comments from source (may include copyright info):

    COMMENT Exported by Fony v1.4.7
'''

# Code generated by font_to_py.py.
# Font: battery19.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/u-char.set u8g2/tools/font/bdf/battery19.bdf 0 tmp_mPyEZfont_u8g2_battery19_u.py
version = '0.33'

def height():
    return 19

def baseline():
    return 19

def max_width():
    return 9

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 48

def max_ch():
    return 55

_font =\
b'\x09\x00\x3c\x00\xff\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00'\
b'\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00'\
b'\x81\x00\x81\x00\x81\x00\xff\x00\x09\x00\x3c\x00\xff\x00\x81\x00'\
b'\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00'\
b'\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\xff\x00'\
b'\x09\x00\x3c\x00\xff\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00'\
b'\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00'\
b'\xbd\x00\xbd\x00\x81\x00\xff\x00\x09\x00\x3c\x00\xff\x00\x81\x00'\
b'\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00'\
b'\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xff\x00'\
b'\x09\x00\x3c\x00\xff\x00\x81\x00\x81\x00\x81\x00\x81\x00\x81\x00'\
b'\x81\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00'\
b'\xbd\x00\xbd\x00\x81\x00\xff\x00\x09\x00\x3c\x00\xff\x00\x81\x00'\
b'\x81\x00\x81\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00'\
b'\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xff\x00'\
b'\x09\x00\x3c\x00\xff\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00'\
b'\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00\xbd\x00\xbd\x00\x81\x00'\
b'\xbd\x00\xbd\x00\x81\x00\xff\x00\x09\x00\x3c\x00\xff\x00\x81\x00'\
b'\x81\x00\x81\x00\x89\x00\x89\x00\x99\x00\x99\x00\xbd\x00\xbd\x00'\
b'\x99\x00\x99\x00\x91\x00\x91\x00\x81\x00\x81\x00\x81\x00\xff\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00'

_index =\
b'\x00\x00\x28\x00\x50\x00\x78\x00\xa0\x00\xc8\x00\xf0\x00\x18\x01'\
b'\x40\x01\x68\x01'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 48 + 1) if oc >= 48 and oc <= 55 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 19
    return _mvfont[doff + 2:next_offs], 19, width
 
