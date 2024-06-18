'''
    ezFBfont_06_spleen_5x8_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original spleen_5x8.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: spleen_5x8
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/spleen-5x8.bdf', '_', './time-char.set']
# Date: 2024-06-18 20:27:41
'''
    Original Copyright, Comments and Notices from source:

    COPYRIGHT /*
    COPYRIGHT * Spleen 5x8 1.9.1
    COPYRIGHT * Copyright (c) 2018-2022, Frederic Cambus
    COPYRIGHT * https://www.cambus.net/
    COPYRIGHT *
    COPYRIGHT * Created:      2018-08-08
    COPYRIGHT * Last Updated: 2021-03-10
    COPYRIGHT *
    COPYRIGHT * Spleen is released under the BSD 2-Clause license.
    COPYRIGHT * See LICENSE file for details.
    COPYRIGHT *
    COPYRIGHT * SPDX-License-Identifier: BSD-2-Clause
    COPYRIGHT */

    COMMENT "Copyright (c) 2018-2022, Frederic Cambus"
'''
version = '0.33'
name = '-misc-spleen-medium-r-normal--8-80-72-72-c-50-iso10646-1'
family = 'spleen'
weight = 'medium'
size = 8

def height():
    return 6

def baseline():
    return 6

def max_width():
    return 5

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 58

_g = {
  32:b'\x00\x00\x00\x00\x00\x00',
  43:b'\x00  \xf8  ',
  45:b'\x00\x00\x00\xf0\x00\x00',
  46:b'\x00\x00\x00\x00\x00 ',
  48:b'`\x90\xb0\xd0\x90`',
  49:b' `   p',
  50:b'`\x90\x10`\x80\xf0',
  51:b'`\x90 \x10\x90`',
  52:b'\x80\xa0\xa0\xf0  ',
  53:b'\xf0\x80\xe0\x10\x10\xe0',
  54:b'`\x80\xe0\x90\x90`',
  55:b'\xf0\x90\x10 @@',
  56:b'`\x90`\x90\x90`',
  57:b'`\x90\x90p\x10`',
  58:b'\x00\x00 \x00\x00 ',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 6, 5
