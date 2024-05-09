# Font files

This folder contains font files suitable for use with `ezFBfont` and Peter Hinches `writer` class.

They are organised by vertical size; and (where possible) come in 3 different character sets:
* The 'height' of each font set is the *true height*; the height of the tallest character in that set.
* This can vary from the height declared in the font name!
* The same font may appear listed as different heights depending which character set is being provided.
  * eg: numeric charsets are typically shorter than the full charsets.

There is a mixture of proportional width and monospaced fonts in the collection; the font name will typically note the size for monospaced fonts. The proportional (X11) fonts also mostly come in regular and bold weights.

The character sets are:
```
r =  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
n =  %*+,-./0123456789:°
e = Every character that font-to-mpy can convert
```
These can loosely be described as **R**eadable (ascii charset), **N**umeric (plus a few related symbols) and **E**verything.

Pay attention to the file sizes;
* With the `e` (everything) set characters will only be present when they are defined in the font source!
* Other charsets encode a 'blank' character in place of missing characters, this *can* make them bigger than the `e` set!

For more detailed font descriptions and previews look for the corresponding font entry in the U8G2 wiki:
https://github.com/olikraus/u8g2/wiki/fntlistall

For usage see the `ezFBfont.py` documentation in the main `README`.

----------------------

Fonts as of May 8, 2024, organised by height.
```
  5px:
    tom_thumb.............. Tom Thumb font (numeric)
    u8glib_4............... U8G2 native font (numeric)
  6px:
    4x6.................... U8G2 default font (everything, numeric, readable)
    font_tiny5............. Tiny font (numeric)
    tom_thumb.............. Tom Thumb font (everything, readable)
    u8glib_4............... U8G2 native font (everything, readable)
  7px:
    5x7.................... U8G2 default font (everything, numeric, readable)
    font_tiny5............. Tiny font (everything, readable)
    u8g2_squeezed_bold_6... U8G2 native font (everything, numeric, readable)
    u8g2_squeezed_regular_6 U8G2 native font (everything, numeric, readable)
  8px:
    5x8.................... U8G2 default font (everything, numeric, readable)
    spleen_5x8............. Spleen small display font (everything, numeric, readable)
    timB08................. Times bold (numeric)
    timR08................. Times regular (numeric)
    u8g2_squeezed_bold_7... U8G2 native font (everything, numeric, readable)
    u8g2_squeezed_regular_7 U8G2 native font (everything, numeric, readable)
  9px:
    6x9.................... U8G2 default font (everything, numeric, readable)
    courB08................ Courier bold (numeric)
 10px:
    6x10................... U8G2 default font (everything, numeric, readable)
    courB08................ Courier bold (everything, readable)
    courR08................ Courier regular (everything, numeric, readable)
    helvB08................ Helvetica bold (numeric)
    helvB08_gps............ Helvetica bold (numeric)
    helvR08................ Helvetica regular (numeric)
    ncenB08................ New Century Schoolbook bold (numeric)
    ncenR08................ New Century Schoolbook regular (numeric)
 11px:
    helvB08................ Helvetica bold (everything, readable)
    helvB08_gps............ Helvetica bold (everything, readable)
    helvR08................ Helvetica regular (everything, readable)
    ncenB08................ New Century Schoolbook bold (everything, readable)
    ncenR08................ New Century Schoolbook regular (everything, readable)
    timB08................. Times bold (everything, readable)
    timR08................. Times regular (everything, readable)
 12px:
    6x12................... U8G2 default font (everything, numeric, readable)
    courB10................ Courier bold (numeric)
    courR10................ Courier regular (numeric)
    freedoomr10r........... Doom! (everything, numeric, readable)
    helvB10................ Helvetica bold (numeric)
    spleen_6x12............ Spleen small display font (everything, numeric, readable)
    timB10................. Times bold (numeric)
    timR10................. Times regular (numeric)
 13px:
    6x13................... U8G2 default font (everything, numeric, readable)
    7x13................... U8G2 default font (everything, numeric, readable)
    8x13................... U8G2 default font (everything, numeric, readable)
    courR12................ Courier regular (numeric)
    helvR10................ Helvetica regular (numeric)
    ncenB10................ New Century Schoolbook bold (numeric)
    ncenR10................ New Century Schoolbook regular (numeric)
    timR12................. Times regular (numeric)
 14px:
    7x14................... U8G2 default font (everything, numeric, readable)
    courB10................ Courier bold (everything, readable)
    courR10................ Courier regular (everything, readable)
    helvR12................ Helvetica regular (numeric)
    timB10................. Times bold (everything, readable)
    timB12................. Times bold (numeric)
    timR10................. Times regular (everything, readable)
 15px:
    9x15................... U8G2 default font (everything, numeric, readable)
    courB12................ Courier bold (everything, numeric, readable)
    courR12................ Courier regular (everything, readable)
    helvB10................ Helvetica bold (everything, readable)
    helvB12................ Helvetica bold (numeric)
    helvR10................ Helvetica regular (everything, readable)
    ncenB10................ New Century Schoolbook bold (everything, readable)
    ncenB12................ New Century Schoolbook bold (numeric)
    ncenR10................ New Century Schoolbook regular (everything, readable)
    ncenR12................ New Century Schoolbook regular (numeric)
    symb08................. Symbols (everything)
    symb10................. Symbols (everything)
 16px:
    courB14................ Courier bold (numeric)
    courR14................ Courier regular (numeric)
    ncenR12................ New Century Schoolbook regular (everything, readable)
    spleen_8x16............ Spleen small display font (everything, numeric, readable)
    timB12................. Times bold (everything, readable)
    timB14................. Times bold (numeric)
    timR12................. Times regular (everything, readable)
    unifont................ GNU unicode font (everything, numeric, readable)
 17px:
    courB14................ Courier bold (everything, readable)
    courR14................ Courier regular (everything, readable)
    helvB12................ Helvetica bold (everything, readable)
    helvB14................ Helvetica bold (numeric)
    helvR12................ Helvetica regular (everything, readable)
    helvR14................ Helvetica regular (numeric)
    ncenB12................ New Century Schoolbook bold (everything, readable)
    ncenB14................ New Century Schoolbook bold (numeric)
    ncenR14................ New Century Schoolbook regular (numeric)
    symb12................. Symbols (everything)
    timR14................. Times regular (numeric)
 18px:
    9x18................... U8G2 default font (everything, numeric, readable)
    helvB14................ Helvetica bold (everything, readable)
    helvR14................ Helvetica regular (everything, readable)
    timB14................. Times bold (everything, readable)
    timR14................. Times regular (everything, readable)
 19px:
    battery19.............. Battery level indicator (everything, numeric, readable)
    courR18................ Courier regular (numeric)
    ncenR14................ New Century Schoolbook regular (everything, readable)
    symb14................. Symbols (everything)
 20px:
    10x20.................. U8G2 default font (everything, numeric, readable)
    courB18................ Courier bold (numeric)
    ncenB14................ New Century Schoolbook bold (everything, readable)
 21px:
    emoticons21............ Emoticon font (everything, numeric, readable)
    timR18................. Times regular (numeric)
 22px:
    courB18................ Courier bold (everything, readable)
    courR18................ Courier regular (everything, readable)
    helvB18................ Helvetica bold (numeric)
    helvR18................ Helvetica regular (numeric)
    ncenB18................ New Century Schoolbook bold (numeric)
    ncenR18................ New Century Schoolbook regular (numeric)
    timB18................. Times bold (numeric)
 23px:
    timB18................. Times bold (everything, readable)
 24px:
    battery24.............. Battery level indicator (everything, numeric, readable)
    cursor................. Cursors (numeric)
    helvB18................ Helvetica bold (everything, readable)
    spleen_12x24........... Spleen small display font (everything, numeric, readable)
    symb18................. Symbols (everything)
 25px:
    helvR18................ Helvetica regular (everything, readable)
    ncenB18................ New Century Schoolbook bold (everything, readable)
    ncenR18................ New Century Schoolbook regular (everything, readable)
    timR18................. Times regular (everything, readable)
 26px:
    courR24................ Courier regular (numeric)
    freedoomr25n........... Doom! (everything, numeric, readable)
    timR24................. Times regular (numeric)
 28px:
    courB24................ Courier bold (numeric)
    courR24................ Courier regular (everything, readable)
 30px:
    courB24................ Courier bold (everything, readable)
    ncenB24................ New Century Schoolbook bold (numeric)
 31px:
    7_Seg_33x19............ 7 segment display font (everything, numeric, readable)
    cursor................. Cursors (everything, readable)
    helvB24................ Helvetica bold (numeric)
    helvR24................ Helvetica regular (numeric)
    ncenR24................ New Century Schoolbook regular (numeric)
    timB24................. Times bold (numeric)
 32px:
    helvB24................ Helvetica bold (everything, readable)
    spleen_16x32........... Spleen small display font (everything, numeric, readable)
    timR24................. Times regular (everything, readable)
 33px:
    ncenB24................ New Century Schoolbook bold (everything, readable)
    timB24................. Times bold (everything, readable)
 34px:
    helvR24................ Helvetica regular (everything, readable)
    ncenR24................ New Century Schoolbook regular (everything, readable)
    symb24................. Symbols (everything)
 39px:
    7_Seg_41x21............ 7 segment display font (everything, numeric, readable)
 42px:
    7Segments_26x42........ 7 segment display font (everything, numeric, readable)
 64px:
    spleen_32x64........... Spleen small display font (everything, numeric, readable)
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
