import os
import re
'''
    Indexer for Symbol font packs.
    surprisingly badly documented for one of my scripts.. sorry.
    - it is 'documented in code', I suppose.
'''
sourceDir = '.'
prefix = 'ezFBfont_'
dirname = os.getcwd().split('/')[-1]

families = []
heights = []
outmap = {}
namewidth = 0
famwidth = 0

charsets = {
        'base':'base (0x00 - 0x3F)',
        'lower':'lower (0x40 - 0x7F)',
        'mid':'mid (0x80 - 0xBF)',
        'upper':'upper (0xC0 - 0xFF)',
        'extended':'extended (0x100 - 0xFFF)',
        'full':'full (0x00 - 0xFFF)',
        }
csets = charsets.keys()
foundsets = []

# Find our font files
sources = os.scandir(sourceDir)
for family in sources:
    if family.is_dir() and (family.name != '__pycache__') and family.name[0].islower():
        famname = family.name.replace('new-century-','').replace('-extended','')
        if famname not in families:
            families.append(famname)
        famwidth = max(famwidth, len(famname))
        setlist = os.scandir(family)
        for cset in setlist:
            if cset.name not in charsets.keys():
                print('unknown: set "{}" in {}'.format(cset.name, famname))
                continue
            if cset.name not in foundsets:
                foundsets.append(cset.name)
            for font in os.scandir(cset):
                if font.name[:len(prefix)] != prefix:
                    continue
                namewidth = max(namewidth, len(font.name))
                height = int(font.name.split('_')[-1].split('.')[0])
                if height not in heights:
                    heights.append(height)
                outmap[font.name] =  {'family':famname,
                                           'cset':cset.name,
                                           'height':height}
heights.sort()
families.sort()

if len(foundsets) == 0:
    # nothing found; simply exit
    exit()

print('Micropython font module tree for: {}\n'.format(dirname))
cols = 'Size:  {:>{}}  {:>{}}'.format('Family', famwidth, 'Name', namewidth)

# Show us the money
for cset in csets:
    if cset not in foundsets:
        continue
    h = '{} character set'.format(charsets[cset].capitalize())
    print('{}\n{}\n{}'.format(h, '-' * len(h), cols))
    for height in heights:
        # scan matching fonts at this height)
        fontlist = []
        for font in outmap:
            if (outmap[font]['height'] == height) and (outmap[font]['cset'] == cset):
                fontlist.append(font)
        if len(fontlist) == 0:
            continue
        print('  {:3d}px:'.format(height))
        for font in fontlist:
            famstr = font.split('_')[2:-1]
            if 'B' in famstr[0]:
                style = ' (bold)'
            elif 'R' in famstr[0]:
                style = ' (regular)'
            elif famstr[-1] == 'b':
                style = ' (bold)'
            else:
                style = ''
            print('       {:>{}}  {:.>{}}{}'.format(outmap[font]['family'], famwidth, font, namewidth, style))
    print()
