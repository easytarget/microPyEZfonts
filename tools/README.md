# Tools I used to build and test the font packs.

These are incidental scripts mostly for my own use, but kept here as part of the repo. See the comments in them for usage etc.

## Setup
You need Python 3.7+, but otherwise there are no further requirements, the tooling is self-contained.

# Bulk Converter script

The `make-sets.py` script will create and populate the current folder with all matching and successful fonts; organised by family, then height. It reads details from the file 'set.py' 

# Glyph Dumper

`glyphdump.py` is a utility that is run against a `font.py` file itself, it loads and renders all glyphs defined in the font module as ASC-II art.

This is the ultimate 'debug my font' tool, see the comments in it for usage. It can also render fonts made by `font-to-py`

# Indexer scripts
These are located in the *Latin-1* and *Symbols* folders themselves. When run in their folder they will index the font packs and provide the font size/family/name map that I copy into the README.md files themselves.
