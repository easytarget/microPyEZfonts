# Symbol Font files

This folder contains font files suitable for use with `ezFBfont` and Peter Hinches `writer` class.

They are organised by font family, character set and vertical size.
* See below for a discussion of the available character sets.
* The font family is that declared in the source font file, or `Generic` if unknown.
* The 'height' of each font set is the *true height*; the height of the tallest character in that set.
  * This can vary from the height declared in the font name!
  * The same fonts may appear listed as different heights depending which character set is being provided.

There is a mixture of proportional width and monospaced fonts in the collection; the font name will typically note the size for monospaced fonts. The proportional (X11) fonts also mostly come in regular and bold weights.

# COPYRIGHT
Please read the copyright notices in the font files themselves; all the fonts here were sourced from the [u8g2](https://github.com/olikraus/u8g2/blob/master/LICENSE) project fonts; a curated repository of freely redistributable + open-source fonts.

All fonts retain copyright info in the `.py` include file for the font; some are very simple, especially the fonts created for the U8G2 project itself. Some are more general open-source type licences, all are redistributable as is.

If using the X11 fonts (COUR, HELV, NCEN, TIM, SYMB) you should include the Adobe/Digital boilerplate licence in your distributed codes main licence, see the example in this repositories [LICENSE](/LICENSE) file.

# Collections (character sets)

The symbol character sets are organised into logical blocks based on the ordinal (character #) values. The sets are:

* **base** : `0x00` through `0x39`
* **lower** : `0x40` through `0x80`
* **mid** : `0x80` through `0xC0`
* **upper** : `0xC0` through `0x100`
* **extended** : `0x100` through `0xFFF`
* **full** : `0x00` through `0xFFF`

These are essentially blocks of 64 characters covering the first 256 character values. Plus an extended range since several symbol fonts extend beyond `0xFF`.

In addition there are a number of symbol related blocks in the [Unicode](/Unicode) folder, includingrd dingbats, arrows, mathematical symbols, runes and more.


* Pay attention to the file sizes; the `extended` and `all` sets can get large, and will consume more ram on your target device.
* For a detailed font file description and preview look at the corresponding `.map` file in the 'maps' sub-folder.
  * This contains an ascii-art glyph for all characters in the font file; showing the name, size, bitmap and baseline.

For usage see the `ezFBfont.py` documentation in the main `README`.

# The list

----------------------

Fonts as of ????? June 2024 organised by charset/family/height.
```
```

---------------------

## Converter script
The font structure is created by the 'convert.py' script in the `tooling` folder, see the README there for more.

The `sets.py` file in this folder contains the character definitions and source font filters.
