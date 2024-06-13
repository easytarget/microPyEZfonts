'''
    ezFBfont_08_open_iconic_all_1x_upper : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_all_1x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    Original Copyright information from source:
    COPYRIGHT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"

    Original Comments and Notices from source:
    (may include copyright and trademark info):
    None found
'''
# Code generated by bdf2dict.py
# Font: open_iconic_all_1x
# Cmd: [bdf2dict.py], ['Symbols-bdf-sources/open_iconic_all_1x.bdf', '_', './upper-char.set']
# Date: 2024-06-13 11:38:11

version = '0.33'
name = '"open_iconic_all_1x"'
family = 'None'
weight = 'None'
size = None

def height():
    return 8

def baseline():
    return 8

def max_width():
    return 8

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 192

def max_ch():
    return 255

_g = {
 192:[b'\xff\x00\xff\x00\xff\x00?\x00'],
 193:[b'\x0e\x19\x19?~x\xe0\xe0'],
 194:[b'\x00~BBB\xe7\xff\x00'],
 195:[b'\xf0\xf0\xf4\xf4\x05=\x01\x0f'],
 196:[b'\x18p\x1cp\x1c8\x00\x10'],
 197:[b'&i\x01"D\x80\x96d'],
 198:[b'\x06\x01\x19"D\x98\x80`'],
 199:[b'\xbf\x00\xbf\x00\xbf\x00\xbf\x00'],
 200:[b'\xef\xe0\xee\x00\xef\xe0\xee\x00'],
 201:[b'\x00\x06\x1e|<\x18\x08\x00'],
 202:[b'\x18$$~~~~\x00'],
 203:[b'\x18$\x04\x04~~~~'],
 204:[b'\x02\xff\x82\x00A\xff@\x00'],
 205:[b'\x000bG\xe2F\x0c\x00'],
 206:[b'~B\x02G\xe2@B~'],
 207:[b'8D\x82\x82\x82F?\x03'],
 208:[b'\xff\x81\xb9\xa9\xb9\x97\x81\xff'],
 209:[b'<fBBf<\x18\x00'],
 210:[b'\x00ffffff\x00'],
 211:[b'\x00@p||p@\x00'],
 212:[b'\x00<~~~~<\x00'],
 213:[b'\x00\x113ww3\x11\x00'],
 214:[b'\x00\x88\xcc\xee\xee\xcc\x88\x00'],
 215:[b'\x00\xc2\xc6\xde\xde\xc6\xc2\x00'],
 216:[b'\x00\x86\xc6\xf6\xf6\xc6\x86\x00'],
 217:[b'\x00~~~~~~\x00'],
 218:[b'<<\xff\xff\xff\xff<<'],
 219:[b'\x00\xff\x00\x00\xff\x00\x00\xff'],
 220:[b'\x18\x18ZZf<\x08<'],
 221:[b'\x00\x00\x00\xff\xff\x00\x00\x00'],
 222:[b'\xff\x81\x81\x81\x81\xff\x18~'],
 223:[b'\x00`\xe0\xe0\xf0\xfe~\x18'],
 224:[b'\x10\x10\x10\xfe\x10\x10\x10\x00'],
 225:[b"\x1f?!!'\xe7\xe7\xe0"],
 226:[b'\x0c\x12"D\xa8\xb0\xc8p'],
 227:[b'\x00\x02\x00\x188p\xe0\xc0'],
 228:[b'\x04&vt!\x8b\xfb\xf8'],
 229:[b'\x18<<<\x18F\xff\xff'],
 230:[b'|DDDDD||'],
 231:[b'04\x16\xc7\xe7\xcf\x1e\x1c'],
 232:[b'|88\xfe\x10\x10\x10\x00'],
 233:[b'<~\xef\xe7\xe7\xef~<'],
 234:[b'\x18\x18\x18\xff\xff\x18\x18\x18'],
 235:[b'\x10\x10T\x92\x82\x82D8'],
 236:[b'<<\x00\xff\x81\xbd<<'],
 237:[b'\x81\xb1\x81\x99\x81\x8d\x81\x00'],
 238:[b'\x00\x100<\xefh\x00\x00'],
 239:[b'00\xfc\xfc\xff\xff\xcc\xcc'],
 240:[b'\x1c"\x02\x04\x0c\x08\x00\x08'],
 241:[b'\x1c>~\xff\xc7\x11TT'],
 242:[b'\x02\xc7j00j\xc7\x02'],
 243:[b'<C\x87\x80\x80\x80@<'],
 244:[b'\x07\x07\x07\x08\x90\xe0\xe0\xe0'],
 245:[b'\x108|\x10\x10|8\x10'],
 246:[b'\x00$f\xfff$\x00\x00'],
 247:[b'p\x18d\x1ak5\xd5\xc0'],
 248:[b'\xe0\xf8<\xce\xf67\x9b\xdb'],
 249:[b'?// >\xbe\xbe\xfe'],
 250:[b'\x04\x06?~\xc4\x80\x00\x00'],
 251:[b'\xe0\x8f\x9e\x80\x80\x84\xfc\x00'],
 252:[b'\x18\xef\x8f\x8fNN,\x18'],
 253:[b'\x02\n\n**\xaa\xaa\xaa'],
 254:[b'\x10p|\x1c\x10\x10\x10\x10'],
 255:[b', . / p '],
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), 8, 8

