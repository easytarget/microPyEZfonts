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
font_weight = None
if 'weight_name' in font.props.keys():
    font_weight = font.props['weight_name']
font_size = None
if 'pixel_size' in font.props.keys():
    font_size = font.props['pixel_size']
font_box_width = int(font.headers['fbbx'])
font_box_height = int(font.headers['fbby'])
font_box_off_x = int(font.headers['fbbxoff'])
font_box_off_y = int(font.headers['fbbyoff'])
if font_box_off_y > 0:
    print(font_file, ":: BAD FONT BOX Y POSITION")
    exit()
# Find the baseline
font_base_line = font_box_height + font_box_off_y
# declared variation from baseline. (unreliable?)
font_above = int(font.props['font_ascent'])
font_below = int(font.props['font_descent'])

# Defaults
matches = 0
fixed_width = True

# glyph data
glyph_dict = {}
glyph_px = {}
glyph_top = {}

# Import and format glyph data
for fchar in font.glyphs.keys():
    # load ALL glyphs to find absolute font size
    # ... Necesscary? if not, only load if valid..
    g = font.glyphbycp(fchar)
    # Extreme debug..
    # print(g.draw(),end='\n\n')
    # Test if char is a byte (latin-1), skip if outside range
    if fchar not in range(0,256):
        continue
    # If so, compare to the byte array of valid chars and skip if not present
    if fchar not in cset:
        continue
    # Valid character, now see if it has a glyph.
    if len(g.meta['hexdata']) == 0:
        continue

    # If we got here, we have a glyph to process
    matches += 1
    # add to the dict
    glyph_dict[fchar] = []
    glyph_name = g.meta['glyphname']
    # get width data
    glyph_bit_width = int(g.meta['dwx0'])
    glyph_box_width = int(g.meta['bbw'])
    glyph_box_off_x = int(g.meta['bbxoff'])
    # start with the full glyph, so top line = 1
    glyph_top[fchar] = 1
    # check if we have a variable width font
    # TODO: do this test later by looking at widths..
    if glyph_box_width != font_box_width:
        fixed_width = False
    # define the width of glyph.
    if glyph_box_width < glyph_bit_width:
        wide = glyph_bit_width
        cent = (wide - glyph_box_width) // 2
    else:
        wide = glyph_box_width
        cent = 0
    # store width in dict, and calculate byte width
    glyph_px[fchar] = wide
    glyph_bytes = (wide - 1) // 8 + 1
    # calculate the left edge
    start = -font_box_off_x + glyph_box_off_x - cent
    end = start + wide
    if start < 0:
        #### FIX THIS (7Seg font fails here)
        print(font_file, ":: BAD GLYPH BOX for", fchar)
        start = 0
    glyph_grid = str(g.draw()).split('\n')

    glyph_map = ""
    for line in range(1, len(glyph_grid) + 1):
        line_string = glyph_grid[line - 1]
        vnote = '  '
        if line == font_base_line:
            vnote = '-O'
        # Find the section we need
        line_string = line_string[start:end]
        # Calculate how many zeros to append to match byte width
        xbits = ((glyph_bytes * 8) - len(line_string))
        # Now create an int() to store from the binary representation
        bit_string = line_string.replace('.','0').replace('#','1')
        bit_string += '0' * xbits
        dict_entry = int(bit_string, 2)
        glyph_dict[fchar].append(dict_entry)
        # dump the glyph data
        glyph_map += '{}{}{:<2d} {} {} {}\n'.format(
                        line_string,
                        ' ' * xbits,
                        line,
                        vnote,
                        bit_string,
                        dict_entry)
    if show_glyph:
        print('Char: {} ({})'.format(fchar, glyph_name))
        print(glyph_map)

# No matching characters, exit.
if matches == 0:
    print('No matches for this charset, skipping')
    exit(1)

# Scan the matched glyphs to find true top and height of charset

# Remove all empty lines from top and bottom of glyph

# Construct the output glyph dictionary
glyph_dict_string = 'glyph_dict = {\n'
for fchar in glyph_dict.keys():
    bytesWide = (glyph_px[fchar] - 1) // 8 + 1
    if False:
        print('{: 4d}:: top: {: 3d}, width: {: 3d}, {: 3d}-bit'
          .format(fchar, glyph_top[fchar], glyph_px[fchar], bytesWide * 8))
    line_string = ''
    for l in glyph_dict[fchar]:
        line_string += '{:d},'.format(l)
    glyph_dict_string += ' {}:({},[{}]'.format(fchar,
                                                  glyph_top[fchar],
                                                  line_string[:-1])
    if fixed_width:
        glyph_dict_string += ')\n'
    else:
        glyph_dict_string += ',{})\n'.format(glyph_px[fchar])
glyph_dict_string += '}'

# output font summary
print('\nFont: {} ({})'.format(name, font_file))
print('Declared: name: {}'.format(font_name))
print('Declared: family: {}'.format(font_family))
print('Declared: weight: {}'.format(font_weight))
print('Declared: size: {}'.format(font_size))
print('Matching: {}'.format(matches))
print('Fixed width: {}'.format(fixed_width))

if debug:
    print('Headers:\n', font.headers)
    print('Props:\n', font.props)

if not True:
    exit()   # turn on to avoid font.py output

# Generate the Output:
print('===============================================')
# add preamble, static methods
print('\n{}'.format(glyph_dict_string))
print('Length: {}'.format(len(glyph_dict_string)))

if fixed_width:
    pass
    # add the fixed-width-writer
else:
    pass
    # add the variable-width-writer
