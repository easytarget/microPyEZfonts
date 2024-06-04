# Latin-1 Font files

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
t : ``` +-.0123456789:```
n : ``` %()*+,-./0123456789:°```
u : ``` !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_```
r : ``` !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_```abcdefghijklmnopqrstuvwxyz{|}~```
s : ```¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ```
e : ``` !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ```
Nb: All charsets except `e` begin with 0x32, the space character
These can loosely be described as:
* **t**ime (numbers and seperators for clocks and timers)
* **n**umeric (numbers, seperators and related symbols for displaying values)
* **u**uppercase (ascii charset up to `0x5F`, lower memory, useful for symbols etc)
* **r**eadable (ascii charset up to `0x7F`)
* **s**upplemental (characters from `0xA0` to `0xFF`)
* **e**verything (all the *printable* latin-1 chars in the font up to `0xFF`)

Pay attention to the file sizes; the full sets (especially the '`e`' set) can get large. Font size is a major factor too.

For more detailed font descriptions and previews look for the corresponding font entry in the U8G2 wiki:
https://github.com/olikraus/u8g2/wiki/fntlistall

For usage see the `ezFBfont.py` documentation in the main `README`.

# The list
----------------------

Fonts as of May 14, 2024, organised by height.
```
```
---------------------

# Housekeeping
Stuff related to building this collection

## Converter script
The font structure is created by the 'convert.py' script in the `tooling` folder, see the README there for more.
