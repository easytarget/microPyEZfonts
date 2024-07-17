# Driver archive
Drivers here have been tested and where necesscary modified for use with `ezFBfont`, they are provided for convenience.

# Useful sources of framebuffer drivers for micropython:
* https://github.com/bdbarnett/mpdisplay
* https://github.com/peterhinch/micropython-nano-gui/tree/master/drivers

## Using other drivers
*ezFBfont* will work with any 3rd party driver that is compatible with the inbuilt microPython framebuffer.
* Color and Greyscale displays are supported, you will need to set the foreground (and possibly background) colors at init or when writing.

## Drivers provided here:
(current as of 16/Jul/2024), these are the 'tested' drivers for reference.
* `ssd1306.py`
  * for I2C and SPI connected displays based on the ssd1306 chip (and compatibles)
  * based on the default micropython driver from [@stlehmann](https://github.com/stlehmann/micropython-ssd1306) modified to support a rotate() method
* `st7567_i2c.py`
  * for I2C connected displays based on the ST7567 chip (and compatibles)
  * A copy of the driver from [@mcGeorge](https://forum.micropython.org/viewtopic.php?t=12747)
* `sh1106.py`
  * for I2C connected displays based on the SH1106 chip (and compatibles)
  * A copy of the driver from [@robert-hh](https://github.com/robert-hh/SH1106)

# Bonus
* `repl_1306.py`
  * A drop in replacement for *ssd1306.py* (but *does not* take the SPI/I2C options!)
  * Displays an ascii representation of the framebuffer to the repl console, useful when debugging on a desktop machine and for checking positions/alignments
  * A couple of [examples](/examples) for this are provided.
