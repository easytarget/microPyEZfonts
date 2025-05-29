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

# TTF / OTF import tools

Are in the folder [otf2bdf](otf2bdf), there are two scripts:
* `make-bdfs.sh` : generates a range of bdf files with set point sizes, edit the list inside the script to produce other sizes..
* `insert-licence.sh` : Inserts a supplied file as COMMENT lines starting on line 2 of all bdf files in the current directory.

These scripts are intended for manual use on the command line, you need to install `otf2bdf` to use the converter (it is available via `dnf install otf2bdf`, `apt install odf2bdf` etc.)
* Warning: the otf2bdf tool messes up on spaces. You need to edit the resulting .bdf file and look at the first character defined, which is usually the space character (0x20, 32 decimal),
  * Set the `BBX` line to read `BBX 0 1 0 0`
  * Insert a line between `BITMAP` and `ENDCHAR` containing just `00`.
  * This is needed otherwise the space character will get omitted from the generated python files. Sorry about this.
