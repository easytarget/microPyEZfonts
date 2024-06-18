'''
    ezFBfont_12_6x13O_ascii : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 6x13O.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: 6x13O
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/6x13O.bdf', '_', './ascii-char.set']
# Date: 2024-06-18 20:26:50
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain font.  Share and enjoy."
'''
version = '0.33'
name = '-misc-fixed-medium-o-semicondensed--13-120-75-75-c-60-iso10646-1'
family = 'fixed'
weight = 'medium'
size = 13

def height():
    return 12

def baseline():
    return 10

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
    return 126

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  33:b'\x00\x10\x10\x10\x10   \x00 \x00\x00',
  34:b'\x00\x14\x14(\x00\x00\x00\x00\x00\x00\x00\x00',
  35:b'\x00\x00((|(\xf8PP\x00\x00\x00',
  36:b'\x00\x10<PP8$(\xf0 \x00\x00',
  37:b'\x00$T(\x08\x10 P\xa8\x90\x00\x00',
  38:b'\x00\x00\x10((0P\x94\x98h\x00\x00',
  39:b'\x00\x08\x08\x10\x00\x00\x00\x00\x00\x00\x00\x00',
  40:b'\x08\x10  @@@@  \x10\x00',
  41:b' \x10\x10\x08\x08\x08\x08\x10\x10 @\x00',
  42:b'\x00\x00\x10T|8|\xa8 \x00\x00\x00',
  43:b'\x00\x00\x00\x10\x10x  \x00\x00\x00\x00',
  44:b'\x00\x00\x00\x00\x00\x00\x00\x000 @\x00',
  45:b'\x00\x00\x00\x00\x00x\x00\x00\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00 p \x00',
  47:b'\x00\x04\x04\x08\x10\x10 @\x80\x80\x00\x00',
  48:b'\x00\x10(DDD\x88\x88P \x00\x00',
  49:b'\x00\x100P\x10\x10   \xf8\x00\x00',
  50:b'\x008DD\x08\x10 @\x80\xf8\x00\x00',
  51:b'\x00|\x04\x08\x108\x04\x08\x88p\x00\x00',
  52:b'\x00\x08\x08\x18((H\xf8\x10\x10\x00\x00',
  53:b'\x00|@@Xd\x04\x08\x88p\x00\x00',
  54:b'\x008D@@p\x88\x88\x88p\x00\x00',
  55:b'\x00|\x04\x08\x08\x10  @@\x00\x00',
  56:b'\x008DDDx\x88\x88\x88p\x00\x00',
  57:b'\x008DDD8\x08\x08\x88p\x00\x00',
  58:b'\x00\x00\x00\x108\x10\x00\x00 p \x00',
  59:b'\x00\x00\x00\x108\x10\x00\x000 @\x00',
  60:b'\x00\x04\x08\x10 @  \x10\x08\x00\x00',
  61:b'\x00\x00\x00\x00|\x00\x00\xf8\x00\x00\x00\x00',
  62:b'\x00@ \x10\x08\x04\x080@\x80\x00\x00',
  63:b'\x008DD\x04\x08\x10 \x00 \x00\x00',
  64:b'\x008DDX\xa8\xa8\x90\x80x\x00\x00',
  65:b'\x00\x10(DDD\xf8\x88\x88\x88\x00\x00',
  66:b'\x00x$$$8HHH\xf0\x00\x00',
  67:b'\x008D@@@\x80\x80\x88p\x00\x00',
  68:b'\x00x$$$$HHH\xf0\x00\x00',
  69:b'\x00|@@@x\x80\x80\x80\xf8\x00\x00',
  70:b'\x00|@@@x\x80\x80\x80\x80\x00\x00',
  71:b'\x008D@@@\x98\x88\x88p\x00\x00',
  72:b'\x00DDDD|\x88\x88\x88\x88\x00\x00',
  73:b'\x008\x10\x10\x10\x10   p\x00\x00',
  74:b'\x00\x1c\x08\x08\x08\x08\x10\x10\x90`\x00\x00',
  75:b'\x00DDHP`\xa0\x90\x88\x88\x00\x00',
  76:b'\x00@@@@@\x80\x80\x80\xf8\x00\x00',
  77:b'\x00DDlTT\x88\x88\x88\x88\x00\x00',
  78:b'\x00DddTT\x98\x88\x88\x88\x00\x00',
  79:b'\x008DDDD\x88\x88\x88p\x00\x00',
  80:b'\x00xDDDx\x80\x80\x80\x80\x00\x00',
  81:b'\x008DDDD\x88\x88\xa8p\x08\x00',
  82:b'\x00xDDDx\x90\x90\x88\x88\x00\x00',
  83:b'\x008D@@0\x08\x08\x88p\x00\x00',
  84:b'\x00|\x10\x10\x10\x10    \x00\x00',
  85:b'\x00DDDDD\x88\x88\x88p\x00\x00',
  86:b'\x00DDDDHHPP \x00\x00',
  87:b'\x00DDDD\xa8\xa8\xa8\xa8P\x00\x00',
  88:b'\x00DD((\x100H\x88\x88\x00\x00',
  89:b'\x00DD((\x10\x10   \x00\x00',
  90:b'\x00|\x04\x08\x08\x10 @\x80\xf8\x00\x00',
  91:b'8   @@@\x80\x80\x80\xe0\x00',
  92:b'\x00@@   \x10\x10\x08\x08\x00\x00',
  93:b'8\x08\x08\x08\x10\x10\x10   \xe0\x00',
  94:b'\x00\x10(D\x00\x00\x00\x00\x00\x00\x00\x00',
  95:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00',
  96:b'\x10\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  97:b'\x00\x00\x00\x008\x04|\x88\x98h\x00\x00',
  98:b'\x00@@@xD\x88\x88\x88\xf0\x00\x00',
  99:b'\x00\x00\x00\x008D\x80\x80\x88p\x00\x00',
  100:b'\x00\x04\x04\x04<D\x88\x88\x88x\x00\x00',
  101:b'\x00\x00\x00\x008D|\x80\x88p\x00\x00',
  102:b'\x00\x18$  x @@@\x00\x00',
  103:b'\x00\x00\x00\x008DD\x88x\x08\x88p',
  104:b'\x00   XdD\x88\x88\x88\x00\x00',
  105:b'\x00\x00\x10\x000\x10\x10  p\x00\x00',
  106:b'\x00\x00\x08\x00\x18\x08\x08\x10\x10\x90\x90`',
  107:b'\x00   HP`\xa0\x90\x88\x00\x00',
  108:b'\x00\x18\x08\x08\x10\x10\x10  p\x00\x00',
  109:b'\x00\x00\x00\x00hTT\xa8\xa8\x88\x00\x00',
  110:b'\x00\x00\x00\x00XdD\x88\x88\x88\x00\x00',
  111:b'\x00\x00\x00\x008DD\x88\x88p\x00\x00',
  112:b'\x00\x00\x00\x00xDD\x88\xf0\x80\x80\x80',
  113:b'\x00\x00\x00\x00<D\x84\x88x\x08\x10\x10',
  114:b'\x00\x00\x00\x00Xd@\x80\x80\x80\x00\x00',
  115:b'\x00\x00\x00\x008D \x10\x88p\x00\x00',
  116:b'\x00\x00\x10\x10x  @H0\x00\x00',
  117:b'\x00\x00\x00\x00DD\x88\x88\x98h\x00\x00',
  118:b'\x00\x00\x00\x00DDDHP \x00\x00',
  119:b'\x00\x00\x00\x00DDT\xa8\xa8P\x00\x00',
  120:b'\x00\x00\x00\x00D(\x10 P\x88\x00\x00',
  121:b'\x00\x00\x00\x00DD\x88\x98h\x08\x90`',
  122:b'\x00\x00\x00\x00|\x08\x10`\x80\xf8\x00\x00',
  123:b'\x18    \xc0 @@@0\x00',
  124:b'\x00\x10\x10\x10\x10\x10    \x00\x00',
  125:b'`\x10\x10\x10\x10\x0c\x10   \xc0\x00',
  126:b'\x00$TH\x00\x00\x00\x00\x00\x00\x00\x00',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 12, 6
