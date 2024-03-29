# Fonts for the MicroPython framebuffer

A collection of fonts sourced from the [u8g2](https://github.com/olikraus/u8g2) project

Converted to use with Peter Hinches [writer](https://github.com/peterhinch/micropython-font-to-py/tree/master/writer) class using the tools provided in [his Repo](https://github.com/peterhinch/micropython-font-to-py)

These can be used with the built-in microPyton framebuffer: https://docs.micropython.org/en/latest/library/framebuf.html and any display device that can be attached to that (eg OLED's)

The goal, eventually, is to provide a simpler 'string writer' class to enble very casual use of these fonts in microPython

## This is very much a WORK IN PROGRESS; but it does have an initial font set

Fot the moment the only way to use these is via Peter Hinches Writer class, see the links above.

I am writing a much simpler tool since the scope and complexity of that class is a barrier to casual font use.

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

# ezFBstr.py

Design notes; not canon. But this is an attempt to document the alpha release.

Class initiated against a font..

```python
from ezFBstr.py import ezFBstr
import mPyEZFont_XYZ

... create a font object attahed to a framebuffer device
myfont = ezFBstr(device,'mPyEZFont_XYZ')

... use it to write on the framebuffer
myfont.write(string,x,y)

... eventually..
device.show()
```

## Create an instance for the font:

The font needs to be imported:

```python
import mPyEZFont_myfont
```

And is then used to create a font writer instance:

```python
myfont = ezFBstr(device, fontName, fg=max_allowed, bg=0 ,tkey=-1, halign='left', valign='top', colors=?, size=(?,?))
```
Positional Arguments:
* device : The framebuffer device to write to
* fontName : the name of the font you imported above, eg: mPyEZFont_myfont
Optional Arguments:
* foreground and background colors, plus transparentcy key
  * foreground and background will default to max-color and min-color respectively
  * max and min colors are derived from the Framebuffer type
  * transparent key is -1 by default (none), otherwise the transparent color
* halign: 'left|right|center' : how to align on the X axis
* valign: 'top|center|baseline|bottom' : how to align on Y axis
Device dependent arguments:
* colors: integer, the total number of colors we support, 2 for mono, up to 65536 for 16 bit color
  * the max-color used above will always be this value -1, min-color is always 0
* size: display dimensions as a tuple (x,y)

## Use it:

```python
myfont.write(str, X, Y, fg=None, bg=None, tkey=None, halign=None, valign=None)
```
Positional Arguments:
* string : The string to be written to the framebuffer
* x, y : position (pixels), framebuffer top-left is 0, 0

Optional Arguments:
* as per init options, override the default.

Returns False if anything was clipped

```python
TODO: x,y = myfont.size(str)
```
Returns the pixel width and height of the string

```python
TODO: xmin,xmax,ymin,ymax = myfont.area(str, x, y, halign=None, valign=None)
```
Returns the area to be written to, options as above

```python
myfont.set_color(fg=None, bg=None, tkey=None)
```
Sets the default foreground, background and transparency colors as needed

```python
myfont.area(str, x, y, halign=None, valign=None)
```
Sets the default horizontal and vertical alignment as needed

### Thoughts:

Instead of rotation; provide an orient tuple of bool's : `(Mirror, Flip, Turn)`, this will allow all text directions and effects etc. Better than just 0,90,180,270 rotation options provide.

Class can provide height, width and other props for the font

### Wanted:
a python library to rotate `MONO_VLSB` framebuffers..
