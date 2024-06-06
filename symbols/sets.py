'''
    defines the source files and glyph sets to produce for this font type
'''

fonts = [
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
    'base':list(range(0x00, 0x40)),
    'lower':list(range(0x40, 0x80)),
    'mid':list(range(0x80, 0xc0)),
    'upper':list(range(0xc0, 0x100)),
    'extended':list(range(0x100, 0xfff)),
    'all':list(range(0x00, 0xfff)),
}


