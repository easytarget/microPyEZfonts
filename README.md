# Fonts for the MicroPython framebuffer

A collection of fonts sourced from the [u8g2](https://github.com/olikraus/u8g2) project and converted to use with Peter Hinches [writer](https://github.com/peterhinch/micropython-font-to-py/tree/master/writer) class using the tools provided in [his Repo](https://github.com/peterhinch/micropython-font-to-py)

## WORK IN PROGRESS; But we do have an initial font set
Font files are now in the [mpy-fonts](mpy_fonts) folder.

They are organised by vertical size! and (where possible) come in up to 5 different charset formats:
```
f = !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
r =  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
U =  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
n =  *+,-./0123456789:
e = Every character that font-to-mpy can convert, can be large
```
These can loosely be described as **f**ull (all chars up to 255), **r**eadable (ascii charset), **u**ppercase (just the minimum, good for symbol fonts), **n**umbers (plus a few time related symbols) and **e**verything.
* Characters will only be present when they are defined in the font source
  * missing characters are skipped.
  * Empty font files are not uploaded.

 !! There is a known issue with class naming (some font names have a '-' hyphen in them, this will be fixed soon.

See the `Writer` class (link above) to use these; I will provide better use documentation later. For now look at the `writer-demo.py` script to see how these fonts can be used.

### Converter script Requirements
* This repo
* Git Submodules updated
* `freetype-py` installed:
  * pip install --upgrade freetype-py

The `convert.py` script will create and populate the `mpy-fonts` folder with all matching and successful fonts; organised by height.
