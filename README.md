# Fonts and Font Writer for the MicroPython framebuffer

A collection of fonts and a writer for them, inspired by the [u8g2](https://github.com/olikraus/u8g2) project and packaged for use on devices with small displays running [MicroPython](https://micropython.org/).

[![Demo Examples on two different displays](examples/doc/demo-collage1.thumb.jpg)](examples/doc/demo-collage1.jpg)

The font packs here will work with my **`Font Writer`** and **`Marquee`** classes (see below).
* The writer and marquee are optimised for ease of installation and use; especially for small 'info panel' type projects and will work with *any* display that has a driver for the built-in microPyton [framebuffer](https://docs.micropython.org/en/latest/library/framebuf.html).

***Additionally*** these font packs also work with Peter Hinche's comprehensive [writer](https://github.com/peterhinch/micropython-font-to-py/blob/master/writer/WRITER.md) class and [nano-gui](https://github.com/peterhinch/micropython-nano-gui/tree/master) **and** the `EZFont` class from Brad Barnett's [mpdisplay](https://github.com/bdbarnett/mpdisplay)

The font packs presented here were created using my own `bdf2dict` font module creator, see below.

-----------------
# Latin-1 and Symbol Font Packs

Font files are in the [`Latin-1`](Latin-1) and [`Symbols`](Symbols) folders as appropriate.
* See the `README` in each for a description, a map of all the fonts and heights, and other considerations.

The selection provided here was derived from the default U8G2 fonts; it contains common X11 fonts, the 'spleen' small font set, OpenIconic icons, tiny fonts, and some symbol and other icon fonts too.

They are all derived from **112** open and redistributable *.bdf* font definition files covering 11 font families. These have been packed into *.py* font modules based on the character set(s) they contain.

Fonts are generated and stored by font family, then character set and vertical size.
* 561 **Latin-1** font modules cover the basic latin character sets in groups of related characters.
* 144 **Symbol** modules cover specialist symbol fonts (battery, 7 segment, etc) and the Open Iconic icon sets.

All provided font modules contain and retain the original copyright notices from the source '.bdf' files, most are very 'free'; but the proportional X11 derived fonts need extra consideration. See the documentation on the font index pages for more.

# Unicode font packs?

There is no sensible way of grouping general Unicode fonts into packs that are small enought to be useful on micropython devices. The common blocks have thousands of characters in them and the resulting files are too large to use sensibly.

Instead; tooling and examples are provided to help you make a custom font pack with the glyphs and characters you need, and no excess.
* The `bdf2dict` tool (below) is designed to be easy to install and use, just requiring Python3.7 or higher
  * The [Unicode](Unicode/README.md) page has an example of it's use
  * The [unifont](https://savannah.gnu.org/projects/unifont) and [efont](http://openlab.ring.gr.jp/efont/) unicode font *.bdf* sources are provided in the Unicode folder.
 
-------------------------

# Font Writer: [`ezFBfont.py`](ezFBfont.py)
The writer class `exFBfont.py` works with these fonts, it takes a string to write, plus X and Y position, and writes the string in that position in the selected font. There are color, transparency, spacing and positioning options, plus functions to give info about the written area and support for multi-line strings.

For more see the documentation in [`WRITER.md`](WRITER.md), there are examples of using this in the [examples](examples) folder.

# Marquee: [`ezFBmarquee.py`](ezFBmarquee.py)

A simple marquee / scrolling banner display that uses the fonts from this repo. You can define an output 'box' and the string will be scrolled within that. Supports a couple of 'modes' for the scroll, adjustable character spacing and step rate.

Details are in [`MARQUEE.md`](MARQUEE.md), and examples of driving the animation with an IRQ timer loop are in the examples folder.

# Font module creator: [`bdf2dict.py`](bdf2dict.py)

All the font module packs provided here were made with this tool, it is a simple to use CPython *(not microPython!)* script that can import and process a `.bdf` font file and extract just the characters you need into a `.py` font module file. It is fully compatible with Unicode characters and fonts.

See [`BDF2DICT.md`](BDF2DICT.md) for further documentation and usage instructions, and the Unicode [readme](Unicode/README.md) for some Unicode fonts and a documented example of using this tool to generate a custom font pack.

# Display Drivers

The font writer and marquee will work with **any** display that has a MicroPython **framebuffer** compatible driver.

A couple of common 'good' drivers for popular ssd1306 and st7567 displays are provided. Along with documentation on finding and using drivers for other displays in the [`drivers`](drivers) folder.

If you find a driver that works and is not in the list there please let me know by submitting a issue!

# Alternatives

If you are implementing a full 'GUI', or have a color display, especially a large(ish) one, then you should consider the alternatives below. They support large displays, full color displays, have GUI elements, are fast and use less memory..

The fonts in this repo will work with Peter Hinches `writer` and `nano-gui` classes:
* https://github.com/peterhinch/micropython-font-to-py/blob/master/writer/WRITER.md
  * This is a good class to use if you are driving a console type display since it has goodies like word-wrap, tab alignment, etc.
* https://github.com/peterhinch/micropython-nano-gui/tree/master
  * A good alternative to the complexity of LVGL (below), and my fonts work with it.
* Peter also has a `micropython-font-to-py` tool that makes fonts that will work with my writer and marquee classes!
  * Fonts from this tool are better for advanced users since they use far less RAM when byte-compiled and frozen in firmware, see the bdf2dict readme for a discussion of this.

From the same author are the display drivers here:
* https://github.com/peterhinch/micropython-nano-gui/blob/master/DRIVERS.md
* These support several large color displays and can also use the fonts from this repo.

Another great resource for display drivers and GUI elements is Brad Barnetts `mpdisplay` at:
* https://github.com/bdbarnett/mpdisplay
* The EZFont class in his tooling (just one of several font classes it provides!) is compatible with my ezFBfont packs.

And finally; for people building fast GUI's on color displays and who are willing to deal with more complex installs; there is [LVGL](https://lvgl.io/):
* https://docs.lvgl.io/7.11/get-started/micropython.html

-----------------

# Status

I created ezFBfont, the font packs and tooling to support a [project](https://github.com/easytarget/PrintPy2040) that I am currently working on, and several others I have planned.

[![PrintPy, still under development..](examples/doc/printpy.thumb.jpg)](examples/doc/printpy.jpg)

This is a 3d printer status and progress display, driven by a Seeedstudio XIAO RP2040, and using my fonts + writer + marquee.
* It also uses another specialised MicroPython tool I wrote, [serialOM](https://github.com/easytarget/serialOM); a framework and class for fetching and synchronising the RepRapFirmware [ObjectModel](https://docs.duet3d.com/en/User_manual/RepRapFirmware/Object_Model) via any serial stream. This is notable partly because it is a cross-python class; it works under both MicroPython and CPython

The fonts, writer and marquee have been tested using I2C on a `ssd1306` OLED display, and a `st7567` LCD module. Using both by ESP32 and RP2040 development boards.
