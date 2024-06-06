'''
    defines the source files and glyph sets to produce for this font type
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
        'u-arrows' : list(range(0x2190, 0x21FF)),
        'u-box-drawing' : list(range(0x2500, 0x257F)),
        'u-block-elements' : list(range(0x2580, 0x259F)),
        'u-geometric-shapes' : list(range(0x25A0, 0x25FF)),
        'u-miscellaneous-symbols' : list(range(0x2600, 0x26FF)),
        'u-dingbats' : list(range(0x2700, 0x27BF)),
        'u-braille-patterns' : list(range(0x2800, 0x28FF)),
        'u-musical-symbols' : list(range(0x1D100, 0x1D1FF)),
        'u-mahjong-tiles' : list(range(0x1F000, 0x1F02F)),
        'u-domino-tiles' : list(range(0x1F030, 0x1F09F)),
        'u-playing-cards' : list(range(0x1F0A0, 0x1F0FF)),
        'u-emoticons' : list(range(0x1F600, 0x1F64F)),
        'u-ornamental-dingbats' : list(range(0x1F650, 0x1F67F)),
        'u-chess-symbols' : list(range(0x1FA00, 0x1FA6F)),
        }
