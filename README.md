# Fonts for the MicroPython framebuffer

A collection of fonts sourced from the [u8g2](https://github.com/olikraus/u8g2) project and converted to use with Peter Hinches [writer](https://github.com/peterhinch/micropython-font-to-py/tree/master/writer) class using the tools provided in [his Repo](https://github.com/peterhinch/micropython-font-to-py)

## WORK IN PROGRESS; NO FONTS YET
I need to work out licencing and copyright notice xfer into the `font.py` files; until then I im only presenting the conversion tool here.

### Requirements
* This repo
* Git Submodules updated
* `freetype-py` installed:
  * pip install --upgrade freetype-py

The `convert.py` script will create and populate the `mpy-fonts` folder with all matching and successful fonts; organised by height.
