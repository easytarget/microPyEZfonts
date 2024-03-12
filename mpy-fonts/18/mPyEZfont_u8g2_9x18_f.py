'''
    mPyEZfont_u8g2_9x18_f.py : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    Original 9x18.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

    This font definition can be used with the "writer" class from Peter Hinches
      micropython font-to-py tool, and was generated using his tooling from
      https://github.com/peterhinch/micropython-font-to-py

    Original Copyright Notice from source:

    COPYRIGHT "Public domain font.  Share and enjoy."

    Original Comments from source (may include copyright info):

    None found:
'''

# Code generated by font_to_py.py.
# Font: 9x18.bdf Char set:  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
# Cmd: micropython-font-to-py/font_to_py.py -x -k mpy-fonts/f-char.set u8g2/tools/font/bdf/9x18.bdf 0 tmp_mPyEZfont_u8g2_9x18_f.py
version = '0.33'

def height():
    return 18

def baseline():
    return 14

def max_width():
    return 9

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 255

_font =\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x22\x00\x41\x00'\
b'\x01\x00\x02\x00\x04\x00\x08\x00\x08\x00\x00\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00\x08\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x12\x00\x12\x00\x12\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x24\x00\x24\x00\x24\x00'\
b'\xff\x00\x24\x00\x24\x00\xff\x00\x24\x00\x24\x00\x24\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x3e\x00\x49\x00\x48\x00\x28\x00\x1c\x00\x0a\x00'\
b'\x09\x00\x49\x00\x3e\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x21\x00\x52\x00\x52\x00'\
b'\x24\x00\x08\x00\x08\x00\x12\x00\x25\x00\x25\x00\x42\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x30\x00\x48\x00\x48\x00\x48\x00\x30\x00\x31\x00\x4a\x00'\
b'\x44\x00\x4a\x00\x31\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x08\x00\x08\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00'\
b'\x10\x00\x08\x00\x08\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x10\x00\x08\x00\x08\x00\x04\x00'\
b'\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x08\x00\x08\x00\x10\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x49\x00\x2a\x00\x1c\x00\x2a\x00\x49\x00\x08\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'\
b'\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x0c\x00\x04\x00\x08\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x02\x00'\
b'\x04\x00\x08\x00\x08\x00\x10\x00\x20\x00\x20\x00\x40\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1c\x00\x22\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x22\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x18\x00\x28\x00'\
b'\x48\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1c\x00\x22\x00\x41\x00\x01\x00\x02\x00\x04\x00\x08\x00'\
b'\x10\x00\x20\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x01\x00\x02\x00'\
b'\x04\x00\x0c\x00\x02\x00\x01\x00\x01\x00\x42\x00\x3c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x02\x00\x06\x00\x0a\x00\x12\x00\x22\x00\x42\x00\x7f\x00'\
b'\x02\x00\x02\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x40\x00\x40\x00'\
b'\x40\x00\x7c\x00\x02\x00\x01\x00\x01\x00\x42\x00\x3c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1e\x00\x20\x00\x40\x00\x40\x00\x5c\x00\x62\x00\x41\x00'\
b'\x41\x00\x22\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x01\x00\x02\x00'\
b'\x02\x00\x04\x00\x04\x00\x08\x00\x08\x00\x08\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1c\x00\x22\x00\x41\x00\x22\x00\x1c\x00\x22\x00\x41\x00'\
b'\x41\x00\x22\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x22\x00\x41\x00'\
b'\x41\x00\x23\x00\x1d\x00\x01\x00\x01\x00\x02\x00\x3c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x04\x00'\
b'\x08\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x02\x00\x04\x00\x08\x00\x10\x00\x20\x00\x10\x00'\
b'\x08\x00\x04\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7f\x00\x00\x00\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x20\x00\x10\x00\x08\x00\x04\x00\x02\x00\x04\x00'\
b'\x08\x00\x10\x00\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x22\x00\x41\x00'\
b'\x01\x00\x02\x00\x04\x00\x08\x00\x08\x00\x00\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1c\x00\x22\x00\x4d\x00\x55\x00\x55\x00\x55\x00\x55\x00'\
b'\x4e\x00\x20\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x14\x00'\
b'\x14\x00\x22\x00\x3e\x00\x22\x00\x41\x00\x41\x00\x41\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7c\x00\x42\x00\x41\x00\x42\x00\x7c\x00\x42\x00\x41\x00'\
b'\x41\x00\x42\x00\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x21\x00\x40\x00'\
b'\x40\x00\x40\x00\x40\x00\x40\x00\x40\x00\x21\x00\x1e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7c\x00\x42\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x42\x00\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x40\x00\x40\x00'\
b'\x40\x00\x7c\x00\x40\x00\x40\x00\x40\x00\x40\x00\x7f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7f\x00\x40\x00\x40\x00\x40\x00\x7c\x00\x40\x00\x40\x00'\
b'\x40\x00\x40\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x22\x00\x41\x00'\
b'\x40\x00\x40\x00\x47\x00\x41\x00\x41\x00\x22\x00\x1c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x41\x00\x41\x00\x41\x00\x41\x00\x7f\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3e\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1f\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00'\
b'\x44\x00\x44\x00\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x41\x00\x42\x00\x44\x00'\
b'\x48\x00\x50\x00\x68\x00\x44\x00\x42\x00\x41\x00\x41\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x40\x00\x40\x00\x40\x00\x40\x00\x40\x00\x40\x00\x40\x00'\
b'\x40\x00\x40\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x41\x00\x41\x00\x63\x00'\
b'\x55\x00\x49\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x41\x00\x41\x00\x61\x00\x51\x00\x49\x00\x45\x00\x43\x00'\
b'\x41\x00\x41\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3e\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7c\x00\x42\x00\x41\x00\x41\x00\x42\x00\x7c\x00\x40\x00'\
b'\x40\x00\x40\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x22\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x41\x00\x45\x00\x22\x00\x1d\x00\x00\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7c\x00\x42\x00\x41\x00\x41\x00\x42\x00\x7c\x00\x48\x00'\
b'\x44\x00\x42\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3e\x00\x41\x00\x40\x00'\
b'\x40\x00\x3e\x00\x01\x00\x01\x00\x01\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7f\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x22\x00\x1c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x41\x00\x41\x00\x41\x00\x22\x00\x22\x00\x22\x00\x14\x00'\
b'\x14\x00\x14\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x49\x00\x49\x00\x49\x00\x49\x00\x55\x00\x22\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x41\x00\x41\x00\x22\x00\x14\x00\x08\x00\x08\x00\x14\x00'\
b'\x22\x00\x41\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x41\x00\x41\x00\x22\x00'\
b'\x14\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7f\x00\x01\x00\x02\x00\x04\x00\x08\x00\x10\x00\x20\x00'\
b'\x40\x00\x40\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x10\x00\x10\x00\x10\x00'\
b'\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x1e\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x40\x00\x20\x00\x20\x00\x10\x00\x08\x00\x08\x00\x04\x00'\
b'\x02\x00\x02\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x04\x00\x04\x00\x04\x00'\
b'\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x3c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x14\x00\x22\x00\x41\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x10\x00\x08\x00'\
b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x3e\x00\x01\x00\x01\x00\x3f\x00\x41\x00\x43\x00\x3d\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x40\x00\x40\x00\x40\x00\x5e\x00\x61\x00\x41\x00\x41\x00'\
b'\x41\x00\x61\x00\x5e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x3e\x00\x41\x00\x40\x00\x40\x00\x40\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x01\x00\x01\x00\x01\x00\x3d\x00\x43\x00\x41\x00\x41\x00'\
b'\x41\x00\x43\x00\x3d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x3e\x00\x41\x00\x41\x00\x7f\x00\x40\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0e\x00\x11\x00\x11\x00\x10\x00\x10\x00\x7c\x00\x10\x00'\
b'\x10\x00\x10\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x3d\x00\x42\x00\x42\x00\x42\x00\x3c\x00\x40\x00\x3e\x00\x41\x00'\
b'\x41\x00\x3e\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x40\x00\x40\x00\x40\x00\x5e\x00\x61\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00'\
b'\x38\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x06\x00\x00\x00\x00\x00\x0e\x00\x02\x00\x02\x00\x02\x00'\
b'\x02\x00\x02\x00\x02\x00\x22\x00\x22\x00\x1c\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x40\x00\x40\x00'\
b'\x42\x00\x44\x00\x48\x00\x58\x00\x64\x00\x42\x00\x41\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x38\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x76\x00\x49\x00\x49\x00\x49\x00\x49\x00\x49\x00\x41\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x5e\x00\x61\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x3e\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x5c\x00\x62\x00\x41\x00\x41\x00'\
b'\x41\x00\x62\x00\x5c\x00\x40\x00\x40\x00\x40\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x1d\x00\x23\x00\x41\x00\x41\x00\x41\x00\x23\x00\x1d\x00\x01\x00'\
b'\x01\x00\x01\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x4e\x00\x31\x00\x21\x00\x20\x00'\
b'\x20\x00\x20\x00\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x3e\x00\x41\x00\x40\x00\x3e\x00\x01\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x10\x00\x10\x00\x7e\x00\x10\x00\x10\x00\x10\x00'\
b'\x10\x00\x11\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x43\x00\x3d\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x41\x00\x41\x00\x22\x00\x22\x00'\
b'\x14\x00\x14\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x41\x00\x41\x00\x49\x00\x49\x00\x49\x00\x55\x00\x22\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x41\x00\x22\x00\x14\x00\x08\x00'\
b'\x14\x00\x22\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x21\x00\x21\x00\x12\x00\x12\x00\x12\x00\x0c\x00\x0c\x00\x08\x00'\
b'\x48\x00\x30\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x02\x00\x04\x00\x08\x00'\
b'\x10\x00\x20\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x07\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x30\x00\x08\x00\x08\x00\x08\x00\x08\x00\x07\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x70\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x06\x00\x08\x00\x08\x00\x08\x00\x08\x00\x70\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x31\x00\x49\x00\x46\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x00\x00\x00\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x04\x00\x3c\x00\x4a\x00\x48\x00\x50\x00'\
b'\x52\x00\x3c\x00\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x11\x00\x10\x00'\
b'\x10\x00\x7c\x00\x10\x00\x10\x00\x30\x00\x51\x00\x2e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x41\x00\x3e\x00\x22\x00\x22\x00\x3e\x00\x41\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x41\x00\x41\x00\x22\x00'\
b'\x14\x00\x3e\x00\x08\x00\x3e\x00\x08\x00\x08\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x00\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x24\x00\x20\x00'\
b'\x18\x00\x24\x00\x24\x00\x24\x00\x18\x00\x04\x00\x24\x00\x18\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x14\x00\x14\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x42\x00\x99\x00'\
b'\xa5\x00\xa1\x00\xa5\x00\x99\x00\x42\x00\x3c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x30\x00\x48\x00\x38\x00\x48\x00\x3c\x00\x00\x00\x7c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x12\x00'\
b'\x24\x00\x48\x00\x48\x00\x24\x00\x12\x00\x09\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7e\x00\x02\x00\x02\x00'\
b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x42\x00\xb9\x00'\
b'\xa5\x00\xbd\x00\xa9\x00\xa5\x00\x42\x00\x3c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x7e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x12\x00\x12\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x08\x00\x08\x00\x7f\x00\x08\x00\x08\x00\x08\x00'\
b'\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30\x00\x48\x00\x08\x00'\
b'\x30\x00\x40\x00\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x30\x00\x48\x00\x10\x00\x08\x00\x48\x00\x30\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x04\x00\x08\x00\x10\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x41\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x63\x00\x5d\x00\x40\x00\x40\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\x00\x45\x00\x45\x00'\
b'\x45\x00\x3d\x00\x05\x00\x05\x00\x05\x00\x05\x00\x05\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'\
b'\x24\x00\x18\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x20\x00\x60\x00\x20\x00\x20\x00\x20\x00\x70\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x00\x44\x00\x44\x00'\
b'\x38\x00\x00\x00\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x48\x00\x24\x00\x12\x00\x09\x00\x09\x00\x12\x00'\
b'\x24\x00\x48\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x60\x00\x20\x00'\
b'\x20\x00\x21\x00\x73\x00\x05\x00\x09\x00\x0d\x00\x03\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x20\x00\x60\x00\x20\x00\x20\x00\x26\x00\x79\x00\x01\x00'\
b'\x06\x00\x08\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30\x00\x48\x00\x10\x00'\
b'\x08\x00\x49\x00\x33\x00\x05\x00\x09\x00\x0d\x00\x03\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x00\x00\x08\x00\x08\x00\x10\x00\x20\x00\x40\x00'\
b'\x41\x00\x41\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x10\x00\x08\x00\x04\x00\x00\x00\x08\x00\x14\x00\x14\x00'\
b'\x14\x00\x22\x00\x3e\x00\x22\x00\x41\x00\x41\x00\x41\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x04\x00\x08\x00\x10\x00'\
b'\x00\x00\x08\x00\x14\x00\x14\x00\x14\x00\x22\x00\x3e\x00\x22\x00'\
b'\x41\x00\x41\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x08\x00\x14\x00\x22\x00\x00\x00\x08\x00\x14\x00\x14\x00'\
b'\x14\x00\x22\x00\x3e\x00\x22\x00\x41\x00\x41\x00\x41\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x1a\x00\x2c\x00'\
b'\x00\x00\x08\x00\x14\x00\x14\x00\x14\x00\x22\x00\x3e\x00\x22\x00'\
b'\x41\x00\x41\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x14\x00\x14\x00\x00\x00\x08\x00\x14\x00\x14\x00'\
b'\x14\x00\x22\x00\x3e\x00\x22\x00\x41\x00\x41\x00\x41\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x08\x00\x14\x00\x14\x00'\
b'\x08\x00\x08\x00\x14\x00\x14\x00\x14\x00\x22\x00\x3e\x00\x22\x00'\
b'\x41\x00\x41\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x14\x00\x14\x00'\
b'\x14\x00\x27\x00\x3c\x00\x24\x00\x44\x00\x44\x00\x47\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1e\x00\x21\x00\x40\x00\x40\x00\x40\x00\x40\x00\x40\x00'\
b'\x40\x00\x21\x00\x1e\x00\x04\x00\x12\x00\x0c\x00\x00\x00\x00\x00'\
b'\x09\x00\x10\x00\x08\x00\x04\x00\x00\x00\x7f\x00\x40\x00\x40\x00'\
b'\x40\x00\x7c\x00\x40\x00\x40\x00\x40\x00\x40\x00\x7f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x04\x00\x08\x00\x10\x00'\
b'\x00\x00\x7f\x00\x40\x00\x40\x00\x40\x00\x7c\x00\x40\x00\x40\x00'\
b'\x40\x00\x40\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x08\x00\x14\x00\x22\x00\x00\x00\x7f\x00\x40\x00\x40\x00'\
b'\x40\x00\x7c\x00\x40\x00\x40\x00\x40\x00\x40\x00\x7f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x14\x00\x14\x00'\
b'\x00\x00\x7f\x00\x40\x00\x40\x00\x40\x00\x7c\x00\x40\x00\x40\x00'\
b'\x40\x00\x40\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x10\x00\x08\x00\x04\x00\x00\x00\x3e\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x04\x00\x08\x00\x10\x00'\
b'\x00\x00\x3e\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x08\x00\x14\x00\x22\x00\x00\x00\x3e\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x14\x00\x14\x00'\
b'\x00\x00\x3e\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x22\x00\x21\x00'\
b'\x21\x00\x79\x00\x21\x00\x21\x00\x21\x00\x22\x00\x3c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x1a\x00\x2c\x00'\
b'\x00\x00\x41\x00\x41\x00\x61\x00\x51\x00\x49\x00\x45\x00\x43\x00'\
b'\x41\x00\x41\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x10\x00\x08\x00\x04\x00\x00\x00\x3e\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x04\x00\x08\x00\x10\x00'\
b'\x00\x00\x3e\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x08\x00\x14\x00\x22\x00\x00\x00\x3e\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x1a\x00\x2c\x00'\
b'\x00\x00\x3e\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x14\x00\x14\x00\x00\x00\x3e\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x41\x00\x22\x00\x14\x00\x08\x00\x14\x00'\
b'\x22\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x01\x00\x3e\x00\x43\x00\x45\x00'\
b'\x45\x00\x49\x00\x49\x00\x51\x00\x51\x00\x61\x00\x3e\x00\x40\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x10\x00\x08\x00\x04\x00'\
b'\x00\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x22\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x04\x00\x08\x00\x10\x00\x00\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x22\x00\x1c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x08\x00\x14\x00\x22\x00'\
b'\x00\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x22\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x14\x00\x14\x00\x00\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x22\x00\x1c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x04\x00\x08\x00\x10\x00'\
b'\x00\x00\x41\x00\x41\x00\x22\x00\x14\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x40\x00\x7e\x00'\
b'\x41\x00\x41\x00\x41\x00\x7e\x00\x40\x00\x40\x00\x40\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1c\x00\x22\x00\x22\x00\x24\x00\x68\x00\x24\x00\x22\x00'\
b'\x22\x00\x22\x00\x2c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x10\x00\x08\x00\x04\x00\x00\x00'\
b'\x3e\x00\x01\x00\x01\x00\x3f\x00\x41\x00\x43\x00\x3d\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x08\x00\x10\x00\x00\x00\x3e\x00\x01\x00\x01\x00\x3f\x00'\
b'\x41\x00\x43\x00\x3d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x22\x00\x00\x00'\
b'\x3e\x00\x01\x00\x01\x00\x3f\x00\x41\x00\x43\x00\x3d\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1a\x00\x2c\x00\x00\x00\x3e\x00\x01\x00\x01\x00\x3f\x00'\
b'\x41\x00\x43\x00\x3d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x14\x00\x00\x00'\
b'\x3e\x00\x01\x00\x01\x00\x3f\x00\x41\x00\x43\x00\x3d\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x08\x00'\
b'\x14\x00\x14\x00\x08\x00\x00\x00\x3e\x00\x01\x00\x01\x00\x3f\x00'\
b'\x41\x00\x43\x00\x3d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x36\x00\x09\x00\x09\x00\x3f\x00\x48\x00\x49\x00\x36\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3e\x00\x41\x00\x40\x00\x40\x00'\
b'\x40\x00\x41\x00\x3e\x00\x08\x00\x24\x00\x18\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x10\x00\x08\x00\x04\x00\x00\x00'\
b'\x3e\x00\x41\x00\x41\x00\x7f\x00\x40\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x08\x00\x10\x00\x00\x00\x3e\x00\x41\x00\x41\x00\x7f\x00'\
b'\x40\x00\x41\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x22\x00\x00\x00'\
b'\x3e\x00\x41\x00\x41\x00\x7f\x00\x40\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x14\x00\x14\x00\x00\x00\x3e\x00\x41\x00\x41\x00\x7f\x00'\
b'\x40\x00\x41\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x20\x00\x10\x00\x08\x00\x00\x00\x00\x00'\
b'\x38\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x04\x00'\
b'\x08\x00\x10\x00\x00\x00\x00\x00\x38\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x08\x00\x14\x00\x22\x00\x00\x00\x00\x00'\
b'\x38\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x14\x00\x00\x00\x00\x00\x38\x00\x08\x00\x08\x00\x08\x00'\
b'\x08\x00\x08\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x24\x00\x18\x00\x28\x00\x04\x00'\
b'\x1e\x00\x22\x00\x41\x00\x41\x00\x41\x00\x22\x00\x1c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1a\x00\x2c\x00\x00\x00\x5e\x00\x61\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x10\x00\x08\x00\x04\x00\x00\x00'\
b'\x3e\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x08\x00\x10\x00\x00\x00\x3e\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x22\x00\x00\x00'\
b'\x3e\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1a\x00\x2c\x00\x00\x00\x3e\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x41\x00\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x14\x00\x00\x00'\
b'\x3e\x00\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x3e\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x7f\x00\x00\x00'\
b'\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00'\
b'\x3e\x00\x45\x00\x45\x00\x49\x00\x51\x00\x51\x00\x3e\x00\x40\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x20\x00\x10\x00\x08\x00\x00\x00\x41\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x43\x00\x3d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x04\x00\x08\x00\x10\x00\x00\x00'\
b'\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x43\x00\x3d\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x14\x00\x22\x00\x00\x00\x41\x00\x41\x00\x41\x00\x41\x00'\
b'\x41\x00\x43\x00\x3d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x14\x00\x00\x00'\
b'\x41\x00\x41\x00\x41\x00\x41\x00\x41\x00\x43\x00\x3d\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x02\x00\x04\x00\x08\x00\x00\x00\x21\x00\x21\x00\x12\x00\x12\x00'\
b'\x12\x00\x0c\x00\x0c\x00\x08\x00\x48\x00\x30\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x40\x00'\
b'\x5c\x00\x62\x00\x41\x00\x41\x00\x41\x00\x62\x00\x5c\x00\x40\x00'\
b'\x40\x00\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x12\x00\x12\x00\x00\x00\x21\x00\x21\x00\x12\x00\x12\x00'\
b'\x12\x00\x0c\x00\x0c\x00\x08\x00\x48\x00\x30\x00\x00\x00'

