# Font files

This folder contains font files suitable for use with `ezFBfont` and Peter Hinches `writer` class.

They are organised by vertical size; and (where possible) come in 3 different character sets:
* The 'height' of each font set is the *true height*; the height of the tallest character in that set.
* This can vary from the height declared in the font name!
* The same font may appear listed as different heights depending which character set is being provided.
  * eg: numeric charsets are typically shorter than the full charsets.

There is a mixture of proportional width and monospaced fonts in the collection; the font name will typically note the size for monospaced fonts. The proportional (X11) fonts also mostly come in regular and bold weights.

# COPYRIGHT
Please read the copyright notices in the font files themselves; all the fonts here were sourced from the [u8g2](https://github.com/olikraus/u8g2/blob/master/LICENSE) project fonts; a curated repository of freely redistributable + open-source fonts.

All fonts retain copyright info in the `.py` include file for the font; some are very simple, especially the fonts created for the U8G2 project itself. Some are more general open-source type licences, all are redistributable as is.

If using the X11 fonts (COUR, HELV, NCEN, TIM, SYMB) you should include the Adobe/Digital boilerplate licence in your distributed codes main licence, see the example in this repositories [LICENSE](/LICENSE) file.

# Collections (character sets)

The character sets are:
```python
# all charsets begin with 0x32, the space character
t =  +-.0123456789
n =  %()*+,-./0123456789:°
r =  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
e =  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþ
```
These can loosely be described as:
* **t**ime (numbers and seperators for clocks and timers)
* **n**umeric (numbers, seperators and related symbols for displaying values)
* **r**eadable (ascii charset up to `0x7F`)
* **e**verything (all the available latin-1 chars in the font up to `0xFF`)

Pay attention to the file sizes;
* With the `e` (everything) set characters will only be present when they are defined in the font source!
* Other charsets encode a 'blank' character in place of missing characters, this *can* make them bigger than the `e` set!

For more detailed font descriptions and previews look for the corresponding font entry in the U8G2 wiki:
https://github.com/olikraus/u8g2/wiki/fntlistall

For usage see the `ezFBfont.py` documentation in the main `README`.

# The list
----------------------

Fonts as of May 14, 2024, organised by height.
```
  4px:
    u8glib_4............... U8G2 native font (time)
  5px:
    font_tiny5............. Tiny font (time)
    tom_thumb.............. Tom Thumb font (numeric, time)
  6px:
    4x6.................... U8G2 default font (everything, numeric, readable, time)
    font_tiny5............. Tiny font (numeric)
    tom_thumb.............. Tom Thumb font (everything, readable)
    u8g2_squeezed_bold_6... U8G2 native font (time)
    u8g2_squeezed_regular_6 U8G2 native font (time)
    u8glib_4............... U8G2 native font (numeric, readable)
  7px:
    5x7.................... U8G2 default font (everything, numeric, readable, time)
    courB08................ Courier bold (time)
    courR08................ Courier regular (time)
    font_tiny5............. Tiny font (everything, readable)
    timB08................. Times bold (time)
    timR08................. Times regular (time)
    u8g2_squeezed_bold_6... U8G2 native font (everything, numeric, readable)
    u8g2_squeezed_bold_7... U8G2 native font (time)
    u8g2_squeezed_regular_6 U8G2 native font (everything, numeric, readable)
    u8g2_squeezed_regular_7 U8G2 native font (time)
    u8glib_4............... U8G2 native font (everything)
  8px:
    5x8.................... U8G2 default font (everything, numeric, readable, time)
    helvB08................ Helvetica bold (time)
    helvB08_gps............ Helvetica bold (time)
    helvR08................ Helvetica regular (time)
    ncenB08................ New Century Schoolbook bold (time)
    ncenR08................ New Century Schoolbook regular (time)
    spleen_5x8............. Spleen small display font (everything, numeric, readable, time)
    u8g2_squeezed_bold_7... U8G2 native font (everything, numeric, readable)
    u8g2_squeezed_regular_7 U8G2 native font (everything, numeric, readable)
  9px:
    6x9.................... U8G2 default font (everything, numeric, readable, time)
    courB08................ Courier bold (numeric)
    timR08................. Times regular (numeric)
 10px:
    6x10................... U8G2 default font (everything, numeric, readable, time)
    courB08................ Courier bold (readable)
    courB10................ Courier bold (time)
    courR08................ Courier regular (numeric, readable)
    courR10................ Courier regular (time)
    helvB08................ Helvetica bold (numeric)
    helvB08_gps............ Helvetica bold (numeric)
    helvR08................ Helvetica regular (numeric)
    ncenB08................ New Century Schoolbook bold (numeric)
    ncenR08................ New Century Schoolbook regular (numeric)
    timB08................. Times bold (numeric)
    timB10................. Times bold (time)
    timR10................. Times regular (time)
 11px:
    courB08................ Courier bold (everything)
    courB12................ Courier bold (time)
    courR08................ Courier regular (everything)
    courR12................ Courier regular (time)
    helvB08................ Helvetica bold (readable)
    helvB08_gps............ Helvetica bold (everything, readable)
    helvB10................ Helvetica bold (time)
    helvR08................ Helvetica regular (readable)
    helvR10................ Helvetica regular (time)
    ncenB08................ New Century Schoolbook bold (readable)
    ncenB10................ New Century Schoolbook bold (time)
    ncenR08................ New Century Schoolbook regular (readable)
    ncenR10................ New Century Schoolbook regular (time)
    timB08................. Times bold (readable)
    timB12................. Times bold (time)
    timR08................. Times regular (readable)
    timR12................. Times regular (time)
 12px:
    6x12................... U8G2 default font (everything, numeric, readable, time)
    courB10................ Courier bold (numeric)
    courB14................ Courier bold (time)
    courR10................ Courier regular (numeric)
    courR14................ Courier regular (time)
    freedoomr10r........... Doom! (everything, numeric, readable, time)
    helvB12................ Helvetica bold (time)
    helvR12................ Helvetica regular (time)
    ncenB12................ New Century Schoolbook bold (time)
    ncenR12................ New Century Schoolbook regular (time)
    spleen_6x12............ Spleen small display font (everything, numeric, readable, time)
 13px:
    6x13................... U8G2 default font (everything, numeric, readable, time)
    7x13................... U8G2 default font (everything, numeric, readable, time)
    8x13................... U8G2 default font (everything, numeric, readable, time)
    courR12................ Courier regular (numeric)
    helvB08................ Helvetica bold (everything)
    helvB14................ Helvetica bold (time)
    helvR08................ Helvetica regular (everything)
    helvR14................ Helvetica regular (time)
    ncenB08................ New Century Schoolbook bold (everything)
    ncenB10................ New Century Schoolbook bold (numeric)
    ncenR08................ New Century Schoolbook regular (everything)
    ncenR10................ New Century Schoolbook regular (numeric)
    timB08................. Times bold (everything)
    timB10................. Times bold (numeric)
    timB14................. Times bold (time)
    timR08................. Times regular (everything)
    timR10................. Times regular (numeric)
    timR14................. Times regular (time)
 14px:
    7x14................... U8G2 default font (everything, numeric, readable, time)
    courB10................ Courier bold (readable)
    courR10................ Courier regular (readable)
    helvB10................ Helvetica bold (numeric)
    helvR10................ Helvetica regular (numeric)
    ncenB14................ New Century Schoolbook bold (time)
    ncenR14................ New Century Schoolbook regular (time)
    timB10................. Times bold (readable)
    timR10................. Times regular (readable)
    timR12................. Times regular (numeric)
 15px:
    9x15................... U8G2 default font (everything, numeric, readable, time)
    courB12................ Courier bold (numeric, readable)
    courR10................ Courier regular (everything)
    courR12................ Courier regular (readable)
    courR18................ Courier regular (time)
    helvB10................ Helvetica bold (readable)
    helvB12................ Helvetica bold (numeric)
    helvR10................ Helvetica regular (readable)
    ncenB10................ New Century Schoolbook bold (readable)
    ncenB12................ New Century Schoolbook bold (numeric)
    ncenR10................ New Century Schoolbook regular (readable)
    ncenR12................ New Century Schoolbook regular (numeric)
    timB12................. Times bold (numeric)
 16px:
    courB10................ Courier bold (everything)
    courB14................ Courier bold (numeric)
    courB18................ Courier bold (time)
    courR14................ Courier regular (numeric)
    helvR12................ Helvetica regular (numeric)
    ncenR12................ New Century Schoolbook regular (readable)
    spleen_8x16............ Spleen small display font (everything, numeric, readable, time)
    timB12................. Times bold (readable)
    timR12................. Times regular (readable)
    unifont................ GNU unicode font (everything, numeric, readable, time)
 17px:
    courB12................ Courier bold (everything)
    courB14................ Courier bold (readable)
    courR12................ Courier regular (everything)
    courR14................ Courier regular (readable)
    helvB10................ Helvetica bold (everything)
    helvB12................ Helvetica bold (readable)
    helvR10................ Helvetica regular (everything)
    helvR12................ Helvetica regular (readable)
    ncenB12................ New Century Schoolbook bold (readable)
    ncenB14................ New Century Schoolbook bold (numeric)
    ncenR10................ New Century Schoolbook regular (everything)
    ncenR14................ New Century Schoolbook regular (numeric)
    timB10................. Times bold (everything)
    timB14................. Times bold (numeric)
    timB18................. Times bold (time)
    timR10................. Times regular (everything)
    timR14................. Times regular (numeric)
    timR18................. Times regular (time)
 18px:
    9x18................... U8G2 default font (everything, numeric, readable, time)
    helvB14................ Helvetica bold (numeric, readable)
    helvB18................ Helvetica bold (time)
    helvR14................ Helvetica regular (numeric, readable)
    helvR18................ Helvetica regular (time)
    ncenB10................ New Century Schoolbook bold (everything)
    ncenB18................ New Century Schoolbook bold (time)
    ncenR18................ New Century Schoolbook regular (time)
    timB14................. Times bold (readable)
    timR14................. Times regular (readable)
 19px:
    battery19.............. Battery level indicator (everything, numeric, readable, time)
    courR14................ Courier regular (everything)
    courR18................ Courier regular (numeric)
    ncenB12................ New Century Schoolbook bold (everything)
    ncenR12................ New Century Schoolbook regular (everything)
    ncenR14................ New Century Schoolbook regular (readable)
    timR12................. Times regular (everything)
 20px:
    10x20.................. U8G2 default font (everything, numeric, readable, time)
    courB14................ Courier bold (everything)
    courR24................ Courier regular (time)
    helvB12................ Helvetica bold (everything)
    helvR12................ Helvetica regular (everything)
    ncenB14................ New Century Schoolbook bold (readable)
    timB12................. Times bold (everything)
 21px:
    courB18................ Courier bold (numeric)
    courB24................ Courier bold (time)
    emoticons21............ Emoticon font (everything, numeric, readable, time)
    timB14................. Times bold (everything)
 22px:
    courB18................ Courier bold (readable)
    courR18................ Courier regular (readable)
    helvR14................ Helvetica regular (everything)
    ncenB18................ New Century Schoolbook bold (numeric)
    ncenR18................ New Century Schoolbook regular (numeric)
    timB18................. Times bold (numeric)
    timR14................. Times regular (everything)
    timR18................. Times regular (numeric)
 23px:
    helvB14................ Helvetica bold (everything)
    ncenB14................ New Century Schoolbook bold (everything)
    ncenR14................ New Century Schoolbook regular (everything)
    timB18................. Times bold (readable)
    timB24................. Times bold (time)
    timR24................. Times regular (time)
 24px:
    battery24.............. Battery level indicator (everything, numeric, readable, time)
    courR18................ Courier regular (everything)
    cursor................. Cursors (numeric, time)
    helvB18................ Helvetica bold (numeric, readable)
    helvB24................ Helvetica bold (time)
    helvR18................ Helvetica regular (numeric)
    helvR24................ Helvetica regular (time)
    ncenB24................ New Century Schoolbook bold (time)
    spleen_12x24........... Spleen small display font (everything, numeric, readable, time)
 25px:
    helvR18................ Helvetica regular (readable)
    ncenB18................ New Century Schoolbook bold (readable)
    ncenR18................ New Century Schoolbook regular (readable)
    ncenR24................ New Century Schoolbook regular (time)
    timR18................. Times regular (readable)
 26px:
    courB18................ Courier bold (everything)
    courR24................ Courier regular (numeric)
    freedoomr25n........... Doom! (everything, numeric, readable, time)
 28px:
    courB24................ Courier bold (numeric)
    courR24................ Courier regular (readable)
    timR24................. Times regular (numeric)
 29px:
    helvB18................ Helvetica bold (everything)
    helvR18................ Helvetica regular (everything)
    ncenB18................ New Century Schoolbook bold (everything)
    ncenR18................ New Century Schoolbook regular (everything)
    timB18................. Times bold (everything)
    timR18................. Times regular (everything)
 30px:
    courB24................ Courier bold (readable)
    ncenB24................ New Century Schoolbook bold (numeric)
 31px:
    7_Seg_33x19............ 7 segment display font (everything, numeric, readable, time)
    cursor................. Cursors (everything, readable)
    helvB24................ Helvetica bold (numeric)
    ncenR24................ New Century Schoolbook regular (numeric)
    timB24................. Times bold (numeric)
 32px:
    courR24................ Courier regular (everything)
    helvB24................ Helvetica bold (readable)
    spleen_16x32........... Spleen small display font (everything, numeric, readable, time)
    timR24................. Times regular (readable)
 33px:
    courB24................ Courier bold (everything)
    helvR24................ Helvetica regular (numeric)
    ncenB24................ New Century Schoolbook bold (readable)
    timB24................. Times bold (readable)
 34px:
    helvR24................ Helvetica regular (readable)
    ncenR24................ New Century Schoolbook regular (readable)
 37px:
    timB24................. Times bold (everything)
    timR24................. Times regular (everything)
 38px:
    helvB24................ Helvetica bold (everything)
    helvR24................ Helvetica regular (everything)
 39px:
    7_Seg_41x21............ 7 segment display font (everything, numeric, readable, time)
    ncenR24................ New Century Schoolbook regular (everything)
 40px:
    ncenB24................ New Century Schoolbook bold (everything)
 42px:
    7Segments_26x42........ 7 segment display font (everything, numeric, readable, time)
 64px:
    spleen_32x64........... Spleen small display font (everything, numeric, readable, time)
```
---------------------

# Housekeeping
Stuff related to building this collection

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
