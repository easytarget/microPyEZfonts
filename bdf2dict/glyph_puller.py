# Raw .bdf file reader of my own.
'''
    Notes: things that proper fonts do but we cannot handle (ie. ezFBfont cannot handle)
        If glyph box is wider than the device width this means the glyph is supposed to overlap the next one. but we cant handle that properly so we widen the glyph.
        If glyph box has a negative offset this is supposed to print char to left of current pos, again we do not handle this, so the glyph is left aligned and it's device width set to the glyph box width
'''

from sys import argv

# Start stuff here
debug = True if len(argv) > 2 else False

# Main data structs
glyph_data = {}
report = {}

# Functions

# Get a named value from a set of input file lines
def get_val(block,value):
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
    # we he the EOF, ignore and treat as 'just another glyph'
    if bitmap[-1] == 'ENDFONT':
        bitmap.pop()
    # Check we have a complete char defined.
    if bitmap[-1] != 'ENDCHAR':
        print('BAD CHAR!', header)
        return None, None
    bitmap.pop()
    # Gather basics for glyph
    name = header[0]
    ordinal = int(get_val(header,'ENCODING'))
    if ordinal < 0:
        # todo, should we handle chars specified as chr(-1) etc.
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
with open(argv[1],'r') as readlines:
    bdf = readlines.read().split('STARTCHAR')
startblock = bdf.pop(0).split('\n')

# get basics
font_name = get_val(startblock, 'FONT')
font_box = [eval(i) for i in get_val(startblock, 'FONTBOUNDINGBOX').split(' ')]
font_family = get_val(startblock, 'FAMILY_NAME').strip('"')

print('startblock lines: {}, glyph entries {}'.format(len(startblock),len(bdf)))

# walk all the glyph blocks in the .bdf and save matching glyphs
for block in bdf:
    ordinal, entry = pull_glyph(block)
    if ordinal is None:
        continue
    # todo: replace with user supplied charset
    if debug and (chr(ordinal) not in ' -/(*0129aAbBpPZ'):
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
    # ToDo
    # Add any reports for the glyph..
    if len(rep) > 0:
        report[ordinal] = rep
    # Save the glyph
    glyph_data[ordinal] = entry

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
print('name  :', font_name)
print('family:', font_family)
print('box   :',font_box)
for g in list(glyph_data.keys()):
    print('{:>4d}:{}'.format(g, glyph_data[g]))

if report:
    #report.sort(key=lambda x: x[0])
    for line in report:
        print(line, report[line])
