import os
import re
'''
    Indexer for Latin-1 font packs.
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
        'time':'time',
        'num':'numeric',
        'upper':'uppercase',
        'ascii':'ascii',
        'supp':'supplemental',
        'latin':'latin-1',
        'full':'full',
        }
csets = charsets.keys()
foundsets = []

# Find our font files
sources = os.scandir(sourceDir)
for family in sources:
    if family.is_dir() and (family.name != '__pycache__'):
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
                height = int(font.name.split('_')[1])
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
print('   Size{:>{}}    {:^{}}{}\n'.format('Family', famwidth, 'Name', namewidth, '(weight)'))

# Show us the money
for cset in csets:
    if cset not in foundsets:
        continue
    h = '{} character set'.format(charsets[cset].capitalize())
    print('{}\n{}'.format(h,'-' * len(h)))
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
            print('       {:>{}}{:.>{}}{}'.format(outmap[font]['family'], famwidth, font, namewidth + 2, style))
    print()
