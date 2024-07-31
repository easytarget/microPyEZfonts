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

Sets will only be genereated when *unique*; if a previous set for the font already contains an identical charset the current set will be skipped.
* Pay attention to the file sizes; the full sets (especially the '`latin`' set) can get large.
* For a detailed font file description and preview look at the corresponding `.map` file in the 'maps' sub-folder.
  * This contains an ascii-art glyph for all characters in the font file; showing the name, size, bitmap and baseline.

Only 'Basic Latin' and 'Latin Supplemental' characters are covered by these sets. If you want Latin characters from the Unicode 'Latin Extended ..' or 'IPA Extensions' blocks you will need to generate them using the tools in the [Unicode](/Unicode) folder.

For usage see the `ezFBfont.py` documentation in the main `README`.

# The list

Fonts as of 18 Jun 2024 organised by charset/height/family.

```
Micropython font module tree for: Latin-1

Time character set
------------------
Size:       Family                                       Name
    5px:
           generic  ................ezFBfont_micro_time_05.py
           generic  ...........ezFBfont_font_tiny5_time_05.py
             fixed  ..................ezFBfont_4x6_time_05.py
             fixed  ............ezFBfont_tom_thumb_time_05.py
    6px:
             fixed  ..................ezFBfont_5x7_time_06.py
             fixed  ..................ezFBfont_6x9_time_06.py
            spleen  ...........ezFBfont_spleen_5x8_time_06.py
    7px:
             fixed  .................ezFBfont_6x12_time_07.py
             fixed  ..................ezFBfont_5x8_time_07.py
           courier  ..............ezFBfont_courB08_time_07.py
           courier  ..............ezFBfont_courR08_time_07.py
             times  ...............ezFBfont_timR08_time_07.py
             times  ...............ezFBfont_timB08_time_07.py
    8px:
             fixed  .................ezFBfont_6x10_time_08.py
       amstrad-cpc  .ezFBfont_amstrad_cpc_extended_time_08.py
         helvetica  ..............ezFBfont_helvR08_time_08.py
         helvetica  ..............ezFBfont_helvB08_time_08.py
         helvetica  ..........ezFBfont_helvB08_gps_time_08.py
        schoolbook  ..............ezFBfont_ncenR08_time_08.py
        schoolbook  ..............ezFBfont_ncenB08_time_08.py
            spleen  ..........ezFBfont_spleen_6x12_time_08.py
   10px:
             fixed  ................ezFBfont_6x13O_time_10.py
             fixed  .................ezFBfont_6x13_time_10.py
             fixed  ................ezFBfont_7x13B_time_10.py
             fixed  ................ezFBfont_6x13B_time_10.py
             fixed  ................ezFBfont_7x13O_time_10.py
             fixed  .................ezFBfont_8x13_time_10.py
             fixed  ................ezFBfont_8x13O_time_10.py
             fixed  .................ezFBfont_9x18_time_10.py
             fixed  ................ezFBfont_7x14B_time_10.py
             fixed  ................ezFBfont_8x13B_time_10.py
             fixed  .................ezFBfont_9x15_time_10.py
             fixed  .................ezFBfont_7x13_time_10.py
             fixed  ................ezFBfont_9x18B_time_10.py
           courier  ..............ezFBfont_courB10_time_10.py
           courier  ..............ezFBfont_courR10_time_10.py
             times  ...............ezFBfont_timB10_time_10.py
             times  ...............ezFBfont_timR10_time_10.py
            spleen  ..........ezFBfont_spleen_8x16_time_10.py
   11px:
             fixed  .................ezFBfont_7x14_time_11.py
             fixed  ................ezFBfont_9x15B_time_11.py
           courier  ..............ezFBfont_courB12_time_11.py
           courier  ..............ezFBfont_courR12_time_11.py
             times  ...............ezFBfont_timR12_time_11.py
             times  ...............ezFBfont_timB12_time_11.py
         helvetica  ..............ezFBfont_helvB10_time_11.py
         helvetica  ..............ezFBfont_helvR10_time_11.py
        schoolbook  ..............ezFBfont_ncenR10_time_11.py
        schoolbook  ..............ezFBfont_ncenB10_time_11.py
   12px:
           courier  ..............ezFBfont_courB14_time_12.py
           courier  ..............ezFBfont_courR14_time_12.py
         helvetica  ..............ezFBfont_helvR12_time_12.py
         helvetica  ..............ezFBfont_helvB12_time_12.py
        schoolbook  ..............ezFBfont_ncenB12_time_12.py
        schoolbook  ..............ezFBfont_ncenR12_time_12.py
   13px:
             fixed  ................ezFBfont_10x20_time_13.py
             times  ...............ezFBfont_timB14_time_13.py
             times  ...............ezFBfont_timR14_time_13.py
         helvetica  ..............ezFBfont_helvB14_time_13.py
         helvetica  ..............ezFBfont_helvR14_time_13.py
   14px:
        schoolbook  ..............ezFBfont_ncenB14_time_14.py
        schoolbook  ..............ezFBfont_ncenR14_time_14.py
   15px:
           courier  ..............ezFBfont_courR18_time_15.py
            spleen  .........ezFBfont_spleen_12x24_time_15.py
   16px:
           courier  ..............ezFBfont_courB18_time_16.py
   17px:
             times  ...............ezFBfont_timR18_time_17.py
             times  ...............ezFBfont_timB18_time_17.py
   18px:
         helvetica  ..............ezFBfont_helvR18_time_18.py
         helvetica  ..............ezFBfont_helvB18_time_18.py
        schoolbook  ..............ezFBfont_ncenR18_time_18.py
        schoolbook  ..............ezFBfont_ncenB18_time_18.py
   20px:
           courier  ..............ezFBfont_courR24_time_20.py
            spleen  .........ezFBfont_spleen_16x32_time_20.py
   21px:
           courier  ..............ezFBfont_courB24_time_21.py
   23px:
             times  ...............ezFBfont_timB24_time_23.py
             times  ...............ezFBfont_timR24_time_23.py
   24px:
         helvetica  ..............ezFBfont_helvR24_time_24.py
         helvetica  ..............ezFBfont_helvB24_time_24.py
        schoolbook  ..............ezFBfont_ncenB24_time_24.py
   25px:
        schoolbook  ..............ezFBfont_ncenR24_time_25.py
   40px:
            spleen  .........ezFBfont_spleen_32x64_time_40.py

Numeric character set
---------------------
Size:       Family                                       Name
    5px:
           generic  .................ezFBfont_micro_num_05.py
             fixed  .............ezFBfont_tom_thumb_num_05.py
    6px:
           generic  ............ezFBfont_font_tiny5_num_06.py
             fixed  ...................ezFBfont_4x6_num_06.py
    7px:
             fixed  ...................ezFBfont_5x8_num_07.py
             fixed  ...................ezFBfont_5x7_num_07.py
    8px:
             fixed  ..................ezFBfont_6x10_num_08.py
       amstrad-cpc  ..ezFBfont_amstrad_cpc_extended_num_08.py
            spleen  ............ezFBfont_spleen_5x8_num_08.py
    9px:
             fixed  ...................ezFBfont_6x9_num_09.py
           courier  ...............ezFBfont_courB08_num_09.py
             times  ................ezFBfont_timR08_num_09.py
   10px:
             fixed  ..................ezFBfont_7x13_num_10.py
             fixed  ..................ezFBfont_6x12_num_10.py
             fixed  ..................ezFBfont_8x13_num_10.py
             fixed  .................ezFBfont_7x13O_num_10.py
             fixed  .................ezFBfont_7x13B_num_10.py
             fixed  .................ezFBfont_8x13O_num_10.py
           courier  ...............ezFBfont_courR08_num_10.py
             times  ................ezFBfont_timB08_num_10.py
         helvetica  ...........ezFBfont_helvB08_gps_num_10.py
         helvetica  ...............ezFBfont_helvR08_num_10.py
         helvetica  ...............ezFBfont_helvB08_num_10.py
        schoolbook  ...............ezFBfont_ncenB08_num_10.py
        schoolbook  ...............ezFBfont_ncenR08_num_10.py
            spleen  ...........ezFBfont_spleen_6x12_num_10.py
   11px:
             fixed  ..................ezFBfont_6x13_num_11.py
             fixed  .................ezFBfont_6x13B_num_11.py
             fixed  .................ezFBfont_6x13O_num_11.py
             fixed  .................ezFBfont_8x13B_num_11.py
   12px:
           courier  ...............ezFBfont_courB10_num_12.py
           courier  ...............ezFBfont_courR10_num_12.py
            spleen  ...........ezFBfont_spleen_8x16_num_12.py
   13px:
             fixed  ..................ezFBfont_9x18_num_13.py
             fixed  ..................ezFBfont_7x14_num_13.py
             fixed  .................ezFBfont_7x14B_num_13.py
           courier  ...............ezFBfont_courR12_num_13.py
             times  ................ezFBfont_timB10_num_13.py
             times  ................ezFBfont_timR10_num_13.py
        schoolbook  ...............ezFBfont_ncenR10_num_13.py
        schoolbook  ...............ezFBfont_ncenB10_num_13.py
   14px:
             fixed  .................ezFBfont_9x18B_num_14.py
             fixed  ..................ezFBfont_9x15_num_14.py
             fixed  .................ezFBfont_9x15B_num_14.py
             fixed  .................ezFBfont_10x20_num_14.py
             times  ................ezFBfont_timR12_num_14.py
         helvetica  ...............ezFBfont_helvR10_num_14.py
         helvetica  ...............ezFBfont_helvB10_num_14.py
   15px:
           courier  ...............ezFBfont_courB12_num_15.py
             times  ................ezFBfont_timB12_num_15.py
         helvetica  ...............ezFBfont_helvB12_num_15.py
        schoolbook  ...............ezFBfont_ncenB12_num_15.py
        schoolbook  ...............ezFBfont_ncenR12_num_15.py
   16px:
           courier  ...............ezFBfont_courR14_num_16.py
           courier  ...............ezFBfont_courB14_num_16.py
         helvetica  ...............ezFBfont_helvR12_num_16.py
   17px:
             times  ................ezFBfont_timB14_num_17.py
             times  ................ezFBfont_timR14_num_17.py
        schoolbook  ...............ezFBfont_ncenR14_num_17.py
        schoolbook  ...............ezFBfont_ncenB14_num_17.py
   18px:
         helvetica  ...............ezFBfont_helvB14_num_18.py
         helvetica  ...............ezFBfont_helvR14_num_18.py
   19px:
           courier  ...............ezFBfont_courR18_num_19.py
   20px:
            spleen  ..........ezFBfont_spleen_12x24_num_20.py
   21px:
           courier  ...............ezFBfont_courB18_num_21.py
   22px:
             times  ................ezFBfont_timB18_num_22.py
             times  ................ezFBfont_timR18_num_22.py
        schoolbook  ...............ezFBfont_ncenR18_num_22.py
        schoolbook  ...............ezFBfont_ncenB18_num_22.py
   24px:
         helvetica  ...............ezFBfont_helvB18_num_24.py
         helvetica  ...............ezFBfont_helvR18_num_24.py
   26px:
           courier  ...............ezFBfont_courR24_num_26.py
            spleen  ..........ezFBfont_spleen_16x32_num_26.py
   28px:
           courier  ...............ezFBfont_courB24_num_28.py
             times  ................ezFBfont_timR24_num_28.py
   30px:
        schoolbook  ...............ezFBfont_ncenB24_num_30.py
   31px:
             times  ................ezFBfont_timB24_num_31.py
         helvetica  ...............ezFBfont_helvB24_num_31.py
        schoolbook  ...............ezFBfont_ncenR24_num_31.py
   33px:
         helvetica  ...............ezFBfont_helvR24_num_33.py
   56px:
            spleen  ..........ezFBfont_spleen_32x64_num_56.py

Uppercase character set
-----------------------
Size:       Family                                       Name
    5px:
           generic  ...............ezFBfont_micro_upper_05.py
             fixed  ...........ezFBfont_tom_thumb_upper_05.py
    6px:
           generic  ..........ezFBfont_font_tiny5_upper_06.py
             fixed  .................ezFBfont_4x6_upper_06.py
    7px:
             fixed  .................ezFBfont_5x7_upper_07.py
    8px:
             fixed  ................ezFBfont_6x10_upper_08.py
             fixed  .................ezFBfont_5x8_upper_08.py
       amstrad-cpc  ezFBfont_amstrad_cpc_extended_upper_08.py
            spleen  ..........ezFBfont_spleen_5x8_upper_08.py
    9px:
             fixed  .................ezFBfont_6x9_upper_09.py
   10px:
             fixed  ...............ezFBfont_8x13O_upper_10.py
             fixed  ................ezFBfont_6x12_upper_10.py
             fixed  ................ezFBfont_8x13_upper_10.py
             fixed  ...............ezFBfont_7x13B_upper_10.py
           courier  .............ezFBfont_courB08_upper_10.py
           courier  .............ezFBfont_courR08_upper_10.py
            spleen  .........ezFBfont_spleen_6x12_upper_10.py
   11px:
             fixed  ...............ezFBfont_7x13O_upper_11.py
             fixed  ................ezFBfont_7x13_upper_11.py
             fixed  ...............ezFBfont_6x13O_upper_11.py
             fixed  ...............ezFBfont_6x13B_upper_11.py
             fixed  ...............ezFBfont_8x13B_upper_11.py
             fixed  ................ezFBfont_6x13_upper_11.py
             times  ..............ezFBfont_timB08_upper_11.py
             times  ..............ezFBfont_timR08_upper_11.py
         helvetica  .............ezFBfont_helvB08_upper_11.py
         helvetica  .........ezFBfont_helvB08_gps_upper_11.py
         helvetica  .............ezFBfont_helvR08_upper_11.py
        schoolbook  .............ezFBfont_ncenB08_upper_11.py
        schoolbook  .............ezFBfont_ncenR08_upper_11.py
   13px:
             fixed  ................ezFBfont_7x14_upper_13.py
             fixed  ................ezFBfont_9x18_upper_13.py
             fixed  ...............ezFBfont_9x18B_upper_13.py
           courier  .............ezFBfont_courB10_upper_13.py
   14px:
             fixed  ...............ezFBfont_9x15B_upper_14.py
             fixed  ...............ezFBfont_10x20_upper_14.py
             fixed  ................ezFBfont_9x15_upper_14.py
             fixed  ...............ezFBfont_7x14B_upper_14.py
           courier  .............ezFBfont_courR10_upper_14.py
             times  ..............ezFBfont_timB10_upper_14.py
             times  ..............ezFBfont_timR10_upper_14.py
        schoolbook  .............ezFBfont_ncenR10_upper_14.py
            spleen  .........ezFBfont_spleen_8x16_upper_14.py
   15px:
           courier  .............ezFBfont_courR12_upper_15.py
           courier  .............ezFBfont_courB12_upper_15.py
             times  ..............ezFBfont_timR12_upper_15.py
         helvetica  .............ezFBfont_helvR10_upper_15.py
         helvetica  .............ezFBfont_helvB10_upper_15.py
        schoolbook  .............ezFBfont_ncenB10_upper_15.py
   16px:
             times  ..............ezFBfont_timB12_upper_16.py
         helvetica  .............ezFBfont_helvB12_upper_16.py
        schoolbook  .............ezFBfont_ncenR12_upper_16.py
   17px:
           courier  .............ezFBfont_courR14_upper_17.py
           courier  .............ezFBfont_courB14_upper_17.py
         helvetica  .............ezFBfont_helvR12_upper_17.py
        schoolbook  .............ezFBfont_ncenB12_upper_17.py
   18px:
             times  ..............ezFBfont_timR14_upper_18.py
             times  ..............ezFBfont_timB14_upper_18.py
         helvetica  .............ezFBfont_helvB14_upper_18.py
         helvetica  .............ezFBfont_helvR14_upper_18.py
   19px:
        schoolbook  .............ezFBfont_ncenR14_upper_19.py
   20px:
        schoolbook  .............ezFBfont_ncenB14_upper_20.py
   21px:
           courier  .............ezFBfont_courB18_upper_21.py
   22px:
           courier  .............ezFBfont_courR18_upper_22.py
            spleen  ........ezFBfont_spleen_12x24_upper_22.py
   23px:
             times  ..............ezFBfont_timB18_upper_23.py
   24px:
             times  ..............ezFBfont_timR18_upper_24.py
         helvetica  .............ezFBfont_helvB18_upper_24.py
        schoolbook  .............ezFBfont_ncenR18_upper_24.py
   25px:
         helvetica  .............ezFBfont_helvR18_upper_25.py
        schoolbook  .............ezFBfont_ncenB18_upper_25.py
   28px:
           courier  .............ezFBfont_courR24_upper_28.py
            spleen  ........ezFBfont_spleen_16x32_upper_28.py
   30px:
           courier  .............ezFBfont_courB24_upper_30.py
   31px:
             times  ..............ezFBfont_timR24_upper_31.py
         helvetica  .............ezFBfont_helvB24_upper_31.py
   32px:
             times  ..............ezFBfont_timB24_upper_32.py
        schoolbook  .............ezFBfont_ncenB24_upper_32.py
   33px:
        schoolbook  .............ezFBfont_ncenR24_upper_33.py
   34px:
         helvetica  .............ezFBfont_helvR24_upper_34.py
   56px:
            spleen  ........ezFBfont_spleen_32x64_upper_56.py

Ascii character set
-------------------
Size:       Family                                       Name
    5px:
           generic  ...............ezFBfont_micro_ascii_05.py
    6px:
             fixed  .................ezFBfont_4x6_ascii_06.py
             fixed  ...........ezFBfont_tom_thumb_ascii_06.py
    7px:
           generic  ..........ezFBfont_font_tiny5_ascii_07.py
             fixed  .................ezFBfont_5x7_ascii_07.py
    8px:
             fixed  .................ezFBfont_5x8_ascii_08.py
       amstrad-cpc  ezFBfont_amstrad_cpc_extended_ascii_08.py
            spleen  ..........ezFBfont_spleen_5x8_ascii_08.py
    9px:
             fixed  .................ezFBfont_6x9_ascii_09.py
   10px:
             fixed  ................ezFBfont_6x12_ascii_10.py
             fixed  ................ezFBfont_6x10_ascii_10.py
           courier  .............ezFBfont_courB08_ascii_10.py
           courier  .............ezFBfont_courR08_ascii_10.py
   11px:
             times  ..............ezFBfont_timR08_ascii_11.py
             times  ..............ezFBfont_timB08_ascii_11.py
         helvetica  .............ezFBfont_helvR08_ascii_11.py
         helvetica  .............ezFBfont_helvB08_ascii_11.py
         helvetica  .........ezFBfont_helvB08_gps_ascii_11.py
        schoolbook  .............ezFBfont_ncenB08_ascii_11.py
        schoolbook  .............ezFBfont_ncenR08_ascii_11.py
   12px:
             fixed  ...............ezFBfont_6x13O_ascii_12.py
             fixed  ...............ezFBfont_8x13O_ascii_12.py
             fixed  ...............ezFBfont_6x13B_ascii_12.py
             fixed  ................ezFBfont_8x13_ascii_12.py
             fixed  ................ezFBfont_6x13_ascii_12.py
             fixed  ...............ezFBfont_7x13B_ascii_12.py
             fixed  ...............ezFBfont_8x13B_ascii_12.py
             fixed  ...............ezFBfont_7x13O_ascii_12.py
             fixed  ................ezFBfont_7x13_ascii_12.py
            spleen  .........ezFBfont_spleen_6x12_ascii_12.py
   13px:
             fixed  ................ezFBfont_7x14_ascii_13.py
   14px:
             fixed  ................ezFBfont_9x15_ascii_14.py
             fixed  ...............ezFBfont_9x15B_ascii_14.py
             fixed  ...............ezFBfont_7x14B_ascii_14.py
           courier  .............ezFBfont_courB10_ascii_14.py
           courier  .............ezFBfont_courR10_ascii_14.py
             times  ..............ezFBfont_timR10_ascii_14.py
             times  ..............ezFBfont_timB10_ascii_14.py
            spleen  .........ezFBfont_spleen_8x16_ascii_14.py
   15px:
           courier  .............ezFBfont_courB12_ascii_15.py
           courier  .............ezFBfont_courR12_ascii_15.py
         helvetica  .............ezFBfont_helvR10_ascii_15.py
         helvetica  .............ezFBfont_helvB10_ascii_15.py
        schoolbook  .............ezFBfont_ncenB10_ascii_15.py
        schoolbook  .............ezFBfont_ncenR10_ascii_15.py
   16px:
             fixed  ................ezFBfont_9x18_ascii_16.py
             fixed  ...............ezFBfont_9x18B_ascii_16.py
             times  ..............ezFBfont_timR12_ascii_16.py
             times  ..............ezFBfont_timB12_ascii_16.py
        schoolbook  .............ezFBfont_ncenR12_ascii_16.py
   17px:
             fixed  ...............ezFBfont_10x20_ascii_17.py
           courier  .............ezFBfont_courB14_ascii_17.py
           courier  .............ezFBfont_courR14_ascii_17.py
         helvetica  .............ezFBfont_helvB12_ascii_17.py
         helvetica  .............ezFBfont_helvR12_ascii_17.py
        schoolbook  .............ezFBfont_ncenB12_ascii_17.py
   18px:
             times  ..............ezFBfont_timR14_ascii_18.py
             times  ..............ezFBfont_timB14_ascii_18.py
         helvetica  .............ezFBfont_helvR14_ascii_18.py
         helvetica  .............ezFBfont_helvB14_ascii_18.py
   19px:
        schoolbook  .............ezFBfont_ncenR14_ascii_19.py
   20px:
        schoolbook  .............ezFBfont_ncenB14_ascii_20.py
   22px:
           courier  .............ezFBfont_courB18_ascii_22.py
           courier  .............ezFBfont_courR18_ascii_22.py
   23px:
             times  ..............ezFBfont_timB18_ascii_23.py
            spleen  ........ezFBfont_spleen_12x24_ascii_23.py
   24px:
         helvetica  .............ezFBfont_helvB18_ascii_24.py
   25px:
             times  ..............ezFBfont_timR18_ascii_25.py
         helvetica  .............ezFBfont_helvR18_ascii_25.py
        schoolbook  .............ezFBfont_ncenR18_ascii_25.py
        schoolbook  .............ezFBfont_ncenB18_ascii_25.py
   28px:
           courier  .............ezFBfont_courR24_ascii_28.py
   30px:
           courier  .............ezFBfont_courB24_ascii_30.py
            spleen  ........ezFBfont_spleen_16x32_ascii_30.py
   32px:
             times  ..............ezFBfont_timR24_ascii_32.py
         helvetica  .............ezFBfont_helvB24_ascii_32.py
   33px:
             times  ..............ezFBfont_timB24_ascii_33.py
        schoolbook  .............ezFBfont_ncenB24_ascii_33.py
   34px:
         helvetica  .............ezFBfont_helvR24_ascii_34.py
        schoolbook  .............ezFBfont_ncenR24_ascii_34.py
   60px:
            spleen  ........ezFBfont_spleen_32x64_ascii_60.py

Supplemental character set
--------------------------
Size:       Family                                       Name
    1px:
            spleen  ...........ezFBfont_spleen_5x8_supp_01.py
    6px:
             fixed  ..................ezFBfont_4x6_supp_06.py
             fixed  ............ezFBfont_tom_thumb_supp_06.py
    7px:
           generic  ...........ezFBfont_font_tiny5_supp_07.py
             fixed  ..................ezFBfont_5x7_supp_07.py
    8px:
             fixed  ..................ezFBfont_5x8_supp_08.py
       amstrad-cpc  .ezFBfont_amstrad_cpc_extended_supp_08.py
    9px:
             fixed  ..................ezFBfont_6x9_supp_09.py
   10px:
             fixed  .................ezFBfont_6x10_supp_10.py
   11px:
           courier  ..............ezFBfont_courB08_supp_11.py
           courier  ..............ezFBfont_courR08_supp_11.py
   12px:
             fixed  ................ezFBfont_7x13O_supp_12.py
             fixed  ................ezFBfont_6x13B_supp_12.py
             fixed  ................ezFBfont_8x13O_supp_12.py
             fixed  .................ezFBfont_6x13_supp_12.py
             fixed  .................ezFBfont_8x13_supp_12.py
             fixed  ................ezFBfont_6x13O_supp_12.py
             fixed  .................ezFBfont_7x13_supp_12.py
             fixed  .................ezFBfont_6x12_supp_12.py
             fixed  ................ezFBfont_7x13B_supp_12.py
            spleen  ..........ezFBfont_spleen_6x12_supp_12.py
   13px:
             fixed  ................ezFBfont_8x13B_supp_13.py
             times  ...............ezFBfont_timB08_supp_13.py
             times  ...............ezFBfont_timR08_supp_13.py
         helvetica  ..............ezFBfont_helvB08_supp_13.py
         helvetica  ..............ezFBfont_helvR08_supp_13.py
        schoolbook  ..............ezFBfont_ncenR08_supp_13.py
        schoolbook  ..............ezFBfont_ncenB08_supp_13.py
   14px:
             fixed  .................ezFBfont_7x14_supp_14.py
             fixed  ................ezFBfont_7x14B_supp_14.py
   15px:
             fixed  .................ezFBfont_9x15_supp_15.py
             fixed  ................ezFBfont_9x15B_supp_15.py
           courier  ..............ezFBfont_courR10_supp_15.py
            spleen  ..........ezFBfont_spleen_8x16_supp_15.py
   16px:
           courier  ..............ezFBfont_courB10_supp_16.py
   17px:
             fixed  .................ezFBfont_9x18_supp_17.py
           courier  ..............ezFBfont_courR12_supp_17.py
           courier  ..............ezFBfont_courB12_supp_17.py
             times  ...............ezFBfont_timR10_supp_17.py
             times  ...............ezFBfont_timB10_supp_17.py
         helvetica  ..............ezFBfont_helvR10_supp_17.py
         helvetica  ..............ezFBfont_helvB10_supp_17.py
        schoolbook  ..............ezFBfont_ncenR10_supp_17.py
   18px:
             fixed  ................ezFBfont_9x18B_supp_18.py
        schoolbook  ..............ezFBfont_ncenB10_supp_18.py
   19px:
           courier  ..............ezFBfont_courR14_supp_19.py
             times  ...............ezFBfont_timR12_supp_19.py
        schoolbook  ..............ezFBfont_ncenR12_supp_19.py
        schoolbook  ..............ezFBfont_ncenB12_supp_19.py
   20px:
             fixed  ................ezFBfont_10x20_supp_20.py
           courier  ..............ezFBfont_courB14_supp_20.py
             times  ...............ezFBfont_timB12_supp_20.py
         helvetica  ..............ezFBfont_helvR12_supp_20.py
         helvetica  ..............ezFBfont_helvB12_supp_20.py
   21px:
             times  ...............ezFBfont_timB14_supp_21.py
   22px:
             times  ...............ezFBfont_timR14_supp_22.py
         helvetica  ..............ezFBfont_helvR14_supp_22.py
   23px:
         helvetica  ..............ezFBfont_helvB14_supp_23.py
        schoolbook  ..............ezFBfont_ncenR14_supp_23.py
        schoolbook  ..............ezFBfont_ncenB14_supp_23.py
   24px:
           courier  ..............ezFBfont_courR18_supp_24.py
            spleen  .........ezFBfont_spleen_12x24_supp_24.py
   26px:
           courier  ..............ezFBfont_courB18_supp_26.py
   29px:
             times  ...............ezFBfont_timR18_supp_29.py
             times  ...............ezFBfont_timB18_supp_29.py
         helvetica  ..............ezFBfont_helvB18_supp_29.py
         helvetica  ..............ezFBfont_helvR18_supp_29.py
        schoolbook  ..............ezFBfont_ncenB18_supp_29.py
        schoolbook  ..............ezFBfont_ncenR18_supp_29.py
   32px:
           courier  ..............ezFBfont_courR24_supp_32.py
            spleen  .........ezFBfont_spleen_16x32_supp_32.py
   33px:
           courier  ..............ezFBfont_courB24_supp_33.py
   37px:
             times  ...............ezFBfont_timB24_supp_37.py
             times  ...............ezFBfont_timR24_supp_37.py
   38px:
         helvetica  ..............ezFBfont_helvR24_supp_38.py
         helvetica  ..............ezFBfont_helvB24_supp_38.py
   39px:
        schoolbook  ..............ezFBfont_ncenR24_supp_39.py
   40px:
        schoolbook  ..............ezFBfont_ncenB24_supp_40.py
   64px:
            spleen  .........ezFBfont_spleen_32x64_supp_64.py

Latin-1 character set
---------------------
Size:       Family                                       Name
    6px:
             fixed  .................ezFBfont_4x6_latin_06.py
             fixed  ...........ezFBfont_tom_thumb_latin_06.py
    7px:
           generic  ..........ezFBfont_font_tiny5_latin_07.py
             fixed  .................ezFBfont_5x7_latin_07.py
    8px:
             fixed  .................ezFBfont_5x8_latin_08.py
       amstrad-cpc  ezFBfont_amstrad_cpc_extended_latin_08.py
            spleen  ..........ezFBfont_spleen_5x8_latin_08.py
    9px:
             fixed  .................ezFBfont_6x9_latin_09.py
   10px:
             fixed  ................ezFBfont_6x10_latin_10.py
   11px:
           courier  .............ezFBfont_courB08_latin_11.py
           courier  .............ezFBfont_courR08_latin_11.py
   12px:
             fixed  ................ezFBfont_7x13_latin_12.py
             fixed  ................ezFBfont_6x12_latin_12.py
             fixed  ...............ezFBfont_8x13O_latin_12.py
             fixed  ...............ezFBfont_7x13O_latin_12.py
             fixed  ................ezFBfont_8x13_latin_12.py
             fixed  ...............ezFBfont_7x13B_latin_12.py
             fixed  ................ezFBfont_6x13_latin_12.py
             fixed  ...............ezFBfont_6x13B_latin_12.py
             fixed  ...............ezFBfont_6x13O_latin_12.py
            spleen  .........ezFBfont_spleen_6x12_latin_12.py
   13px:
             fixed  ...............ezFBfont_8x13B_latin_13.py
             times  ..............ezFBfont_timB08_latin_13.py
             times  ..............ezFBfont_timR08_latin_13.py
         helvetica  .............ezFBfont_helvR08_latin_13.py
         helvetica  .............ezFBfont_helvB08_latin_13.py
        schoolbook  .............ezFBfont_ncenB08_latin_13.py
        schoolbook  .............ezFBfont_ncenR08_latin_13.py
   14px:
             fixed  ...............ezFBfont_7x14B_latin_14.py
             fixed  ................ezFBfont_7x14_latin_14.py
   15px:
             fixed  ...............ezFBfont_9x15B_latin_15.py
             fixed  ................ezFBfont_9x15_latin_15.py
           courier  .............ezFBfont_courR10_latin_15.py
            spleen  .........ezFBfont_spleen_8x16_latin_15.py
   16px:
           courier  .............ezFBfont_courB10_latin_16.py
   17px:
             fixed  ................ezFBfont_9x18_latin_17.py
           courier  .............ezFBfont_courB12_latin_17.py
           courier  .............ezFBfont_courR12_latin_17.py
             times  ..............ezFBfont_timR10_latin_17.py
             times  ..............ezFBfont_timB10_latin_17.py
         helvetica  .............ezFBfont_helvR10_latin_17.py
         helvetica  .............ezFBfont_helvB10_latin_17.py
        schoolbook  .............ezFBfont_ncenR10_latin_17.py
   18px:
             fixed  ...............ezFBfont_9x18B_latin_18.py
        schoolbook  .............ezFBfont_ncenB10_latin_18.py
   19px:
           courier  .............ezFBfont_courR14_latin_19.py
             times  ..............ezFBfont_timR12_latin_19.py
        schoolbook  .............ezFBfont_ncenR12_latin_19.py
        schoolbook  .............ezFBfont_ncenB12_latin_19.py
   20px:
             fixed  ...............ezFBfont_10x20_latin_20.py
           courier  .............ezFBfont_courB14_latin_20.py
             times  ..............ezFBfont_timB12_latin_20.py
         helvetica  .............ezFBfont_helvR12_latin_20.py
         helvetica  .............ezFBfont_helvB12_latin_20.py
   21px:
             times  ..............ezFBfont_timB14_latin_21.py
   22px:
             times  ..............ezFBfont_timR14_latin_22.py
         helvetica  .............ezFBfont_helvR14_latin_22.py
   23px:
         helvetica  .............ezFBfont_helvB14_latin_23.py
        schoolbook  .............ezFBfont_ncenR14_latin_23.py
        schoolbook  .............ezFBfont_ncenB14_latin_23.py
   24px:
           courier  .............ezFBfont_courR18_latin_24.py
            spleen  ........ezFBfont_spleen_12x24_latin_24.py
   26px:
           courier  .............ezFBfont_courB18_latin_26.py
   29px:
             times  ..............ezFBfont_timB18_latin_29.py
             times  ..............ezFBfont_timR18_latin_29.py
         helvetica  .............ezFBfont_helvR18_latin_29.py
         helvetica  .............ezFBfont_helvB18_latin_29.py
        schoolbook  .............ezFBfont_ncenB18_latin_29.py
        schoolbook  .............ezFBfont_ncenR18_latin_29.py
   32px:
           courier  .............ezFBfont_courR24_latin_32.py
            spleen  ........ezFBfont_spleen_16x32_latin_32.py
   33px:
           courier  .............ezFBfont_courB24_latin_33.py
   37px:
             times  ..............ezFBfont_timR24_latin_37.py
             times  ..............ezFBfont_timB24_latin_37.py
   38px:
         helvetica  .............ezFBfont_helvB24_latin_38.py
         helvetica  .............ezFBfont_helvR24_latin_38.py
   39px:
        schoolbook  .............ezFBfont_ncenR24_latin_39.py
   40px:
        schoolbook  .............ezFBfont_ncenB24_latin_40.py
   64px:
            spleen  ........ezFBfont_spleen_32x64_latin_64.py

Full character set
------------------
Size:       Family                                       Name
    5px:
           generic  ................ezFBfont_micro_full_05.py
    6px:
             fixed  ..................ezFBfont_4x6_full_06.py
    7px:
             fixed  ..................ezFBfont_5x7_full_07.py
    8px:
             fixed  ..................ezFBfont_5x8_full_08.py
       amstrad-cpc  .ezFBfont_amstrad_cpc_extended_full_08.py
            spleen  ...........ezFBfont_spleen_5x8_full_08.py
    9px:
             fixed  ..................ezFBfont_6x9_full_09.py
   10px:
             fixed  .................ezFBfont_6x10_full_10.py
   11px:
           courier  ..............ezFBfont_courB08_full_11.py
           courier  ..............ezFBfont_courR08_full_11.py
         helvetica  ..........ezFBfont_helvB08_gps_full_11.py
   12px:
             fixed  .................ezFBfont_6x12_full_12.py
             fixed  ................ezFBfont_7x13O_full_12.py
             fixed  ................ezFBfont_7x13B_full_12.py
             fixed  ................ezFBfont_6x13B_full_12.py
             fixed  .................ezFBfont_7x13_full_12.py
             fixed  ................ezFBfont_6x13O_full_12.py
             fixed  ................ezFBfont_8x13O_full_12.py
             fixed  .................ezFBfont_8x13_full_12.py
             fixed  .................ezFBfont_6x13_full_12.py
            spleen  ..........ezFBfont_spleen_6x12_full_12.py
   13px:
             fixed  ................ezFBfont_8x13B_full_13.py
             times  ...............ezFBfont_timB08_full_13.py
             times  ...............ezFBfont_timR08_full_13.py
         helvetica  ..............ezFBfont_helvB08_full_13.py
         helvetica  ..............ezFBfont_helvR08_full_13.py
        schoolbook  ..............ezFBfont_ncenR08_full_13.py
        schoolbook  ..............ezFBfont_ncenB08_full_13.py
   14px:
             fixed  ................ezFBfont_7x14B_full_14.py
             fixed  .................ezFBfont_7x14_full_14.py
   15px:
             fixed  .................ezFBfont_9x15_full_15.py
             fixed  ................ezFBfont_9x15B_full_15.py
           courier  ..............ezFBfont_courR10_full_15.py
            spleen  ..........ezFBfont_spleen_8x16_full_15.py
   16px:
           courier  ..............ezFBfont_courB10_full_16.py
   17px:
             fixed  .................ezFBfont_9x18_full_17.py
           courier  ..............ezFBfont_courR12_full_17.py
           courier  ..............ezFBfont_courB12_full_17.py
             times  ...............ezFBfont_timR10_full_17.py
             times  ...............ezFBfont_timB10_full_17.py
         helvetica  ..............ezFBfont_helvR10_full_17.py
         helvetica  ..............ezFBfont_helvB10_full_17.py
        schoolbook  ..............ezFBfont_ncenR10_full_17.py
   18px:
             fixed  ................ezFBfont_9x18B_full_18.py
        schoolbook  ..............ezFBfont_ncenB10_full_18.py
   19px:
           courier  ..............ezFBfont_courR14_full_19.py
             times  ...............ezFBfont_timR12_full_19.py
        schoolbook  ..............ezFBfont_ncenR12_full_19.py
        schoolbook  ..............ezFBfont_ncenB12_full_19.py
   20px:
             fixed  ................ezFBfont_10x20_full_20.py
           courier  ..............ezFBfont_courB14_full_20.py
             times  ...............ezFBfont_timB12_full_20.py
         helvetica  ..............ezFBfont_helvR12_full_20.py
         helvetica  ..............ezFBfont_helvB12_full_20.py
   21px:
             times  ...............ezFBfont_timB14_full_21.py
   22px:
             times  ...............ezFBfont_timR14_full_22.py
         helvetica  ..............ezFBfont_helvR14_full_22.py
   23px:
         helvetica  ..............ezFBfont_helvB14_full_23.py
        schoolbook  ..............ezFBfont_ncenR14_full_23.py
        schoolbook  ..............ezFBfont_ncenB14_full_23.py
   24px:
           courier  ..............ezFBfont_courR18_full_24.py
            spleen  .........ezFBfont_spleen_12x24_full_24.py
   26px:
           courier  ..............ezFBfont_courB18_full_26.py
   29px:
             times  ...............ezFBfont_timB18_full_29.py
             times  ...............ezFBfont_timR18_full_29.py
         helvetica  ..............ezFBfont_helvR18_full_29.py
         helvetica  ..............ezFBfont_helvB18_full_29.py
        schoolbook  ..............ezFBfont_ncenB18_full_29.py
        schoolbook  ..............ezFBfont_ncenR18_full_29.py
   32px:
           courier  ..............ezFBfont_courR24_full_32.py
            spleen  .........ezFBfont_spleen_16x32_full_32.py
   33px:
           courier  ..............ezFBfont_courB24_full_33.py
   37px:
             times  ...............ezFBfont_timB24_full_37.py
             times  ...............ezFBfont_timR24_full_37.py
   38px:
         helvetica  ..............ezFBfont_helvB24_full_38.py
         helvetica  ..............ezFBfont_helvR24_full_38.py
   39px:
        schoolbook  ..............ezFBfont_ncenR24_full_39.py
   40px:
        schoolbook  ..............ezFBfont_ncenB24_full_40.py
   64px:
            spleen  .........ezFBfont_spleen_32x64_full_64.py
```
---------------------
## Converter script
The font structure is created by the 'build-sets.py' script in the `bdf2dict` folder, see the README there for more.

The `sets.py` file in this folder contains the character definitions and font source.
