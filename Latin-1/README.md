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

Fonts as of 9 Jun 2024 organised by charset/height/family.

```
Micropython font module tree for: Latin-1

   Size     Family                      Name                   (weight)

Time character set
------------------
    5px:
          fixed4x6..............ezFBfont_05_tom_thumb_time.py
           generic.............ezFBfont_05_font_tiny5_time.py
           generic..................ezFBfont_05_micro_time.py
             fixed....................ezFBfont_05_4x6_time.py
    6px:
             fixed....................ezFBfont_06_6x9_time.py
             fixed....................ezFBfont_06_5x7_time.py
            spleen.............ezFBfont_06_spleen_5x8_time.py
    7px:
       amstrad-cpc...ezFBfont_07_amstrad_cpc_extended_time.py
             times.................ezFBfont_07_timB08_time.py (bold)
             times.................ezFBfont_07_timR08_time.py (regular)
           courier................ezFBfont_07_courB08_time.py (bold)
           courier................ezFBfont_07_courR08_time.py (regular)
             fixed...................ezFBfont_07_6x12_time.py
             fixed....................ezFBfont_07_5x8_time.py
           biwidth..................ezFBfont_07_b12_b_time.py (bold)
           biwidth....................ezFBfont_07_b12_time.py
           biwidth....................ezFBfont_07_b10_time.py
           biwidth..................ezFBfont_07_b10_b_time.py (bold)
    8px:
         helvetica................ezFBfont_08_helvB08_time.py (bold)
         helvetica................ezFBfont_08_helvR08_time.py (regular)
         helvetica............ezFBfont_08_helvB08_gps_time.py (bold)
             fixed...................ezFBfont_08_6x10_time.py
            spleen............ezFBfont_08_spleen_6x12_time.py
        schoolbook................ezFBfont_08_ncenR08_time.py (regular)
        schoolbook................ezFBfont_08_ncenB08_time.py (bold)
    9px:
             fixed.............ezFBfont_09_etl14_thai_time.py
           biwidth..................ezFBfont_09_b14_b_time.py (bold)
           biwidth....................ezFBfont_09_b14_time.py
   10px:
             times.................ezFBfont_10_timB10_time.py (bold)
             times.................ezFBfont_10_timR10_time.py (regular)
           courier................ezFBfont_10_courB10_time.py (bold)
           courier................ezFBfont_10_courR10_time.py (regular)
             fixed...................ezFBfont_10_7x13_time.py
             fixed.............ezFBfont_10_etl16_thai_time.py
             fixed...................ezFBfont_10_9x18_time.py
             fixed...................ezFBfont_10_6x13_time.py
             fixed...................ezFBfont_10_9x15_time.py
             fixed...................ezFBfont_10_8x13_time.py
            spleen............ezFBfont_10_spleen_8x16_time.py
           biwidth..................ezFBfont_10_b16_b_time.py (bold)
           biwidth....................ezFBfont_10_b16_time.py
   11px:
             times.................ezFBfont_11_timB12_time.py (bold)
             times.................ezFBfont_11_timR12_time.py (regular)
           courier................ezFBfont_11_courB12_time.py (bold)
           courier................ezFBfont_11_courR12_time.py (regular)
         helvetica................ezFBfont_11_helvB10_time.py (bold)
         helvetica................ezFBfont_11_helvR10_time.py (regular)
             fixed...................ezFBfont_11_7x14_time.py
        schoolbook................ezFBfont_11_ncenR10_time.py (regular)
        schoolbook................ezFBfont_11_ncenB10_time.py (bold)
   12px:
           courier................ezFBfont_12_courR14_time.py (regular)
           courier................ezFBfont_12_courB14_time.py (bold)
         helvetica................ezFBfont_12_helvB12_time.py (bold)
         helvetica................ezFBfont_12_helvR12_time.py (regular)
        schoolbook................ezFBfont_12_ncenB12_time.py (bold)
        schoolbook................ezFBfont_12_ncenR12_time.py (regular)
   13px:
             times.................ezFBfont_13_timR14_time.py (regular)
             times.................ezFBfont_13_timB14_time.py (bold)
         helvetica................ezFBfont_13_helvB14_time.py (bold)
         helvetica................ezFBfont_13_helvR14_time.py (regular)
             fixed..................ezFBfont_13_10x20_time.py
   14px:
             fixed.............ezFBfont_14_etl24_thai_time.py
        schoolbook................ezFBfont_14_ncenB14_time.py (bold)
        schoolbook................ezFBfont_14_ncenR14_time.py (regular)
   15px:
           courier................ezFBfont_15_courR18_time.py (regular)
            spleen...........ezFBfont_15_spleen_12x24_time.py
   16px:
           courier................ezFBfont_16_courB18_time.py (bold)
   17px:
             times.................ezFBfont_17_timB18_time.py (bold)
             times.................ezFBfont_17_timR18_time.py (regular)
   18px:
         helvetica................ezFBfont_18_helvR18_time.py (regular)
         helvetica................ezFBfont_18_helvB18_time.py (bold)
        schoolbook................ezFBfont_18_ncenB18_time.py (bold)
        schoolbook................ezFBfont_18_ncenR18_time.py (regular)
   20px:
           courier................ezFBfont_20_courR24_time.py (regular)
            spleen...........ezFBfont_20_spleen_16x32_time.py
   21px:
           courier................ezFBfont_21_courB24_time.py (bold)
   23px:
             times.................ezFBfont_23_timR24_time.py (regular)
             times.................ezFBfont_23_timB24_time.py (bold)
   24px:
         helvetica................ezFBfont_24_helvR24_time.py (regular)
         helvetica................ezFBfont_24_helvB24_time.py (bold)
        schoolbook................ezFBfont_24_ncenB24_time.py (bold)
   25px:
        schoolbook................ezFBfont_25_ncenR24_time.py (regular)
   40px:
            spleen...........ezFBfont_40_spleen_32x64_time.py

Numeric character set
---------------------
    5px:
          fixed4x6...............ezFBfont_05_tom_thumb_num.py
           generic...................ezFBfont_05_micro_num.py
    6px:
           generic..............ezFBfont_06_font_tiny5_num.py
             fixed.....................ezFBfont_06_4x6_num.py
    7px:
             fixed.....................ezFBfont_07_5x7_num.py
             fixed.....................ezFBfont_07_5x8_num.py
           biwidth.....................ezFBfont_07_b10_num.py
           biwidth...................ezFBfont_07_b10_b_num.py (bold)
    8px:
       amstrad-cpc....ezFBfont_08_amstrad_cpc_extended_num.py
             fixed....................ezFBfont_08_6x10_num.py
            spleen..............ezFBfont_08_spleen_5x8_num.py
    9px:
             times..................ezFBfont_09_timR08_num.py (regular)
           courier.................ezFBfont_09_courB08_num.py (bold)
             fixed.....................ezFBfont_09_6x9_num.py
   10px:
             times..................ezFBfont_10_timB08_num.py (bold)
           courier.................ezFBfont_10_courR08_num.py (regular)
         helvetica.............ezFBfont_10_helvB08_gps_num.py (bold)
         helvetica.................ezFBfont_10_helvR08_num.py (regular)
         helvetica.................ezFBfont_10_helvB08_num.py (bold)
             fixed....................ezFBfont_10_6x12_num.py
             fixed....................ezFBfont_10_7x13_num.py
             fixed....................ezFBfont_10_8x13_num.py
            spleen.............ezFBfont_10_spleen_6x12_num.py
        schoolbook.................ezFBfont_10_ncenB08_num.py (bold)
        schoolbook.................ezFBfont_10_ncenR08_num.py (regular)
           biwidth...................ezFBfont_10_b12_b_num.py (bold)
           biwidth.....................ezFBfont_10_b12_num.py
   11px:
             fixed....................ezFBfont_11_6x13_num.py
   12px:
           courier.................ezFBfont_12_courB10_num.py (bold)
           courier.................ezFBfont_12_courR10_num.py (regular)
             fixed..............ezFBfont_12_etl14_thai_num.py
            spleen.............ezFBfont_12_spleen_8x16_num.py
   13px:
             times..................ezFBfont_13_timB10_num.py (bold)
             times..................ezFBfont_13_timR10_num.py (regular)
           courier.................ezFBfont_13_courR12_num.py (regular)
             fixed....................ezFBfont_13_9x18_num.py
             fixed....................ezFBfont_13_7x14_num.py
             fixed..............ezFBfont_13_etl16_thai_num.py
        schoolbook.................ezFBfont_13_ncenB10_num.py (bold)
        schoolbook.................ezFBfont_13_ncenR10_num.py (regular)
   14px:
             times..................ezFBfont_14_timR12_num.py (regular)
         helvetica.................ezFBfont_14_helvB10_num.py (bold)
         helvetica.................ezFBfont_14_helvR10_num.py (regular)
             fixed...................ezFBfont_14_10x20_num.py
             fixed....................ezFBfont_14_9x15_num.py
           biwidth...................ezFBfont_14_b14_b_num.py (bold)
           biwidth.....................ezFBfont_14_b14_num.py
   15px:
             times..................ezFBfont_15_timB12_num.py (bold)
           courier.................ezFBfont_15_courB12_num.py (bold)
         helvetica.................ezFBfont_15_helvB12_num.py (bold)
        schoolbook.................ezFBfont_15_ncenR12_num.py (regular)
        schoolbook.................ezFBfont_15_ncenB12_num.py (bold)
   16px:
           courier.................ezFBfont_16_courR14_num.py (regular)
           courier.................ezFBfont_16_courB14_num.py (bold)
         helvetica.................ezFBfont_16_helvR12_num.py (regular)
           biwidth...................ezFBfont_16_b16_b_num.py (bold)
           biwidth.....................ezFBfont_16_b16_num.py
   17px:
             times..................ezFBfont_17_timB14_num.py (bold)
             times..................ezFBfont_17_timR14_num.py (regular)
             fixed..............ezFBfont_17_etl24_thai_num.py
        schoolbook.................ezFBfont_17_ncenB14_num.py (bold)
        schoolbook.................ezFBfont_17_ncenR14_num.py (regular)
   18px:
         helvetica.................ezFBfont_18_helvB14_num.py (bold)
         helvetica.................ezFBfont_18_helvR14_num.py (regular)
   19px:
           courier.................ezFBfont_19_courR18_num.py (regular)
   20px:
            spleen............ezFBfont_20_spleen_12x24_num.py
   21px:
           courier.................ezFBfont_21_courB18_num.py (bold)
   22px:
             times..................ezFBfont_22_timR18_num.py (regular)
             times..................ezFBfont_22_timB18_num.py (bold)
        schoolbook.................ezFBfont_22_ncenB18_num.py (bold)
        schoolbook.................ezFBfont_22_ncenR18_num.py (regular)
   24px:
         helvetica.................ezFBfont_24_helvB18_num.py (bold)
         helvetica.................ezFBfont_24_helvR18_num.py (regular)
   26px:
           courier.................ezFBfont_26_courR24_num.py (regular)
            spleen............ezFBfont_26_spleen_16x32_num.py
   28px:
             times..................ezFBfont_28_timR24_num.py (regular)
           courier.................ezFBfont_28_courB24_num.py (bold)
   30px:
        schoolbook.................ezFBfont_30_ncenB24_num.py (bold)
   31px:
             times..................ezFBfont_31_timB24_num.py (bold)
         helvetica.................ezFBfont_31_helvB24_num.py (bold)
        schoolbook.................ezFBfont_31_ncenR24_num.py (regular)
   33px:
         helvetica.................ezFBfont_33_helvR24_num.py (regular)
   56px:
            spleen............ezFBfont_56_spleen_32x64_num.py

Uppercase character set
-----------------------
    5px:
          fixed4x6.............ezFBfont_05_tom_thumb_upper.py
           generic.................ezFBfont_05_micro_upper.py
    6px:
           generic............ezFBfont_06_font_tiny5_upper.py
             fixed...................ezFBfont_06_4x6_upper.py
    7px:
             fixed...................ezFBfont_07_5x7_upper.py
    8px:
       amstrad-cpc..ezFBfont_08_amstrad_cpc_extended_upper.py
             fixed...................ezFBfont_08_5x8_upper.py
             fixed..................ezFBfont_08_6x10_upper.py
            spleen............ezFBfont_08_spleen_5x8_upper.py
           biwidth...................ezFBfont_08_b10_upper.py
           biwidth.................ezFBfont_08_b10_b_upper.py (bold)
    9px:
             fixed...................ezFBfont_09_6x9_upper.py
   10px:
           courier...............ezFBfont_10_courB08_upper.py (bold)
           courier...............ezFBfont_10_courR08_upper.py (regular)
             fixed..................ezFBfont_10_6x12_upper.py
             fixed..................ezFBfont_10_8x13_upper.py
            spleen...........ezFBfont_10_spleen_6x12_upper.py
           biwidth...................ezFBfont_10_b12_upper.py
           biwidth.................ezFBfont_10_b12_b_upper.py (bold)
   11px:
             times................ezFBfont_11_timR08_upper.py (regular)
             times................ezFBfont_11_timB08_upper.py (bold)
         helvetica...............ezFBfont_11_helvR08_upper.py (regular)
         helvetica...........ezFBfont_11_helvB08_gps_upper.py (bold)
         helvetica...............ezFBfont_11_helvB08_upper.py (bold)
             fixed..................ezFBfont_11_7x13_upper.py
             fixed..................ezFBfont_11_6x13_upper.py
        schoolbook...............ezFBfont_11_ncenB08_upper.py (bold)
        schoolbook...............ezFBfont_11_ncenR08_upper.py (regular)
   13px:
           courier...............ezFBfont_13_courB10_upper.py (bold)
             fixed..................ezFBfont_13_9x18_upper.py
             fixed..................ezFBfont_13_7x14_upper.py
             fixed............ezFBfont_13_etl14_thai_upper.py
           biwidth...................ezFBfont_13_b14_upper.py
           biwidth.................ezFBfont_13_b14_b_upper.py (bold)
   14px:
             times................ezFBfont_14_timB10_upper.py (bold)
             times................ezFBfont_14_timR10_upper.py (regular)
           courier...............ezFBfont_14_courR10_upper.py (regular)
             fixed.................ezFBfont_14_10x20_upper.py
             fixed..................ezFBfont_14_9x15_upper.py
             fixed............ezFBfont_14_etl16_thai_upper.py
            spleen...........ezFBfont_14_spleen_8x16_upper.py
        schoolbook...............ezFBfont_14_ncenR10_upper.py (regular)
           biwidth...................ezFBfont_14_b16_upper.py
           biwidth.................ezFBfont_14_b16_b_upper.py (bold)
   15px:
             times................ezFBfont_15_timR12_upper.py (regular)
           courier...............ezFBfont_15_courR12_upper.py (regular)
           courier...............ezFBfont_15_courB12_upper.py (bold)
         helvetica...............ezFBfont_15_helvB10_upper.py (bold)
         helvetica...............ezFBfont_15_helvR10_upper.py (regular)
        schoolbook...............ezFBfont_15_ncenB10_upper.py (bold)
   16px:
             times................ezFBfont_16_timB12_upper.py (bold)
         helvetica...............ezFBfont_16_helvB12_upper.py (bold)
        schoolbook...............ezFBfont_16_ncenR12_upper.py (regular)
   17px:
           courier...............ezFBfont_17_courR14_upper.py (regular)
           courier...............ezFBfont_17_courB14_upper.py (bold)
         helvetica...............ezFBfont_17_helvR12_upper.py (regular)
        schoolbook...............ezFBfont_17_ncenB12_upper.py (bold)
   18px:
             times................ezFBfont_18_timR14_upper.py (regular)
             times................ezFBfont_18_timB14_upper.py (bold)
         helvetica...............ezFBfont_18_helvB14_upper.py (bold)
         helvetica...............ezFBfont_18_helvR14_upper.py (regular)
   19px:
             fixed............ezFBfont_19_etl24_thai_upper.py
        schoolbook...............ezFBfont_19_ncenR14_upper.py (regular)
   20px:
        schoolbook...............ezFBfont_20_ncenB14_upper.py (bold)
   21px:
           courier...............ezFBfont_21_courB18_upper.py (bold)
   22px:
           courier...............ezFBfont_22_courR18_upper.py (regular)
            spleen..........ezFBfont_22_spleen_12x24_upper.py
   23px:
             times................ezFBfont_23_timB18_upper.py (bold)
   24px:
             times................ezFBfont_24_timR18_upper.py (regular)
         helvetica...............ezFBfont_24_helvB18_upper.py (bold)
        schoolbook...............ezFBfont_24_ncenR18_upper.py (regular)
   25px:
         helvetica...............ezFBfont_25_helvR18_upper.py (regular)
        schoolbook...............ezFBfont_25_ncenB18_upper.py (bold)
   28px:
           courier...............ezFBfont_28_courR24_upper.py (regular)
            spleen..........ezFBfont_28_spleen_16x32_upper.py
   30px:
           courier...............ezFBfont_30_courB24_upper.py (bold)
   31px:
             times................ezFBfont_31_timR24_upper.py (regular)
         helvetica...............ezFBfont_31_helvB24_upper.py (bold)
   32px:
             times................ezFBfont_32_timB24_upper.py (bold)
        schoolbook...............ezFBfont_32_ncenB24_upper.py (bold)
   33px:
        schoolbook...............ezFBfont_33_ncenR24_upper.py (regular)
   34px:
         helvetica...............ezFBfont_34_helvR24_upper.py (regular)
   56px:
            spleen..........ezFBfont_56_spleen_32x64_upper.py

Ascii character set
-------------------
    5px:
           generic.................ezFBfont_05_micro_ascii.py
    6px:
          fixed4x6.............ezFBfont_06_tom_thumb_ascii.py
           generic............ezFBfont_06_font_tiny5_ascii.py
             fixed...................ezFBfont_06_4x6_ascii.py
    7px:
             fixed...................ezFBfont_07_5x7_ascii.py
    8px:
       amstrad-cpc..ezFBfont_08_amstrad_cpc_extended_ascii.py
             fixed...................ezFBfont_08_5x8_ascii.py
            spleen............ezFBfont_08_spleen_5x8_ascii.py
           biwidth.................ezFBfont_08_b10_b_ascii.py (bold)
           biwidth...................ezFBfont_08_b10_ascii.py
    9px:
             fixed...................ezFBfont_09_6x9_ascii.py
   10px:
           courier...............ezFBfont_10_courR08_ascii.py (regular)
           courier...............ezFBfont_10_courB08_ascii.py (bold)
             fixed..................ezFBfont_10_6x10_ascii.py
             fixed..................ezFBfont_10_6x12_ascii.py
           biwidth.................ezFBfont_10_b12_b_ascii.py (bold)
           biwidth...................ezFBfont_10_b12_ascii.py
   11px:
             times................ezFBfont_11_timR08_ascii.py (regular)
             times................ezFBfont_11_timB08_ascii.py (bold)
         helvetica...............ezFBfont_11_helvB08_ascii.py (bold)
         helvetica...............ezFBfont_11_helvR08_ascii.py (regular)
         helvetica...........ezFBfont_11_helvB08_gps_ascii.py (bold)
        schoolbook...............ezFBfont_11_ncenB08_ascii.py (bold)
        schoolbook...............ezFBfont_11_ncenR08_ascii.py (regular)
   12px:
             fixed..................ezFBfont_12_7x13_ascii.py
             fixed..................ezFBfont_12_8x13_ascii.py
             fixed..................ezFBfont_12_6x13_ascii.py
            spleen...........ezFBfont_12_spleen_6x12_ascii.py
   13px:
             fixed............ezFBfont_13_etl14_thai_ascii.py
             fixed..................ezFBfont_13_7x14_ascii.py
           biwidth...................ezFBfont_13_b14_ascii.py
           biwidth.................ezFBfont_13_b14_b_ascii.py (bold)
   14px:
             times................ezFBfont_14_timR10_ascii.py (regular)
             times................ezFBfont_14_timB10_ascii.py (bold)
           courier...............ezFBfont_14_courB10_ascii.py (bold)
           courier...............ezFBfont_14_courR10_ascii.py (regular)
             fixed..................ezFBfont_14_9x15_ascii.py
             fixed............ezFBfont_14_etl16_thai_ascii.py
            spleen...........ezFBfont_14_spleen_8x16_ascii.py
           biwidth.................ezFBfont_14_b16_b_ascii.py (bold)
           biwidth...................ezFBfont_14_b16_ascii.py
   15px:
           courier...............ezFBfont_15_courB12_ascii.py (bold)
           courier...............ezFBfont_15_courR12_ascii.py (regular)
         helvetica...............ezFBfont_15_helvB10_ascii.py (bold)
         helvetica...............ezFBfont_15_helvR10_ascii.py (regular)
        schoolbook...............ezFBfont_15_ncenB10_ascii.py (bold)
        schoolbook...............ezFBfont_15_ncenR10_ascii.py (regular)
   16px:
             times................ezFBfont_16_timB12_ascii.py (bold)
             times................ezFBfont_16_timR12_ascii.py (regular)
             fixed..................ezFBfont_16_9x18_ascii.py
        schoolbook...............ezFBfont_16_ncenR12_ascii.py (regular)
   17px:
           courier...............ezFBfont_17_courB14_ascii.py (bold)
           courier...............ezFBfont_17_courR14_ascii.py (regular)
         helvetica...............ezFBfont_17_helvB12_ascii.py (bold)
         helvetica...............ezFBfont_17_helvR12_ascii.py (regular)
             fixed.................ezFBfont_17_10x20_ascii.py
        schoolbook...............ezFBfont_17_ncenB12_ascii.py (bold)
   18px:
             times................ezFBfont_18_timB14_ascii.py (bold)
             times................ezFBfont_18_timR14_ascii.py (regular)
         helvetica...............ezFBfont_18_helvR14_ascii.py (regular)
         helvetica...............ezFBfont_18_helvB14_ascii.py (bold)
   19px:
        schoolbook...............ezFBfont_19_ncenR14_ascii.py (regular)
   20px:
        schoolbook...............ezFBfont_20_ncenB14_ascii.py (bold)
   22px:
           courier...............ezFBfont_22_courR18_ascii.py (regular)
           courier...............ezFBfont_22_courB18_ascii.py (bold)
   23px:
             times................ezFBfont_23_timB18_ascii.py (bold)
             fixed............ezFBfont_23_etl24_thai_ascii.py
            spleen..........ezFBfont_23_spleen_12x24_ascii.py
   24px:
         helvetica...............ezFBfont_24_helvB18_ascii.py (bold)
   25px:
             times................ezFBfont_25_timR18_ascii.py (regular)
         helvetica...............ezFBfont_25_helvR18_ascii.py (regular)
        schoolbook...............ezFBfont_25_ncenB18_ascii.py (bold)
        schoolbook...............ezFBfont_25_ncenR18_ascii.py (regular)
   28px:
           courier...............ezFBfont_28_courR24_ascii.py (regular)
   30px:
           courier...............ezFBfont_30_courB24_ascii.py (bold)
            spleen..........ezFBfont_30_spleen_16x32_ascii.py
   32px:
             times................ezFBfont_32_timR24_ascii.py (regular)
         helvetica...............ezFBfont_32_helvB24_ascii.py (bold)
   33px:
             times................ezFBfont_33_timB24_ascii.py (bold)
        schoolbook...............ezFBfont_33_ncenB24_ascii.py (bold)
   34px:
         helvetica...............ezFBfont_34_helvR24_ascii.py (regular)
        schoolbook...............ezFBfont_34_ncenR24_ascii.py (regular)
   60px:
            spleen..........ezFBfont_60_spleen_32x64_ascii.py

Supplemental character set
--------------------------
    6px:
          fixed4x6..............ezFBfont_06_tom_thumb_supp.py
           generic.............ezFBfont_06_font_tiny5_supp.py
             fixed....................ezFBfont_06_4x6_supp.py
    7px:
             fixed....................ezFBfont_07_5x7_supp.py
    8px:
       amstrad-cpc...ezFBfont_08_amstrad_cpc_extended_supp.py
             fixed....................ezFBfont_08_5x8_supp.py
           biwidth..................ezFBfont_08_b10_b_supp.py (bold)
           biwidth....................ezFBfont_08_b10_supp.py
    9px:
             fixed....................ezFBfont_09_6x9_supp.py
   10px:
             fixed...................ezFBfont_10_6x10_supp.py
   11px:
           courier................ezFBfont_11_courR08_supp.py (regular)
           courier................ezFBfont_11_courB08_supp.py (bold)
   12px:
             fixed...................ezFBfont_12_7x13_supp.py
             fixed...................ezFBfont_12_6x13_supp.py
             fixed...................ezFBfont_12_8x13_supp.py
             fixed...................ezFBfont_12_6x12_supp.py
            spleen............ezFBfont_12_spleen_6x12_supp.py
           biwidth..................ezFBfont_12_b12_b_supp.py (bold)
           biwidth....................ezFBfont_12_b12_supp.py
   13px:
             times.................ezFBfont_13_timB08_supp.py (bold)
             times.................ezFBfont_13_timR08_supp.py (regular)
         helvetica................ezFBfont_13_helvB08_supp.py (bold)
         helvetica................ezFBfont_13_helvR08_supp.py (regular)
        schoolbook................ezFBfont_13_ncenB08_supp.py (bold)
        schoolbook................ezFBfont_13_ncenR08_supp.py (regular)
   14px:
             fixed...................ezFBfont_14_7x14_supp.py
           biwidth..................ezFBfont_14_b14_b_supp.py (bold)
           biwidth....................ezFBfont_14_b14_supp.py
   15px:
           courier................ezFBfont_15_courR10_supp.py (regular)
             fixed...................ezFBfont_15_9x15_supp.py
            spleen............ezFBfont_15_spleen_8x16_supp.py
   16px:
           courier................ezFBfont_16_courB10_supp.py (bold)
           biwidth..................ezFBfont_16_b16_b_supp.py (bold)
           biwidth....................ezFBfont_16_b16_supp.py
   17px:
             times.................ezFBfont_17_timB10_supp.py (bold)
             times.................ezFBfont_17_timR10_supp.py (regular)
           courier................ezFBfont_17_courB12_supp.py (bold)
           courier................ezFBfont_17_courR12_supp.py (regular)
         helvetica................ezFBfont_17_helvR10_supp.py (regular)
         helvetica................ezFBfont_17_helvB10_supp.py (bold)
             fixed.............ezFBfont_17_etl14_thai_supp.py
             fixed...................ezFBfont_17_9x18_supp.py
        schoolbook................ezFBfont_17_ncenR10_supp.py (regular)
   18px:
        schoolbook................ezFBfont_18_ncenB10_supp.py (bold)
   19px:
             times.................ezFBfont_19_timR12_supp.py (regular)
           courier................ezFBfont_19_courR14_supp.py (regular)
             fixed.............ezFBfont_19_etl16_thai_supp.py
        schoolbook................ezFBfont_19_ncenR12_supp.py (regular)
        schoolbook................ezFBfont_19_ncenB12_supp.py (bold)
   20px:
             times.................ezFBfont_20_timB12_supp.py (bold)
           courier................ezFBfont_20_courB14_supp.py (bold)
         helvetica................ezFBfont_20_helvB12_supp.py (bold)
         helvetica................ezFBfont_20_helvR12_supp.py (regular)
             fixed..................ezFBfont_20_10x20_supp.py
   21px:
             times.................ezFBfont_21_timB14_supp.py (bold)
   22px:
             times.................ezFBfont_22_timR14_supp.py (regular)
         helvetica................ezFBfont_22_helvR14_supp.py (regular)
   23px:
         helvetica................ezFBfont_23_helvB14_supp.py (bold)
        schoolbook................ezFBfont_23_ncenB14_supp.py (bold)
        schoolbook................ezFBfont_23_ncenR14_supp.py (regular)
   24px:
           courier................ezFBfont_24_courR18_supp.py (regular)
            spleen...........ezFBfont_24_spleen_12x24_supp.py
   26px:
           courier................ezFBfont_26_courB18_supp.py (bold)
   29px:
             times.................ezFBfont_29_timR18_supp.py (regular)
             times.................ezFBfont_29_timB18_supp.py (bold)
         helvetica................ezFBfont_29_helvB18_supp.py (bold)
         helvetica................ezFBfont_29_helvR18_supp.py (regular)
             fixed.............ezFBfont_29_etl24_thai_supp.py
        schoolbook................ezFBfont_29_ncenB18_supp.py (bold)
        schoolbook................ezFBfont_29_ncenR18_supp.py (regular)
   32px:
           courier................ezFBfont_32_courR24_supp.py (regular)
            spleen...........ezFBfont_32_spleen_16x32_supp.py
   33px:
           courier................ezFBfont_33_courB24_supp.py (bold)
   37px:
             times.................ezFBfont_37_timR24_supp.py (regular)
             times.................ezFBfont_37_timB24_supp.py (bold)
   38px:
         helvetica................ezFBfont_38_helvB24_supp.py (bold)
         helvetica................ezFBfont_38_helvR24_supp.py (regular)
   39px:
        schoolbook................ezFBfont_39_ncenR24_supp.py (regular)
   40px:
        schoolbook................ezFBfont_40_ncenB24_supp.py (bold)
   64px:
            spleen...........ezFBfont_64_spleen_32x64_supp.py

Latin-1 character set
---------------------
    6px:
          fixed4x6.............ezFBfont_06_tom_thumb_latin.py
           generic............ezFBfont_06_font_tiny5_latin.py
             fixed...................ezFBfont_06_4x6_latin.py
    7px:
             fixed...................ezFBfont_07_5x7_latin.py
    8px:
       amstrad-cpc..ezFBfont_08_amstrad_cpc_extended_latin.py
             fixed...................ezFBfont_08_5x8_latin.py
            spleen............ezFBfont_08_spleen_5x8_latin.py
           biwidth.................ezFBfont_08_b10_b_latin.py (bold)
           biwidth...................ezFBfont_08_b10_latin.py
    9px:
             fixed...................ezFBfont_09_6x9_latin.py
   10px:
             fixed..................ezFBfont_10_6x10_latin.py
   11px:
           courier...............ezFBfont_11_courR08_latin.py (regular)
           courier...............ezFBfont_11_courB08_latin.py (bold)
   12px:
             fixed..................ezFBfont_12_7x13_latin.py
             fixed..................ezFBfont_12_8x13_latin.py
             fixed..................ezFBfont_12_6x12_latin.py
             fixed..................ezFBfont_12_6x13_latin.py
            spleen...........ezFBfont_12_spleen_6x12_latin.py
           biwidth.................ezFBfont_12_b12_b_latin.py (bold)
           biwidth...................ezFBfont_12_b12_latin.py
   13px:
             times................ezFBfont_13_timB08_latin.py (bold)
             times................ezFBfont_13_timR08_latin.py (regular)
         helvetica...............ezFBfont_13_helvB08_latin.py (bold)
         helvetica...............ezFBfont_13_helvR08_latin.py (regular)
        schoolbook...............ezFBfont_13_ncenB08_latin.py (bold)
        schoolbook...............ezFBfont_13_ncenR08_latin.py (regular)
   14px:
             fixed..................ezFBfont_14_7x14_latin.py
           biwidth...................ezFBfont_14_b14_latin.py
           biwidth.................ezFBfont_14_b14_b_latin.py (bold)
   15px:
           courier...............ezFBfont_15_courR10_latin.py (regular)
             fixed..................ezFBfont_15_9x15_latin.py
            spleen...........ezFBfont_15_spleen_8x16_latin.py
   16px:
           courier...............ezFBfont_16_courB10_latin.py (bold)
           biwidth...................ezFBfont_16_b16_latin.py
           biwidth.................ezFBfont_16_b16_b_latin.py (bold)
   17px:
             times................ezFBfont_17_timB10_latin.py (bold)
             times................ezFBfont_17_timR10_latin.py (regular)
           courier...............ezFBfont_17_courR12_latin.py (regular)
           courier...............ezFBfont_17_courB12_latin.py (bold)
         helvetica...............ezFBfont_17_helvR10_latin.py (regular)
         helvetica...............ezFBfont_17_helvB10_latin.py (bold)
             fixed..................ezFBfont_17_9x18_latin.py
             fixed............ezFBfont_17_etl14_thai_latin.py
        schoolbook...............ezFBfont_17_ncenR10_latin.py (regular)
   18px:
        schoolbook...............ezFBfont_18_ncenB10_latin.py (bold)
   19px:
             times................ezFBfont_19_timR12_latin.py (regular)
           courier...............ezFBfont_19_courR14_latin.py (regular)
             fixed............ezFBfont_19_etl16_thai_latin.py
        schoolbook...............ezFBfont_19_ncenB12_latin.py (bold)
        schoolbook...............ezFBfont_19_ncenR12_latin.py (regular)
   20px:
             times................ezFBfont_20_timB12_latin.py (bold)
           courier...............ezFBfont_20_courB14_latin.py (bold)
         helvetica...............ezFBfont_20_helvB12_latin.py (bold)
         helvetica...............ezFBfont_20_helvR12_latin.py (regular)
             fixed.................ezFBfont_20_10x20_latin.py
   21px:
             times................ezFBfont_21_timB14_latin.py (bold)
   22px:
             times................ezFBfont_22_timR14_latin.py (regular)
         helvetica...............ezFBfont_22_helvR14_latin.py (regular)
   23px:
         helvetica...............ezFBfont_23_helvB14_latin.py (bold)
        schoolbook...............ezFBfont_23_ncenR14_latin.py (regular)
        schoolbook...............ezFBfont_23_ncenB14_latin.py (bold)
   24px:
           courier...............ezFBfont_24_courR18_latin.py (regular)
            spleen..........ezFBfont_24_spleen_12x24_latin.py
   26px:
           courier...............ezFBfont_26_courB18_latin.py (bold)
   29px:
             times................ezFBfont_29_timB18_latin.py (bold)
             times................ezFBfont_29_timR18_latin.py (regular)
         helvetica...............ezFBfont_29_helvB18_latin.py (bold)
         helvetica...............ezFBfont_29_helvR18_latin.py (regular)
             fixed............ezFBfont_29_etl24_thai_latin.py
        schoolbook...............ezFBfont_29_ncenB18_latin.py (bold)
        schoolbook...............ezFBfont_29_ncenR18_latin.py (regular)
   32px:
           courier...............ezFBfont_32_courR24_latin.py (regular)
            spleen..........ezFBfont_32_spleen_16x32_latin.py
   33px:
           courier...............ezFBfont_33_courB24_latin.py (bold)
   37px:
             times................ezFBfont_37_timR24_latin.py (regular)
             times................ezFBfont_37_timB24_latin.py (bold)
   38px:
         helvetica...............ezFBfont_38_helvR24_latin.py (regular)
         helvetica...............ezFBfont_38_helvB24_latin.py (bold)
   39px:
        schoolbook...............ezFBfont_39_ncenR24_latin.py (regular)
   40px:
        schoolbook...............ezFBfont_40_ncenB24_latin.py (bold)
   64px:
            spleen..........ezFBfont_64_spleen_32x64_latin.py

Full character set
------------------
    5px:
           generic..................ezFBfont_05_micro_full.py
    6px:
             fixed....................ezFBfont_06_4x6_full.py
    7px:
             fixed....................ezFBfont_07_5x7_full.py
    8px:
       amstrad-cpc...ezFBfont_08_amstrad_cpc_extended_full.py
             fixed....................ezFBfont_08_5x8_full.py
            spleen.............ezFBfont_08_spleen_5x8_full.py
           biwidth....................ezFBfont_08_b10_full.py
           biwidth..................ezFBfont_08_b10_b_full.py (bold)
    9px:
             fixed....................ezFBfont_09_6x9_full.py
   10px:
             fixed...................ezFBfont_10_6x10_full.py
   11px:
           courier................ezFBfont_11_courR08_full.py (regular)
           courier................ezFBfont_11_courB08_full.py (bold)
         helvetica............ezFBfont_11_helvB08_gps_full.py (bold)
   12px:
             fixed...................ezFBfont_12_6x13_full.py
             fixed...................ezFBfont_12_7x13_full.py
             fixed...................ezFBfont_12_6x12_full.py
             fixed...................ezFBfont_12_8x13_full.py
            spleen............ezFBfont_12_spleen_6x12_full.py
           biwidth..................ezFBfont_12_b12_b_full.py (bold)
           biwidth....................ezFBfont_12_b12_full.py
   13px:
             times.................ezFBfont_13_timR08_full.py (regular)
             times.................ezFBfont_13_timB08_full.py (bold)
         helvetica................ezFBfont_13_helvR08_full.py (regular)
         helvetica................ezFBfont_13_helvB08_full.py (bold)
        schoolbook................ezFBfont_13_ncenR08_full.py (regular)
        schoolbook................ezFBfont_13_ncenB08_full.py (bold)
   14px:
             fixed...................ezFBfont_14_7x14_full.py
   15px:
           courier................ezFBfont_15_courR10_full.py (regular)
             fixed...................ezFBfont_15_9x15_full.py
            spleen............ezFBfont_15_spleen_8x16_full.py
   16px:
           courier................ezFBfont_16_courB10_full.py (bold)
           biwidth....................ezFBfont_16_b16_full.py
           biwidth..................ezFBfont_16_b16_b_full.py (bold)
   17px:
             times.................ezFBfont_17_timB10_full.py (bold)
             times.................ezFBfont_17_timR10_full.py (regular)
           courier................ezFBfont_17_courR12_full.py (regular)
           courier................ezFBfont_17_courB12_full.py (bold)
         helvetica................ezFBfont_17_helvB10_full.py (bold)
         helvetica................ezFBfont_17_helvR10_full.py (regular)
             fixed...................ezFBfont_17_9x18_full.py
        schoolbook................ezFBfont_17_ncenR10_full.py (regular)
   18px:
        schoolbook................ezFBfont_18_ncenB10_full.py (bold)
   19px:
             times.................ezFBfont_19_timR12_full.py (regular)
           courier................ezFBfont_19_courR14_full.py (regular)
        schoolbook................ezFBfont_19_ncenR12_full.py (regular)
        schoolbook................ezFBfont_19_ncenB12_full.py (bold)
   20px:
             times.................ezFBfont_20_timB12_full.py (bold)
           courier................ezFBfont_20_courB14_full.py (bold)
         helvetica................ezFBfont_20_helvR12_full.py (regular)
         helvetica................ezFBfont_20_helvB12_full.py (bold)
             fixed..................ezFBfont_20_10x20_full.py
   21px:
             times.................ezFBfont_21_timB14_full.py (bold)
   22px:
             times.................ezFBfont_22_timR14_full.py (regular)
         helvetica................ezFBfont_22_helvR14_full.py (regular)
   23px:
         helvetica................ezFBfont_23_helvB14_full.py (bold)
        schoolbook................ezFBfont_23_ncenR14_full.py (regular)
        schoolbook................ezFBfont_23_ncenB14_full.py (bold)
   24px:
           courier................ezFBfont_24_courR18_full.py (regular)
            spleen...........ezFBfont_24_spleen_12x24_full.py
   26px:
           courier................ezFBfont_26_courB18_full.py (bold)
   29px:
             times.................ezFBfont_29_timB18_full.py (bold)
             times.................ezFBfont_29_timR18_full.py (regular)
         helvetica................ezFBfont_29_helvR18_full.py (regular)
         helvetica................ezFBfont_29_helvB18_full.py (bold)
        schoolbook................ezFBfont_29_ncenB18_full.py (bold)
        schoolbook................ezFBfont_29_ncenR18_full.py (regular)
   32px:
           courier................ezFBfont_32_courR24_full.py (regular)
            spleen...........ezFBfont_32_spleen_16x32_full.py
   33px:
           courier................ezFBfont_33_courB24_full.py (bold)
   37px:
             times.................ezFBfont_37_timR24_full.py (regular)
             times.................ezFBfont_37_timB24_full.py (bold)
   38px:
         helvetica................ezFBfont_38_helvR24_full.py (regular)
         helvetica................ezFBfont_38_helvB24_full.py (bold)
   39px:
        schoolbook................ezFBfont_39_ncenR24_full.py (regular)
   40px:
        schoolbook................ezFBfont_40_ncenB24_full.py (bold)
   64px:
            spleen...........ezFBfont_64_spleen_32x64_full.py

```

---------------------

## Converter script
The font structure is created by the 'convert.py' script in the `tooling` folder, see the README there for more.

The `sets.py` file in this folder contains the character definitions and source font filters.
