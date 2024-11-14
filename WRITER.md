# `ezFBfont.py`
## Font Writer for MicroPython Framebuffer

A font system designed for easy installation and use, particularly for small "info panel" type projects.

This will work with *any* display that has a driver compatible with the built-in MicroPython [framebuffer](https://docs.micropython.org/en/latest/library/framebuf.html).

## Installation:
Copy the `ezFBfont.py` file from this repository into the main directory (or specified path) of your MicroPython project. You’ll also need to include the display driver and any font files you want to use. No additional dependencies are required.

## Quick Start
*ezFBfont* is a Python class you initialize with a framebuffer device and a font. Then, you can use the *write()* method to write text to the framebuffer.

Check the [`examples`](examples) folder for sample code that demonstrates the features explained below.
```python
from ezFBfont import ezFBfont
import mPyEZFont_XYZ

# Create a font object linked to a framebuffer device
myfont = ezFBfont(device, mPyEZFont_XYZ)

# Use it to write text on the framebuffer
myfont.write('string', x, y)

# Finally, display the results
device.show()
```

## Detailed Guide
### Creating a Font Instance:

Import both the font class and any font(s) you need:
```python
from ezFBfont import ezFBfont
import mPyEZFont_myfont as fontName
#...repeat for all fonts
```

Then create a font instance for each imported font:
```python
myfont = ezFBfont(device, fontName,
                  fg=1, bg=0, tkey=-1,
                  halign='left', valign='top',
                  hgap=0, vgap=0,
                  split='\n',
                  cswap=False,
                  verbose=False)
```

**Required Arguments:**
* *device*: The framebuffer device to write on.
* *fontName*: The name of the imported font module.

**Optional Arguments:**
* *fg*, *bg*, *tkey* (integers): foreground and background colors, plus transparency key.
  * Foreground defaults to 1 (mono); adjust as needed for color displays.
  * Background defaults to 0.
  * Transparency key is `-1` by default (none), otherwise set to the font color to make transparent; only supports `-1`, `0`, or `1` for mono fonts.
* *halign* (string): `left|right|center`, sets horizontal alignment.
  * Default is `left`.
  * Aligns text line by line, effectively justifying each line.
* *valign* (string): `top|center|baseline|bottom`, sets vertical alignment.
  * Default is `top`.
  * If using multi-line text, `baseline` aligns at the first line.
* *hgap* & *vgap* (integers): controls space between characters and lines.
  * Defaults to `0`. Negative values are allowed. This gap is not padding, so background won’t be drawn in these spaces.
  * For negative values, consider using a transparent background (`tkey=0`) to prevent character backgrounds from "clipping" each other.
* *split* (character/string): the character to split multi-line text, defaults to '\n' (newline).
* *cswap* (bool): Swaps bytes in a 16-bit color word.
  * Default is `False`; set to `True` for RGB displays with reversed byte order (e.g., st7789).
* *verbose* (bool): Enables detailed feedback on initialization, default changes, and missing characters, default `False`.

### Methods:
*(Note: Don’t forget to call `device.show()` after writing text to make it visible on the display.)*

#### `write()`
```python
myfont.write(string, X, Y, fg=None, bg=None, tkey=None, halign=None, valign=None)
```
Writes the given text to the framebuffer.

**Positional Arguments:**
* *string*: The text to write on the framebuffer.
* *x*, *y*: Position in pixels; top-left of framebuffer is 0, 0.

**Optional Arguments:**
* Overrides for the initialization settings.

Returns `False` if any characters fail to display (missing in the font).

#### `size()`
```python
x, y = myfont.size(str)
```
Returns the width and height (in pixels) of the text string.

#### `rect()`
```python
xmin, xmax, width, height = myfont.rect(str, x, y, halign=None, valign=None)
```
Returns the exact area that the text will cover when using `myfont.write()`.
* This output can be directly used with `display.rect()`.
* Alignment options will override current defaults.

#### `set_default()`
```python
myfont.set_default(fg=None, bg=None, tkey=None, halign=None, valign=None, hgap=None, vgap=None, split=None, verbose=None)
```
Changes the default values for the specified argument(s).

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
myfont.split  : default split character/string
```

### Future Ideas:
* `Flip`, `Mirror`, `Turn`: to add various text orientations and effects.
