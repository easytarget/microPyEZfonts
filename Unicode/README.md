# Unicode Font files

This folder contains font files suitable for use with `ezFBfont` and Peter Hinches `writer` class.

They are organised by character set, font family and vertical size.
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

The unicode standard defines standard 'blocks' for character sets in different scripts. The character sets here reflect this block structure.

For a good description of the blocks structure  and the characters they contain I recommend the Wikipedia [Unicode Blocks](https://en.m.wikipedia.org/wiki/Unicode_block) page.

* Pay attention to the file sizes; the full sets (especially the '`latin`' set) can get large.
* For a detailed font file description and preview look at the corresponding `.map` file in the 'maps' sub-folder.
  * This contains an ascii-art glyph for all characters in the font file; showing the name, size, bitmap and baseline.
* The `basic latin' and 'latin-1 supplement' blocks are not included here; these are provided in the main [Latin][/Latin] sets.

For usage see the `ezFBfont.py` documentation in the main `README`.

# The list

----------------------

Fonts as of 9 June 2024 organised by charset/family/height.
```
character set: Letterlike-symbols
---------------------------------
    3px :
       amstrad-cpc.......ezFBfont_03_amstrad_cpc_extended_letterlike-symbols.py
    5px :
             fixed........................ezFBfont_05_4x6_letterlike-symbols.py
    7px :
             fixed........................ezFBfont_07_6x9_letterlike-symbols.py
             fixed........................ezFBfont_07_5x7_letterlike-symbols.py
    8px :
             fixed........................ezFBfont_08_5x8_letterlike-symbols.py
    9px :
           courier....................ezFBfont_09_courR08_letterlike-symbols.py (regular)
           courier....................ezFBfont_09_courB08_letterlike-symbols.py (bold)
             fixed.......................ezFBfont_09_6x10_letterlike-symbols.py
           biwidth......................ezFBfont_09_b10_b_letterlike-symbols.py (bold)
           biwidth........................ezFBfont_09_b10_letterlike-symbols.py
   10px :
             times.....................ezFBfont_10_timB08_letterlike-symbols.py (bold)
   11px :
         helvetica....................ezFBfont_11_helvB08_letterlike-symbols.py (bold)
         helvetica....................ezFBfont_11_helvR08_letterlike-symbols.py (regular)
        schoolbook....................ezFBfont_11_ncenB08_letterlike-symbols.py (bold)
        schoolbook....................ezFBfont_11_ncenR08_letterlike-symbols.py (regular)
           biwidth........................ezFBfont_11_b12_letterlike-symbols.py
           biwidth......................ezFBfont_11_b12_b_letterlike-symbols.py (bold)
   12px :
             times.....................ezFBfont_12_timR08_letterlike-symbols.py (regular)
           courier....................ezFBfont_12_courB10_letterlike-symbols.py (bold)
           courier....................ezFBfont_12_courR10_letterlike-symbols.py (regular)
             fixed.......................ezFBfont_12_6x12_letterlike-symbols.py
           biwidth........................ezFBfont_12_b14_letterlike-symbols.py
           biwidth......................ezFBfont_12_b14_b_letterlike-symbols.py (bold)
   13px :
             fixed.......................ezFBfont_13_7x13_letterlike-symbols.py
             fixed.......................ezFBfont_13_8x13_letterlike-symbols.py
             fixed.......................ezFBfont_13_6x13_letterlike-symbols.py
             fixed.......................ezFBfont_13_7x14_letterlike-symbols.py
   14px :
             times.....................ezFBfont_14_timB10_letterlike-symbols.py (bold)
           courier....................ezFBfont_14_courB12_letterlike-symbols.py (bold)
           courier....................ezFBfont_14_courR12_letterlike-symbols.py (regular)
         helvetica....................ezFBfont_14_helvR10_letterlike-symbols.py (regular)
         helvetica....................ezFBfont_14_helvB10_letterlike-symbols.py (bold)
        schoolbook....................ezFBfont_14_ncenR10_letterlike-symbols.py (regular)
           biwidth........................ezFBfont_14_b16_letterlike-symbols.py
           biwidth......................ezFBfont_14_b16_b_letterlike-symbols.py (bold)
   15px :
           courier....................ezFBfont_15_courR14_letterlike-symbols.py (regular)
           courier....................ezFBfont_15_courB14_letterlike-symbols.py (bold)
         helvetica....................ezFBfont_15_helvR12_letterlike-symbols.py (regular)
             fixed.......................ezFBfont_15_9x18_letterlike-symbols.py
             fixed.......................ezFBfont_15_9x15_letterlike-symbols.py
        schoolbook....................ezFBfont_15_ncenB10_letterlike-symbols.py (bold)
   16px :
             times.....................ezFBfont_16_timB12_letterlike-symbols.py (bold)
         helvetica....................ezFBfont_16_helvB12_letterlike-symbols.py (bold)
        schoolbook....................ezFBfont_16_ncenB12_letterlike-symbols.py (bold)
        schoolbook....................ezFBfont_16_ncenR12_letterlike-symbols.py (regular)
   17px :
             times.....................ezFBfont_17_timR10_letterlike-symbols.py (regular)
             times.....................ezFBfont_17_timB14_letterlike-symbols.py (bold)
         helvetica....................ezFBfont_17_helvR14_letterlike-symbols.py (regular)
   18px :
             times.....................ezFBfont_18_timR12_letterlike-symbols.py (regular)
         helvetica....................ezFBfont_18_helvB14_letterlike-symbols.py (bold)
   19px :
           courier....................ezFBfont_19_courR18_letterlike-symbols.py (regular)
             fixed......................ezFBfont_19_10x20_letterlike-symbols.py
        schoolbook....................ezFBfont_19_ncenB14_letterlike-symbols.py (bold)
        schoolbook....................ezFBfont_19_ncenR14_letterlike-symbols.py (regular)
   20px :
           courier....................ezFBfont_20_courB18_letterlike-symbols.py (bold)
   22px :
             times.....................ezFBfont_22_timR14_letterlike-symbols.py (regular)
   23px :
             times.....................ezFBfont_23_timB18_letterlike-symbols.py (bold)
   24px :
         helvetica....................ezFBfont_24_helvB18_letterlike-symbols.py (bold)
         helvetica....................ezFBfont_24_helvR18_letterlike-symbols.py (regular)
        schoolbook....................ezFBfont_24_ncenB18_letterlike-symbols.py (bold)
        schoolbook....................ezFBfont_24_ncenR18_letterlike-symbols.py (regular)
   26px :
           courier....................ezFBfont_26_courR24_letterlike-symbols.py (regular)
           courier....................ezFBfont_26_courB24_letterlike-symbols.py (bold)
   28px :
             times.....................ezFBfont_28_timR18_letterlike-symbols.py (regular)
   30px :
             times.....................ezFBfont_30_timB24_letterlike-symbols.py (bold)
   31px :
         helvetica....................ezFBfont_31_helvB24_letterlike-symbols.py (bold)
         helvetica....................ezFBfont_31_helvR24_letterlike-symbols.py (regular)
   32px :
        schoolbook....................ezFBfont_32_ncenR24_letterlike-symbols.py (regular)
   33px :
        schoolbook....................ezFBfont_33_ncenB24_letterlike-symbols.py (bold)
   37px :
             times.....................ezFBfont_37_timR24_letterlike-symbols.py (regular)

character set: High-surrogates
------------------------------
    5px :
          fixed4x6.....................ezFBfont_05_tom_thumb_high-surrogates.py
           generic....................ezFBfont_05_font_tiny5_high-surrogates.py
           generic.........................ezFBfont_05_micro_high-surrogates.py
             fixed...........................ezFBfont_05_4x6_high-surrogates.py
    6px :
           courier.......................ezFBfont_06_courB08_high-surrogates.py (bold)
           courier.......................ezFBfont_06_courR08_high-surrogates.py (regular)
             fixed...........................ezFBfont_06_5x7_high-surrogates.py
             fixed...........................ezFBfont_06_5x8_high-surrogates.py
           biwidth.........................ezFBfont_06_b10_b_high-surrogates.py (bold)
           biwidth...........................ezFBfont_06_b10_high-surrogates.py
    7px :
       amstrad-cpc..........ezFBfont_07_amstrad_cpc_extended_high-surrogates.py
             times........................ezFBfont_07_timB08_high-surrogates.py (bold)
             times........................ezFBfont_07_timR08_high-surrogates.py (regular)
             fixed..........................ezFBfont_07_6x12_high-surrogates.py
             fixed..........................ezFBfont_07_6x10_high-surrogates.py
             fixed...........................ezFBfont_07_6x9_high-surrogates.py
            spleen....................ezFBfont_07_spleen_5x8_high-surrogates.py
           biwidth...........................ezFBfont_07_b12_high-surrogates.py
           biwidth.........................ezFBfont_07_b12_b_high-surrogates.py (bold)
    8px :
         helvetica...................ezFBfont_08_helvB08_gps_high-surrogates.py (bold)
         helvetica.......................ezFBfont_08_helvB08_high-surrogates.py (bold)
         helvetica.......................ezFBfont_08_helvR08_high-surrogates.py (regular)
            spleen...................ezFBfont_08_spleen_6x12_high-surrogates.py
        schoolbook.......................ezFBfont_08_ncenB08_high-surrogates.py (bold)
        schoolbook.......................ezFBfont_08_ncenR08_high-surrogates.py (regular)
    9px :
           courier.......................ezFBfont_09_courB10_high-surrogates.py (bold)
           courier.......................ezFBfont_09_courR10_high-surrogates.py (regular)
             fixed..........................ezFBfont_09_6x13_high-surrogates.py
             fixed....................ezFBfont_09_etl14_thai_high-surrogates.py
             fixed..........................ezFBfont_09_8x13_high-surrogates.py
             fixed..........................ezFBfont_09_7x13_high-surrogates.py
           biwidth.........................ezFBfont_09_b14_b_high-surrogates.py (bold)
           biwidth...........................ezFBfont_09_b14_high-surrogates.py
   10px :
             times........................ezFBfont_10_timB10_high-surrogates.py (bold)
             times........................ezFBfont_10_timR10_high-surrogates.py (regular)
           courier.......................ezFBfont_10_courB12_high-surrogates.py (bold)
           courier.......................ezFBfont_10_courR12_high-surrogates.py (regular)
             fixed....................ezFBfont_10_etl16_thai_high-surrogates.py
             fixed..........................ezFBfont_10_9x15_high-surrogates.py
             fixed..........................ezFBfont_10_7x14_high-surrogates.py
             fixed..........................ezFBfont_10_9x18_high-surrogates.py
            spleen...................ezFBfont_10_spleen_8x16_high-surrogates.py
           biwidth.........................ezFBfont_10_b16_b_high-surrogates.py (bold)
           biwidth...........................ezFBfont_10_b16_high-surrogates.py
   11px :
             times........................ezFBfont_11_timR12_high-surrogates.py (regular)
             times........................ezFBfont_11_timB12_high-surrogates.py (bold)
           courier.......................ezFBfont_11_courB14_high-surrogates.py (bold)
           courier.......................ezFBfont_11_courR14_high-surrogates.py (regular)
         helvetica.......................ezFBfont_11_helvR10_high-surrogates.py (regular)
         helvetica.......................ezFBfont_11_helvB10_high-surrogates.py (bold)
        schoolbook.......................ezFBfont_11_ncenR10_high-surrogates.py (regular)
        schoolbook.......................ezFBfont_11_ncenB10_high-surrogates.py (bold)
   12px :
         helvetica.......................ezFBfont_12_helvR12_high-surrogates.py (regular)
         helvetica.......................ezFBfont_12_helvB12_high-surrogates.py (bold)
        schoolbook.......................ezFBfont_12_ncenB12_high-surrogates.py (bold)
        schoolbook.......................ezFBfont_12_ncenR12_high-surrogates.py (regular)
   13px :
             times........................ezFBfont_13_timR14_high-surrogates.py (regular)
             times........................ezFBfont_13_timB14_high-surrogates.py (bold)
             fixed.........................ezFBfont_13_10x20_high-surrogates.py
   14px :
           courier.......................ezFBfont_14_courR18_high-surrogates.py (regular)
         helvetica.......................ezFBfont_14_helvR14_high-surrogates.py (regular)
         helvetica.......................ezFBfont_14_helvB14_high-surrogates.py (bold)
        schoolbook.......................ezFBfont_14_ncenB14_high-surrogates.py (bold)
        schoolbook.......................ezFBfont_14_ncenR14_high-surrogates.py (regular)
   15px :
           courier.......................ezFBfont_15_courB18_high-surrogates.py (bold)
             fixed....................ezFBfont_15_etl24_thai_high-surrogates.py
            spleen..................ezFBfont_15_spleen_12x24_high-surrogates.py
   17px :
             times........................ezFBfont_17_timB18_high-surrogates.py (bold)
             times........................ezFBfont_17_timR18_high-surrogates.py (regular)
   18px :
        schoolbook.......................ezFBfont_18_ncenB18_high-surrogates.py (bold)
        schoolbook.......................ezFBfont_18_ncenR18_high-surrogates.py (regular)
   19px :
           courier.......................ezFBfont_19_courR24_high-surrogates.py (regular)
         helvetica.......................ezFBfont_19_helvR18_high-surrogates.py (regular)
         helvetica.......................ezFBfont_19_helvB18_high-surrogates.py (bold)
   20px :
           courier.......................ezFBfont_20_courB24_high-surrogates.py (bold)
            spleen..................ezFBfont_20_spleen_16x32_high-surrogates.py
   23px :
             times........................ezFBfont_23_timR24_high-surrogates.py (regular)
             times........................ezFBfont_23_timB24_high-surrogates.py (bold)
   25px :
         helvetica.......................ezFBfont_25_helvB24_high-surrogates.py (bold)
         helvetica.......................ezFBfont_25_helvR24_high-surrogates.py (regular)
        schoolbook.......................ezFBfont_25_ncenB24_high-surrogates.py (bold)
        schoolbook.......................ezFBfont_25_ncenR24_high-surrogates.py (regular)
   40px :
            spleen..................ezFBfont_40_spleen_32x64_high-surrogates.py

character set: General-punctuation
----------------------------------
    3px :
       amstrad-cpc......ezFBfont_03_amstrad_cpc_extended_general-punctuation.py
          fixed4x6.................ezFBfont_03_tom_thumb_general-punctuation.py
    6px :
             fixed.......................ezFBfont_06_4x6_general-punctuation.py
    7px :
             fixed.......................ezFBfont_07_5x7_general-punctuation.py
    8px :
           courier...................ezFBfont_08_courB08_general-punctuation.py (bold)
             fixed.......................ezFBfont_08_5x8_general-punctuation.py
    9px :
             times....................ezFBfont_09_timR08_general-punctuation.py (regular)
             times....................ezFBfont_09_timB08_general-punctuation.py (bold)
             fixed.......................ezFBfont_09_6x9_general-punctuation.py
           biwidth.....................ezFBfont_09_b10_b_general-punctuation.py (bold)
           biwidth.......................ezFBfont_09_b10_general-punctuation.py
   10px :
           courier...................ezFBfont_10_courR08_general-punctuation.py (regular)
         helvetica...................ezFBfont_10_helvB08_general-punctuation.py (bold)
         helvetica...................ezFBfont_10_helvR08_general-punctuation.py (regular)
             fixed......................ezFBfont_10_6x10_general-punctuation.py
        schoolbook...................ezFBfont_10_ncenR08_general-punctuation.py (regular)
        schoolbook...................ezFBfont_10_ncenB08_general-punctuation.py (bold)
   11px :
           biwidth.......................ezFBfont_11_b12_general-punctuation.py
           biwidth.....................ezFBfont_11_b12_b_general-punctuation.py (bold)
   12px :
             times....................ezFBfont_12_timB10_general-punctuation.py (bold)
             times....................ezFBfont_12_timR10_general-punctuation.py (regular)
           courier...................ezFBfont_12_courR10_general-punctuation.py (regular)
           courier...................ezFBfont_12_courB10_general-punctuation.py (bold)
             fixed......................ezFBfont_12_8x13_general-punctuation.py
             fixed......................ezFBfont_12_6x12_general-punctuation.py
             fixed......................ezFBfont_12_6x13_general-punctuation.py
            spleen...............ezFBfont_12_spleen_8x16_general-punctuation.py
   13px :
             fixed......................ezFBfont_13_7x14_general-punctuation.py
             fixed......................ezFBfont_13_7x13_general-punctuation.py
        schoolbook...................ezFBfont_13_ncenB10_general-punctuation.py (bold)
   14px :
           courier...................ezFBfont_14_courB12_general-punctuation.py (bold)
           courier...................ezFBfont_14_courR12_general-punctuation.py (regular)
         helvetica...................ezFBfont_14_helvB10_general-punctuation.py (bold)
         helvetica...................ezFBfont_14_helvR10_general-punctuation.py (regular)
        schoolbook...................ezFBfont_14_ncenR10_general-punctuation.py (regular)
           biwidth.....................ezFBfont_14_b14_b_general-punctuation.py (bold)
           biwidth.......................ezFBfont_14_b14_general-punctuation.py
   15px :
             times....................ezFBfont_15_timR12_general-punctuation.py (regular)
           courier...................ezFBfont_15_courR14_general-punctuation.py (regular)
           courier...................ezFBfont_15_courB14_general-punctuation.py (bold)
         helvetica...................ezFBfont_15_helvR12_general-punctuation.py (regular)
         helvetica...................ezFBfont_15_helvB12_general-punctuation.py (bold)
             fixed......................ezFBfont_15_9x18_general-punctuation.py
             fixed......................ezFBfont_15_9x15_general-punctuation.py
        schoolbook...................ezFBfont_15_ncenR12_general-punctuation.py (regular)
        schoolbook...................ezFBfont_15_ncenB12_general-punctuation.py (bold)
   16px :
             times....................ezFBfont_16_timR14_general-punctuation.py (regular)
             times....................ezFBfont_16_timB14_general-punctuation.py (bold)
             times....................ezFBfont_16_timB12_general-punctuation.py (bold)
           biwidth.....................ezFBfont_16_b16_b_general-punctuation.py (bold)
           biwidth.......................ezFBfont_16_b16_general-punctuation.py
   17px :
        schoolbook...................ezFBfont_17_ncenR14_general-punctuation.py (regular)
        schoolbook...................ezFBfont_17_ncenB14_general-punctuation.py (bold)
   18px :
         helvetica...................ezFBfont_18_helvR14_general-punctuation.py (regular)
         helvetica...................ezFBfont_18_helvB14_general-punctuation.py (bold)
   19px :
           courier...................ezFBfont_19_courR18_general-punctuation.py (regular)
           courier...................ezFBfont_19_courB18_general-punctuation.py (bold)
            spleen..............ezFBfont_19_spleen_12x24_general-punctuation.py
   20px :
             fixed.....................ezFBfont_20_10x20_general-punctuation.py
   21px :
             times....................ezFBfont_21_timR18_general-punctuation.py (regular)
   22px :
             times....................ezFBfont_22_timB18_general-punctuation.py (bold)
        schoolbook...................ezFBfont_22_ncenR18_general-punctuation.py (regular)
        schoolbook...................ezFBfont_22_ncenB18_general-punctuation.py (bold)
   24px :
         helvetica...................ezFBfont_24_helvB18_general-punctuation.py (bold)
         helvetica...................ezFBfont_24_helvR18_general-punctuation.py (regular)
            spleen..............ezFBfont_24_spleen_16x32_general-punctuation.py
   26px :
           courier...................ezFBfont_26_courB24_general-punctuation.py (bold)
   27px :
           courier...................ezFBfont_27_courR24_general-punctuation.py (regular)
   29px :
             times....................ezFBfont_29_timB24_general-punctuation.py (bold)
   30px :
             times....................ezFBfont_30_timR24_general-punctuation.py (regular)
        schoolbook...................ezFBfont_30_ncenR24_general-punctuation.py (regular)
   31px :
         helvetica...................ezFBfont_31_helvR24_general-punctuation.py (regular)
        schoolbook...................ezFBfont_31_ncenB24_general-punctuation.py (bold)
   32px :
         helvetica...................ezFBfont_32_helvB24_general-punctuation.py (bold)
   48px :
            spleen..............ezFBfont_48_spleen_32x64_general-punctuation.py

character set: Currency-symbols
-------------------------------
    5px :
          fixed4x6....................ezFBfont_05_tom_thumb_currency-symbols.py
             fixed..........................ezFBfont_05_4x6_currency-symbols.py
    7px :
       amstrad-cpc.........ezFBfont_07_amstrad_cpc_extended_currency-symbols.py
             fixed..........................ezFBfont_07_5x7_currency-symbols.py
    8px :
             times.......................ezFBfont_08_timR08_currency-symbols.py (regular)
             times.......................ezFBfont_08_timB08_currency-symbols.py (bold)
           courier......................ezFBfont_08_courB08_currency-symbols.py (bold)
             fixed..........................ezFBfont_08_5x8_currency-symbols.py
           biwidth........................ezFBfont_08_b10_b_currency-symbols.py (bold)
           biwidth..........................ezFBfont_08_b10_currency-symbols.py
    9px :
           courier......................ezFBfont_09_courR08_currency-symbols.py (regular)
         helvetica......................ezFBfont_09_helvB08_currency-symbols.py (bold)
         helvetica......................ezFBfont_09_helvR08_currency-symbols.py (regular)
             fixed..........................ezFBfont_09_6x9_currency-symbols.py
             fixed.........................ezFBfont_09_6x10_currency-symbols.py
            spleen..................ezFBfont_09_spleen_8x16_currency-symbols.py
        schoolbook......................ezFBfont_09_ncenB08_currency-symbols.py (bold)
           biwidth........................ezFBfont_09_b12_b_currency-symbols.py (bold)
           biwidth..........................ezFBfont_09_b12_currency-symbols.py
   10px :
             fixed.........................ezFBfont_10_6x12_currency-symbols.py
        schoolbook......................ezFBfont_10_ncenR08_currency-symbols.py (regular)
   11px :
             times.......................ezFBfont_11_timB10_currency-symbols.py (bold)
           courier......................ezFBfont_11_courR10_currency-symbols.py (regular)
   12px :
             times.......................ezFBfont_12_timR10_currency-symbols.py (regular)
             times.......................ezFBfont_12_timB12_currency-symbols.py (bold)
           courier......................ezFBfont_12_courB10_currency-symbols.py (bold)
         helvetica......................ezFBfont_12_helvB10_currency-symbols.py (bold)
         helvetica......................ezFBfont_12_helvR10_currency-symbols.py (regular)
             fixed.........................ezFBfont_12_6x13_currency-symbols.py
             fixed.........................ezFBfont_12_8x13_currency-symbols.py
             fixed.........................ezFBfont_12_7x13_currency-symbols.py
             fixed.........................ezFBfont_12_7x14_currency-symbols.py
           biwidth..........................ezFBfont_12_b14_currency-symbols.py
           biwidth........................ezFBfont_12_b14_b_currency-symbols.py (bold)
   13px :
             times.......................ezFBfont_13_timR12_currency-symbols.py (regular)
           courier......................ezFBfont_13_courR12_currency-symbols.py (regular)
         helvetica......................ezFBfont_13_helvB12_currency-symbols.py (bold)
         helvetica......................ezFBfont_13_helvR12_currency-symbols.py (regular)
             fixed.........................ezFBfont_13_9x18_currency-symbols.py
             fixed.........................ezFBfont_13_9x15_currency-symbols.py
        schoolbook......................ezFBfont_13_ncenR10_currency-symbols.py (regular)
        schoolbook......................ezFBfont_13_ncenB10_currency-symbols.py (bold)
   14px :
           courier......................ezFBfont_14_courB12_currency-symbols.py (bold)
        schoolbook......................ezFBfont_14_ncenB12_currency-symbols.py (bold)
        schoolbook......................ezFBfont_14_ncenR12_currency-symbols.py (regular)
           biwidth........................ezFBfont_14_b16_b_currency-symbols.py (bold)
           biwidth..........................ezFBfont_14_b16_currency-symbols.py
   15px :
             times.......................ezFBfont_15_timB14_currency-symbols.py (bold)
   16px :
           courier......................ezFBfont_16_courB14_currency-symbols.py (bold)
           courier......................ezFBfont_16_courR14_currency-symbols.py (regular)
         helvetica......................ezFBfont_16_helvR14_currency-symbols.py (regular)
         helvetica......................ezFBfont_16_helvB14_currency-symbols.py (bold)
            spleen.................ezFBfont_16_spleen_12x24_currency-symbols.py
        schoolbook......................ezFBfont_16_ncenR14_currency-symbols.py (regular)
        schoolbook......................ezFBfont_16_ncenB14_currency-symbols.py (bold)
   17px :
             times.......................ezFBfont_17_timR14_currency-symbols.py (regular)
   18px :
           courier......................ezFBfont_18_courR18_currency-symbols.py (regular)
             fixed........................ezFBfont_18_10x20_currency-symbols.py
   19px :
             times.......................ezFBfont_19_timB18_currency-symbols.py (bold)
   20px :
           courier......................ezFBfont_20_courB18_currency-symbols.py (bold)
            spleen.................ezFBfont_20_spleen_16x32_currency-symbols.py
   21px :
             times.......................ezFBfont_21_timR18_currency-symbols.py (regular)
         helvetica......................ezFBfont_21_helvR18_currency-symbols.py (regular)
         helvetica......................ezFBfont_21_helvB18_currency-symbols.py (bold)
        schoolbook......................ezFBfont_21_ncenB18_currency-symbols.py (bold)
        schoolbook......................ezFBfont_21_ncenR18_currency-symbols.py (regular)
   25px :
           courier......................ezFBfont_25_courR24_currency-symbols.py (regular)
   27px :
             times.......................ezFBfont_27_timB24_currency-symbols.py (bold)
           courier......................ezFBfont_27_courB24_currency-symbols.py (bold)
   28px :
             times.......................ezFBfont_28_timR24_currency-symbols.py (regular)
         helvetica......................ezFBfont_28_helvB24_currency-symbols.py (bold)
         helvetica......................ezFBfont_28_helvR24_currency-symbols.py (regular)
   29px :
        schoolbook......................ezFBfont_29_ncenB24_currency-symbols.py (bold)
        schoolbook......................ezFBfont_29_ncenR24_currency-symbols.py (regular)
   40px :
            spleen.................ezFBfont_40_spleen_32x64_currency-symbols.py

character set: Ipa-extensions
-----------------------------
    4px :
             fixed............................ezFBfont_04_6x9_ipa-extensions.py
             fixed............................ezFBfont_04_4x6_ipa-extensions.py
             fixed............................ezFBfont_04_5x8_ipa-extensions.py
    5px :
             fixed...........................ezFBfont_05_6x10_ipa-extensions.py
    7px :
             fixed............................ezFBfont_07_5x7_ipa-extensions.py
           biwidth............................ezFBfont_07_b10_ipa-extensions.py
           biwidth..........................ezFBfont_07_b10_b_ipa-extensions.py (bold)
    9px :
             times.........................ezFBfont_09_timR08_ipa-extensions.py (regular)
           courier........................ezFBfont_09_courB08_ipa-extensions.py (bold)
           courier........................ezFBfont_09_courR08_ipa-extensions.py (regular)
   10px :
         helvetica........................ezFBfont_10_helvB08_ipa-extensions.py (bold)
         helvetica........................ezFBfont_10_helvR08_ipa-extensions.py (regular)
             fixed...........................ezFBfont_10_6x12_ipa-extensions.py
        schoolbook........................ezFBfont_10_ncenB08_ipa-extensions.py (bold)
        schoolbook........................ezFBfont_10_ncenR08_ipa-extensions.py (regular)
           biwidth............................ezFBfont_10_b12_ipa-extensions.py
           biwidth..........................ezFBfont_10_b12_b_ipa-extensions.py (bold)
   11px :
             times.........................ezFBfont_11_timB08_ipa-extensions.py (bold)
   12px :
             fixed...........................ezFBfont_12_8x13_ipa-extensions.py
             fixed...........................ezFBfont_12_7x13_ipa-extensions.py
             fixed...........................ezFBfont_12_6x13_ipa-extensions.py
   13px :
             times.........................ezFBfont_13_timR10_ipa-extensions.py (regular)
             times.........................ezFBfont_13_timB10_ipa-extensions.py (bold)
           courier........................ezFBfont_13_courB10_ipa-extensions.py (bold)
           courier........................ezFBfont_13_courR12_ipa-extensions.py (regular)
           courier........................ezFBfont_13_courR10_ipa-extensions.py (regular)
           biwidth............................ezFBfont_13_b16_ipa-extensions.py
           biwidth..........................ezFBfont_13_b16_b_ipa-extensions.py (bold)
           biwidth..........................ezFBfont_13_b14_b_ipa-extensions.py (bold)
           biwidth............................ezFBfont_13_b14_ipa-extensions.py
   14px :
           courier........................ezFBfont_14_courB12_ipa-extensions.py (bold)
         helvetica........................ezFBfont_14_helvR10_ipa-extensions.py (regular)
         helvetica........................ezFBfont_14_helvB10_ipa-extensions.py (bold)
             fixed...........................ezFBfont_14_9x15_ipa-extensions.py
             fixed...........................ezFBfont_14_9x18_ipa-extensions.py
             fixed...........................ezFBfont_14_7x14_ipa-extensions.py
        schoolbook........................ezFBfont_14_ncenR10_ipa-extensions.py (regular)
        schoolbook........................ezFBfont_14_ncenB10_ipa-extensions.py (bold)
   15px :
        schoolbook........................ezFBfont_15_ncenR12_ipa-extensions.py (regular)
        schoolbook........................ezFBfont_15_ncenB12_ipa-extensions.py (bold)
   16px :
             times.........................ezFBfont_16_timB12_ipa-extensions.py (bold)
             times.........................ezFBfont_16_timR12_ipa-extensions.py (regular)
           courier........................ezFBfont_16_courR14_ipa-extensions.py (regular)
         helvetica........................ezFBfont_16_helvR12_ipa-extensions.py (regular)
   17px :
             times.........................ezFBfont_17_timR14_ipa-extensions.py (regular)
             times.........................ezFBfont_17_timB14_ipa-extensions.py (bold)
           courier........................ezFBfont_17_courB14_ipa-extensions.py (bold)
         helvetica........................ezFBfont_17_helvB12_ipa-extensions.py (bold)
   18px :
         helvetica........................ezFBfont_18_helvR14_ipa-extensions.py (regular)
         helvetica........................ezFBfont_18_helvB14_ipa-extensions.py (bold)
             fixed..........................ezFBfont_18_10x20_ipa-extensions.py
        schoolbook........................ezFBfont_18_ncenB14_ipa-extensions.py (bold)
        schoolbook........................ezFBfont_18_ncenR14_ipa-extensions.py (regular)
   21px :
           courier........................ezFBfont_21_courR18_ipa-extensions.py (regular)
           courier........................ezFBfont_21_courB18_ipa-extensions.py (bold)
   22px :
             times.........................ezFBfont_22_timB18_ipa-extensions.py (bold)
   23px :
        schoolbook........................ezFBfont_23_ncenR18_ipa-extensions.py (regular)
        schoolbook........................ezFBfont_23_ncenB18_ipa-extensions.py (bold)
   24px :
             times.........................ezFBfont_24_timR18_ipa-extensions.py (regular)
         helvetica........................ezFBfont_24_helvR18_ipa-extensions.py (regular)
         helvetica........................ezFBfont_24_helvB18_ipa-extensions.py (bold)
   26px :
           courier........................ezFBfont_26_courR24_ipa-extensions.py (regular)
   29px :
           courier........................ezFBfont_29_courB24_ipa-extensions.py (bold)
   30px :
             times.........................ezFBfont_30_timB24_ipa-extensions.py (bold)
             times.........................ezFBfont_30_timR24_ipa-extensions.py (regular)
   32px :
         helvetica........................ezFBfont_32_helvB24_ipa-extensions.py (bold)
         helvetica........................ezFBfont_32_helvR24_ipa-extensions.py (regular)
        schoolbook........................ezFBfont_32_ncenR24_ipa-extensions.py (regular)
        schoolbook........................ezFBfont_32_ncenB24_ipa-extensions.py (bold)

character set: Latin-extended-a
-------------------------------
    5px :
          fixed4x6....................ezFBfont_05_tom_thumb_latin-extended-a.py
    6px :
             fixed..........................ezFBfont_06_4x6_latin-extended-a.py
    7px :
             fixed..........................ezFBfont_07_5x7_latin-extended-a.py
    8px :
             fixed..........................ezFBfont_08_5x8_latin-extended-a.py
           biwidth........................ezFBfont_08_b10_b_latin-extended-a.py (bold)
           biwidth..........................ezFBfont_08_b10_latin-extended-a.py
    9px :
             fixed..........................ezFBfont_09_6x9_latin-extended-a.py
   10px :
             fixed.........................ezFBfont_10_6x10_latin-extended-a.py
   12px :
             fixed.........................ezFBfont_12_7x13_latin-extended-a.py
             fixed.........................ezFBfont_12_6x12_latin-extended-a.py
           biwidth..........................ezFBfont_12_b12_latin-extended-a.py
           biwidth........................ezFBfont_12_b12_b_latin-extended-a.py (bold)
   13px :
             fixed.........................ezFBfont_13_6x13_latin-extended-a.py
             fixed.........................ezFBfont_13_8x13_latin-extended-a.py
   14px :
             times.......................ezFBfont_14_timR08_latin-extended-a.py (regular)
           courier......................ezFBfont_14_courR08_latin-extended-a.py (regular)
           courier......................ezFBfont_14_courB08_latin-extended-a.py (bold)
             fixed.........................ezFBfont_14_7x14_latin-extended-a.py
           biwidth........................ezFBfont_14_b14_b_latin-extended-a.py (bold)
           biwidth..........................ezFBfont_14_b14_latin-extended-a.py
   15px :
             times.......................ezFBfont_15_timB08_latin-extended-a.py (bold)
             fixed.........................ezFBfont_15_9x15_latin-extended-a.py
            spleen..................ezFBfont_15_spleen_8x16_latin-extended-a.py
   16px :
         helvetica......................ezFBfont_16_helvR08_latin-extended-a.py (regular)
        schoolbook......................ezFBfont_16_ncenR08_latin-extended-a.py (regular)
           biwidth..........................ezFBfont_16_b16_latin-extended-a.py
           biwidth........................ezFBfont_16_b16_b_latin-extended-a.py (bold)
   17px :
         helvetica......................ezFBfont_17_helvB08_latin-extended-a.py (bold)
             fixed.........................ezFBfont_17_9x18_latin-extended-a.py
        schoolbook......................ezFBfont_17_ncenB08_latin-extended-a.py (bold)
   18px :
             times.......................ezFBfont_18_timR10_latin-extended-a.py (regular)
           courier......................ezFBfont_18_courR10_latin-extended-a.py (regular)
   19px :
             times.......................ezFBfont_19_timB10_latin-extended-a.py (bold)
           courier......................ezFBfont_19_courB10_latin-extended-a.py (bold)
         helvetica......................ezFBfont_19_helvB10_latin-extended-a.py (bold)
   20px :
             times.......................ezFBfont_20_timR12_latin-extended-a.py (regular)
           courier......................ezFBfont_20_courR12_latin-extended-a.py (regular)
         helvetica......................ezFBfont_20_helvR10_latin-extended-a.py (regular)
             fixed........................ezFBfont_20_10x20_latin-extended-a.py
        schoolbook......................ezFBfont_20_ncenR10_latin-extended-a.py (regular)
   21px :
           courier......................ezFBfont_21_courB12_latin-extended-a.py (bold)
         helvetica......................ezFBfont_21_helvR12_latin-extended-a.py (regular)
        schoolbook......................ezFBfont_21_ncenB10_latin-extended-a.py (bold)
   22px :
             times.......................ezFBfont_22_timB12_latin-extended-a.py (bold)
           courier......................ezFBfont_22_courB14_latin-extended-a.py (bold)
           courier......................ezFBfont_22_courR14_latin-extended-a.py (regular)
   23px :
         helvetica......................ezFBfont_23_helvB12_latin-extended-a.py (bold)
        schoolbook......................ezFBfont_23_ncenR12_latin-extended-a.py (regular)
   24px :
             times.......................ezFBfont_24_timR14_latin-extended-a.py (regular)
            spleen.................ezFBfont_24_spleen_12x24_latin-extended-a.py
        schoolbook......................ezFBfont_24_ncenB12_latin-extended-a.py (bold)
   25px :
             times.......................ezFBfont_25_timB14_latin-extended-a.py (bold)
         helvetica......................ezFBfont_25_helvR14_latin-extended-a.py (regular)
        schoolbook......................ezFBfont_25_ncenR14_latin-extended-a.py (regular)
   26px :
         helvetica......................ezFBfont_26_helvB14_latin-extended-a.py (bold)
   27px :
           courier......................ezFBfont_27_courR18_latin-extended-a.py (regular)
        schoolbook......................ezFBfont_27_ncenB14_latin-extended-a.py (bold)
   28px :
           courier......................ezFBfont_28_courB18_latin-extended-a.py (bold)
   29px :
             times.......................ezFBfont_29_timR18_latin-extended-a.py (regular)
   32px :
         helvetica......................ezFBfont_32_helvB18_latin-extended-a.py (bold)
         helvetica......................ezFBfont_32_helvR18_latin-extended-a.py (regular)
            spleen.................ezFBfont_32_spleen_16x32_latin-extended-a.py
        schoolbook......................ezFBfont_32_ncenR18_latin-extended-a.py (regular)
   33px :
        schoolbook......................ezFBfont_33_ncenB18_latin-extended-a.py (bold)
   34px :
             times.......................ezFBfont_34_timB18_latin-extended-a.py (bold)
   36px :
           courier......................ezFBfont_36_courR24_latin-extended-a.py (regular)
   39px :
             times.......................ezFBfont_39_timR24_latin-extended-a.py (regular)
           courier......................ezFBfont_39_courB24_latin-extended-a.py (bold)
   42px :
         helvetica......................ezFBfont_42_helvR24_latin-extended-a.py (regular)
   43px :
             times.......................ezFBfont_43_timB24_latin-extended-a.py (bold)
        schoolbook......................ezFBfont_43_ncenR24_latin-extended-a.py (regular)
   44px :
         helvetica......................ezFBfont_44_helvB24_latin-extended-a.py (bold)
   45px :
        schoolbook......................ezFBfont_45_ncenB24_latin-extended-a.py (bold)
   64px :
            spleen.................ezFBfont_64_spleen_32x64_latin-extended-a.py

character set: Arrows
---------------------
    5px :
             fixed....................................ezFBfont_05_4x6_arrows.py
    7px :
             fixed....................................ezFBfont_07_5x8_arrows.py
             fixed....................................ezFBfont_07_5x7_arrows.py
           biwidth....................................ezFBfont_07_b10_arrows.py
           biwidth..................................ezFBfont_07_b10_b_arrows.py (bold)
    8px :
             fixed....................................ezFBfont_08_6x9_arrows.py
    9px :
             fixed...................................ezFBfont_09_6x12_arrows.py
   10px :
             fixed...................................ezFBfont_10_6x13_arrows.py
             fixed...................................ezFBfont_10_6x10_arrows.py
   11px :
             fixed...................................ezFBfont_11_7x14_arrows.py
   12px :
             fixed...................................ezFBfont_12_7x13_arrows.py
           biwidth..................................ezFBfont_12_b12_b_arrows.py (bold)
           biwidth....................................ezFBfont_12_b12_arrows.py
   13px :
             fixed...................................ezFBfont_13_8x13_arrows.py
             fixed...................................ezFBfont_13_9x18_arrows.py
             fixed...................................ezFBfont_13_9x15_arrows.py
           biwidth..................................ezFBfont_13_b16_b_arrows.py (bold)
           biwidth....................................ezFBfont_13_b16_arrows.py
   14px :
           biwidth....................................ezFBfont_14_b14_arrows.py
           biwidth..................................ezFBfont_14_b14_b_arrows.py (bold)
   15px :
             times.................................ezFBfont_15_timR10_arrows.py (regular)
             times.................................ezFBfont_15_timR08_arrows.py (regular)
             times.................................ezFBfont_15_timR12_arrows.py (regular)
   17px :
             fixed..................................ezFBfont_17_10x20_arrows.py
   19px :
             times.................................ezFBfont_19_timR14_arrows.py (regular)
   24px :
             times.................................ezFBfont_24_timR18_arrows.py (regular)
   32px :
             times.................................ezFBfont_32_timR24_arrows.py (regular)

character set: Latin-extended-additional
----------------------------------------
    6px :
             fixed.................ezFBfont_06_4x6_latin-extended-additional.py
    7px :
             fixed.................ezFBfont_07_5x7_latin-extended-additional.py
    8px :
             fixed.................ezFBfont_08_5x8_latin-extended-additional.py
           biwidth.................ezFBfont_08_b10_latin-extended-additional.py
           biwidth...............ezFBfont_08_b10_b_latin-extended-additional.py (bold)
    9px :
             fixed.................ezFBfont_09_6x9_latin-extended-additional.py
   10px :
             fixed................ezFBfont_10_6x10_latin-extended-additional.py
   12px :
             fixed................ezFBfont_12_6x12_latin-extended-additional.py
           biwidth...............ezFBfont_12_b12_b_latin-extended-additional.py (bold)
           biwidth.................ezFBfont_12_b12_latin-extended-additional.py
   13px :
             fixed................ezFBfont_13_6x13_latin-extended-additional.py
             fixed................ezFBfont_13_8x13_latin-extended-additional.py
             fixed................ezFBfont_13_7x13_latin-extended-additional.py
   14px :
             fixed................ezFBfont_14_7x14_latin-extended-additional.py
           biwidth...............ezFBfont_14_b14_b_latin-extended-additional.py (bold)
           biwidth.................ezFBfont_14_b14_latin-extended-additional.py
   15px :
             fixed................ezFBfont_15_9x15_latin-extended-additional.py
   16px :
           courier.............ezFBfont_16_courB08_latin-extended-additional.py (bold)
           courier.............ezFBfont_16_courR08_latin-extended-additional.py (regular)
           biwidth...............ezFBfont_16_b16_b_latin-extended-additional.py (bold)
           biwidth.................ezFBfont_16_b16_latin-extended-additional.py
   17px :
             times..............ezFBfont_17_timR08_latin-extended-additional.py (regular)
   18px :
             times..............ezFBfont_18_timB08_latin-extended-additional.py (bold)
         helvetica.............ezFBfont_18_helvB08_latin-extended-additional.py (bold)
         helvetica.............ezFBfont_18_helvR08_latin-extended-additional.py (regular)
             fixed................ezFBfont_18_9x18_latin-extended-additional.py
        schoolbook.............ezFBfont_18_ncenR08_latin-extended-additional.py (regular)
   19px :
        schoolbook.............ezFBfont_19_ncenB08_latin-extended-additional.py (bold)
   20px :
           courier.............ezFBfont_20_courR10_latin-extended-additional.py (regular)
             fixed...............ezFBfont_20_10x20_latin-extended-additional.py
   21px :
           courier.............ezFBfont_21_courB10_latin-extended-additional.py (bold)
   22px :
         helvetica.............ezFBfont_22_helvR10_latin-extended-additional.py (regular)
   23px :
         helvetica.............ezFBfont_23_helvB10_latin-extended-additional.py (bold)
   24px :
             times..............ezFBfont_24_timB10_latin-extended-additional.py (bold)
             times..............ezFBfont_24_timR10_latin-extended-additional.py (regular)
           courier.............ezFBfont_24_courB12_latin-extended-additional.py (bold)
           courier.............ezFBfont_24_courR12_latin-extended-additional.py (regular)
        schoolbook.............ezFBfont_24_ncenR10_latin-extended-additional.py (regular)
   25px :
        schoolbook.............ezFBfont_25_ncenB10_latin-extended-additional.py (bold)
   26px :
             times..............ezFBfont_26_timR12_latin-extended-additional.py (regular)
             times..............ezFBfont_26_timB12_latin-extended-additional.py (bold)
           courier.............ezFBfont_26_courR14_latin-extended-additional.py (regular)
           courier.............ezFBfont_26_courB14_latin-extended-additional.py (bold)
         helvetica.............ezFBfont_26_helvR12_latin-extended-additional.py (regular)
        schoolbook.............ezFBfont_26_ncenB12_latin-extended-additional.py (bold)
        schoolbook.............ezFBfont_26_ncenR12_latin-extended-additional.py (regular)
   27px :
         helvetica.............ezFBfont_27_helvB12_latin-extended-additional.py (bold)
   28px :
             times..............ezFBfont_28_timR14_latin-extended-additional.py (regular)
             times..............ezFBfont_28_timB14_latin-extended-additional.py (bold)
   29px :
         helvetica.............ezFBfont_29_helvB14_latin-extended-additional.py (bold)
         helvetica.............ezFBfont_29_helvR14_latin-extended-additional.py (regular)
        schoolbook.............ezFBfont_29_ncenR14_latin-extended-additional.py (regular)
   31px :
        schoolbook.............ezFBfont_31_ncenB14_latin-extended-additional.py (bold)
   32px :
           courier.............ezFBfont_32_courR18_latin-extended-additional.py (regular)
   35px :
             times..............ezFBfont_35_timB18_latin-extended-additional.py (bold)
           courier.............ezFBfont_35_courB18_latin-extended-additional.py (bold)
   36px :
             times..............ezFBfont_36_timR18_latin-extended-additional.py (regular)
        schoolbook.............ezFBfont_36_ncenR18_latin-extended-additional.py (regular)
   37px :
         helvetica.............ezFBfont_37_helvB18_latin-extended-additional.py (bold)
         helvetica.............ezFBfont_37_helvR18_latin-extended-additional.py (regular)
   39px :
        schoolbook.............ezFBfont_39_ncenB18_latin-extended-additional.py (bold)
   42px :
           courier.............ezFBfont_42_courR24_latin-extended-additional.py (regular)
   44px :
           courier.............ezFBfont_44_courB24_latin-extended-additional.py (bold)
   48px :
             times..............ezFBfont_48_timR24_latin-extended-additional.py (regular)
         helvetica.............ezFBfont_48_helvR24_latin-extended-additional.py (regular)
   49px :
             times..............ezFBfont_49_timB24_latin-extended-additional.py (bold)
         helvetica.............ezFBfont_49_helvB24_latin-extended-additional.py (bold)
   50px :
        schoolbook.............ezFBfont_50_ncenR24_latin-extended-additional.py (regular)
   52px :
        schoolbook.............ezFBfont_52_ncenB24_latin-extended-additional.py (bold)

character set: Geometric-shapes
-------------------------------
    4px :
             fixed..........................ezFBfont_04_4x6_geometric-shapes.py
    7px :
             times.......................ezFBfont_07_timR08_geometric-shapes.py (regular)
             fixed..........................ezFBfont_07_5x7_geometric-shapes.py
    8px :
             fixed..........................ezFBfont_08_5x8_geometric-shapes.py
            spleen...................ezFBfont_08_spleen_5x8_geometric-shapes.py
    9px :
             fixed..........................ezFBfont_09_6x9_geometric-shapes.py
   10px :
             fixed.........................ezFBfont_10_6x10_geometric-shapes.py
           biwidth..........................ezFBfont_10_b10_geometric-shapes.py
           biwidth........................ezFBfont_10_b10_b_geometric-shapes.py (bold)
   11px :
             times.......................ezFBfont_11_timR10_geometric-shapes.py (regular)
   12px :
             times.......................ezFBfont_12_timR12_geometric-shapes.py (regular)
             fixed.........................ezFBfont_12_6x12_geometric-shapes.py
            spleen..................ezFBfont_12_spleen_6x12_geometric-shapes.py
           biwidth........................ezFBfont_12_b12_b_geometric-shapes.py (bold)
           biwidth..........................ezFBfont_12_b12_geometric-shapes.py
   13px :
             fixed.........................ezFBfont_13_6x13_geometric-shapes.py
             fixed.........................ezFBfont_13_7x13_geometric-shapes.py
             fixed.........................ezFBfont_13_8x13_geometric-shapes.py
   14px :
             times.......................ezFBfont_14_timR14_geometric-shapes.py (regular)
             fixed.........................ezFBfont_14_7x14_geometric-shapes.py
           biwidth..........................ezFBfont_14_b14_geometric-shapes.py
           biwidth........................ezFBfont_14_b14_b_geometric-shapes.py (bold)
   15px :
             fixed.........................ezFBfont_15_9x15_geometric-shapes.py
   16px :
            spleen..................ezFBfont_16_spleen_8x16_geometric-shapes.py
           biwidth........................ezFBfont_16_b16_b_geometric-shapes.py (bold)
           biwidth..........................ezFBfont_16_b16_geometric-shapes.py
   18px :
             times.......................ezFBfont_18_timR18_geometric-shapes.py (regular)
             fixed.........................ezFBfont_18_9x18_geometric-shapes.py
   20px :
             fixed........................ezFBfont_20_10x20_geometric-shapes.py
   24px :
            spleen.................ezFBfont_24_spleen_12x24_geometric-shapes.py
   25px :
             times.......................ezFBfont_25_timR24_geometric-shapes.py (regular)
   32px :
            spleen.................ezFBfont_32_spleen_16x32_geometric-shapes.py
   64px :
            spleen.................ezFBfont_64_spleen_32x64_geometric-shapes.py

character set: Greek-and-coptic
-------------------------------
    6px :
             fixed..........................ezFBfont_06_4x6_greek-and-coptic.py
    7px :
             fixed..........................ezFBfont_07_5x7_greek-and-coptic.py
    8px :
             fixed..........................ezFBfont_08_5x8_greek-and-coptic.py
           biwidth..........................ezFBfont_08_b10_greek-and-coptic.py
           biwidth........................ezFBfont_08_b10_b_greek-and-coptic.py (bold)
    9px :
             fixed..........................ezFBfont_09_6x9_greek-and-coptic.py
   10px :
             fixed.........................ezFBfont_10_6x10_greek-and-coptic.py
   11px :
           courier......................ezFBfont_11_courB08_greek-and-coptic.py (bold)
           courier......................ezFBfont_11_courR08_greek-and-coptic.py (regular)
   12px :
             times.......................ezFBfont_12_timB08_greek-and-coptic.py (bold)
             fixed.........................ezFBfont_12_8x13_greek-and-coptic.py
             fixed.........................ezFBfont_12_7x13_greek-and-coptic.py
             fixed.........................ezFBfont_12_6x13_greek-and-coptic.py
             fixed.........................ezFBfont_12_6x12_greek-and-coptic.py
        schoolbook......................ezFBfont_12_ncenR08_greek-and-coptic.py (regular)
           biwidth........................ezFBfont_12_b12_b_greek-and-coptic.py (bold)
           biwidth..........................ezFBfont_12_b12_greek-and-coptic.py
   13px :
         helvetica......................ezFBfont_13_helvR08_greek-and-coptic.py (regular)
         helvetica......................ezFBfont_13_helvB08_greek-and-coptic.py (bold)
             fixed.........................ezFBfont_13_7x14_greek-and-coptic.py
        schoolbook......................ezFBfont_13_ncenB08_greek-and-coptic.py (bold)
   14px :
             times.......................ezFBfont_14_timR08_greek-and-coptic.py (regular)
             fixed.........................ezFBfont_14_9x15_greek-and-coptic.py
           biwidth..........................ezFBfont_14_b14_greek-and-coptic.py
           biwidth........................ezFBfont_14_b14_b_greek-and-coptic.py (bold)
   15px :
           courier......................ezFBfont_15_courR10_greek-and-coptic.py (regular)
   16px :
           courier......................ezFBfont_16_courB10_greek-and-coptic.py (bold)
         helvetica......................ezFBfont_16_helvR10_greek-and-coptic.py (regular)
           biwidth........................ezFBfont_16_b16_b_greek-and-coptic.py (bold)
           biwidth..........................ezFBfont_16_b16_greek-and-coptic.py
   17px :
             times.......................ezFBfont_17_timB10_greek-and-coptic.py (bold)
           courier......................ezFBfont_17_courB12_greek-and-coptic.py (bold)
           courier......................ezFBfont_17_courR12_greek-and-coptic.py (regular)
         helvetica......................ezFBfont_17_helvB10_greek-and-coptic.py (bold)
             fixed.........................ezFBfont_17_9x18_greek-and-coptic.py
        schoolbook......................ezFBfont_17_ncenB10_greek-and-coptic.py (bold)
        schoolbook......................ezFBfont_17_ncenR10_greek-and-coptic.py (regular)
   18px :
             times.......................ezFBfont_18_timB12_greek-and-coptic.py (bold)
             times.......................ezFBfont_18_timR10_greek-and-coptic.py (regular)
        schoolbook......................ezFBfont_18_ncenR12_greek-and-coptic.py (regular)
        schoolbook......................ezFBfont_18_ncenB12_greek-and-coptic.py (bold)
   19px :
           courier......................ezFBfont_19_courB14_greek-and-coptic.py (bold)
         helvetica......................ezFBfont_19_helvB12_greek-and-coptic.py (bold)
             fixed........................ezFBfont_19_10x20_greek-and-coptic.py
   20px :
             times.......................ezFBfont_20_timB14_greek-and-coptic.py (bold)
           courier......................ezFBfont_20_courR14_greek-and-coptic.py (regular)
         helvetica......................ezFBfont_20_helvR12_greek-and-coptic.py (regular)
        schoolbook......................ezFBfont_20_ncenR14_greek-and-coptic.py (regular)
   21px :
             times.......................ezFBfont_21_timR12_greek-and-coptic.py (regular)
   22px :
         helvetica......................ezFBfont_22_helvR14_greek-and-coptic.py (regular)
         helvetica......................ezFBfont_22_helvB14_greek-and-coptic.py (bold)
        schoolbook......................ezFBfont_22_ncenB14_greek-and-coptic.py (bold)
   23px :
             times.......................ezFBfont_23_timR14_greek-and-coptic.py (regular)
   24px :
           courier......................ezFBfont_24_courR18_greek-and-coptic.py (regular)
   25px :
           courier......................ezFBfont_25_courB18_greek-and-coptic.py (bold)
   26px :
             times.......................ezFBfont_26_timB18_greek-and-coptic.py (bold)
   27px :
        schoolbook......................ezFBfont_27_ncenR18_greek-and-coptic.py (regular)
   28px :
         helvetica......................ezFBfont_28_helvR18_greek-and-coptic.py (regular)
         helvetica......................ezFBfont_28_helvB18_greek-and-coptic.py (bold)
   29px :
             times.......................ezFBfont_29_timR18_greek-and-coptic.py (regular)
        schoolbook......................ezFBfont_29_ncenB18_greek-and-coptic.py (bold)
   32px :
           courier......................ezFBfont_32_courR24_greek-and-coptic.py (regular)
   35px :
             times.......................ezFBfont_35_timB24_greek-and-coptic.py (bold)
           courier......................ezFBfont_35_courB24_greek-and-coptic.py (bold)
   36px :
        schoolbook......................ezFBfont_36_ncenR24_greek-and-coptic.py (regular)
   37px :
         helvetica......................ezFBfont_37_helvR24_greek-and-coptic.py (regular)
        schoolbook......................ezFBfont_37_ncenB24_greek-and-coptic.py (bold)
   38px :
         helvetica......................ezFBfont_38_helvB24_greek-and-coptic.py (bold)
   40px :
             times.......................ezFBfont_40_timR24_greek-and-coptic.py (regular)

character set: Latin-extended-b
-------------------------------
    6px :
             fixed..........................ezFBfont_06_4x6_latin-extended-b.py
    7px :
             fixed..........................ezFBfont_07_5x7_latin-extended-b.py
    8px :
             fixed..........................ezFBfont_08_5x8_latin-extended-b.py
           biwidth..........................ezFBfont_08_b10_latin-extended-b.py
           biwidth........................ezFBfont_08_b10_b_latin-extended-b.py (bold)
    9px :
             fixed..........................ezFBfont_09_6x9_latin-extended-b.py
   10px :
             fixed.........................ezFBfont_10_6x10_latin-extended-b.py
   12px :
             fixed.........................ezFBfont_12_6x12_latin-extended-b.py
           biwidth........................ezFBfont_12_b12_b_latin-extended-b.py (bold)
           biwidth..........................ezFBfont_12_b12_latin-extended-b.py
   13px :
             fixed.........................ezFBfont_13_8x13_latin-extended-b.py
             fixed.........................ezFBfont_13_6x13_latin-extended-b.py
             fixed.........................ezFBfont_13_7x13_latin-extended-b.py
   14px :
             fixed.........................ezFBfont_14_7x14_latin-extended-b.py
           biwidth..........................ezFBfont_14_b14_latin-extended-b.py
           biwidth........................ezFBfont_14_b14_b_latin-extended-b.py (bold)
   15px :
             fixed.........................ezFBfont_15_9x15_latin-extended-b.py
            spleen..................ezFBfont_15_spleen_8x16_latin-extended-b.py
   16px :
             times.......................ezFBfont_16_timR08_latin-extended-b.py (regular)
           courier......................ezFBfont_16_courB08_latin-extended-b.py (bold)
           courier......................ezFBfont_16_courR08_latin-extended-b.py (regular)
           biwidth........................ezFBfont_16_b16_b_latin-extended-b.py (bold)
           biwidth..........................ezFBfont_16_b16_latin-extended-b.py
   17px :
             times.......................ezFBfont_17_timB08_latin-extended-b.py (bold)
   18px :
         helvetica......................ezFBfont_18_helvR08_latin-extended-b.py (regular)
             fixed.........................ezFBfont_18_9x18_latin-extended-b.py
        schoolbook......................ezFBfont_18_ncenR08_latin-extended-b.py (regular)
   19px :
         helvetica......................ezFBfont_19_helvB08_latin-extended-b.py (bold)
        schoolbook......................ezFBfont_19_ncenB08_latin-extended-b.py (bold)
   20px :
           courier......................ezFBfont_20_courB10_latin-extended-b.py (bold)
           courier......................ezFBfont_20_courR10_latin-extended-b.py (regular)
             fixed........................ezFBfont_20_10x20_latin-extended-b.py
   21px :
         helvetica......................ezFBfont_21_helvB10_latin-extended-b.py (bold)
   22px :
             times.......................ezFBfont_22_timR12_latin-extended-b.py (regular)
             times.......................ezFBfont_22_timR10_latin-extended-b.py (regular)
         helvetica......................ezFBfont_22_helvR10_latin-extended-b.py (regular)
   23px :
             times.......................ezFBfont_23_timB10_latin-extended-b.py (bold)
           courier......................ezFBfont_23_courR12_latin-extended-b.py (regular)
        schoolbook......................ezFBfont_23_ncenR10_latin-extended-b.py (regular)
   24px :
           courier......................ezFBfont_24_courB12_latin-extended-b.py (bold)
         helvetica......................ezFBfont_24_helvR12_latin-extended-b.py (regular)
            spleen.................ezFBfont_24_spleen_12x24_latin-extended-b.py
   25px :
           courier......................ezFBfont_25_courR14_latin-extended-b.py (regular)
           courier......................ezFBfont_25_courB14_latin-extended-b.py (bold)
        schoolbook......................ezFBfont_25_ncenB10_latin-extended-b.py (bold)
   26px :
             times.......................ezFBfont_26_timB12_latin-extended-b.py (bold)
         helvetica......................ezFBfont_26_helvB12_latin-extended-b.py (bold)
        schoolbook......................ezFBfont_26_ncenR12_latin-extended-b.py (regular)
   27px :
         helvetica......................ezFBfont_27_helvR14_latin-extended-b.py (regular)
        schoolbook......................ezFBfont_27_ncenB12_latin-extended-b.py (bold)
   28px :
             times.......................ezFBfont_28_timB14_latin-extended-b.py (bold)
             times.......................ezFBfont_28_timR14_latin-extended-b.py (regular)
   29px :
         helvetica......................ezFBfont_29_helvB14_latin-extended-b.py (bold)
        schoolbook......................ezFBfont_29_ncenR14_latin-extended-b.py (regular)
   31px :
           courier......................ezFBfont_31_courR18_latin-extended-b.py (regular)
   32px :
           courier......................ezFBfont_32_courB18_latin-extended-b.py (bold)
            spleen.................ezFBfont_32_spleen_16x32_latin-extended-b.py
        schoolbook......................ezFBfont_32_ncenB14_latin-extended-b.py (bold)
   34px :
             times.......................ezFBfont_34_timR18_latin-extended-b.py (regular)
   36px :
         helvetica......................ezFBfont_36_helvB18_latin-extended-b.py (bold)
         helvetica......................ezFBfont_36_helvR18_latin-extended-b.py (regular)
   37px :
        schoolbook......................ezFBfont_37_ncenR18_latin-extended-b.py (regular)
   38px :
             times.......................ezFBfont_38_timB18_latin-extended-b.py (bold)
   39px :
        schoolbook......................ezFBfont_39_ncenB18_latin-extended-b.py (bold)
   42px :
           courier......................ezFBfont_42_courR24_latin-extended-b.py (regular)
   44px :
           courier......................ezFBfont_44_courB24_latin-extended-b.py (bold)
   45px :
             times.......................ezFBfont_45_timR24_latin-extended-b.py (regular)
   47px :
         helvetica......................ezFBfont_47_helvR24_latin-extended-b.py (regular)
   49px :
             times.......................ezFBfont_49_timB24_latin-extended-b.py (bold)
         helvetica......................ezFBfont_49_helvB24_latin-extended-b.py (bold)
   50px :
        schoolbook......................ezFBfont_50_ncenR24_latin-extended-b.py (regular)
   52px :
        schoolbook......................ezFBfont_52_ncenB24_latin-extended-b.py (bold)
   64px :
            spleen.................ezFBfont_64_spleen_32x64_latin-extended-b.py

character set: Spacing-modifier-letters
---------------------------------------
    6px :
             fixed..................ezFBfont_06_4x6_spacing-modifier-letters.py
    7px :
             fixed..................ezFBfont_07_5x7_spacing-modifier-letters.py
    8px :
             fixed..................ezFBfont_08_5x8_spacing-modifier-letters.py
    9px :
             fixed..................ezFBfont_09_6x9_spacing-modifier-letters.py
   10px :
             fixed.................ezFBfont_10_6x10_spacing-modifier-letters.py
           biwidth..................ezFBfont_10_b10_spacing-modifier-letters.py
           biwidth................ezFBfont_10_b10_b_spacing-modifier-letters.py (bold)
   11px :
             times...............ezFBfont_11_timR08_spacing-modifier-letters.py (regular)
             times...............ezFBfont_11_timB08_spacing-modifier-letters.py (bold)
             fixed.................ezFBfont_11_6x12_spacing-modifier-letters.py
        schoolbook..............ezFBfont_11_ncenR08_spacing-modifier-letters.py (regular)
        schoolbook..............ezFBfont_11_ncenB08_spacing-modifier-letters.py (bold)
           biwidth................ezFBfont_11_b12_b_spacing-modifier-letters.py (bold)
           biwidth..................ezFBfont_11_b12_spacing-modifier-letters.py
   12px :
           courier..............ezFBfont_12_courB08_spacing-modifier-letters.py (bold)
           courier..............ezFBfont_12_courR08_spacing-modifier-letters.py (regular)
         helvetica..............ezFBfont_12_helvR08_spacing-modifier-letters.py (regular)
         helvetica..............ezFBfont_12_helvB08_spacing-modifier-letters.py (bold)
   13px :
           courier..............ezFBfont_13_courB10_spacing-modifier-letters.py (bold)
           courier..............ezFBfont_13_courR10_spacing-modifier-letters.py (regular)
             fixed.................ezFBfont_13_8x13_spacing-modifier-letters.py
             fixed.................ezFBfont_13_7x13_spacing-modifier-letters.py
             fixed.................ezFBfont_13_6x13_spacing-modifier-letters.py
   14px :
         helvetica..............ezFBfont_14_helvB10_spacing-modifier-letters.py (bold)
         helvetica..............ezFBfont_14_helvR10_spacing-modifier-letters.py (regular)
             fixed.................ezFBfont_14_7x14_spacing-modifier-letters.py
             fixed.................ezFBfont_14_9x15_spacing-modifier-letters.py
           biwidth..................ezFBfont_14_b14_spacing-modifier-letters.py
           biwidth................ezFBfont_14_b14_b_spacing-modifier-letters.py (bold)
   15px :
             times...............ezFBfont_15_timB10_spacing-modifier-letters.py (bold)
             times...............ezFBfont_15_timR10_spacing-modifier-letters.py (regular)
             fixed.................ezFBfont_15_9x18_spacing-modifier-letters.py
            spleen..........ezFBfont_15_spleen_8x16_spacing-modifier-letters.py
        schoolbook..............ezFBfont_15_ncenB10_spacing-modifier-letters.py (bold)
        schoolbook..............ezFBfont_15_ncenR10_spacing-modifier-letters.py (regular)
   16px :
             times...............ezFBfont_16_timR12_spacing-modifier-letters.py (regular)
           courier..............ezFBfont_16_courR14_spacing-modifier-letters.py (regular)
           courier..............ezFBfont_16_courB14_spacing-modifier-letters.py (bold)
           courier..............ezFBfont_16_courB12_spacing-modifier-letters.py (bold)
           courier..............ezFBfont_16_courR12_spacing-modifier-letters.py (regular)
        schoolbook..............ezFBfont_16_ncenB12_spacing-modifier-letters.py (bold)
        schoolbook..............ezFBfont_16_ncenR12_spacing-modifier-letters.py (regular)
           biwidth..................ezFBfont_16_b16_spacing-modifier-letters.py
           biwidth................ezFBfont_16_b16_b_spacing-modifier-letters.py (bold)
   17px :
             times...............ezFBfont_17_timB12_spacing-modifier-letters.py (bold)
         helvetica..............ezFBfont_17_helvB12_spacing-modifier-letters.py (bold)
         helvetica..............ezFBfont_17_helvR12_spacing-modifier-letters.py (regular)
   18px :
             times...............ezFBfont_18_timB14_spacing-modifier-letters.py (bold)
             times...............ezFBfont_18_timR14_spacing-modifier-letters.py (regular)
         helvetica..............ezFBfont_18_helvR14_spacing-modifier-letters.py (regular)
        schoolbook..............ezFBfont_18_ncenR14_spacing-modifier-letters.py (regular)
   19px :
         helvetica..............ezFBfont_19_helvB14_spacing-modifier-letters.py (bold)
             fixed................ezFBfont_19_10x20_spacing-modifier-letters.py
   20px :
        schoolbook..............ezFBfont_20_ncenB14_spacing-modifier-letters.py (bold)
   21px :
           courier..............ezFBfont_21_courB18_spacing-modifier-letters.py (bold)
           courier..............ezFBfont_21_courR18_spacing-modifier-letters.py (regular)
   23px :
             times...............ezFBfont_23_timB18_spacing-modifier-letters.py (bold)
             times...............ezFBfont_23_timR18_spacing-modifier-letters.py (regular)
            spleen.........ezFBfont_23_spleen_12x24_spacing-modifier-letters.py
   24px :
         helvetica..............ezFBfont_24_helvB18_spacing-modifier-letters.py (bold)
         helvetica..............ezFBfont_24_helvR18_spacing-modifier-letters.py (regular)
        schoolbook..............ezFBfont_24_ncenR18_spacing-modifier-letters.py (regular)
   25px :
        schoolbook..............ezFBfont_25_ncenB18_spacing-modifier-letters.py (bold)
   29px :
           courier..............ezFBfont_29_courB24_spacing-modifier-letters.py (bold)
           courier..............ezFBfont_29_courR24_spacing-modifier-letters.py (regular)
   31px :
            spleen.........ezFBfont_31_spleen_16x32_spacing-modifier-letters.py
   32px :
             times...............ezFBfont_32_timB24_spacing-modifier-letters.py (bold)
             times...............ezFBfont_32_timR24_spacing-modifier-letters.py (regular)
         helvetica..............ezFBfont_32_helvB24_spacing-modifier-letters.py (bold)
        schoolbook..............ezFBfont_32_ncenR24_spacing-modifier-letters.py (regular)
        schoolbook..............ezFBfont_32_ncenB24_spacing-modifier-letters.py (bold)
   33px :
         helvetica..............ezFBfont_33_helvR24_spacing-modifier-letters.py (regular)
   62px :
            spleen.........ezFBfont_62_spleen_32x64_spacing-modifier-letters.py

character set: Miscellaneous-symbols
------------------------------------
    5px :
             times..................ezFBfont_05_timR08_miscellaneous-symbols.py (regular)
             fixed.....................ezFBfont_05_4x6_miscellaneous-symbols.py
            spleen.............ezFBfont_05_spleen_6x12_miscellaneous-symbols.py
            spleen..............ezFBfont_05_spleen_5x8_miscellaneous-symbols.py
    7px :
             times..................ezFBfont_07_timR10_miscellaneous-symbols.py (regular)
             fixed.....................ezFBfont_07_5x7_miscellaneous-symbols.py
            spleen.............ezFBfont_07_spleen_8x16_miscellaneous-symbols.py
    8px :
             fixed.....................ezFBfont_08_6x9_miscellaneous-symbols.py
             fixed.....................ezFBfont_08_5x8_miscellaneous-symbols.py
    9px :
             times..................ezFBfont_09_timR14_miscellaneous-symbols.py (regular)
   10px :
             times..................ezFBfont_10_timR12_miscellaneous-symbols.py (regular)
             fixed....................ezFBfont_10_6x10_miscellaneous-symbols.py
           biwidth...................ezFBfont_10_b10_b_miscellaneous-symbols.py (bold)
           biwidth.....................ezFBfont_10_b10_miscellaneous-symbols.py
   12px :
             fixed....................ezFBfont_12_6x12_miscellaneous-symbols.py
            spleen............ezFBfont_12_spleen_12x24_miscellaneous-symbols.py
           biwidth...................ezFBfont_12_b12_b_miscellaneous-symbols.py (bold)
           biwidth.....................ezFBfont_12_b12_miscellaneous-symbols.py
   13px :
             times..................ezFBfont_13_timR18_miscellaneous-symbols.py (regular)
             fixed....................ezFBfont_13_6x13_miscellaneous-symbols.py
             fixed....................ezFBfont_13_8x13_miscellaneous-symbols.py
             fixed....................ezFBfont_13_7x13_miscellaneous-symbols.py
             fixed....................ezFBfont_13_7x14_miscellaneous-symbols.py
           biwidth.....................ezFBfont_13_b16_miscellaneous-symbols.py
           biwidth...................ezFBfont_13_b16_b_miscellaneous-symbols.py (bold)
   14px :
           biwidth.....................ezFBfont_14_b14_miscellaneous-symbols.py
           biwidth...................ezFBfont_14_b14_b_miscellaneous-symbols.py (bold)
   15px :
             fixed....................ezFBfont_15_9x15_miscellaneous-symbols.py
             fixed....................ezFBfont_15_9x18_miscellaneous-symbols.py
   16px :
            spleen............ezFBfont_16_spleen_16x32_miscellaneous-symbols.py
   18px :
             times..................ezFBfont_18_timR24_miscellaneous-symbols.py (regular)
   20px :
             fixed...................ezFBfont_20_10x20_miscellaneous-symbols.py
   32px :
            spleen............ezFBfont_32_spleen_32x64_miscellaneous-symbols.py

character set: Mathematical-operators
-------------------------------------
    5px :
            spleen............ezFBfont_05_spleen_8x16_mathematical-operators.py
    6px :
             fixed....................ezFBfont_06_4x6_mathematical-operators.py
    7px :
             fixed....................ezFBfont_07_5x7_mathematical-operators.py
    8px :
             fixed....................ezFBfont_08_5x8_mathematical-operators.py
            spleen...........ezFBfont_08_spleen_12x24_mathematical-operators.py
    9px :
             times.................ezFBfont_09_timB08_mathematical-operators.py (bold)
           courier................ezFBfont_09_courB08_mathematical-operators.py (bold)
         helvetica................ezFBfont_09_helvB08_mathematical-operators.py (bold)
         helvetica................ezFBfont_09_helvR08_mathematical-operators.py (regular)
             fixed....................ezFBfont_09_6x9_mathematical-operators.py
        schoolbook................ezFBfont_09_ncenB08_mathematical-operators.py (bold)
           biwidth..................ezFBfont_09_b10_b_mathematical-operators.py (bold)
           biwidth....................ezFBfont_09_b10_mathematical-operators.py
   10px :
           courier................ezFBfont_10_courR08_mathematical-operators.py (regular)
             fixed...................ezFBfont_10_6x10_mathematical-operators.py
            spleen...........ezFBfont_10_spleen_16x32_mathematical-operators.py
   12px :
             times.................ezFBfont_12_timR08_mathematical-operators.py (regular)
             times.................ezFBfont_12_timB10_mathematical-operators.py (bold)
           courier................ezFBfont_12_courR10_mathematical-operators.py (regular)
             fixed...................ezFBfont_12_6x12_mathematical-operators.py
        schoolbook................ezFBfont_12_ncenR08_mathematical-operators.py (regular)
           biwidth....................ezFBfont_12_b12_mathematical-operators.py
           biwidth..................ezFBfont_12_b12_b_mathematical-operators.py (bold)
   13px :
           courier................ezFBfont_13_courB10_mathematical-operators.py (bold)
         helvetica................ezFBfont_13_helvR10_mathematical-operators.py (regular)
         helvetica................ezFBfont_13_helvB10_mathematical-operators.py (bold)
             fixed...................ezFBfont_13_6x13_mathematical-operators.py
             fixed...................ezFBfont_13_7x13_mathematical-operators.py
             fixed...................ezFBfont_13_8x13_mathematical-operators.py
        schoolbook................ezFBfont_13_ncenB10_mathematical-operators.py (bold)
   14px :
             times.................ezFBfont_14_timB12_mathematical-operators.py (bold)
         helvetica................ezFBfont_14_helvR12_mathematical-operators.py (regular)
             fixed...................ezFBfont_14_9x15_mathematical-operators.py
             fixed...................ezFBfont_14_9x18_mathematical-operators.py
             fixed...................ezFBfont_14_7x14_mathematical-operators.py
        schoolbook................ezFBfont_14_ncenR10_mathematical-operators.py (regular)
        schoolbook................ezFBfont_14_ncenB12_mathematical-operators.py (bold)
           biwidth..................ezFBfont_14_b14_b_mathematical-operators.py (bold)
           biwidth....................ezFBfont_14_b14_mathematical-operators.py
   15px :
             times.................ezFBfont_15_timR10_mathematical-operators.py (regular)
           courier................ezFBfont_15_courR12_mathematical-operators.py (regular)
         helvetica................ezFBfont_15_helvB12_mathematical-operators.py (bold)
        schoolbook................ezFBfont_15_ncenR12_mathematical-operators.py (regular)
           biwidth..................ezFBfont_15_b16_b_mathematical-operators.py (bold)
           biwidth....................ezFBfont_15_b16_mathematical-operators.py
   16px :
             times.................ezFBfont_16_timB14_mathematical-operators.py (bold)
           courier................ezFBfont_16_courB12_mathematical-operators.py (bold)
        schoolbook................ezFBfont_16_ncenR14_mathematical-operators.py (regular)
   17px :
             times.................ezFBfont_17_timR12_mathematical-operators.py (regular)
           courier................ezFBfont_17_courR14_mathematical-operators.py (regular)
        schoolbook................ezFBfont_17_ncenB14_mathematical-operators.py (bold)
   18px :
           courier................ezFBfont_18_courB14_mathematical-operators.py (bold)
         helvetica................ezFBfont_18_helvR14_mathematical-operators.py (regular)
         helvetica................ezFBfont_18_helvB14_mathematical-operators.py (bold)
             fixed..................ezFBfont_18_10x20_mathematical-operators.py
   19px :
           courier................ezFBfont_19_courR18_mathematical-operators.py (regular)
   20px :
             times.................ezFBfont_20_timR14_mathematical-operators.py (regular)
            spleen...........ezFBfont_20_spleen_32x64_mathematical-operators.py
   21px :
             times.................ezFBfont_21_timB18_mathematical-operators.py (bold)
        schoolbook................ezFBfont_21_ncenB18_mathematical-operators.py (bold)
        schoolbook................ezFBfont_21_ncenR18_mathematical-operators.py (regular)
   22px :
           courier................ezFBfont_22_courB18_mathematical-operators.py (bold)
   23px :
         helvetica................ezFBfont_23_helvB18_mathematical-operators.py (bold)
         helvetica................ezFBfont_23_helvR18_mathematical-operators.py (regular)
   25px :
             times.................ezFBfont_25_timR18_mathematical-operators.py (regular)
   26px :
           courier................ezFBfont_26_courR24_mathematical-operators.py (regular)
   30px :
           courier................ezFBfont_30_courB24_mathematical-operators.py (bold)
         helvetica................ezFBfont_30_helvR24_mathematical-operators.py (regular)
        schoolbook................ezFBfont_30_ncenB24_mathematical-operators.py (bold)
   31px :
             times.................ezFBfont_31_timB24_mathematical-operators.py (bold)
         helvetica................ezFBfont_31_helvB24_mathematical-operators.py (bold)
        schoolbook................ezFBfont_31_ncenR24_mathematical-operators.py (regular)
   34px :
             times.................ezFBfont_34_timR24_mathematical-operators.py (regular)

character set: Miscellaneous-technical
--------------------------------------
    6px :
             fixed...................ezFBfont_06_4x6_miscellaneous-technical.py
    7px :
             fixed...................ezFBfont_07_5x7_miscellaneous-technical.py
    8px :
             fixed...................ezFBfont_08_5x8_miscellaneous-technical.py
           biwidth...................ezFBfont_08_b10_miscellaneous-technical.py
           biwidth.................ezFBfont_08_b10_b_miscellaneous-technical.py (bold)
    9px :
             fixed...................ezFBfont_09_6x9_miscellaneous-technical.py
   10px :
             fixed..................ezFBfont_10_6x10_miscellaneous-technical.py
   12px :
             fixed..................ezFBfont_12_6x12_miscellaneous-technical.py
           biwidth.................ezFBfont_12_b12_b_miscellaneous-technical.py (bold)
           biwidth...................ezFBfont_12_b12_miscellaneous-technical.py
   13px :
             fixed..................ezFBfont_13_8x13_miscellaneous-technical.py
             fixed..................ezFBfont_13_6x13_miscellaneous-technical.py
             fixed..................ezFBfont_13_7x13_miscellaneous-technical.py
   14px :
             fixed..................ezFBfont_14_7x14_miscellaneous-technical.py
           biwidth.................ezFBfont_14_b14_b_miscellaneous-technical.py (bold)
           biwidth...................ezFBfont_14_b14_miscellaneous-technical.py
   15px :
             times................ezFBfont_15_timR10_miscellaneous-technical.py (regular)
             times................ezFBfont_15_timR08_miscellaneous-technical.py (regular)
             fixed..................ezFBfont_15_9x15_miscellaneous-technical.py
   16px :
           biwidth.................ezFBfont_16_b16_b_miscellaneous-technical.py (bold)
           biwidth...................ezFBfont_16_b16_miscellaneous-technical.py
   17px :
             times................ezFBfont_17_timR12_miscellaneous-technical.py (regular)
   18px :
             fixed..................ezFBfont_18_9x18_miscellaneous-technical.py
   19px :
             times................ezFBfont_19_timR14_miscellaneous-technical.py (regular)
   20px :
             fixed.................ezFBfont_20_10x20_miscellaneous-technical.py
   24px :
             times................ezFBfont_24_timR18_miscellaneous-technical.py (regular)
   34px :
             times................ezFBfont_34_timR24_miscellaneous-technical.py (regular)

character set: Superscripts-and-subscripts
------------------------------------------
    3px :
             fixed...............ezFBfont_03_4x6_superscripts-and-subscripts.py
    4px :
             times............ezFBfont_04_timB08_superscripts-and-subscripts.py (bold)
             times............ezFBfont_04_timR08_superscripts-and-subscripts.py (regular)
           courier...........ezFBfont_04_courB08_superscripts-and-subscripts.py (bold)
           courier...........ezFBfont_04_courR08_superscripts-and-subscripts.py (regular)
         helvetica...........ezFBfont_04_helvB08_superscripts-and-subscripts.py (bold)
         helvetica...........ezFBfont_04_helvR08_superscripts-and-subscripts.py (regular)
        schoolbook...........ezFBfont_04_ncenR08_superscripts-and-subscripts.py (regular)
        schoolbook...........ezFBfont_04_ncenB08_superscripts-and-subscripts.py (bold)
    6px :
             times............ezFBfont_06_timB10_superscripts-and-subscripts.py (bold)
             times............ezFBfont_06_timR10_superscripts-and-subscripts.py (regular)
           courier...........ezFBfont_06_courB12_superscripts-and-subscripts.py (bold)
           courier...........ezFBfont_06_courB10_superscripts-and-subscripts.py (bold)
           courier...........ezFBfont_06_courR10_superscripts-and-subscripts.py (regular)
           courier...........ezFBfont_06_courR12_superscripts-and-subscripts.py (regular)
         helvetica...........ezFBfont_06_helvR10_superscripts-and-subscripts.py (regular)
         helvetica...........ezFBfont_06_helvB10_superscripts-and-subscripts.py (bold)
        schoolbook...........ezFBfont_06_ncenR10_superscripts-and-subscripts.py (regular)
        schoolbook...........ezFBfont_06_ncenB10_superscripts-and-subscripts.py (bold)
    7px :
             times............ezFBfont_07_timB12_superscripts-and-subscripts.py (bold)
             times............ezFBfont_07_timR12_superscripts-and-subscripts.py (regular)
           courier...........ezFBfont_07_courR14_superscripts-and-subscripts.py (regular)
           courier...........ezFBfont_07_courB14_superscripts-and-subscripts.py (bold)
         helvetica...........ezFBfont_07_helvR12_superscripts-and-subscripts.py (regular)
         helvetica...........ezFBfont_07_helvB12_superscripts-and-subscripts.py (bold)
             fixed...............ezFBfont_07_5x7_superscripts-and-subscripts.py
        schoolbook...........ezFBfont_07_ncenB12_superscripts-and-subscripts.py (bold)
        schoolbook...........ezFBfont_07_ncenR12_superscripts-and-subscripts.py (regular)
    8px :
             times............ezFBfont_08_timB14_superscripts-and-subscripts.py (bold)
             times............ezFBfont_08_timR14_superscripts-and-subscripts.py (regular)
         helvetica...........ezFBfont_08_helvR14_superscripts-and-subscripts.py (regular)
         helvetica...........ezFBfont_08_helvB14_superscripts-and-subscripts.py (bold)
             fixed...............ezFBfont_08_5x8_superscripts-and-subscripts.py
             fixed...............ezFBfont_08_6x9_superscripts-and-subscripts.py
        schoolbook...........ezFBfont_08_ncenR14_superscripts-and-subscripts.py (regular)
        schoolbook...........ezFBfont_08_ncenB14_superscripts-and-subscripts.py (bold)
           biwidth...............ezFBfont_08_b10_superscripts-and-subscripts.py
           biwidth.............ezFBfont_08_b10_b_superscripts-and-subscripts.py (bold)
    9px :
           courier...........ezFBfont_09_courB18_superscripts-and-subscripts.py (bold)
           courier...........ezFBfont_09_courR18_superscripts-and-subscripts.py (regular)
   10px :
             times............ezFBfont_10_timB18_superscripts-and-subscripts.py (bold)
             times............ezFBfont_10_timR18_superscripts-and-subscripts.py (regular)
         helvetica...........ezFBfont_10_helvR18_superscripts-and-subscripts.py (regular)
         helvetica...........ezFBfont_10_helvB18_superscripts-and-subscripts.py (bold)
             fixed..............ezFBfont_10_6x10_superscripts-and-subscripts.py
   11px :
        schoolbook...........ezFBfont_11_ncenB18_superscripts-and-subscripts.py (bold)
        schoolbook...........ezFBfont_11_ncenR18_superscripts-and-subscripts.py (regular)
   12px :
             fixed..............ezFBfont_12_7x13_superscripts-and-subscripts.py
             fixed..............ezFBfont_12_8x13_superscripts-and-subscripts.py
             fixed..............ezFBfont_12_9x15_superscripts-and-subscripts.py
             fixed..............ezFBfont_12_6x12_superscripts-and-subscripts.py
             fixed..............ezFBfont_12_9x18_superscripts-and-subscripts.py
           biwidth.............ezFBfont_12_b12_b_superscripts-and-subscripts.py (bold)
           biwidth...............ezFBfont_12_b12_superscripts-and-subscripts.py
   13px :
             fixed..............ezFBfont_13_6x13_superscripts-and-subscripts.py
             fixed..............ezFBfont_13_7x14_superscripts-and-subscripts.py
   14px :
             times............ezFBfont_14_timR24_superscripts-and-subscripts.py (regular)
             times............ezFBfont_14_timB24_superscripts-and-subscripts.py (bold)
           courier...........ezFBfont_14_courB24_superscripts-and-subscripts.py (bold)
           courier...........ezFBfont_14_courR24_superscripts-and-subscripts.py (regular)
        schoolbook...........ezFBfont_14_ncenB24_superscripts-and-subscripts.py (bold)
        schoolbook...........ezFBfont_14_ncenR24_superscripts-and-subscripts.py (regular)
           biwidth...............ezFBfont_14_b16_superscripts-and-subscripts.py
           biwidth...............ezFBfont_14_b14_superscripts-and-subscripts.py
           biwidth.............ezFBfont_14_b16_b_superscripts-and-subscripts.py (bold)
           biwidth.............ezFBfont_14_b14_b_superscripts-and-subscripts.py (bold)
   15px :
         helvetica...........ezFBfont_15_helvB24_superscripts-and-subscripts.py (bold)
         helvetica...........ezFBfont_15_helvR24_superscripts-and-subscripts.py (regular)
   16px :
             fixed.............ezFBfont_16_10x20_superscripts-and-subscripts.py

character set: Block-elements
-----------------------------
    6px :
             fixed............................ezFBfont_06_4x6_block-elements.py
    7px :
             fixed............................ezFBfont_07_5x7_block-elements.py
    8px :
             fixed............................ezFBfont_08_5x8_block-elements.py
           biwidth..........................ezFBfont_08_b10_b_block-elements.py (bold)
           biwidth............................ezFBfont_08_b10_block-elements.py
    9px :
             fixed............................ezFBfont_09_6x9_block-elements.py
   10px :
             fixed...........................ezFBfont_10_6x10_block-elements.py
   11px :
           courier........................ezFBfont_11_courB08_block-elements.py (bold)
           courier........................ezFBfont_11_courR08_block-elements.py (regular)
   12px :
             fixed...........................ezFBfont_12_6x12_block-elements.py
           biwidth..........................ezFBfont_12_b12_b_block-elements.py (bold)
           biwidth............................ezFBfont_12_b12_block-elements.py
   13px :
             fixed...........................ezFBfont_13_6x13_block-elements.py
             fixed...........................ezFBfont_13_7x13_block-elements.py
             fixed...........................ezFBfont_13_8x13_block-elements.py
   14px :
             fixed...........................ezFBfont_14_7x14_block-elements.py
           biwidth............................ezFBfont_14_b14_block-elements.py
           biwidth..........................ezFBfont_14_b14_b_block-elements.py (bold)
   15px :
           courier........................ezFBfont_15_courR10_block-elements.py (regular)
             fixed...........................ezFBfont_15_9x15_block-elements.py
   16px :
           courier........................ezFBfont_16_courB12_block-elements.py (bold)
           courier........................ezFBfont_16_courB10_block-elements.py (bold)
           courier........................ezFBfont_16_courR12_block-elements.py (regular)
            spleen....................ezFBfont_16_spleen_8x16_block-elements.py
           biwidth............................ezFBfont_16_b16_block-elements.py
           biwidth..........................ezFBfont_16_b16_b_block-elements.py (bold)
   18px :
           courier........................ezFBfont_18_courR14_block-elements.py (regular)
             fixed...........................ezFBfont_18_9x18_block-elements.py
   19px :
           courier........................ezFBfont_19_courB14_block-elements.py (bold)
   20px :
             fixed..........................ezFBfont_20_10x20_block-elements.py
   23px :
           courier........................ezFBfont_23_courR18_block-elements.py (regular)
   24px :
           courier........................ezFBfont_24_courB18_block-elements.py (bold)
            spleen...................ezFBfont_24_spleen_12x24_block-elements.py
   30px :
           courier........................ezFBfont_30_courR24_block-elements.py (regular)
   31px :
           courier........................ezFBfont_31_courB24_block-elements.py (bold)
   32px :
            spleen...................ezFBfont_32_spleen_16x32_block-elements.py
   64px :
            spleen...................ezFBfont_64_spleen_32x64_block-elements.py

character set: Box-drawing
--------------------------
    6px :
             fixed...............................ezFBfont_06_4x6_box-drawing.py
    7px :
             fixed...............................ezFBfont_07_5x7_box-drawing.py
    8px :
             fixed...............................ezFBfont_08_5x8_box-drawing.py
            spleen........................ezFBfont_08_spleen_5x8_box-drawing.py
           biwidth...............................ezFBfont_08_b10_box-drawing.py
           biwidth.............................ezFBfont_08_b10_b_box-drawing.py (bold)
    9px :
             fixed...............................ezFBfont_09_6x9_box-drawing.py
   10px :
           courier...........................ezFBfont_10_courR08_box-drawing.py (regular)
           courier...........................ezFBfont_10_courB08_box-drawing.py (bold)
             fixed..............................ezFBfont_10_6x10_box-drawing.py
   12px :
             fixed..............................ezFBfont_12_6x12_box-drawing.py
            spleen.......................ezFBfont_12_spleen_6x12_box-drawing.py
           biwidth...............................ezFBfont_12_b12_box-drawing.py
           biwidth.............................ezFBfont_12_b12_b_box-drawing.py (bold)
   13px :
             fixed..............................ezFBfont_13_8x13_box-drawing.py
             fixed..............................ezFBfont_13_7x13_box-drawing.py
             fixed..............................ezFBfont_13_6x13_box-drawing.py
   14px :
           courier...........................ezFBfont_14_courR10_box-drawing.py (regular)
             fixed..............................ezFBfont_14_7x14_box-drawing.py
           biwidth...............................ezFBfont_14_b14_box-drawing.py
           biwidth.............................ezFBfont_14_b14_b_box-drawing.py (bold)
   15px :
           courier...........................ezFBfont_15_courB12_box-drawing.py (bold)
           courier...........................ezFBfont_15_courB10_box-drawing.py (bold)
           courier...........................ezFBfont_15_courR12_box-drawing.py (regular)
             fixed..............................ezFBfont_15_9x15_box-drawing.py
   16px :
            spleen.......................ezFBfont_16_spleen_8x16_box-drawing.py
           biwidth...............................ezFBfont_16_b16_box-drawing.py
           biwidth.............................ezFBfont_16_b16_b_box-drawing.py (bold)
   17px :
           courier...........................ezFBfont_17_courR14_box-drawing.py (regular)
   18px :
           courier...........................ezFBfont_18_courB14_box-drawing.py (bold)
             fixed..............................ezFBfont_18_9x18_box-drawing.py
   20px :
             fixed.............................ezFBfont_20_10x20_box-drawing.py
   22px :
           courier...........................ezFBfont_22_courR18_box-drawing.py (regular)
   23px :
           courier...........................ezFBfont_23_courB18_box-drawing.py (bold)
   24px :
            spleen......................ezFBfont_24_spleen_12x24_box-drawing.py
   29px :
           courier...........................ezFBfont_29_courR24_box-drawing.py (regular)
   30px :
           courier...........................ezFBfont_30_courB24_box-drawing.py (bold)
   32px :
            spleen......................ezFBfont_32_spleen_16x32_box-drawing.py
   64px :
            spleen......................ezFBfont_64_spleen_32x64_box-drawing.py

character set: Lao
------------------
    1px :
          fixed4x6.................................ezFBfont_01_tom_thumb_lao.py
   14px :
           biwidth.....................................ezFBfont_14_b14_b_lao.py (bold)
           biwidth.......................................ezFBfont_14_b14_lao.py
   15px :
             fixed......................................ezFBfont_15_9x15_lao.py
   16px :
           biwidth.......................................ezFBfont_16_b16_lao.py
           biwidth.....................................ezFBfont_16_b16_b_lao.py (bold)

character set: Cherokee
-----------------------
    1px :
          fixed4x6............................ezFBfont_01_tom_thumb_cherokee.py
   11px :
             fixed.................................ezFBfont_11_9x18_cherokee.py

character set: Thai
-------------------
   13px :
             fixed.....................................ezFBfont_13_6x13_thai.py
             fixed.....................................ezFBfont_13_8x13_thai.py
             fixed.....................................ezFBfont_13_7x13_thai.py
   14px :
             fixed.....................................ezFBfont_14_7x14_thai.py
           biwidth......................................ezFBfont_14_b14_thai.py
           biwidth....................................ezFBfont_14_b14_b_thai.py (bold)
   15px :
             fixed.....................................ezFBfont_15_9x15_thai.py
   16px :
           biwidth......................................ezFBfont_16_b16_thai.py
           biwidth....................................ezFBfont_16_b16_b_thai.py (bold)
   18px :
             fixed.....................................ezFBfont_18_9x18_thai.py
   20px :
             fixed....................................ezFBfont_20_10x20_thai.py

character set: Arabic
---------------------
   15px :
             fixed...................................ezFBfont_15_9x15_arabic.py
           biwidth....................................ezFBfont_15_b16_arabic.py
           biwidth..................................ezFBfont_15_b16_b_arabic.py (bold)
   20px :
             fixed..................................ezFBfont_20_10x20_arabic.py

character set: Yijing-hexagram-symbols
--------------------------------------
   17px :
             fixed.................ezFBfont_17_10x20_yijing-hexagram-symbols.py

character set: Optical-character-recognition
--------------------------------------------
    8px :
             fixed............ezFBfont_08_6x12_optical-character-recognition.py
    9px :
             fixed............ezFBfont_09_8x13_optical-character-recognition.py
             fixed............ezFBfont_09_7x13_optical-character-recognition.py
             fixed............ezFBfont_09_6x13_optical-character-recognition.py
   10px :
           biwidth.............ezFBfont_10_b14_optical-character-recognition.py
           biwidth...........ezFBfont_10_b16_b_optical-character-recognition.py (bold)
           biwidth.............ezFBfont_10_b16_optical-character-recognition.py
           biwidth...........ezFBfont_10_b14_b_optical-character-recognition.py (bold)
   11px :
             fixed............ezFBfont_11_9x18_optical-character-recognition.py
             fixed............ezFBfont_11_9x15_optical-character-recognition.py
   13px :
             fixed...........ezFBfont_13_10x20_optical-character-recognition.py

character set: Latin-extended-c
-------------------------------
   11px :
             fixed.........................ezFBfont_11_6x12_latin-extended-c.py

character set: Control-pictures
-------------------------------
    3px :
           biwidth..........................ezFBfont_03_b14_control-pictures.py
           biwidth........................ezFBfont_03_b14_b_control-pictures.py (bold)
    6px :
             fixed..........................ezFBfont_06_4x6_control-pictures.py
             fixed..........................ezFBfont_06_5x7_control-pictures.py
    8px :
             fixed..........................ezFBfont_08_5x8_control-pictures.py
             fixed..........................ezFBfont_08_6x9_control-pictures.py
           biwidth..........................ezFBfont_08_b10_control-pictures.py
           biwidth........................ezFBfont_08_b10_b_control-pictures.py (bold)
    9px :
             fixed.........................ezFBfont_09_8x13_control-pictures.py
             fixed.........................ezFBfont_09_6x10_control-pictures.py
   10px :
           biwidth........................ezFBfont_10_b16_b_control-pictures.py (bold)
           biwidth..........................ezFBfont_10_b16_control-pictures.py
   11px :
             fixed.........................ezFBfont_11_9x18_control-pictures.py
             fixed.........................ezFBfont_11_9x15_control-pictures.py
           biwidth........................ezFBfont_11_b12_b_control-pictures.py (bold)
           biwidth..........................ezFBfont_11_b12_control-pictures.py
   12px :
             fixed.........................ezFBfont_12_6x12_control-pictures.py
   13px :
             fixed.........................ezFBfont_13_7x14_control-pictures.py
             fixed.........................ezFBfont_13_7x13_control-pictures.py
             fixed.........................ezFBfont_13_6x13_control-pictures.py
   15px :
             fixed........................ezFBfont_15_10x20_control-pictures.py

character set: Cyrillic
-----------------------
    6px :
             fixed..................................ezFBfont_06_4x6_cyrillic.py
    7px :
             fixed..................................ezFBfont_07_5x7_cyrillic.py
    8px :
             fixed..................................ezFBfont_08_5x8_cyrillic.py
           biwidth..................................ezFBfont_08_b10_cyrillic.py
           biwidth................................ezFBfont_08_b10_b_cyrillic.py (bold)
    9px :
             fixed..................................ezFBfont_09_6x9_cyrillic.py
   10px :
             fixed.................................ezFBfont_10_6x10_cyrillic.py
   12px :
             fixed.................................ezFBfont_12_6x12_cyrillic.py
           biwidth..................................ezFBfont_12_b12_cyrillic.py
           biwidth................................ezFBfont_12_b12_b_cyrillic.py (bold)
   13px :
             fixed.................................ezFBfont_13_8x13_cyrillic.py
             fixed.................................ezFBfont_13_6x13_cyrillic.py
             fixed.................................ezFBfont_13_7x13_cyrillic.py
   14px :
             fixed.................................ezFBfont_14_7x14_cyrillic.py
           biwidth................................ezFBfont_14_b14_b_cyrillic.py (bold)
           biwidth..................................ezFBfont_14_b14_cyrillic.py
   15px :
             fixed.................................ezFBfont_15_9x15_cyrillic.py
   16px :
           biwidth................................ezFBfont_16_b16_b_cyrillic.py (bold)
           biwidth..................................ezFBfont_16_b16_cyrillic.py
   17px :
             fixed.................................ezFBfont_17_9x18_cyrillic.py
   20px :
             fixed................................ezFBfont_20_10x20_cyrillic.py

character set: Number-forms
---------------------------
    6px :
             fixed..............................ezFBfont_06_4x6_number-forms.py
    7px :
             fixed..............................ezFBfont_07_5x7_number-forms.py
             fixed..............................ezFBfont_07_5x8_number-forms.py
    8px :
             fixed..............................ezFBfont_08_6x9_number-forms.py
    9px :
           biwidth..............................ezFBfont_09_b10_number-forms.py
           biwidth............................ezFBfont_09_b10_b_number-forms.py (bold)
   10px :
             fixed.............................ezFBfont_10_7x13_number-forms.py
             fixed.............................ezFBfont_10_9x18_number-forms.py
             fixed.............................ezFBfont_10_9x15_number-forms.py
             fixed.............................ezFBfont_10_7x14_number-forms.py
             fixed.............................ezFBfont_10_8x13_number-forms.py
             fixed.............................ezFBfont_10_6x10_number-forms.py
             fixed.............................ezFBfont_10_6x13_number-forms.py
   11px :
             fixed.............................ezFBfont_11_6x12_number-forms.py
           biwidth............................ezFBfont_11_b16_b_number-forms.py (bold)
           biwidth..............................ezFBfont_11_b16_number-forms.py
   12px :
           biwidth..............................ezFBfont_12_b14_number-forms.py
           biwidth..............................ezFBfont_12_b12_number-forms.py
           biwidth............................ezFBfont_12_b14_b_number-forms.py (bold)
           biwidth............................ezFBfont_12_b12_b_number-forms.py (bold)
   16px :
             fixed............................ezFBfont_16_10x20_number-forms.py

character set: Georgian
-----------------------
   12px :
             fixed.................................ezFBfont_12_7x13_georgian.py
             fixed.................................ezFBfont_12_6x13_georgian.py
             fixed.................................ezFBfont_12_8x13_georgian.py
           biwidth................................ezFBfont_12_b14_b_georgian.py (bold)
           biwidth..................................ezFBfont_12_b14_georgian.py
   14px :
           biwidth................................ezFBfont_14_b16_b_georgian.py (bold)
           biwidth..................................ezFBfont_14_b16_georgian.py
   15px :
             fixed.................................ezFBfont_15_9x15_georgian.py
             fixed.................................ezFBfont_15_9x18_georgian.py
   20px :
             fixed................................ezFBfont_20_10x20_georgian.py

character set: Supplemental-mathematical-operators
--------------------------------------------------
   11px :
             fixed......ezFBfont_11_8x13_supplemental-mathematical-operators.py
             fixed......ezFBfont_11_7x13_supplemental-mathematical-operators.py
             fixed......ezFBfont_11_6x13_supplemental-mathematical-operators.py
   12px :
             fixed......ezFBfont_12_9x18_supplemental-mathematical-operators.py
             fixed......ezFBfont_12_6x12_supplemental-mathematical-operators.py
   15px :
             fixed......ezFBfont_15_9x15_supplemental-mathematical-operators.py
   17px :
             fixed.....ezFBfont_17_10x20_supplemental-mathematical-operators.py

character set: Halfwidth-and-fullwidth-forms
--------------------------------------------
   10px :
           biwidth.............ezFBfont_10_b10_halfwidth-and-fullwidth-forms.py
           biwidth...........ezFBfont_10_b10_b_halfwidth-and-fullwidth-forms.py (bold)
   11px :
             fixed............ezFBfont_11_8x13_halfwidth-and-fullwidth-forms.py
   12px :
           biwidth...........ezFBfont_12_b12_b_halfwidth-and-fullwidth-forms.py (bold)
           biwidth.............ezFBfont_12_b12_halfwidth-and-fullwidth-forms.py
   13px :
             fixed............ezFBfont_13_9x15_halfwidth-and-fullwidth-forms.py
             fixed............ezFBfont_13_6x13_halfwidth-and-fullwidth-forms.py
             fixed............ezFBfont_13_7x14_halfwidth-and-fullwidth-forms.py
   14px :
             fixed...........ezFBfont_14_10x20_halfwidth-and-fullwidth-forms.py
           biwidth.............ezFBfont_14_b14_halfwidth-and-fullwidth-forms.py
           biwidth...........ezFBfont_14_b14_b_halfwidth-and-fullwidth-forms.py (bold)
   16px :
             fixed............ezFBfont_16_9x18_halfwidth-and-fullwidth-forms.py
           biwidth...........ezFBfont_16_b16_b_halfwidth-and-fullwidth-forms.py (bold)
           biwidth.............ezFBfont_16_b16_halfwidth-and-fullwidth-forms.py

character set: Arabic-presentation-forms-b
------------------------------------------
   15px :
             fixed..............ezFBfont_15_9x15_arabic-presentation-forms-b.py
   20px :
             fixed.............ezFBfont_20_10x20_arabic-presentation-forms-b.py

character set: Combining-diacritical-marks
------------------------------------------
    7px :
             fixed...............ezFBfont_07_5x7_combining-diacritical-marks.py
    8px :
             fixed...............ezFBfont_08_5x8_combining-diacritical-marks.py
    9px :
             fixed...............ezFBfont_09_6x9_combining-diacritical-marks.py
           biwidth...............ezFBfont_09_b10_combining-diacritical-marks.py
           biwidth.............ezFBfont_09_b10_b_combining-diacritical-marks.py (bold)
   10px :
             fixed..............ezFBfont_10_6x10_combining-diacritical-marks.py
   12px :
             fixed..............ezFBfont_12_6x12_combining-diacritical-marks.py
           biwidth...............ezFBfont_12_b12_combining-diacritical-marks.py
           biwidth.............ezFBfont_12_b12_b_combining-diacritical-marks.py (bold)
   13px :
             fixed..............ezFBfont_13_7x13_combining-diacritical-marks.py
             fixed..............ezFBfont_13_6x13_combining-diacritical-marks.py
             fixed..............ezFBfont_13_8x13_combining-diacritical-marks.py
   14px :
             fixed..............ezFBfont_14_7x14_combining-diacritical-marks.py
           biwidth...............ezFBfont_14_b14_combining-diacritical-marks.py
           biwidth.............ezFBfont_14_b14_b_combining-diacritical-marks.py (bold)
   15px :
             fixed..............ezFBfont_15_9x15_combining-diacritical-marks.py
   16px :
           biwidth.............ezFBfont_16_b16_b_combining-diacritical-marks.py (bold)
           biwidth...............ezFBfont_16_b16_combining-diacritical-marks.py
   18px :
             fixed..............ezFBfont_18_9x18_combining-diacritical-marks.py
   20px :
             fixed.............ezFBfont_20_10x20_combining-diacritical-marks.py

character set: Runic
--------------------
    6px :
             fixed.....................................ezFBfont_06_5x7_runic.py
           biwidth...................................ezFBfont_06_b10_b_runic.py (bold)
           biwidth.....................................ezFBfont_06_b10_runic.py
    7px :
             fixed....................................ezFBfont_07_6x10_runic.py
    9px :
             fixed....................................ezFBfont_09_7x13_runic.py
   10px :
             fixed....................................ezFBfont_10_7x14_runic.py
             fixed....................................ezFBfont_10_6x12_runic.py
           biwidth...................................ezFBfont_10_b14_b_runic.py (bold)
           biwidth.....................................ezFBfont_10_b14_runic.py
   11px :
             fixed....................................ezFBfont_11_8x13_runic.py
             fixed....................................ezFBfont_11_9x15_runic.py
             fixed....................................ezFBfont_11_9x18_runic.py
             fixed....................................ezFBfont_11_6x13_runic.py
           biwidth...................................ezFBfont_11_b16_b_runic.py (bold)
           biwidth.....................................ezFBfont_11_b16_runic.py
   15px :
             fixed...................................ezFBfont_15_10x20_runic.py

character set: Unified-canadian-aboriginal-syllabics
----------------------------------------------------
   14px :
             fixed....ezFBfont_14_9x18_unified-canadian-aboriginal-syllabics.py

character set: Supplemental-punctuation
---------------------------------------
   11px :
             fixed.................ezFBfont_11_6x13_supplemental-punctuation.py
   12px :
             fixed.................ezFBfont_12_9x15_supplemental-punctuation.py
             fixed.................ezFBfont_12_9x18_supplemental-punctuation.py

character set: Ethiopic
-----------------------
   13px :
             fixed.................................ezFBfont_13_9x15_ethiopic.py
             fixed.................................ezFBfont_13_9x18_ethiopic.py
   17px :
             fixed................................ezFBfont_17_10x20_ethiopic.py

character set: Enclosed-alphanumerics
-------------------------------------
    9px :
             fixed...................ezFBfont_09_6x13_enclosed-alphanumerics.py
   10px :
           biwidth....................ezFBfont_10_b10_enclosed-alphanumerics.py
           biwidth..................ezFBfont_10_b10_b_enclosed-alphanumerics.py (bold)
   11px :
             fixed...................ezFBfont_11_6x12_enclosed-alphanumerics.py
   12px :
           biwidth....................ezFBfont_12_b12_enclosed-alphanumerics.py
           biwidth..................ezFBfont_12_b12_b_enclosed-alphanumerics.py (bold)
   13px :
             fixed...................ezFBfont_13_9x15_enclosed-alphanumerics.py
             fixed..................ezFBfont_13_10x20_enclosed-alphanumerics.py
             fixed...................ezFBfont_13_9x18_enclosed-alphanumerics.py
   14px :
           biwidth..................ezFBfont_14_b14_b_enclosed-alphanumerics.py (bold)
           biwidth....................ezFBfont_14_b14_enclosed-alphanumerics.py
   16px :
           biwidth....................ezFBfont_16_b16_enclosed-alphanumerics.py
           biwidth..................ezFBfont_16_b16_b_enclosed-alphanumerics.py (bold)

character set: Combining-diacritical-marks-for-symbols
------------------------------------------------------
    7px :
             fixed...ezFBfont_07_5x7_combining-diacritical-marks-for-symbols.py
    8px :
             fixed...ezFBfont_08_5x8_combining-diacritical-marks-for-symbols.py
           biwidth.ezFBfont_08_b10_b_combining-diacritical-marks-for-symbols.py (bold)
           biwidth...ezFBfont_08_b10_combining-diacritical-marks-for-symbols.py
    9px :
             fixed...ezFBfont_09_6x9_combining-diacritical-marks-for-symbols.py
   10px :
             fixed..ezFBfont_10_6x10_combining-diacritical-marks-for-symbols.py
   12px :
             fixed..ezFBfont_12_6x12_combining-diacritical-marks-for-symbols.py
           biwidth...ezFBfont_12_b12_combining-diacritical-marks-for-symbols.py
           biwidth.ezFBfont_12_b12_b_combining-diacritical-marks-for-symbols.py (bold)
   13px :
             fixed..ezFBfont_13_6x13_combining-diacritical-marks-for-symbols.py
             fixed..ezFBfont_13_8x13_combining-diacritical-marks-for-symbols.py
             fixed..ezFBfont_13_7x14_combining-diacritical-marks-for-symbols.py
             fixed..ezFBfont_13_7x13_combining-diacritical-marks-for-symbols.py
           biwidth.ezFBfont_13_b14_b_combining-diacritical-marks-for-symbols.py (bold)
           biwidth...ezFBfont_13_b14_combining-diacritical-marks-for-symbols.py
   15px :
             fixed..ezFBfont_15_9x15_combining-diacritical-marks-for-symbols.py
           biwidth.ezFBfont_15_b16_b_combining-diacritical-marks-for-symbols.py (bold)
           biwidth...ezFBfont_15_b16_combining-diacritical-marks-for-symbols.py
   18px :
             fixed..ezFBfont_18_9x18_combining-diacritical-marks-for-symbols.py
   20px :
             fixed.ezFBfont_20_10x20_combining-diacritical-marks-for-symbols.py

character set: Arabic-presentation-forms-a
------------------------------------------
   15px :
             fixed..............ezFBfont_15_9x15_arabic-presentation-forms-a.py
   20px :
             fixed.............ezFBfont_20_10x20_arabic-presentation-forms-a.py

character set: Specials
-----------------------
    1px :
           biwidth..................................ezFBfont_01_b14_specials.py
           biwidth................................ezFBfont_01_b14_b_specials.py (bold)
    6px :
             fixed..................................ezFBfont_06_4x6_specials.py
    7px :
             fixed..................................ezFBfont_07_5x7_specials.py
    8px :
             fixed..................................ezFBfont_08_5x8_specials.py
             fixed.................................ezFBfont_08_6x10_specials.py
           biwidth..................................ezFBfont_08_b10_specials.py
           biwidth................................ezFBfont_08_b10_b_specials.py (bold)
    9px :
             fixed.................................ezFBfont_09_6x12_specials.py
             fixed..................................ezFBfont_09_6x9_specials.py
             fixed.................................ezFBfont_09_7x13_specials.py
             fixed.................................ezFBfont_09_8x13_specials.py
           biwidth..................................ezFBfont_09_b12_specials.py
           biwidth................................ezFBfont_09_b12_b_specials.py (bold)
   10px :
             fixed.................................ezFBfont_10_7x14_specials.py
             fixed.................................ezFBfont_10_9x15_specials.py
             fixed.................................ezFBfont_10_9x18_specials.py
   11px :
           biwidth................................ezFBfont_11_b16_b_specials.py (bold)
           biwidth..................................ezFBfont_11_b16_specials.py
   13px :
             fixed.................................ezFBfont_13_6x13_specials.py
             fixed................................ezFBfont_13_10x20_specials.py

character set: Hangul-jamo
--------------------------
    8px :
             fixed..............................ezFBfont_08_6x13_hangul-jamo.py
   14px :
           biwidth...............................ezFBfont_14_b14_hangul-jamo.py
           biwidth.............................ezFBfont_14_b14_b_hangul-jamo.py (bold)

character set: Variation-selectors
----------------------------------
    1px :
             fixed.....................ezFBfont_01_10x20_variation-selectors.py

character set: Ogham
--------------------
   10px :
             fixed....................................ezFBfont_10_6x12_ogham.py
             fixed....................................ezFBfont_10_6x13_ogham.py
   15px :
             fixed...................................ezFBfont_15_10x20_ogham.py

character set: Greek-extended
-----------------------------
    7px :
             fixed............................ezFBfont_07_5x7_greek-extended.py
           biwidth............................ezFBfont_07_b10_greek-extended.py
           biwidth..........................ezFBfont_07_b10_b_greek-extended.py (bold)
    9px :
           biwidth..........................ezFBfont_09_b12_b_greek-extended.py (bold)
           biwidth............................ezFBfont_09_b12_greek-extended.py
   10px :
             fixed...........................ezFBfont_10_6x10_greek-extended.py
   12px :
             fixed...........................ezFBfont_12_6x12_greek-extended.py
   13px :
             fixed...........................ezFBfont_13_7x13_greek-extended.py
             fixed...........................ezFBfont_13_6x13_greek-extended.py
             fixed...........................ezFBfont_13_8x13_greek-extended.py
   14px :
             fixed...........................ezFBfont_14_7x14_greek-extended.py
           biwidth..........................ezFBfont_14_b14_b_greek-extended.py (bold)
           biwidth............................ezFBfont_14_b14_greek-extended.py
   15px :
             fixed...........................ezFBfont_15_9x15_greek-extended.py
   16px :
           biwidth..........................ezFBfont_16_b16_b_greek-extended.py (bold)
           biwidth............................ezFBfont_16_b16_greek-extended.py
   17px :
             fixed...........................ezFBfont_17_9x18_greek-extended.py
   19px :
             fixed..........................ezFBfont_19_10x20_greek-extended.py

character set: Armenian
-----------------------
   12px :
             fixed.................................ezFBfont_12_8x13_armenian.py
             fixed.................................ezFBfont_12_7x14_armenian.py
             fixed.................................ezFBfont_12_6x13_armenian.py
             fixed.................................ezFBfont_12_6x12_armenian.py
             fixed.................................ezFBfont_12_7x13_armenian.py
   14px :
           biwidth..................................ezFBfont_14_b14_armenian.py
           biwidth................................ezFBfont_14_b14_b_armenian.py (bold)
   15px :
             fixed.................................ezFBfont_15_9x15_armenian.py
             fixed.................................ezFBfont_15_9x18_armenian.py
   16px :
           biwidth................................ezFBfont_16_b16_b_armenian.py (bold)
           biwidth..................................ezFBfont_16_b16_armenian.py
   17px :
             fixed................................ezFBfont_17_10x20_armenian.py

character set: Cyrillic-extended-a
----------------------------------
    6px :
             fixed......................ezFBfont_06_6x12_cyrillic-extended-a.py

character set: Phonetic-extensions
----------------------------------
   19px :
             fixed.....................ezFBfont_19_10x20_phonetic-extensions.py

character set: Cyrillic-supplement
----------------------------------
    9px :
             fixed......................ezFBfont_09_6x12_cyrillic-supplement.py
   11px :
             fixed......................ezFBfont_11_6x13_cyrillic-supplement.py
             fixed......................ezFBfont_11_8x13_cyrillic-supplement.py
   12px :
             fixed......................ezFBfont_12_7x14_cyrillic-supplement.py
             fixed......................ezFBfont_12_9x15_cyrillic-supplement.py
             fixed......................ezFBfont_12_9x18_cyrillic-supplement.py
   17px :
             fixed.....................ezFBfont_17_10x20_cyrillic-supplement.py

character set: Alphabetic-presentation-forms
--------------------------------------------
    6px :
             fixed.............ezFBfont_06_5x7_alphabetic-presentation-forms.py
             fixed.............ezFBfont_06_5x8_alphabetic-presentation-forms.py
             fixed.............ezFBfont_06_6x9_alphabetic-presentation-forms.py
           biwidth...........ezFBfont_06_b10_b_alphabetic-presentation-forms.py (bold)
           biwidth.............ezFBfont_06_b10_alphabetic-presentation-forms.py
    7px :
             fixed............ezFBfont_07_6x10_alphabetic-presentation-forms.py
             fixed............ezFBfont_07_6x12_alphabetic-presentation-forms.py
           biwidth...........ezFBfont_07_b12_b_alphabetic-presentation-forms.py (bold)
           biwidth.............ezFBfont_07_b12_alphabetic-presentation-forms.py
   11px :
             fixed............ezFBfont_11_7x13_alphabetic-presentation-forms.py
   12px :
             fixed............ezFBfont_12_8x13_alphabetic-presentation-forms.py
             fixed............ezFBfont_12_7x14_alphabetic-presentation-forms.py
             fixed............ezFBfont_12_6x13_alphabetic-presentation-forms.py
           biwidth...........ezFBfont_12_b14_b_alphabetic-presentation-forms.py (bold)
           biwidth.............ezFBfont_12_b14_alphabetic-presentation-forms.py
   14px :
           biwidth...........ezFBfont_14_b16_b_alphabetic-presentation-forms.py (bold)
           biwidth.............ezFBfont_14_b16_alphabetic-presentation-forms.py
   15px :
             fixed............ezFBfont_15_9x15_alphabetic-presentation-forms.py
   16px :
             fixed............ezFBfont_16_9x18_alphabetic-presentation-forms.py
   19px :
             fixed...........ezFBfont_19_10x20_alphabetic-presentation-forms.py

character set: Braille-patterns
-------------------------------
    7px :
             fixed..........................ezFBfont_07_5x7_braille-patterns.py
             fixed.........................ezFBfont_07_6x10_braille-patterns.py
             fixed..........................ezFBfont_07_5x8_braille-patterns.py
             fixed..........................ezFBfont_07_6x9_braille-patterns.py
            spleen...................ezFBfont_07_spleen_5x8_braille-patterns.py
           biwidth..........................ezFBfont_07_b10_braille-patterns.py
           biwidth........................ezFBfont_07_b10_b_braille-patterns.py (bold)
   10px :
            spleen..................ezFBfont_10_spleen_6x12_braille-patterns.py
   11px :
             fixed.........................ezFBfont_11_7x14_braille-patterns.py
             fixed.........................ezFBfont_11_9x15_braille-patterns.py
             fixed.........................ezFBfont_11_8x13_braille-patterns.py
             fixed.........................ezFBfont_11_9x18_braille-patterns.py
             fixed.........................ezFBfont_11_6x13_braille-patterns.py
             fixed.........................ezFBfont_11_7x13_braille-patterns.py
             fixed.........................ezFBfont_11_6x12_braille-patterns.py
           biwidth........................ezFBfont_11_b16_b_braille-patterns.py (bold)
           biwidth..........................ezFBfont_11_b16_braille-patterns.py
           biwidth..........................ezFBfont_11_b14_braille-patterns.py
           biwidth........................ezFBfont_11_b12_b_braille-patterns.py (bold)
           biwidth..........................ezFBfont_11_b12_braille-patterns.py
           biwidth........................ezFBfont_11_b14_b_braille-patterns.py (bold)
   14px :
            spleen..................ezFBfont_14_spleen_8x16_braille-patterns.py
   15px :
             fixed........................ezFBfont_15_10x20_braille-patterns.py
   22px :
            spleen.................ezFBfont_22_spleen_12x24_braille-patterns.py
   28px :
            spleen.................ezFBfont_28_spleen_16x32_braille-patterns.py
   56px :
            spleen.................ezFBfont_56_spleen_32x64_braille-patterns.py

character set: Supplemental-arrows-a
------------------------------------
    7px :
             fixed....................ezFBfont_07_6x12_supplemental-arrows-a.py
             fixed....................ezFBfont_07_6x13_supplemental-arrows-a.py
             fixed....................ezFBfont_07_7x13_supplemental-arrows-a.py
    9px :
             fixed....................ezFBfont_09_8x13_supplemental-arrows-a.py
             fixed...................ezFBfont_09_10x20_supplemental-arrows-a.py
   12px :
             fixed....................ezFBfont_12_9x15_supplemental-arrows-a.py
             fixed....................ezFBfont_12_9x18_supplemental-arrows-a.py

character set: Miscellaneous-mathematical-symbols-a
---------------------------------------------------
    6px :
             fixed......ezFBfont_06_5x8_miscellaneous-mathematical-symbols-a.py
             fixed......ezFBfont_06_5x7_miscellaneous-mathematical-symbols-a.py
    7px :
             fixed.....ezFBfont_07_6x10_miscellaneous-mathematical-symbols-a.py
             fixed......ezFBfont_07_6x9_miscellaneous-mathematical-symbols-a.py
   11px :
             fixed.....ezFBfont_11_6x13_miscellaneous-mathematical-symbols-a.py
             fixed.....ezFBfont_11_7x13_miscellaneous-mathematical-symbols-a.py
             fixed.....ezFBfont_11_8x13_miscellaneous-mathematical-symbols-a.py
   12px :
             fixed.....ezFBfont_12_9x18_miscellaneous-mathematical-symbols-a.py
             fixed.....ezFBfont_12_6x12_miscellaneous-mathematical-symbols-a.py
   13px :
             fixed.....ezFBfont_13_9x15_miscellaneous-mathematical-symbols-a.py
             fixed....ezFBfont_13_10x20_miscellaneous-mathematical-symbols-a.py
   14px :
             fixed.....ezFBfont_14_7x14_miscellaneous-mathematical-symbols-a.py

character set: Combining-half-marks
-----------------------------------
    2px :
             fixed.....................ezFBfont_02_6x13_combining-half-marks.py
             fixed.....................ezFBfont_02_7x13_combining-half-marks.py
             fixed.....................ezFBfont_02_8x13_combining-half-marks.py
             fixed.....................ezFBfont_02_6x12_combining-half-marks.py
           biwidth....................ezFBfont_02_b12_b_combining-half-marks.py (bold)
           biwidth......................ezFBfont_02_b12_combining-half-marks.py
    3px :
             fixed....................ezFBfont_03_10x20_combining-half-marks.py
             fixed.....................ezFBfont_03_9x15_combining-half-marks.py
             fixed.....................ezFBfont_03_9x18_combining-half-marks.py
           biwidth....................ezFBfont_03_b16_b_combining-half-marks.py (bold)
           biwidth......................ezFBfont_03_b16_combining-half-marks.py

character set: Private-use-area
-------------------------------
    8px :
            spleen...................ezFBfont_08_spleen_5x8_private-use-area.py
   12px :
             fixed.........................ezFBfont_12_6x13_private-use-area.py
            spleen..................ezFBfont_12_spleen_6x12_private-use-area.py
   13px :
             fixed.........................ezFBfont_13_9x15_private-use-area.py
   16px :
            spleen..................ezFBfont_16_spleen_8x16_private-use-area.py
   24px :
            spleen.................ezFBfont_24_spleen_12x24_private-use-area.py
   32px :
            spleen.................ezFBfont_32_spleen_16x32_private-use-area.py
   64px :
            spleen.................ezFBfont_64_spleen_32x64_private-use-area.py

character set: Hebrew
---------------------
    5px :
             fixed....................................ezFBfont_05_5x7_hebrew.py
             fixed....................................ezFBfont_05_5x8_hebrew.py
           biwidth....................................ezFBfont_05_b10_hebrew.py
           biwidth..................................ezFBfont_05_b10_b_hebrew.py (bold)
    6px :
             fixed....................................ezFBfont_06_4x6_hebrew.py
    8px :
             fixed....................................ezFBfont_08_6x9_hebrew.py
    9px :
             fixed...................................ezFBfont_09_6x10_hebrew.py
   10px :
           biwidth....................................ezFBfont_10_b12_hebrew.py
           biwidth..................................ezFBfont_10_b12_b_hebrew.py (bold)
   11px :
             fixed...................................ezFBfont_11_7x13_hebrew.py
   12px :
             fixed...................................ezFBfont_12_7x14_hebrew.py
             fixed...................................ezFBfont_12_8x13_hebrew.py
             fixed...................................ezFBfont_12_6x12_hebrew.py
   13px :
             fixed...................................ezFBfont_13_6x13_hebrew.py
           biwidth....................................ezFBfont_13_b14_hebrew.py
           biwidth..................................ezFBfont_13_b14_b_hebrew.py (bold)
   14px :
             fixed...................................ezFBfont_14_9x15_hebrew.py
   15px :
             fixed...................................ezFBfont_15_9x18_hebrew.py
   16px :
           biwidth..................................ezFBfont_16_b16_b_hebrew.py (bold)
           biwidth....................................ezFBfont_16_b16_hebrew.py
   19px :
             fixed..................................ezFBfont_19_10x20_hebrew.py

character set: Miscellaneous-symbols-and-arrows
-----------------------------------------------
   11px :
             fixed.........ezFBfont_11_6x12_miscellaneous-symbols-and-arrows.py
   13px :
             fixed........ezFBfont_13_10x20_miscellaneous-symbols-and-arrows.py

character set: Supplemental-arrows-b
------------------------------------
    7px :
             fixed....................ezFBfont_07_9x15_supplemental-arrows-b.py
             fixed....................ezFBfont_07_6x13_supplemental-arrows-b.py
   10px :
             fixed....................ezFBfont_10_6x12_supplemental-arrows-b.py

character set: Dingbats
-----------------------
    9px :
           biwidth................................ezFBfont_09_b10_b_dingbats.py (bold)
           biwidth..................................ezFBfont_09_b10_dingbats.py
   10px :
             fixed.................................ezFBfont_10_6x12_dingbats.py
   11px :
           biwidth................................ezFBfont_11_b12_b_dingbats.py (bold)
           biwidth..................................ezFBfont_11_b12_dingbats.py
   13px :
             fixed.................................ezFBfont_13_9x18_dingbats.py
             fixed................................ezFBfont_13_10x20_dingbats.py
             fixed.................................ezFBfont_13_9x15_dingbats.py
             fixed.................................ezFBfont_13_6x13_dingbats.py
   14px :
           biwidth................................ezFBfont_14_b14_b_dingbats.py (bold)
           biwidth..................................ezFBfont_14_b14_dingbats.py
   16px :
           biwidth................................ezFBfont_16_b16_b_dingbats.py (bold)
           biwidth..................................ezFBfont_16_b16_dingbats.py

character set: Miscellaneous-mathematical-symbols-b
---------------------------------------------------
   11px :
             fixed.....ezFBfont_11_6x12_miscellaneous-mathematical-symbols-b.py
   12px :
             fixed.....ezFBfont_12_6x13_miscellaneous-mathematical-symbols-b.py

character set: Cjk-compatibility-forms
--------------------------------------
    9px :
           biwidth.................ezFBfont_09_b10_b_cjk-compatibility-forms.py (bold)
           biwidth...................ezFBfont_09_b10_cjk-compatibility-forms.py
   11px :
           biwidth.................ezFBfont_11_b12_b_cjk-compatibility-forms.py (bold)
           biwidth...................ezFBfont_11_b12_cjk-compatibility-forms.py
   13px :
           biwidth...................ezFBfont_13_b14_cjk-compatibility-forms.py
           biwidth.................ezFBfont_13_b14_b_cjk-compatibility-forms.py (bold)
   15px :
           biwidth.................ezFBfont_15_b16_b_cjk-compatibility-forms.py (bold)
           biwidth...................ezFBfont_15_b16_cjk-compatibility-forms.py

character set: Cjk-unified-ideographs
-------------------------------------
   10px :
           biwidth..................ezFBfont_10_b10_b_cjk-unified-ideographs.py (bold)
           biwidth....................ezFBfont_10_b10_cjk-unified-ideographs.py
   12px :
           biwidth....................ezFBfont_12_b12_cjk-unified-ideographs.py
           biwidth..................ezFBfont_12_b12_b_cjk-unified-ideographs.py (bold)
   14px :
           biwidth..................ezFBfont_14_b14_b_cjk-unified-ideographs.py (bold)
           biwidth....................ezFBfont_14_b14_cjk-unified-ideographs.py
   16px :
           biwidth..................ezFBfont_16_b16_b_cjk-unified-ideographs.py (bold)
           biwidth....................ezFBfont_16_b16_cjk-unified-ideographs.py

character set: Cjk-symbols-and-punctuation
------------------------------------------
   10px :
           biwidth...............ezFBfont_10_b10_cjk-symbols-and-punctuation.py
           biwidth.............ezFBfont_10_b10_b_cjk-symbols-and-punctuation.py (bold)
   12px :
           biwidth...............ezFBfont_12_b12_cjk-symbols-and-punctuation.py
           biwidth.............ezFBfont_12_b12_b_cjk-symbols-and-punctuation.py (bold)
   14px :
           biwidth.............ezFBfont_14_b14_b_cjk-symbols-and-punctuation.py (bold)
           biwidth...............ezFBfont_14_b14_cjk-symbols-and-punctuation.py
   16px :
           biwidth.............ezFBfont_16_b16_b_cjk-symbols-and-punctuation.py (bold)
           biwidth...............ezFBfont_16_b16_cjk-symbols-and-punctuation.py

character set: Devanagari
-------------------------
   16px :
           biwidth................................ezFBfont_16_b16_devanagari.py
           biwidth..............................ezFBfont_16_b16_b_devanagari.py (bold)

character set: Katakana
-----------------------
    9px :
           biwidth................................ezFBfont_09_b10_b_katakana.py (bold)
           biwidth..................................ezFBfont_09_b10_katakana.py
   12px :
           biwidth..................................ezFBfont_12_b12_katakana.py
           biwidth................................ezFBfont_12_b12_b_katakana.py (bold)
   14px :
           biwidth..................................ezFBfont_14_b14_katakana.py
           biwidth................................ezFBfont_14_b14_b_katakana.py (bold)
   16px :
           biwidth..................................ezFBfont_16_b16_katakana.py
           biwidth................................ezFBfont_16_b16_b_katakana.py (bold)

character set: Bopomofo
-----------------------
    9px :
           biwidth................................ezFBfont_09_b10_b_bopomofo.py (bold)
           biwidth..................................ezFBfont_09_b10_bopomofo.py
   11px :
           biwidth..................................ezFBfont_11_b12_bopomofo.py
           biwidth................................ezFBfont_11_b12_b_bopomofo.py (bold)
   13px :
           biwidth................................ezFBfont_13_b14_b_bopomofo.py (bold)
           biwidth..................................ezFBfont_13_b14_bopomofo.py
   15px :
           biwidth..................................ezFBfont_15_b16_bopomofo.py
           biwidth................................ezFBfont_15_b16_b_bopomofo.py (bold)

character set: Enclosed-cjk-letters-and-months
----------------------------------------------
   10px :
           biwidth...........ezFBfont_10_b10_enclosed-cjk-letters-and-months.py
           biwidth.........ezFBfont_10_b10_b_enclosed-cjk-letters-and-months.py (bold)
   12px :
           biwidth.........ezFBfont_12_b12_b_enclosed-cjk-letters-and-months.py (bold)
           biwidth...........ezFBfont_12_b12_enclosed-cjk-letters-and-months.py
   14px :
           biwidth...........ezFBfont_14_b14_enclosed-cjk-letters-and-months.py
           biwidth.........ezFBfont_14_b14_b_enclosed-cjk-letters-and-months.py (bold)
   16px :
           biwidth.........ezFBfont_16_b16_b_enclosed-cjk-letters-and-months.py (bold)
           biwidth...........ezFBfont_16_b16_enclosed-cjk-letters-and-months.py

character set: Hangul-syllables
-------------------------------
    9px :
           biwidth........................ezFBfont_09_b10_b_hangul-syllables.py (bold)
           biwidth..........................ezFBfont_09_b10_hangul-syllables.py
   11px :
           biwidth..........................ezFBfont_11_b12_hangul-syllables.py
           biwidth........................ezFBfont_11_b12_b_hangul-syllables.py (bold)
   14px :
           biwidth..........................ezFBfont_14_b14_hangul-syllables.py
           biwidth........................ezFBfont_14_b14_b_hangul-syllables.py (bold)
   16px :
           biwidth..........................ezFBfont_16_b16_hangul-syllables.py
           biwidth........................ezFBfont_16_b16_b_hangul-syllables.py (bold)

character set: Cjk-compatibility
--------------------------------
   10px :
           biwidth.........................ezFBfont_10_b10_cjk-compatibility.py
           biwidth.......................ezFBfont_10_b10_b_cjk-compatibility.py (bold)
   12px :
           biwidth.........................ezFBfont_12_b12_cjk-compatibility.py
           biwidth.......................ezFBfont_12_b12_b_cjk-compatibility.py (bold)
   14px :
           biwidth.......................ezFBfont_14_b14_b_cjk-compatibility.py (bold)
           biwidth.........................ezFBfont_14_b14_cjk-compatibility.py
   16px :
           biwidth.......................ezFBfont_16_b16_b_cjk-compatibility.py (bold)
           biwidth.........................ezFBfont_16_b16_cjk-compatibility.py

character set: Hiragana
-----------------------
    9px :
           biwidth..................................ezFBfont_09_b10_hiragana.py
           biwidth................................ezFBfont_09_b10_b_hiragana.py (bold)
   12px :
           biwidth................................ezFBfont_12_b12_b_hiragana.py (bold)
           biwidth..................................ezFBfont_12_b12_hiragana.py
   14px :
           biwidth..................................ezFBfont_14_b14_hiragana.py
           biwidth................................ezFBfont_14_b14_b_hiragana.py (bold)
   16px :
           biwidth..................................ezFBfont_16_b16_hiragana.py
           biwidth................................ezFBfont_16_b16_b_hiragana.py (bold)

character set: Cjk-compatibility-ideographs
-------------------------------------------
   10px :
           biwidth..............ezFBfont_10_b10_cjk-compatibility-ideographs.py
           biwidth............ezFBfont_10_b10_b_cjk-compatibility-ideographs.py (bold)
   12px :
           biwidth............ezFBfont_12_b12_b_cjk-compatibility-ideographs.py (bold)
           biwidth..............ezFBfont_12_b12_cjk-compatibility-ideographs.py
   14px :
           biwidth..............ezFBfont_14_b14_cjk-compatibility-ideographs.py
           biwidth............ezFBfont_14_b14_b_cjk-compatibility-ideographs.py (bold)
   16px :
           biwidth............ezFBfont_16_b16_b_cjk-compatibility-ideographs.py (bold)
           biwidth..............ezFBfont_16_b16_cjk-compatibility-ideographs.py

character set: Hangul-compatibility-jamo
----------------------------------------
    9px :
           biwidth...............ezFBfont_09_b10_b_hangul-compatibility-jamo.py (bold)
           biwidth.................ezFBfont_09_b10_hangul-compatibility-jamo.py
   11px :
           biwidth...............ezFBfont_11_b12_b_hangul-compatibility-jamo.py (bold)
           biwidth.................ezFBfont_11_b12_hangul-compatibility-jamo.py
   13px :
           biwidth...............ezFBfont_13_b14_b_hangul-compatibility-jamo.py (bold)
           biwidth.................ezFBfont_13_b14_hangul-compatibility-jamo.py
   14px :
           biwidth.................ezFBfont_14_b16_hangul-compatibility-jamo.py
           biwidth...............ezFBfont_14_b16_b_hangul-compatibility-jamo.py (bold)

character set: Small-form-variants
----------------------------------
    8px :
           biwidth.....................ezFBfont_08_b10_b_small-form-variants.py (bold)
           biwidth.......................ezFBfont_08_b10_small-form-variants.py
   10px :
           biwidth.......................ezFBfont_10_b12_small-form-variants.py
           biwidth.....................ezFBfont_10_b12_b_small-form-variants.py (bold)
   13px :
           biwidth.......................ezFBfont_13_b14_small-form-variants.py
           biwidth.....................ezFBfont_13_b14_b_small-form-variants.py (bold)
   15px :
           biwidth.......................ezFBfont_15_b16_small-form-variants.py
           biwidth.....................ezFBfont_15_b16_b_small-form-variants.py (bold)

character set: Cjk-unified-ideographs-extension-a
-------------------------------------------------
    9px :
           biwidth......ezFBfont_09_b10_b_cjk-unified-ideographs-extension-a.py (bold)
           biwidth........ezFBfont_09_b10_cjk-unified-ideographs-extension-a.py
   11px :
           biwidth........ezFBfont_11_b12_cjk-unified-ideographs-extension-a.py
           biwidth......ezFBfont_11_b12_b_cjk-unified-ideographs-extension-a.py (bold)
   14px :
           biwidth........ezFBfont_14_b14_cjk-unified-ideographs-extension-a.py
           biwidth......ezFBfont_14_b14_b_cjk-unified-ideographs-extension-a.py (bold)
   16px :
           biwidth......ezFBfont_16_b16_b_cjk-unified-ideographs-extension-a.py (bold)
           biwidth........ezFBfont_16_b16_cjk-unified-ideographs-extension-a.py
```

---------------------

## Converter script
The font structure is created by the 'convert.py' script in the `tooling` folder, see the README there for more.

The `sets.py` file in this folder contains the character definitions and source font filters.

# Block List Generator:
The following python script was used to generate the block dictionary in the `sets.py` file:
```
# Owen, 20240606:
# This script was adapted from one at https://stackoverflow.com/questions/243831/unicode-block-of-a-character-in-python
# Block list originally retrieved from http://unicode.org/Public/UNIDATA/Blocks.txt

_Blocks = '''
# Blocks-12.0.0.txt
# Date: 2018-07-30, 19:40:00 GMT [KW]
# © 2018 Unicode®, Inc.
# For terms of use, see http://www.unicode.org/terms_of_use.html
#
# Unicode Character Database
# For documentation, see http://www.unicode.org/reports/tr44/
#
# Format:
# Start Code..End Code; Block Name

# ================================================

# Note:   When comparing block names, casing, whitespace, hyphens,
#         and underbars are ignored.
#         For example, "Latin Extended-A" and "latin extended a" are equivalent.
#         For more information on the comparison of property values,
#            see UAX #44: http://www.unicode.org/reports/tr44/
#
#  All block ranges start with a value where (cp MOD 16) = 0,
#  and end with a value where (cp MOD 16) = 15. In other words,
#  the last hexadecimal digit of the start of range is ...0
#  and the last hexadecimal digit of the end of range is ...F.
#  This constraint on block ranges guarantees that allocations
#  are done in terms of whole columns, and that code chart display
#  never involves splitting columns in the charts.
#
#  All code points not explicitly listed for Block
#  have the value No_Block.

# Property: Block
#
# @missing: 0000..10FFFF; No_Block

0000..007F; Basic Latin
0080..00FF; Latin-1 Supplement
0100..017F; Latin Extended-A
0180..024F; Latin Extended-B
0250..02AF; IPA Extensions
02B0..02FF; Spacing Modifier Letters
0300..036F; Combining Diacritical Marks
0370..03FF; Greek and Coptic
0400..04FF; Cyrillic
0500..052F; Cyrillic Supplement
0530..058F; Armenian
0590..05FF; Hebrew
0600..06FF; Arabic
0700..074F; Syriac
0750..077F; Arabic Supplement
0780..07BF; Thaana
07C0..07FF; NKo
0800..083F; Samaritan
0840..085F; Mandaic
0860..086F; Syriac Supplement
08A0..08FF; Arabic Extended-A
0900..097F; Devanagari
0980..09FF; Bengali
0A00..0A7F; Gurmukhi
0A80..0AFF; Gujarati
0B00..0B7F; Oriya
0B80..0BFF; Tamil
0C00..0C7F; Telugu
0C80..0CFF; Kannada
0D00..0D7F; Malayalam
0D80..0DFF; Sinhala
0E00..0E7F; Thai
0E80..0EFF; Lao
0F00..0FFF; Tibetan
1000..109F; Myanmar
10A0..10FF; Georgian
1100..11FF; Hangul Jamo
1200..137F; Ethiopic
1380..139F; Ethiopic Supplement
13A0..13FF; Cherokee
1400..167F; Unified Canadian Aboriginal Syllabics
1680..169F; Ogham
16A0..16FF; Runic
1700..171F; Tagalog
1720..173F; Hanunoo
1740..175F; Buhid
1760..177F; Tagbanwa
1780..17FF; Khmer
1800..18AF; Mongolian
18B0..18FF; Unified Canadian Aboriginal Syllabics Extended
1900..194F; Limbu
1950..197F; Tai Le
1980..19DF; New Tai Lue
19E0..19FF; Khmer Symbols
1A00..1A1F; Buginese
1A20..1AAF; Tai Tham
1AB0..1AFF; Combining Diacritical Marks Extended
1B00..1B7F; Balinese
1B80..1BBF; Sundanese
1BC0..1BFF; Batak
1C00..1C4F; Lepcha
1C50..1C7F; Ol Chiki
1C80..1C8F; Cyrillic Extended-C
1C90..1CBF; Georgian Extended
1CC0..1CCF; Sundanese Supplement
1CD0..1CFF; Vedic Extensions
1D00..1D7F; Phonetic Extensions
1D80..1DBF; Phonetic Extensions Supplement
1DC0..1DFF; Combining Diacritical Marks Supplement
1E00..1EFF; Latin Extended Additional
1F00..1FFF; Greek Extended
2000..206F; General Punctuation
2070..209F; Superscripts and Subscripts
20A0..20CF; Currency Symbols
20D0..20FF; Combining Diacritical Marks for Symbols
2100..214F; Letterlike Symbols
2150..218F; Number Forms
2190..21FF; Arrows
2200..22FF; Mathematical Operators
2300..23FF; Miscellaneous Technical
2400..243F; Control Pictures
2440..245F; Optical Character Recognition
2460..24FF; Enclosed Alphanumerics
2500..257F; Box Drawing
2580..259F; Block Elements
25A0..25FF; Geometric Shapes
2600..26FF; Miscellaneous Symbols
2700..27BF; Dingbats
27C0..27EF; Miscellaneous Mathematical Symbols-A
27F0..27FF; Supplemental Arrows-A
2800..28FF; Braille Patterns
2900..297F; Supplemental Arrows-B
2980..29FF; Miscellaneous Mathematical Symbols-B
2A00..2AFF; Supplemental Mathematical Operators
2B00..2BFF; Miscellaneous Symbols and Arrows
2C00..2C5F; Glagolitic
2C60..2C7F; Latin Extended-C
2C80..2CFF; Coptic
2D00..2D2F; Georgian Supplement
2D30..2D7F; Tifinagh
2D80..2DDF; Ethiopic Extended
2DE0..2DFF; Cyrillic Extended-A
2E00..2E7F; Supplemental Punctuation
2E80..2EFF; CJK Radicals Supplement
2F00..2FDF; Kangxi Radicals
2FF0..2FFF; Ideographic Description Characters
3000..303F; CJK Symbols and Punctuation
3040..309F; Hiragana
30A0..30FF; Katakana
3100..312F; Bopomofo
3130..318F; Hangul Compatibility Jamo
3190..319F; Kanbun
31A0..31BF; Bopomofo Extended
31C0..31EF; CJK Strokes
31F0..31FF; Katakana Phonetic Extensions
3200..32FF; Enclosed CJK Letters and Months
3300..33FF; CJK Compatibility
3400..4DBF; CJK Unified Ideographs Extension A
4DC0..4DFF; Yijing Hexagram Symbols
4E00..9FFF; CJK Unified Ideographs
A000..A48F; Yi Syllables
A490..A4CF; Yi Radicals
A4D0..A4FF; Lisu
A500..A63F; Vai
A640..A69F; Cyrillic Extended-B
A6A0..A6FF; Bamum
A700..A71F; Modifier Tone Letters
A720..A7FF; Latin Extended-D
A800..A82F; Syloti Nagri
A830..A83F; Common Indic Number Forms
A840..A87F; Phags-pa
A880..A8DF; Saurashtra
A8E0..A8FF; Devanagari Extended
A900..A92F; Kayah Li
A930..A95F; Rejang
A960..A97F; Hangul Jamo Extended-A
A980..A9DF; Javanese
A9E0..A9FF; Myanmar Extended-B
AA00..AA5F; Cham
AA60..AA7F; Myanmar Extended-A
AA80..AADF; Tai Viet
AAE0..AAFF; Meetei Mayek Extensions
AB00..AB2F; Ethiopic Extended-A
AB30..AB6F; Latin Extended-E
AB70..ABBF; Cherokee Supplement
ABC0..ABFF; Meetei Mayek
AC00..D7AF; Hangul Syllables
D7B0..D7FF; Hangul Jamo Extended-B
D800..DB7F; High Surrogates
DB80..DBFF; High Private Use Surrogates
DC00..DFFF; Low Surrogates
E000..F8FF; Private Use Area
F900..FAFF; CJK Compatibility Ideographs
FB00..FB4F; Alphabetic Presentation Forms
FB50..FDFF; Arabic Presentation Forms-A
FE00..FE0F; Variation Selectors
FE10..FE1F; Vertical Forms
FE20..FE2F; Combining Half Marks
FE30..FE4F; CJK Compatibility Forms
FE50..FE6F; Small Form Variants
FE70..FEFF; Arabic Presentation Forms-B
FF00..FFEF; Halfwidth and Fullwidth Forms
FFF0..FFFF; Specials
10000..1007F; Linear B Syllabary
10080..100FF; Linear B Ideograms
10100..1013F; Aegean Numbers
10140..1018F; Ancient Greek Numbers
10190..101CF; Ancient Symbols
101D0..101FF; Phaistos Disc
10280..1029F; Lycian
102A0..102DF; Carian
102E0..102FF; Coptic Epact Numbers
10300..1032F; Old Italic
10330..1034F; Gothic
10350..1037F; Old Permic
10380..1039F; Ugaritic
103A0..103DF; Old Persian
10400..1044F; Deseret
10450..1047F; Shavian
10480..104AF; Osmanya
104B0..104FF; Osage
10500..1052F; Elbasan
10530..1056F; Caucasian Albanian
10600..1077F; Linear A
10800..1083F; Cypriot Syllabary
10840..1085F; Imperial Aramaic
10860..1087F; Palmyrene
10880..108AF; Nabataean
108E0..108FF; Hatran
10900..1091F; Phoenician
10920..1093F; Lydian
10980..1099F; Meroitic Hieroglyphs
109A0..109FF; Meroitic Cursive
10A00..10A5F; Kharoshthi
10A60..10A7F; Old South Arabian
10A80..10A9F; Old North Arabian
10AC0..10AFF; Manichaean
10B00..10B3F; Avestan
10B40..10B5F; Inscriptional Parthian
10B60..10B7F; Inscriptional Pahlavi
10B80..10BAF; Psalter Pahlavi
10C00..10C4F; Old Turkic
10C80..10CFF; Old Hungarian
10D00..10D3F; Hanifi Rohingya
10E60..10E7F; Rumi Numeral Symbols
10F00..10F2F; Old Sogdian
10F30..10F6F; Sogdian
10FE0..10FFF; Elymaic
11000..1107F; Brahmi
11080..110CF; Kaithi
110D0..110FF; Sora Sompeng
11100..1114F; Chakma
11150..1117F; Mahajani
11180..111DF; Sharada
111E0..111FF; Sinhala Archaic Numbers
11200..1124F; Khojki
11280..112AF; Multani
112B0..112FF; Khudawadi
11300..1137F; Grantha
11400..1147F; Newa
11480..114DF; Tirhuta
11580..115FF; Siddham
11600..1165F; Modi
11660..1167F; Mongolian Supplement
11680..116CF; Takri
11700..1173F; Ahom
11800..1184F; Dogra
118A0..118FF; Warang Citi
119A0..119FF; Nandinagari
11A00..11A4F; Zanabazar Square
11A50..11AAF; Soyombo
11AC0..11AFF; Pau Cin Hau
11C00..11C6F; Bhaiksuki
11C70..11CBF; Marchen
11D00..11D5F; Masaram Gondi
11D60..11DAF; Gunjala Gondi
11EE0..11EFF; Makasar
11FC0..11FFF; Tamil Supplement
12000..123FF; Cuneiform
12400..1247F; Cuneiform Numbers and Punctuation
12480..1254F; Early Dynastic Cuneiform
13000..1342F; Egyptian Hieroglyphs
13430..1343F; Egyptian Hieroglyph Format Controls
14400..1467F; Anatolian Hieroglyphs
16800..16A3F; Bamum Supplement
16A40..16A6F; Mro
16AD0..16AFF; Bassa Vah
16B00..16B8F; Pahawh Hmong
16E40..16E9F; Medefaidrin
16F00..16F9F; Miao
16FE0..16FFF; Ideographic Symbols and Punctuation
17000..187FF; Tangut
18800..18AFF; Tangut Components
1B000..1B0FF; Kana Supplement
1B100..1B12F; Kana Extended-A
1B130..1B16F; Small Kana Extension
1B170..1B2FF; Nushu
1BC00..1BC9F; Duployan
1BCA0..1BCAF; Shorthand Format Controls
1D000..1D0FF; Byzantine Musical Symbols
1D100..1D1FF; Musical Symbols
1D200..1D24F; Ancient Greek Musical Notation
1D2E0..1D2FF; Mayan Numerals
1D300..1D35F; Tai Xuan Jing Symbols
1D360..1D37F; Counting Rod Numerals
1D400..1D7FF; Mathematical Alphanumeric Symbols
1D800..1DAAF; Sutton SignWriting
1E000..1E02F; Glagolitic Supplement
1E100..1E14F; Nyiakeng Puachue Hmong
1E2C0..1E2FF; Wancho
1E800..1E8DF; Mende Kikakui
1E900..1E95F; Adlam
1EC70..1ECBF; Indic Siyaq Numbers
1ED00..1ED4F; Ottoman Siyaq Numbers
1EE00..1EEFF; Arabic Mathematical Alphabetic Symbols
1F000..1F02F; Mahjong Tiles
1F030..1F09F; Domino Tiles
1F0A0..1F0FF; Playing Cards
1F100..1F1FF; Enclosed Alphanumeric Supplement
1F200..1F2FF; Enclosed Ideographic Supplement
1F300..1F5FF; Miscellaneous Symbols and Pictographs
1F600..1F64F; Emoticons
1F650..1F67F; Ornamental Dingbats
1F680..1F6FF; Transport and Map Symbols
1F700..1F77F; Alchemical Symbols
1F780..1F7FF; Geometric Shapes Extended
1F800..1F8FF; Supplemental Arrows-C
1F900..1F9FF; Supplemental Symbols and Pictographs
1FA00..1FA6F; Chess Symbols
1FA70..1FAFF; Symbols and Pictographs Extended-A
20000..2A6DF; CJK Unified Ideographs Extension B
2A700..2B73F; CJK Unified Ideographs Extension C
2B740..2B81F; CJK Unified Ideographs Extension D
2B820..2CEAF; CJK Unified Ideographs Extension E
2CEB0..2EBEF; CJK Unified Ideographs Extension F
2F800..2FA1F; CJK Compatibility Ideographs Supplement
E0000..E007F; Tags
E0100..E01EF; Variation Selectors Supplement
F0000..FFFFF; Supplementary Private Use Area-A
100000..10FFFF; Supplementary Private Use Area-B

# EOF
'''
# Generate dict{} entries for character sets based on Unicode blocks.
import re
pattern = re.compile(r'([0-9A-F]+)\.\.([0-9A-F]+);\ (\S.*\S)')
for line in _Blocks.splitlines():
    m = pattern.match(line)
    if m:
        start, end, n = m.groups()
        name = n.lower().replace(' ','-')
        print("        '{}' : list(range(0x{}, 0x{})),".format(name, start, end))
```
