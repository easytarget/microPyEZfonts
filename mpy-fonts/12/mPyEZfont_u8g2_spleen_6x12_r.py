'''
    mPyEZfont_u8g2_spleen_6x12_r.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original spleen-6x12.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "Copyright (c) 2018-2022, Frederic Cambus"

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
# Font: spleen-6x12.bdf
# Cmd: ../micropython-font-to-py/font_to_py.py -x -l 127 -e 32 ../u8g2/tools/font/bdf/spleen-6x12.bdf 0 tmp_mPyEZfont_u8g2_spleen_6x12_r.py
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
    return 127

_font =\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x20\x20\x20\x20\x20\x20\x00\x20\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x50\x50\x50\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x50\xf8\x50\x50\x50\xf8\x50\x00\x00\x00\x00\x00'\
b'\x06\x00\x20\x78\xa0\xa0\x70\x28\x28\x28\xf0\x20\x00\x00\x00\x00'\
b'\x06\x00\x00\x08\x48\x50\x10\x20\x28\x48\x40\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x30\x48\x48\x30\x60\x94\x88\x74\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x20\x20\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x18\x20\x40\x40\x40\x40\x40\x40\x20\x18\x00\x00\x00\x00'\
b'\x06\x00\x60\x10\x08\x08\x08\x08\x08\x08\x10\x60\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x48\x30\xfc\x30\x48\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x20\x20\xf8\x20\x20\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x20\x20\x40\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x00\x00\x00'\
b'\x06\x00\x08\x08\x10\x10\x20\x20\x40\x40\x80\x80\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x88\x98\xa8\xc8\x88\x88\x70\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x20\x60\x20\x20\x20\x20\x20\x70\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x88\x08\x08\x70\x80\x80\xf8\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x88\x08\x30\x08\x08\x88\x70\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x80\x80\x90\x90\x90\xf8\x10\x10\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\xf8\x80\x80\xf0\x08\x08\x08\xf0\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x80\x80\xf0\x88\x88\x88\x70\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\xf8\x88\x08\x10\x20\x20\x20\x20\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x88\x88\x70\x88\x88\x88\x70\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x88\x88\x88\x78\x08\x08\x70\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x20\x00\x00\x00\x20\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x20\x00\x00\x20\x20\x40\x00\x00\x00\x00'\
b'\x06\x00\x00\x08\x10\x20\x40\x40\x20\x10\x08\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x40\x20\x10\x08\x08\x10\x20\x40\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x88\x08\x10\x20\x20\x00\x20\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x88\x88\xb8\xb8\xb8\x80\x78\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x88\x88\x88\xf8\x88\x88\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\xf0\x88\x88\xf0\x88\x88\x88\xf0\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x78\x80\x80\x80\x80\x80\x80\x78\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\xf0\x88\x88\x88\x88\x88\x88\xf0\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x78\x80\x80\xf0\x80\x80\x80\x78\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x78\x80\x80\xf0\x80\x80\x80\x80\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x78\x80\x80\xb8\x88\x88\x88\x78\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x88\x88\x88\xf8\x88\x88\x88\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x20\x20\x20\x20\x20\x20\x70\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x20\x20\x20\x20\x20\x20\xc0\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x88\x88\x90\xe0\x90\x88\x88\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x80\x80\x80\x80\x80\x80\x80\x78\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x88\xd8\xf8\xa8\x88\x88\x88\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x88\xc8\xc8\xa8\xa8\x98\x98\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x88\x88\x88\x88\x88\x88\x70\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\xf0\x88\x88\x88\xf0\x80\x80\x80\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x70\x88\x88\x88\x88\x88\x88\x70\x18\x00\x00\x00\x00'\
b'\x06\x00\x00\xf0\x88\x88\x88\xf0\x88\x88\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x78\x80\x80\x70\x08\x08\x08\xf0\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\xf8\x20\x20\x20\x20\x20\x20\x20\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x88\x88\x88\x88\x88\x88\x88\x78\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x88\x88\x88\x88\x88\x88\x70\x70\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x88\x88\x88\x88\xa8\xf8\xd8\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x88\x88\x50\x20\x50\x88\x88\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x88\x88\x88\x88\x78\x08\x08\xf0\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\xf8\x08\x10\x20\x40\x80\x80\xf8\x00\x00\x00\x00\x00'\
b'\x06\x00\x78\x40\x40\x40\x40\x40\x40\x40\x40\x78\x00\x00\x00\x00'\
b'\x06\x00\x80\x80\x40\x40\x20\x20\x10\x10\x08\x08\x00\x00\x00\x00'\
b'\x06\x00\x78\x08\x08\x08\x08\x08\x08\x08\x08\x78\x00\x00\x00\x00'\
b'\x06\x00\x00\x20\x50\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00'\
b'\x06\x00\x00\x40\x20\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x70\x08\x78\x88\x88\x78\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x80\x80\xf0\x88\x88\x88\x88\xf0\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x78\x80\x80\x80\x80\x78\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x08\x08\x78\x88\x88\x88\x88\x78\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x78\x88\x88\xf8\x80\x78\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x38\x40\x40\xf0\x40\x40\x40\x40\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x78\x88\x88\x88\x88\x70\x08\xf0\x00\x00\x00'\
b'\x06\x00\x00\x80\x80\xf0\x88\x88\x88\x88\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x20\x00\x60\x20\x20\x20\x20\x30\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x10\x00\x10\x10\x10\x10\x10\x10\x60\x00\x00\x00\x00'\
b'\x06\x00\x00\x80\x80\x90\xa0\xc0\xa0\x90\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x40\x40\x40\x40\x40\x40\x40\x30\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\xf0\xa8\xa8\xa8\x88\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\xf0\x88\x88\x88\x88\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x70\x88\x88\x88\x88\x70\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\xf0\x88\x88\x88\x88\xf0\x80\x80\x80\x00\x00'\
b'\x06\x00\x00\x00\x00\x78\x88\x88\x88\x88\x78\x08\x08\x08\x00\x00'\
b'\x06\x00\x00\x00\x00\x78\x88\x80\x80\x80\x80\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x78\x80\x70\x08\x08\xf0\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x40\x40\xe0\x40\x40\x40\x40\x30\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x88\x88\x88\x88\x88\x78\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x88\x88\x88\x88\x50\x20\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x88\x88\xa8\xf8\xd8\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x88\x88\x70\x70\x88\x88\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x88\x88\x88\x88\x88\x78\x08\x08\xf0\x00\x00'\
b'\x06\x00\x00\x00\x00\xf8\x08\x10\x20\x40\xf8\x00\x00\x00\x00\x00'\
b'\x06\x00\x18\x20\x20\x20\xc0\xc0\x20\x20\x20\x18\x00\x00\x00\x00'\
b'\x06\x00\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x00\x00\x00\x00'\
b'\x06\x00\x60\x10\x10\x10\x0c\x0c\x10\x10\x10\x60\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x48\xb0\x00\x00\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

_sparse =\
b'\x20\x00\x02\x00\x21\x00\x04\x00\x22\x00\x06\x00\x23\x00\x08\x00'\
b'\x24\x00\x0a\x00\x25\x00\x0c\x00\x26\x00\x0e\x00\x27\x00\x10\x00'\
b'\x28\x00\x12\x00\x29\x00\x14\x00\x2a\x00\x16\x00\x2b\x00\x18\x00'\
b'\x2c\x00\x1a\x00\x2d\x00\x1c\x00\x2e\x00\x1e\x00\x2f\x00\x20\x00'\
b'\x30\x00\x22\x00\x31\x00\x24\x00\x32\x00\x26\x00\x33\x00\x28\x00'\
b'\x34\x00\x2a\x00\x35\x00\x2c\x00\x36\x00\x2e\x00\x37\x00\x30\x00'\
b'\x38\x00\x32\x00\x39\x00\x34\x00\x3a\x00\x36\x00\x3b\x00\x38\x00'\
b'\x3c\x00\x3a\x00\x3d\x00\x3c\x00\x3e\x00\x3e\x00\x3f\x00\x40\x00'\
b'\x40\x00\x42\x00\x41\x00\x44\x00\x42\x00\x46\x00\x43\x00\x48\x00'\
b'\x44\x00\x4a\x00\x45\x00\x4c\x00\x46\x00\x4e\x00\x47\x00\x50\x00'\
b'\x48\x00\x52\x00\x49\x00\x54\x00\x4a\x00\x56\x00\x4b\x00\x58\x00'\
b'\x4c\x00\x5a\x00\x4d\x00\x5c\x00\x4e\x00\x5e\x00\x4f\x00\x60\x00'\
b'\x50\x00\x62\x00\x51\x00\x64\x00\x52\x00\x66\x00\x53\x00\x68\x00'\
b'\x54\x00\x6a\x00\x55\x00\x6c\x00\x56\x00\x6e\x00\x57\x00\x70\x00'\
b'\x58\x00\x72\x00\x59\x00\x74\x00\x5a\x00\x76\x00\x5b\x00\x78\x00'\
b'\x5c\x00\x7a\x00\x5d\x00\x7c\x00\x5e\x00\x7e\x00\x5f\x00\x80\x00'\
b'\x60\x00\x82\x00\x61\x00\x84\x00\x62\x00\x86\x00\x63\x00\x88\x00'\
b'\x64\x00\x8a\x00\x65\x00\x8c\x00\x66\x00\x8e\x00\x67\x00\x90\x00'\
b'\x68\x00\x92\x00\x69\x00\x94\x00\x6a\x00\x96\x00\x6b\x00\x98\x00'\
b'\x6c\x00\x9a\x00\x6d\x00\x9c\x00\x6e\x00\x9e\x00\x6f\x00\xa0\x00'\
b'\x70\x00\xa2\x00\x71\x00\xa4\x00\x72\x00\xa6\x00\x73\x00\xa8\x00'\
b'\x74\x00\xaa\x00\x75\x00\xac\x00\x76\x00\xae\x00\x77\x00\xb0\x00'\
b'\x78\x00\xb2\x00\x79\x00\xb4\x00\x7a\x00\xb6\x00\x7b\x00\xb8\x00'\
b'\x7c\x00\xba\x00\x7d\x00\xbc\x00\x7e\x00\xbe\x00\x7f\x00\xc0\x00'\

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

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 12
    return _mvfont[doff + 2:next_offs], 12, width
 
