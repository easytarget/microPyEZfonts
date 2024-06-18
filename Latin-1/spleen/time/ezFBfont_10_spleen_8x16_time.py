'''
    ezFBfont_10_spleen_8x16_time : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original spleen_8x16.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: spleen_8x16
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/spleen-8x16.bdf', '_', './time-char.set']
# Date: 2024-06-18 20:27:42
'''
    Original Copyright, Comments and Notices from source:

    COPYRIGHT /*
    COPYRIGHT * Spleen 8x16 1.9.1
    COPYRIGHT * Copyright (c) 2018-2022, Frederic Cambus
    COPYRIGHT * https://www.cambus.net/
    COPYRIGHT *
    COPYRIGHT * Created:      2018-08-11
    COPYRIGHT * Last Updated: 2020-10-10
    COPYRIGHT *
    COPYRIGHT * Spleen is released under the BSD 2-Clause license.
    COPYRIGHT * See LICENSE file for details.
    COPYRIGHT *
    COPYRIGHT * SPDX-License-Identifier: BSD-2-Clause
    COPYRIGHT */

    COMMENT "Copyright (c) 2018-2022, Frederic Cambus"
'''
version = '0.33'
name = '-misc-spleen-medium-r-normal--16-160-72-72-c-80-iso10646-1'
family = 'spleen'
weight = 'medium'
size = 16

def height():
    return 10

def baseline():
    return 10

def max_width():
    return 8

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
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  43:b'\x00\x00\x00\x18\x18~\x18\x18\x00\x00',
  45:b'\x00\x00\x00\x00\x00~\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\x18',
  48:b'|\xc6\xc6\xce\xde\xf6\xe6\xc6\xc6|',
  49:b'\x188xX\x18\x18\x18\x18\x18~',
  50:b'|\xc6\x06\x06\x0c\x180`\xc6\xfe',
  51:b'|\xc6\x06\x06<\x06\x06\x06\xc6|',
  52:b'\xc0\xc0\xcc\xcc\xcc\xcc\xfe\x0c\x0c\x0c',
  53:b'\xfe\xc6\xc0\xc0\xfc\x06\x06\x06\xc6|',
  54:b'|\xc6\xc0\xc0\xfc\xc6\xc6\xc6\xc6|',
  55:b'\xfe\xc6\x06\x06\x0c\x180000',
  56:b'|\xc6\xc6\xc6|\xc6\xc6\xc6\xc6|',
  57:b'|\xc6\xc6\xc6\xc6~\x06\x06\xc6|',
  58:b'\x00\x00\x00\x18\x18\x00\x00\x00\x18\x18',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 10, 8
