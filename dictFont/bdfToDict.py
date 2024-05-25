from bdfparser import Font
from sys import argv

debug = argv[3] if len(argv) == 4 else False
if len(argv) < 3:
    print('Two arguments, the font file path, and the charset, are required')
    exit()

fontFile = argv[1]
charset = argv[2]

if debug:
    print('Parsing: {} with charset {}'.format(fontFile, charset))

# import the charset
with open(charset,'rb') as setfile:
    cset = setfile.read()

# import font
font = Font(argv[1])
if 'fontname' not in font.headers.keys():
    print('{}: font has no headers, skipping'.format(argv[1]))
    exit(1)

fontName = font.headers['fontname']
fontWidth = int(font.headers['fbbx'])
fontHeight = int(font.headers['fbby'])

matches = 0
maxWidth = 0
maxHeight = 0
maxDepth = 0  # ToDo; work from baseline..
fixed = True

width = {}
height = {}
origin = {}
# todo: position and baseline..
glyphDict = {}
glyphDraw = {}

font_dict_string = 'font_dict = {\n'

# find info we need:
#print(len(font.glyphs), font.glyphs.keys())
for fchar in font.glyphs.keys():
    if fchar not in range(0,256):
        continue
    if fchar in cset:
        g = font.glyphbycp(fchar)
        if len(g.meta['hexdata']) == 0:
            continue
        matches += 1
        width[fchar] = int(g.meta['bbw'])
        maxWidth = max(maxWidth, width[fchar])
        if width[fchar] != fontWidth:
            fixed = False
        height[fchar] = int(g.meta['bbh'])
        maxHeight = max(maxHeight, height[fchar])
        origin[fchar] = g.origin()
        glyphDict[fchar] = g.meta['hexdata']
        glyphDraw[fchar] = g.draw()

if matches == 0:
    print('No matches for this charset, skipping')
    exit(1)

# dump info, for present
for c in glyphDict.keys():
    #print('{}({}):  w{} h{} o{}\ndraw:\n{}\nhexdata:'
    #      .format(c, chr(c), width[c], height[c], origin[c], glyphDraw[c]))
    #print('{}({}):  w{} h{} o{}'
    #      .format(c, chr(c), width[c], height[c], origin[c]))
    print('{: 3d}: w{} h{} o{}'
          .format(c, width[c], height[c], origin[c]))
    for l in range(len(glyphDict[c])):
        glyphDict[c][l] = int(glyphDict[c][l],16)
        bintxt = '{:b}'.format(glyphDict[c][l])
        bintxt = bintxt.replace('0','.').replace('1','#')
        binpad = '.' * (fontWidth - len(bintxt))
        #print('{}{}'.format(binpad,bintxt))

    dictstring = ''
    for l in glyphDict[c]:
        dictstring += '0x{:X},'.format(l)
    font_dict_string += ' "{}":[{}]\n'.format(c, dictstring[:-1])
font_dict_string += '}'

print('\nFont: {}\nWidth: {}\nHeight: {}'.format(fontName, fontWidth, fontHeight))
print('Matching: {}'.format(matches))
print('Fixed Width: {}'.format(fixed))
print('maxWidth: {}, maxHeight: {}'.format(maxWidth, maxHeight))
print(font_dict_string)
print('Length:',len(font_dict_string))

