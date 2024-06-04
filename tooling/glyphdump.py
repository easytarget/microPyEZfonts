# a demo
from sys import argv
print(argv)
import font as font

print('Name: {}'.format(font.__name__))
print('height: {}px, baseline: {}, max width: {}px'.format(font.height(), font.baseline(), font.max_width()))
print('chars from: {} to {}'.format(font.min_ch(), font.max_ch()))

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
        pix(line[0:char_width], '-' if index == font.baseline() else ':')
    print()
