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

Sets will only be genereated when *unique*; if a previous set for the font already contains an identical charset the current set will be skipped.

* Pay attention to the file sizes; the `extended` and `all` sets can get large, and will consume more ram on your target device.
* For a detailed font file description and preview look at the corresponding `.map` file in the 'maps' sub-folder.
  * This contains an ascii-art glyph for all characters in the font file; showing the name, size, bitmap and baseline.

In addition there are a number of symbol related charsets that can be generated in the [Unicode](/Unicode) folder, including dingbats, arrows, mathematical symbols, runes and more.

For usage see the `ezFBfont.py` documentation in the main `README`.

# The list

----------------------

Fonts as of 11 June 2024 organised by charset/family/height.
```
Base (0x00 - 0x3f) character set
--------------------------------
Size:   Family                                          Name
    9px:
        symbol  ..................ezFBfont_09_symb08_base.py
   13px:
        symbol  ..................ezFBfont_13_symb10_base.py
   14px:
        symbol  ..................ezFBfont_14_symb12_base.py
   17px:
        symbol  ..................ezFBfont_17_symb14_base.py
   19px:
       generic  ...............ezFBfont_19_battery19_base.py
   20px:
       generic  .............ezFBfont_20_emoticons21_base.py
   22px:
        symbol  ..................ezFBfont_22_symb18_base.py
   23px:
       generic  .................ezFBfont_23_cursorr_base.py
   24px:
       generic  ...............ezFBfont_24_battery24_base.py
   25px:
       generic  ..ezFBfont_25_u8g2_percent_circle_25_base.py
   30px:
       generic  ..................ezFBfont_30_cursor_base.py
        symbol  ..................ezFBfont_30_symb24_base.py
   32px:
       generic  .............ezFBfont_32_7_Seg_33x19_base.py
   40px:
       generic  .............ezFBfont_40_7_Seg_41x21_base.py
   42px:
       generic  .........ezFBfont_42_7Segments_26x42_base.py

Lower (0x40 - 0x7f) character set
---------------------------------
Size:   Family                                          Name
    6px:
       generic  ...............ezFBfont_06_m2icon_5_lower.py
    8px:
       generic  ...............ezFBfont_08_m2icon_7_lower.py
       generic  .....ezFBfont_08_open_iconic_www_1x_lower.py
       generic  .....ezFBfont_08_open_iconic_all_1x_lower.py
       generic  .ezFBfont_08_open_iconic_weather_1x_lower.py
       generic  ...ezFBfont_08_open_iconic_other_1x_lower.py
       generic  .....ezFBfont_08_open_iconic_gui_1x_lower.py
       generic  .....ezFBfont_08_open_iconic_app_1x_lower.py
       generic  ....ezFBfont_08_open_iconic_text_1x_lower.py
       generic  ....ezFBfont_08_open_iconic_play_1x_lower.py
       generic  ....ezFBfont_08_open_iconic_mime_1x_lower.py
       generic  ezFBfont_08_open_iconic_embedded_1x_lower.py
       generic  ...ezFBfont_08_open_iconic_check_1x_lower.py
       generic  ...ezFBfont_08_open_iconic_human_1x_lower.py
       generic  ...ezFBfont_08_open_iconic_arrow_1x_lower.py
       generic  ...ezFBfont_08_open_iconic_email_1x_lower.py
       generic  ...ezFBfont_08_open_iconic_thing_1x_lower.py
   11px:
       generic  ...............ezFBfont_11_m2icon_9_lower.py
   13px:
        symbol  .................ezFBfont_13_symb08_lower.py
   15px:
        symbol  .................ezFBfont_15_symb10_lower.py
   16px:
       generic  ....ezFBfont_16_open_iconic_mime_2x_lower.py
       generic  ...ezFBfont_16_open_iconic_arrow_2x_lower.py
       generic  .....ezFBfont_16_open_iconic_app_2x_lower.py
       generic  ezFBfont_16_open_iconic_embedded_2x_lower.py
       generic  .....ezFBfont_16_open_iconic_gui_2x_lower.py
       generic  ...ezFBfont_16_open_iconic_human_2x_lower.py
       generic  ...ezFBfont_16_open_iconic_other_2x_lower.py
       generic  ...ezFBfont_16_open_iconic_check_2x_lower.py
       generic  .....ezFBfont_16_open_iconic_all_2x_lower.py
       generic  .....ezFBfont_16_open_iconic_www_2x_lower.py
       generic  ....ezFBfont_16_open_iconic_text_2x_lower.py
       generic  .ezFBfont_16_open_iconic_weather_2x_lower.py
       generic  ...ezFBfont_16_open_iconic_email_2x_lower.py
       generic  ...ezFBfont_16_open_iconic_thing_2x_lower.py
       generic  ....ezFBfont_16_open_iconic_play_2x_lower.py
   17px:
        symbol  .................ezFBfont_17_symb12_lower.py
   19px:
        symbol  .................ezFBfont_19_symb14_lower.py
   21px:
       generic  ................ezFBfont_21_cursorr_lower.py
   24px:
       generic  ..............ezFBfont_24_battery24_lower.py
        symbol  .................ezFBfont_24_symb18_lower.py
   31px:
       generic  .................ezFBfont_31_cursor_lower.py
   32px:
       generic  ...ezFBfont_32_open_iconic_arrow_4x_lower.py
       generic  ....ezFBfont_32_open_iconic_text_4x_lower.py
       generic  ....ezFBfont_32_open_iconic_mime_4x_lower.py
       generic  .ezFBfont_32_open_iconic_weather_4x_lower.py
       generic  ...ezFBfont_32_open_iconic_other_4x_lower.py
       generic  .....ezFBfont_32_open_iconic_www_4x_lower.py
       generic  ...ezFBfont_32_open_iconic_human_4x_lower.py
       generic  ...ezFBfont_32_open_iconic_email_4x_lower.py
       generic  .....ezFBfont_32_open_iconic_all_4x_lower.py
       generic  ....ezFBfont_32_open_iconic_play_4x_lower.py
       generic  .....ezFBfont_32_open_iconic_gui_4x_lower.py
       generic  ezFBfont_32_open_iconic_embedded_4x_lower.py
       generic  ...ezFBfont_32_open_iconic_check_4x_lower.py
       generic  ...ezFBfont_32_open_iconic_thing_4x_lower.py
       generic  .....ezFBfont_32_open_iconic_app_4x_lower.py
   34px:
        symbol  .................ezFBfont_34_symb24_lower.py
   48px:
       generic  .....ezFBfont_48_open_iconic_gui_6x_lower.py
       generic  .....ezFBfont_48_open_iconic_www_6x_lower.py
       generic  ...ezFBfont_48_open_iconic_arrow_6x_lower.py
       generic  ...ezFBfont_48_open_iconic_check_6x_lower.py
       generic  ....ezFBfont_48_open_iconic_play_6x_lower.py
       generic  ....ezFBfont_48_open_iconic_text_6x_lower.py
       generic  .ezFBfont_48_open_iconic_weather_6x_lower.py
       generic  .....ezFBfont_48_open_iconic_app_6x_lower.py
       generic  .....ezFBfont_48_open_iconic_all_6x_lower.py
       generic  ...ezFBfont_48_open_iconic_thing_6x_lower.py
       generic  ...ezFBfont_48_open_iconic_email_6x_lower.py
       generic  ....ezFBfont_48_open_iconic_mime_6x_lower.py
       generic  ezFBfont_48_open_iconic_embedded_6x_lower.py
       generic  ...ezFBfont_48_open_iconic_human_6x_lower.py
       generic  ...ezFBfont_48_open_iconic_other_6x_lower.py
   64px:
       generic  .ezFBfont_64_open_iconic_weather_8x_lower.py
       generic  ...ezFBfont_64_open_iconic_arrow_8x_lower.py
       generic  .....ezFBfont_64_open_iconic_all_8x_lower.py
       generic  .....ezFBfont_64_open_iconic_www_8x_lower.py
       generic  ...ezFBfont_64_open_iconic_other_8x_lower.py
       generic  .....ezFBfont_64_open_iconic_gui_8x_lower.py
       generic  ...ezFBfont_64_open_iconic_thing_8x_lower.py
       generic  ....ezFBfont_64_open_iconic_text_8x_lower.py
       generic  ...ezFBfont_64_open_iconic_human_8x_lower.py
       generic  ...ezFBfont_64_open_iconic_check_8x_lower.py
       generic  .....ezFBfont_64_open_iconic_app_8x_lower.py
       generic  ezFBfont_64_open_iconic_embedded_8x_lower.py
       generic  ....ezFBfont_64_open_iconic_play_8x_lower.py
       generic  ....ezFBfont_64_open_iconic_mime_8x_lower.py
       generic  ...ezFBfont_64_open_iconic_email_8x_lower.py

Mid (0x80 - 0xbf) character set
-------------------------------
Size:   Family                                          Name
    8px:
       generic  .......ezFBfont_08_open_iconic_all_1x_mid.py
   15px:
        symbol  ...................ezFBfont_15_symb10_mid.py
        symbol  ...................ezFBfont_15_symb08_mid.py
   16px:
       generic  .......ezFBfont_16_open_iconic_all_2x_mid.py
   17px:
        symbol  ...................ezFBfont_17_symb12_mid.py
   19px:
        symbol  ...................ezFBfont_19_symb14_mid.py
   24px:
        symbol  ...................ezFBfont_24_symb18_mid.py
   25px:
       generic  ...................ezFBfont_25_cursor_mid.py
   32px:
       generic  .......ezFBfont_32_open_iconic_all_4x_mid.py
   34px:
        symbol  ...................ezFBfont_34_symb24_mid.py
   48px:
       generic  .......ezFBfont_48_open_iconic_all_6x_mid.py
   64px:
       generic  .......ezFBfont_64_open_iconic_all_8x_mid.py

Upper (0xc0 - 0xff) character set
---------------------------------
Size:   Family                                          Name
    8px:
       generic  .....ezFBfont_08_open_iconic_all_1x_upper.py
   15px:
        symbol  .................ezFBfont_15_symb08_upper.py
        symbol  .................ezFBfont_15_symb10_upper.py
   16px:
       generic  .....ezFBfont_16_open_iconic_all_2x_upper.py
   17px:
        symbol  .................ezFBfont_17_symb12_upper.py
   19px:
        symbol  .................ezFBfont_19_symb14_upper.py
   24px:
        symbol  .................ezFBfont_24_symb18_upper.py
   32px:
       generic  .....ezFBfont_32_open_iconic_all_4x_upper.py
   34px:
        symbol  .................ezFBfont_34_symb24_upper.py
   48px:
       generic  .....ezFBfont_48_open_iconic_all_6x_upper.py
   64px:
       generic  .....ezFBfont_64_open_iconic_all_8x_upper.py

Extended (0x100 - 0xfff) character set
--------------------------------------
Size:   Family                                          Name
    8px:
       generic  ..ezFBfont_08_open_iconic_all_1x_extended.py
   16px:
       generic  ..ezFBfont_16_open_iconic_all_2x_extended.py
   32px:
       generic  ..ezFBfont_32_open_iconic_all_4x_extended.py
   48px:
       generic  ..ezFBfont_48_open_iconic_all_6x_extended.py
   64px:
       generic  ..ezFBfont_64_open_iconic_all_8x_extended.py

Full (0x00 - 0xfff) character set
---------------------------------
Size:   Family                                          Name
    8px:
       generic  ......ezFBfont_08_open_iconic_all_1x_full.py
   15px:
        symbol  ..................ezFBfont_15_symb10_full.py
        symbol  ..................ezFBfont_15_symb08_full.py
   16px:
       generic  ......ezFBfont_16_open_iconic_all_2x_full.py
   17px:
        symbol  ..................ezFBfont_17_symb12_full.py
   19px:
        symbol  ..................ezFBfont_19_symb14_full.py
   23px:
       generic  .................ezFBfont_23_cursorr_full.py
   24px:
       generic  ...............ezFBfont_24_battery24_full.py
        symbol  ..................ezFBfont_24_symb18_full.py
   31px:
       generic  ..................ezFBfont_31_cursor_full.py
   32px:
       generic  ......ezFBfont_32_open_iconic_all_4x_full.py
   34px:
        symbol  ..................ezFBfont_34_symb24_full.py
   48px:
       generic  ......ezFBfont_48_open_iconic_all_6x_full.py
   64px:
       generic  ......ezFBfont_64_open_iconic_all_8x_full.py
```
---------------------
## Converter script
The font structure is created by the 'build-sets.py' script in the `bdf2dict` folder, see the README there for more.

The `sets.py` file in this folder contains the character definitions and font source.
Micropython font module tree for: Symbols
