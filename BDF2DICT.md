# bdf font to pyton dict utility

## `bdf2dict.py`
```python
python bdf2dict.py <font_file> <prefix> [charset]
```

#### Arguments:
* `<font_file>` : (path): a `.bdf` file, with the font you want to convert
* `<prefix>` : (string): A prefix that will be added to the output files.
  If the prefix begins with a path this will be used as the output folder, eg '../proj/myfont_`
* `[charset]`: optional:
  * If not supplied the user will be prompted to enter the desired characters.
  * If a valid file path is supplied this will be read and all unique chars in it added to the charset.
  * If the keyword `FULL` is used the entire font will be converted (can get big..)
  * A `-` tells the script to read it's charset from `stdin`, it will be de-duplicated as necessary
* `debug`: optional: append the key word *debug* to the arguments to switch on a (potentially very lengthy) debug output
#### Output
Three files are created:
* `<prefix><font_name>.py`
* `<prefix><font_name>.map`
* `<prefix><font_name>.set`

** TODO; explain these **

## Font module format
** todo **

## Setup
You need Python 3.7+, but otherwise there are no further requirements, the tooling is self-contained.

## Converter script

The `make-sets.py` script will create and populate the current folder with all matching and successful fonts; organised by family, then height. It reads details from the file 'set.py' 

### `.bdf` files
These are in the relevent folders for Latin-1, Symbols and Unicode. See the README files in there for Copyright considerations.

You can, of course, supply your own font source; the *bdf-to-dict* script should work with any viable *.bdf*, check the output in the *.map* file to verify you are getting what you expect!

## Glyph Dumper
`glyphdump.py` is a utility that is run against a `font.py` file itself, it loads and renders all glyphs defined in the font module. 

This is the ultimate 'debug my font' tool, see the comments in it for usage. It can also render fonts made by font-to-py

## Indexer scripts
These are located in the *Latin-1* and *Symbols* folders themselves. When run in their folder they will index the font packs and provide the that I copy into the README.md files there.
