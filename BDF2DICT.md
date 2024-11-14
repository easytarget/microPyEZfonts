# `bdf2dict.py`
## A tool to convert `.bdf` font files into Python font files

## Setup
This tool is for **CPython 3.7+** and runs from the command line on a desktop or laptop. It may use a lot of memory if you load a large font file, but it works quickly and reliably.

There are no additional requirements. Just copy `bdf2dict.py` to where you need it, or run it directly from the repository.

```bash
python bdf2dict.py <font_file> <prefix> [<charset>] [debug]
```

### Arguments:
* `<font_file>` : (path) The `.bdf` font file you want to convert.
* `<prefix>` : (string) A prefix for the output files. If it includes a path (e.g., `../proj/myfont_`), that will be used as the output folder.
* `[<charset>]` : Optional.
  * If not provided, you’ll be asked to enter the characters you want.
  * If a valid file path is given, the script will read the characters from it.
  * If you give an empty string (`''`), the entire font will be converted (this could be large).
  * If you use a `-`, the charset will be read from `stdin`.
  * The charset is always cleaned (duplicates removed) and sorted before processing.
* `[debug]` : Optional. Add the word *debug* to see detailed debug information.

### Output
The script creates three files:
* `<prefix><font_name>.py` : This is the Python font file. It should be copied to the device/folder.
* `<prefix><font_name>.map` : A summary file with a text representation of the font and its characters.
* `<prefix><font_name>.set` : A text file containing all characters from the font.

You can usually discard the `.map` and `.set` files, but they can be useful for reference.

---

# Font module format
Unlike the binary format used by the `micropython-font-to-py` tool, this uses a simple Python `dict{}` format.

Font glyphs are stored as `bytes` objects in a dictionary, with the character’s integer value as the key.

For variable-width fonts, the width of the character is added as a byte at the end.

The `get_ch()` function looks up the character, returning a memoryview of the glyph’s bytes, or `None` if the character is not found.

## Note: *easy* fonts

***These fonts and the tool focus on ease of use.***
* They are designed for casual developers and educators.
* They work well for small device data displays.
* The goal is to get good results quickly, with minimal complexity.
* Ideal for people using Thonny or Viper IDE, who can drag and drop font files onto the device.

These fonts are best for devices with more RAM and flash storage, like **ESP32** and **RP2040** boards. They can also work on **ESP8266**, but the limited RAM on smaller devices may make it hard to use large font packs. However, smaller font packs like the *Number* and *Time* packs work well even on these devices.

*Note: The size of the `.py` file on disk is roughly the same as the amount of RAM used when it’s imported, but this can vary depending on the font.*

### Test Results: Real-World Data
See the [Memory Test](examples/memory-test/import_test.md) for a comparison between this and the `micropython-font-to-py` method.

Fonts in the dictionary format use about 20-50% more RAM compared to fonts from the other tool, but both are very fast. Response times are always below 1ms, and no speed difference is noticeable.

#### Minimizing RAM Use with Bytecode in Custom Firmware
If you need to save memory, freezing files as bytecode can help. The fonts generated with the `micropython-font-to-py` tool store all their data in Flash memory, using only 400 bytes of RAM regardless of font size.

The fonts from this tool do not store all data in Flash. They use some RAM for indexing the characters (a dictionary of memory pointers), but the glyph data is kept in Flash.

For example:
- *Time* and *Number* font packs use around 500 bytes of RAM.
- A *full* font pack uses about 1.9K of RAM.
- When loaded from the filesystem, these packs may use between 1.8K and 16K of RAM.

---

### `.bdf` Files
The `.bdf` files for Latin-1, Symbols, and Unicode are in the relevant folders. See the README files there for copyright details.

You can also use your own font source. The *bdf-to-dict* script should work with any valid `.bdf` file. You can check the `.map` file to ensure the output looks as expected.
