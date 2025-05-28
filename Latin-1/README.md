# Latin-1 Font Files

This folder includes font files for use with `ezFBfont` and Peter Hinches' `writer` class.

The fonts are organized by character set, font family, and vertical size:
* See the discussion below for details on each character set.
* The font family name comes from the source font file. If unknown, it is labeled `Generic`.
* The 'height' of each font set refers to its *true height*—the height of the tallest character in that set.
  * This may differ from the height specified in the font name!
  * The same fonts may be listed with different heights depending on the character set provided.
    * For example, numeric character sets are often shorter than full ASCII character sets.

There is a mix of proportional-width and monospaced fonts in the collection. Monospaced fonts usually have their size specified in the font name, while the proportional (X11) fonts typically come in both regular and bold styles.

# COPYRIGHT
Please review the copyright notices in each font file. All fonts here are sourced from the [u8g2](https://github.com/olikraus/u8g2/blob/master/LICENSE) project fonts, a curated repository of freely redistributable, open-source fonts.

Each font retains copyright information in its `.py` include file. Some notices are simple, especially those for fonts created specifically for the U8G2 project, while others are more general open-source licenses. All fonts are freely redistributable.

If using any X11 fonts (such as COUR, HELV, NCEN, TIM, SYMB), please include the Adobe/Digital boilerplate license in your main code license, as shown in this repository’s [LICENSE](/LICENSE) file.

# Collections (Character Sets)

The character sets are grouped by purpose, with smaller sets for time and sensor data, and larger sets with the full character range, as shown below:

* **time** : ``` +-.0123456789:```
* **num** : ``` %()*+,-./0123456789:°```
* **upper** : ``` !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_```
* **ascii** : ``` !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~```
* **supp** : ```¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ```
* **latin** : ``` !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ```
* **full** : All characters from `0x00` to `0xFF`

Note: Most character sets start with `0x32`, the space character.

These can be loosely described as:
* **Time** : numbers and separators used for clocks and timers.
* **Numeric** : numbers, separators, and related symbols used for displaying values.
* **Upper**case : ASCII characters up to `0x5F`, useful for symbols, and requires less memory.
* **Ascii** : full ASCII character set up to `0x7F`.
* **Supplemental** : characters from `0xA0` to `0xFF`.
* **Latin** : all *printable* characters in the font up to `0xFF`.
* **Full** : all characters in the font up to `0xFF`, including those that may not be *printable*.

Sets are generated only if they are *unique*; if a previous set already contains an identical charset, the current set will be skipped.
* Be aware of file sizes; full sets (especially the '`latin`' set) can become large.
* For a detailed font file description and preview, check the corresponding `.map` file in the 'maps' sub-folder.
  * The `.map` file includes an ASCII art glyph for all characters in the font file, showing each character's name, size, bitmap, and baseline.

These sets only cover 'Basic Latin' and 'Latin Supplemental' characters.
* Many of the fonts here have additional characters outside the main Latin range in the Unicode 'Latin Extended ..' or 'IPA Extensions' blocks.
* If you need font packs with these unicode Latin characters you’ll need to generate them using the tools in the [Unicode Folder](/Unicode).

# The list

Fonts as of 28 May 2025 organised by charset/height/family.

```
Micropython font module tree for: Latin-1

Time character set
------------------
Size:          Family                                       Name
    5px:
              generic  ................ezFBfont_micro_time_05.py
                tiny5  ........ezFBfont_tiny5_Regular_time_05.py (regular)
                fixed  ............ezFBfont_tom_thumb_time_05.py
                fixed  ..................ezFBfont_4x6_time_05.py
    6px:
                fixed  ..................ezFBfont_5x7_time_06.py
                fixed  ..................ezFBfont_6x9_time_06.py
               spleen  ...........ezFBfont_spleen_5x8_time_06.py
              pt-sans  ............ezFBfont_PTSans_06_time_06.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_06_time_06.py
    7px:
                times  ...............ezFBfont_timB08_time_07.py (bold)
                times  ...............ezFBfont_timR08_time_07.py (regular)
              courier  ..............ezFBfont_courR08_time_07.py (regular)
              courier  ..............ezFBfont_courB08_time_07.py (bold)
                fixed  .................ezFBfont_6x12_time_07.py
                fixed  ..................ezFBfont_5x8_time_07.py
              pt-sans  ............ezFBfont_PTSans_07_time_07.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_07_time_07.py
    8px:
          amstrad-cpc  .ezFBfont_amstrad_cpc_extended_time_08.py
            helvetica  ..............ezFBfont_helvB08_time_08.py (bold)
            helvetica  ..........ezFBfont_helvB08_gps_time_08.py (bold)
            helvetica  ..............ezFBfont_helvR08_time_08.py (regular)
                fixed  .................ezFBfont_6x10_time_08.py
               spleen  ..........ezFBfont_spleen_6x12_time_08.py
              pt-sans  ............ezFBfont_PTSans_08_time_08.py
           schoolbook  ..............ezFBfont_ncenR08_time_08.py (regular)
           schoolbook  ..............ezFBfont_ncenB08_time_08.py (bold)
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_08_time_08.py
    9px:
              pt-sans  ............ezFBfont_PTSans_09_time_09.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_09_time_09.py
   10px:
                times  ...............ezFBfont_timR10_time_10.py (regular)
                times  ...............ezFBfont_timB10_time_10.py (bold)
              courier  ..............ezFBfont_courB10_time_10.py (bold)
              courier  ..............ezFBfont_courR10_time_10.py (regular)
                fixed  ................ezFBfont_6x13O_time_10.py
                fixed  .................ezFBfont_9x18_time_10.py
                fixed  ................ezFBfont_8x13O_time_10.py
                fixed  .................ezFBfont_6x13_time_10.py
                fixed  .................ezFBfont_7x13_time_10.py
                fixed  ................ezFBfont_6x13B_time_10.py (bold)
                fixed  ................ezFBfont_7x13O_time_10.py
                fixed  ................ezFBfont_9x18B_time_10.py (bold)
                fixed  ................ezFBfont_7x14B_time_10.py (bold)
                fixed  ................ezFBfont_8x13B_time_10.py (bold)
                fixed  .................ezFBfont_9x15_time_10.py
                fixed  .................ezFBfont_8x13_time_10.py
                fixed  ................ezFBfont_7x13B_time_10.py (bold)
               spleen  ..........ezFBfont_spleen_8x16_time_10.py
              pt-sans  ............ezFBfont_PTSans_10_time_10.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_10_time_10.py
   11px:
                times  ...............ezFBfont_timR12_time_11.py (regular)
                times  ...............ezFBfont_timB12_time_11.py (bold)
              courier  ..............ezFBfont_courB12_time_11.py (bold)
              courier  ..............ezFBfont_courR12_time_11.py (regular)
            helvetica  ..............ezFBfont_helvR10_time_11.py (regular)
            helvetica  ..............ezFBfont_helvB10_time_11.py (bold)
                fixed  ................ezFBfont_9x15B_time_11.py (bold)
                fixed  .................ezFBfont_7x14_time_11.py
              pt-sans  ............ezFBfont_PTSans_11_time_11.py
           schoolbook  ..............ezFBfont_ncenB10_time_11.py (bold)
           schoolbook  ..............ezFBfont_ncenR10_time_11.py (regular)
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_11_time_11.py
   12px:
              courier  ..............ezFBfont_courB14_time_12.py (bold)
              courier  ..............ezFBfont_courR14_time_12.py (regular)
            helvetica  ..............ezFBfont_helvB12_time_12.py (bold)
            helvetica  ..............ezFBfont_helvR12_time_12.py (regular)
              pt-sans  ............ezFBfont_PTSans_12_time_12.py
           schoolbook  ..............ezFBfont_ncenR12_time_12.py (regular)
           schoolbook  ..............ezFBfont_ncenB12_time_12.py (bold)
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_12_time_12.py
   13px:
                times  ...............ezFBfont_timR14_time_13.py (regular)
                times  ...............ezFBfont_timB14_time_13.py (bold)
            helvetica  ..............ezFBfont_helvR14_time_13.py (regular)
            helvetica  ..............ezFBfont_helvB14_time_13.py (bold)
                fixed  ................ezFBfont_10x20_time_13.py
   14px:
              pt-sans  ............ezFBfont_PTSans_14_time_14.py
           schoolbook  ..............ezFBfont_ncenR14_time_14.py (regular)
           schoolbook  ..............ezFBfont_ncenB14_time_14.py (bold)
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_14_time_14.py
   15px:
              courier  ..............ezFBfont_courR18_time_15.py (regular)
               spleen  .........ezFBfont_spleen_12x24_time_15.py
   16px:
              courier  ..............ezFBfont_courB18_time_16.py (bold)
              pt-sans  ............ezFBfont_PTSans_16_time_16.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_16_time_16.py
   17px:
                times  ...............ezFBfont_timB18_time_17.py (bold)
                times  ...............ezFBfont_timR18_time_17.py (regular)
   18px:
            helvetica  ..............ezFBfont_helvR18_time_18.py (regular)
            helvetica  ..............ezFBfont_helvB18_time_18.py (bold)
              pt-sans  ............ezFBfont_PTSans_18_time_18.py
           schoolbook  ..............ezFBfont_ncenR18_time_18.py (regular)
           schoolbook  ..............ezFBfont_ncenB18_time_18.py (bold)
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_18_time_18.py
   20px:
              courier  ..............ezFBfont_courR24_time_20.py (regular)
               spleen  .........ezFBfont_spleen_16x32_time_20.py
              pt-sans  ............ezFBfont_PTSans_20_time_20.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_20_time_20.py
   21px:
              courier  ..............ezFBfont_courB24_time_21.py (bold)
   23px:
                times  ...............ezFBfont_timB24_time_23.py (bold)
                times  ...............ezFBfont_timR24_time_23.py (regular)
              pt-sans  ............ezFBfont_PTSans_24_time_23.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_24_time_23.py
   24px:
            helvetica  ..............ezFBfont_helvR24_time_24.py (regular)
            helvetica  ..............ezFBfont_helvB24_time_24.py (bold)
           schoolbook  ..............ezFBfont_ncenB24_time_24.py (bold)
   25px:
           schoolbook  ..............ezFBfont_ncenR24_time_25.py (regular)
   28px:
              pt-sans  ............ezFBfont_PTSans_28_time_28.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_28_time_28.py
   31px:
              pt-sans  ............ezFBfont_PTSans_32_time_31.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_32_time_31.py
   35px:
              pt-sans  ............ezFBfont_PTSans_36_time_35.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_36_time_35.py
   40px:
               spleen  .........ezFBfont_spleen_32x64_time_40.py
   41px:
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_42_time_41.py
   42px:
              pt-sans  ............ezFBfont_PTSans_42_time_42.py
   49px:
              pt-sans  ............ezFBfont_PTSans_48_time_49.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_48_time_49.py
   57px:
              pt-sans  ............ezFBfont_PTSans_56_time_57.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_56_time_57.py
   64px:
              pt-sans  ............ezFBfont_PTSans_64_time_64.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_64_time_64.py

Numeric character set
---------------------
Size:          Family                                       Name
    5px:
              generic  .................ezFBfont_micro_num_05.py
                fixed  .............ezFBfont_tom_thumb_num_05.py
    6px:
                tiny5  .........ezFBfont_tiny5_Regular_num_06.py (regular)
                fixed  ...................ezFBfont_4x6_num_06.py
    7px:
                fixed  ...................ezFBfont_5x8_num_07.py
                fixed  ...................ezFBfont_5x7_num_07.py
    8px:
          amstrad-cpc  ..ezFBfont_amstrad_cpc_extended_num_08.py
                fixed  ..................ezFBfont_6x10_num_08.py
               spleen  ............ezFBfont_spleen_5x8_num_08.py
              pt-sans  .............ezFBfont_PTSans_06_num_08.py
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_06_num_08.py
    9px:
                times  ................ezFBfont_timR08_num_09.py (regular)
              courier  ...............ezFBfont_courB08_num_09.py (bold)
                fixed  ...................ezFBfont_6x9_num_09.py
              pt-sans  .............ezFBfont_PTSans_07_num_09.py
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_07_num_09.py
   10px:
                times  ................ezFBfont_timB08_num_10.py (bold)
              courier  ...............ezFBfont_courR08_num_10.py (regular)
            helvetica  ...........ezFBfont_helvB08_gps_num_10.py (bold)
            helvetica  ...............ezFBfont_helvB08_num_10.py (bold)
            helvetica  ...............ezFBfont_helvR08_num_10.py (regular)
                fixed  ..................ezFBfont_6x12_num_10.py
                fixed  .................ezFBfont_7x13O_num_10.py
                fixed  .................ezFBfont_7x13B_num_10.py (bold)
                fixed  ..................ezFBfont_8x13_num_10.py
                fixed  .................ezFBfont_8x13O_num_10.py
                fixed  ..................ezFBfont_7x13_num_10.py
               spleen  ...........ezFBfont_spleen_6x12_num_10.py
           schoolbook  ...............ezFBfont_ncenB08_num_10.py (bold)
           schoolbook  ...............ezFBfont_ncenR08_num_10.py (regular)
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_08_num_10.py
   11px:
                fixed  .................ezFBfont_6x13O_num_11.py
                fixed  ..................ezFBfont_6x13_num_11.py
                fixed  .................ezFBfont_6x13B_num_11.py (bold)
                fixed  .................ezFBfont_8x13B_num_11.py (bold)
              pt-sans  .............ezFBfont_PTSans_08_num_11.py
   12px:
              courier  ...............ezFBfont_courB10_num_12.py (bold)
              courier  ...............ezFBfont_courR10_num_12.py (regular)
               spleen  ...........ezFBfont_spleen_8x16_num_12.py
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_09_num_12.py
   13px:
                times  ................ezFBfont_timB10_num_13.py (bold)
                times  ................ezFBfont_timR10_num_13.py (regular)
              courier  ...............ezFBfont_courR12_num_13.py (regular)
                fixed  .................ezFBfont_7x14B_num_13.py (bold)
                fixed  ..................ezFBfont_7x14_num_13.py
                fixed  ..................ezFBfont_9x18_num_13.py
              pt-sans  .............ezFBfont_PTSans_09_num_13.py
              pt-sans  .............ezFBfont_PTSans_10_num_13.py
           schoolbook  ...............ezFBfont_ncenR10_num_13.py (regular)
           schoolbook  ...............ezFBfont_ncenB10_num_13.py (bold)
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_10_num_13.py
   14px:
                times  ................ezFBfont_timR12_num_14.py (regular)
            helvetica  ...............ezFBfont_helvR10_num_14.py (regular)
            helvetica  ...............ezFBfont_helvB10_num_14.py (bold)
                fixed  .................ezFBfont_10x20_num_14.py
                fixed  .................ezFBfont_9x18B_num_14.py (bold)
                fixed  ..................ezFBfont_9x15_num_14.py
                fixed  .................ezFBfont_9x15B_num_14.py (bold)
              pt-sans  .............ezFBfont_PTSans_11_num_14.py
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_11_num_14.py
   15px:
                times  ................ezFBfont_timB12_num_15.py (bold)
              courier  ...............ezFBfont_courB12_num_15.py (bold)
            helvetica  ...............ezFBfont_helvB12_num_15.py (bold)
           schoolbook  ...............ezFBfont_ncenR12_num_15.py (regular)
           schoolbook  ...............ezFBfont_ncenB12_num_15.py (bold)
   16px:
              courier  ...............ezFBfont_courR14_num_16.py (regular)
              courier  ...............ezFBfont_courB14_num_16.py (bold)
            helvetica  ...............ezFBfont_helvR12_num_16.py (regular)
              pt-sans  .............ezFBfont_PTSans_12_num_16.py
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_12_num_16.py
   17px:
                times  ................ezFBfont_timR14_num_17.py (regular)
                times  ................ezFBfont_timB14_num_17.py (bold)
           schoolbook  ...............ezFBfont_ncenR14_num_17.py (regular)
           schoolbook  ...............ezFBfont_ncenB14_num_17.py (bold)
   18px:
            helvetica  ...............ezFBfont_helvB14_num_18.py (bold)
            helvetica  ...............ezFBfont_helvR14_num_18.py (regular)
              pt-sans  .............ezFBfont_PTSans_14_num_18.py
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_14_num_18.py
   19px:
              courier  ...............ezFBfont_courR18_num_19.py (regular)
   20px:
               spleen  ..........ezFBfont_spleen_12x24_num_20.py
   21px:
              courier  ...............ezFBfont_courB18_num_21.py (bold)
              pt-sans  .............ezFBfont_PTSans_16_num_21.py
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_16_num_21.py
   22px:
                times  ................ezFBfont_timB18_num_22.py (bold)
                times  ................ezFBfont_timR18_num_22.py (regular)
           schoolbook  ...............ezFBfont_ncenB18_num_22.py (bold)
           schoolbook  ...............ezFBfont_ncenR18_num_22.py (regular)
   23px:
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_18_num_23.py
   24px:
            helvetica  ...............ezFBfont_helvR18_num_24.py (regular)
            helvetica  ...............ezFBfont_helvB18_num_24.py (bold)
              pt-sans  .............ezFBfont_PTSans_18_num_24.py
   26px:
              courier  ...............ezFBfont_courR24_num_26.py (regular)
               spleen  ..........ezFBfont_spleen_16x32_num_26.py
              pt-sans  .............ezFBfont_PTSans_20_num_26.py
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_20_num_26.py
   28px:
                times  ................ezFBfont_timR24_num_28.py (regular)
              courier  ...............ezFBfont_courB24_num_28.py (bold)
   30px:
              pt-sans  .............ezFBfont_PTSans_24_num_30.py
           schoolbook  ...............ezFBfont_ncenB24_num_30.py (bold)
   31px:
                times  ................ezFBfont_timB24_num_31.py (bold)
            helvetica  ...............ezFBfont_helvB24_num_31.py (bold)
           schoolbook  ...............ezFBfont_ncenR24_num_31.py (regular)
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_24_num_31.py
   33px:
            helvetica  ...............ezFBfont_helvR24_num_33.py (regular)
   36px:
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_28_num_36.py
   37px:
              pt-sans  .............ezFBfont_PTSans_28_num_37.py
   41px:
              pt-sans  .............ezFBfont_PTSans_32_num_41.py
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_32_num_41.py
   47px:
              pt-sans  .............ezFBfont_PTSans_36_num_47.py
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_36_num_47.py
   54px:
              pt-sans  .............ezFBfont_PTSans_42_num_54.py
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_42_num_54.py
   56px:
               spleen  ..........ezFBfont_spleen_32x64_num_56.py
   62px:
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_48_num_62.py
   63px:
              pt-sans  .............ezFBfont_PTSans_48_num_63.py
   73px:
              pt-sans  .............ezFBfont_PTSans_56_num_73.py
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_56_num_73.py
   83px:
       pt-sans-narrow  .......ezFBfont_PTSansNarrow_64_num_83.py
   84px:
              pt-sans  .............ezFBfont_PTSans_64_num_84.py

Uppercase character set
-----------------------
Size:          Family                                       Name
    5px:
              generic  ...............ezFBfont_micro_upper_05.py
                fixed  ...........ezFBfont_tom_thumb_upper_05.py
    6px:
                tiny5  .......ezFBfont_tiny5_Regular_upper_06.py (regular)
                fixed  .................ezFBfont_4x6_upper_06.py
    7px:
                fixed  .................ezFBfont_5x7_upper_07.py
    8px:
          amstrad-cpc  ezFBfont_amstrad_cpc_extended_upper_08.py
                fixed  ................ezFBfont_6x10_upper_08.py
                fixed  .................ezFBfont_5x8_upper_08.py
               spleen  ..........ezFBfont_spleen_5x8_upper_08.py
              pt-sans  ...........ezFBfont_PTSans_06_upper_08.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_06_upper_08.py
    9px:
                fixed  .................ezFBfont_6x9_upper_09.py
   10px:
              courier  .............ezFBfont_courR08_upper_10.py (regular)
              courier  .............ezFBfont_courB08_upper_10.py (bold)
                fixed  ...............ezFBfont_7x13B_upper_10.py (bold)
                fixed  ................ezFBfont_8x13_upper_10.py
                fixed  ...............ezFBfont_8x13O_upper_10.py
                fixed  ................ezFBfont_6x12_upper_10.py
               spleen  .........ezFBfont_spleen_6x12_upper_10.py
   11px:
                times  ..............ezFBfont_timR08_upper_11.py (regular)
                times  ..............ezFBfont_timB08_upper_11.py (bold)
            helvetica  .........ezFBfont_helvB08_gps_upper_11.py (bold)
            helvetica  .............ezFBfont_helvB08_upper_11.py (bold)
            helvetica  .............ezFBfont_helvR08_upper_11.py (regular)
                fixed  ...............ezFBfont_8x13B_upper_11.py (bold)
                fixed  ...............ezFBfont_7x13O_upper_11.py
                fixed  ................ezFBfont_7x13_upper_11.py
                fixed  ...............ezFBfont_6x13O_upper_11.py
                fixed  ................ezFBfont_6x13_upper_11.py
                fixed  ...............ezFBfont_6x13B_upper_11.py (bold)
              pt-sans  ...........ezFBfont_PTSans_07_upper_11.py
           schoolbook  .............ezFBfont_ncenB08_upper_11.py (bold)
           schoolbook  .............ezFBfont_ncenR08_upper_11.py (regular)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_07_upper_11.py
   12px:
              pt-sans  ...........ezFBfont_PTSans_08_upper_12.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_08_upper_12.py
   13px:
              courier  .............ezFBfont_courB10_upper_13.py (bold)
                fixed  ................ezFBfont_9x18_upper_13.py
                fixed  ...............ezFBfont_9x18B_upper_13.py (bold)
                fixed  ................ezFBfont_7x14_upper_13.py
              pt-sans  ...........ezFBfont_PTSans_09_upper_13.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_09_upper_13.py
   14px:
                times  ..............ezFBfont_timR10_upper_14.py (regular)
                times  ..............ezFBfont_timB10_upper_14.py (bold)
              courier  .............ezFBfont_courR10_upper_14.py (regular)
                fixed  ...............ezFBfont_9x15B_upper_14.py (bold)
                fixed  ...............ezFBfont_10x20_upper_14.py
                fixed  ................ezFBfont_9x15_upper_14.py
                fixed  ...............ezFBfont_7x14B_upper_14.py (bold)
               spleen  .........ezFBfont_spleen_8x16_upper_14.py
              pt-sans  ...........ezFBfont_PTSans_10_upper_14.py
           schoolbook  .............ezFBfont_ncenR10_upper_14.py (regular)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_10_upper_14.py
   15px:
                times  ..............ezFBfont_timR12_upper_15.py (regular)
              courier  .............ezFBfont_courB12_upper_15.py (bold)
              courier  .............ezFBfont_courR12_upper_15.py (regular)
            helvetica  .............ezFBfont_helvB10_upper_15.py (bold)
            helvetica  .............ezFBfont_helvR10_upper_15.py (regular)
              pt-sans  ...........ezFBfont_PTSans_11_upper_15.py
           schoolbook  .............ezFBfont_ncenB10_upper_15.py (bold)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_11_upper_15.py
   16px:
                times  ..............ezFBfont_timB12_upper_16.py (bold)
            helvetica  .............ezFBfont_helvB12_upper_16.py (bold)
           schoolbook  .............ezFBfont_ncenR12_upper_16.py (regular)
   17px:
              courier  .............ezFBfont_courR14_upper_17.py (regular)
              courier  .............ezFBfont_courB14_upper_17.py (bold)
            helvetica  .............ezFBfont_helvR12_upper_17.py (regular)
           schoolbook  .............ezFBfont_ncenB12_upper_17.py (bold)
   18px:
                times  ..............ezFBfont_timB14_upper_18.py (bold)
                times  ..............ezFBfont_timR14_upper_18.py (regular)
            helvetica  .............ezFBfont_helvB14_upper_18.py (bold)
            helvetica  .............ezFBfont_helvR14_upper_18.py (regular)
              pt-sans  ...........ezFBfont_PTSans_12_upper_18.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_12_upper_18.py
   19px:
           schoolbook  .............ezFBfont_ncenR14_upper_19.py (regular)
   20px:
              pt-sans  ...........ezFBfont_PTSans_14_upper_20.py
           schoolbook  .............ezFBfont_ncenB14_upper_20.py (bold)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_14_upper_20.py
   21px:
              courier  .............ezFBfont_courB18_upper_21.py (bold)
   22px:
              courier  .............ezFBfont_courR18_upper_22.py (regular)
               spleen  ........ezFBfont_spleen_12x24_upper_22.py
   23px:
                times  ..............ezFBfont_timB18_upper_23.py (bold)
              pt-sans  ...........ezFBfont_PTSans_16_upper_23.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_16_upper_23.py
   24px:
                times  ..............ezFBfont_timR18_upper_24.py (regular)
            helvetica  .............ezFBfont_helvB18_upper_24.py (bold)
           schoolbook  .............ezFBfont_ncenR18_upper_24.py (regular)
   25px:
            helvetica  .............ezFBfont_helvR18_upper_25.py (regular)
           schoolbook  .............ezFBfont_ncenB18_upper_25.py (bold)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_18_upper_25.py
   26px:
              pt-sans  ...........ezFBfont_PTSans_18_upper_26.py
   28px:
              courier  .............ezFBfont_courR24_upper_28.py (regular)
               spleen  ........ezFBfont_spleen_16x32_upper_28.py
              pt-sans  ...........ezFBfont_PTSans_20_upper_28.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_20_upper_28.py
   30px:
              courier  .............ezFBfont_courB24_upper_30.py (bold)
   31px:
                times  ..............ezFBfont_timR24_upper_31.py (regular)
            helvetica  .............ezFBfont_helvB24_upper_31.py (bold)
   32px:
                times  ..............ezFBfont_timB24_upper_32.py (bold)
           schoolbook  .............ezFBfont_ncenB24_upper_32.py (bold)
   33px:
           schoolbook  .............ezFBfont_ncenR24_upper_33.py (regular)
   34px:
            helvetica  .............ezFBfont_helvR24_upper_34.py (regular)
              pt-sans  ...........ezFBfont_PTSans_24_upper_34.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_24_upper_34.py
   39px:
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_28_upper_39.py
   40px:
              pt-sans  ...........ezFBfont_PTSans_28_upper_40.py
   45px:
              pt-sans  ...........ezFBfont_PTSans_32_upper_45.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_32_upper_45.py
   51px:
              pt-sans  ...........ezFBfont_PTSans_36_upper_51.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_36_upper_51.py
   56px:
               spleen  ........ezFBfont_spleen_32x64_upper_56.py
   59px:
              pt-sans  ...........ezFBfont_PTSans_42_upper_59.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_42_upper_59.py
   69px:
              pt-sans  ...........ezFBfont_PTSans_48_upper_69.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_48_upper_69.py
   80px:
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_56_upper_80.py
   81px:
              pt-sans  ...........ezFBfont_PTSans_56_upper_81.py
   91px:
              pt-sans  ...........ezFBfont_PTSans_64_upper_91.py
   92px:
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_64_upper_92.py

Ascii character set
-------------------
Size:          Family                                       Name
    5px:
              generic  ...............ezFBfont_micro_ascii_05.py
    6px:
                fixed  .................ezFBfont_4x6_ascii_06.py
                fixed  ...........ezFBfont_tom_thumb_ascii_06.py
    7px:
                tiny5  .......ezFBfont_tiny5_Regular_ascii_07.py (regular)
                fixed  .................ezFBfont_5x7_ascii_07.py
    8px:
          amstrad-cpc  ezFBfont_amstrad_cpc_extended_ascii_08.py
                fixed  .................ezFBfont_5x8_ascii_08.py
               spleen  ..........ezFBfont_spleen_5x8_ascii_08.py
              pt-sans  ...........ezFBfont_PTSans_06_ascii_08.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_06_ascii_08.py
    9px:
                fixed  .................ezFBfont_6x9_ascii_09.py
   10px:
              courier  .............ezFBfont_courR08_ascii_10.py (regular)
              courier  .............ezFBfont_courB08_ascii_10.py (bold)
                fixed  ................ezFBfont_6x12_ascii_10.py
                fixed  ................ezFBfont_6x10_ascii_10.py
   11px:
                times  ..............ezFBfont_timB08_ascii_11.py (bold)
                times  ..............ezFBfont_timR08_ascii_11.py (regular)
            helvetica  .........ezFBfont_helvB08_gps_ascii_11.py (bold)
            helvetica  .............ezFBfont_helvR08_ascii_11.py (regular)
            helvetica  .............ezFBfont_helvB08_ascii_11.py (bold)
              pt-sans  ...........ezFBfont_PTSans_07_ascii_11.py
           schoolbook  .............ezFBfont_ncenR08_ascii_11.py (regular)
           schoolbook  .............ezFBfont_ncenB08_ascii_11.py (bold)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_07_ascii_11.py
   12px:
                fixed  ................ezFBfont_6x13_ascii_12.py
                fixed  ...............ezFBfont_7x13O_ascii_12.py
                fixed  ...............ezFBfont_6x13O_ascii_12.py
                fixed  ................ezFBfont_8x13_ascii_12.py
                fixed  ...............ezFBfont_8x13O_ascii_12.py
                fixed  ...............ezFBfont_7x13B_ascii_12.py (bold)
                fixed  ................ezFBfont_7x13_ascii_12.py
                fixed  ...............ezFBfont_6x13B_ascii_12.py (bold)
                fixed  ...............ezFBfont_8x13B_ascii_12.py (bold)
               spleen  .........ezFBfont_spleen_6x12_ascii_12.py
              pt-sans  ...........ezFBfont_PTSans_08_ascii_12.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_08_ascii_12.py
   13px:
                fixed  ................ezFBfont_7x14_ascii_13.py
              pt-sans  ...........ezFBfont_PTSans_09_ascii_13.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_09_ascii_13.py
   14px:
                times  ..............ezFBfont_timB10_ascii_14.py (bold)
                times  ..............ezFBfont_timR10_ascii_14.py (regular)
              courier  .............ezFBfont_courR10_ascii_14.py (regular)
              courier  .............ezFBfont_courB10_ascii_14.py (bold)
                fixed  ................ezFBfont_9x15_ascii_14.py
                fixed  ...............ezFBfont_9x15B_ascii_14.py (bold)
                fixed  ...............ezFBfont_7x14B_ascii_14.py (bold)
               spleen  .........ezFBfont_spleen_8x16_ascii_14.py
              pt-sans  ...........ezFBfont_PTSans_10_ascii_14.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_10_ascii_14.py
   15px:
              courier  .............ezFBfont_courR12_ascii_15.py (regular)
              courier  .............ezFBfont_courB12_ascii_15.py (bold)
            helvetica  .............ezFBfont_helvB10_ascii_15.py (bold)
            helvetica  .............ezFBfont_helvR10_ascii_15.py (regular)
              pt-sans  ...........ezFBfont_PTSans_11_ascii_15.py
           schoolbook  .............ezFBfont_ncenR10_ascii_15.py (regular)
           schoolbook  .............ezFBfont_ncenB10_ascii_15.py (bold)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_11_ascii_15.py
   16px:
                times  ..............ezFBfont_timR12_ascii_16.py (regular)
                times  ..............ezFBfont_timB12_ascii_16.py (bold)
                fixed  ................ezFBfont_9x18_ascii_16.py
                fixed  ...............ezFBfont_9x18B_ascii_16.py (bold)
           schoolbook  .............ezFBfont_ncenR12_ascii_16.py (regular)
   17px:
              courier  .............ezFBfont_courR14_ascii_17.py (regular)
              courier  .............ezFBfont_courB14_ascii_17.py (bold)
            helvetica  .............ezFBfont_helvR12_ascii_17.py (regular)
            helvetica  .............ezFBfont_helvB12_ascii_17.py (bold)
                fixed  ...............ezFBfont_10x20_ascii_17.py
           schoolbook  .............ezFBfont_ncenB12_ascii_17.py (bold)
   18px:
                times  ..............ezFBfont_timB14_ascii_18.py (bold)
                times  ..............ezFBfont_timR14_ascii_18.py (regular)
            helvetica  .............ezFBfont_helvB14_ascii_18.py (bold)
            helvetica  .............ezFBfont_helvR14_ascii_18.py (regular)
              pt-sans  ...........ezFBfont_PTSans_12_ascii_18.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_12_ascii_18.py
   19px:
           schoolbook  .............ezFBfont_ncenR14_ascii_19.py (regular)
   20px:
              pt-sans  ...........ezFBfont_PTSans_14_ascii_20.py
           schoolbook  .............ezFBfont_ncenB14_ascii_20.py (bold)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_14_ascii_20.py
   22px:
              courier  .............ezFBfont_courB18_ascii_22.py (bold)
              courier  .............ezFBfont_courR18_ascii_22.py (regular)
   23px:
                times  ..............ezFBfont_timB18_ascii_23.py (bold)
               spleen  ........ezFBfont_spleen_12x24_ascii_23.py
              pt-sans  ...........ezFBfont_PTSans_16_ascii_23.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_16_ascii_23.py
   24px:
            helvetica  .............ezFBfont_helvB18_ascii_24.py (bold)
   25px:
                times  ..............ezFBfont_timR18_ascii_25.py (regular)
            helvetica  .............ezFBfont_helvR18_ascii_25.py (regular)
           schoolbook  .............ezFBfont_ncenB18_ascii_25.py (bold)
           schoolbook  .............ezFBfont_ncenR18_ascii_25.py (regular)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_18_ascii_25.py
   26px:
              pt-sans  ...........ezFBfont_PTSans_18_ascii_26.py
   28px:
              courier  .............ezFBfont_courR24_ascii_28.py (regular)
              pt-sans  ...........ezFBfont_PTSans_20_ascii_28.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_20_ascii_28.py
   30px:
              courier  .............ezFBfont_courB24_ascii_30.py (bold)
               spleen  ........ezFBfont_spleen_16x32_ascii_30.py
   32px:
                times  ..............ezFBfont_timR24_ascii_32.py (regular)
            helvetica  .............ezFBfont_helvB24_ascii_32.py (bold)
   33px:
                times  ..............ezFBfont_timB24_ascii_33.py (bold)
           schoolbook  .............ezFBfont_ncenB24_ascii_33.py (bold)
   34px:
            helvetica  .............ezFBfont_helvR24_ascii_34.py (regular)
              pt-sans  ...........ezFBfont_PTSans_24_ascii_34.py
           schoolbook  .............ezFBfont_ncenR24_ascii_34.py (regular)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_24_ascii_34.py
   39px:
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_28_ascii_39.py
   40px:
              pt-sans  ...........ezFBfont_PTSans_28_ascii_40.py
   45px:
              pt-sans  ...........ezFBfont_PTSans_32_ascii_45.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_32_ascii_45.py
   51px:
              pt-sans  ...........ezFBfont_PTSans_36_ascii_51.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_36_ascii_51.py
   59px:
              pt-sans  ...........ezFBfont_PTSans_42_ascii_59.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_42_ascii_59.py
   60px:
               spleen  ........ezFBfont_spleen_32x64_ascii_60.py
   69px:
              pt-sans  ...........ezFBfont_PTSans_48_ascii_69.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_48_ascii_69.py
   80px:
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_56_ascii_80.py
   81px:
              pt-sans  ...........ezFBfont_PTSans_56_ascii_81.py
   91px:
              pt-sans  ...........ezFBfont_PTSans_64_ascii_91.py
   92px:
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_64_ascii_92.py

Supplemental character set
--------------------------
Size:          Family                                       Name
    1px:
               spleen  ...........ezFBfont_spleen_5x8_supp_01.py
    6px:
                fixed  ..................ezFBfont_4x6_supp_06.py
                fixed  ............ezFBfont_tom_thumb_supp_06.py
    7px:
                fixed  ..................ezFBfont_5x7_supp_07.py
    8px:
          amstrad-cpc  .ezFBfont_amstrad_cpc_extended_supp_08.py
                fixed  ..................ezFBfont_5x8_supp_08.py
    9px:
                tiny5  ........ezFBfont_tiny5_Regular_supp_09.py (regular)
                fixed  ..................ezFBfont_6x9_supp_09.py
              pt-sans  ............ezFBfont_PTSans_06_supp_09.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_06_supp_09.py
   10px:
                fixed  .................ezFBfont_6x10_supp_10.py
   11px:
              courier  ..............ezFBfont_courR08_supp_11.py (regular)
              courier  ..............ezFBfont_courB08_supp_11.py (bold)
   12px:
                fixed  ................ezFBfont_8x13O_supp_12.py
                fixed  ................ezFBfont_6x13B_supp_12.py (bold)
                fixed  .................ezFBfont_8x13_supp_12.py
                fixed  .................ezFBfont_6x13_supp_12.py
                fixed  .................ezFBfont_7x13_supp_12.py
                fixed  ................ezFBfont_7x13B_supp_12.py (bold)
                fixed  ................ezFBfont_6x13O_supp_12.py
                fixed  .................ezFBfont_6x12_supp_12.py
                fixed  ................ezFBfont_7x13O_supp_12.py
               spleen  ..........ezFBfont_spleen_6x12_supp_12.py
              pt-sans  ............ezFBfont_PTSans_07_supp_12.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_07_supp_12.py
   13px:
                times  ...............ezFBfont_timR08_supp_13.py (regular)
                times  ...............ezFBfont_timB08_supp_13.py (bold)
            helvetica  ..............ezFBfont_helvR08_supp_13.py (regular)
            helvetica  ..............ezFBfont_helvB08_supp_13.py (bold)
                fixed  ................ezFBfont_8x13B_supp_13.py (bold)
              pt-sans  ............ezFBfont_PTSans_08_supp_13.py
           schoolbook  ..............ezFBfont_ncenB08_supp_13.py (bold)
           schoolbook  ..............ezFBfont_ncenR08_supp_13.py (regular)
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_08_supp_13.py
   14px:
                fixed  .................ezFBfont_7x14_supp_14.py
                fixed  ................ezFBfont_7x14B_supp_14.py (bold)
   15px:
              courier  ..............ezFBfont_courR10_supp_15.py (regular)
                fixed  .................ezFBfont_9x15_supp_15.py
                fixed  ................ezFBfont_9x15B_supp_15.py (bold)
               spleen  ..........ezFBfont_spleen_8x16_supp_15.py
              pt-sans  ............ezFBfont_PTSans_09_supp_15.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_09_supp_15.py
   16px:
              courier  ..............ezFBfont_courB10_supp_16.py (bold)
              pt-sans  ............ezFBfont_PTSans_10_supp_16.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_10_supp_16.py
   17px:
                times  ...............ezFBfont_timR10_supp_17.py (regular)
                times  ...............ezFBfont_timB10_supp_17.py (bold)
              courier  ..............ezFBfont_courB12_supp_17.py (bold)
              courier  ..............ezFBfont_courR12_supp_17.py (regular)
            helvetica  ..............ezFBfont_helvR10_supp_17.py (regular)
            helvetica  ..............ezFBfont_helvB10_supp_17.py (bold)
                fixed  .................ezFBfont_9x18_supp_17.py
              pt-sans  ............ezFBfont_PTSans_11_supp_17.py
           schoolbook  ..............ezFBfont_ncenR10_supp_17.py (regular)
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_11_supp_17.py
   18px:
                fixed  ................ezFBfont_9x18B_supp_18.py (bold)
           schoolbook  ..............ezFBfont_ncenB10_supp_18.py (bold)
   19px:
                times  ...............ezFBfont_timR12_supp_19.py (regular)
              courier  ..............ezFBfont_courR14_supp_19.py (regular)
              pt-sans  ............ezFBfont_PTSans_12_supp_19.py
           schoolbook  ..............ezFBfont_ncenR12_supp_19.py (regular)
           schoolbook  ..............ezFBfont_ncenB12_supp_19.py (bold)
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_12_supp_19.py
   20px:
                times  ...............ezFBfont_timB12_supp_20.py (bold)
              courier  ..............ezFBfont_courB14_supp_20.py (bold)
            helvetica  ..............ezFBfont_helvR12_supp_20.py (regular)
            helvetica  ..............ezFBfont_helvB12_supp_20.py (bold)
                fixed  ................ezFBfont_10x20_supp_20.py
   21px:
                times  ...............ezFBfont_timB14_supp_21.py (bold)
   22px:
                times  ...............ezFBfont_timR14_supp_22.py (regular)
            helvetica  ..............ezFBfont_helvR14_supp_22.py (regular)
              pt-sans  ............ezFBfont_PTSans_14_supp_22.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_14_supp_22.py
   23px:
            helvetica  ..............ezFBfont_helvB14_supp_23.py (bold)
           schoolbook  ..............ezFBfont_ncenB14_supp_23.py (bold)
           schoolbook  ..............ezFBfont_ncenR14_supp_23.py (regular)
   24px:
              courier  ..............ezFBfont_courR18_supp_24.py (regular)
               spleen  .........ezFBfont_spleen_12x24_supp_24.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_16_supp_24.py
   25px:
              pt-sans  ............ezFBfont_PTSans_16_supp_25.py
   26px:
              courier  ..............ezFBfont_courB18_supp_26.py (bold)
   27px:
              pt-sans  ............ezFBfont_PTSans_18_supp_27.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_18_supp_27.py
   29px:
                times  ...............ezFBfont_timR18_supp_29.py (regular)
                times  ...............ezFBfont_timB18_supp_29.py (bold)
            helvetica  ..............ezFBfont_helvR18_supp_29.py (regular)
            helvetica  ..............ezFBfont_helvB18_supp_29.py (bold)
           schoolbook  ..............ezFBfont_ncenR18_supp_29.py (regular)
           schoolbook  ..............ezFBfont_ncenB18_supp_29.py (bold)
   30px:
              pt-sans  ............ezFBfont_PTSans_20_supp_30.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_20_supp_30.py
   32px:
              courier  ..............ezFBfont_courR24_supp_32.py (regular)
               spleen  .........ezFBfont_spleen_16x32_supp_32.py
   33px:
              courier  ..............ezFBfont_courB24_supp_33.py (bold)
   35px:
              pt-sans  ............ezFBfont_PTSans_24_supp_35.py
   36px:
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_24_supp_36.py
   37px:
                times  ...............ezFBfont_timR24_supp_37.py (regular)
                times  ...............ezFBfont_timB24_supp_37.py (bold)
   38px:
            helvetica  ..............ezFBfont_helvB24_supp_38.py (bold)
            helvetica  ..............ezFBfont_helvR24_supp_38.py (regular)
   39px:
           schoolbook  ..............ezFBfont_ncenR24_supp_39.py (regular)
   40px:
           schoolbook  ..............ezFBfont_ncenB24_supp_40.py (bold)
   42px:
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_28_supp_42.py
   43px:
              pt-sans  ............ezFBfont_PTSans_28_supp_43.py
   47px:
              pt-sans  ............ezFBfont_PTSans_32_supp_47.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_32_supp_47.py
   54px:
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_36_supp_54.py
   55px:
              pt-sans  ............ezFBfont_PTSans_36_supp_55.py
   63px:
              pt-sans  ............ezFBfont_PTSans_42_supp_63.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_42_supp_63.py
   64px:
               spleen  .........ezFBfont_spleen_32x64_supp_64.py
   72px:
              pt-sans  ............ezFBfont_PTSans_48_supp_72.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_48_supp_72.py
   85px:
              pt-sans  ............ezFBfont_PTSans_56_supp_85.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_56_supp_85.py
   97px:
              pt-sans  ............ezFBfont_PTSans_64_supp_97.py
       pt-sans-narrow  ......ezFBfont_PTSansNarrow_64_supp_97.py

Latin-1 character set
---------------------
Size:          Family                                       Name
    6px:
                fixed  .................ezFBfont_4x6_latin_06.py
                fixed  ...........ezFBfont_tom_thumb_latin_06.py
    7px:
                fixed  .................ezFBfont_5x7_latin_07.py
    8px:
          amstrad-cpc  ezFBfont_amstrad_cpc_extended_latin_08.py
                fixed  .................ezFBfont_5x8_latin_08.py
               spleen  ..........ezFBfont_spleen_5x8_latin_08.py
    9px:
                tiny5  .......ezFBfont_tiny5_Regular_latin_09.py (regular)
                fixed  .................ezFBfont_6x9_latin_09.py
              pt-sans  ...........ezFBfont_PTSans_06_latin_09.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_06_latin_09.py
   10px:
                fixed  ................ezFBfont_6x10_latin_10.py
   11px:
              courier  .............ezFBfont_courR08_latin_11.py (regular)
              courier  .............ezFBfont_courB08_latin_11.py (bold)
   12px:
                fixed  ...............ezFBfont_8x13O_latin_12.py
                fixed  ................ezFBfont_6x12_latin_12.py
                fixed  ................ezFBfont_7x13_latin_12.py
                fixed  ...............ezFBfont_6x13O_latin_12.py
                fixed  ...............ezFBfont_7x13B_latin_12.py (bold)
                fixed  ...............ezFBfont_7x13O_latin_12.py
                fixed  ................ezFBfont_8x13_latin_12.py
                fixed  ................ezFBfont_6x13_latin_12.py
                fixed  ...............ezFBfont_6x13B_latin_12.py (bold)
               spleen  .........ezFBfont_spleen_6x12_latin_12.py
   13px:
                times  ..............ezFBfont_timR08_latin_13.py (regular)
                times  ..............ezFBfont_timB08_latin_13.py (bold)
            helvetica  .............ezFBfont_helvB08_latin_13.py (bold)
            helvetica  .............ezFBfont_helvR08_latin_13.py (regular)
                fixed  ...............ezFBfont_8x13B_latin_13.py (bold)
              pt-sans  ...........ezFBfont_PTSans_07_latin_13.py
           schoolbook  .............ezFBfont_ncenB08_latin_13.py (bold)
           schoolbook  .............ezFBfont_ncenR08_latin_13.py (regular)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_07_latin_13.py
   14px:
                fixed  ...............ezFBfont_7x14B_latin_14.py (bold)
                fixed  ................ezFBfont_7x14_latin_14.py
              pt-sans  ...........ezFBfont_PTSans_08_latin_14.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_08_latin_14.py
   15px:
              courier  .............ezFBfont_courR10_latin_15.py (regular)
                fixed  ................ezFBfont_9x15_latin_15.py
                fixed  ...............ezFBfont_9x15B_latin_15.py (bold)
               spleen  .........ezFBfont_spleen_8x16_latin_15.py
              pt-sans  ...........ezFBfont_PTSans_09_latin_15.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_09_latin_15.py
   16px:
              courier  .............ezFBfont_courB10_latin_16.py (bold)
              pt-sans  ...........ezFBfont_PTSans_10_latin_16.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_10_latin_16.py
   17px:
                times  ..............ezFBfont_timB10_latin_17.py (bold)
                times  ..............ezFBfont_timR10_latin_17.py (regular)
              courier  .............ezFBfont_courR12_latin_17.py (regular)
              courier  .............ezFBfont_courB12_latin_17.py (bold)
            helvetica  .............ezFBfont_helvB10_latin_17.py (bold)
            helvetica  .............ezFBfont_helvR10_latin_17.py (regular)
                fixed  ................ezFBfont_9x18_latin_17.py
              pt-sans  ...........ezFBfont_PTSans_11_latin_17.py
           schoolbook  .............ezFBfont_ncenR10_latin_17.py (regular)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_11_latin_17.py
   18px:
                fixed  ...............ezFBfont_9x18B_latin_18.py (bold)
           schoolbook  .............ezFBfont_ncenB10_latin_18.py (bold)
   19px:
                times  ..............ezFBfont_timR12_latin_19.py (regular)
              courier  .............ezFBfont_courR14_latin_19.py (regular)
              pt-sans  ...........ezFBfont_PTSans_12_latin_19.py
           schoolbook  .............ezFBfont_ncenB12_latin_19.py (bold)
           schoolbook  .............ezFBfont_ncenR12_latin_19.py (regular)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_12_latin_19.py
   20px:
                times  ..............ezFBfont_timB12_latin_20.py (bold)
              courier  .............ezFBfont_courB14_latin_20.py (bold)
            helvetica  .............ezFBfont_helvB12_latin_20.py (bold)
            helvetica  .............ezFBfont_helvR12_latin_20.py (regular)
                fixed  ...............ezFBfont_10x20_latin_20.py
   21px:
                times  ..............ezFBfont_timB14_latin_21.py (bold)
   22px:
                times  ..............ezFBfont_timR14_latin_22.py (regular)
            helvetica  .............ezFBfont_helvR14_latin_22.py (regular)
              pt-sans  ...........ezFBfont_PTSans_14_latin_22.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_14_latin_22.py
   23px:
            helvetica  .............ezFBfont_helvB14_latin_23.py (bold)
           schoolbook  .............ezFBfont_ncenR14_latin_23.py (regular)
           schoolbook  .............ezFBfont_ncenB14_latin_23.py (bold)
   24px:
              courier  .............ezFBfont_courR18_latin_24.py (regular)
               spleen  ........ezFBfont_spleen_12x24_latin_24.py
   25px:
              pt-sans  ...........ezFBfont_PTSans_16_latin_25.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_16_latin_25.py
   26px:
              courier  .............ezFBfont_courB18_latin_26.py (bold)
   27px:
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_18_latin_27.py
   28px:
              pt-sans  ...........ezFBfont_PTSans_18_latin_28.py
   29px:
                times  ..............ezFBfont_timB18_latin_29.py (bold)
                times  ..............ezFBfont_timR18_latin_29.py (regular)
            helvetica  .............ezFBfont_helvB18_latin_29.py (bold)
            helvetica  .............ezFBfont_helvR18_latin_29.py (regular)
           schoolbook  .............ezFBfont_ncenB18_latin_29.py (bold)
           schoolbook  .............ezFBfont_ncenR18_latin_29.py (regular)
   30px:
              pt-sans  ...........ezFBfont_PTSans_20_latin_30.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_20_latin_30.py
   32px:
              courier  .............ezFBfont_courR24_latin_32.py (regular)
               spleen  ........ezFBfont_spleen_16x32_latin_32.py
   33px:
              courier  .............ezFBfont_courB24_latin_33.py (bold)
   36px:
              pt-sans  ...........ezFBfont_PTSans_24_latin_36.py
   37px:
                times  ..............ezFBfont_timR24_latin_37.py (regular)
                times  ..............ezFBfont_timB24_latin_37.py (bold)
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_24_latin_37.py
   38px:
            helvetica  .............ezFBfont_helvR24_latin_38.py (regular)
            helvetica  .............ezFBfont_helvB24_latin_38.py (bold)
   39px:
           schoolbook  .............ezFBfont_ncenR24_latin_39.py (regular)
   40px:
           schoolbook  .............ezFBfont_ncenB24_latin_40.py (bold)
   42px:
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_28_latin_42.py
   44px:
              pt-sans  ...........ezFBfont_PTSans_28_latin_44.py
   48px:
              pt-sans  ...........ezFBfont_PTSans_32_latin_48.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_32_latin_48.py
   56px:
              pt-sans  ...........ezFBfont_PTSans_36_latin_56.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_36_latin_56.py
   64px:
               spleen  ........ezFBfont_spleen_32x64_latin_64.py
              pt-sans  ...........ezFBfont_PTSans_42_latin_64.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_42_latin_64.py
   73px:
              pt-sans  ...........ezFBfont_PTSans_48_latin_73.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_48_latin_73.py
   86px:
              pt-sans  ...........ezFBfont_PTSans_56_latin_86.py
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_56_latin_86.py
   98px:
              pt-sans  ...........ezFBfont_PTSans_64_latin_98.py
   99px:
       pt-sans-narrow  .....ezFBfont_PTSansNarrow_64_latin_99.py

Full character set
------------------
Size:          Family                                       Name
    5px:
              generic  ................ezFBfont_micro_full_05.py
    6px:
                fixed  ..................ezFBfont_4x6_full_06.py
    7px:
                fixed  ..................ezFBfont_5x7_full_07.py
    8px:
          amstrad-cpc  .ezFBfont_amstrad_cpc_extended_full_08.py
                fixed  ..................ezFBfont_5x8_full_08.py
               spleen  ...........ezFBfont_spleen_5x8_full_08.py
    9px:
                fixed  ..................ezFBfont_6x9_full_09.py
   10px:
                fixed  .................ezFBfont_6x10_full_10.py
   11px:
              courier  ..............ezFBfont_courR08_full_11.py (regular)
              courier  ..............ezFBfont_courB08_full_11.py (bold)
            helvetica  ..........ezFBfont_helvB08_gps_full_11.py (bold)
   12px:
                fixed  .................ezFBfont_6x13_full_12.py
                fixed  ................ezFBfont_8x13O_full_12.py
                fixed  .................ezFBfont_6x12_full_12.py
                fixed  .................ezFBfont_7x13_full_12.py
                fixed  ................ezFBfont_7x13O_full_12.py
                fixed  ................ezFBfont_6x13B_full_12.py (bold)
                fixed  .................ezFBfont_8x13_full_12.py
                fixed  ................ezFBfont_7x13B_full_12.py (bold)
                fixed  ................ezFBfont_6x13O_full_12.py
               spleen  ..........ezFBfont_spleen_6x12_full_12.py
   13px:
                times  ...............ezFBfont_timB08_full_13.py (bold)
                times  ...............ezFBfont_timR08_full_13.py (regular)
            helvetica  ..............ezFBfont_helvR08_full_13.py (regular)
            helvetica  ..............ezFBfont_helvB08_full_13.py (bold)
                fixed  ................ezFBfont_8x13B_full_13.py (bold)
           schoolbook  ..............ezFBfont_ncenB08_full_13.py (bold)
           schoolbook  ..............ezFBfont_ncenR08_full_13.py (regular)
   14px:
                fixed  ................ezFBfont_7x14B_full_14.py (bold)
                fixed  .................ezFBfont_7x14_full_14.py
   15px:
              courier  ..............ezFBfont_courR10_full_15.py (regular)
                fixed  ................ezFBfont_9x15B_full_15.py (bold)
                fixed  .................ezFBfont_9x15_full_15.py
               spleen  ..........ezFBfont_spleen_8x16_full_15.py
   16px:
              courier  ..............ezFBfont_courB10_full_16.py (bold)
   17px:
                times  ...............ezFBfont_timR10_full_17.py (regular)
                times  ...............ezFBfont_timB10_full_17.py (bold)
              courier  ..............ezFBfont_courB12_full_17.py (bold)
              courier  ..............ezFBfont_courR12_full_17.py (regular)
            helvetica  ..............ezFBfont_helvB10_full_17.py (bold)
            helvetica  ..............ezFBfont_helvR10_full_17.py (regular)
                fixed  .................ezFBfont_9x18_full_17.py
           schoolbook  ..............ezFBfont_ncenR10_full_17.py (regular)
   18px:
                fixed  ................ezFBfont_9x18B_full_18.py (bold)
           schoolbook  ..............ezFBfont_ncenB10_full_18.py (bold)
   19px:
                times  ...............ezFBfont_timR12_full_19.py (regular)
              courier  ..............ezFBfont_courR14_full_19.py (regular)
           schoolbook  ..............ezFBfont_ncenB12_full_19.py (bold)
           schoolbook  ..............ezFBfont_ncenR12_full_19.py (regular)
   20px:
                times  ...............ezFBfont_timB12_full_20.py (bold)
              courier  ..............ezFBfont_courB14_full_20.py (bold)
            helvetica  ..............ezFBfont_helvR12_full_20.py (regular)
            helvetica  ..............ezFBfont_helvB12_full_20.py (bold)
                fixed  ................ezFBfont_10x20_full_20.py
   21px:
                times  ...............ezFBfont_timB14_full_21.py (bold)
   22px:
                times  ...............ezFBfont_timR14_full_22.py (regular)
            helvetica  ..............ezFBfont_helvR14_full_22.py (regular)
   23px:
            helvetica  ..............ezFBfont_helvB14_full_23.py (bold)
           schoolbook  ..............ezFBfont_ncenB14_full_23.py (bold)
           schoolbook  ..............ezFBfont_ncenR14_full_23.py (regular)
   24px:
              courier  ..............ezFBfont_courR18_full_24.py (regular)
               spleen  .........ezFBfont_spleen_12x24_full_24.py
   26px:
              courier  ..............ezFBfont_courB18_full_26.py (bold)
   29px:
                times  ...............ezFBfont_timR18_full_29.py (regular)
                times  ...............ezFBfont_timB18_full_29.py (bold)
            helvetica  ..............ezFBfont_helvR18_full_29.py (regular)
            helvetica  ..............ezFBfont_helvB18_full_29.py (bold)
           schoolbook  ..............ezFBfont_ncenR18_full_29.py (regular)
           schoolbook  ..............ezFBfont_ncenB18_full_29.py (bold)
   32px:
              courier  ..............ezFBfont_courR24_full_32.py (regular)
               spleen  .........ezFBfont_spleen_16x32_full_32.py
   33px:
              courier  ..............ezFBfont_courB24_full_33.py (bold)
   37px:
                times  ...............ezFBfont_timB24_full_37.py (bold)
                times  ...............ezFBfont_timR24_full_37.py (regular)
   38px:
            helvetica  ..............ezFBfont_helvR24_full_38.py (regular)
            helvetica  ..............ezFBfont_helvB24_full_38.py (bold)
   39px:
           schoolbook  ..............ezFBfont_ncenR24_full_39.py (regular)
   40px:
           schoolbook  ..............ezFBfont_ncenB24_full_40.py (bold)
   64px:
               spleen  .........ezFBfont_spleen_32x64_full_64.py

```
---------------------
## Converter script
The font structure is created by the 'build-sets.py' script in the `bdf2dict` folder, see the README there for more.

The `sets.py` file in this folder contains the character definitions and font source.
