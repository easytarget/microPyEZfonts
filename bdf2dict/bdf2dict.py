'''
    bsd2dict, takes two arguments; a .bdf font file and a file with a UTF-8
    encoded list of characters in it.

    It returns a .py file with the corresponding micropython font class
    and a .map file giving more details and ascii glyph representations.

    This is a /terrible/ script as far as structure goes.. my apologies.
    Basically it starts at the top and runs to the end, no real use of functions,
    classes or python niceities. It's also wasteful of memory and cpu cycles..
    However, it gets the job done well enough to be useful ;-)
'''
from datetime import datetime
from sys import argv, stderr, stdin
from pathlib import Path

try:
    from bdfparser import Font
except ImportError:
    print('"bdfparser" needs to be available! exiting.\n(hint: Use a venv then "pip install bdfparser", see README.md for more)')
    exit()

if len(argv) < 2:
    print('\nUsage: {} <font-file>.bdf [charset]\n'.format(argv[0]))
    print('Generates a python font module from the supplied .bdf file',end='')
    print(' containing all matching glyphs for the characters in [charset]\n')
    print('If [charset] is a valid file path this will be read',end='')
    print(' and used as the character set.')
    print("If [charset] is 'FULL' the entire font file will be converted.")
    print('Otherwise the charset will be read from stdin.\n')
    print("Outputs two files in cwd; 'font.py' and 'font.map'")
    exit(1)

font_file = argv[1]
if not Path(font_file).is_file():
    print('{}: Error; font file: {} not found.'.format(argv[0], font_file))
    exit(1)

if len(argv) > 2:
    if Path(argv[2]).is_file():
        print('Reading charset from file: {}'.format(argv[2]))
        with open(argv[2], 'r') as setfile:
            cset = setfile.read()
    elif argv[2] == 'FULL':
        print('Generating for all glyphs in font')
        cset = None
    elif argv[2] == '-':
        # wait for stdin + eof
        print('Reading charset from stdin: ', end='', flush=True)
        with stdin as sin:
            cset = sin.read()
        print()
    else:
        print('Reading charset from arguments')
        cset = argv[2]
else:
    cset = input('Enter charset: ')

# make cset a sorted unique list of chars
cset = sorted(set(cset))

# Enable debug here...
debug = False

# extract font file name
name = Path(font_file).stem

# import font
font = Font(font_file)
if 'fontname' not in font.headers.keys():
    stderr.write('ERROR: {}: font has no headers, nothing to output\n'.format(argv[1]))
    exit(1)
print('Processing: {}'.format(font_file))

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

# Defaults
matches = 0
withdata = 0

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
    # Compare to the valid chars and skip if not present
    if cset and chr(fchar) not in cset:
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
    else:
        withdata += 1
    if debug:
        print('Char: {} ({})'.format(fchar, glyph_name[fchar]))
        print(g.meta)
        print(glyph_map,end='')
        high = last[fchar] - first[fchar] + 1
        print('Width: {}, Lines: {}, first line: {}, last line: {}'.format(wide, high, first[fchar], last[fchar]))
        print('dict entry: {} ({} chars)'.format(glyph_dict[fchar], len(glyph_dict[fchar])))
        print()

# No matching characters, exit.
if matches == 0 or withdata == 0:
    print('No valid matches for this charset')
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
        glyph_dict_string += ",b'{}'],\n".format(glyph_px[fchar])
glyph_dict_string += '}'

# generate the map file
with open(name + '.map','w') as mapfile:
    # output font summary
    mapfile.write('Font: {} ({})\n'.format(name, font_file))
    mapfile.write('Declared name: {}\n'.format(font_name))
    mapfile.write('Declared family: {}\n'.format(font_family))
    mapfile.write('Declared weight: {}\n'.format(font_weight))
    mapfile.write('Declared size: {}\n'.format(font_size))
    mapfile.write('Matching characters: {}\n'.format(matches))
    mapfile.write('Height: {}\n'.format(font_height))
    mapfile.write('Baseline: {}\n'.format(font_baseline))
    mapfile.write('Max width: {}\n'.format(glyph_widest))
    mapfile.write('Fixed width: {}\n'.format(fixed_width))
    if debug:
        print('Headers:\n', font.headers)
        print('Props:\n', font.props)
    else:
        # A human-readable ascii-art glyph map
        for fchar in glyph_dict.keys():
            wide = glyph_widest if fixed_width else glyph_px[fchar]
            hwide = ((glyph_px[fchar] - 1) // 8 + 1) * 2
            mapfile.write('\nChar: {} ({}), width: {}\n'.format(fchar, glyph_name[fchar], wide))
            for l in range(0, len(glyph_dict[fchar]), hwide):
                bs = '{:0{}b}'.format(int(glyph_dict[fchar][l:l+hwide], 16), hwide * 4)
                bt = bs.replace('0',' ').replace('1','#')[0:wide]
                bl = '_' if l  == ((font_baseline - 1) * hwide)  else '.'
                mapfile.write('  {1}{0}{1}\n'.format(bt, bl))

# Generate a .set file
with open(name + '.set','w') as setfile:
    for fchar in glyph_dict.keys():
        setfile.write(chr(fchar))

# Report unmatched characters
unmatched = []
for cchar in cset:
    if (ord(cchar) not in glyph_dict.keys()) and cchar.isprintable():
        unmatched.append(cchar)
if unmatched:
    print('Requested characters not matched in the source font:\n{}'.format(unmatched))


# Generate the output .py file
with open(name + '.py','w') as pyfile:
    # add preamble, static properties and methods
    cmdname = argv[0].split('/')[-1]
    prelude = ('''# Code generated by bdf2dict.py
# Font: {}
# Cmd: [{}], {}
# Date: {}
\n''').format(name, cmdname, argv[1:], datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    pyfile.write(prelude)

    static = ('''version = '0.33'
name = '{}'
family = '{}'
weight = '{}'
size = {}
\n''').format(font_name, font_family, font_weight, font_size)
    pyfile.write(static)

    def method(n,v):
        pyfile.write('def {}():\n    return {}\n\n'.format(n,v))
    method('height', font_height)
    method('baseline', font_baseline)
    method('max_width', glyph_widest)
    method('hmap', True)
    method('reverse', False)
    method('monospaced', fixed_width)
    method('min_ch', list(glyph_dict.keys())[0])
    method('max_ch', list(glyph_dict.keys())[-1])

    # This is the glyph data
    pyfile.write('_g = {}\n'.format(glyph_dict_string))

    # Now the get_ch() method:
    func = '''
def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c][0]), {}, {}
\n'''.format(font_height, glyph_widest if fixed_width else 'int(_g[c][1])')
    pyfile.write(func)
