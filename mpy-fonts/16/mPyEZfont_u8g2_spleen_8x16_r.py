'''
    mPyEZfont_u8g2_spleen_8x16_r.py : generated as part of the microPyEZfonts repository
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
# Font: spleen-8x16.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -l 127 -e 32 ../u8g2/tools/font/bdf/spleen-8x16.bdf 0 tmp_mPyEZfont_u8g2_spleen_8x16_r.py
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
    return 127

_font =\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x18\x18\x18\x18\x18\x18\x18\x00\x18\x18\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x66\x66\x66\x66\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x6c\x6c\xfe\x6c\x6c\x6c\x6c\xfe\x6c\x6c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x10\x7e\xd0\xd0\xd0'\
b'\x7c\x16\x16\x16\x16\xfc\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x06\x66\x6c\x0c\x18\x18\x30\x36\x66\x60\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x38\x6c\x6c\x6c'\
b'\x38\x70\xda\xcc\xcc\x7a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x18\x18\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x0e\x18\x30\x30\x60'\
b'\x60\x60\x60\x30\x30\x18\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x70\x18\x0c\x0c\x06\x06\x06\x06\x0c\x0c\x18\x70\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x66\x3c'\
b'\x18\xff\x18\x3c\x66\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x18\x18\x7e\x18\x18\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x18\x18\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x7e\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x06\x06\x0c\x0c\x18\x18\x30\x30\x60\x60\xc0\xc0\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x7c\xc6\xc6\xce'\
b'\xde\xf6\xe6\xc6\xc6\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x18\x38\x78\x58\x18\x18\x18\x18\x18\x7e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x7c\xc6\x06\x06'\
b'\x0c\x18\x30\x60\xc6\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x7c\xc6\x06\x06\x3c\x06\x06\x06\xc6\x7c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xc0\xc0\xcc\xcc'\
b'\xcc\xcc\xfe\x0c\x0c\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\xfe\xc6\xc0\xc0\xfc\x06\x06\x06\xc6\x7c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x7c\xc6\xc0\xc0'\
b'\xfc\xc6\xc6\xc6\xc6\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\xfe\xc6\x06\x06\x0c\x18\x30\x30\x30\x30\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x7c\xc6\xc6\xc6'\
b'\x7c\xc6\xc6\xc6\xc6\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x7c\xc6\xc6\xc6\xc6\x7e\x06\x06\xc6\x7c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x18'\
b'\x18\x00\x00\x00\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x18\x18\x00\x00\x00\x18\x18\x30\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x06\x0c\x18\x30'\
b'\x60\x60\x30\x18\x0c\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x7e\x00\x00\x7e\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x60\x30\x18\x0c'\
b'\x06\x06\x0c\x18\x30\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x7c\xc6\x06\x0c\x18\x30\x30\x00\x30\x30\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x7c\xc2\xda'\
b'\xda\xda\xda\xde\xc0\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x7c\xc6\xc6\xc6\xfe\xc6\xc6\xc6\xc6\xc6\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xfc\xc6\xc6\xc6'\
b'\xfc\xc6\xc6\xc6\xc6\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x7e\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\x7e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xfc\xc6\xc6\xc6'\
b'\xc6\xc6\xc6\xc6\xc6\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x7e\xc0\xc0\xc0\xf8\xc0\xc0\xc0\xc0\x7e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x7e\xc0\xc0\xc0'\
b'\xf8\xc0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x7e\xc0\xc0\xc0\xde\xc6\xc6\xc6\xc6\x7e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xc6\xc6\xc6\xc6'\
b'\xfe\xc6\xc6\xc6\xc6\xc6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x7e\x18\x18\x18\x18\x18\x18\x18\x18\x7e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x7e\x18\x18\x18'\
b'\x18\x18\x18\x18\x18\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\xc6\xc6\xc6\xcc\xf8\xcc\xc6\xc6\xc6\xc6\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xc0\xc0\xc0\xc0'\
b'\xc0\xc0\xc0\xc0\xc0\x7e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\xc6\xee\xfe\xd6\xc6\xc6\xc6\xc6\xc6\xc6\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xc6\xc6\xe6\xe6'\
b'\xd6\xd6\xce\xce\xc6\xc6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x7c\xc6\xc6\xc6\xc6\xc6\xc6\xc6\xc6\x7c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xfc\xc6\xc6\xc6'\
b'\xfc\xc0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x7c\xc6\xc6\xc6\xc6\xc6\xc6\xd6\xd6\x7c\x18\x0c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xfc\xc6\xc6\xc6'\
b'\xfc\xc6\xc6\xc6\xc6\xc6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x7e\xc0\xc0\xc0\x7c\x06\x06\x06\x06\xfc\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xff\x18\x18\x18'\
b'\x18\x18\x18\x18\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\xc6\xc6\xc6\xc6\xc6\xc6\xc6\xc6\xc6\x7e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xc6\xc6\xc6\xc6'\
b'\xc6\xc6\xc6\x6c\x38\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\xc6\xc6\xc6\xc6\xc6\xc6\xd6\xfe\xee\xc6\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xc6\xc6\xc6\x6c'\
b'\x38\x6c\xc6\xc6\xc6\xc6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\xc6\xc6\xc6\xc6\x7e\x06\x06\x06\x06\xfc\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xfe\x06\x06\x0c'\
b'\x18\x30\x60\xc0\xc0\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x3e\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x3e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\xc0\xc0\x60\x60\x30'\
b'\x30\x18\x18\x0c\x0c\x06\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x7c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x7c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x10\x38\x6c\xc6\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\xfe\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x30\x18\x0c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x7c\x06\x7e\xc6\xc6\xc6\x7e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xc0\xc0\xc0\xfc'\
b'\xc6\xc6\xc6\xc6\xc6\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x7e\xc0\xc0\xc0\xc0\xc0\x7e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x06\x06\x06\x7e'\
b'\xc6\xc6\xc6\xc6\xc6\x7e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x7e\xc6\xc6\xfe\xc0\xc0\x7e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x1e\x30\x30\x30'\
b'\x7c\x30\x30\x30\x30\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x7e\xc6\xc6\xc6\xc6\xc6\x7c\x06\x06'\
b'\xfc\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xc0\xc0\xc0\xfc'\
b'\xc6\xc6\xc6\xc6\xc6\xc6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x18\x18\x00\x38\x18\x18\x18\x18\x18\x1c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x18\x18\x00\x18'\
b'\x18\x18\x18\x18\x18\x18\x18\x18\x70\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\xc0\xc0\xc0\xcc\xd8\xf0\xf0\xd8\xcc\xc6\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x30\x30\x30\x30'\
b'\x30\x30\x30\x30\x30\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\xec\xd6\xd6\xd6\xd6\xc6\xc6\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\xfc'\
b'\xc6\xc6\xc6\xc6\xc6\xc6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x7c\xc6\xc6\xc6\xc6\xc6\x7c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\xfc'\
b'\xc6\xc6\xc6\xc6\xc6\xfc\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x7e\xc6\xc6\xc6\xc6\xc6\x7e\x06\x06'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x7e'\
b'\xc6\xc0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x7e\xc0\xc0\x7c\x06\x06\xfc\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x30\x30\x30\x7c'\
b'\x30\x30\x30\x30\x30\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\xc6\xc6\xc6\xc6\xc6\xc6\x7e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\xc6'\
b'\xc6\xc6\xc6\x6c\x38\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\xc6\xc6\xd6\xd6\xd6\xd6\x6e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\xc6'\
b'\x6c\x38\x38\x6c\xc6\xc6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\xc6\xc6\xc6\xc6\xc6\xc6\x7e\x06\x06'\
b'\xfc\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\xfe'\
b'\x06\x0c\x18\x30\x60\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x0e\x18\x18\x18\x18\x70\x70\x18\x18\x18\x18\x0e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x18\x18\x18\x18\x18'\
b'\x18\x18\x18\x18\x18\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x70\x18\x18\x18\x18\x0e\x0e\x18\x18\x18\x18\x70\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x32\x7e\x4c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00'

_sparse =\
b'\x20\x00\x03\x00\x21\x00\x06\x00\x22\x00\x09\x00\x23\x00\x0c\x00'\
b'\x24\x00\x0f\x00\x25\x00\x12\x00\x26\x00\x15\x00\x27\x00\x18\x00'\
b'\x28\x00\x1b\x00\x29\x00\x1e\x00\x2a\x00\x21\x00\x2b\x00\x24\x00'\
b'\x2c\x00\x27\x00\x2d\x00\x2a\x00\x2e\x00\x2d\x00\x2f\x00\x30\x00'\
b'\x30\x00\x33\x00\x31\x00\x36\x00\x32\x00\x39\x00\x33\x00\x3c\x00'\
b'\x34\x00\x3f\x00\x35\x00\x42\x00\x36\x00\x45\x00\x37\x00\x48\x00'\
b'\x38\x00\x4b\x00\x39\x00\x4e\x00\x3a\x00\x51\x00\x3b\x00\x54\x00'\
b'\x3c\x00\x57\x00\x3d\x00\x5a\x00\x3e\x00\x5d\x00\x3f\x00\x60\x00'\
b'\x40\x00\x63\x00\x41\x00\x66\x00\x42\x00\x69\x00\x43\x00\x6c\x00'\
b'\x44\x00\x6f\x00\x45\x00\x72\x00\x46\x00\x75\x00\x47\x00\x78\x00'\
b'\x48\x00\x7b\x00\x49\x00\x7e\x00\x4a\x00\x81\x00\x4b\x00\x84\x00'\
b'\x4c\x00\x87\x00\x4d\x00\x8a\x00\x4e\x00\x8d\x00\x4f\x00\x90\x00'\
b'\x50\x00\x93\x00\x51\x00\x96\x00\x52\x00\x99\x00\x53\x00\x9c\x00'\
b'\x54\x00\x9f\x00\x55\x00\xa2\x00\x56\x00\xa5\x00\x57\x00\xa8\x00'\
b'\x58\x00\xab\x00\x59\x00\xae\x00\x5a\x00\xb1\x00\x5b\x00\xb4\x00'\
b'\x5c\x00\xb7\x00\x5d\x00\xba\x00\x5e\x00\xbd\x00\x5f\x00\xc0\x00'\
b'\x60\x00\xc3\x00\x61\x00\xc6\x00\x62\x00\xc9\x00\x63\x00\xcc\x00'\
b'\x64\x00\xcf\x00\x65\x00\xd2\x00\x66\x00\xd5\x00\x67\x00\xd8\x00'\
b'\x68\x00\xdb\x00\x69\x00\xde\x00\x6a\x00\xe1\x00\x6b\x00\xe4\x00'\
b'\x6c\x00\xe7\x00\x6d\x00\xea\x00\x6e\x00\xed\x00\x6f\x00\xf0\x00'\
b'\x70\x00\xf3\x00\x71\x00\xf6\x00\x72\x00\xf9\x00\x73\x00\xfc\x00'\
b'\x74\x00\xff\x00\x75\x00\x02\x01\x76\x00\x05\x01\x77\x00\x08\x01'\
b'\x78\x00\x0b\x01\x79\x00\x0e\x01\x7a\x00\x11\x01\x7b\x00\x14\x01'\
b'\x7c\x00\x17\x01\x7d\x00\x1a\x01\x7e\x00\x1d\x01\x7f\x00\x20\x01'\

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
 
