# Unicode Fonts
### [unicode.org](https://home.unicode.org/)

This folder contains instructions and examples for producing custom Unicode font files suitable for use with `ezFBfont`.

There are many thousands of characters and glyphs in the Unicode character set, it is impractical to pre-prepare font files that contain usable & useful character sets, yet are small enough to fit on a micropython device.

Instead; this is a guide to producing a custom font pack with just the characters and symbols *you* need for *your* project.

## Unicode font sources:
Two Unicode font sets are provided here:
* The Electronic Font Open Laboratory [efont](https://openlab.ring.gr.jp/efont/)
  * [Downloads](https://openlab.ring.gr.jp/efont/dist/unicode-bdf/).
  * These have multiple heights, and bold/italic variants.
  * Fixed-width and bi-width versions
  * Partial; ~25k glyphs focussed on oriental and asian blocks.
* GNU [unifont](https://savannah.gnu.org/projects/unifont)
  * Downloads at [unifoundry](https://unifoundry.com/unifont/).
  * Only available as 16px height, 8px / 16px bi-width.
  * Complete; 65534 glyphs covering all blocks.

Additionally: The Fixed and X11 fonts in the [Latin-1](../Latin-1/Latin-1-bdf-sources) folder (Helvetica, Times, Courier, Schoolbook and the fixed fonts) all have some Unicode glyphs as part of the extended Latin-1 blocks.

# COPYRIGHT
Both Unicode fonts here are open source projects and have permissive licencing; but they **do** have licence terms and some restrictions:
* Please read the copyright notice in the efont folder; and ensure you follow any restrictions and requirements there if you redistribute fonts based on this set; see [efont-unicode-bdf-0.4.2/COPYRIGHT](efont-unicode-bdf-0.4.2/COPYRIGHT)
* The Unifont is dual licenced (SIL and GPL2 with font exceptions); see https://unifoundry.com/LICENSE.txt

# Example

The following is a walkthrough of using `bdf2dict` to create a simple Unicode font pack for a simple app.

## Requirements
To run the tool you need a desktop/laptop system with a working python3.7+ install, and this repository cloned or unpacked.

Next we will need a list of characters to add to the font!
* The easiest way to do this is to create a 'charset' file with the characters you want in it.

For this example I have a file which says 'Hello' in simplified Chinese followed by a newline and 'microPython' with a 'µ'.

```console
user@pc:~/MPython/uniProj$ cat unicode.txt
```
```
你好
µPython
```

(You can also provide the charset as a string, via stdin or a user prompt. see the *bdf2dict* readme for more.)

Now we need to prepare our font module file using `bdf2dict`.

In this example I have cloned the *ezFBfont* repo alongside a folder for my project on my PC, and used relative paths for the tool and font source.

The font module file is generated and saved in the local working directory, then copied to the target device via the IDE (or whatever method used).

See the [`bdf2dict`](../BDF2DICT.md) page to understand the options used here; we are using the unifont `.bdf` file, prefixing our output files with `my_`, and passing the charset in a (unicode) text file.

```console
user@pc:~/MPython/uniProj$ python ../microPyEZfonts/bdf2dict.py ../microPyEZfonts/Unicode/unifont_15.1.05/unifont-15.1.05.bdf my_ unicode.txt 
bdf2dict.py: processing ../microPyEZfonts/Unicode/unifont_15.1.05/unifont-15.1.05.bdf
10 Matching characters rendered to my_unifont_15_1_05.py

user@pc:~/MPython/uniProj$ ll
total 48
-rw-r--r--. 1 owen owen 3212 Jul  5 16:38 my_unifont_15_1_05.map
-rw-r--r--. 1 owen owen 1854 Jul  5 16:38 my_unifont_15_1_05.py
-rw-r--r--. 1 owen owen   15 Jul  5 16:38 my_unifont_15_1_05.set
-rw-r--r--. 1 owen owen   16 Jul  5 16:16 unicode.txt
```
The font itself is in the `.py` file, the `.map` file has a summary of the glyphs and the `.set` file all the unique characters (the last two are just for reference, they do not belong in your project folder..)

## App

Having made the font we need an app that uses it.

If you do not (yet) have your own app the following is a simple example; it uses a ssd_1306 OLED display connected via I2C on a ESP32 / RP2040 default pins.
* A 'more complete' version of this is in the examples folder,
* that example has defaults for esp8266 and sh1106/st7567 displays.
* for other displays you will need to find drivers etc and adapt the following as necesscary.

Demo code example:

```console
user@pc:~/MPython/uniProj$ cat uniProj-i2c.py
```
```python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from ezFBfont import ezFBfont

import my_unifont_15_1_05 as unicode_font

# HW
#SDA = 28  # default rp2040
#SCL = 29  # default rp2040
SDA = 21  # default esp32
SCL = 22  # default esp32
i2c=I2C(0,sda=Pin(SDA), scl=Pin(SCL))

# Display
display = SSD1306_I2C(128, 64, i2c, addr=0x3c)

# Font Init
font = ezFBfont(display, unicode_font,
                halign='center',
                valign='center',
                hgap=1,
                verbose=True)

# Write (stripping trailing newlines)
with open('unicode.txt','r') as text:
    font.write(text.read().strip('\n'), 63, 31)
display.show()
```

You need to copy the `ezFBfont.py` and `ssd1306.py` class libraries into the project via the file dialog in your IDE or whatever method you use.

We should be able to run the demo now: 
* Copy the `my_unifont_15_1_05.py` font file we created above, and `unicode.txt` to your project
* Run `uniProj-i2c.py` (or whatever your app is called.

## REPL

It is possible to test using the [console/repl framebuffer driver](../drivers/repl_1306.py).

This can be a good method for fast testing and developing without needing actual hardware.

You need to have a commandline port of MicroPython available, on Linux (RH/Fedora/Ubuntu/Debian) install 'micropython' via the package manager, it can then be run from the commandline. There *is* a windows port of micropython but it is a work-in-progress, see the micropython documentation for more.

The following has been tested with micopython 1.23 on Fedora40, Ubuntu24.04, FreeBSD14.1 and in the repl console of an ESP32 devboard.
```console
user@pc:~/MPython/uniProj$ cp ../microPyEZfonts/ezFBfont.py .
user@pc:~/MPython/uniProj$ cp ../microPyEZfonts/drivers/repl_1306.py .
```

The script is slightly different since it does not have a physical display.

```console
user@pc:~/MPython/uniProj$ cat uniProj-repl.py
```
```
from repl_1306 import REPL_1306
from ezFBfont import ezFBfont

import my_unifont_15_1_05 as unicode_font

display = REPL_1306(80, 37)

# Font Init
font = ezFBfont(display, unicode_font,
                halign='center', valign='center',
                hgap=1,
                verbose=True)

# Write (stripping trailing newlines)
with open('unicode.txt','r') as text:
    font.write(text.read().strip('\n'), 39, 17)
display.show()
```
run the script:

NOTE: *Some* web browsers (cough, Chrome on Android, cough) render the following badly since their 'monospaced' fonts are not very 'mono', just 'spaced'.
```console
user@pc:~/MPython/uniProj$ micropython uniProj-repl.py 
repl_1306: init 81x37
my_unifont_15_1_05 : initialised: height: 16, max width: 16, baseline: 14
my_unifont_15_1_05 = fg: 1, bg: 0, tkey: -1, halign: center, valign: center, hgap: 1, vgap: 0
repl_1306: show
                          ▄   ▄           ▄                                      
                          █   █           █    ▀▀▀▀▀█                            
                         █   █▀▀▀▀▀▀█  ▄▄▄█▄▄     ▄▀                             
                        ██ ▄▀   ▄  ▀     █  █    █                               
                      ▄▀ █   ▄  █ ▄      █  █ ▀▀▀█▀▀▀▀                           
                         █  ▄▀  █  █    ▀▄ █     █                               
                         █ ▄▀   █   █    ▄▀▄     █                               
                         █    ▄ █      ▄▀   █  ▄ █                               
                         ▀     ▀                ▀                                
                                                                                 
                  ▄▄▄▄▄               ▄      █                                   
         ▄    ▄   █    █   ▄    ▄     █      █ ▄▄▄     ▄▄▄▄    ▄ ▄▄▄             
         █    █   █▄▄▄▄▀   █    █   ▀▀█▀▀    █▀   █   █    █   █▀   █            
         █    █   █        █    █     █      █    █   █    █   █    █            
         █▄  ▄█   █         ▀▄▄▀█     █      █    █   █    █   █    █            
         █ ▀▀  ▀  ▀             █      ▀▀    ▀    ▀    ▀▀▀▀    ▀    ▀            
        ▀                   ▀▀▀▀                                                 
                                                                                 
                                                                                 
```
# Experiment!

The efont collection has bold and italic fonts, trying it is easy:
```console
user@pc:~/MPython/uniProj$ python ../microPyEZfonts/bdf2dict.py ../microPyEZfonts/Unicode/efont-unicode-bdf-0.4.2/b16_b.bdf my_ unicode.txt 
bdf2dict.py: processing ../microPyEZfonts/Unicode/efont-unicode-bdf-0.4.2/b16_b.bdf
9 Matching characters rendered to my_b16_b.py
```
edit the font line in your code to read:

`import my_b16_b as unicode_font`

and try it out:
```console
user@pc:~/MPython/uniProj$ micropython uniProj-repl.py 
repl_1306: init 80x37
my_b16_b : initialised: height: 16, max width: 16, baseline: 14
my_b16_b = fg: 1, bg: 0, tkey: -1, halign: center, valign: center, hgap: 1, vgap: 0
repl_1306: show
                          ▄▄ ▄▄           ▄▄                                    
                         ▄██ ██           ██   ▀▀▀▀▀██                          
                        ▄██ ██▀▀██▀▀██ ▄▄▄██▄▄▄   ▄█▀                           
                       ▄██ ▀▀▀  ██ ██▀   ██ ██   ▄█▀                            
                      ██▀█   ▄▄ ██ ▄▄    ██ ██▀▀▀██▀▀▀▀                         
                        ██   ██ ██ ██   ██▄▄█▀   ██                             
                        ██  ██▀ ██ ▀██  ▀▀▄█▀█▄  ██                             
                        ██      ██     ▄▄█▀      ██                             
                        ▀▀    ▀▀▀▀              ▀▀▀                             
                                                                                
                 ▄▄▄▄▄▄              ▄▄     ██                                  
                 ██   ██  ▄▄   ▄▄  ▄▄██▄▄   ██ ▄▄▄    ▄▄▄▄▄   ▄▄ ▄▄▄            
         ▄▄  ▄▄  ██▄▄▄█▀  ██   ██    ██     ██▀  ██  ██   ██  ██▀  ██           
         ██  ██  ██       ██   ██    ██     ██   ██  ██   ██  ██   ██           
         ██▄ ██  ██        ▀█▄█▀█    ██     ██   ██  ██   ██  ██   ██           
         ██ ▀ ▀  ▀▀            ██     ▀▀▀   ▀▀   ▀▀   ▀▀▀▀▀   ▀▀   ▀▀           
         ▀▀                ▀▀▀▀▀                                                
```
## Note:
* If you look above you will see that the *unifont* has ten matching glyphs, but the *efont* only has nine!
* This is because there is a informational glyph for the `\n` newline character in the unifont, but not in efont.

-------------------------------------------

# Addendum: Unicode Block List
Unicode is divided into standard 'blocks' of related glyphs, this is an overview for reference.

(from: https://www.unicode.org/Public/UCD/latest/ucd/Blocks.txt):
```
# Blocks-15.1.0.txt
# Date: 2023-07-28, 15:47:20 GMT
# © 2023 Unicode®, Inc.
# For terms of use, see https://www.unicode.org/terms_of_use.html
#
# Unicode Character Database
# For documentation, see https://www.unicode.org/reports/tr44/
#
# Format:
# Start Code..End Code; Block Name

# ================================================

# Note:   When comparing block names, casing, whitespace, hyphens,
#         and underbars are ignored.
#         For example, "Latin Extended-A" and "latin extended a" are equivalent.
#         For more information on the comparison of property values,
#            see UAX #44: https://www.unicode.org/reports/tr44/
#
#  All block ranges start with a value where (cp MOD 16) = 0,
#  and end with a value where (cp MOD 16) = 15. In other words,
#  the last hexadecimal digit of the start of range is ...0
#  and the last hexadecimal digit of the end of range is ...F.
#  This constraint on block ranges guarantees that allocations
#  are done in terms of whole columns, and that code chart display
#  never involves splitting columns in the charts.
#
#  All code points not explicitly listed for Block
#  have the value No_Block.

# Property:	Block
#
# @missing: 0000..10FFFF; No_Block

0000..007F; Basic Latin
0080..00FF; Latin-1 Supplement
0100..017F; Latin Extended-A
0180..024F; Latin Extended-B
0250..02AF; IPA Extensions
02B0..02FF; Spacing Modifier Letters
0300..036F; Combining Diacritical Marks
0370..03FF; Greek and Coptic
0400..04FF; Cyrillic
0500..052F; Cyrillic Supplement
0530..058F; Armenian
0590..05FF; Hebrew
0600..06FF; Arabic
0700..074F; Syriac
0750..077F; Arabic Supplement
0780..07BF; Thaana
07C0..07FF; NKo
0800..083F; Samaritan
0840..085F; Mandaic
0860..086F; Syriac Supplement
0870..089F; Arabic Extended-B
08A0..08FF; Arabic Extended-A
0900..097F; Devanagari
0980..09FF; Bengali
0A00..0A7F; Gurmukhi
0A80..0AFF; Gujarati
0B00..0B7F; Oriya
0B80..0BFF; Tamil
0C00..0C7F; Telugu
0C80..0CFF; Kannada
0D00..0D7F; Malayalam
0D80..0DFF; Sinhala
0E00..0E7F; Thai
0E80..0EFF; Lao
0F00..0FFF; Tibetan
1000..109F; Myanmar
10A0..10FF; Georgian
1100..11FF; Hangul Jamo
1200..137F; Ethiopic
1380..139F; Ethiopic Supplement
13A0..13FF; Cherokee
1400..167F; Unified Canadian Aboriginal Syllabics
1680..169F; Ogham
16A0..16FF; Runic
1700..171F; Tagalog
1720..173F; Hanunoo
1740..175F; Buhid
1760..177F; Tagbanwa
1780..17FF; Khmer
1800..18AF; Mongolian
18B0..18FF; Unified Canadian Aboriginal Syllabics Extended
1900..194F; Limbu
1950..197F; Tai Le
1980..19DF; New Tai Lue
19E0..19FF; Khmer Symbols
1A00..1A1F; Buginese
1A20..1AAF; Tai Tham
1AB0..1AFF; Combining Diacritical Marks Extended
1B00..1B7F; Balinese
1B80..1BBF; Sundanese
1BC0..1BFF; Batak
1C00..1C4F; Lepcha
1C50..1C7F; Ol Chiki
1C80..1C8F; Cyrillic Extended-C
1C90..1CBF; Georgian Extended
1CC0..1CCF; Sundanese Supplement
1CD0..1CFF; Vedic Extensions
1D00..1D7F; Phonetic Extensions
1D80..1DBF; Phonetic Extensions Supplement
1DC0..1DFF; Combining Diacritical Marks Supplement
1E00..1EFF; Latin Extended Additional
1F00..1FFF; Greek Extended
2000..206F; General Punctuation
2070..209F; Superscripts and Subscripts
20A0..20CF; Currency Symbols
20D0..20FF; Combining Diacritical Marks for Symbols
2100..214F; Letterlike Symbols
2150..218F; Number Forms
2190..21FF; Arrows
2200..22FF; Mathematical Operators
2300..23FF; Miscellaneous Technical
2400..243F; Control Pictures
2440..245F; Optical Character Recognition
2460..24FF; Enclosed Alphanumerics
2500..257F; Box Drawing
2580..259F; Block Elements
25A0..25FF; Geometric Shapes
2600..26FF; Miscellaneous Symbols
2700..27BF; Dingbats
27C0..27EF; Miscellaneous Mathematical Symbols-A
27F0..27FF; Supplemental Arrows-A
2800..28FF; Braille Patterns
2900..297F; Supplemental Arrows-B
2980..29FF; Miscellaneous Mathematical Symbols-B
2A00..2AFF; Supplemental Mathematical Operators
2B00..2BFF; Miscellaneous Symbols and Arrows
2C00..2C5F; Glagolitic
2C60..2C7F; Latin Extended-C
2C80..2CFF; Coptic
2D00..2D2F; Georgian Supplement
2D30..2D7F; Tifinagh
2D80..2DDF; Ethiopic Extended
2DE0..2DFF; Cyrillic Extended-A
2E00..2E7F; Supplemental Punctuation
2E80..2EFF; CJK Radicals Supplement
2F00..2FDF; Kangxi Radicals
2FF0..2FFF; Ideographic Description Characters
3000..303F; CJK Symbols and Punctuation
3040..309F; Hiragana
30A0..30FF; Katakana
3100..312F; Bopomofo
3130..318F; Hangul Compatibility Jamo
3190..319F; Kanbun
31A0..31BF; Bopomofo Extended
31C0..31EF; CJK Strokes
31F0..31FF; Katakana Phonetic Extensions
3200..32FF; Enclosed CJK Letters and Months
3300..33FF; CJK Compatibility
3400..4DBF; CJK Unified Ideographs Extension A
4DC0..4DFF; Yijing Hexagram Symbols
4E00..9FFF; CJK Unified Ideographs
A000..A48F; Yi Syllables
A490..A4CF; Yi Radicals
A4D0..A4FF; Lisu
A500..A63F; Vai
A640..A69F; Cyrillic Extended-B
A6A0..A6FF; Bamum
A700..A71F; Modifier Tone Letters
A720..A7FF; Latin Extended-D
A800..A82F; Syloti Nagri
A830..A83F; Common Indic Number Forms
A840..A87F; Phags-pa
A880..A8DF; Saurashtra
A8E0..A8FF; Devanagari Extended
A900..A92F; Kayah Li
A930..A95F; Rejang
A960..A97F; Hangul Jamo Extended-A
A980..A9DF; Javanese
A9E0..A9FF; Myanmar Extended-B
AA00..AA5F; Cham
AA60..AA7F; Myanmar Extended-A
AA80..AADF; Tai Viet
AAE0..AAFF; Meetei Mayek Extensions
AB00..AB2F; Ethiopic Extended-A
AB30..AB6F; Latin Extended-E
AB70..ABBF; Cherokee Supplement
ABC0..ABFF; Meetei Mayek
AC00..D7AF; Hangul Syllables
D7B0..D7FF; Hangul Jamo Extended-B
D800..DB7F; High Surrogates
DB80..DBFF; High Private Use Surrogates
DC00..DFFF; Low Surrogates
E000..F8FF; Private Use Area
F900..FAFF; CJK Compatibility Ideographs
FB00..FB4F; Alphabetic Presentation Forms
FB50..FDFF; Arabic Presentation Forms-A
FE00..FE0F; Variation Selectors
FE10..FE1F; Vertical Forms
FE20..FE2F; Combining Half Marks
FE30..FE4F; CJK Compatibility Forms
FE50..FE6F; Small Form Variants
FE70..FEFF; Arabic Presentation Forms-B
FF00..FFEF; Halfwidth and Fullwidth Forms
FFF0..FFFF; Specials
10000..1007F; Linear B Syllabary
10080..100FF; Linear B Ideograms
10100..1013F; Aegean Numbers
10140..1018F; Ancient Greek Numbers
10190..101CF; Ancient Symbols
101D0..101FF; Phaistos Disc
10280..1029F; Lycian
102A0..102DF; Carian
102E0..102FF; Coptic Epact Numbers
10300..1032F; Old Italic
10330..1034F; Gothic
10350..1037F; Old Permic
10380..1039F; Ugaritic
103A0..103DF; Old Persian
10400..1044F; Deseret
10450..1047F; Shavian
10480..104AF; Osmanya
104B0..104FF; Osage
10500..1052F; Elbasan
10530..1056F; Caucasian Albanian
10570..105BF; Vithkuqi
10600..1077F; Linear A
10780..107BF; Latin Extended-F
10800..1083F; Cypriot Syllabary
10840..1085F; Imperial Aramaic
10860..1087F; Palmyrene
10880..108AF; Nabataean
108E0..108FF; Hatran
10900..1091F; Phoenician
10920..1093F; Lydian
10980..1099F; Meroitic Hieroglyphs
109A0..109FF; Meroitic Cursive
10A00..10A5F; Kharoshthi
10A60..10A7F; Old South Arabian
10A80..10A9F; Old North Arabian
10AC0..10AFF; Manichaean
10B00..10B3F; Avestan
10B40..10B5F; Inscriptional Parthian
10B60..10B7F; Inscriptional Pahlavi
10B80..10BAF; Psalter Pahlavi
10C00..10C4F; Old Turkic
10C80..10CFF; Old Hungarian
10D00..10D3F; Hanifi Rohingya
10E60..10E7F; Rumi Numeral Symbols
10E80..10EBF; Yezidi
10EC0..10EFF; Arabic Extended-C
10F00..10F2F; Old Sogdian
10F30..10F6F; Sogdian
10F70..10FAF; Old Uyghur
10FB0..10FDF; Chorasmian
10FE0..10FFF; Elymaic
11000..1107F; Brahmi
11080..110CF; Kaithi
110D0..110FF; Sora Sompeng
11100..1114F; Chakma
11150..1117F; Mahajani
11180..111DF; Sharada
111E0..111FF; Sinhala Archaic Numbers
11200..1124F; Khojki
11280..112AF; Multani
112B0..112FF; Khudawadi
11300..1137F; Grantha
11400..1147F; Newa
11480..114DF; Tirhuta
11580..115FF; Siddham
11600..1165F; Modi
11660..1167F; Mongolian Supplement
11680..116CF; Takri
11700..1174F; Ahom
11800..1184F; Dogra
118A0..118FF; Warang Citi
11900..1195F; Dives Akuru
119A0..119FF; Nandinagari
11A00..11A4F; Zanabazar Square
11A50..11AAF; Soyombo
11AB0..11ABF; Unified Canadian Aboriginal Syllabics Extended-A
11AC0..11AFF; Pau Cin Hau
11B00..11B5F; Devanagari Extended-A
11C00..11C6F; Bhaiksuki
11C70..11CBF; Marchen
11D00..11D5F; Masaram Gondi
11D60..11DAF; Gunjala Gondi
11EE0..11EFF; Makasar
11F00..11F5F; Kawi
11FB0..11FBF; Lisu Supplement
11FC0..11FFF; Tamil Supplement
12000..123FF; Cuneiform
12400..1247F; Cuneiform Numbers and Punctuation
12480..1254F; Early Dynastic Cuneiform
12F90..12FFF; Cypro-Minoan
13000..1342F; Egyptian Hieroglyphs
13430..1345F; Egyptian Hieroglyph Format Controls
14400..1467F; Anatolian Hieroglyphs
16800..16A3F; Bamum Supplement
16A40..16A6F; Mro
16A70..16ACF; Tangsa
16AD0..16AFF; Bassa Vah
16B00..16B8F; Pahawh Hmong
16E40..16E9F; Medefaidrin
16F00..16F9F; Miao
16FE0..16FFF; Ideographic Symbols and Punctuation
17000..187FF; Tangut
18800..18AFF; Tangut Components
18B00..18CFF; Khitan Small Script
18D00..18D7F; Tangut Supplement
1AFF0..1AFFF; Kana Extended-B
1B000..1B0FF; Kana Supplement
1B100..1B12F; Kana Extended-A
1B130..1B16F; Small Kana Extension
1B170..1B2FF; Nushu
1BC00..1BC9F; Duployan
1BCA0..1BCAF; Shorthand Format Controls
1CF00..1CFCF; Znamenny Musical Notation
1D000..1D0FF; Byzantine Musical Symbols
1D100..1D1FF; Musical Symbols
1D200..1D24F; Ancient Greek Musical Notation
1D2C0..1D2DF; Kaktovik Numerals
1D2E0..1D2FF; Mayan Numerals
1D300..1D35F; Tai Xuan Jing Symbols
1D360..1D37F; Counting Rod Numerals
1D400..1D7FF; Mathematical Alphanumeric Symbols
1D800..1DAAF; Sutton SignWriting
1DF00..1DFFF; Latin Extended-G
1E000..1E02F; Glagolitic Supplement
1E030..1E08F; Cyrillic Extended-D
1E100..1E14F; Nyiakeng Puachue Hmong
1E290..1E2BF; Toto
1E2C0..1E2FF; Wancho
1E4D0..1E4FF; Nag Mundari
1E7E0..1E7FF; Ethiopic Extended-B
1E800..1E8DF; Mende Kikakui
1E900..1E95F; Adlam
1EC70..1ECBF; Indic Siyaq Numbers
1ED00..1ED4F; Ottoman Siyaq Numbers
1EE00..1EEFF; Arabic Mathematical Alphabetic Symbols
1F000..1F02F; Mahjong Tiles
1F030..1F09F; Domino Tiles
1F0A0..1F0FF; Playing Cards
1F100..1F1FF; Enclosed Alphanumeric Supplement
1F200..1F2FF; Enclosed Ideographic Supplement
1F300..1F5FF; Miscellaneous Symbols and Pictographs
1F600..1F64F; Emoticons
1F650..1F67F; Ornamental Dingbats
1F680..1F6FF; Transport and Map Symbols
1F700..1F77F; Alchemical Symbols
1F780..1F7FF; Geometric Shapes Extended
1F800..1F8FF; Supplemental Arrows-C
1F900..1F9FF; Supplemental Symbols and Pictographs
1FA00..1FA6F; Chess Symbols
1FA70..1FAFF; Symbols and Pictographs Extended-A
1FB00..1FBFF; Symbols for Legacy Computing
20000..2A6DF; CJK Unified Ideographs Extension B
2A700..2B73F; CJK Unified Ideographs Extension C
2B740..2B81F; CJK Unified Ideographs Extension D
2B820..2CEAF; CJK Unified Ideographs Extension E
2CEB0..2EBEF; CJK Unified Ideographs Extension F
2EBF0..2EE5F; CJK Unified Ideographs Extension I
2F800..2FA1F; CJK Compatibility Ideographs Supplement
30000..3134F; CJK Unified Ideographs Extension G
31350..323AF; CJK Unified Ideographs Extension H
E0000..E007F; Tags
E0100..E01EF; Variation Selectors Supplement
F0000..FFFFF; Supplementary Private Use Area-A
100000..10FFFF; Supplementary Private Use Area-B

# EOF
```
