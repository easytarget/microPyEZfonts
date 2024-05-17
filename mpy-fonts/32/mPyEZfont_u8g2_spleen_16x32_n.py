'''
    mPyEZfont_u8g2_spleen_16x32_n.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original spleen-16x32.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "Copyright (c) 2018-2022, Frederic Cambus"

    Original Comments from source (may include copyright info):

    COMMENT /*
    COMMENT  * Spleen 16x32 1.9.1
    COMMENT  * Copyright (c) 2018-2022, Frederic Cambus
    COMMENT  * https://www.cambus.net/
    COMMENT  *
    COMMENT  * Created:      2018-08-12
    COMMENT  * Last Updated: 2020-10-10
    COMMENT  *
    COMMENT  * Spleen is released under the BSD 2-Clause license.
    COMMENT  * See LICENSE file for details.
    COMMENT  *
    COMMENT  * SPDX-License-Identifier: BSD-2-Clause
    COMMENT  */
'''

# Code generated by font_to_py.py.
# Font: spleen-16x32.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -l 95 -e 32 ../u8g2/tools/font/bdf/spleen-16x32.bdf 0 tmp_mPyEZfont_u8g2_spleen_16x32_n.py
version = '0.33'

def height():
    return 32

def baseline():
    return 26

def max_width():
    return 16

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
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x00\x00'\
b'\x00\x00\x00\x00\x01\x80\x01\x80\x01\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x18\x18\x18\x18\x18\x18\x18\x18\x7f\xfe'\
b'\x7f\xfe\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18'\
b'\x18\x18\x7f\xfe\x7f\xfe\x18\x18\x18\x18\x18\x18\x18\x18\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x01\x80\x01\x80\x0f\xfc\x1f\xfc\x39\x80\x31\x80'\
b'\x31\x80\x31\x80\x31\x80\x39\x80\x1f\xf0\x0f\xf8\x01\x9c\x01\x8c'\
b'\x01\x8c\x01\x8c\x01\x8c\x01\x8c\x01\x8c\x01\x9c\x3f\xf8\x3f\xf0'\
b'\x01\x80\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x0e\x0c\x1b\x18'\
b'\x1b\x18\x1b\x30\x0e\x30\x00\x60\x00\x60\x00\xc0\x00\xc0\x01\x80'\
b'\x01\x80\x03\x00\x03\x00\x06\x38\x06\x6c\x0c\x6c\x0c\x6c\x18\x38'\
b'\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xe0\x0f\xf0'\
b'\x1c\x38\x18\x18\x18\x18\x18\x18\x18\x18\x1c\x38\x0f\xf0\x07\xe0'\
b'\x1f\x80\x3f\xc0\x70\xec\x60\x7c\x60\x38\x60\x30\x60\x38\x70\x7c'\
b'\x3f\xee\x1f\xc6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80\x01\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\xfc\x01\xe0'\
b'\x03\x80\x07\x00\x06\x00\x0e\x00\x0c\x00\x1c\x00\x18\x00\x18\x00'\
b'\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x1c\x00\x0c\x00'\
b'\x0e\x00\x06\x00\x07\x00\x03\x80\x01\xe0\x00\xfc\x00\x3c\x00\x00'\
b'\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x3f\x00'\
b'\x07\x80\x01\xc0\x00\xe0\x00\x60\x00\x70\x00\x30\x00\x38\x00\x18'\
b'\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x38'\
b'\x00\x30\x00\x70\x00\x60\x00\xe0\x01\xc0\x07\x80\x3f\x00\x3c\x00'\
b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x18\x1c\x38'\
b'\x0e\x70\x07\xe0\x03\xc0\x03\xc0\x7f\xfe\x7f\xfe\x03\xc0\x03\xc0'\
b'\x07\xe0\x0e\x70\x1c\x38\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x01\x80\x01\x80\x01\x80\x01\x80\x1f\xf8\x1f\xf8\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80\x01\x80\x01\x80\x03\x80'\
b'\x07\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfc'\
b'\x3f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80'\
b'\x01\x80\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x06\x00\x0c\x00\x0c'\
b'\x00\x18\x00\x18\x00\x30\x00\x30\x00\x60\x00\x60\x00\xc0\x00\xc0'\
b'\x01\x80\x01\x80\x03\x00\x03\x00\x06\x00\x06\x00\x0c\x00\x0c\x00'\
b'\x18\x00\x18\x00\x30\x00\x30\x00\x60\x00\x60\x00\x00\x00\x00\x00'\
b'\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\xf0\x1f\xf8\x38\x1c\x30\x0c\x30\x0c\x30\x1c\x30\x3c\x30\x7c'\
b'\x30\xec\x31\xcc\x33\x8c\x37\x0c\x3e\x0c\x3c\x0c\x38\x0c\x30\x0c'\
b'\x30\x0c\x38\x1c\x1f\xf8\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x03\x80\x07\x80\x0d\x80\x19\x80\x11\x80\x01\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x1f\xf8\x1f\xf8\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0f\xf0\x1f\xf8\x38\x1c\x30\x0c\x00\x0c\x00\x0c'\
b'\x00\x0c\x00\x18\x00\x30\x00\x60\x00\xc0\x01\x80\x03\x00\x06\x00'\
b'\x0c\x00\x18\x00\x30\x0c\x30\x0c\x3f\xfc\x3f\xfc\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0f\xf0\x1f\xf8\x38\x1c\x30\x0c\x00\x0c'\
b'\x00\x0c\x00\x0c\x00\x18\x07\xf0\x07\xf0\x00\x18\x00\x0c\x00\x0c'\
b'\x00\x0c\x00\x0c\x00\x0c\x30\x0c\x38\x1c\x1f\xf8\x0f\xf0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x30\x00\x30\x00\x30\x00\x30\x00'\
b'\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\x3f\xfc\x3f\xfc\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfc\x3f\xfc\x30\x0c'\
b'\x30\x0c\x30\x00\x30\x00\x30\x00\x30\x00\x3f\xf0\x3f\xf8\x00\x1c'\
b'\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x30\x0c\x38\x1c\x1f\xf8'\
b'\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf0\x1f\xf8'\
b'\x38\x1c\x30\x0c\x30\x00\x30\x00\x30\x00\x30\x00\x3f\xf0\x3f\xf8'\
b'\x30\x1c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x38\x1c'\
b'\x1f\xf8\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfc'\
b'\x3f\xfc\x30\x0c\x30\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x18\x00\x30'\
b'\x00\x60\x00\xc0\x01\x80\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\xf0\x1f\xf8\x38\x1c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x18\x18'\
b'\x0f\xf0\x0f\xf0\x18\x18\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x38\x1c\x1f\xf8\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0f\xf0\x1f\xf8\x38\x1c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x38\x0c\x1f\xfc\x0f\xfc\x00\x0c\x00\x0c\x00\x0c'\
b'\x00\x0c\x30\x0c\x38\x1c\x1f\xf8\x0f\xf0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x01\x80\x01\x80\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x01\x80\x01\x80\x01\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x01\x80\x01\x80\x01\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x01\x80\x01\x80\x01\x80\x03\x80\x07\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x38\x00\x70\x00\xe0'\
b'\x01\xc0\x03\x80\x07\x00\x0e\x00\x1c\x00\x38\x00\x38\x00\x1c\x00'\
b'\x0e\x00\x07\x00\x03\x80\x01\xc0\x00\xe0\x00\x70\x00\x38\x00\x1c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x3f\xfc\x3f\xfc\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x3f\xfc\x3f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x00\x1c\x00'\
b'\x0e\x00\x07\x00\x03\x80\x01\xc0\x00\xe0\x00\x70\x00\x38\x00\x1c'\
b'\x00\x1c\x00\x38\x00\x70\x00\xe0\x01\xc0\x03\x80\x07\x00\x0e\x00'\
b'\x1c\x00\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf0'\
b'\x1f\xf8\x38\x1c\x30\x0c\x00\x0c\x00\x0c\x00\x18\x00\x30\x00\x60'\
b'\x00\xc0\x00\xc0\x01\x80\x01\x80\x01\x80\x00\x00\x00\x00\x00\x00'\
b'\x01\x80\x01\x80\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0f\xf0\x1f\xf8\x38\x1c\x30\x0c\x30\x0c\x31\xcc'\
b'\x31\xcc\x31\xcc\x31\xcc\x31\xcc\x31\xcc\x31\xfc\x31\xfc\x30\x00'\
b'\x30\x00\x38\x00\x1f\xf8\x0f\xf8\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0f\xf0\x1f\xf8\x38\x1c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x3f\xfc\x3f\xfc\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x3f\xf0\x3f\xf8\x30\x1c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x18\x3f\xf0\x3f\xf0\x30\x18\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x1c\x3f\xf8\x3f\xf0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0f\xfc\x1f\xfc\x38\x00\x30\x00\x30\x00'\
b'\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00'\
b'\x30\x00\x30\x00\x30\x00\x30\x00\x38\x00\x1f\xfc\x0f\xfc\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xf0\x3f\xf8\x30\x1c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x1c\x3f\xf8\x3f\xf0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xfc\x1f\xfc\x38\x00'\
b'\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x3f\xe0\x3f\xe0'\
b'\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x38\x00\x1f\xfc'\
b'\x0f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xfc\x1f\xfc'\
b'\x38\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x3f\xe0'\
b'\x3f\xe0\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00'\
b'\x30\x00\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xfc'\
b'\x1f\xfc\x38\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00'\
b'\x30\xfc\x30\xfc\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x38\x0c\x1f\xfc\x0f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x3f\xfc\x3f\xfc\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1f\xf8\x1f\xf8\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x1f\xf8\x1f\xf8\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x1f\xf8\x1f\xf8\x01\x80\x01\x80\x01\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x03\x80\x7f\x00\x7e\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x18\x30\x30\x30\x60\x3f\xc0\x3f\xc0\x30\x60\x30\x30'\
b'\x30\x18\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x30\x00\x30\x00\x30\x00\x30\x00'\
b'\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00'\
b'\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x38\x00\x1f\xfc\x0f\xfc'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30\x0c\x38\x1c\x3c\x3c'\
b'\x3e\x7c\x37\xec\x33\xcc\x31\x8c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30\x0c\x30\x0c'\
b'\x38\x0c\x38\x0c\x3c\x0c\x3c\x0c\x36\x0c\x36\x0c\x33\x0c\x33\x0c'\
b'\x31\x8c\x31\x8c\x30\xcc\x30\xcc\x30\x6c\x30\x6c\x30\x3c\x30\x3c'\
b'\x30\x1c\x30\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf0'\
b'\x1f\xf8\x38\x1c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x38\x1c\x1f\xf8\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x3f\xf0\x3f\xf8\x30\x1c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x1c\x3f\xf8\x3f\xf0\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00'\
b'\x30\x00\x30\x00\x30\x00\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0f\xf0\x1f\xf8\x38\x1c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x31\x8c'\
b'\x31\x8c\x30\xcc\x38\xdc\x1f\xf8\x0f\xf0\x00\x30\x00\x30\x00\x18'\
b'\x00\x18\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x3f\xf0\x3f\xf8\x30\x1c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x18\x3f\xf0\x3f\xf0\x30\x18\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0f\xfc\x1f\xfc\x38\x00\x30\x00\x30\x00'\
b'\x30\x00\x30\x00\x30\x00\x38\x00\x1f\xf0\x0f\xf8\x00\x1c\x00\x0c'\
b'\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x1c\x3f\xf8\x3f\xf0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xfe\x7f\xfe\x01\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x38\x0c\x1f\xfc'\
b'\x0f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x38\x1c\x1c\x38\x0e\x70\x07\xe0'\
b'\x03\xc0\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x31\x8c\x33\xcc\x37\xec\x3e\x7c'\
b'\x3c\x3c\x38\x1c\x30\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x38\x1c\x1c\x38'\
b'\x0e\x70\x07\xe0\x07\xe0\x0e\x70\x1c\x38\x38\x1c\x30\x0c\x30\x0c'\
b'\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c\x30\x0c'\
b'\x30\x0c\x38\x0c\x1f\xfc\x0f\xfc\x00\x0c\x00\x0c\x00\x0c\x00\x0c'\
b'\x00\x0c\x00\x0c\x00\x1c\x3f\xf8\x3f\xf0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x3f\xfc\x3f\xfc\x00\x0c\x00\x0c\x00\x0c\x00\x0c'\
b'\x00\x18\x00\x30\x00\x60\x00\xc0\x01\x80\x03\x00\x06\x00\x0c\x00'\
b'\x18\x00\x30\x00\x30\x00\x30\x00\x3f\xfc\x3f\xfc\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x0f\xfc'\
b'\x0f\xfc\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0f\xfc\x0f\xfc\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'\
b'\x00\x00\x60\x00\x60\x00\x30\x00\x30\x00\x18\x00\x18\x00\x0c\x00'\
b'\x0c\x00\x06\x00\x06\x00\x03\x00\x03\x00\x01\x80\x01\x80\x00\xc0'\
b'\x00\xc0\x00\x60\x00\x60\x00\x30\x00\x30\x00\x18\x00\x18\x00\x0c'\
b'\x00\x0c\x00\x06\x00\x06\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\x00\x00\x3f\xf0\x3f\xf0\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30'\
b'\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30'\
b'\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30'\
b'\x00\x30\x00\x30\x00\x30\x3f\xf0\x3f\xf0\x00\x00\x00\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80\x03\xc0\x07\xe0\x0e\x70'\
b'\x1c\x38\x38\x1c\x70\x0e\x60\x06\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xfe\x7f\xfe\x00\x00'\
b'\x00\x00'

