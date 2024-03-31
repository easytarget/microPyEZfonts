# Driver archive
Drivers here have been tested and where necesscary modified for use with `ezFBfont`, they are provided for convenience.

## Using other drivers
*ezFBfont* should work with any 3rd party driver that is compatible with the inbuilt microPython framebuffer.
* For color or greyscale displays you need to supply the optional `color` argument at init.
  * Or modify the driver to return a `.format` property with the framebuffer format as defined [here](https://docs.micropython.org/en/latest/library/framebuf.html#constants).

## List
(current as of 31/mar/2024)
* `ssd1306.py`
  * for I2C and SPI connected displays based on the ssd1306 chip (and compatibles)
  * based on the default micropython driver from (todo!) modified to return the format as a property
