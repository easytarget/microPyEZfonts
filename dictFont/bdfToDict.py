from sys import argv
try:
    from bdfparser import Font
except ImportError:
    print('bdfparser (patched) needs to be installed, use venv.')
    exit()

if len(argv) < 3:
    print('Two arguments, the font and charset file paths, are required')
    exit()

font_file = argv[1]
charset = argv[2]
# You can add 'True' as a extra argument to turn debug on
debug = argv[3] if len(argv) > 3 else False
# You can add 'True' as a extra argument to turn debug on
show_glyph = argv[4] if len(argv) > 4 else False

if debug:
    print('Parsing: {} with charset {}'.format(font_file, charset))

# import the charset
with open(charset,'rb') as setfile:
    cset = setfile.read()

# import font
font = Font(argv[1])
if 'fontname' not in font.headers.keys():
    print('{}: font has no headers, skipping'.format(argv[1]))
    exit(1)

# Gather basic font data
font_name = font.headers['fontname']
font_width = int(font.headers['fbbx'])
font_height = int(font.headers['fbby'])

# Defaults
matches = 0
maxWidth = 0
maxHeight = 0
maxDepth = 0  # ToDo; work from baseline..
fixed_width = True

# glyph data
glyph_dict = {}
width = {}
height = {}
origin = {}
box = {}

# Import and format glyph data
for fchar in font.glyphs.keys():
    # first test if we have a byte (eg, not an extended char)
    if fchar not in range(0,256):
        continue
    # Now it is safe to compare to the byte array of valid chars
    if fchar not in cset:
        continue
    # Valid character, now see if it is in font
    g = font.glyphbycp(fchar)
    if debug:
        print(g.meta)
    if len(g.meta['hexdata']) == 0:
        continue
    # If we got here, we have a glyph to process
    matches += 1
    width[fchar] = int(g.meta['bbw'])
    maxWidth = max(maxWidth, width[fchar])
    if width[fchar] != font_width:
        fixed_width = False
    height[fchar] = int(g.meta['bbh'])
    maxHeight = max(maxHeight, height[fchar])
    origin[fchar] = g.origin()
    box[fchar] = [int(g.meta['bbxoff']), int(g.meta['bbyoff'])]
    glyph_dict[fchar] = g.meta['hexdata']
    for l in range(len(glyph_dict[fchar])):
        # glyph_dict returns Hexadecimal strings; convert to int()
        glyph_dict[fchar][l] = int(glyph_dict[fchar][l],16)

# No matching characters, exit.
if matches == 0:
    print('No matches for this charset, skipping')
    exit(1)

# Generate DICT structure from glyphs
if debug:
    print('\nGlyphs: ord#, width, height, origin(x,y), box(x,y), bytes/line')
# Glyph bitmap data
glyph_dict_string = 'glyph_dict = {\n'
for c in glyph_dict.keys():
    bytesWide = (width[c] - 1) // 8 + 1
    if debug:
        print('{: 3d}: w{} h{} o{} b{} {} bytes'
          .format(c, width[c], height[c], origin[c], box[c], bytesWide))
    for l in range(len(glyph_dict[c])):
        if show_glyph:
            bintxt = '{:b}'.format(glyph_dict[c][l])
            bintxt = bintxt.replace('0','.').replace('1','#')
            binpad = '.' * ((bytesWide * 8) - len(bintxt))
            print('{}{}'.format(binpad, bintxt)[:width[c]])
    line_string = ''
    for l in glyph_dict[c]:
        line_string += '{:d},'.format(l)
    glyph_dict_string += ' {}:[{}]\n'.format(c, line_string[:-1])
glyph_dict_string += '}'
# Width table (wont be used for fixed fonts)
glyph_width = list(width.values())
glyph_width_string = 'glyph_widths = {}'.format(str(glyph_width).replace(' ',''))

print('\nFont: {}\nWidth: {}\nHeight: {}'.format(font_name, font_width, font_height))
print('Matching: {}'.format(matches))
print('Fixed Width: {}'.format(fixed_width))
print('maxWidth: {}, maxHeight: {}'.format(maxWidth, maxHeight))
print('\n{}'.format(glyph_dict_string))
if fixed_width:
    print('Length: {}'.format(len(glyph_dict_string)))
    # insert the fixed-width-writer
else:
    print('\n{}'.format(glyph_width_string))
    print('Length: {}'.format(len(glyph_dict_string) + len(glyph_width_string)))
    # insert the variable-width-writer

if debug:
    print('Headers:\n', font.headers)
    print('Props:\n', font.props)
