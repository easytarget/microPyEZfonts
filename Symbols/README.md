# Symbol Font Files

This folder contains font files for use with `ezFBfont` and Peter Hinches' `writer` class.

They are organized by font family, character set, and vertical size:
* See the discussion below on the different character sets.
* The font family is taken from the source font file. If unknown, it is labeled `Generic`.
* Each font set's height is the *true height*—meaning the height of the tallest character in that set.
  * This may differ from the height indicated in the font name!
  * The same fonts might appear with different heights depending on the character set being used.

There are both proportional-width and monospaced fonts in this collection. For monospaced fonts, the font name typically specifies the size. The proportional (X11) fonts usually come in both regular and bold styles.

# COPYRIGHT
Please review the copyright details in each font file. All fonts here are from the [u8g2](https://github.com/olikraus/u8g2/blob/master/LICENSE) project fonts, a collection of freely redistributable and open-source fonts.

All fonts keep copyright information in the `.py` include file for each font. Some have simple notices, particularly those created for the U8G2 project, while others have more general open-source licenses, and all are freely redistributable.

If you use any X11 fonts (such as COUR, HELV, NCEN, TIM, SYMB), please add the Adobe/Digital boilerplate license in your main code license, as seen in this repository’s [LICENSE](/LICENSE) file.

# Collections (Character Sets)

The symbol character sets are grouped into blocks based on ordinal (character #) values. These sets include:

* `  0x0_0x39` : **base**
* `  0x40_0x7F`: **lower**
* `  0x80_0xBF`: **mid**
* `  0xC0_0xFF`: **upper**
* `0x100_0x1FF`: **extended**
* `  0x0_0xFFF`: **full**

These blocks contain groups of 64 characters each, covering the first 256 character values. Additionally, an extended range is included since some symbol fonts go beyond `0xFF`.

Sets are generated only if they are *unique*; if a previous set already includes an identical charset, the current set will be skipped.

* Watch the file sizes; the `extended` and `all` sets can become large and use more memory on your device.
* For a full font description and preview, check the corresponding `.map` file in the 'maps' sub-folder.
  * The `.map` file includes an ASCII art glyph of all characters in the font file, showing each character's name, size, bitmap, and baseline.

Additionally, various symbol-related character sets can be generated in the [Unicode](/Unicode) folder, including dingbats, arrows, mathematical symbols, runes, and more.

For usage instructions, refer to the `ezFBfont.py` documentation in the main `README`.

# The List

This is a list of fonts (as of June 18, 2024) organized by character set, family, and height.
```
Micropython font module tree for: Symbols

Base (0x00 - 0x3f) character set
--------------------------------
Size:   Family                                              Name
    9px:
        symbol  ..................ezFBfont_symb08_0x0_0x39_09.py
   13px:
        symbol  ..................ezFBfont_symb10_0x0_0x39_13.py
   14px:
        symbol  ..................ezFBfont_symb12_0x0_0x39_14.py
   17px:
        symbol  ..................ezFBfont_symb14_0x0_0x39_17.py
   19px:
       generic  ...............ezFBfont_battery19_0x0_0x39_19.py
   21px:
       generic  .............ezFBfont_emoticons21_0x0_0x39_21.py
   22px:
        symbol  ..................ezFBfont_symb18_0x0_0x39_22.py
   23px:
       generic  .................ezFBfont_cursorr_0x0_0x39_23.py
   24px:
       generic  ...............ezFBfont_battery24_0x0_0x39_24.py
   25px:
       generic  ..ezFBfont_u8g2_percent_circle_25_0x0_0x39_25.py
   29px:
       generic  .............ezFBfont_7_Seg_33x19_0x0_0x39_29.py
   30px:
       generic  ..................ezFBfont_cursor_0x0_0x39_30.py
        symbol  ..................ezFBfont_symb24_0x0_0x39_30.py
   37px:
       generic  .............ezFBfont_7_Seg_41x21_0x0_0x39_37.py
   42px:
       generic  .........ezFBfont_7Segments_26x42_0x0_0x39_42.py

Lower (0x40 - 0x7f) character set
---------------------------------
Size:   Family                                              Name
    6px:
       generic  ...............ezFBfont_m2icon_5_0x40_0x79_06.py
    8px:
       generic  ...............ezFBfont_m2icon_7_0x40_0x79_08.py
        iconic  ...ezFBfont_open_iconic_check_1x_0x40_0x79_08.py
        iconic  ezFBfont_open_iconic_embedded_1x_0x40_0x79_08.py
        iconic  ....ezFBfont_open_iconic_play_1x_0x40_0x79_08.py
        iconic  .....ezFBfont_open_iconic_app_1x_0x40_0x79_08.py
        iconic  .....ezFBfont_open_iconic_all_1x_0x40_0x79_08.py
        iconic  .....ezFBfont_open_iconic_gui_1x_0x40_0x79_08.py
        iconic  ...ezFBfont_open_iconic_other_1x_0x40_0x79_08.py
        iconic  ....ezFBfont_open_iconic_mime_1x_0x40_0x79_08.py
        iconic  ...ezFBfont_open_iconic_human_1x_0x40_0x79_08.py
        iconic  ...ezFBfont_open_iconic_thing_1x_0x40_0x79_08.py
        iconic  ....ezFBfont_open_iconic_text_1x_0x40_0x79_08.py
        iconic  .....ezFBfont_open_iconic_www_1x_0x40_0x79_08.py
        iconic  .ezFBfont_open_iconic_weather_1x_0x40_0x79_08.py
        iconic  ...ezFBfont_open_iconic_email_1x_0x40_0x79_08.py
        iconic  ...ezFBfont_open_iconic_arrow_1x_0x40_0x79_08.py
   11px:
       generic  ...............ezFBfont_m2icon_9_0x40_0x79_11.py
   13px:
        symbol  .................ezFBfont_symb08_0x40_0x79_13.py
   16px:
        iconic  .....ezFBfont_open_iconic_gui_2x_0x40_0x79_16.py
        iconic  ....ezFBfont_open_iconic_play_2x_0x40_0x79_16.py
        iconic  ...ezFBfont_open_iconic_thing_2x_0x40_0x79_16.py
        iconic  ....ezFBfont_open_iconic_mime_2x_0x40_0x79_16.py
        iconic  .ezFBfont_open_iconic_weather_2x_0x40_0x79_16.py
        iconic  ...ezFBfont_open_iconic_email_2x_0x40_0x79_16.py
        iconic  ...ezFBfont_open_iconic_check_2x_0x40_0x79_16.py
        iconic  ...ezFBfont_open_iconic_other_2x_0x40_0x79_16.py
        iconic  ...ezFBfont_open_iconic_arrow_2x_0x40_0x79_16.py
        iconic  ....ezFBfont_open_iconic_text_2x_0x40_0x79_16.py
        iconic  ...ezFBfont_open_iconic_human_2x_0x40_0x79_16.py
        iconic  .....ezFBfont_open_iconic_all_2x_0x40_0x79_16.py
        iconic  .....ezFBfont_open_iconic_www_2x_0x40_0x79_16.py
        iconic  .....ezFBfont_open_iconic_app_2x_0x40_0x79_16.py
        iconic  ezFBfont_open_iconic_embedded_2x_0x40_0x79_16.py
   17px:
        symbol  .................ezFBfont_symb12_0x40_0x79_17.py
   19px:
        symbol  .................ezFBfont_symb14_0x40_0x79_19.py
   21px:
       generic  ................ezFBfont_cursorr_0x40_0x79_21.py
   24px:
       generic  ..............ezFBfont_battery24_0x40_0x79_24.py
        symbol  .................ezFBfont_symb18_0x40_0x79_24.py
   31px:
       generic  .................ezFBfont_cursor_0x40_0x79_31.py
   32px:
        iconic  ...ezFBfont_open_iconic_email_4x_0x40_0x79_32.py
        iconic  .....ezFBfont_open_iconic_www_4x_0x40_0x79_32.py
        iconic  ...ezFBfont_open_iconic_other_4x_0x40_0x79_32.py
        iconic  ...ezFBfont_open_iconic_thing_4x_0x40_0x79_32.py
        iconic  .ezFBfont_open_iconic_weather_4x_0x40_0x79_32.py
        iconic  .....ezFBfont_open_iconic_all_4x_0x40_0x79_32.py
        iconic  ...ezFBfont_open_iconic_check_4x_0x40_0x79_32.py
        iconic  ....ezFBfont_open_iconic_text_4x_0x40_0x79_32.py
        iconic  ....ezFBfont_open_iconic_play_4x_0x40_0x79_32.py
        iconic  ....ezFBfont_open_iconic_mime_4x_0x40_0x79_32.py
        iconic  .....ezFBfont_open_iconic_gui_4x_0x40_0x79_32.py
        iconic  ...ezFBfont_open_iconic_arrow_4x_0x40_0x79_32.py
        iconic  .....ezFBfont_open_iconic_app_4x_0x40_0x79_32.py
        iconic  ezFBfont_open_iconic_embedded_4x_0x40_0x79_32.py
        iconic  ...ezFBfont_open_iconic_human_4x_0x40_0x79_32.py
   34px:
        symbol  .................ezFBfont_symb24_0x40_0x79_34.py
   48px:
        iconic  .ezFBfont_open_iconic_weather_6x_0x40_0x79_48.py
        iconic  ...ezFBfont_open_iconic_email_6x_0x40_0x79_48.py
        iconic  ...ezFBfont_open_iconic_check_6x_0x40_0x79_48.py
        iconic  ...ezFBfont_open_iconic_other_6x_0x40_0x79_48.py
        iconic  ...ezFBfont_open_iconic_arrow_6x_0x40_0x79_48.py
        iconic  .....ezFBfont_open_iconic_all_6x_0x40_0x79_48.py
        iconic  .....ezFBfont_open_iconic_www_6x_0x40_0x79_48.py
        iconic  ....ezFBfont_open_iconic_mime_6x_0x40_0x79_48.py
        iconic  ....ezFBfont_open_iconic_play_6x_0x40_0x79_48.py
        iconic  ezFBfont_open_iconic_embedded_6x_0x40_0x79_48.py
        iconic  ....ezFBfont_open_iconic_text_6x_0x40_0x79_48.py
        iconic  .....ezFBfont_open_iconic_gui_6x_0x40_0x79_48.py
        iconic  ...ezFBfont_open_iconic_human_6x_0x40_0x79_48.py
        iconic  ...ezFBfont_open_iconic_thing_6x_0x40_0x79_48.py
        iconic  .....ezFBfont_open_iconic_app_6x_0x40_0x79_48.py
   64px:
        iconic  .ezFBfont_open_iconic_weather_8x_0x40_0x79_64.py
        iconic  ...ezFBfont_open_iconic_other_8x_0x40_0x79_64.py
        iconic  .....ezFBfont_open_iconic_gui_8x_0x40_0x79_64.py
        iconic  .....ezFBfont_open_iconic_app_8x_0x40_0x79_64.py
        iconic  ...ezFBfont_open_iconic_human_8x_0x40_0x79_64.py
        iconic  ....ezFBfont_open_iconic_play_8x_0x40_0x79_64.py
        iconic  .....ezFBfont_open_iconic_all_8x_0x40_0x79_64.py
        iconic  ...ezFBfont_open_iconic_check_8x_0x40_0x79_64.py
        iconic  ....ezFBfont_open_iconic_text_8x_0x40_0x79_64.py
        iconic  ezFBfont_open_iconic_embedded_8x_0x40_0x79_64.py
        iconic  .....ezFBfont_open_iconic_www_8x_0x40_0x79_64.py
        iconic  ...ezFBfont_open_iconic_arrow_8x_0x40_0x79_64.py
        iconic  ...ezFBfont_open_iconic_thing_8x_0x40_0x79_64.py
        iconic  ...ezFBfont_open_iconic_email_8x_0x40_0x79_64.py
        iconic  ....ezFBfont_open_iconic_mime_8x_0x40_0x79_64.py

Mid (0x80 - 0xbf) character set
-------------------------------
Size:   Family                                              Name
    8px:
        iconic  .....ezFBfont_open_iconic_all_1x_0x80_0xBF_08.py
   15px:
        symbol  .................ezFBfont_symb08_0x80_0xBF_15.py
        symbol  .................ezFBfont_symb10_0x80_0xBF_15.py
   16px:
        iconic  .....ezFBfont_open_iconic_all_2x_0x80_0xBF_16.py
   17px:
        symbol  .................ezFBfont_symb12_0x80_0xBF_17.py
   19px:
        symbol  .................ezFBfont_symb14_0x80_0xBF_19.py
   24px:
        symbol  .................ezFBfont_symb18_0x80_0xBF_24.py
   25px:
       generic  .................ezFBfont_cursor_0x80_0xBF_25.py
   32px:
        iconic  .....ezFBfont_open_iconic_all_4x_0x80_0xBF_32.py
   34px:
        symbol  .................ezFBfont_symb24_0x80_0xBF_34.py
   48px:
        iconic  .....ezFBfont_open_iconic_all_6x_0x80_0xBF_48.py
   64px:
        iconic  .....ezFBfont_open_iconic_all_8x_0x80_0xBF_64.py

Upper (0xc0 - 0xff) character set
---------------------------------
Size:   Family                                              Name
    8px:
        iconic  .....ezFBfont_open_iconic_all_1x_0xC0_0xFF_08.py
   15px:
        symbol  .................ezFBfont_symb08_0xC0_0xFF_15.py
        symbol  .................ezFBfont_symb10_0xC0_0xFF_15.py
   16px:
        iconic  .....ezFBfont_open_iconic_all_2x_0xC0_0xFF_16.py
   17px:
        symbol  .................ezFBfont_symb12_0xC0_0xFF_17.py
   19px:
        symbol  .................ezFBfont_symb14_0xC0_0xFF_19.py
   24px:
        symbol  .................ezFBfont_symb18_0xC0_0xFF_24.py
   32px:
        iconic  .....ezFBfont_open_iconic_all_4x_0xC0_0xFF_32.py
   34px:
        symbol  .................ezFBfont_symb24_0xC0_0xFF_34.py
   48px:
        iconic  .....ezFBfont_open_iconic_all_6x_0xC0_0xFF_48.py
   64px:
        iconic  .....ezFBfont_open_iconic_all_8x_0xC0_0xFF_64.py

Extended (0x100 - 0x1ff) character set
--------------------------------------
Size:   Family                                              Name
    8px:
        iconic  ...ezFBfont_open_iconic_all_1x_0x100_0x1FF_08.py
   16px:
        iconic  ...ezFBfont_open_iconic_all_2x_0x100_0x1FF_16.py
   32px:
        iconic  ...ezFBfont_open_iconic_all_4x_0x100_0x1FF_32.py
   48px:
        iconic  ...ezFBfont_open_iconic_all_6x_0x100_0x1FF_48.py
   64px:
        iconic  ...ezFBfont_open_iconic_all_8x_0x100_0x1FF_64.py

Full (0x00 - 0xfff) character set
---------------------------------
Size:   Family                                              Name
    8px:
        iconic  .....ezFBfont_open_iconic_all_1x_0x0_0xFFF_08.py
   15px:
        symbol  .................ezFBfont_symb08_0x0_0xFFF_15.py
   16px:
        iconic  .....ezFBfont_open_iconic_all_2x_0x0_0xFFF_16.py
   17px:
        symbol  .................ezFBfont_symb12_0x0_0xFFF_17.py
   19px:
        symbol  .................ezFBfont_symb14_0x0_0xFFF_19.py
   23px:
       generic  ................ezFBfont_cursorr_0x0_0xFFF_23.py
   24px:
       generic  ..............ezFBfont_battery24_0x0_0xFFF_24.py
        symbol  .................ezFBfont_symb18_0x0_0xFFF_24.py
   31px:
       generic  .................ezFBfont_cursor_0x0_0xFFF_31.py
   32px:
        iconic  .....ezFBfont_open_iconic_all_4x_0x0_0xFFF_32.py
   34px:
        symbol  .................ezFBfont_symb24_0x0_0xFFF_34.py
   48px:
        iconic  .....ezFBfont_open_iconic_all_6x_0x0_0xFFF_48.py
   64px:
        iconic  .....ezFBfont_open_iconic_all_8x_0x0_0xFFF_64.py
```
---------------------
## Converter script
The font structure is created by the 'build-sets.py' script in the `bdf2dict` folder, see the README there for more.

The `sets.py` file in this folder contains the character definitions and font source.
