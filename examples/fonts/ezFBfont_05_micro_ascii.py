'''
    ezFBfont_05_micro_ascii : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original micro.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: micro
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/micro.bdf', '_', './ascii-char.set']
# Date: 2024-06-18 16:22:57
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain font.  Share and enjoy."
'''
version = '0.33'
name = 'micro'
family = 'none'
weight = 'none'
size = None

def height():
    return 5

def baseline():
    return 5

def max_width():
    return 4

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 126

_g = {
  32:b'\x00\x00\x00\x00\x00',
  33:b'\xc0\xc0\xc0\x00\xc0',
  34:b'\xa0\xa0\x00\x00\x00',
  35:b'\xa0\xe0\xa0\xe0\xa0',
  36:b'@\xe0\xc0`\xe0',
  37:b'\xa0`\xc0\xa0\x00',
  38:b'@@\xe0\xc0@',
  39:b' `\x00\x00\x00',
  40:b' @@@ ',
  41:b'\x80@@@\x80',
  42:b'\xa0@\xe0@\xa0',
  43:b'\x00@\xe0@\x00',
  44:b'\x00\x00\x00@\xc0',
  45:b'\x00\x00\xe0\x00\x00',
  46:b'\x00\x00\x00\xc0\xc0',
  47:b'  @@\x80',
  48:b'@\xa0\xa0\xa0@',
  49:b'@\xc0@@@',
  50:b'\xc0 @\x80\xe0',
  51:b'\xc0 ` \xe0',
  52:b'\xa0\xa0\xa0\xe0 ',
  53:b'\xe0\x80\xc0 \xc0',
  54:b'`\x80\xe0\xa0\xe0',
  55:b'\xe0  @@',
  56:b'\xe0\xa0\xe0\xa0\xe0',
  57:b'\xe0\xa0\xe0 \xc0',
  58:b'\xc0\xc0\x00\xc0\xc0',
  59:b'\xc0\xc0\x00@\xc0',
  60:b' @\x80@ ',
  61:b'\x00\xe0\x00\xe0\x00',
  62:b'\x80@ @\x80',
  63:b'\xe0 `\x00@',
  64:b'`\xa0\xc0\x80`',
  65:b'\xe0\xa0\xe0\xa0\xa0',
  66:b'\xe0\xa0\xc0\xa0\xe0',
  67:b'\xe0\x80\x80\x80\xe0',
  68:b'\xc0\xa0\xa0\xa0\xc0',
  69:b'\xe0\x80\xe0\x80\xe0',
  70:b'\xe0\x80\xe0\x80\x80',
  71:b'\xe0\x80\xa0\xa0\xe0',
  72:b'\xa0\xa0\xe0\xa0\xa0',
  73:b'\xe0@@@\xe0',
  74:b'   \xa0\xe0',
  75:b'\xa0\xa0\xc0\xa0\xa0',
  76:b'\x80\x80\x80\x80\xe0',
  77:b'\xa0\xe0\xa0\xa0\xa0',
  78:b'\xe0\xa0\xa0\xa0\xa0',
  79:b'\xe0\xa0\xa0\xa0\xe0',
  80:b'\xe0\xa0\xe0\x80\x80',
  81:b'\xe0\xa0\xa0\xc0`',
  82:b'\xe0\xa0\xc0\xa0\xa0',
  83:b'\xe0\x80\xe0 \xe0',
  84:b'\xe0@@@@',
  85:b'\xa0\xa0\xa0\xa0\xe0',
  86:b'\xa0\xa0\xa0\xa0@',
  87:b'\xa0\xa0\xa0\xe0\xa0',
  88:b'\xa0\xe0@\xe0\xa0',
  89:b'\xa0\xa0\xe0@@',
  90:b'\xe0 @\x80\xe0',
  91:b'`@@@`',
  92:b'\x80\x80@@ ',
  93:b'\xc0@@@\xc0',
  94:b'@\xa0\x00\x00\x00',
  95:b'\x00\x00\x00\x00\xe0',
  96:b'@`\x00\x00\x00',
  97:b'\x00\xe0`\xa0\xe0',
  98:b'\x80\xe0\xa0\xa0\xe0',
  99:b'\x00\xe0\x80\x80\xe0',
  100:b' \xe0\xa0\xa0\xe0',
  101:b'\x00\xe0\xa0\xc0\xe0',
  102:b'`\x80\xc0\x80\x80',
  103:b'\x00\xe0\xa0`\xe0',
  104:b'\x80\xe0\xa0\xa0\xa0',
  105:b'\x00@@@@',
  106:b'\x00  \xa0\xe0',
  107:b'\x80\xa0\xc0\xc0\xa0',
  108:b'\xc0@@@@',
  109:b'\x00\xa0\xe0\xa0\xa0',
  110:b'\x00\xe0\xa0\xa0\xa0',
  111:b'\x00\xe0\xa0\xa0\xe0',
  112:b'\x00\xe0\xa0\xe0\x80',
  113:b'\x00\xe0\xa0\xe0 ',
  114:b'\x00\xe0\xa0\x80\x80',
  115:b'\x00\xe0\xc0`\xe0',
  116:b'@\xe0@@`',
  117:b'\x00\xa0\xa0\xa0\xe0',
  118:b'\x00\xa0\xa0\xa0@',
  119:b'\x00\xa0\xa0\xe0\xa0',
  120:b'\x00\xa0@@\xa0',
  121:b'\x00\xa0\xa0`\xc0',
  122:b'\x00\xe0`\xc0\xe0',
  123:b'`@\xc0@`',
  124:b'@@@@@',
  125:b'\xc0@`@\xc0',
  126:b'\x00\xc0`\x00\x00',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 5, 4
