import os
import re
'''
    Indexer for Latin-1 font packs.
    surprisingly badly documented for one of my scripts.. sorry.
    - it is 'documented in code', I suppose.
'''
sourceDir = '.'
prefix = 'ezFBfont_'
#prefix = 'mPyEZfont_u8g2_'
csets = []
families = []
heights = []
outmap = {}
namewidth = 0
famwidth = 0

from sets import charsets

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
            if cset.name not in csets:
                csets.append(cset.name)
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

# Show us the money
for cset in csets:
    h = 'character set: {}'.format(cset.capitalize())
    print('{}\n{}'.format(h,'-' * len(h)))
    for height in heights:
        # scan matching fonts at this height)
        fontlist = []
        for font in outmap:
            if (outmap[font]['height'] == height) and (outmap[font]['cset'] == cset):
                fontlist.append(font)
        if len(fontlist) == 0:
            continue
        print('  {:3d}px :'.format(height))
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
            print('       {:>{}}{:.>{}}{}'.format(outmap[font]['family'], famwidth, font, namewidth + 1, style))
    print()
