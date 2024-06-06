'''
    This script was originally used to produce a set of Unicode symbo fonts.
    But I was unhappy with the confusion this caused in the Symbols folder.
    So it now also contains a scriptlet that generates a list to go in the
    README.md file..
'''

fonts = [
        # All the normal latin/unicode fonts
        '^cour',
        '^helv',
        '^ncen',
        '^tim',
        '^font_tiny',
        '^tom-thumb',
        '^spleen',
        '^amstrad',
        '^etl',
        #'^b\\d+', --> overheats my laptop!
        '^freedoom',
        '^unifont',
        '^\\d+x\\d+$',  # X11 fonts
        '^micro',
        # And the symbol fonts too
        '^symb',
        '^emoticons',
        '^battery',
        '^freedoom',
        '^7Segments',
        '^7_Seg',
        '^m2icon',
        '^cursor',
        '^open_iconic',
        '^u8g2_percent_circle',
        ]

charsets = {
        'arrows' : list(range(0x2190, 0x21FF)),
        'box-drawing' : list(range(0x2500, 0x257F)),
        'block-elements' : list(range(0x2580, 0x259F)),
        'geometric-shapes' : list(range(0x25A0, 0x25FF)),
        'miscellaneous-symbols' : list(range(0x2600, 0x26FF)),
        'dingbats' : list(range(0x2700, 0x27BF)),
        'braille-patterns' : list(range(0x2800, 0x28FF)),
        'musical-symbols' : list(range(0x1D100, 0x1D1FF)),
        'mahjong-tiles' : list(range(0x1F000, 0x1F02F)),
        'domino-tiles' : list(range(0x1F030, 0x1F09F)),
        'playing-cards' : list(range(0x1F0A0, 0x1F0FF)),
        'emoticons' : list(range(0x1F600, 0x1F64F)),
        'ornamental-dingbats' : list(range(0x1F650, 0x1F67F)),
        'chess-symbols' : list(range(0x1FA00, 0x1FA6F)),
        }

from os import path
print('Some common unicode symbol font blocks are:\n')
for set in charsets.keys():
    if path.isdir('../Unicode/{0}'.format(set)):
        print("* [{0}](../Unicode/{0}); chars: '0x{1:x}:0x{2:x} ({1}:{2})'".format(set, charsets[set][0], charsets[set][-1]))
print('\nThey are to be found in the [Unicode](../Unicode) folder, along with specialist mathematics and similar font sets.')
