'''
    Dump out a (micro) python font as ascii-art glyphs.
    Takes a single argument, the name of the font file.
'''
import importlib
from sys import argv
from os import path

# Do some minimal checking to catch obvious errors
if len(argv) != 2:
    print(argv[0], ': please supply a path to one font file')
    exit()
if argv[1][-3:] != '.py':
    print(argv[0], ': file must be a python font file')
    exit()
if not path.isfile(argv[1]):
    print(argv[0], ': file not found:', argv[1])
    exit()

# import as 'font'
font = importlib.import_module(argv[1][:-3], package=None)

print('name: {}, file: {}'.format(font.__name__, argv[1]))
print('height: {}px, baseline: {}, max width: {}px'.format(font.height(), font.baseline(), font.max_width()))
print('chars from: {} to {}\n'.format(font.min_ch(), font.max_ch()))

def pix(bitchars,frame):
    print(' ' + frame, end='')
    for bit in bitchars:
        if bit == '0':
            print(' ', end='')
        elif bit == '1':
            print('*', end='')
    print(frame)

for char in range(font.min_ch(), font.max_ch() + 1):
#for char in range(48, 50):
    glyph, char_height, char_width = font.get_ch(chr(char))
    if glyph is None:
        continue  # Nothing to show, skip.
    buf = bytearray(glyph)
    if len(buf) == 0 or char_width == 0:
        continue
    print('{} : {}x{}, {} bytes:'.format(char, char_width, char_height, len(buf)))
    bwidth = int((char_width -1) / 8) + 1
    for index in range(0, char_height):
        line = ""
        for byte in range(0, bwidth):
            line += '{0:08b}'.format(buf[(index * bwidth) + byte])
        pix(line[0:char_width], '-' if index == font.baseline() - 1 else ':')
    print()
