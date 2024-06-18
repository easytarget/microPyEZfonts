# Raw .bdf file reader of my own.
'''
    Notes: things that proper fonts do but we cannot handle (ie. ezFBfont cannot handle)
        If glyph box is wider than the device width this means the glyph is supposed to overlap the next one. but we cant handle that properly so we widen the glyph.
        If glyph box has a negative offset this is supposed to print char to left of current pos, again we do not handle this, so the glyph is left aligned and it's device width set to the glyph box width
'''

from datetime import datetime
from sys import argv, stderr, stdin
from pathlib import Path

# Arguments
scriptname = Path(argv[0]).name

# append 'debug' to arguments to enable debug
if argv[-1] == 'debug':
    debug = True
    argv.pop()
else:
    debug = False

if len(argv) not in [3, 4]:
    print("\nUsage: {} <font>.bdf <prefix> [charset]\n".format(scriptname))
    print("Generates a python font module from the supplied .bdf file",end='')
    print(" containing all matching glyphs for the characters in [charset]\n")
    print("If [charset] is a valid file path this will be read",end='')
    print(" and used as the character set.")
    print("If [charset] is 'FULL' the entire font file will be converted.")
    print("If [charset] is '-' the charset will be read from stdin.")
    print("Otherwise the user will be prompted to enter the charset.\n")
    print("The output file names will begin with the supplied prefix.")
    print("Spaces, hyphens and dots in the prefix and font name will be",end='')
    print(" mapped to an underscore '_' since the generated .py filename",end='')
    print(" needs to conform to the python module naming standard.\n")
    print("Outputs three files in cwd; '<prefix><font>.py', '<prefix><font>.map' ")
    print("and '<prefix><font>.set'.")
    exit(1)

def safe_module_name(name):
    for s in "!@#$%^&*()+-={}[]:;'<>?,.~":
        name = name.replace(s, '_')
    return name

font_file = argv[1]
if not Path(font_file).is_file():
    print('{}: Error; font file: {} not found.'.format(argv[0], font_file))
    exit(1)

prefix = safe_module_name(argv[2])
stem = safe_module_name(Path(font_file).stem)
name = '{}{}'.format(prefix, stem)

if len(argv) == 4:
    if Path(argv[3]).is_file():
        #print('Reading charset from file: {}'.format(argv[3]))
        with open(argv[3], 'r') as setfile:
            cset = setfile.read()
    elif argv[3] == 'FULL':
        #print('Generating for all glyphs in font')
        cset = None
    elif argv[3] == '-':
        # wait for stdin + eof
        #print('Reading charset from stdin: ', end='', flush=True)
        with stdin as sin:
            cset = sin.read()
        print()
    else:
        #print('Reading charset from arguments')
        cset = argv[3]
else:
    cset = input('Enter charset: ')

# make cset a sorted unique list of chars
if cset:
    cset = sorted(set(cset))

# data
glyph_data = {}
report = {}

# functions
def get_val(block,value):
    # Get a named value from a set of input file lines
    for line in block:
        if line.startswith(value):
            return line[len(value):].strip()
    return 'None'

def get_meta(block,value):
    # Get all matching values from a set of input file lines
    ret = []
    for line in block:
        if line.startswith(value):
            ret.append(line[len(value):].strip())
    return ret

def pull_glyph(glyph_block):
    # Takes a text block and pulls the character
    # definition and bitmap out of it.
    header, bitmap = glyph_block.split('BITMAP')
    header = header.strip().split('\n')
    bitmap = bitmap.strip().split('\n')
    # if we meet the EOF marker (after last glyph) remove it
    if bitmap[-1] == 'ENDFONT':
        bitmap.pop()
    # Check we have a complete char defined.
    if bitmap[-1] != 'ENDCHAR':
        print('BAD CHAR!', header)
        return None, None
    bitmap.pop()
    if len(bitmap) == 0:
        return None, None
    # Gather basics for glyph
    name = header[0]
    ordinal = int(get_val(header,'ENCODING'))
    if ordinal < 0:
        # todo, how should we handle chars specified as chr(-1) etc.?
        return None, None
    box = [eval(i) for i in get_val(header,'BBX').split(' ')]
    width = int(get_val(header,'DWIDTH').split(' ')[0])
    out = {'name': name, 'width': width, 'box': box, 'rawhex': bitmap}
    return ordinal, out


