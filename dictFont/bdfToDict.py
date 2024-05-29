from sys import argv
from pathlib import Path

try:
    from bdfparser import Font
except ImportError:
    print('bdfparser (patched) needs to be installed; hint: use a venv.')
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

# extract font file name
name = Path(font_file).stem

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
font_family = None
if 'family_name' in font.props.keys():
    font_family = font.props['family_name']
font_box_width = int(font.headers['fbbx'])
font_box_height = int(font.headers['fbby'])
font_box_off_x = int(font.headers['fbbxoff'])
font_box_off_y = int(font.headers['fbbyoff'])
# work from baseline.
font_above = int(font.props['font_ascent'])
font_below = int(font.props['font_descent'])

# Defaults
font_max_width = 0
font_max_height = 0
matches = 0
glyph_max_width = 0
glyph_max_height = 0
fixed_width = True

# glyph data
glyph_dict = {}
glyph_widths = {}

# Import and format glyph data
for fchar in font.glyphs.keys():
    # load ALL glyphs to find absolute font size
    # ... Necesscary? if not, only load if valid..
    g = font.glyphbycp(fchar)
    font_max_width = max(font_max_width, int(g.meta['bbw']))
    font_max_height = max(font_max_height, int(g.meta['bbh']))
    # Test if char is a byte (latin-1), skip if outside range
    if fchar not in range(0,256):
        continue
    # If so, compare to the byte array of valid chars and skip if not present
    if fchar not in cset:
        continue
    # Valid character, now see if it has a glyph.
    if len(g.meta['hexdata']) == 0:
        continue
    # If we got here, we have a glyph to process, add to the dict and lists
    matches += 1
    glyph_dict[fchar] = []
    glyph_bit_width = int(g.meta['dwx0'])
    glyph_box_width = int(g.meta['bbw'])
    glyph_box_off_x = int(g.meta['bbxoff'])
    # define the width of glyph.
    if glyph_box_width < glyph_bit_width:
        wide = glyph_bit_width
        cent = (wide - int(g.meta['bbw'])) // 2
    else:
        wide = int(g.meta['bbw'])
        cent = 0
    glyph_widths[fchar] = wide
    # calculate the left edge
    start = -font_box_off_x + glyph_box_off_x - cent
    end = start + wide
    if start < 0:
        print(font_file, ":: BAD GLYPH BOX")
        exit()
    if debug:
        print(g.meta)
        #print('center: {}; start: {}, wide: {}, end: {}'.format(cent, start, wide, end))
        print(' ' * cent + '=' * glyph_box_width)
        #####################
        for line in str(g.draw()).split('\n'):
            line_string = line[start:end].replace('.','0').replace('#','1')
            glyph_dict[fchar].append(int(line_string,2))
            print(line_string, glyph_dict[fchar])
        #####################
    glyph_max_width = max(glyph_max_width, glyph_box_width)
    if glyph_box_width != font_box_width:
        fixed_width = False
    glyph_max_height = max(glyph_max_height, int(g.meta['bbh']))
    glyph_dict[fchar] = g.meta['hexdata']
    for l in range(len(glyph_dict[fchar])):
        # THIS NEEDS TO BE COMBINED WITH LINE STUFF ABOVE
        #####################
        glyph_dict[fchar][l] = int(glyph_dict[fchar][l],16)
        #####################

# No matching characters, exit.
if matches == 0:
    print('No matches for this charset, skipping')
    exit(1)

# Generate DICT structure from glyphs
if debug:
    print('\nGlyphs')
# Glyph bitmap data
glyph_dict_string = 'glyph_dict = {\n'
for fchar in glyph_dict.keys():
    bytesWide = (glyph_widths[fchar] - 1) // 8 + 1
    if debug:
        print('{: 3d}: width: {}, {}bits'
          .format(fchar, glyph_widths[fchar], bytesWide * 8))
    line_string = ''
    for l in glyph_dict[fchar]:
        line_string += '{:d},'.format(l)
    glyph_dict_string += ' {}:[{}]\n'.format(fchar, line_string[:-1])
glyph_dict_string += '}'
# generate width list (wont be used for fixed fonts)
glyph_width = list(glyph_widths.values())
glyph_width_string = 'glyph_widths = {}'.format(str(glyph_width).replace(' ',''))

print('-\nFont: {}'.format(name))
print('Declared: name: {}, family: {}'.format(font_name, font_family))
print('Declared: box width: {}, Height: {}'.format(font_box_width, font_box_height))
print('Declared: offset: x:{} y:{}'.format(font_box_off_x, font_box_off_y))
print('Declared: above / below baseline: {}, {}'.format(font_above, font_below))
print('Discovered: max width: {}, max height: {}'.format(font_max_width, font_max_height))

print('Matching: {}'.format(matches))
print('Matching: max width: {}, max height: {}'.format(glyph_max_width, glyph_max_height))
print('Fixed width: {}'.format(fixed_width))

if debug:
    print('Headers:\n', font.headers)
    print('Props:\n', font.props)

if True:
    exit()   # turn on to avoid font.py output

# Generate the Output:
print('===============================================')
# add preamble, static methods
print('\n{}'.format(glyph_dict_string))
if fixed_width:
    print('Length: {}'.format(len(glyph_dict_string)))
    # add the fixed-width-writer
else:
    print('\n{}'.format(glyph_width_string))
    print('Length: {}'.format(len(glyph_dict_string) + len(glyph_width_string)))
    # add the variable-width-writer
