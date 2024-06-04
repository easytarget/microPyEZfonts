# bdf font to pyton dictFont utility
WIP..

## Setup
install bsdparser (see below):

## Converter script

The `convert.py` script will create and populate the supplied folder with all matching and successful fonts; organised by family, then height

### requirements
* This repo
* bdfparser

### `.bdf` files
The files in the `bdf-sources` folder have been modified; all whiespace lines have been removed since this can cause bdfparser errors; some fonts (notably symbol ones!) needed the main 'font box' size adjusting since they contained glyphs that are larger than this box and were being clipped.

## Indexer script
No requirements, when run in the font folder it will index the font packs and provide the above summary

---------------------
```console
# create venv if needed
~/microPyEZfonts/mpy-fonts $ python -m venv env

# activate it
~/microPyEZfonts/mpy-fonts $ source env/bin/activate

# upgrade pip (optional)
(env) ~/microPyEZfonts/mpy-fonts $ pip install --upgrade pip
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Requirement already satisfied: pip in ./env/lib/python3.11/site-packages (23.0.1)
Collecting pip
  Using cached https://www.piwheels.org/simple/pip/pip-24.0-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.0.1
    Uninstalling pip-23.0.1:
      Successfully uninstalled pip-23.0.1
Successfully installed pip-24.0owen@sam:~/MPython-fonts/microPyEZfonts/dictFont$ python -m venv env

# install bdfparser from the local folder
pip install --upgrade bdfparser
```
