import os
import re
'''
    Indexer
    surprisingly badly documented for one of my scripts.. sorry.
    - it is 'documented in code', I suppose.
'''
sourceDir = '.'
prefix = 'mPyEZfont_u8g2_'
fonts = {}
heights = []
outmap = {}

charsets = {
            'e':'everything',
            'f':'full',
            'r':'readable',
            'n':'numeric',
            'u':'uppercase',
            }

fontnames = {
        'helvR':'Helvetica regular',
        'helvB':'Helvetica bold',
        'timR':'Times regular',
        'timB':'Times bold',
        'ncenR':'New Century Schoolbook regular',
        'ncenB':'New Century Schoolbook bold',
        'courR':'Courier regular',
        'courB':'Courier bold',
        'symb':'Symbols',
        '7_Seg':'7 segment display font',
        '7Seg':'7 segment display font',
        'spleen':'Spleen small display fonts',
        'freedoom':'Doom!',
        'cursor':'Cursors',
        'battery':'Battery level indicator',
        'u8g2':'U8G2 native font',
        'u8glib':'U8G2 native font',
        'font_tiny5':'Tiny fonts',
        'tom_thumb':'Tom Thumb fonts',
        'emoticons':'Emoticon font',
        'unifont':'GNU unicode font',
        }

def mapfont(name, height):
    n = name[:-2]
    s = name[-1:]
    if (name[-2:-1] != '_') or (s not in 'rfneu'):
        print('Not a font: ' + height + '/' + name)
        return
    if n not in outmap[height].keys():
        outmap[height][n] = s
    else:
        outmap[height][n] = outmap[height][n] + s

# Find our font files
sources = os.scandir(sourceDir)
for i in sources:
    if i.is_dir():
        if i.name.isnumeric():
            fonts[i.name] = []
            outmap[i.name] = {}
            heights.append(int(i.name))
            fontlist = os.scandir(i.name)
            for f in fontlist:
                fonts[i.name].append(f.name)

# tease details from each font name, in height order`
heights.sort()
for height in heights:
    for font in fonts[str(height)]:
        name = font.removeprefix(prefix).removesuffix('.py')
        mapfont(name,str(height))

# sort each font set list alphabetically
# and find the longest font name length
widest = 0
for height in heights:
    for name in outmap[str(height)]:
        outmap[str(height)][name] = ''.join(sorted(outmap[str(height)][name]))
        widest = len(name) if len(name) > widest else widest

# Show us the money
for height in heights:
    print('{:>3}px:'.format(height))
    #print(list(sorted(outmap[str(height)].keys())))
    #continue
    for font in sorted(outmap[str(height)].keys()):
        print('    ' + font + '.' * (widest - len(font)), end=' ')
        named = False
        for name in fontnames:
            if font[:len(name)] == name:
                print(fontnames[name], end='')
                named = True
                break
        if not named:
            if  font[:1].isnumeric():
                print('U8G2 default font', end='')
            else:
                print('unknown font', end='')
        print(' (', end='')
        sets = ''
        for char in outmap[str(height)][font]:
            sets = sets + charsets[char] + ', '
        print(sets[:-2] + ')')
