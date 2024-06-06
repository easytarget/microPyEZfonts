'''
    defines the source files and glyph sets to produce for this font type
'''

fonts = [
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
        ]

charsets = {
        'time':bytes([32] + [43] + [45] + [46] + list(range(48, 59))),
        'num':bytes([32] + [37] + list(range(40, 59)) + [176]),
        'upper':bytes(list(range(32, 96))),
        'ascii':bytes(list(range(32, 127))),
        'supp':bytes(list(range(160, 256))),
        'latin':bytes(list(range(32, 127)) + list(range(160, 256))),
        'full':bytes(list(range(0, 256)))
        }
