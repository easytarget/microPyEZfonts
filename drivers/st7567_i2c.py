#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Imported and modified for use with ezFBfont by o.carter, Apr 2024
# Original from @mcGeorge on micropython forum:
#   https://forum.micropython.org/viewtopic.php?t=12747
# - modified to support the `.format` property


from micropython import const
from time import sleep_ms
import framebuf

# LCD Commands definition
CMD_DISPLAY_ON          = const(0xAF)
CMD_DISPLAY_OFF         = const(0xAE)
CMD_SET_START_LINE      = const(0x40)
CMD_SET_PAGE            = const(0xB0)
CMD_COLUMN_UPPER        = const(0x10)
CMD_COLUMN_LOWER        = const(0x00)
CMD_SET_ADC_NORMAL      = const(0xA0)
CMD_SET_ADC_REVERSE     = const(0xA1)
CMD_SET_COL_NORMAL      = const(0xC0)
CMD_SET_COL_REVERSE     = const(0xC8)
CMD_SET_DISPLAY_NORMAL  = const(0xA6)
CMD_SET_DISPLAY_REVERSE = const(0xA7)
CMD_SET_ALLPX_ON        = const(0xA5)
CMD_SET_ALLPX_NORMAL    = const(0xA4)
CMD_SET_BIAS_9          = const(0xA2)
CMD_SET_BIAS_7          = const(0xA3)
CMD_DISPLAY_RESET       = const(0xE2)
CMD_NOP                 = const(0xE3)
CMD_TEST                = const(0xF0)  # Exit this mode with CMD_NOP
CMD_SET_POWER           = const(0x28)
CMD_SET_RESISTOR_RATIO  = const(0x20)
CMD_SET_VOLUME          = const(0x81)

# Display parameters
DISPLAY_W               = const(128)
DISPLAY_H               = const(64)
DISPLAY_CONTRAST        = const(0x1B)
DISPLAY_RESISTOR_RATIO  = const(5)
DISPLAY_POWER_MODE      = 7


class ST7567(framebuf.FrameBuffer):

    def __init__(self, width, height, i2c, addr=0x3F, external_vcc=False):
        self.i2c          = i2c
        self.addr         = addr
        self.temp         = bytearray(2)
        self.write_list   = [b"\x40", None]  # Co=0, D/C#=1
        self.width        = width
        self.height       = height
        self.external_vcc = external_vcc
        self.pages        = self.height // 8
        self.buffer       = bytearray(self.pages * self.width)
        self.format       = framebuf.MONO_VLSB
        super().__init__( self.buffer, self.width, self.height, self.format)
        self.display_init()

    def display_init(self):
        self.write_cmd( CMD_DISPLAY_RESET )
        sleep_ms(1)
        for cmd in (
            CMD_DISPLAY_OFF,                                  # Display off
            CMD_SET_BIAS_9,                                   # Display drive voltage 1/9 bias
            CMD_SET_ADC_NORMAL,                               # Normal SEG
            CMD_SET_COL_REVERSE,                              # Commmon mode reverse direction
            CMD_SET_RESISTOR_RATIO + DISPLAY_RESISTOR_RATIO,  # V5 R ratio
            CMD_SET_VOLUME,                                   # Contrast
            DISPLAY_CONTRAST,                                 # Contrast value
            CMD_SET_POWER + DISPLAY_POWER_MODE):
            self.write_cmd(cmd)

        self.show()
        self.write_cmd(CMD_DISPLAY_ON)

    def set_contrast(self, value):
        if (0x1 <= value <= 0x3f):
            for cmd in ( CMD_SET_VOLUME, value ):
                self.write_cmd(cmd)

    def show(self):
        for i in range(8):
            for cmd in (
                CMD_SET_START_LINE,
                CMD_SET_PAGE + i,
                CMD_COLUMN_UPPER,
                    CMD_COLUMN_LOWER):
                self.write_cmd(cmd)
            self.write_data( self.buffer[i*128:(i+1)*128] )

    def write_cmd(self, cmd):
        self.temp[0] = 0x80  # Co=1, D/C#=0
        self.temp[1] = cmd
        self.i2c.writeto( self.addr, self.temp )

    def write_data(self, buf):
        self.write_list[1] = buf
        self.i2c.writevto( self.addr, self.write_list )