_index =\
b'\x00\x00\x42\x00\x84\x00\xc6\x00\x08\x01\x4a\x01\x8c\x01\xce\x01'\
b'\x10\x02\x52\x02\x94\x02\xd6\x02\x18\x03\x5a\x03\x9c\x03\xde\x03'\
b'\x20\x04\x62\x04\xa4\x04\xe6\x04\x28\x05\x6a\x05\xac\x05\xee\x05'\
b'\x30\x06\x72\x06\xb4\x06\xf6\x06\x38\x07\x7a\x07\xbc\x07\xfe\x07'\
b'\x40\x08\x82\x08\xc4\x08\x06\x09\x48\x09\x8a\x09\xcc\x09\x0e\x0a'\
b'\x50\x0a\x92\x0a\xd4\x0a\x16\x0b\x58\x0b\x9a\x0b\xdc\x0b\x1e\x0c'\
b'\x60\x0c\xa2\x0c\xe4\x0c\x26\x0d\x68\x0d\xaa\x0d\xec\x0d\x2e\x0e'\
b'\x70\x0e\xb2\x0e\xf4\x0e\x36\x0f\x78\x0f\xba\x0f\xfc\x0f\x3e\x10'\
b'\x80\x10\xc2\x10'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 32
    return _mvfont[doff + 2:next_offs], 32, width
 
