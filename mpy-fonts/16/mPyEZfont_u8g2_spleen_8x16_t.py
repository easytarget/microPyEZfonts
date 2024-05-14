'''
    mPyEZfont_u8g2_spleen_8x16_t.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original spleen-8x16.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "Copyright (c) 2018-2022, Frederic Cambus"

    Original Comments from source (may include copyright info):

    COMMENT /*
    COMMENT  * Spleen 8x16 1.9.1
    COMMENT  * Copyright (c) 2018-2022, Frederic Cambus
    COMMENT  * https://www.cambus.net/
    COMMENT  *
    COMMENT  * Created:      2018-08-11
    COMMENT  * Last Updated: 2020-10-10
    COMMENT  *
    COMMENT  * Spleen is released under the BSD 2-Clause license.
    COMMENT  * See LICENSE file for details.
    COMMENT  *
    COMMENT  * SPDX-License-Identifier: BSD-2-Clause
    COMMENT  */
'''

# Code generated by font_to_py.py.
# Font: spleen-8x16.bdf Char set:  +-.0123456789:
# Cmd: ../micropython-font-to-py/font_to_py.py -x -k ./t-char.set -e 32 ../u8g2/tools/font/bdf/spleen-8x16.bdf 0 tmp_mPyEZfont_u8g2_spleen_8x16_t.py
version = '0.33'

def height():
    return 16

def baseline():
    return 12

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
    return 58

_font =\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x18\x18\x7e\x18\x18'\
b'\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x7e'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x18\x18\x00\x00\x00\x00\x08\x00\x00\x00\x7c\xc6'\
b'\xc6\xce\xde\xf6\xe6\xc6\xc6\x7c\x00\x00\x00\x00\x08\x00\x00\x00'\
b'\x18\x38\x78\x58\x18\x18\x18\x18\x18\x7e\x00\x00\x00\x00\x08\x00'\
b'\x00\x00\x7c\xc6\x06\x06\x0c\x18\x30\x60\xc6\xfe\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x7c\xc6\x06\x06\x3c\x06\x06\x06\xc6\x7c\x00\x00'\
b'\x00\x00\x08\x00\x00\x00\xc0\xc0\xcc\xcc\xcc\xcc\xfe\x0c\x0c\x0c'\
b'\x00\x00\x00\x00\x08\x00\x00\x00\xfe\xc6\xc0\xc0\xfc\x06\x06\x06'\
b'\xc6\x7c\x00\x00\x00\x00\x08\x00\x00\x00\x7c\xc6\xc0\xc0\xfc\xc6'\
b'\xc6\xc6\xc6\x7c\x00\x00\x00\x00\x08\x00\x00\x00\xfe\xc6\x06\x06'\
b'\x0c\x18\x30\x30\x30\x30\x00\x00\x00\x00\x08\x00\x00\x00\x7c\xc6'\
b'\xc6\xc6\x7c\xc6\xc6\xc6\xc6\x7c\x00\x00\x00\x00\x08\x00\x00\x00'\
b'\x7c\xc6\xc6\xc6\xc6\x7e\x06\x06\xc6\x7c\x00\x00\x00\x00\x08\x00'\
b'\x00\x00\x00\x00\x00\x18\x18\x00\x00\x00\x18\x18\x00\x00\x00\x00'\

_index =\
b'\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x24\x00\x00\x00\x36\x00\x48\x00'\
b'\x00\x00\x5a\x00\x6c\x00\x7e\x00\x90\x00\xa2\x00\xb4\x00\xc6\x00'\
b'\xd8\x00\xea\x00\xfc\x00\x0e\x01\x20\x01'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 58 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 16
    return _mvfont[doff + 2:next_offs], 16, width
 