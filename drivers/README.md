# Driver archive
The monochrome drivers in this folder have been tested and where necesscary modified for use with `ezFBfont`, they are provided for convenience.

# Useful sources of framebuffer drivers for micropython:
* https://github.com/bdbarnett/mpdisplay
* https://github.com/peterhinch/micropython-nano-gui/tree/master/drivers

# ST7789 TFT Color displays
* I have a repo with [my own ST7789 display driver](https://github.com/easytarget/st7789-framebuffer) for high-memory (ESP32 and RP2040 class) devices, This has been well  tested and works with the Writer and Marquee.
  * This has been tested and works on various devices, including the Lillygo T-Watch 2020 and T-Display Touch.
* This also has a summary of the current drivers available for this display type, and links to faster and more advanced drivers, some of which require custom firmwares.

## Mono Drivers provided here:
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

## Using other drivers
*ezFBfont* will work with any 3rd party driver that is compatible with the inbuilt microPython framebuffer.
* Color and Greyscale displays are supported, you will need to set the foreground (and possibly background) colors at init or when writing.

# Bonus
* `repl_1306.py`
  * A drop in replacement for *ssd1306.py* (but *does not* take the SPI/I2C options!)
  * Displays an ascii representation of the framebuffer to the repl console, useful when debugging on a desktop machine and for checking positions/alignments
  * A couple of [examples](/examples) for this are provided.
