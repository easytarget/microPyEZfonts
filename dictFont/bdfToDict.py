from bdfparser import Font
from sys import argv

debug = argv[2] if len(argv) == 3 else False
if len(argv) < 2:
    print('A single argument, the font file path, is required')
    exit()

if debug:
    print('Parsing: {}'.format(argv[1]))
font = Font(argv[1])
if 'fontname' not in font.headers.keys():
    print('{}: font has no headers, failing'.format(argv[1]))
    exit(1)
print('Name: {}, Glyphs total: {}'.format(font.headers['fontname'], font.length()))
