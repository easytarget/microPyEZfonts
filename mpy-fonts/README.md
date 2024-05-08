# Font files

This folder contains font files suitable for use with `ezFBfont` and Peter Hinches `writer` class.

They are organised by vertical size; and (where possible) come in up to 5 different character sets:
* The 'height' of each font set is the *true height*; the height of the tallest character in that set.
* This can vary from the height declared in the font name!
* The same font may appear listed as different heights depending which character set is being provided.
  * eg: numeric charsets are typically shorter than the full charsets.
 
The character sets are:
```
r =  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
n =  *+,-./0123456789:
e = Every character that font-to-mpy can convert
```
These can loosely be described as **R**eadable (ascii charset), **N**umeric (plus a few time related symbols) and **E**verything.

Pay attention to the file sizes; 
* With the `e` (everything) set characters will only be present when they are defined in the font source!
* Other charsets encode a 'blank' character in place of missing characters, this can make them bigger than the `e` set!

For more detailed font descriptions and previews look for the corresponding font entry in the U8G2 wiki:
https://github.com/olikraus/u8g2/wiki/fntlistall

For usage see the `ezFBfont.py` documentation in the main `README`.

----------------------

Fonts as of May 8, 2024, organised by height.
```
  5px:
    tom_thumb.............. Tom Thumb fonts (numeric, uppercase)
    u8glib_4............... U8G2 native font (numeric)
  6px:
    4x6.................... U8G2 default font (everything, full, numeric, readable, uppercase)
    font_tiny5............. Tiny fonts (numeric, uppercase)
    tom_thumb.............. Tom Thumb fonts (everything, full, readable)
    u8glib_4............... U8G2 native font (everything, readable, uppercase)
  7px:
    5x7.................... U8G2 default font (everything, full, numeric, readable, uppercase)
    font_tiny5............. Tiny fonts (everything, full, readable)
    u8g2_squeezed_bold_6... U8G2 native font (everything, full, numeric, readable, uppercase)
    u8g2_squeezed_regular_6 U8G2 native font (everything, full, numeric, readable, uppercase)
    u8glib_4............... U8G2 native font (full)
  8px:
    5x8.................... U8G2 default font (everything, full, numeric, readable, uppercase)
    spleen_5x8............. Spleen small display fonts (everything, full, numeric, readable, uppercase)
    timB08................. Times bold (numeric)
    timR08................. Times regular (numeric)
    u8g2_squeezed_bold_7... U8G2 native font (everything, full, numeric, readable, uppercase)
    u8g2_squeezed_regular_7 U8G2 native font (everything, full, numeric, readable, uppercase)
  9px:
    6x9.................... U8G2 default font (everything, full, numeric, readable, uppercase)
    courB08................ Courier bold (numeric)
 10px:
    6x10................... U8G2 default font (everything, full, numeric, readable, uppercase)
    courB08................ Courier bold (everything, readable, uppercase)
    courR08................ Courier regular (everything, numeric, readable, uppercase)
    helvB08................ Helvetica bold (numeric)
    helvB08_gps............ Helvetica bold (numeric)
    helvR08................ Helvetica regular (numeric)
    ncenB08................ New Century Schoolbook bold (numeric)
    ncenR08................ New Century Schoolbook regular (numeric)
 11px:
    courB08................ Courier bold (full)
    courR08................ Courier regular (full)
    helvB08................ Helvetica bold (everything, readable, uppercase)
    helvB08_gps............ Helvetica bold (everything, full, readable, uppercase)
    helvR08................ Helvetica regular (everything, readable, uppercase)
    ncenB08................ New Century Schoolbook bold (everything, readable, uppercase)
    ncenR08................ New Century Schoolbook regular (everything, readable, uppercase)
    timB08................. Times bold (everything, readable, uppercase)
    timR08................. Times regular (everything, readable, uppercase)
 12px:
    6x12................... U8G2 default font (everything, full, numeric, readable, uppercase)
    courB10................ Courier bold (numeric)
    courR10................ Courier regular (numeric)
    freedoomr10r........... Doom! (everything, full, numeric, readable, uppercase)
    helvB10................ Helvetica bold (numeric)
    spleen_6x12............ Spleen small display fonts (everything, full, numeric, readable, uppercase)
    timB10................. Times bold (numeric)
    timR10................. Times regular (numeric)
 13px:
    6x13................... U8G2 default font (everything, full, numeric, readable, uppercase)
    7x13................... U8G2 default font (everything, full, numeric, readable, uppercase)
    8x13................... U8G2 default font (everything, full, numeric, readable, uppercase)
    courB10................ Courier bold (uppercase)
    courR12................ Courier regular (numeric)
    helvB08................ Helvetica bold (full)
    helvR08................ Helvetica regular (full)
    helvR10................ Helvetica regular (numeric)
    ncenB08................ New Century Schoolbook bold (full)
    ncenB10................ New Century Schoolbook bold (numeric)
    ncenR08................ New Century Schoolbook regular (full)
    ncenR10................ New Century Schoolbook regular (numeric)
    timB08................. Times bold (full)
    timR08................. Times regular (full)
    timR12................. Times regular (numeric)
 14px:
    7x14................... U8G2 default font (everything, full, numeric, readable, uppercase)
    courB10................ Courier bold (everything, readable)
    courR10................ Courier regular (everything, readable, uppercase)
    helvR12................ Helvetica regular (numeric)
    ncenR10................ New Century Schoolbook regular (uppercase)
    timB10................. Times bold (everything, readable, uppercase)
    timB12................. Times bold (numeric)
    timR10................. Times regular (everything, readable, uppercase)
 15px:
    9x15................... U8G2 default font (everything, full, numeric, readable, uppercase)
    courB12................ Courier bold (everything, numeric, readable, uppercase)
    courR10................ Courier regular (full)
    courR12................ Courier regular (everything, readable, uppercase)
    helvB10................ Helvetica bold (everything, readable, uppercase)
    helvB12................ Helvetica bold (numeric)
    helvR10................ Helvetica regular (everything, readable, uppercase)
    ncenB10................ New Century Schoolbook bold (everything, readable, uppercase)
    ncenB12................ New Century Schoolbook bold (numeric)
    ncenR10................ New Century Schoolbook regular (everything, readable)
    ncenR12................ New Century Schoolbook regular (numeric)
    symb08................. Symbols (everything)
    symb10................. Symbols (everything)
    timR12................. Times regular (uppercase)
 16px:
    courB10................ Courier bold (full)
    courB14................ Courier bold (numeric)
    courR14................ Courier regular (numeric)
    helvB12................ Helvetica bold (uppercase)
    ncenR12................ New Century Schoolbook regular (everything, readable, uppercase)
    spleen_8x16............ Spleen small display fonts (everything, full, numeric, readable, uppercase)
    timB12................. Times bold (everything, readable, uppercase)
    timB14................. Times bold (numeric)
    timR12................. Times regular (everything, readable)
    unifont................ GNU unicode font (everything, full, numeric, readable, uppercase)
 17px:
    courB12................ Courier bold (full)
    courB14................ Courier bold (everything, readable, uppercase)
    courR12................ Courier regular (full)
    courR14................ Courier regular (everything, readable, uppercase)
    helvB10................ Helvetica bold (full)
    helvB12................ Helvetica bold (everything, readable)
    helvB14................ Helvetica bold (numeric)
    helvR10................ Helvetica regular (full)
    helvR12................ Helvetica regular (everything, readable, uppercase)
    helvR14................ Helvetica regular (numeric)
    ncenB12................ New Century Schoolbook bold (everything, readable, uppercase)
    ncenB14................ New Century Schoolbook bold (numeric)
    ncenR10................ New Century Schoolbook regular (full)
    ncenR14................ New Century Schoolbook regular (numeric)
    symb12................. Symbols (everything)
    timB10................. Times bold (full)
    timR10................. Times regular (full)
    timR14................. Times regular (numeric)
 18px:
    9x18................... U8G2 default font (everything, full, numeric, readable, uppercase)
    helvB14................ Helvetica bold (everything, readable, uppercase)
    helvR14................ Helvetica regular (everything, readable, uppercase)
    ncenB10................ New Century Schoolbook bold (full)
    timB14................. Times bold (everything, readable, uppercase)
    timR14................. Times regular (everything, readable, uppercase)
 19px:
    battery19.............. Battery level indicator (everything, full, numeric, readable, uppercase)
    courR14................ Courier regular (full)
    courR18................ Courier regular (numeric)
    ncenB12................ New Century Schoolbook bold (full)
    ncenR12................ New Century Schoolbook regular (full)
    ncenR14................ New Century Schoolbook regular (everything, readable, uppercase)
    symb14................. Symbols (everything)
    timR12................. Times regular (full)
 20px:
    10x20.................. U8G2 default font (everything, full, numeric, readable, uppercase)
    courB14................ Courier bold (full)
    courB18................ Courier bold (numeric)
    helvB12................ Helvetica bold (full)
    helvR12................ Helvetica regular (full)
    ncenB14................ New Century Schoolbook bold (everything, readable, uppercase)
    timB12................. Times bold (full)
 21px:
    courB18................ Courier bold (uppercase)
    emoticons21............ Emoticon font (everything, full, numeric, readable, uppercase)
    timB14................. Times bold (full)
    timR18................. Times regular (numeric)
 22px:
    courB18................ Courier bold (everything, readable)
    courR18................ Courier regular (everything, readable, uppercase)
    helvB18................ Helvetica bold (numeric)
    helvR14................ Helvetica regular (full)
    helvR18................ Helvetica regular (numeric)
    ncenB18................ New Century Schoolbook bold (numeric)
    ncenR18................ New Century Schoolbook regular (numeric)
    timB18................. Times bold (numeric)
    timR14................. Times regular (full)
 23px:
    helvB14................ Helvetica bold (full)
    ncenB14................ New Century Schoolbook bold (full)
    ncenR14................ New Century Schoolbook regular (full)
    timB18................. Times bold (everything, readable, uppercase)
 24px:
    battery24.............. Battery level indicator (everything, full, numeric, readable, uppercase)
    courR18................ Courier regular (full)
    cursor................. Cursors (numeric)
    helvB18................ Helvetica bold (everything, readable, uppercase)
    ncenR18................ New Century Schoolbook regular (uppercase)
    spleen_12x24........... Spleen small display fonts (everything, full, numeric, readable, uppercase)
    symb18................. Symbols (everything)
    timR18................. Times regular (uppercase)
 25px:
    helvR18................ Helvetica regular (everything, readable, uppercase)
    ncenB18................ New Century Schoolbook bold (everything, readable, uppercase)
    ncenR18................ New Century Schoolbook regular (everything, readable)
    timR18................. Times regular (everything, readable)
 26px:
    courB18................ Courier bold (full)
    courR24................ Courier regular (numeric)
    freedoomr25n........... Doom! (everything, full, numeric, readable, uppercase)
    timR24................. Times regular (numeric)
 28px:
    courB24................ Courier bold (numeric)
    courR24................ Courier regular (everything, readable, uppercase)
 29px:
    helvB18................ Helvetica bold (full)
    helvR18................ Helvetica regular (full)
    ncenB18................ New Century Schoolbook bold (full)
    ncenR18................ New Century Schoolbook regular (full)
    timB18................. Times bold (full)
    timR18................. Times regular (full)
 30px:
    courB24................ Courier bold (everything, readable, uppercase)
    ncenB24................ New Century Schoolbook bold (numeric)
 31px:
    7_Seg_33x19............ 7 segment display font (everything, full, numeric, readable, uppercase)
    cursor................. Cursors (everything, full, readable, uppercase)
    helvB24................ Helvetica bold (numeric, uppercase)
    helvR24................ Helvetica regular (numeric)
    ncenR24................ New Century Schoolbook regular (numeric)
    timB24................. Times bold (numeric)
    timR24................. Times regular (uppercase)
 32px:
    courR24................ Courier regular (full)
    helvB24................ Helvetica bold (everything, readable)
    ncenB24................ New Century Schoolbook bold (uppercase)
    spleen_16x32........... Spleen small display fonts (everything, full, numeric, readable, uppercase)
    timB24................. Times bold (uppercase)
    timR24................. Times regular (everything, readable)
 33px:
    courB24................ Courier bold (full)
    ncenB24................ New Century Schoolbook bold (everything, readable)
    ncenR24................ New Century Schoolbook regular (uppercase)
    timB24................. Times bold (everything, readable)
 34px:
    helvR24................ Helvetica regular (everything, readable, uppercase)
    ncenR24................ New Century Schoolbook regular (everything, readable)
    symb24................. Symbols (everything)
 37px:
    timB24................. Times bold (full)
    timR24................. Times regular (full)
 38px:
    helvB24................ Helvetica bold (full)
    helvR24................ Helvetica regular (full)
 39px:
    7_Seg_41x21............ 7 segment display font (everything, full, numeric, readable, uppercase)
    ncenR24................ New Century Schoolbook regular (full)
 40px:
    ncenB24................ New Century Schoolbook bold (full)
 42px:
    7Segments_26x42........ 7 segment display font (everything, full, numeric, readable, uppercase)
 64px:
    spleen_32x64........... Spleen small display fonts (everything, full, numeric, readable, uppercase)
```
---------------------

## Converter script
The font structure is created by the 'convert.py' script in this folder.

### requirements
* This repo
* Git Submodules updated
* `freetype-py` installed:
  * pip install --upgrade freetype-py

The `convert.py` script will create and populate the `mpy-fonts` folder with all matching and successful fonts; organised by height

## Indexer script
No requirements, when run in the font folder it will index the font packs and provide the above summary
