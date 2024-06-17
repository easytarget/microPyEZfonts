# Raw .bdf file reader of my own.
'''
    Notes: things that proper fonts do but we cannot handle (ie. ezFBfont cannot handle)
        If glyph box is wider than the device width this means the glyph is supposed to overlap the next one. but we cant handle that properly so we widen the glyph.
        If glyph box has a negative offset this is supposed to print char to left of current pos, again we do not handle this, so the glyph is left aligned and it's device width set to the glyph box width
'''

#from datetime import datetime
from sys import argv, stderr, stdin
from pathlib import Path
#from re import match

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
        print('Reading charset from file: {}'.format(argv[3]))
        with open(argv[3], 'r') as setfile:
            cset = setfile.read()
    elif argv[3] == 'FULL':
        print('Generating for all glyphs in font')
        cset = None
    elif argv[3] == '-':
        # wait for stdin + eof
        print('Reading charset from stdin: ', end='', flush=True)
        with stdin as sin:
            cset = sin.read()
        print()
    else:
        print('Reading charset from arguments')
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

def pull_glyph(glyph_block):
    # Takes a text block and pulls the character
    # definition and bitmap out of it.
    header, bitmap = glyph_block.split('BITMAP')
    header = header.strip().split('\n')
    bitmap = bitmap.strip().split('\n')
    # EOF marker, ignore and treat as 'just another glyph'
    if bitmap[-1] == 'ENDFONT':
        bitmap.pop()
    # Check we have a complete char defined.
    if bitmap[-1] != 'ENDCHAR':
        print('BAD CHAR!', header)
        return None, None
    bitmap.pop()
    if len(bitmap) == 0:
        print('EMPTY CHAR!', header)
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


def line_hex(glyph, line, device_wide, box_wide, xoff, hex_bits, extra_bits, report):
    # Generates the full-width hex line with the glyph aligned
    #  in it and padded.
    val = int(line,16)
    binline = '{:0{}b}'.format(val, hex_bits)
    boxline = binline[:box_wide]
    trim = binline[box_wide:].replace('0','x')
    if '1' in trim:
        print(glyph, 'pixels to right of box')
        exit()    # <---------  TODO, trim and log a report..  ------>
    # pad by xoff
    boxline = '{}{}'.format('0' * xoff, boxline)
    width_pad = device_wide - len(boxline)
    # append padding bits to make a full byte
    byteline = '{}{}'.format(boxline, '0' * (width_pad + extra_bits))
    hexline = '{:0{}x}'.format(int(byteline,2), len(byteline) // 4)
    if debug:
        print('{}{}| {} {}'.format(boxline.replace('0',' '),
                                   ' ' * width_pad, byteline,
                                   hexline))
    return hexline

# Main Code

# Open and ingest the source
with open(font_file,'r') as readlines:
    bdf = readlines.read().split('STARTCHAR')
startblock = bdf.pop(0).split('\n')

# get basics
font_name = get_val(startblock, 'FONT')
font_box = [eval(i) for i in get_val(startblock, 'FONTBOUNDINGBOX').split(' ')]
font_family = get_val(startblock, 'FAMILY_NAME').strip('"')

if debug:
    print('startblock lines: {}, glyph entries {}'.format(len(startblock),len(bdf)))
    print('{}: processing {} as {}'.format(scriptname, font_file, name))
    if cset is not None:
        print('requested charset: {}'.format(cset))
    else:
        print('requested charset: FULL')

# walk all the glyph blocks in the .bdf and save matching glyphs
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
        r = 'box width ({}) is greater than device width ({}), widening'
        rep.append(r.format(entry['box'][0], entry['width']))
        entry['width'] = entry['box'][0]
    if entry['box'][2] < 0:
        r = 'negative horizontal padding ({}), left aligning'.format(entry['box'][2])
        entry['box'][2] = 0
        if entry['width'] > entry['box'][0]:
            r += ' and reducing device width ({}) to box width ({})'.format(entry['width'], entry['box'][0])
            entry['width'] = entry['box'][0]
        rep.append(r)
    if entry['width'] > font_box[0]:
        r = 'width ({}) is wider than overall font box width ({}), clipping'
        rep.append(r.format(entry['width'], font_box[0]))
        entry['width'] = font_box[0]
    # Sanity check vertical box + baseline, note start/stop lines
    # Save the glyph
    glyph_data[ordinal] = entry
    report[ordinal] = rep

# We now have dict with all the desired and matching glyphs and metadata
# Compute the bytearray for each.
for glyph in glyph_data:
    device_wide = glyph_data[glyph]['width']
    box_wide =  glyph_data[glyph]['box'][0]
    box_xoff =  glyph_data[glyph]['box'][2]
    rawhex = glyph_data[glyph]['rawhex']
    if debug:
        p = '\nChar: {} ({}), device width {}, box width {}, box offset {}'
        print(p.format(glyph, glyph_data[glyph]['name'], device_wide, box_wide, box_xoff))
        print('{}{}'.format(' ' * box_xoff, '.' * box_wide))
        print('{}'.format('-' * device_wide))
    # work out how many bits of data are in the bdf bitmap lines
    rawhex_bits = 0
    for line in rawhex:
        rawhex_bits = max(rawhex_bits, len(line) * 4)
    # work out how many bytes wide we need to be and calculate bit padding
    output_bytes = ((device_wide - 1) // 8) + 1
    extra_bits = (output_bytes * 8) - device_wide
    # Now process the lines
    glyph_data[glyph]['hex'] = []
    for line in rawhex:
        glyph_data[glyph]['hex'].append(line_hex(glyph, line, device_wide,
                                                 box_wide, box_xoff,
                                                 rawhex_bits, extra_bits,
                                                 report))
    del glyph_data[glyph]['rawhex']

# Output..
print('\nOUT:')
print('name  :', font_name)
print('family:', font_family)
print('box   :',font_box)
for glyph in glyph_data:
    print('{:>4d}:{}'.format(glyph, glyph_data[glyph]))

#report.sort(key=lambda x: x[0])
for line in report:
    if report[line]:
        print(line, report[line])
