from datetime import datetime
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
# You can add 'True' as a extra argument to turn glyph output on
show_glyph = argv[3] if len(argv) > 3 else False
# You can add another 'True' to turn debug on
debug = argv[4] if len(argv) > 4 else False

# extract font file name
name = Path(font_file).stem

# import the charset
with open(charset,'rb') as setfile:
    cset = setfile.read()

# import font
font = Font(argv[1])
if debug or show_glyph:
    print('\nProcessing: {} with charset {}\n'.format(font_file, charset))
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
    #print(g.draw(),end='\n\n')
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
        print('INFO: Bad glyph box for char# {}'.format(fchar))
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
        dict_entry = int(bit_string, 2)
        glyph_dict[fchar].append(dict_entry)
        # determine first/last lines.
        if dict_entry > 0:
            first[fchar] = min(first[fchar], line)
            last[fchar] = max(last[fchar], line)
        # dump the glyph data
        glyph_map += '{}{}{:<2d} {} {:X}\n'.format(
                        line_string,
                        ' ' * xbits,
                        line,
                        vnote,
                        dict_entry)
    if last[fchar] == 0:
        # empty char (eg space), set to a single entry @ baseline
        last[fchar] = first[fchar] = font_baseline
    if show_glyph:
        print('Char: {} ({})'.format(fchar, glyph_name))
        if debug:
            print(g.meta)
        print(glyph_map,end='')
        high = last[fchar] - first[fchar] + 1
        print('Width: {}, Lines: {}, first line: {}, last line: {}\n'.format(wide, high, first[fchar], last[fchar]))

# No matching characters, soft exit.
if matches == 0:
    print('No matches for this charset, skipping')
    exit(0)

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

# Remove all empty lines from top and bottom of glyph, set top line position
for fchar in glyph_dict.keys():
    glyph_dict[fchar] = glyph_dict[fchar][first[fchar] - 1 :last[fchar]]
    glyph_top[fchar] = first[fchar] - font_first + 1
# adjust baseline too
font_baseline = font_baseline - font_first + 1

# Construct the output glyph dictionary
glyph_dict_string = '_g = {\n'
for fchar in glyph_dict.keys():
    line_string = ''
    for l in glyph_dict[fchar]:
        line_string += '{},'.format(l)
    glyph_dict_string += ' {}:[{},[{}]'.format(fchar, glyph_top[fchar], line_string[:-1])
    if fixed_width:
        glyph_dict_string += '],\n'
    else:
        glyph_dict_string += ',{}],\n'.format(glyph_px[fchar])
glyph_dict_string += '}'

if show_glyph or debug:
    # output font summary
    print('Font: {} ({})'.format(name, font_file))
    print('Declared: name: {}'.format(font_name))
    print('Declared: family: {}'.format(font_family))
    print('Declared: weight: {}'.format(font_weight))
    print('Declared: size: {}'.format(font_size))
    print('Matching: {}'.format(matches))
    print('Height: {}'.format(font_height))
    print('Baseline: {}'.format(font_baseline))
    print('Max width: {}'.format(glyph_widest))
    print('Fixed width: {}'.format(fixed_width))
    if debug:
        print('Headers:\n', font.headers)
        print('Props:\n', font.props)
    print('===============================================')

# Generate the Output:

# add preamble, static properties and methods
def method(n,v):
    print('def {}():\n    return {}\n'.format(n,v))

prelude = ('''# Code generated by bdf2dict.py
# Font: {} Char set: {}
# Cmd: {}
# Date: {}
''').format(name, cset, argv, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(prelude)

static = ('''version = '0.33'
name = '{}'
family = '{}'
weight = '{}'
size = {}
''').format(font_name, font_family, font_weight, font_size)
print(static)

method('height', font_height)
method('baseline', font_baseline)
method('max_width', glyph_widest)
method('hmap', True)
method('reverse', False)
method('monospaced', fixed_width)
method('min_ch', list(glyph_dict.keys())[0])
method('max_ch', list(glyph_dict.keys())[-1])

custom = ('''def clean():
    for i in font._g.keys():
        if len(font._g[i]) > {0}:
            del(font._g[i][{0}])
''').format(2 if fixed_width else 3)
print(custom)

# This is the glyph data
print('{}'.format(glyph_dict_string))

# Now the get_ch() method:
# The following only differ in how width is handled,
# otherwise identical.
if fixed_width:
    func = '''
def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    if len(_g[c]) == 2:
        bw = ((max_width() - 1) // 8) + 1
        bstr = '0' * ((_g[c][0] - 1) * bw * 2)
        for l in _g[c][1]:
            bstr += '{:0{}x}'.format(l, bw * 2)
        bstr += '0' * ((height() -  _g[c][0] - len(_g[c][1]) + 1) * bw * 2)
        _g[c].append(bytearray.fromhex(bstr))
    return memoryview(_g[c][2]), height(), max_width()
'''
else:
    func = '''
def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    if len(_g[c]) == 3:
        bw = ((_g[c][2] - 1) // 8) + 1
        bs = '0' * ((_g[c][0] - 1) * bw * 2)
        for l in _g[c][1]:
            bs += '{:0{}x}'.format(l, bw * 2)
        bs += '0' * ((height() -  _g[c][0] - len(_g[c][1]) + 1) * bw * 2)
        _g[c].append(bytearray.fromhex(bs))
    return memoryview(_g[c][3]), height(), _g[c][2]
'''
print(func)
