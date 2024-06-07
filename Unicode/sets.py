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
        'ipa-extensions' : list(range(0x0250, 0x02AF)),
        'spacing-modifier-letters' : list(range(0x02B0, 0x02FF)),
        'combining-diacritical-marks' : list(range(0x0300, 0x036F)),
        'greek-and-coptic' : list(range(0x0370, 0x03FF)),
        'cyrillic' : list(range(0x0400, 0x04FF)),
        'cyrillic-supplement' : list(range(0x0500, 0x052F)),
        'armenian' : list(range(0x0530, 0x058F)),
        'hebrew' : list(range(0x0590, 0x05FF)),
        'arabic' : list(range(0x0600, 0x06FF)),
        'syriac' : list(range(0x0700, 0x074F)),
        'arabic-supplement' : list(range(0x0750, 0x077F)),
        'thaana' : list(range(0x0780, 0x07BF)),
        'nko' : list(range(0x07C0, 0x07FF)),
        'samaritan' : list(range(0x0800, 0x083F)),
        'mandaic' : list(range(0x0840, 0x085F)),
        'syriac-supplement' : list(range(0x0860, 0x086F)),
        'arabic-extended-a' : list(range(0x08A0, 0x08FF)),
        'devanagari' : list(range(0x0900, 0x097F)),
        'bengali' : list(range(0x0980, 0x09FF)),
        'gurmukhi' : list(range(0x0A00, 0x0A7F)),
        'gujarati' : list(range(0x0A80, 0x0AFF)),
        'oriya' : list(range(0x0B00, 0x0B7F)),
        'tamil' : list(range(0x0B80, 0x0BFF)),
        'telugu' : list(range(0x0C00, 0x0C7F)),
        'kannada' : list(range(0x0C80, 0x0CFF)),
        'malayalam' : list(range(0x0D00, 0x0D7F)),
        'sinhala' : list(range(0x0D80, 0x0DFF)),
        'thai' : list(range(0x0E00, 0x0E7F)),
        'lao' : list(range(0x0E80, 0x0EFF)),
        'tibetan' : list(range(0x0F00, 0x0FFF)),
        'myanmar' : list(range(0x1000, 0x109F)),
        'georgian' : list(range(0x10A0, 0x10FF)),
        'hangul-jamo' : list(range(0x1100, 0x11FF)),
        'ethiopic' : list(range(0x1200, 0x137F)),
        'ethiopic-supplement' : list(range(0x1380, 0x139F)),
        'cherokee' : list(range(0x13A0, 0x13FF)),
        'unified-canadian-aboriginal-syllabics' : list(range(0x1400, 0x167F)),
        'ogham' : list(range(0x1680, 0x169F)),
        'runic' : list(range(0x16A0, 0x16FF)),
        'tagalog' : list(range(0x1700, 0x171F)),
        'hanunoo' : list(range(0x1720, 0x173F)),
        'buhid' : list(range(0x1740, 0x175F)),
        'tagbanwa' : list(range(0x1760, 0x177F)),
        'khmer' : list(range(0x1780, 0x17FF)),
        'mongolian' : list(range(0x1800, 0x18AF)),
        'unified-canadian-aboriginal-syllabics-extended' : list(range(0x18B0, 0x18FF)),
        'limbu' : list(range(0x1900, 0x194F)),
        'tai-le' : list(range(0x1950, 0x197F)),
        'new-tai-lue' : list(range(0x1980, 0x19DF)),
        'khmer-symbols' : list(range(0x19E0, 0x19FF)),
        'buginese' : list(range(0x1A00, 0x1A1F)),
        'tai-tham' : list(range(0x1A20, 0x1AAF)),
        'combining-diacritical-marks-extended' : list(range(0x1AB0, 0x1AFF)),
        'balinese' : list(range(0x1B00, 0x1B7F)),
        'sundanese' : list(range(0x1B80, 0x1BBF)),
        'batak' : list(range(0x1BC0, 0x1BFF)),
        'lepcha' : list(range(0x1C00, 0x1C4F)),
        'ol-chiki' : list(range(0x1C50, 0x1C7F)),
        'cyrillic-extended-c' : list(range(0x1C80, 0x1C8F)),
        'georgian-extended' : list(range(0x1C90, 0x1CBF)),
        'sundanese-supplement' : list(range(0x1CC0, 0x1CCF)),
        'vedic-extensions' : list(range(0x1CD0, 0x1CFF)),
        'phonetic-extensions' : list(range(0x1D00, 0x1D7F)),
        'phonetic-extensions-supplement' : list(range(0x1D80, 0x1DBF)),
        'combining-diacritical-marks-supplement' : list(range(0x1DC0, 0x1DFF)),
        'latin-extended-additional' : list(range(0x1E00, 0x1EFF)),
        'greek-extended' : list(range(0x1F00, 0x1FFF)),
        'general-punctuation' : list(range(0x2000, 0x206F)),
        'superscripts-and-subscripts' : list(range(0x2070, 0x209F)),
        'currency-symbols' : list(range(0x20A0, 0x20CF)),
        'combining-diacritical-marks-for-symbols' : list(range(0x20D0, 0x20FF)),
        'letterlike-symbols' : list(range(0x2100, 0x214F)),
        'number-forms' : list(range(0x2150, 0x218F)),
        'arrows' : list(range(0x2190, 0x21FF)),
        'mathematical-operators' : list(range(0x2200, 0x22FF)),
        'miscellaneous-technical' : list(range(0x2300, 0x23FF)),
        'control-pictures' : list(range(0x2400, 0x243F)),
        'optical-character-recognition' : list(range(0x2440, 0x245F)),
        'enclosed-alphanumerics' : list(range(0x2460, 0x24FF)),
        'box-drawing' : list(range(0x2500, 0x257F)),
        'block-elements' : list(range(0x2580, 0x259F)),
        'geometric-shapes' : list(range(0x25A0, 0x25FF)),
        'miscellaneous-symbols' : list(range(0x2600, 0x26FF)),
        'dingbats' : list(range(0x2700, 0x27BF)),
        'miscellaneous-mathematical-symbols-a' : list(range(0x27C0, 0x27EF)),
        'supplemental-arrows-a' : list(range(0x27F0, 0x27FF)),
        'braille-patterns' : list(range(0x2800, 0x28FF)),
        'supplemental-arrows-b' : list(range(0x2900, 0x297F)),
        'miscellaneous-mathematical-symbols-b' : list(range(0x2980, 0x29FF)),
        'supplemental-mathematical-operators' : list(range(0x2A00, 0x2AFF)),
        'miscellaneous-symbols-and-arrows' : list(range(0x2B00, 0x2BFF)),
        'glagolitic' : list(range(0x2C00, 0x2C5F)),
        'latin-extended-c' : list(range(0x2C60, 0x2C7F)),
        'coptic' : list(range(0x2C80, 0x2CFF)),
        'georgian-supplement' : list(range(0x2D00, 0x2D2F)),
        'tifinagh' : list(range(0x2D30, 0x2D7F)),
        'ethiopic-extended' : list(range(0x2D80, 0x2DDF)),
        'cyrillic-extended-a' : list(range(0x2DE0, 0x2DFF)),
        'supplemental-punctuation' : list(range(0x2E00, 0x2E7F)),
        'cjk-radicals-supplement' : list(range(0x2E80, 0x2EFF)),
        'kangxi-radicals' : list(range(0x2F00, 0x2FDF)),
        'ideographic-description-characters' : list(range(0x2FF0, 0x2FFF)),
        'cjk-symbols-and-punctuation' : list(range(0x3000, 0x303F)),
        'hiragana' : list(range(0x3040, 0x309F)),
        'katakana' : list(range(0x30A0, 0x30FF)),
        'bopomofo' : list(range(0x3100, 0x312F)),
        'hangul-compatibility-jamo' : list(range(0x3130, 0x318F)),
        'kanbun' : list(range(0x3190, 0x319F)),
        'bopomofo-extended' : list(range(0x31A0, 0x31BF)),
        'cjk-strokes' : list(range(0x31C0, 0x31EF)),
        'katakana-phonetic-extensions' : list(range(0x31F0, 0x31FF)),
        'enclosed-cjk-letters-and-months' : list(range(0x3200, 0x32FF)),
        'cjk-compatibility' : list(range(0x3300, 0x33FF)),
        'cjk-unified-ideographs-extension-a' : list(range(0x3400, 0x4DBF)),
        'yijing-hexagram-symbols' : list(range(0x4DC0, 0x4DFF)),
        'cjk-unified-ideographs' : list(range(0x4E00, 0x9FFF)),
        'yi-syllables' : list(range(0xA000, 0xA48F)),
        'yi-radicals' : list(range(0xA490, 0xA4CF)),
        'lisu' : list(range(0xA4D0, 0xA4FF)),
        'vai' : list(range(0xA500, 0xA63F)),
        'cyrillic-extended-b' : list(range(0xA640, 0xA69F)),
        'bamum' : list(range(0xA6A0, 0xA6FF)),
        'modifier-tone-letters' : list(range(0xA700, 0xA71F)),
        'latin-extended-d' : list(range(0xA720, 0xA7FF)),
        'syloti-nagri' : list(range(0xA800, 0xA82F)),
        'common-indic-number-forms' : list(range(0xA830, 0xA83F)),
        'phags-pa' : list(range(0xA840, 0xA87F)),
        'saurashtra' : list(range(0xA880, 0xA8DF)),
        'devanagari-extended' : list(range(0xA8E0, 0xA8FF)),
        'kayah-li' : list(range(0xA900, 0xA92F)),
        'rejang' : list(range(0xA930, 0xA95F)),
        'hangul-jamo-extended-a' : list(range(0xA960, 0xA97F)),
        'javanese' : list(range(0xA980, 0xA9DF)),
        'myanmar-extended-b' : list(range(0xA9E0, 0xA9FF)),
        'cham' : list(range(0xAA00, 0xAA5F)),
        'myanmar-extended-a' : list(range(0xAA60, 0xAA7F)),
        'tai-viet' : list(range(0xAA80, 0xAADF)),
        'meetei-mayek-extensions' : list(range(0xAAE0, 0xAAFF)),
        'ethiopic-extended-a' : list(range(0xAB00, 0xAB2F)),
        'latin-extended-e' : list(range(0xAB30, 0xAB6F)),
        'cherokee-supplement' : list(range(0xAB70, 0xABBF)),
        'meetei-mayek' : list(range(0xABC0, 0xABFF)),
        'hangul-syllables' : list(range(0xAC00, 0xD7AF)),
        'hangul-jamo-extended-b' : list(range(0xD7B0, 0xD7FF)),
        'high-surrogates' : list(range(0xD800, 0xDB7F)),
        'high-private-use-surrogates' : list(range(0xDB80, 0xDBFF)),
        'low-surrogates' : list(range(0xDC00, 0xDFFF)),
        'private-use-area' : list(range(0xE000, 0xF8FF)),
        'cjk-compatibility-ideographs' : list(range(0xF900, 0xFAFF)),
        'alphabetic-presentation-forms' : list(range(0xFB00, 0xFB4F)),
        'arabic-presentation-forms-a' : list(range(0xFB50, 0xFDFF)),
        'variation-selectors' : list(range(0xFE00, 0xFE0F)),
        'vertical-forms' : list(range(0xFE10, 0xFE1F)),
        'combining-half-marks' : list(range(0xFE20, 0xFE2F)),
        'cjk-compatibility-forms' : list(range(0xFE30, 0xFE4F)),
        'small-form-variants' : list(range(0xFE50, 0xFE6F)),
        'arabic-presentation-forms-b' : list(range(0xFE70, 0xFEFF)),
        'halfwidth-and-fullwidth-forms' : list(range(0xFF00, 0xFFEF)),
        'specials' : list(range(0xFFF0, 0xFFFF)),
        'linear-b-syllabary' : list(range(0x10000, 0x1007F)),
        'linear-b-ideograms' : list(range(0x10080, 0x100FF)),
        'aegean-numbers' : list(range(0x10100, 0x1013F)),
        'ancient-greek-numbers' : list(range(0x10140, 0x1018F)),
        'ancient-symbols' : list(range(0x10190, 0x101CF)),
        'phaistos-disc' : list(range(0x101D0, 0x101FF)),
        'lycian' : list(range(0x10280, 0x1029F)),
        'carian' : list(range(0x102A0, 0x102DF)),
        'coptic-epact-numbers' : list(range(0x102E0, 0x102FF)),
        'old-italic' : list(range(0x10300, 0x1032F)),
        'gothic' : list(range(0x10330, 0x1034F)),
        'old-permic' : list(range(0x10350, 0x1037F)),
        'ugaritic' : list(range(0x10380, 0x1039F)),
        'old-persian' : list(range(0x103A0, 0x103DF)),
        'deseret' : list(range(0x10400, 0x1044F)),
        'shavian' : list(range(0x10450, 0x1047F)),
        'osmanya' : list(range(0x10480, 0x104AF)),
        'osage' : list(range(0x104B0, 0x104FF)),
        'elbasan' : list(range(0x10500, 0x1052F)),
        'caucasian-albanian' : list(range(0x10530, 0x1056F)),
        'linear-a' : list(range(0x10600, 0x1077F)),
        'cypriot-syllabary' : list(range(0x10800, 0x1083F)),
        'imperial-aramaic' : list(range(0x10840, 0x1085F)),
        'palmyrene' : list(range(0x10860, 0x1087F)),
        'nabataean' : list(range(0x10880, 0x108AF)),
        'hatran' : list(range(0x108E0, 0x108FF)),
        'phoenician' : list(range(0x10900, 0x1091F)),
        'lydian' : list(range(0x10920, 0x1093F)),
        'meroitic-hieroglyphs' : list(range(0x10980, 0x1099F)),
        'meroitic-cursive' : list(range(0x109A0, 0x109FF)),
        'kharoshthi' : list(range(0x10A00, 0x10A5F)),
        'old-south-arabian' : list(range(0x10A60, 0x10A7F)),
        'old-north-arabian' : list(range(0x10A80, 0x10A9F)),
        'manichaean' : list(range(0x10AC0, 0x10AFF)),
        'avestan' : list(range(0x10B00, 0x10B3F)),
        'inscriptional-parthian' : list(range(0x10B40, 0x10B5F)),
        'inscriptional-pahlavi' : list(range(0x10B60, 0x10B7F)),
        'psalter-pahlavi' : list(range(0x10B80, 0x10BAF)),
        'old-turkic' : list(range(0x10C00, 0x10C4F)),
        'old-hungarian' : list(range(0x10C80, 0x10CFF)),
        'hanifi-rohingya' : list(range(0x10D00, 0x10D3F)),
        'rumi-numeral-symbols' : list(range(0x10E60, 0x10E7F)),
        'old-sogdian' : list(range(0x10F00, 0x10F2F)),
        'sogdian' : list(range(0x10F30, 0x10F6F)),
        'elymaic' : list(range(0x10FE0, 0x10FFF)),
        'brahmi' : list(range(0x11000, 0x1107F)),
        'kaithi' : list(range(0x11080, 0x110CF)),
        'sora-sompeng' : list(range(0x110D0, 0x110FF)),
        'chakma' : list(range(0x11100, 0x1114F)),
        'mahajani' : list(range(0x11150, 0x1117F)),
        'sharada' : list(range(0x11180, 0x111DF)),
        'sinhala-archaic-numbers' : list(range(0x111E0, 0x111FF)),
        'khojki' : list(range(0x11200, 0x1124F)),
        'multani' : list(range(0x11280, 0x112AF)),
        'khudawadi' : list(range(0x112B0, 0x112FF)),
        'grantha' : list(range(0x11300, 0x1137F)),
        'newa' : list(range(0x11400, 0x1147F)),
        'tirhuta' : list(range(0x11480, 0x114DF)),
        'siddham' : list(range(0x11580, 0x115FF)),
        'modi' : list(range(0x11600, 0x1165F)),
        'mongolian-supplement' : list(range(0x11660, 0x1167F)),
        'takri' : list(range(0x11680, 0x116CF)),
        'ahom' : list(range(0x11700, 0x1173F)),
        'dogra' : list(range(0x11800, 0x1184F)),
        'warang-citi' : list(range(0x118A0, 0x118FF)),
        'nandinagari' : list(range(0x119A0, 0x119FF)),
        'zanabazar-square' : list(range(0x11A00, 0x11A4F)),
        'soyombo' : list(range(0x11A50, 0x11AAF)),
        'pau-cin-hau' : list(range(0x11AC0, 0x11AFF)),
        'bhaiksuki' : list(range(0x11C00, 0x11C6F)),
        'marchen' : list(range(0x11C70, 0x11CBF)),
        'masaram-gondi' : list(range(0x11D00, 0x11D5F)),
        'gunjala-gondi' : list(range(0x11D60, 0x11DAF)),
        'makasar' : list(range(0x11EE0, 0x11EFF)),
        'tamil-supplement' : list(range(0x11FC0, 0x11FFF)),
        'cuneiform' : list(range(0x12000, 0x123FF)),
        'cuneiform-numbers-and-punctuation' : list(range(0x12400, 0x1247F)),
        'early-dynastic-cuneiform' : list(range(0x12480, 0x1254F)),
        'egyptian-hieroglyphs' : list(range(0x13000, 0x1342F)),
        'egyptian-hieroglyph-format-controls' : list(range(0x13430, 0x1343F)),
        'anatolian-hieroglyphs' : list(range(0x14400, 0x1467F)),
        'bamum-supplement' : list(range(0x16800, 0x16A3F)),
        'mro' : list(range(0x16A40, 0x16A6F)),
        'bassa-vah' : list(range(0x16AD0, 0x16AFF)),
        'pahawh-hmong' : list(range(0x16B00, 0x16B8F)),
        'medefaidrin' : list(range(0x16E40, 0x16E9F)),
        'miao' : list(range(0x16F00, 0x16F9F)),
        'ideographic-symbols-and-punctuation' : list(range(0x16FE0, 0x16FFF)),
        'tangut' : list(range(0x17000, 0x187FF)),
        'tangut-components' : list(range(0x18800, 0x18AFF)),
        'kana-supplement' : list(range(0x1B000, 0x1B0FF)),
        'kana-extended-a' : list(range(0x1B100, 0x1B12F)),
        'small-kana-extension' : list(range(0x1B130, 0x1B16F)),
        'nushu' : list(range(0x1B170, 0x1B2FF)),
        'duployan' : list(range(0x1BC00, 0x1BC9F)),
        'shorthand-format-controls' : list(range(0x1BCA0, 0x1BCAF)),
        'byzantine-musical-symbols' : list(range(0x1D000, 0x1D0FF)),
        'musical-symbols' : list(range(0x1D100, 0x1D1FF)),
        'ancient-greek-musical-notation' : list(range(0x1D200, 0x1D24F)),
        'mayan-numerals' : list(range(0x1D2E0, 0x1D2FF)),
        'tai-xuan-jing-symbols' : list(range(0x1D300, 0x1D35F)),
        'counting-rod-numerals' : list(range(0x1D360, 0x1D37F)),
        'mathematical-alphanumeric-symbols' : list(range(0x1D400, 0x1D7FF)),
        'sutton-signwriting' : list(range(0x1D800, 0x1DAAF)),
        'glagolitic-supplement' : list(range(0x1E000, 0x1E02F)),
        'nyiakeng-puachue-hmong' : list(range(0x1E100, 0x1E14F)),
        'wancho' : list(range(0x1E2C0, 0x1E2FF)),
        'mende-kikakui' : list(range(0x1E800, 0x1E8DF)),
        'adlam' : list(range(0x1E900, 0x1E95F)),
        'indic-siyaq-numbers' : list(range(0x1EC70, 0x1ECBF)),
        'ottoman-siyaq-numbers' : list(range(0x1ED00, 0x1ED4F)),
        'arabic-mathematical-alphabetic-symbols' : list(range(0x1EE00, 0x1EEFF)),
        'mahjong-tiles' : list(range(0x1F000, 0x1F02F)),
        'domino-tiles' : list(range(0x1F030, 0x1F09F)),
        'playing-cards' : list(range(0x1F0A0, 0x1F0FF)),
        'enclosed-alphanumeric-supplement' : list(range(0x1F100, 0x1F1FF)),
        'enclosed-ideographic-supplement' : list(range(0x1F200, 0x1F2FF)),
        'miscellaneous-symbols-and-pictographs' : list(range(0x1F300, 0x1F5FF)),
        'emoticons' : list(range(0x1F600, 0x1F64F)),
        'ornamental-dingbats' : list(range(0x1F650, 0x1F67F)),
        'transport-and-map-symbols' : list(range(0x1F680, 0x1F6FF)),
        'alchemical-symbols' : list(range(0x1F700, 0x1F77F)),
        'geometric-shapes-extended' : list(range(0x1F780, 0x1F7FF)),
        'supplemental-arrows-c' : list(range(0x1F800, 0x1F8FF)),
        'supplemental-symbols-and-pictographs' : list(range(0x1F900, 0x1F9FF)),
        'chess-symbols' : list(range(0x1FA00, 0x1FA6F)),
        'symbols-and-pictographs-extended-a' : list(range(0x1FA70, 0x1FAFF)),
        'cjk-unified-ideographs-extension-b' : list(range(0x20000, 0x2A6DF)),
        'cjk-unified-ideographs-extension-c' : list(range(0x2A700, 0x2B73F)),
        'cjk-unified-ideographs-extension-d' : list(range(0x2B740, 0x2B81F)),
        'cjk-unified-ideographs-extension-e' : list(range(0x2B820, 0x2CEAF)),
        'cjk-unified-ideographs-extension-f' : list(range(0x2CEB0, 0x2EBEF)),
        'cjk-compatibility-ideographs-supplement' : list(range(0x2F800, 0x2FA1F)),
        'tags' : list(range(0xE0000, 0xE007F)),
        'variation-selectors-supplement' : list(range(0xE0100, 0xE01EF)),
        'supplementary-private-use-area-a' : list(range(0xF0000, 0xFFFFF)),
        'supplementary-private-use-area-b' : list(range(0x100000, 0x10FFFF)),
        }
