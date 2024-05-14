'''
    mPyEZfont_u8g2_spleen_12x24_e.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original spleen-12x24.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "Copyright (c) 2018-2022, Frederic Cambus"

    Original Comments from source (may include copyright info):

    COMMENT /*
    COMMENT  * Spleen 12x24 1.9.1
    COMMENT  * Copyright (c) 2018-2022, Frederic Cambus
    COMMENT  * https://www.cambus.net/
    COMMENT  *
    COMMENT  * Created:      2018-08-15
    COMMENT  * Last Updated: 2020-10-10
    COMMENT  *
    COMMENT  * Spleen is released under the BSD 2-Clause license.
    COMMENT  * See LICENSE file for details.
    COMMENT  *
    COMMENT  * SPDX-License-Identifier: BSD-2-Clause
    COMMENT  */
'''

# Code generated by font_to_py.py.
# Font: spleen-12x24.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -e 32 ../u8g2/tools/font/bdf/spleen-12x24.bdf 0 tmp_mPyEZfont_u8g2_spleen_12x24_e.py
version = '0.33'

def height():
    return 24

def baseline():
    return 19

def max_width():
    return 12

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 126

_font =\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'\
b'\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x00\x00\x00\x00\x06\x00\x06\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x30\xc0\x30\xc0'\
b'\x30\xc0\x30\xc0\x30\xc0\x30\xc0\x30\xc0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x30\xc0\x30\xc0\x30\xc0\x7f\xe0\x30\xc0\x30\xc0\x30\xc0'\
b'\x30\xc0\x30\xc0\x30\xc0\x30\xc0\x7f\xe0\x30\xc0\x30\xc0\x30\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\x06\x00\x06\x00\x1f\xe0\x36\x00\x66\x00\x66\x00\x66\x00\x66\x00'\
b'\x36\x00\x1f\x80\x06\xc0\x06\x60\x06\x60\x06\x60\x06\x60\x06\xc0'\
b'\x7f\x80\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x38\xc0\x6d\x80\x6d\x80'\
b'\x3b\x00\x03\x00\x06\x00\x06\x00\x0c\x00\x0d\xc0\x1b\x60\x1b\x60'\
b'\x31\xc0\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x19\x80\x30\xc0\x30\xc0'\
b'\x30\xc0\x30\xc0\x19\x80\x0f\x00\x33\x00\x61\xa0\x60\xe0\x60\xc0'\
b'\x60\xc0\x31\xe0\x1f\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x00\x00\x00\x00\x00\xe0\x01\x80\x03\x00\x06\x00'\
b'\x0c\x00\x0c\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00'\
b'\x18\x00\x18\x00\x0c\x00\x0c\x00\x06\x00\x03\x00\x01\x80\x00\xe0'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x70\x00\x18\x00\x0c\x00'\
b'\x06\x00\x03\x00\x03\x00\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x03\x00\x03\x00\x06\x00\x0c\x00\x18\x00'\
b'\x70\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x30\xc0\x19\x80\x0f\x00\x06\x00'\
b'\x7f\xe0\x06\x00\x0f\x00\x19\x80\x30\xc0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x06\x00'\
b'\x06\x00\x3f\xc0\x06\x00\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x06\x00'\
b'\x06\x00\x0c\x00\x18\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x3f\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x30\x00\x30\x00\x60\x00\x60\x00\xc0'\
b'\x00\xc0\x01\x80\x01\x80\x03\x00\x03\x00\x06\x00\x06\x00\x0c\x00'\
b'\x0c\x00\x18\x00\x18\x00\x30\x00\x30\x00\x60\x00\x60\x00\x00\x00'\
b'\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80\x30\xc0'\
b'\x60\x60\x60\x60\x60\xe0\x61\xe0\x63\x60\x66\x60\x6c\x60\x78\x60'\
b'\x70\x60\x60\x60\x60\x60\x30\xc0\x1f\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00'\
b'\x1e\x00\x36\x00\x26\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x3f\xc0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x1f\x80\x30\xc0\x60\x60\x00\x60\x00\x60\x00\x60\x00\xc0\x01\x80'\
b'\x03\x00\x06\x00\x0c\x00\x18\x00\x30\x00\x60\x60\x7f\xe0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1f\x80\x30\xc0\x60\x60\x00\x60\x00\x60\x00\xc0\x0f\x80'\
b'\x00\xc0\x00\x60\x00\x60\x00\x60\x00\x60\x60\x60\x30\xc0\x1f\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x60\x00\x60\x00\x60\x00\x61\x80\x61\x80\x61\x80'\
b'\x61\x80\x61\x80\x61\x80\x61\x80\x7f\xe0\x01\x80\x01\x80\x01\x80'\
b'\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x7f\xe0\x60\x60\x60\x00\x60\x00\x60\x00'\
b'\x60\x00\x7f\x80\x00\xc0\x00\x60\x00\x60\x00\x60\x00\x60\x60\x60'\
b'\x30\xc0\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xc0\x30\x60\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x7f\x80\x60\xc0\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x30\xc0\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xe0\x60\x60\x00\x60'\
b'\x00\x60\x00\x60\x00\xc0\x01\x80\x03\x00\x06\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80\x30\xc0'\
b'\x60\x60\x60\x60\x60\x60\x30\xc0\x1f\x80\x30\xc0\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x30\xc0\x1f\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80'\
b'\x30\xc0\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x30\x60\x1f\xe0'\
b'\x00\x60\x00\x60\x00\x60\x00\x60\x60\xc0\x3f\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x06\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x06\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x06\x00\x06\x00'\
b'\x0c\x00\x18\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x60\x00\xc0\x01\x80\x03\x00\x06\x00\x0c\x00'\
b'\x18\x00\x30\x00\x18\x00\x0c\x00\x06\x00\x03\x00\x01\x80\x00\xc0'\
b'\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x7f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x30\x00\x18\x00\x0c\x00\x06\x00'\
b'\x03\x00\x01\x80\x00\xc0\x00\x60\x00\xc0\x01\x80\x03\x00\x06\x00'\
b'\x0c\x00\x18\x00\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80\x30\xc0\x60\x60'\
b'\x00\x60\x00\x60\x00\xc0\x01\x80\x03\x00\x06\x00\x06\x00\x06\x00'\
b'\x00\x00\x00\x00\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80'\
b'\x30\xc0\x60\x60\x60\x60\x67\x60\x67\x60\x67\x60\x67\x60\x67\x60'\
b'\x67\x60\x67\xe0\x60\x00\x30\x00\x1f\xc0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80'\
b'\x30\xc0\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x7f\xe0\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x7f\x80\x60\xc0\x60\x60\x60\x60\x60\x60\x60\x60\x60\xc0\x7f\x80'\
b'\x60\xc0\x60\x60\x60\x60\x60\x60\x60\x60\x60\xc0\x7f\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1f\xe0\x30\x00\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x30\x00\x1f\xe0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x7f\x80\x60\xc0\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\xc0'\
b'\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x1f\xe0\x30\x00\x60\x00\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x7f\x80\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00'\
b'\x30\x00\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xe0\x30\x00\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x60\x00\x7f\x80\x60\x00\x60\x00\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xe0\x30\x00\x60\x00'\
b'\x60\x00\x60\x00\x60\x00\x60\x00\x63\xe0\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x30\x60\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x7f\xe0\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xc0'\
b'\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x3f\xc0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x3f\xc0\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x0e\x00\x7c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\xc0\x61\x80'\
b'\x7f\x00\x61\x80\x60\xc0\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x30\x00'\
b'\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x60\x60\x70\xe0\x79\xe0\x6f\x60\x66\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x70\x60\x70\x60\x78\x60'\
b'\x78\x60\x6c\x60\x6c\x60\x66\x60\x66\x60\x63\x60\x63\x60\x61\xe0'\
b'\x61\xe0\x60\xe0\x60\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80\x30\xc0\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x30\xc0\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x60\xc0'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\xc0\x7f\x80\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80'\
b'\x30\xc0\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x66\x60\x66\x60\x63\x60\x33\xc0\x1f\x80\x01\x80\x00\xc0'\
b'\x00\xc0\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x7f\x80\x60\xc0\x60\x60\x60\x60\x60\x60\x60\x60\x60\xc0\x7f\x80'\
b'\x60\xc0\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1f\xe0\x30\x00\x60\x00\x60\x00\x60\x00\x60\x00\x30\x00'\
b'\x1f\x80\x00\xc0\x00\x60\x00\x60\x00\x60\x00\x60\x00\xc0\x7f\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x7f\xe0\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x30\x60\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x30\xc0\x30\xc0'\
b'\x19\x80\x0f\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x66\x60'\
b'\x6f\x60\x79\xe0\x70\xe0\x60\x60\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x30\xc0\x1f\x80\x30\xc0\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x30\x60\x1f\xe0\x00\x60'\
b'\x00\x60\x00\x60\x00\x60\x00\x60\x00\xe0\x7f\xc0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x7f\xe0\x00\x60\x00\x60\x00\x60\x00\xc0\x01\x80\x03\x00\x06\x00'\
b'\x0c\x00\x18\x00\x30\x00\x60\x00\x60\x00\x60\x00\x7f\xe0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x1f\xe0\x18\x00'\
b'\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00'\
b'\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00'\
b'\x18\x00\x18\x00\x18\x00\x1f\xe0\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\xc0\x00\xc0\x00\x60\x00\x60\x00\x30\x00\x30\x00\x18\x00\x18\x00'\
b'\x0c\x00\x0c\x00\x06\x00\x06\x00\x03\x00\x03\x00\x01\x80\x01\x80'\
b'\x00\xc0\x00\xc0\x00\x60\x00\x60\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x7f\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
b'\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x7f\x80\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x04\x00\x0e\x00\x1b\x00\x31\x80\x60\xc0\xc0\x60'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xe0'\
b'\x00\x00\x0c\x00\x00\x00\x00\x00\x18\x00\x0c\x00\x06\x00\x03\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x3f\x80\x00\xc0\x00\x60\x00\x60\x1f\xe0'\
b'\x30\x60\x60\x60\x60\x60\x60\x60\x30\x60\x1f\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x60\x00\x60\x00\x60\x00\x60\x00\x7f\x80\x60\xc0\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\xc0\x7f\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xe0\x30\x00\x60\x00'\
b'\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x30\x00\x1f\xe0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x60\x00\x60\x00\x60\x00\x60\x1f\xe0\x30\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x30\x60'\
b'\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xe0'\
b'\x30\x60\x60\x60\x60\x60\x60\x60\x7f\xe0\x60\x00\x60\x00\x60\x00'\
b'\x30\x00\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xc0\x0e\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x3f\x80\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1f\xe0\x30\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x30\x60\x1f\xc0\x00\xc0\x00\x60\x00\x60\x00\xc0'\
b'\x3f\x80\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x7f\x80\x60\xc0\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'\
b'\x06\x00\x00\x00\x00\x00\x1e\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x07\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x06\x00\x00\x00\x00\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x0c\x00\x78\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\xc0\x30\xc0\x31\x80'\
b'\x33\x00\x3e\x00\x36\x00\x33\x00\x31\x80\x30\xc0\x30\x60\x30\x60'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0e\x00'\
b'\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x79\x80'\
b'\x66\xc0\x66\x60\x66\x60\x66\x60\x66\x60\x66\x60\x66\x60\x60\x60'\
b'\x60\x60\x60\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x7f\x80\x60\xc0\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1f\x80\x30\xc0\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x30\xc0\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x7f\x80\x60\xc0\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\xc0\x7f\x80\x60\x00\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x1f\xe0\x30\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x30\x60\x1f\xe0\x00\x60\x00\x60'\
b'\x00\x60\x00\x60\x00\x60\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xe0\x30\x60\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x60\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xe0\x60\x00\x60\x00'\
b'\x60\x00\x60\x00\x3f\xc0\x00\x60\x00\x60\x00\x60\x00\x60\x7f\xc0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x3f\x80\x0c\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0e\x00'\
b'\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x30\x60\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x30\xc0\x30\xc0'\
b'\x19\x80\x0f\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x60\x60\x60\x60\x60\x60\x66\x60\x66\x60\x66\x60\x66\x60'\
b'\x66\x60\x66\x60\x36\x60\x19\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x60\x60\x60\x60\x30\xc0\x19\x80\x0f\x00\x0f\x00'\
b'\x19\x80\x30\xc0\x30\xc0\x60\x60\x60\x60\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60'\
b'\x60\x60\x60\x60\x60\x60\x60\x60\x30\x60\x1f\xe0\x00\x60\x00\x60'\
b'\x00\x60\x00\xc0\x7f\x80\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xe0\x00\x60\x00\xc0\x01\x80'\
b'\x03\x00\x06\x00\x0c\x00\x18\x00\x30\x00\x60\x00\x7f\xe0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01\xe0\x03\x00'\
b'\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x0c\x00'\
b'\x38\x00\x38\x00\x0c\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x03\x00\x01\xe0\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00'\
b'\x06\x00\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x3c\x00\x06\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x01\x80\x00\xe0\x00\xe0\x01\x80\x03\x00\x03\x00\x03\x00'\
b'\x03\x00\x03\x00\x03\x00\x03\x00\x06\x00\x3c\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x38\x60\x6c\x60\xc6\xc0\xc3\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