_sparse =\
b'\x20\x00\x05\x00\x21\x00\x0a\x00\x22\x00\x0f\x00\x23\x00\x14\x00'\
b'\x24\x00\x19\x00\x25\x00\x1e\x00\x26\x00\x23\x00\x27\x00\x28\x00'\
b'\x28\x00\x2d\x00\x29\x00\x32\x00\x2a\x00\x37\x00\x2b\x00\x3c\x00'\
b'\x2c\x00\x41\x00\x2d\x00\x46\x00\x2e\x00\x4b\x00\x2f\x00\x50\x00'\
b'\x30\x00\x55\x00\x31\x00\x5a\x00\x32\x00\x5f\x00\x33\x00\x64\x00'\
b'\x34\x00\x69\x00\x35\x00\x6e\x00\x36\x00\x73\x00\x37\x00\x78\x00'\
b'\x38\x00\x7d\x00\x39\x00\x82\x00\x3a\x00\x87\x00\x3b\x00\x8c\x00'\
b'\x3c\x00\x91\x00\x3d\x00\x96\x00\x3e\x00\x9b\x00\x3f\x00\xa0\x00'\
b'\x40\x00\xa5\x00\x41\x00\xaa\x00\x42\x00\xaf\x00\x43\x00\xb4\x00'\
b'\x44\x00\xb9\x00\x45\x00\xbe\x00\x46\x00\xc3\x00\x47\x00\xc8\x00'\
b'\x48\x00\xcd\x00\x49\x00\xd2\x00\x4a\x00\xd7\x00\x4b\x00\xdc\x00'\
b'\x4c\x00\xe1\x00\x4d\x00\xe6\x00\x4e\x00\xeb\x00\x4f\x00\xf0\x00'\
b'\x50\x00\xf5\x00\x51\x00\xfa\x00\x52\x00\xff\x00\x53\x00\x04\x01'\
b'\x54\x00\x09\x01\x55\x00\x0e\x01\x56\x00\x13\x01\x57\x00\x18\x01'\
b'\x58\x00\x1d\x01\x59\x00\x22\x01\x5a\x00\x27\x01\x5b\x00\x2c\x01'\
b'\x5c\x00\x31\x01\x5d\x00\x36\x01\x5e\x00\x3b\x01\x5f\x00\x40\x01'\
b'\x60\x00\x45\x01\x61\x00\x4a\x01\x62\x00\x4f\x01\x63\x00\x54\x01'\
b'\x64\x00\x59\x01\x65\x00\x5e\x01\x66\x00\x63\x01\x67\x00\x68\x01'\
b'\x68\x00\x6d\x01\x69\x00\x72\x01\x6a\x00\x77\x01\x6b\x00\x7c\x01'\
b'\x6c\x00\x81\x01\x6d\x00\x86\x01\x6e\x00\x8b\x01\x6f\x00\x90\x01'\
b'\x70\x00\x95\x01\x71\x00\x9a\x01\x72\x00\x9f\x01\x73\x00\xa4\x01'\
b'\x74\x00\xa9\x01\x75\x00\xae\x01\x76\x00\xb3\x01\x77\x00\xb8\x01'\
b'\x78\x00\xbd\x01\x79\x00\xc2\x01\x7a\x00\xc7\x01\x7b\x00\xcc\x01'\
b'\x7c\x00\xd1\x01\x7d\x00\xd6\x01\x7e\x00\xdb\x01\xa1\x00\xe0\x01'\
b'\xa2\x00\xe5\x01\xa3\x00\xea\x01\xa4\x00\xef\x01\xa5\x00\xf4\x01'\
b'\xa6\x00\xf9\x01\xa7\x00\xfe\x01\xa8\x00\x03\x02\xa9\x00\x08\x02'\
b'\xaa\x00\x0d\x02\xab\x00\x12\x02\xac\x00\x17\x02\xae\x00\x1c\x02'\
b'\xaf\x00\x21\x02\xb0\x00\x26\x02\xb1\x00\x2b\x02\xb2\x00\x30\x02'\
b'\xb3\x00\x35\x02\xb4\x00\x3a\x02\xb5\x00\x3f\x02\xb6\x00\x44\x02'\
b'\xb7\x00\x49\x02\xb8\x00\x4e\x02\xb9\x00\x53\x02\xba\x00\x58\x02'\
b'\xbb\x00\x5d\x02\xbc\x00\x62\x02\xbd\x00\x67\x02\xbe\x00\x6c\x02'\
b'\xbf\x00\x71\x02\xc0\x00\x76\x02\xc1\x00\x7b\x02\xc2\x00\x80\x02'\
b'\xc3\x00\x85\x02\xc4\x00\x8a\x02\xc5\x00\x8f\x02\xc6\x00\x94\x02'\
b'\xc7\x00\x99\x02\xc8\x00\x9e\x02\xc9\x00\xa3\x02\xca\x00\xa8\x02'\
b'\xcb\x00\xad\x02\xcc\x00\xb2\x02\xcd\x00\xb7\x02\xce\x00\xbc\x02'\
b'\xcf\x00\xc1\x02\xd0\x00\xc6\x02\xd1\x00\xcb\x02\xd2\x00\xd0\x02'\
b'\xd3\x00\xd5\x02\xd4\x00\xda\x02\xd5\x00\xdf\x02\xd6\x00\xe4\x02'\
b'\xd7\x00\xe9\x02\xd8\x00\xee\x02\xd9\x00\xf3\x02\xda\x00\xf8\x02'\
b'\xdb\x00\xfd\x02\xdc\x00\x02\x03\xdd\x00\x07\x03\xde\x00\x0c\x03'\
b'\xdf\x00\x11\x03\xe0\x00\x16\x03\xe1\x00\x1b\x03\xe2\x00\x20\x03'\
b'\xe3\x00\x25\x03\xe4\x00\x2a\x03\xe5\x00\x2f\x03\xe6\x00\x34\x03'\
b'\xe7\x00\x39\x03\xe8\x00\x3e\x03\xe9\x00\x43\x03\xea\x00\x48\x03'\
b'\xeb\x00\x4d\x03\xec\x00\x52\x03\xed\x00\x57\x03\xee\x00\x5c\x03'\
b'\xef\x00\x61\x03\xf0\x00\x66\x03\xf1\x00\x6b\x03\xf2\x00\x70\x03'\
b'\xf3\x00\x75\x03\xf4\x00\x7a\x03\xf5\x00\x7f\x03\xf6\x00\x84\x03'\
b'\xf7\x00\x89\x03\xf8\x00\x8e\x03\xf9\x00\x93\x03\xfa\x00\x98\x03'\
b'\xfb\x00\x9d\x03\xfc\x00\xa2\x03\xfd\x00\xa7\x03\xfe\x00\xac\x03'\
b'\xff\x00\xb1\x03'

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

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 18
    return _mvfont[doff + 2:next_offs], 18, width
 
