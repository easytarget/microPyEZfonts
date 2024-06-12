'''
    ezFBfont_10_spleen_6x12_num : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original spleen_6x12.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Copyright (c) 2018-2022, Frederic Cambus"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
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
# Code generated by bdf2dict.py
# Font: spleen_6x12
# Cmd: [bdf2dict.py], ['Latin-1-bdf-sources/spleen-6x12.bdf', '_', './num-char.set']
# Date: 2024-06-12 20:09:07

version = '0.33'
name = '-misc-spleen-medium-r-normal--12-120-72-72-C-60-ISO10646-1'
family = 'spleen'
weight = 'medium'
size = 12

def height():
    return 10

def baseline():
    return 9

def max_width():
    return 6

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 176

_g = {
 32:[b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 37:[b'\x00\x08HP\x10 (H@\x00'],
 40:[b'\x18 @@@@@@ \x18'],
 41:[b'`\x10\x08\x08\x08\x08\x08\x08\x10`'],
 42:[b'\x00\x00\x00H0\xfc0H\x00\x00'],
 43:[b'\x00\x00\x00  \xf8  \x00\x00'],
 44:[b'\x00\x00\x00\x00\x00\x00\x00  @'],
 45:[b'\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00'],
 46:[b'\x00\x00\x00\x00\x00\x00\x00\x00 \x00'],
 47:[b'\x08\x08\x10\x10  @@\x80\x80'],
 48:[b'\x00p\x88\x98\xa8\xc8\x88\x88p\x00'],
 49:[b'\x00 `     p\x00'],
 50:[b'\x00p\x88\x08\x08p\x80\x80\xf8\x00'],
 51:[b'\x00p\x88\x080\x08\x08\x88p\x00'],
 52:[b'\x00\x80\x80\x90\x90\x90\xf8\x10\x10\x00'],
 53:[b'\x00\xf8\x80\x80\xf0\x08\x08\x08\xf0\x00'],
 54:[b'\x00p\x80\x80\xf0\x88\x88\x88p\x00'],
 55:[b'\x00\xf8\x88\x08\x10    \x00'],
 56:[b'\x00p\x88\x88p\x88\x88\x88p\x00'],
 57:[b'\x00p\x88\x88\x88x\x08\x08p\x00'],
 58:[b'\x00\x00\x00\x00 \x00\x00\x00 \x00'],
 176:[b'\x000HH0\x00\x00\x00\x00\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 10, 6

