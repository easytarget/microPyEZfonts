'''
    mPyEZfont_u8g2_spleen-6x12_u.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original spleen-6x12.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "Copyright (c) 2018-2022, Frederic Cambus"
    STARTCHAR COPYRIGHT SIGN

    Original Comments from source (may include copyright info):

    COMMENT /*
    COMMENT  * Spleen 6x12 1.9.1
    COMMENT  * Copyright (c) 2018-2022, Frederic Cambus
    COMMENT  * https://www.cambus.net/
    COMMENT  *
    COMMENT  * Created:      2020-04-08
    COMMENT  * Last Updated: 2021-03-12
    COMMENT  *
    COMMENT  * Spleen is released under the BSD 2-Clause license.
    COMMENT  * See LICENSE file for details.
    COMMENT  *
    COMMENT  * SPDX-License-Identifier: BSD-2-Clause
    COMMENT  */
'''

# Code generated by font_to_py.py.
# Font: spleen-6x12.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/u-char.set u8g2/tools/font/bdf/spleen-6x12.bdf 0 tmp_mPyEZfont_u8g2_spleen-6x12_u.py
version = '0.33'

def height():
    return 12

def baseline():
    return 9

def max_width():
    return 6

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
b'\x06\x00\x00\x70\x88\x08\x10\x20\x20\x00\x20\x00\x00\x00\x06\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x20'\
b'\x20\x20\x20\x20\x20\x00\x20\x00\x00\x00\x06\x00\x00\x50\x50\x50'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x50\xf8\x50\x50'\
b'\x50\xf8\x50\x00\x00\x00\x06\x00\x20\x78\xa0\xa0\x70\x28\x28\x28'\
b'\xf0\x20\x00\x00\x06\x00\x00\x08\x48\x50\x10\x20\x28\x48\x40\x00'\
b'\x00\x00\x06\x00\x00\x30\x48\x48\x30\x60\x94\x88\x74\x00\x00\x00'\
b'\x06\x00\x00\x20\x20\x20\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'\
b'\x18\x20\x40\x40\x40\x40\x40\x40\x20\x18\x00\x00\x06\x00\x60\x10'\
b'\x08\x08\x08\x08\x08\x08\x10\x60\x00\x00\x06\x00\x00\x00\x00\x48'\
b'\x30\xfc\x30\x48\x00\x00\x00\x00\x06\x00\x00\x00\x00\x20\x20\xf8'\
b'\x20\x20\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x20'\
b'\x20\x40\x00\x00\x06\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00'\
b'\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x00'\
b'\x06\x00\x08\x08\x10\x10\x20\x20\x40\x40\x80\x80\x00\x00\x06\x00'\
b'\x00\x70\x88\x98\xa8\xc8\x88\x88\x70\x00\x00\x00\x06\x00\x00\x20'\
b'\x60\x20\x20\x20\x20\x20\x70\x00\x00\x00\x06\x00\x00\x70\x88\x08'\
b'\x08\x70\x80\x80\xf8\x00\x00\x00\x06\x00\x00\x70\x88\x08\x30\x08'\
b'\x08\x88\x70\x00\x00\x00\x06\x00\x00\x80\x80\x90\x90\x90\xf8\x10'\
b'\x10\x00\x00\x00\x06\x00\x00\xf8\x80\x80\xf0\x08\x08\x08\xf0\x00'\
b'\x00\x00\x06\x00\x00\x70\x80\x80\xf0\x88\x88\x88\x70\x00\x00\x00'\
b'\x06\x00\x00\xf8\x88\x08\x10\x20\x20\x20\x20\x00\x00\x00\x06\x00'\
b'\x00\x70\x88\x88\x70\x88\x88\x88\x70\x00\x00\x00\x06\x00\x00\x70'\
b'\x88\x88\x88\x78\x08\x08\x70\x00\x00\x00\x06\x00\x00\x00\x00\x00'\
b'\x20\x00\x00\x00\x20\x00\x00\x00\x06\x00\x00\x00\x00\x00\x20\x00'\
b'\x00\x20\x20\x40\x00\x00\x06\x00\x00\x08\x10\x20\x40\x40\x20\x10'\
b'\x08\x00\x00\x00\x06\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\x00\x00'\
b'\x00\x00\x06\x00\x00\x40\x20\x10\x08\x08\x10\x20\x40\x00\x00\x00'\
b'\x06\x00\x00\x70\x88\x08\x10\x20\x20\x00\x20\x00\x00\x00\x06\x00'\
b'\x00\x70\x88\x88\xb8\xb8\xb8\x80\x78\x00\x00\x00\x06\x00\x00\x70'\
b'\x88\x88\x88\xf8\x88\x88\x88\x00\x00\x00\x06\x00\x00\xf0\x88\x88'\
b'\xf0\x88\x88\x88\xf0\x00\x00\x00\x06\x00\x00\x78\x80\x80\x80\x80'\
b'\x80\x80\x78\x00\x00\x00\x06\x00\x00\xf0\x88\x88\x88\x88\x88\x88'\
b'\xf0\x00\x00\x00\x06\x00\x00\x78\x80\x80\xf0\x80\x80\x80\x78\x00'\
b'\x00\x00\x06\x00\x00\x78\x80\x80\xf0\x80\x80\x80\x80\x00\x00\x00'\
b'\x06\x00\x00\x78\x80\x80\xb8\x88\x88\x88\x78\x00\x00\x00\x06\x00'\
b'\x00\x88\x88\x88\xf8\x88\x88\x88\x88\x00\x00\x00\x06\x00\x00\x70'\
b'\x20\x20\x20\x20\x20\x20\x70\x00\x00\x00\x06\x00\x00\x70\x20\x20'\
b'\x20\x20\x20\x20\xc0\x00\x00\x00\x06\x00\x00\x88\x88\x90\xe0\x90'\
b'\x88\x88\x88\x00\x00\x00\x06\x00\x00\x80\x80\x80\x80\x80\x80\x80'\
b'\x78\x00\x00\x00\x06\x00\x00\x88\xd8\xf8\xa8\x88\x88\x88\x88\x00'\
b'\x00\x00\x06\x00\x00\x88\xc8\xc8\xa8\xa8\x98\x98\x88\x00\x00\x00'\
b'\x06\x00\x00\x70\x88\x88\x88\x88\x88\x88\x70\x00\x00\x00\x06\x00'\
b'\x00\xf0\x88\x88\x88\xf0\x80\x80\x80\x00\x00\x00\x06\x00\x00\x70'\
b'\x88\x88\x88\x88\x88\x88\x70\x18\x00\x00\x06\x00\x00\xf0\x88\x88'\
b'\x88\xf0\x88\x88\x88\x00\x00\x00\x06\x00\x00\x78\x80\x80\x70\x08'\
b'\x08\x08\xf0\x00\x00\x00\x06\x00\x00\xf8\x20\x20\x20\x20\x20\x20'\
b'\x20\x00\x00\x00\x06\x00\x00\x88\x88\x88\x88\x88\x88\x88\x78\x00'\
b'\x00\x00\x06\x00\x00\x88\x88\x88\x88\x88\x88\x70\x70\x00\x00\x00'\
b'\x06\x00\x00\x88\x88\x88\x88\xa8\xf8\xd8\x88\x00\x00\x00\x06\x00'\
b'\x00\x88\x88\x50\x20\x50\x88\x88\x88\x00\x00\x00\x06\x00\x00\x88'\
b'\x88\x88\x88\x78\x08\x08\xf0\x00\x00\x00\x06\x00\x00\xf8\x08\x10'\
b'\x20\x40\x80\x80\xf8\x00\x00\x00\x06\x00\x78\x40\x40\x40\x40\x40'\
b'\x40\x40\x40\x78\x00\x00\x06\x00\x80\x80\x40\x40\x20\x20\x10\x10'\
b'\x08\x08\x00\x00\x06\x00\x78\x08\x08\x08\x08\x08\x08\x08\x08\x78'\
b'\x00\x00\x06\x00\x00\x20\x50\x88\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00'

_index =\
b'\x00\x00\x0e\x00\x1c\x00\x2a\x00\x38\x00\x46\x00\x54\x00\x62\x00'\
b'\x70\x00\x7e\x00\x8c\x00\x9a\x00\xa8\x00\xb6\x00\xc4\x00\xd2\x00'\
b'\xe0\x00\xee\x00\xfc\x00\x0a\x01\x18\x01\x26\x01\x34\x01\x42\x01'\
b'\x50\x01\x5e\x01\x6c\x01\x7a\x01\x88\x01\x96\x01\xa4\x01\xb2\x01'\
b'\xc0\x01\xce\x01\xdc\x01\xea\x01\xf8\x01\x06\x02\x14\x02\x22\x02'\
b'\x30\x02\x3e\x02\x4c\x02\x5a\x02\x68\x02\x76\x02\x84\x02\x92\x02'\
b'\xa0\x02\xae\x02\xbc\x02\xca\x02\xd8\x02\xe6\x02\xf4\x02\x02\x03'\
b'\x10\x03\x1e\x03\x2c\x03\x3a\x03\x48\x03\x56\x03\x64\x03\x72\x03'\
b'\x80\x03\x8e\x03'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 12
    return _mvfont[doff + 2:next_offs], 12, width
 
