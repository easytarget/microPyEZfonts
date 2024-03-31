# Fonts for the MicroPython framebuffer

A collection of fonts sourced from the [u8g2](https://github.com/olikraus/u8g2) project

Thes fonts have been processed using the tools provided in Peter Hinches [`font-to-py`](https://github.com/peterhinch/micropython-font-to-py) repo, and can be used with either his (comprehensive) [writer](https://github.com/peterhinch/micropython-font-to-py/tree/master/writer) class, or the easy font writer class in this repo.

These can be used with any display that has a driver for the built-in microPyton [framebuffer](https://docs.micropython.org/en/latest/library/framebuf.html), I intend to build a driver database here for all screens tested and known to work

## This is a WORK IN PROGRESS!

See the `examples` folder for the alpha release..

..the `dev` branch is where the latest stuff will be (unstable? unusable? ymmv!)

## Provided Fonts

Font files are in the [mpy-fonts](mpy_fonts) folder. See the `README` there for a 'map'

This is a *restricted* set of the `U8G2` fonts, many of the fonts available there are in an older version of `.bdf` font file format that is not supported by the converter tool. Others have unclear or burdonsome licence restrictions.

The selection provided here covers the devault U8G2 fonts, a lot of common X11 fonts and the 'spleen' small font set. There are some symbol and icon fonts but I wish the selction was better, sorry.

They are organised by vertical size! and (where possible) come in up to 5 different charset formats:
* Characters will only be present when they are defined in the font source! not all fonts have all characters.
  * missing characters are skipped.
  * Empty font files are not uploaded.

```
f = !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
r =  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
U =  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
n =  *+,-./0123456789:
e = Every character that font-to-mpy can convert, can be large
```
These can loosely be described as **f**ull (all chars up to 255), **r**eadable (ascii charset), **u**ppercase (just the minimum, good for symbol fonts), **n**umbers (plus a few time related symbols) and **e**verything.

See the `Writer` class (link above) to use these; I will provide better use documentation later. For now look at the `writer-demo.py` script to see how these fonts can be used.

### Converter script Requirements
* This repo
* Git Submodules updated
* `freetype-py` installed:
  * pip install --upgrade freetype-py

The `convert.py` script will create and populate the `mpy-fonts` folder with all matching and successful fonts; organised by height.

-----------------------------------------------------------------------------------------------------------------------------

# ezFBfont.py

Design notes; not canon. But this is an attempt to document the alpha release.

Class initiated against a font..

```python
from ezFBfont import ezFBfont
import mPyEZFont_XYZ

... create a font object attached to a framebuffer device
myfont = ezFBfont(device, mPyEZFont_XYZ)

... use it to write on the framebuffer
myfont.write(string, x, y)

... eventually..
device.show()
```

## Create an instance for the font:

The font class and the font(s) required need to be imported:

```python
from ezFBfont import ezFBfont
import mPyEZFont_myfont
...
```

And then used to create a font writer instance for all the imported fonts:

```python
myfont = ezFBfont(device, fontName, fg=None, bg=None ,tkey=None, halign=None, valign=None, colors=None)
```
Positional Arguments:
* *device* : The framebuffer device to write to
* *fontName* : the name of the font you imported above, eg: mPyEZFont_myfont

Optional Arguments:
* *fg*, *bg*, *tkey*: (integers) foreground and background colors, plus transparency key
  * foreground and background will default to *max-color* and *min-color* respectively (see below)
  * transparent key is -1 by default (none), otherwise the transparent color
* *halign*: (string) 'left|right|center' : how to align on the X axis
  * Defaults to `left`
  * This also works as justification, and is applied on a per-line basis
* *valign*: (string) 'top|center|baseline|bottom' : how to align on Y axis
  * Defaults to `top`
  * The `baseline` setting is applied for the first line of multi-line strings

Device dependent: May need to be supplied if your display device driver does not report it's settings properly.
* *colors*: (integer) the total number of colors or greyscales we support, 2 for mono, up to 65536 for 16 bit color
  * The *max-color* used above will always be `total colors - 1`, *min-color* is always 0
  * This defaults to `2` (mono displays) if not supplied and not determined automatically

## Use:
#### write()
```python
myfont.write(str, X, Y, fg=None, bg=None, tkey=None, halign=None, valign=None)
```
Positional Arguments:
* *string* : The string to be written to the framebuffer
* *x*, *y* : position (pixels), framebuffer top-left is 0, 0

Optional Arguments:
* as per init options, override the default.

#### size()
```python
x, y = myfont.size(str)
```
Returns the pixel width and height of the string

#### rect()
```python
xmin, xmax, width, height = myfont.rect(str, x, y, halign=None, valign=None)
```
Returns the area that the string would be written to with `myfont.write()`
* The return is suitable for passing directly to `display.rect()`

#### set_default()
```python
myfont.set_default(fg=None, bg=None, tkey=None, halign=None, valign=None)
```
Changes the default value of the supplied argument(s)

### Thoughts:

Instead of rotation; provide an orient tuple of bool's : `(Mirror, Flip, Turn)`, this will allow all text directions and effects etc. Better than just 0,90,180,270 rotation options provide.

Class can provide height, width and other props for the font

### Wanted:
a python library to rotate `MONO_VLSB` and `MONO_HMSB` framebuffers by 90 degrees
