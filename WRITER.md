# `ezFBfont.py`
## a Font Writer for the MicroPython framebuffer

A font system optimised for ease of installation and use; especially for small 'info panel' type projects.

This will work with *any* display that has a driver for the built-in microPyton [framebuffer](https://docs.micropython.org/en/latest/library/framebuf.html).

## install:
Copy the `ezFBfont.py` file from this repository into the root (or path) of your MicroPython project, along with the relevant display driver and font files you want to use. There are no other requirements.

## quickstart
*ezFBfont* is a python class that is initiated against a framebuffer device, and a font. You then write strings to the framebuffer using the *write()* method.

See the [`examples`](examples) folder for some working code that uses the features described below.
```python
from ezFBfont import ezFBfont
import mPyEZFont_XYZ

... create a font object attached to a framebuffer device
myfont = ezFBfont(device, mPyEZFont_XYZ)

... use it to write on the framebuffer
myfont.write('string', x, y)

... eventually..
device.show()
```

## In detail
### Create an instance for the font:

The font class and the font(s) required need to be imported:
```python
from ezFBfont import ezFBfont
import mPyEZFont_myfont as fontName
#...etc for all fonts
```

You then create a font instance for each imported font:
```python
myfont = ezFBfont(device, fontName,
                  fg=1, bg=0 ,tkey=-1,
                  halign='left', valign='top', hgap=0, vgap=0,
                  colors=2, verbose=False)
```
Required Arguments:
* *device* : The framebuffer device to write to.
* *fontName* : the name of the imported font module.

Optional Arguments:
* *fg*, *bg*, *tkey*: (integers) foreground and background colors, plus transparency key.
  * foreground will default to the value of *colors* -1; for mono displays this will be `1`
  * transparent key is `-1` by default (none), otherwise the font color that should be rendered transparent; currently we only support mono fonts so is limited to `-1`, `0` or `1`.
* *halign*: (string) `left|right|center` : how to align on the X axis.
  * Defaults to `left`.
  * This also works as justification, and is applied on a per-line basis.
* *valign*: (string) `top|center|baseline|bottom` : how to align on Y axis.
  * Defaults to `top`.
  * The `baseline` setting is applied at the first line with multi-line strings.
* *hgap* and *vgap*: (integer) add or remove spacing between characters and lines
  * Defaults to `0`, and is only applied between individual characters and between lines, negative values are allowed.
  * This is a gap, not padding; no background is drawn in the space created.
  * Negative values are allowed, if using them you should also use a transparent background (`tkey=0`) to stop character backgrounds 'clipping' the previous characters as they are drawn.
* *colors*: (integer) the total number of colors or greyscales we support, 2 for mono, up to 65536 for 16 bit color.
  * This defaults to `2` (mono displays) if not supplied and not determined automatically.
    * If the display driver reports a 'format' property this is used to determine the color map.
  * The default foreground color will be `colors - 1`, default background is always `0`.
* *verbose*: Enables verbose feedback on init, default changes and missing characters, default `False`.

### Methods:
(After writing your data do not forget to do a `device.show()` or equivalent to see the results :wink:)

#### write()
```python
myfont.write(string, X, Y, fg=None, bg=None, tkey=None, halign=None, valign=None, hgap=None, vgap=None)
```
Writes the supplied text to the framebuffer

Positional Arguments:
* *string* : The text to be written to the framebuffer
* *x*, *y* : position (pixels), framebuffer top-left is 0, 0

Optional Arguments:
* as per init options, values supplied will override the default.

Returns `False` if any characters failed to be written (not present in the font).

#### size()
```python
x, y = myfont.size(str, hgap=None, vgap=None)
```
Returns the pixel width and height of the string.
* The gap options will override the current default.

#### rect()
```python
xmin, xmax, width, height = myfont.rect(str, x, y, halign=None, valign=None, hgap=None, vgap=None)
```
Returns the exact area that the string would be written to with `myfont.write()`.
* The return is suitable for passing directly to `display.rect()`.
* The alignment and gap options will override the current default.

#### set_default()
```python
myfont.set_default(fg=None, bg=None, tkey=None, halign=None, valign=None, hgap=None, vgap=None, verbose=None)
```
Changes the default value of the supplied argument(s).

### Properties
```
myfont.name   : font name
myfont.fg     : default foreground color
myfont.bg     : default background color
myfont.tkey   : default transparency key
myfont.halign : default horizontal alignment
myfont.valign : default vertical alignment
myfont.hgap   : default horizontal gap
myfont.vgap   : default vertical gap
myfont.colors : total number of available colors
```

### Thoughts:
* `Flip`, `Mirror`, `Turn`: these will allow all text directions and effects etc.
