'''
    ezFBfont_spleen_5x8_s : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original spleen-5x8.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "Copyright (c) 2018-2022, Frederic Cambus"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
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
# Code generated by bdf2dict.py
# Font: spleen-5x8 Char set: b'\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
# Cmd: ['bdf2dict.py', 'bdf-sources/spleen-5x8.bdf', '../latin-1/s-char.set']
# Date: 2024-06-04 14:21:26

version = '0.33'
name = '-misc-spleen-medium-r-normal--8-80-72-72-C-50-ISO10646-1'
family = 'Spleen'
weight = 'Medium'
size = 8

def height():
    return 1

def baseline():
    return 1

def max_width():
    return 5

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 160

def max_ch():
    return 255

_g = {
 160:[b'\x00'],
 161:[b'\x00'],
 162:[b'\x00'],
 163:[b'\x00'],
 164:[b'\x00'],
 165:[b'\x00'],
 166:[b'\x00'],
 167:[b'\x00'],
 168:[b'\x00'],
 169:[b'\x00'],
 170:[b'\x00'],
 171:[b'\x00'],
 172:[b'\x00'],
 173:[b'\x00'],
 174:[b'\x00'],
 175:[b'\x00'],
 176:[b'\x00'],
 177:[b'\x00'],
 178:[b'\x00'],
 179:[b'\x00'],
 180:[b'\x00'],
 181:[b'\x00'],
 182:[b'\x00'],
 183:[b'\x00'],
 184:[b'\x00'],
 185:[b'\x00'],
 186:[b'\x00'],
 187:[b'\x00'],
 188:[b'\x00'],
 189:[b'\x00'],
 190:[b'\x00'],
 191:[b'\x00'],
 192:[b'\x00'],
 193:[b'\x00'],
 194:[b'\x00'],
 195:[b'\x00'],
 196:[b'\x00'],
 197:[b'\x00'],
 198:[b'\x00'],
 199:[b'\x00'],
 200:[b'\x00'],
 201:[b'\x00'],
 202:[b'\x00'],
 203:[b'\x00'],
 204:[b'\x00'],
 205:[b'\x00'],
 206:[b'\x00'],
 207:[b'\x00'],
 208:[b'\x00'],
 209:[b'\x00'],
 210:[b'\x00'],
 211:[b'\x00'],
 212:[b'\x00'],
 213:[b'\x00'],
 214:[b'\x00'],
 215:[b'\x00'],
 216:[b'\x00'],
 217:[b'\x00'],
 218:[b'\x00'],
 219:[b'\x00'],
 220:[b'\x00'],
 221:[b'\x00'],
 222:[b'\x00'],
 223:[b'\x00'],
 224:[b'\x00'],
 225:[b'\x00'],
 226:[b'\x00'],
 227:[b'\x00'],
 228:[b'\x00'],
 229:[b'\x00'],
 230:[b'\x00'],
 231:[b'\x00'],
 232:[b'\x00'],
 233:[b'\x00'],
 234:[b'\x00'],
 235:[b'\x00'],
 236:[b'\x00'],
 237:[b'\x00'],
 238:[b'\x00'],
 239:[b'\x00'],
 240:[b'\x00'],
 241:[b'\x00'],
 242:[b'\x00'],
 243:[b'\x00'],
 244:[b'\x00'],
 245:[b'\x00'],
 246:[b'\x00'],
 247:[b'\x00'],
 248:[b'\x00'],
 249:[b'\x00'],
 250:[b'\x00'],
 251:[b'\x00'],
 252:[b'\x00'],
 253:[b'\x00'],
 254:[b'\x00'],
 255:[b'\x00'],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), max_width()

