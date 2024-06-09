# Latin-1 Font files

This folder contains font files suitable for use with `ezFBfont` and Peter Hinches `writer` class.

They are organised by character set, font family and vertical size.
* See below for a discussion of the available character sets.
* The font family is that declared in the source font file, or `Generic` if unknown.
* The 'height' of each font set is the *true height*; the height of the tallest character in that set.
* This can vary from the height declared in the font name!
* The same fonts may appear listed as different heights depending which character set is being provided.
  * eg: numeric charsets are typically shorter than the full ascii charsets.

There is a mixture of proportional width and monospaced fonts in the collection; the font name will typically note the size for monospaced fonts. The proportional (X11) fonts also mostly come in regular and bold weights.

# COPYRIGHT
Please read the copyright notices in the font files themselves; all the fonts here were sourced from the [u8g2](https://github.com/olikraus/u8g2/blob/master/LICENSE) project fonts; a curated repository of freely redistributable + open-source fonts.

All fonts retain copyright info in the `.py` include file for the font; some are very simple, especially the fonts created for the U8G2 project itself. Some are more general open-source type licences, all are redistributable as is.

If using the X11 fonts (COUR, HELV, NCEN, TIM, SYMB) you should include the Adobe/Digital boilerplate licence in your distributed codes main licence, see the example in this repositories [LICENSE](/LICENSE) file.

# Collections (character sets)

The character sets are organised by function, with small sets for time and sensor data, and larger sets with the full character range, as follows:

* **time** : ``` +-.0123456789:```
* **num** : ``` %()*+,-./0123456789:°```
* **upper** : ``` !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_```
* **ascii** : ``` !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~```
* **supp** : ```¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ```
* **latin** : ``` !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ```
* **full** : All chars from `0x00` to `0xFF`

Nb: Most charsets begin with `0x32`, the space character.

These can loosely be described as:
* **Time** : numbers and seperators for clocks and timers.
* **Num**eric : numbers, seperators and related symbols for displaying values.
* **Upper**case : ascii charset up to `0x5F`, lower memory, useful for symbols etc.
* **Ascii** : full ascii charset up to `0x7F`.
* **Supp**lemental : characters from `0xA0` to `0xFF`.
* **Latin** : all the *printable* chars in the font up to `0xFF`.
* **Full** : every character in the font pack up to `0xFF`, even if not *printable*.

Only 'Basic Latin' and 'Latin Supplemental' characters are covered by these sets. If you want Latin characters from the Unicode 'Latin Extended ..' or 'IPA Extensions' blocks these can be found in the [Unicode](/Unicode) folder.

* Pay attention to the file sizes; the full sets (especially the '`latin`' set) can get large.
* For a detailed font file description and preview look at the corresponding `.map` file in the 'maps' sub-folder.
  * This contains an ascii-art glyph for all characters in the font file; showing the name, size, bitmap and baseline.

For usage see the `ezFBfont.py` documentation in the main `README`.

# The list

----------------------

Fonts as of ????? organised by charset/family/height.
```
###TBD
```

---------------------

## Converter script
The font structure is created by the 'convert.py' script in the `tooling` folder, see the README there for more.

The `sets.py` file in this folder contains the character definitions and source font filters.
