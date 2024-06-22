# Fonts and Font Writer for the MicroPython framebuffer

A collection of fonts and a writer for them, sourced from the [u8g2](https://github.com/olikraus/u8g2) project and packaged for use on small devices, with small displays, running [MicroPython](https://micropython.org/).

![Demo Examples on two different displays](examples/doc/demo-collage1.thumb.jpg)

They will work with **`EZ FrameBuffer Font Writer`** (see [below](#easy-font-use-via-ezfbfontpy)).
* This is optimised for ease of installation and use; especially for small 'info panel' type projects and will work with *any* display that has a driver for the built-in microPyton [framebuffer](https://docs.micropython.org/en/latest/library/framebuf.html).

And will also work with Peter Hinches comprehensive [writer](https://github.com/peterhinch/micropython-font-to-py/tree/master/writer) class and [nano-gui](https://github.com/peterhinch/micropython-nano-gui/tree/master).

The fonts presented here were created using my own `bdf2dict` font module creator. Details in the [`bdf2dict`](bdf2dict) folder.


## Status
The fonts and libraries have been tested on a `ssd1306` OLED display, and a `st7567` LCD module, both using I2C.



The above is showing demo programs from the [examples](examples); with various fonts, alignments and colors.

-----------------
# Fonts
Font files are in the [`Latin-1`](Latin-1) and [`Symbols`](Symbols) folders as appropriate.
* See the `README` in each for a description, a map of all the fonts and heights, and other considerations.

The selection provided here covers the default U8G2 fonts, a lot of common X11 fonts and the 'spleen' small font set. There are some symbol and icon fonts too.

They are all derived from **112** open and redistributable *.bdf* font definition files covering 11 font families. These have been packed into *.py* font modules based on the character set(s) they contain.

Fonts are generated and stored by font family, then character set and vertical size.
* 560 **Latin-1** font modules cover the basic latin character sets in groups of related characters.
* 144 **Symbol** modules cover specialist symbol fonts (battery, 7 segment, etc) and the Open Iconic icon sets.
* **Unicode** font modules need to made on demand using the `bdf2dict` tool, see the Unicode [README](/Unicode/README.md) for details.
  * There is no sensible way of grouping Unicode fonts into packs that are small enought to be useful on micropython devices. The most popular blocks have thousands of characters in them and the resulting files are too large to use sensibly.
  * The `bdf2dict` tool is designed to be easy to install and use, just requiring Python3.7 or higher.
  * You can specify your own charset when prompted on the command line (or via a file/arguments/stdin).
  * The script will output a python font module containing only the characters requested, plus an ascii-art map of the glyphs.
  * The [efont](http://openlab.ring.gr.jp/efont/dist/unicode-bdf/) unicode fonts are provided in the Unicode folder, but other fonts in the Latin-1 folder also provide unicode characters; these are noted in the README.

All provided font modules contain and retain the original copyright notices from the source '.bdf' files, most are very 'free'; but the proportional X11 derived fonts need extra consideration. See the documentation on the font index pages for more.

## Drivers
The font writer should work with any display that has a MicroPython framebuffer compatible driver.

Some 'good' drivers are provided, along with some documentation on finding and using other drivers, in the [`drivers`](drivers) folder. If you find a driver that works and is not in my list please let me know by submitting a issue.

## Alternatives
If you are implementing a full 'GUI', or have a color display, especially a large(ish) one, then you should consider the alternatives below. They support large displays, full color displays, have GUI elements, and are faster.

The fonts in this repo will work with Peter Hinches `writer` and `nano-gui` classes:
* https://github.com/peterhinch/micropython-font-to-py/blob/master/writer/WRITER.md
  * This is a good class to use if you are driving a console type display since it has goodies like word-wrap, tab alignment, etc.
* https://github.com/peterhinch/micropython-nano-gui/tree/master
  * A good alternative to the complexity of LVGL (below), and my fonts work with it.

From the same author are the display drivers here:
* https://github.com/peterhinch/micropython-nano-gui/blob/master/DRIVERS.md
* These support several large color displays and can also use the fonts from this repo.

Another great resource, especially for display drivers, is at:
* https://github.com/bdbarnett/mpdisplay

And finally; for people building fast GUI's on color displays and who are willing to deal with more complex installs; there is [LVGL](https://lvgl.io/):
* https://docs.lvgl.io/7.11/get-started/micropython.html

-----------------
# Easy font use via `ezFBfont.py`
*easyFBfont* is a python class that is initiated against a framebuffer device, and a font.

### install:
Copy the `ezFBfont.py` file from this repository into the root (or path) of your MicroPython project, along with the relevant display driver and font files you want to use.

### quickstart
See the [`examples`](examples) folder for some working code that uses all the features described below.
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

## Create an instance for the font:

The font class and the font(s) required need to be imported:
```python
from ezFBfont import ezFBfont
import mPyEZFont_myfont as font1
#...etc for all fonts
```

You then create a font instance for each imported font:
```python
myfont = ezFBfont(device, font1,
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
* *hgap* and *vgap*: add (or remove) spacing between characters and lines
  * Defaults to `0`, and is only applied between individual characters and between lines, negative values are allowed.
  * This is a gap, not padding; no background is drawn in the space created.
* *colors*: (integer) the total number of colors or greyscales we support, 2 for mono, up to 65536 for 16 bit color.
  * This defaults to `2` (mono displays) if not supplied and not determined automatically.
    * If the display driver reports a 'format' property this is used to determine the color map.
  * The default foreground color will be `colors - 1`, default background is always `0`.
* *verbose*: Enables verbose feedback on init, default changes and missing characters, default `False`.

## Methods:
(After writing your data do not forget to do a `device.show()` or equivalent to see the results :wink:)

#### write()
```python
myfont.write(string, X, Y, fg=None, bg=None, tkey=None, halign=None, valign=None, hgap=None, vgap=None)
```
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

#### rect()
```python
xmin, xmax, width, height = myfont.rect(str, x, y, halign=None, valign=None, hgap=None, vgap=None)
```
Returns the exact area that the string would be written to with `myfont.write()`.
* The return is suitable for passing directly to `display.rect()`.

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
See the issue list for status/planning.
* `Flip`, `Mirror`, `Turn`: these will allow all text directions and effects etc.
