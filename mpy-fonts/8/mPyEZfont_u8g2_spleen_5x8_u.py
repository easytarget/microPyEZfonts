'''
    mPyEZfont_u8g2_spleen_5x8_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original spleen-5x8.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "Copyright (c) 2018-2022, Frederic Cambus"

    Original Comments from source (may include copyright info):

    COMMENT /*
    COMMENT  * Spleen 5x8 1.9.1
    COMMENT  * Copyright (c) 2018-2022, Frederic Cambus
    COMMENT  * https://www.cambus.net/
    COMMENT  *
    COMMENT  * Created:      2018-08-08
    COMMENT  * Last Updated: 2021-03-10
    COMMENT  *
    COMMENT  * Spleen is released under the BSD 2-Clause license.
    COMMENT  * See LICENSE file for details.
    COMMENT  *
    COMMENT  * SPDX-License-Identifier: BSD-2-Clause
    COMMENT  */
'''

# Code generated by font_to_py.py.
# Font: spleen-5x8.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -l 95 -e 32 ../u8g2/tools/font/bdf/spleen-5x8.bdf 0 tmp_mPyEZfont_u8g2_spleen_5x8_u.py
version = '0.33'

def height():
    return 8

def baseline():
    return 7

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
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x05\x00\x20\x20\x20\x20\x20\x00\x20\x00\x05\x00'\
b'\x50\x50\x50\x00\x00\x00\x00\x00\x05\x00\x00\x50\xf8\x50\x50\xf8'\
b'\x50\x00\x05\x00\x20\x70\xa0\x60\x30\x30\xe0\x20\x05\x00\x10\x90'\
b'\xa0\x20\x40\x50\x90\x80\x05\x00\x20\x50\x50\x60\xa8\x90\x68\x00'\
b'\x05\x00\x20\x20\x20\x00\x00\x00\x00\x00\x05\x00\x10\x20\x40\x40'\
b'\x40\x40\x20\x10\x05\x00\x40\x20\x10\x10\x10\x10\x20\x40\x05\x00'\
b'\x00\x00\x90\x60\xf0\x60\x90\x00\x05\x00\x00\x00\x20\x20\xf8\x20'\
b'\x20\x00\x05\x00\x00\x00\x00\x00\x00\x20\x20\x40\x05\x00\x00\x00'\
b'\x00\x00\xf0\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x20\x00'\
b'\x05\x00\x10\x10\x20\x20\x40\x40\x80\x80\x05\x00\x00\x60\x90\xb0'\
b'\xd0\x90\x60\x00\x05\x00\x00\x20\x60\x20\x20\x20\x70\x00\x05\x00'\
b'\x00\x60\x90\x10\x60\x80\xf0\x00\x05\x00\x00\x60\x90\x20\x10\x90'\
b'\x60\x00\x05\x00\x00\x80\xa0\xa0\xf0\x20\x20\x00\x05\x00\x00\xf0'\
b'\x80\xe0\x10\x10\xe0\x00\x05\x00\x00\x60\x80\xe0\x90\x90\x60\x00'\
b'\x05\x00\x00\xf0\x90\x10\x20\x40\x40\x00\x05\x00\x00\x60\x90\x60'\
b'\x90\x90\x60\x00\x05\x00\x00\x60\x90\x90\x70\x10\x60\x00\x05\x00'\
b'\x00\x00\x00\x20\x00\x00\x20\x00\x05\x00\x00\x00\x00\x20\x00\x20'\
b'\x20\x40\x05\x00\x00\x10\x20\x40\x40\x20\x10\x00\x05\x00\x00\x00'\
b'\x00\xf0\x00\xf0\x00\x00\x05\x00\x00\x40\x20\x10\x10\x20\x40\x00'\
b'\x05\x00\x60\x90\x10\x20\x40\x00\x40\x00\x05\x00\x00\x60\x90\xb0'\
b'\xb0\x80\x70\x00\x05\x00\x00\x60\x90\x90\xf0\x90\x90\x00\x05\x00'\
b'\x00\xe0\x90\xe0\x90\x90\xe0\x00\x05\x00\x00\x70\x80\x80\x80\x80'\
b'\x70\x00\x05\x00\x00\xe0\x90\x90\x90\x90\xe0\x00\x05\x00\x00\x70'\
b'\x80\xe0\x80\x80\x70\x00\x05\x00\x00\x70\x80\x80\xe0\x80\x80\x00'\
b'\x05\x00\x00\x70\x80\xb0\x90\x90\x70\x00\x05\x00\x00\x90\x90\xf0'\
b'\x90\x90\x90\x00\x05\x00\x00\x70\x20\x20\x20\x20\x70\x00\x05\x00'\
b'\x00\x70\x20\x20\x20\x20\xc0\x00\x05\x00\x00\x90\x90\xe0\x90\x90'\
b'\x90\x00\x05\x00\x00\x80\x80\x80\x80\x80\x70\x00\x05\x00\x00\x90'\
b'\xf0\xf0\x90\x90\x90\x00\x05\x00\x00\x90\xd0\xd0\xb0\xb0\x90\x00'\
b'\x05\x00\x00\x60\x90\x90\x90\x90\x60\x00\x05\x00\x00\xe0\x90\x90'\
b'\xe0\x80\x80\x00\x05\x00\x00\x60\x90\x90\x90\x90\x60\x30\x05\x00'\
b'\x00\xe0\x90\x90\xe0\x90\x90\x00\x05\x00\x00\x70\x80\x60\x10\x10'\
b'\xe0\x00\x05\x00\x00\xf8\x20\x20\x20\x20\x20\x00\x05\x00\x00\x90'\
b'\x90\x90\x90\x90\x70\x00\x05\x00\x00\x90\x90\x90\x90\x60\x60\x00'\
b'\x05\x00\x00\x90\x90\x90\xf0\xf0\x90\x00\x05\x00\x00\x90\x90\x60'\
b'\x60\x90\x90\x00\x05\x00\x00\x90\x90\x90\x70\x10\xe0\x00\x05\x00'\
b'\x00\xf0\x10\x20\x40\x80\xf0\x00\x05\x00\x70\x40\x40\x40\x40\x40'\
b'\x40\x70\x05\x00\x80\x80\x40\x40\x20\x20\x10\x10\x05\x00\x70\x10'\
b'\x10\x10\x10\x10\x10\x70\x05\x00\x00\x20\x50\x88\x00\x00\x00\x00'\
b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\xf0'

_index =\
b'\x00\x00\x0a\x00\x14\x00\x1e\x00\x28\x00\x32\x00\x3c\x00\x46\x00'\
b'\x50\x00\x5a\x00\x64\x00\x6e\x00\x78\x00\x82\x00\x8c\x00\x96\x00'\
b'\xa0\x00\xaa\x00\xb4\x00\xbe\x00\xc8\x00\xd2\x00\xdc\x00\xe6\x00'\
b'\xf0\x00\xfa\x00\x04\x01\x0e\x01\x18\x01\x22\x01\x2c\x01\x36\x01'\
b'\x40\x01\x4a\x01\x54\x01\x5e\x01\x68\x01\x72\x01\x7c\x01\x86\x01'\
b'\x90\x01\x9a\x01\xa4\x01\xae\x01\xb8\x01\xc2\x01\xcc\x01\xd6\x01'\
b'\xe0\x01\xea\x01\xf4\x01\xfe\x01\x08\x02\x12\x02\x1c\x02\x26\x02'\
b'\x30\x02\x3a\x02\x44\x02\x4e\x02\x58\x02\x62\x02\x6c\x02\x76\x02'\
b'\x80\x02\x8a\x02'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 8
    return _mvfont[doff + 2:next_offs], 8, width
 