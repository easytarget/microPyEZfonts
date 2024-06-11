'''
    defines the source files and glyph sets to produce for this font type
'''

fonts = [
        '^helv',
        '^spleen',
        ]

charsets = {
        'time':list([32, 43, 45, 46] + list(range(48, 59))),
        'num':list([32, 37] + list(range(40, 59)) + [176]),
        'upper':list(range(32, 96)),
        'ascii':list(range(32, 127)),
        'supp':list(range(160, 256)),
        'latin':list(list(range(32, 127)) + list(range(160, 256))),
        'full':list(range(0, 256))
        }
