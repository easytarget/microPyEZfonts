# Font files

This folder contains font files suitable for use with `ezFBfont` and Peter Hinches `writer` class.

They are organised by vertical size; and (where possible) come in up to 5 different charset formats:
* Characters will only be present when they are defined in the font source!
  * Not all fonts have all characters.
  * Empty font files are ignored.

```
f = !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
r =  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
U =  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
n =  *+,-./0123456789:
e = Every character that font-to-mpy can convert, can be large
```
These can loosely be described as **f**ull (all chars up to 255), **r**eadable (ascii charset), **u**ppercase (just the minimum, good for symbol fonts), **n**umbers (plus a few time related symbols) and **e**verything.

For more detailed font descriptions and previews look for the corresponding font entry in the U8G2 wiki:
https://github.com/olikraus/u8g2/wiki/fntlistall

For usage see the `ezFBfont.py` documentation in the main `README`.

----------------------

Fonts as of May 7, 2024, organised by height.
```
  5:
    tom_thumb..............Tom Thumb fonts (numeric, uppercase)
    u8glib_4...............U8G2 native font (numeric)
  6:
    font_tiny5.............Tiny fonts (numeric, uppercase)
    4x6....................U8G2 default font (everything, full, numeric, readable, uppercase)
    u8glib_4...............U8G2 native font (everything, readable, uppercase)
    tom_thumb..............Tom Thumb fonts (everything, full, readable)
  7:
    u8glib_4...............U8G2 native font (full)
    5x7....................U8G2 default font (everything, full, numeric, readable, uppercase)
    u8g2_squeezed_bold_6...U8G2 native font (everything, full, numeric, readable, uppercase)
    font_tiny5.............Tiny fonts (everything, full, readable)
    u8g2_squeezed_regular_6U8G2 native font (everything, full, numeric, readable, uppercase)
  8:
    u8g2_squeezed_bold_7...U8G2 native font (everything, full, numeric, readable, uppercase)
    u8g2_squeezed_regular_7U8G2 native font (everything, full, numeric, readable, uppercase)
    5x8....................U8G2 default font (everything, full, numeric, readable, uppercase)
    spleen_5x8.............Spleen small display fonts (everything, full, numeric, readable, uppercase)
    timB08.................Times bold (numeric)
    timR08.................Times regular (numeric)
  9:
    6x9....................U8G2 default font (everything, full, numeric, readable, uppercase)
    courB08................Courier bold (numeric)
 10:
    6x10...................U8G2 default font (everything, full, numeric, readable, uppercase)
    courB08................Courier bold (everything, readable, uppercase)
    courR08................Courier regular (everything, numeric, readable, uppercase)
    helvR08................Helvetica regular (numeric)
    ncenB08................New Century Schoolbook bold (numeric)
    helvB08................Helvetica bold (numeric)
    ncenR08................New Century Schoolbook regular (numeric)
    helvB08_gps............Helvetica bold (numeric)
 11:
    ncenB08................New Century Schoolbook bold (everything, readable, uppercase)
    helvR08................Helvetica regular (everything, readable, uppercase)
    helvB08_gps............Helvetica bold (everything, full, readable, uppercase)
    ncenR08................New Century Schoolbook regular (everything, readable, uppercase)
    timB08.................Times bold (everything, readable, uppercase)
    courR08................Courier regular (full)
    helvB08................Helvetica bold (everything, readable, uppercase)
    timR08.................Times regular (everything, readable, uppercase)
    courB08................Courier bold (full)
 12:
    spleen_6x12............Spleen small display fonts (everything, full, numeric, readable, uppercase)
    freedoomr10r...........Doom! (everything, full, numeric, readable, uppercase)
    6x12...................U8G2 default font (everything, full, numeric, readable, uppercase)
    courR10................Courier regular (numeric)
    timB10.................Times bold (numeric)
    helvB10................Helvetica bold (numeric)
    courB10................Courier bold (numeric)
    timR10.................Times regular (numeric)
 13:
    courB10................Courier bold (uppercase)
    7x13...................U8G2 default font (everything, full, numeric, readable, uppercase)
    8x13...................U8G2 default font (everything, full, numeric, readable, uppercase)
    ncenR08................New Century Schoolbook regular (full)
    ncenR10................New Century Schoolbook regular (numeric)
    courR12................Courier regular (numeric)
    ncenB08................New Century Schoolbook bold (full)
    6x13...................U8G2 default font (everything, full, numeric, readable, uppercase)
    timR12.................Times regular (numeric)
    ncenB10................New Century Schoolbook bold (numeric)
    timR08.................Times regular (full)
    helvR08................Helvetica regular (full)
    helvR10................Helvetica regular (numeric)
    timB08.................Times bold (full)
    helvB08................Helvetica bold (full)
 14:
    timR10.................Times regular (everything, readable, uppercase)
    7x14...................U8G2 default font (everything, full, numeric, readable, uppercase)
    courR10................Courier regular (everything, readable, uppercase)
    courB10................Courier bold (everything, readable)
    ncenR10................New Century Schoolbook regular (uppercase)
    timB10.................Times bold (everything, readable, uppercase)
    helvR12................Helvetica regular (numeric)
    timB12.................Times bold (numeric)
 15:
    courR12................Courier regular (everything, readable, uppercase)
    ncenB10................New Century Schoolbook bold (everything, readable, uppercase)
    helvR10................Helvetica regular (everything, readable, uppercase)
    9x15...................U8G2 default font (everything, full, numeric, readable, uppercase)
    helvB12................Helvetica bold (numeric)
    ncenR12................New Century Schoolbook regular (numeric)
    symb10.................Symbols (everything)
    ncenR10................New Century Schoolbook regular (everything, readable)
    courB12................Courier bold (everything, numeric, readable, uppercase)
    symb08.................Symbols (everything)
    helvB10................Helvetica bold (everything, readable, uppercase)
    timR12.................Times regular (uppercase)
    ncenB12................New Century Schoolbook bold (numeric)
    courR10................Courier regular (full)
 16:
    spleen_8x16............Spleen small display fonts (everything, full, numeric, readable, uppercase)
    ncenR12................New Century Schoolbook regular (everything, readable, uppercase)
    timR12.................Times regular (everything, readable)
    unifont................GNU unicode font (everything, full, numeric, readable, uppercase)
    courB10................Courier bold (full)
    helvB12................Helvetica bold (uppercase)
    courB14................Courier bold (numeric)
    timB12.................Times bold (everything, readable, uppercase)
    timB14.................Times bold (numeric)
    courR14................Courier regular (numeric)
 17:
    courB14................Courier bold (everything, readable, uppercase)
    helvB12................Helvetica bold (everything, readable)
    ncenB12................New Century Schoolbook bold (everything, readable, uppercase)
    helvR12................Helvetica regular (everything, readable, uppercase)
    courR14................Courier regular (everything, readable, uppercase)
    courB12................Courier bold (full)
    symb12.................Symbols (everything)
    timB10.................Times bold (full)
    timR10.................Times regular (full)
    helvB14................Helvetica bold (numeric)
    helvB10................Helvetica bold (full)
    courR12................Courier regular (full)
    ncenR14................New Century Schoolbook regular (numeric)
    ncenR10................New Century Schoolbook regular (full)
    timR14.................Times regular (numeric)
    helvR10................Helvetica regular (full)
    helvR14................Helvetica regular (numeric)
    ncenB14................New Century Schoolbook bold (numeric)
 18:
    ncenB10................New Century Schoolbook bold (full)
    helvR14................Helvetica regular (everything, readable, uppercase)
    9x18...................U8G2 default font (everything, full, numeric, readable, uppercase)
    helvB14................Helvetica bold (everything, readable, uppercase)
    timR14.................Times regular (everything, readable, uppercase)
    timB14.................Times bold (everything, readable, uppercase)
 19:
    battery19..............Battery level indicator (everything, full, numeric, readable, uppercase)
    timR12.................Times regular (full)
    ncenR14................New Century Schoolbook regular (everything, readable, uppercase)
    courR18................Courier regular (numeric)
    ncenB12................New Century Schoolbook bold (full)
    symb14.................Symbols (everything)
    ncenR12................New Century Schoolbook regular (full)
    courR14................Courier regular (full)
 20:
    courB18................Courier bold (numeric)
    helvB12................Helvetica bold (full)
    ncenB14................New Century Schoolbook bold (everything, readable, uppercase)
    courB14................Courier bold (full)
    timB12.................Times bold (full)
    10x20..................U8G2 default font (everything, full, numeric, readable, uppercase)
    helvR12................Helvetica regular (full)
 21:
    emoticons21............Emoticon font (everything, full, numeric, readable, uppercase)
    timR18.................Times regular (numeric)
    timB14.................Times bold (full)
    courB18................Courier bold (uppercase)
 22:
    courR18................Courier regular (everything, readable, uppercase)
    helvR14................Helvetica regular (full)
    ncenR18................New Century Schoolbook regular (numeric)
    courB18................Courier bold (everything, readable)
    helvR18................Helvetica regular (numeric)
    ncenB18................New Century Schoolbook bold (numeric)
    timR14.................Times regular (full)
    helvB18................Helvetica bold (numeric)
    timB18.................Times bold (numeric)
 23:
    helvB14................Helvetica bold (full)
    ncenB14................New Century Schoolbook bold (full)
    timB18.................Times bold (everything, readable, uppercase)
    ncenR14................New Century Schoolbook regular (full)
 24:
    helvB18................Helvetica bold (everything, readable, uppercase)
    spleen_12x24...........Spleen small display fonts (everything, full, numeric, readable, uppercase)
    ncenR18................New Century Schoolbook regular (uppercase)
    symb18.................Symbols (everything)
    battery24..............Battery level indicator (everything, full, numeric, readable, uppercase)
    timR18.................Times regular (uppercase)
    courR18................Courier regular (full)
    cursor.................Cursors (numeric)
 25:
    ncenB18................New Century Schoolbook bold (everything, readable, uppercase)
    timR18.................Times regular (everything, readable)
    ncenR18................New Century Schoolbook regular (everything, readable)
    helvR18................Helvetica regular (everything, readable, uppercase)
 26:
    courB18................Courier bold (full)
    timR24.................Times regular (numeric)
    freedoomr25n...........Doom! (everything, full, numeric, readable, uppercase)
    courR24................Courier regular (numeric)
 28:
    courR24................Courier regular (everything, readable, uppercase)
    courB24................Courier bold (numeric)
 29:
    helvR18................Helvetica regular (full)
    timR18.................Times regular (full)
    ncenR18................New Century Schoolbook regular (full)
    ncenB18................New Century Schoolbook bold (full)
    helvB18................Helvetica bold (full)
    timB18.................Times bold (full)
 30:
    courB24................Courier bold (everything, readable, uppercase)
    ncenB24................New Century Schoolbook bold (numeric)
 31:
    7_Seg_33x19............7 segment display font (everything, full, numeric, readable, uppercase)
    cursor.................Cursors (everything, full, readable, uppercase)
    helvB24................Helvetica bold (numeric, uppercase)
    timB24.................Times bold (numeric)
    ncenR24................New Century Schoolbook regular (numeric)
    timR24.................Times regular (uppercase)
    helvR24................Helvetica regular (numeric)
 32:
    helvB24................Helvetica bold (everything, readable)
    courR24................Courier regular (full)
    spleen_16x32...........Spleen small display fonts (everything, full, numeric, readable, uppercase)
    timR24.................Times regular (everything, readable)
    ncenB24................New Century Schoolbook bold (uppercase)
    timB24.................Times bold (uppercase)
 33:
    timB24.................Times bold (everything, readable)
    courB24................Courier bold (full)
    ncenR24................New Century Schoolbook regular (uppercase)
    ncenB24................New Century Schoolbook bold (everything, readable)
 34:
    symb24.................Symbols (everything)
    helvR24................Helvetica regular (everything, readable, uppercase)
    ncenR24................New Century Schoolbook regular (everything, readable)
 37:
    timB24.................Times bold (full)
    timR24.................Times regular (full)
 38:
    helvR24................Helvetica regular (full)
    helvB24................Helvetica bold (full)
 39:
    7_Seg_41x21............7 segment display font (everything, full, numeric, readable, uppercase)
    ncenR24................New Century Schoolbook regular (full)
 40:
    ncenB24................New Century Schoolbook bold (full)
 42:
    7Segments_26x42........7 segment display font (everything, full, numeric, readable, uppercase)
 64:
    spleen_32x64...........Spleen small display fonts (everything, full, numeric, readable, uppercase)
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
