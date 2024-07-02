# `bdf2dict.py`
## a `.bdf` font file to python font file utility

## Setup
This is a **CPython 3.7+** tool (not micropython..)

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
  * If the keyword `FULL` is used the entire font will be converted (can get big..)
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

A simple unicode 'text' file with each character from the output in it. This can be discarded; but is useful for reference, copy/paste, etc..

## Font module format
In contrast to the `micropython-font-to-py` tool I use a simpler format based on a python `dict{}` structure.

Font glyphs are stored as [`bytes`](https://docs.python.org/3.5/library/functions.html#bytes) objectt in the dict, with the integer ordinal value of the character as the key.

If the font is variable-width the width of the character is appended to the bytearray.

The `get_ch()` function then becomes very simple; look up the glyph and return 'None' if not found. Otherwise return a memoryview object pointing the the *bytes* of the glyph and return that along with the (fixed) font height and width of the glyph (or a fixed value for fixed width fonts)

## Note: *easy* fonts

These fonts are most suitable for devices with relatively large amounts of ram and flash storage. All my work has been done on **ESP32** and **RP2040** boards, 

The fonts, and the writer, target 'Ease of Use' (*) as a core ethos.
* They are aimed at casual developers and educators.
* You can get good looking results quickly and without excess complexity and learning curves.
* My 'target' developer is someone working with Thonny or Viper IDE and simply drag-dropping the font files and classes onto the device.
* They cover 'small device data display' scenarios very well.

'Smaller' devices such as the **ESP8266** can use them but their more limited ram may make using 'full' font packs difficult. The *Number* and *Time* packs may, however, be quite useful since they are generally very small, even for big fonts.

These fonts have similar memory and ram consumption to the fonts from `micropython-font-to-py` when copied to the target device in an IDE and run on a default firmware for the device.

However; if you are developing a memory critical application where you are freezing files as bytecode the 'micropython-font-to-py' generated fonts are able to keep their data in the Flash memory. the 'ezFBfonts' use a dictionary which, being mutable, is copied to ram even when the font file itself is frozen.

If this wasteful use of memory when frozen is an issue then these fonts are not for you1 Although the font writer and marquee classes  (being compatible with both font creation systems) may be.

(*) *For a given value of 'Ease of Use'*

### `.bdf` files
These are in the relevent folders for Latin-1, Symbols and Unicode. See the README files in there for Copyright considerations.

You can, of course, supply your own font source; the *bdf-to-dict* script should work with any viable *.bdf* file. Check the output in the *.map* file to verify you are getting what you expect.
