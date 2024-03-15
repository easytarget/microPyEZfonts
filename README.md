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
```
f = !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
r =  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
U =  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
n =  *+,-./0123456789:
e = Every character that font-to-mpy can convert, can be large
```
These can loosely be described as **f**ull (all chars up to 255), **r**eadable (ascii charset), **u**ppercase (just the minimum, good for symbol fonts), **n**umbers (plus a few time related symbols) and **e**verything.
* Characters will only be present when they are defined in the font source! not all fonts have all characters.
  * missing characters are skipped.
  * Empty font files are not uploaded.

See the `Writer` class (link above) to use these; I will provide better use documentation later. For now look at the `writer-demo.py` script to see how these fonts can be used.

### Converter script Requirements
* This repo
* Git Submodules updated
* `freetype-py` installed:
  * pip install --upgrade freetype-py

The `convert.py` script will create and populate the `mpy-fonts` folder with all matching and successful fonts; organised by height.

-----------------------------------------------------------------------------------------------------------------------------
# ezFBstr.py
Design notes; not canon. When I have code I can publish this will get updated, ignore till then.

Class initiated against a font..
```python
from ezFBstr.py import ezFBstr
import mPyEZFont_XYY
... create a framebuffer device
ZYXfont = ezFBstr(device,'mPyEZFont_XYY')
... code runs, eventually it wants to output something
XYZfont.write(string,position,[Kargs])
device.show()
```


```python
XYZfont.write(str,(X,Y), invert=False, solid=False, XOR=False)
```
Positional Arguments:
* string : natch..
* (X,Y) : position, pixels, top-left is (0,0)
  
optional:
* clip : What to do if string will go off screen:
  * True;  Clip rendered text where it exceeds screen bounds
  * False; return an exception and do not render
* invert : False : inverse FG & BG
* solid : True: render background, otherwise only render foreground.
* XOR : False : Humm... would be good to have this; can the blit do it?
* ? baseLine? : False : use font baseline for Y=0
* ? alignRight ? : False : Align X=0 to string end (Padding?? remove or keep?)

Returns False if anything was clipped.

```python
XYZfont.wide(str, solid=False, invert=False)
```
Returns the pixel width (excluding trailing padding unless 'solid' or 'inverse') of the string

### Thoughts:

Vertical text can wait, I've got enough to do already.

Can provide height, width and other props.

### Wanted:
* A nice way to selct the invert/solid/Xor prefs. Feels clumsy as it.
