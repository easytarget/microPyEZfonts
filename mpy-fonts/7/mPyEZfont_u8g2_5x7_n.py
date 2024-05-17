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
# Font: 5x7.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -l 95 -e 32 ../u8g2/tools/font/bdf/5x7.bdf 0 tmp_mPyEZfont_u8g2_5x7_n.py
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
    return 95

_font =\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x05\x00\x20\x20\x20\x20\x00\x20\x00\x05\x00\x50\x50\x50'\
b'\x00\x00\x00\x00\x05\x00\x00\x50\xf8\x50\xf8\x50\x00\x05\x00\x00'\
b'\x70\xa0\x70\x28\x70\x00\x05\x00\x80\x90\x20\x40\x90\x10\x00\x05'\
b'\x00\x00\x40\xa0\x40\xa0\x50\x00\x05\x00\x20\x20\x20\x00\x00\x00'\
b'\x00\x05\x00\x20\x40\x40\x40\x40\x20\x00\x05\x00\x40\x20\x20\x20'\
b'\x20\x40\x00\x05\x00\x00\x50\x20\x70\x20\x50\x00\x05\x00\x00\x20'\
b'\x20\xf8\x20\x20\x00\x05\x00\x00\x00\x00\x00\x30\x20\x40\x05\x00'\
b'\x00\x00\x00\xf0\x00\x00\x00\x05\x00\x00\x00\x00\x00\x60\x60\x00'\
b'\x05\x00\x00\x10\x20\x40\x80\x00\x00\x05\x00\x20\x50\x50\x50\x50'\
b'\x20\x00\x05\x00\x20\x60\x20\x20\x20\x70\x00\x05\x00\x60\x90\x10'\
b'\x20\x40\xf0\x00\x05\x00\xf0\x10\x60\x10\x90\x60\x00\x05\x00\x20'\
b'\x60\xa0\xf0\x20\x20\x00\x05\x00\xf0\x80\xe0\x10\x90\x60\x00\x05'\
b'\x00\x60\x80\xe0\x90\x90\x60\x00\x05\x00\xf0\x10\x20\x20\x40\x40'\
b'\x00\x05\x00\x60\x90\x60\x90\x90\x60\x00\x05\x00\x60\x90\x90\x70'\
b'\x10\x60\x00\x05\x00\x00\x60\x60\x00\x60\x60\x00\x05\x00\x00\x60'\
b'\x60\x00\x60\x40\x80\x05\x00\x00\x10\x20\x40\x20\x10\x00\x05\x00'\
b'\x00\x00\xf0\x00\xf0\x00\x00\x05\x00\x00\x40\x20\x10\x20\x40\x00'\
b'\x05\x00\x20\x50\x10\x20\x00\x20\x00\x05\x00\x60\x90\xb0\xb0\x80'\
b'\x60\x00\x05\x00\x60\x90\x90\xf0\x90\x90\x00\x05\x00\xe0\x90\xe0'\
b'\x90\x90\xe0\x00\x05\x00\x60\x90\x80\x80\x90\x60\x00\x05\x00\xe0'\
b'\x90\x90\x90\x90\xe0\x00\x05\x00\xf0\x80\xe0\x80\x80\xf0\x00\x05'\
b'\x00\xf0\x80\xe0\x80\x80\x80\x00\x05\x00\x60\x90\x80\xb0\x90\x70'\
b'\x00\x05\x00\x90\x90\xf0\x90\x90\x90\x00\x05\x00\x70\x20\x20\x20'\
b'\x20\x70\x00\x05\x00\x10\x10\x10\x10\x90\x60\x00\x05\x00\x90\xa0'\
b'\xc0\xc0\xa0\x90\x00\x05\x00\x80\x80\x80\x80\x80\xf0\x00\x05\x00'\
b'\x90\xf0\xf0\x90\x90\x90\x00\x05\x00\x90\xd0\xd0\xb0\xb0\x90\x00'\
b'\x05\x00\x60\x90\x90\x90\x90\x60\x00\x05\x00\xe0\x90\x90\xe0\x80'\
b'\x80\x00\x05\x00\x60\x90\x90\x90\xd0\x60\x10\x05\x00\xe0\x90\x90'\
b'\xe0\xa0\x90\x00\x05\x00\x60\x90\x40\x20\x90\x60\x00\x05\x00\x70'\
b'\x20\x20\x20\x20\x20\x00\x05\x00\x90\x90\x90\x90\x90\x60\x00\x05'\
b'\x00\x90\x90\x90\x90\x60\x60\x00\x05\x00\x90\x90\x90\xf0\xf0\x90'\
b'\x00\x05\x00\x90\x90\x60\x60\x90\x90\x00\x05\x00\x50\x50\x50\x20'\
b'\x20\x20\x00\x05\x00\xf0\x10\x20\x40\x80\xf0\x00\x05\x00\x70\x40'\
b'\x40\x40\x40\x70\x00\x05\x00\x00\x80\x40\x20\x10\x00\x00\x05\x00'\
b'\x70\x10\x10\x10\x10\x70\x00\x05\x00\x20\x50\x00\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\xf0\x00'

_index =\
b'\x00\x00\x09\x00\x12\x00\x1b\x00\x24\x00\x2d\x00\x36\x00\x3f\x00'\
b'\x48\x00\x51\x00\x5a\x00\x63\x00\x6c\x00\x75\x00\x7e\x00\x87\x00'\
b'\x90\x00\x99\x00\xa2\x00\xab\x00\xb4\x00\xbd\x00\xc6\x00\xcf\x00'\
b'\xd8\x00\xe1\x00\xea\x00\xf3\x00\xfc\x00\x05\x01\x0e\x01\x17\x01'\
b'\x20\x01\x29\x01\x32\x01\x3b\x01\x44\x01\x4d\x01\x56\x01\x5f\x01'\
b'\x68\x01\x71\x01\x7a\x01\x83\x01\x8c\x01\x95\x01\x9e\x01\xa7\x01'\
b'\xb0\x01\xb9\x01\xc2\x01\xcb\x01\xd4\x01\xdd\x01\xe6\x01\xef\x01'\
b'\xf8\x01\x01\x02\x0a\x02\x13\x02\x1c\x02\x25\x02\x2e\x02\x37\x02'\
b'\x40\x02\x49\x02'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 7
    return _mvfont[doff + 2:next_offs], 7, width
 
