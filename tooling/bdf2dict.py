'''
    bsd2dict, takes two arguments; a .bdf font file and a binary file with a UTF-8
    encoded list of characters in it.

    It returns a text output with the corresponding micropython font class.

    There are two optional arguments; appending 'True' will ialso return a
    human-readable summary and ascii-art glyph maps for the font pack.
    Adding a second 'True' enables debug; displaying a lot more info, including
    raw data structures from the font, and extended data in the glyph maps.

    This is a /terrible/ script as far as structure goes.. my apologies.
    Basically it starts at the top and runs to the end, no real use of functions,
    classes or python niceities. It's also wasteful of memory and cpu cycles..
    However, it gets the job done well enough to be useful ;-)
'''
from datetime import datetime
from sys import argv, stderr
from pathlib import Path

try:
    from bdfparser import Font
except ImportError:
    print('"bdfparser" needs to be installed! exiting.\n(hint: Use a venv then "pip install bdfparser", see README.md for more)')
    exit()

if len(argv) < 3:
    print('Two arguments, the font and charset file paths, are required')
    exit(1)

font_file = argv[1]
charset = argv[2]
# You can add 'True' as a extra argument to turn glyph output on
show_glyph = argv[3] if len(argv) > 3 else False
# You can add another 'True' to turn debug on
debug = argv[4] if len(argv) > 4 else False

# extract font file name
name = Path(font_file).stem

# import the charset
with open(charset,'r') as setfile:
    cset = setfile.read()

# import font
font = Font(argv[1])
if 'fontname' not in font.headers.keys():
    stderr.write('ERROR: {}: font has no headers, nothing to output\n'.format(argv[1]))
    exit(1)
if debug:
    print('\nProcessing: {} with charset {}\n'.format(font_file, charset))

# Gather basic font data
font_name = font.headers['fontname']
font_family = None
if 'family_name' in font.props.keys():
    font_family = font.props['family_name'].lower()
font_weight = None
if 'weight_name' in font.props.keys():
    font_weight = font.props['weight_name'].lower()
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
glyph_name = {}
glyph_widest = 0

# Import and format glyph data
for fchar in font.glyphs.keys():
    # check ordinal value is in UTF range
    if fchar not in range(0,0x110000):
        continue
    # Compare to the byte array of valid chars and skip if not present
    if chr(fchar) not in cset:
        continue
    # Valid character, see if it has a glyph.
    g = font.glyphbycp(fchar)
    if len(g.meta['hexdata']) == 0:
        continue

    # If we got here, we have a glyph to process
    matches += 1

    # add to the dict
    glyph_dict[fchar] = ''
    glyph_name[fchar] = g.meta['glyphname']
    # Deep debug..
    #print(g.draw(),end='\n\n')

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

    # calculate the left edge
    start = -font_box_off_x + glyph_box_off_x - cent
    end = start + wide
    if start < 0:
        stderr.write('WARNING: Bad glyph box for char# {}\n'.format(fchar))
        start = 0

    # store width in dict, and note byte width and max width
    glyph_px[fchar] = wide
    glyph_bytes = (wide - 1) // 8 + 1
    glyph_widest = max(glyph_widest, wide)

    # get the grid as drawn by bsdparser
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
        dict_entry = '{:0{}x}'.format(int(bit_string, 2), glyph_bytes * 2)
        glyph_dict[fchar] += dict_entry

        # determine first/last lines.
        if int(dict_entry, 16) > 0:
            first[fchar] = min(first[fchar], line)
            last[fchar] = max(last[fchar], line)
        # dump the glyph data
        glyph_map += '{}{}{:<2d} {} {}\n'.format(
                        line_string,
                        ' ' * xbits,
                        line,
                        vnote,
                        dict_entry)
    if last[fchar] == 0:
        # empty char (eg space): set to a single entry @ baseline
        last[fchar] = first[fchar] = font_baseline
    if debug:
        print('Char: {} ({})'.format(fchar, glyph_name[fchar]))
        print(g.meta)
        print(glyph_map,end='')
        high = last[fchar] - first[fchar] + 1
        print('Width: {}, Lines: {}, first line: {}, last line: {}'.format(wide, high, first[fchar], last[fchar]))
        print('dict entry: {} ({} chars)'.format(glyph_dict[fchar], len(glyph_dict[fchar])))
        print()

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
    hwide = ((glyph_px[fchar] - 1) // 8 + 1) * 2
    glyph_dict[fchar] = glyph_dict[fchar][(font_first - 1) * hwide : font_last * hwide]
# adjust baseline too
font_baseline = font_baseline - font_first + 1

# Construct the output glyph dictionary
glyph_dict_string = '{\n'
for fchar in glyph_dict.keys():
    glyph_dict_string += ' {}:[{}'.format(fchar, bytes.fromhex(glyph_dict[fchar]))
    if fixed_width:
        glyph_dict_string += '],\n'
    else:
        glyph_dict_string += ',{}],\n'.format(glyph_px[fchar])
glyph_dict_string += '}'

if show_glyph or debug:
    # output font summary
    print('Font: {} ({})'.format(name, font_file))
    print('Declared name: {}'.format(font_name))
    print('Declared family: {}'.format(font_family))
    print('Declared weight: {}'.format(font_weight))
    print('Declared size: {}'.format(font_size))
    print('Matching characters: {}'.format(matches))
    print('Height: {}'.format(font_height))
    print('Baseline: {}'.format(font_baseline))
    print('Max width: {}'.format(glyph_widest))
    print('Fixed width: {}'.format(fixed_width))
    if debug:
        print('Headers:\n', font.headers)
        print('Props:\n', font.props)
    else:
        # A human-readable ascii-art glyph map
        for fchar in glyph_dict.keys():
            wide = glyph_widest if fixed_width else glyph_px[fchar]
            hwide = ((glyph_px[fchar] - 1) // 8 + 1) * 2
            print('\nChar: {} ({}), width: {}'.format(fchar, glyph_name[fchar], wide))
            for l in range(0, len(glyph_dict[fchar]), hwide):
                bs = '{:0{}b}'.format(int(glyph_dict[fchar][l:l+hwide], 16), hwide * 4)
                bt = bs.replace('0',' ').replace('1','#')[0:wide]
                bl = '_' if l  == ((font_baseline - 1) * hwide)  else '.'
                print('  {1}{0}{1}'.format(bt, bl))

    print('\n===============================================')

# Generate the Output:

# add preamble, static properties and methods

# construct a unicode string from the provided chars.
our_chars = u''.join([chr(n) for n in glyph_dict.keys()])

prelude = ('''# Code generated by bdf2dict.py
# Font: {}
# Char set: {}
# Cmd: {}
# Date: {}
''').format(name, our_chars, argv, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(prelude)

static = ('''version = '0.33'
name = '{}'
family = '{}'
weight = '{}'
size = {}
''').format(font_name, font_family, font_weight, font_size)
print(static)

def method(n,v):
    print('def {}():\n    return {}\n'.format(n,v))
method('height', font_height)
method('baseline', font_baseline)
method('max_width', glyph_widest)
method('hmap', True)
method('reverse', False)
method('monospaced', fixed_width)
method('min_ch', list(glyph_dict.keys())[0])
method('max_ch', list(glyph_dict.keys())[-1])

# This is the glyph data
print('_g = {}'.format(glyph_dict_string))

# Now the get_ch() method:
func = '''
def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), height(), {}
'''.format('max_width()' if fixed_width else '_g[c][1]')
print(func)