_index =\
b'\x00\x00\x32\x00\x64\x00\x96\x00\xc8\x00\xfa\x00\x2c\x01\x5e\x01'\
b'\x90\x01\xc2\x01\xf4\x01\x26\x02\x58\x02\x8a\x02\xbc\x02\xee\x02'\
b'\x20\x03\x52\x03\x84\x03\xb6\x03\xe8\x03\x1a\x04\x4c\x04\x7e\x04'\
b'\xb0\x04\xe2\x04\x14\x05\x46\x05\x78\x05\xaa\x05\xdc\x05\x0e\x06'\
b'\x40\x06\x72\x06\xa4\x06\xd6\x06\x08\x07\x3a\x07\x6c\x07\x9e\x07'\
b'\xd0\x07\x02\x08\x34\x08\x66\x08\x98\x08\xca\x08\xfc\x08\x2e\x09'\
b'\x60\x09\x92\x09\xc4\x09\xf6\x09\x28\x0a\x5a\x0a\x8c\x0a\xbe\x0a'\
b'\xf0\x0a\x22\x0b\x54\x0b\x86\x0b\xb8\x0b\xea\x0b\x1c\x0c\x4e\x0c'\
b'\x80\x0c\xb2\x0c\xe4\x0c\x16\x0d\x48\x0d\x7a\x0d\xac\x0d\xde\x0d'\
b'\x10\x0e\x42\x0e\x74\x0e\xa6\x0e\xd8\x0e\x0a\x0f\x3c\x0f\x6e\x0f'\
b'\xa0\x0f\xd2\x0f\x04\x10\x36\x10\x68\x10\x9a\x10\xcc\x10\xfe\x10'\
b'\x30\x11\x62\x11\x94\x11\xc6\x11\xf8\x11\x2a\x12\x5c\x12\x8e\x12'\
b'\xc0\x12'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 126 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 24
    return _mvfont[doff + 2:next_offs], 24, width
 
