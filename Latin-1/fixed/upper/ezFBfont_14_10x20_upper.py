'''
    ezFBfont_14_10x20_upper : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 10x20.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: 10x20
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/10x20.bdf', '_', './upper-char.set']
# Date: 2024-06-18 20:26:40
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain font.  Share and enjoy."
'''
version = '0.33'
name = '-misc-fixed-medium-r-normal--20-200-75-75-c-100-iso10646-1'
family = 'fixed'
weight = 'medium'
size = 20

def height():
    return 14

def baseline():
    return 13

def max_width():
    return 10

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 95

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  33:b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x0c\x00\x0c\x00\x00\x00',
  34:b'3\x003\x003\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  35:b'\x00\x00\r\x80\r\x80\r\x80?\xc0\x1b\x00\x1b\x00\x1b\x00\x7f\x806\x006\x006\x00\x00\x00\x00\x00',
  36:b'\x0c\x00?\x00m\x80l\x00l\x00l\x00?\x00\r\x80\r\x80\r\x80m\x80?\x00\x0c\x00\x00\x00',
  37:b'\x00\x009\x80m\x80o\x00;\x00\x06\x00\x06\x00\x0c\x00\x0c\x00\x1b\x80\x1e\xc06\xc03\x80\x00\x00',
  38:b'\x1c\x006\x006\x006\x00<\x00\x18\x008\x00l\x00f\xc0c\x80c\x00w\x80<\xc0\x00\x00',
  39:b'\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  40:b'\x03\x00\x06\x00\x0c\x00\x0c\x00\x18\x00\x18\x00\x18\x00\x18\x00\x18\x00\x0c\x00\x0c\x00\x06\x00\x03\x00\x00\x00',
  41:b'0\x00\x18\x00\x0c\x00\x0c\x00\x06\x00\x06\x00\x06\x00\x06\x00\x06\x00\x0c\x00\x0c\x00\x18\x000\x00\x00\x00',
  42:b'\x00\x00\x00\x00\x00\x003\x003\x00\x1e\x00\x7f\x80\x1e\x003\x003\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  43:b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  44:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x1c\x00',
  45:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x0e\x00\x00\x00',
  47:b'\x00\x00\x01\x80\x01\x80\x03\x00\x03\x00\x06\x00\x06\x00\x0c\x00\x0c\x00\x18\x00\x18\x000\x000\x00\x00\x00',
  48:b'\x0c\x00\x1e\x003\x003\x00a\x80a\x80a\x80a\x80a\x803\x003\x00\x1e\x00\x0c\x00\x00\x00',
  49:b'\x0c\x00\x1c\x00<\x00l\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80\x00\x00',
  50:b'\x1e\x003\x00a\x80a\x80\x01\x80\x01\x80\x03\x00\x0e\x00\x18\x000\x00`\x00`\x00\x7f\x80\x00\x00',
  51:b'\x1e\x003\x00a\x80a\x80\x01\x80\x03\x00\x0e\x00\x03\x00\x01\x80a\x80a\x803\x00\x1e\x00\x00\x00',
  52:b'\x01\x00\x03\x00\x07\x00\x0f\x00\x1b\x003\x00c\x00c\x00\x7f\x80\x03\x00\x03\x00\x03\x00\x03\x00\x00\x00',
  53:b'\x7f\x80`\x00`\x00`\x00`\x00n\x00s\x00\x01\x80\x01\x80\x01\x80a\x803\x00\x1e\x00\x00\x00',
  54:b'\x1e\x003\x00a\x00`\x00`\x00n\x00s\x00a\x80a\x80a\x80a\x803\x00\x1e\x00\x00\x00',
  55:b'\x7f\x80\x01\x80\x01\x80\x03\x00\x03\x00\x06\x00\x06\x00\x0c\x00\x0c\x00\x18\x00\x18\x000\x000\x00\x00\x00',
  56:b'\x1e\x003\x00a\x80a\x80a\x803\x00\x1e\x003\x00a\x80a\x80a\x803\x00\x1e\x00\x00\x00',
  57:b'\x1e\x003\x00a\x80a\x80a\x80a\x803\x80\x1d\x80\x01\x80\x01\x80!\x803\x00\x1e\x00\x00\x00',
  58:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x00\x00',
  59:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x1c\x00',
  60:b'\x01\x00\x03\x00\x06\x00\x0c\x00\x18\x000\x00`\x000\x00\x18\x00\x0c\x00\x06\x00\x03\x00\x01\x00\x00\x00',
  61:b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00',
  62:b' \x000\x00\x18\x00\x0c\x00\x06\x00\x03\x00\x01\x80\x03\x00\x06\x00\x0c\x00\x18\x000\x00 \x00\x00\x00',
  63:b'\x1e\x003\x00a\x80a\x80a\x80\x03\x00\x06\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x0c\x00\x0c\x00\x00\x00',
  64:b'\x1e\x003\x00a\x80g\x80o\x80m\x80m\x80m\x80o\x00f\x00`\x001\x80\x1f\x00\x00\x00',
  65:b'\x0c\x00\x1e\x003\x003\x00a\x80a\x80a\x80\x7f\x80a\x80a\x80a\x80a\x80a\x80\x00\x00',
  66:b'|\x00f\x00c\x00c\x00c\x00f\x00~\x00c\x00a\x80a\x80a\x80c\x00~\x00\x00\x00',
  67:b'\x1e\x003\x00a\x80`\x00`\x00`\x00`\x00`\x00`\x00`\x00a\x803\x00\x1e\x00\x00\x00',
  68:b'~\x00c\x00a\x80a\x80a\x80a\x80a\x80a\x80a\x80a\x80a\x80c\x00~\x00\x00\x00',
  69:b'\x7f\x80`\x00`\x00`\x00`\x00`\x00~\x00`\x00`\x00`\x00`\x00`\x00\x7f\x80\x00\x00',
  70:b'\x7f\x80`\x00`\x00`\x00`\x00`\x00~\x00`\x00`\x00`\x00`\x00`\x00`\x00\x00\x00',
  71:b'\x1e\x003\x00a\x80`\x00`\x00`\x00g\x80a\x80a\x80a\x80a\x803\x80\x1e\x80\x00\x00',
  72:b'a\x80a\x80a\x80a\x80a\x80a\x80\x7f\x80a\x80a\x80a\x80a\x80a\x80a\x80\x00\x00',
  73:b'\x7f\x80\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x7f\x80\x00\x00',
  74:b'\x0f\xc0\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00c\x00c\x006\x00\x1c\x00\x00\x00',
  75:b'a\x80a\x80c\x00c\x00f\x00f\x00|\x00f\x00f\x00c\x00c\x00a\x80a\x80\x00\x00',
  76:b'`\x00`\x00`\x00`\x00`\x00`\x00`\x00`\x00`\x00`\x00`\x00`\x00\x7f\x80\x00\x00',
  77:b'a\x80a\x80s\x80s\x80\x7f\x80m\x80m\x80m\x80m\x80a\x80a\x80a\x80a\x80\x00\x00',
  78:b'a\x80q\x80q\x80y\x80y\x80m\x80m\x80g\x80g\x80c\x80c\x80a\x80a\x80\x00\x00',
  79:b'\x1e\x003\x00a\x80a\x80a\x80a\x80a\x80a\x80a\x80a\x80a\x803\x00\x1e\x00\x00\x00',
  80:b'~\x00c\x00a\x80a\x80a\x80a\x80c\x00~\x00`\x00`\x00`\x00`\x00`\x00\x00\x00',
  81:b'\x1e\x003\x00a\x80a\x80a\x80a\x80a\x80a\x80a\x80m\x80g\x803\x00\x1f\x00\x01\x80',
  82:b'~\x00c\x00a\x80a\x80a\x80a\x80c\x00~\x00f\x00c\x00c\x00a\x80a\x80\x00\x00',
  83:b'\x1e\x003\x00a\x80`\x00`\x000\x00\x1e\x00\x03\x00\x01\x80\x01\x80a\x803\x00\x1e\x00\x00\x00',
  84:b'\x7f\x80\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00',
  85:b'a\x80a\x80a\x80a\x80a\x80a\x80a\x80a\x80a\x80a\x80a\x803\x00\x1e\x00\x00\x00',
  86:b'a\x80a\x80a\x80a\x803\x003\x003\x00\x1e\x00\x1e\x00\x1e\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00',
  87:b'a\x80a\x80a\x80a\x80a\x80m\x80m\x80m\x80m\x80s\x80s\x80a\x80a\x80\x00\x00',
  88:b'a\x80a\x803\x003\x00\x1e\x00\x1e\x00\x0c\x00\x1e\x00\x1e\x003\x003\x00a\x80a\x80\x00\x00',
  89:b'a\x80a\x803\x003\x00\x1e\x00\x1e\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00',
  90:b'\x7f\x80\x01\x80\x01\x80\x03\x00\x06\x00\x06\x00\x0c\x00\x18\x00\x18\x000\x00`\x00`\x00\x7f\x80\x00\x00',
  91:b'?\x000\x000\x000\x000\x000\x000\x000\x000\x000\x000\x000\x00?\x00\x00\x00',
  92:b'\x00\x000\x000\x00\x18\x00\x18\x00\x0c\x00\x0c\x00\x06\x00\x06\x00\x03\x00\x03\x00\x01\x80\x01\x80\x00\x00',
  93:b'?\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00?\x00\x00\x00',
  94:b'\x0c\x00\x1e\x003\x00a\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  95:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xc0',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 14, 10
