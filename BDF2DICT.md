# `bdf2dict.py`
## a `.bdf` font file to python font file conversion utility

## Setup
This is a **CPython 3.7+** tool intended to be run from the commandline on a desk/laptop system, it can use a *quite a bit* of memory when fed a huge font file and charset, but is also fast and robust.

Otherwise there are no further requirements, the tooling is self-contained, simply copy `bdf2dict.py` where needed or run from in the repo.

```python
python bdf2dict.py <font_file> <prefix> [<charset>] [debug]
```

### Arguments:
* `<font_file>` : (path): a `.bdf` file, with the font you want to convert
* `<prefix>` : (string): A prefix that will be added to the output files.
  If the prefix begins with a path this will be used as the output folder, eg '../proj/myfont_`
* `[<charset>]`: optional:
  * If not supplied the user will be prompted to enter the desired characters.
  * If a valid file path is supplied this will be read as ascii / unicode text and all unique chars in it added to the charset.
  * If an empty string is passed (`''`) the entire font will be converted (can get big..)
  * A `-` tells the script to read it's charset from `stdin`.
  * The charset is always de-duplcated and sorted before processing.
* `[debug]`: optional: append the key word *debug* to the arguments to switch on a (potentially very lengthy) comprehensive debug output

### Output
Three files are created:
* `<prefix><font_name>.py`

  This is the font file itself, it needs to be copied to the target device/folder.

* `<prefix><font_name>.map`

  A text file with a font data summary and an ascii-art rendition of every glyph provided in the output.

* `<prefix><font_name>.set`

  A simple unicode 'text' file with all characters from the output font file in it. 

The map and set files can typically be discarded; but can also be useful for reference, copy/paste, etc..

------------------------------------
# Font module format
In contrast to the binary format of the `micropython-font-to-py` tool I use a simpler format based on a python `dict{}` structure.

Font glyphs are stored as [`bytes`](https://docs.python.org/3.5/library/functions.html#bytes) objects declared in a dictionary with the integer ordinal value of the character as the dict key.

If the font is variable-width a byte with the width of the character is appended to the byte object.

The `get_ch()` function then becomes very simple; it looks up the glyph and returns 'None' if not found. Otherwise it returns a memoryview object pointing the the *bytes* of the glyph along with the (fixed) font height, and width of the glyph.

## Note: *easy* fonts

***The fonts, and the writer, target 'Ease of Use' (\*) as a core ethos.***
* They are aimed at casual developers and educators.
* They cover 'small device data display' scenarios very well.
* You can get good looking results quickly and without excess complexity and learning curves.
* My 'target' developer is someone working with Thonny or Viper IDE and simply drag-dropping the font files and classes onto the device.

These fonts are most suitable for devices with relatively large amounts of ram and flash storage. All my development work was done on **ESP32** and **RP2040** boards, but I have also tested on a **ESP8266**.

'Smaller' devices such as the **ESP8266** can use them but their more limited ram may make using 'full' font packs difficult. The *Number* and *Time* packs may, however, be quite useful since they are generally very small, even for huge font faces such as the LCD packs.

***As an approximate rule of thumb the size of the `.py` file on disk is similar to the amount of RAM used on import.***
* But only AFTER dicarding the copyright block in the *.py* file (which can be up to 2K in size for the adobe fonts).

### Test Results; real-world data ###
Please see the [Memory Test](examples/memory-test/import_test.md) document I wrote, this has the results from an imformal test suite I wrote to compare the two font mechanisms.

The dictionary fonts typically use 20-50% more ram in comparison to the fonts from `micropython-font-to-py` when copied to the target device filesystem and imported from there.

In terms of speed both mechanisms are *very* fast, simply looking up then returning a memory pointer. Attempts to measure this failed, with any difference in speed undetectable amidst the noise, and reponse times always in the sub-ms range.

#### Mimimizing ram use by freezing as bytecode in a custom firmware
If you are developing a memory critical application and freezing files as bytecode the 'micropython-font-to-py' generated fonts are able to keep *all* their data in the Flash memory, and only ever use 400 bytes of memory, no matter how large the font is.

The ezFBfonts cannot do this for *all* their data, and still consume some ram for a character index (a dictionary full of memory pointers) even though the glyph data itself remains frozen in the firmware.
- The width/height size of the font has no effect on RAM use, only the number of characters in the set matters.
- In practice this means that *time* and *number* packs only use ~500 bytes of RAM, while a *full* pack uses ~1.9K.
  - For comparison; the same packs loaded from the filesystem use between ~1.8K and 16K of ram.

(*) *For a given value of 'Ease of Use'*

### `.bdf` files
These are in the relevent folders for Latin-1, Symbols and Unicode. See the README files in there for Copyright considerations.

You can, of course, supply your own font source; the *bdf-to-dict* script should work with any viable *.bdf* file. Check the output in the *.map* file to verify you are getting what you expect.