def line_hex(glyph, line, device_wide, box_wide, xoff, hex_bits, extra_bits):
    # Generates the full-width hex line with the glyph aligned
    #  in it and padded.
    val = int(line,16)
    binline = '{:0{}b}'.format(val, hex_bits)
    boxline = binline[:box_wide]
    trim = binline[box_wide:].replace('0','x')
    if '1' in trim:
        print(glyph, 'pixels to right of box')
        exit()    # Shouldn't happen.. we can skip if this is an issue in practice
    # pad by xoff
    boxline = '{}{}'.format('0' * xoff, boxline)
    width_pad = device_wide - len(boxline)
    # append padding bits to make a full byte
    byteline = '{}{}'.format(boxline, '0' * (width_pad + extra_bits))
    hexline = '{:0{}x}'.format(int(byteline,2), len(byteline) // 4)
    humanline = '{}{}'.format(boxline.replace('0',' '), ' ' * width_pad)
    if debug:
        print('{}| {} {}'.format(humanline, byteline, hexline))
    return hexline, humanline.replace('1','#')

# Main Code

# Open and ingest the source
with open(font_file,'r') as readlines:
    bdf = readlines.read().split('STARTCHAR')
startblock = bdf.pop(0).split('\n')

# get basics
font_name = get_val(startblock, 'FONT').strip('"')
font_box = [eval(i) for i in get_val(startblock, 'FONTBOUNDINGBOX').split(' ')]
font_family = get_val(startblock, 'FAMILY_NAME').strip('"')
font_weight = get_val(startblock, 'WEIGHT_NAME').strip('"')
font_size = get_val(startblock, 'PIXEL_SIZE').strip('"')

print('{}: processing {}'.format(scriptname, font_file))
if debug:
    print('startblock lines: {}, glyph entries {}'.format(len(startblock),len(bdf)))
    if cset is not None:
        print('requested charset: {}'.format(cset))
    else:
        print('requested charset: FULL')
    print('font name   : {}'.format(font_name))
    print('font family : {}'.format(font_family))
    print('font box    : {}'.format(font_box))

# walk all the glyph blocks in the .bdf, adjust and save matching glyphs
for block in bdf:
    ordinal, entry = pull_glyph(block)
    if ordinal is None:
        continue
    if cset and (chr(ordinal) not in cset):
        continue
    # collect any reports about adjustments and errors for the glyph
    rep = []
    # Sanity check glyph and box widths
    if entry['width'] < entry['box'][0]:
        r = 'Char box width ({}) is greater than device width ({}), increasing device width.'
        rep.append(r.format(entry['box'][0], entry['width']))
        entry['width'] = entry['box'][0]
    if entry['box'][2] < 0:
        rep.append('Negative horizontal padding ({}), zeroing.'.format(entry['box'][2]))
        entry['box'][2] = 0
    if entry['width'] > font_box[0]:
        r = 'Device width ({}) is wider than overall font box width ({}), reducing device width.'
        rep.append(r.format(entry['width'], font_box[0]))
        entry['width'] = font_box[0]
    # Sanity check vertical box + baseline, note start/stop lines
    if entry['box'][1] != len(entry['rawhex']):
        r = 'Bitmap height ({}) differs from box height ({}), adjusting box.'
        rep.append(r.format(len(entry['rawhex']), font_box[1]))
        entry['box'][1] = len(entry['rawhex'])
    # Strip empty (0) lines from top and bottom of bitmap and adjust box to match
    while (int(entry['rawhex'][0], 16) == 0) and (len(entry['rawhex']) > -entry['box'][3] + 1):
        entry['rawhex'].pop(0)
        entry['box'][1] -= 1
    while (int(entry['rawhex'][-1], 16) == 0) and (len(entry['rawhex']) > 1):
        entry['rawhex'].pop()
        entry['box'][1] -= 1
        entry['box'][3] += 1
    entry['top'] = entry['box'][3] + entry['box'][1] 
    entry['bottom'] = entry['box'][3]
    # Save the glyph
    glyph_data[ordinal] = entry
    if len(rep) > 0:
        report[ordinal] = rep

# Check that we have matching glyphs
matches = len(glyph_data)
if matches == 0:
    print('No matches for character set found in font file, exiting.')
    exit()

# Find the widest character
widest = max([glyph_data[d]['width'] for d in glyph_data])
fixed = True if len(set(glyph_data[d]['width'] for d in glyph_data)) == 1 else False

# Find the first and last lines of bitmap in our chars
top = max([glyph_data[d]['top'] for d in glyph_data])
bottom = min([glyph_data[d]['bottom'] for d in glyph_data])
height = top - bottom
# baseline; constrained within font height
baseline = min(max(0, -bottom), height)

# Pad glyph raw hex as needed to the overall height from above
if debug:
    print('\nheight: {}, baseline {}'.format(height, baseline))
for glyph in glyph_data:
    pad_top = top - glyph_data[glyph]['top']
    pad_bottom = glyph_data[glyph]['bottom'] - bottom
    if debug:
        hm = '{}{}{}'.format('+' * pad_top, '#' * len(glyph_data[glyph]['rawhex']), '-' * pad_bottom)
        print('{:>5d} {}|{}'.format(glyph, hm[:-baseline], hm[-baseline:]))
    glyph_data[glyph]['padhex'] = ['0'] * pad_top + glyph_data[glyph]['rawhex'] + ['0'] * pad_bottom
    del glyph_data[glyph]['rawhex']

# We now have dict with all the desired and matching glyphs and metadata
# Compute the bytearray for each.
for glyph in glyph_data:
    device_wide = glyph_data[glyph]['width']
    box_wide =  glyph_data[glyph]['box'][0]
    box_xoff =  glyph_data[glyph]['box'][2]
    box_high = glyph_data[glyph]['box'][1]
    box_yoff = glyph_data[glyph]['box'][3]
    padhex = glyph_data[glyph]['padhex']
    if debug:
        p = '\nChar: {} ({})'
        print(p.format(glyph, glyph_data[glyph]['name']), end='')
        p = ', device width {}, box width {}, box Xoff {}'
        print(p.format(device_wide, box_wide, box_xoff), end='')
        p = ', box height  {}, box Yoff {}'
        print(p.format(box_high, box_yoff))
        print(padhex)
        print('{}{}'.format(' ' * box_xoff, '.' * box_wide))
        print('{}'.format('-' * device_wide))
    # work out how many bits of data are in the bdf bitmap lines
    padhex_bits = 0
    for line in padhex:
        padhex_bits = max(padhex_bits, len(line) * 4)
    # work out how many bytes wide we need to be, and calculate bit padding
    output_bytes = ((device_wide - 1) // 8) + 1
    extra_bits = (output_bytes * 8) - device_wide
    # Now process the lines
    glyph_data[glyph]['hex'] = []
    glyph_data[glyph]['map'] = []
    for line in padhex:
        bytehex, human = line_hex(glyph, line, device_wide, box_wide, box_xoff, padhex_bits, extra_bits)
        glyph_data[glyph]['hex'].append(bytehex)
        glyph_data[glyph]['map'].append(human)
    del glyph_data[glyph]['padhex']

# Font processing complete, generate output

# Output the map file
with open(name + '.map','w') as mapfile:
    # output font summary
    mapfile.write('Font: {} ({})\n'.format(stem, font_file))
    mapfile.write('Declared name: {}\n'.format(font_name))
    mapfile.write('Declared family: {}\n'.format(font_family))
    mapfile.write('Declared weight: {}\n'.format(font_weight))
    mapfile.write('Declared size: {}\n'.format(font_size))
    mapfile.write('Characters: {}\n'.format(matches))
    mapfile.write('Height: {}\n'.format(height))
    mapfile.write('Baseline: {}\n'.format(baseline))
    mapfile.write('Max width: {}\n'.format(widest))
    mapfile.write('Fixed width: {}\n'.format(fixed))
    # A human-readable ascii-art glyph map
    for glyph in glyph_data:
        mapfile.write('\nChar {} ({}), width {}\n'.format(glyph, glyph_data[glyph]['name'],glyph_data[glyph]['width']))
        for l in range(len(glyph_data[glyph]['map'])):
            border = '__' if (height - l - 1) == baseline else '.'
            mapfile.write(' {1:>2}{0}{1:<2}\n'.format(glyph_data[glyph]['map'][l], border))
    # Show position and box adjustment reports as needed
    if len(report) > 0:
        mapfile.write('\nFont rendering notes:\n')
        for line in report:
            mapfile.write('Char {}:\n'.format(line))
            for entry in report[line]:
                mapfile.write('  {}\n'.format(entry))

# Generate a .set file for the available chars
with open(name + '.set','w') as setfile:
    for mchar in glyph_data:
        setfile.write(chr(mchar))

# Gather metadata from original font file
comment_text = get_meta(startblock, 'COPYRIGHT')
copyright_text = get_meta(startblock, 'COMMENT')
notice_text = get_meta(startblock, 'NOTICE')

glyph_dict_string = '{\n'
for glyph in glyph_data:
    glyph_dict_entry = ''
    for line in glyph_data[glyph]['hex']:
        glyph_dict_entry += line
    glyph_dict_string += '  {}:{},\n'.format(glyph, bytes.fromhex(glyph_dict_entry))
glyph_dict_string += '}'

# Generate the output .py file
with open(name + '.py','w') as pyfile:
    # Preamble
    cmdname = argv[0].split('/')[-1]
    pyfile.write('''# Code generated by bdf2dict.py
# Font: {}
# Cmd: ['{}'], {}
# Date: {}
'''.format(stem, cmdname, argv[1:], datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    # Append copyright, comments and notices from source font.
    if len(copyright_text) > 0 or len(comment_text) > 0 or len(notice_text) > 0:
        pyfile.write("'''\n    Original Copyright, Comments and Notices from source:\n")
        if len(copyright_text) > 0:
            pyfile.write('\n')
            for line in copyright_text:
                pyfile.write('    COPYRIGHT {}\n'.format(line.strip()))
        if len(comment_text) > 0:
            pyfile.write('\n')
            for line in comment_text:
                pyfile.write('    COMMENT {}\n'.format(line.strip()))
        if len(notice_text) > 0:
            pyfile.write('\n')
        for line in notice_text:
            pyfile.write('    NOTICE {}\n'.format(line.strip()))
        pyfile.write("'''\n")

    # Static properties
    pyfile.write('''version = '0.33'
name = '{}'
family = '{}'
weight = '{}'
size = {}
\n'''.format(font_name, font_family, font_weight, font_size))

    # Font methods
    def method(n,v):
        pyfile.write('def {}():\n    return {}\n\n'.format(n,v))

    method('height', height)
    method('baseline', baseline)
    method('max_width', widest)
    method('hmap', True)
    method('reverse', False)
    method('monospaced', fixed)
    method('min_ch', list(glyph_data.keys())[0])
    method('max_ch', list(glyph_data.keys())[-1])

    # The glyph data
    pyfile.write('_g = {}\n'.format(glyph_dict_string))

    # The get_ch() method:
    pyfile.write('''
def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), {}, {}
\n'''.format(height, widest if fixed else 'int(_g[c][1])'))

# Wrap up
print('{} Matching characters rendered to {}.py'.format(matches, name))
if cset:
    unmatched = []
    for cchar in cset:
        if (ord(cchar) not in glyph_data.keys()) and cchar.isprintable():
            unmatched.append(cchar)
    if unmatched:
        print('Characters requested but not available in the font:\n{}'.format(unmatched))
# Fin
