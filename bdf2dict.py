# Published 2024/06 by Owen (https://github.com/easytarget/)
# Licenced under a Createive-Commons zero licence: see repo LICENCE file.
'''
    bdf2dict.py : generates a .py module containing a font derived from a .bdf file

    - Takes a .bdf font file as input, and a list of characters to be rendered
      Outputs a .py module named after the prefix + font
    - This output module can be used with the ezFBfont writer, and is fully
      compatible with the font writer and gui class from Peter Hinch; to whom
      I owe a lot of inspiration.
    - Works seamlessly with Unicode charsets and fonts that have unicode characters
    - The desired character set can be specified as an argument, in a file,
        passed via stdin or at a user prompt.
      All matching font characters will be present in the .py font module,
        if requested characters have no font entry they are reported.
    - The prefix for the result files is required, this can include a path to
        specify the output directory.
    - A '.map' file containing an asc-ii art representation of the font module
        glyphs will also be saved to the output path, as will a '.set' file with
        the characters that are present in the font.
    - Module and prefix names will be sanitised to replace all punctuation with
        underscores (_) in order to conform to python module naming requirements

    Notes:
    This is a tool for making small font files for use on micropython devices
    with small displays. It only handles monochrome fonts that write right->left.
    There are several things that may be specified in the font file but cannot
    be handled properly with the format used here:
    - If the glyph box is wider than the printing width this means the character is
      supposed to overlap the next one. The writer cannot handle this, instead the
      glyph is widened to ensure it is all displayed.
    - If the glyph box has a negative offset this is supposed to print to the left
      of the start position, overlapping the previous character. In this case the
      glyph is left justified and it's device width set to the glyph box width
    - A report on what adjustments are made (if any) is appended to the .map file.
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

# Oeps
if len(argv) not in [3, 4]:
    print("\nUsage: {} <font>.bdf <prefix> [charset]\n".format(scriptname))
    print("Generates a python font module from the supplied .bdf file",end='')
    print(" containing all matching glyphs for the characters in [charset]\n")
    print("If [charset] is a valid file path this will be read",end='')
    print(" and used as the character set.")
    print("If [charset] is empty ('') the entire font file will be converted.")
    print("If [charset] is '--' the charset will be read from stdin.")
    print("Otherwise the user will be prompted to enter the charset.")
    print("Duplicate charset entries are ignored.\n")
    print("The output file names will begin with the supplied prefix.")
    print("The prefix can include a path for the output.")
    print("Spaces, hyphens and dots in the prefix and font name will be",end='')
    print(" mapped to an underscore '_' since the generated .py filename",end='')
    print(" needs to conform to the python module naming standard.\n")
    print("Outputs three files '<prefix><font>.py', '<prefix><font>.map' ")
    print("and '<prefix><font>.set'.")
    exit(1)

# Python module names cannot contain common punctuation chars, replace with underscores.
def safe_module_name(name):
    for s in "!@#$%^&*()+-={}[]:;'<>?,.~":
        name = name.replace(s, '_')
    return name

# Check the font file exists
font_file = argv[1]
if not Path(font_file).is_file():
    print('{}: Error; font file: {} not found.'.format(argv[0], font_file))
    exit(1)

# Names and paths
prefix = safe_module_name(Path(argv[2]).name)
stem = safe_module_name(Path(font_file).stem)
name = '{}{}'.format(prefix, stem)
outdir = Path(argv[2]).parent
if not Path(outdir).is_dir():
    print("{}: output directory '{}/' does not exist".format(argv[0], outdir))
    exit(1)
py_file = Path(outdir).joinpath(name + '.py')
map_file = Path(outdir).joinpath(name + '.map')
set_file = Path(outdir).joinpath(name + '.set')

# Determine charset
if len(argv) == 4:
    if Path(argv[3]).is_file():
        with open(argv[3], 'r') as setfile:
            cset = setfile.read()
    elif len(argv[3]) == 0:
        cset = None
    elif argv[3] == '--':
        # wait for stdin + eof
        with stdin as sin:
            cset = sin.read()
        print()
    else:
        cset = argv[3]
else:
    cset = input('Enter charset: ')

# make cset a sorted unique list of chars
if cset:
    cset = sorted(set(cset))

# data structures
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
font_name = get_val(startblock, 'FONT').strip('"').lower()
font_box = [eval(i) for i in get_val(startblock, 'FONTBOUNDINGBOX').split(' ')]
font_family = get_val(startblock, 'FAMILY_NAME').strip('"').lower()
font_weight = get_val(startblock, 'WEIGHT_NAME').strip('"').lower()
font_size = get_val(startblock, 'PIXEL_SIZE').strip('"')
comment_text = get_meta(startblock, 'COPYRIGHT')
copyright_text = get_meta(startblock, 'COMMENT')
notice_text = get_meta(startblock, 'NOTICE')

if font_family == 'none':
    font_family = 'generic'

# let the user know we are working on things
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
    while (len(entry['rawhex']) > -entry['box'][3] + 1) and (int(entry['rawhex'][0], 16) == 0):
        entry['rawhex'].pop(0)
        entry['box'][1] -= 1
        if len(entry['rawhex']) == 0:
            break  # stops index errors if rawhex len is shorter than box height for space chars
    while (len(entry['rawhex']) > 1) and (int(entry['rawhex'][-1], 16) == 0):
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

# Find the widest character, look to see if we have a fixed-width
widest = max([glyph_data[d]['width'] for d in glyph_data])
fixed = True if len(set(glyph_data[d]['width'] for d in glyph_data)) == 1 else False

# Find the first and last lines of bitmap, calculate height and baseline
top = max([glyph_data[d]['top'] for d in glyph_data])
bottom = min([glyph_data[d]['bottom'] for d in glyph_data])
height = top - bottom
baseline = min(max(0, height+bottom), height)

# Pad glyph hex out to top and bottom as needed to ensure all chars have the same height
if debug:
    print('\nheight: {}, baseline {}'.format(height, baseline))
for glyph in glyph_data:
    pad_top = top - glyph_data[glyph]['top']
    pad_bottom = glyph_data[glyph]['bottom'] - bottom
    if debug:
        hm = '{}{}{}'.format('+' * pad_top, '#' * len(glyph_data[glyph]['rawhex']), '-' * pad_bottom)
        print('{:>5d} {}|{}'.format(glyph, hm[:baseline], hm[baseline:]))
    glyph_data[glyph]['padhex'] = ['0'] * pad_top + glyph_data[glyph]['rawhex'] + ['0'] * pad_bottom
    # clean up as we go.
    del glyph_data[glyph]['rawhex']

# Vertical padding is now complete
# The glyph_data[] dict has all the matching glyphs, metadata, and line values
# Compute horizontally justified and padded raw hex strings for the glyph lines
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
    # clean up as we go.
    del glyph_data[glyph]['padhex']

# Font processing is complete, generate output dict[] string
glyph_dict_string = '{\n'
for glyph in glyph_data:
    glyph_dict_entry = ''
    for line in glyph_data[glyph]['hex']:
        glyph_dict_entry += line
    if not fixed:
        # for variable width fonts we append a byte containg the width.
        glyph_dict_entry += '{:02x}'.format(glyph_data[glyph]['width'])
    glyph_dict_string += '  {}:{},\n'.format(glyph, bytes.fromhex(glyph_dict_entry))
glyph_dict_string += '}'

# Generate the output .py file
try:
    with open(py_file, 'w') as pyfile:
        # Preamble
        cmdname = argv[0].split('/')[-1]
        pyfile.write("# Code generated by bdf2dict.py\n")
        pyfile.write("# Font: {}\n".format(stem))
        pyfile.write("# Cmd: ['{}'], {}\n".format(cmdname, argv[1:]))
        pyfile.write("# Date: {}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
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
        pyfile.write("version = '0.33'\n")
        pyfile.write("name = '{}'\n".format(font_name))
        pyfile.write("family = '{}'\n".format(font_family))
        pyfile.write("weight = '{}'\n".format(font_weight))
        pyfile.write("size = {}\n\n".format(font_size))
        # Font methods
        def method(n,v):
            pyfile.write("def {}():\n    return {}\n\n".format(n,v))
        method('height', height)
        method('baseline', baseline)
        method('max_width', widest)
        method('hmap', True)
        method('reverse', False)
        method('monospaced', fixed)
        method('min_ch', list(glyph_data.keys())[0])
        method('max_ch', list(glyph_data.keys())[-1])
        # The glyph data
        pyfile.write('_g = {}\n\n'.format(glyph_dict_string))
        # The get_ch() method:
        pyfile.write("def get_ch(ch):\n")
        pyfile.write("    c = ord(ch)\n")
        pyfile.write("    if c not in _g.keys():\n")
        pyfile.write("        return None, 0, 0\n")
        pyfile.write("    return memoryview(_g[c]), {}, {}\n".format(
            height, widest if fixed else 'int(_g[c][-1])'))
except Exception as e:
    print('{}: cannot write to {}:\n{}'.format(argv[0], py_file, e))
    exit(1)

# Output the map file
with open(map_file, 'w') as mapfile:
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
            border = '__' if l == baseline - 1 else '.'
            mapfile.write(' {1:>2}{0}{1:<2}\n'.format(glyph_data[glyph]['map'][l], border))
    # Show position and box adjustment reports as needed
    if len(report) > 0:
        mapfile.write('\nFont rendering notes:\n')
        for line in report:
            mapfile.write('Char {}:\n'.format(line))
            for entry in report[line]:
                mapfile.write('  {}\n'.format(entry))

# Generate a .set file for the available chars
with open(set_file, 'w') as setfile:
    for mchar in glyph_data:
        setfile.write(chr(mchar))

# Wrap up
print('{} Matching characters rendered to {}'.format(matches, py_file))
if cset:
    unmatched = []
    for cchar in cset:
        if (ord(cchar) not in glyph_data.keys()) and cchar.isprintable():
            unmatched.append(cchar)
    if unmatched:
        print('Characters requested but not available in the font:\n{}'.format(unmatched))
# Fin
