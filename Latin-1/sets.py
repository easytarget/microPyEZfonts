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
        '^b\\d+', # --> has been known to overheat my laptop!
        '^freedoom',
        '^unifont',
        '^\\d+x\\d+$',  # X11 fonts
        '^micro',
        ]

charsets = {
        'time':list([32, 43, 45, 46] + list(range(48, 59))),
        'num':list([32, 37] + list(range(40, 59)) + [176]),
        'upper':list(range(32, 96)),
        'ascii':list(range(32, 127)),
        'supp':list(range(160, 256)),
        'latin':list(list(range(32, 127)) + list(range(160, 256))),
        'full':list(range(0, 256))
        #'basic-latin' : list(range(0x0000, 0x007F)),
        #'latin-1-supplement' : list(range(0x0080, 0x00FF)),
        'extended-a' : list(range(0x0100, 0x017F)),
        'extended-b' : list(range(0x0180, 0x024F)),
        }
