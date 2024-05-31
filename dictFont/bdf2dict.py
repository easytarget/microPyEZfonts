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
font_baseline = font_box_height + font_box_off_y
# declared variation from baseline. (unreliable?)
font_above = int(font.props['font_ascent'])
font_below = int(font.props['font_descent'])

# Defaults
matches = 0

# glyph line limits
first = {}
last = {}

# glyph data
glyph_dict = {}
glyph_px = {}
glyph_top = {}
glyph_widest = 0

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
    # define the width of glyph.
    if glyph_box_width < glyph_bit_width:
        wide = glyph_bit_width
        cent = (wide - glyph_box_width) // 2
    else:
        wide = glyph_box_width
        cent = 0
    # store width in dict, and note byte width
    glyph_px[fchar] = wide
    glyph_bytes = (wide - 1) // 8 + 1
    glyph_widest = max(glyph_widest, wide)
    # calculate the left edge
    start = -font_box_off_x + glyph_box_off_x - cent
    end = start + wide
    if start < 0:
        #### FIX THIS (7Seg font fails here)
        print(font_file, ":: BAD GLYPH BOX for", fchar)
        start = 0
    glyph_grid = str(g.draw()).split('\n')

    # Walk the lines of the drawn glyph select and generate the correct padded
    # dict entry values for all glyph lines
    # also find first and last line numbers, plus create a preview map of the glyph
    first[fchar] = len(glyph_grid)
    last[fchar] = 0
    glyph_map = ""
    for line in range(1, len(glyph_grid) + 1):
        line_string = glyph_grid[line - 1]
        vnote = '  '
        if line == font_baseline:
            vnote = '-O'
        # Find the section we need
        line_string = line_string[start:end]
        # Calculate how many zeros need to be appended to reach the byte width
        xbits = ((glyph_bytes * 8) - len(line_string))
        # Now create an int() from that and store it in the glyphs line list
        bit_string = line_string.replace('.','0').replace('#','1')
        bit_string += '0' * xbits
        dict_entry = int(bit_string, 2)
        glyph_dict[fchar].append(dict_entry)
        # determine first/last lines.
        if dict_entry > 0:
            first[fchar] = min(first[fchar], line)
            last[fchar] = max(last[fchar], line)
        # dump the glyph data
        glyph_map += '{}{}{:<2d} {} {} {}\n'.format(
                        line_string,
                        ' ' * xbits,
                        line,
                        vnote,
                        bit_string,
                        dict_entry)
    if last[fchar] == 0:
        # empty char (eg space), set to a single entry @ baseline
        last[fchar] = first[fchar] = font_baseline
    if show_glyph:
        print('Char: {} ({})'.format(fchar, glyph_name))
        print(glyph_map,end='')
        high = last[fchar] - first[fchar] + 1
        print('Lines: {}, first line: {}, last line: {}\n'.format(high, first[fchar], last[fchar]))

# No matching characters, exit.
if matches == 0:
    print('No matches for this charset, skipping')
    exit(1)

# Scan the matched glyphs to find true top and height of charset
font_first = font_baseline
font_last = 0
fixed_width = True
for fchar in glyph_dict.keys():
    font_first = min(font_first, first[fchar])
    font_last = max(font_last, last[fchar])
    if glyph_px[fchar] != glyph_widest:
        fixed_width = False
font_height = font_last - font_first + 1

# Remove all empty lines from top and bottom of glyph
for fchar in glyph_dict.keys():
    glyph_dict[fchar] = glyph_dict[fchar][first[fchar] - 1 :last[fchar]]
    glyph_top[fchar] = first[fchar] - font_first + 1

# Construct the output glyph dictionary
glyph_dict_string = 'glyph_dict = {\n'
for fchar in glyph_dict.keys():
    line_string = ''
    for l in glyph_dict[fchar]:
        line_string += '{:d},'.format(l)
    glyph_dict_string += ' {}:({},[{}]'.format(fchar, glyph_top[fchar], line_string[:-1])
    if fixed_width:
        glyph_dict_string += ')\n'
    else:
        glyph_dict_string += ',{})\n'.format(glyph_px[fchar])
glyph_dict_string += '}'

# output font summary
print('Font: {} ({})'.format(name, font_file))
print('Declared: name: {}'.format(font_name))
print('Declared: family: {}'.format(font_family))
print('Declared: weight: {}'.format(font_weight))
print('Declared: size: {}'.format(font_size))
print('Matching: {}'.format(matches))
print('Height: {}'.format(font_height))
print('Max width: {}'.format(glyph_widest))
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

if fixed_width:
    pass
    # add the fixed-width-writer
else:
    pass
    # add the variable-width-writer
