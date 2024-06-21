from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
from ezFBfont import ezFBfont
from sys import path
from time import ticks_ms

# fonts
path.append('fonts')
import ezFBfont_17_helvB12_ascii as header
import ezFBfont_37_7_Seg_41x21_base as digits
import ezFBfont_29_7_Seg_33x19_base as decimals
import ezFBfont_16_open_iconic_human_2x_lower as icons

'''
A demo of using ezMPfont to do a simple uptime counter.
The 'baseline' vertical alignment, along with 'left'
and 'right' horizontal alignment, is used to align the
different fonts used in the time display.
'''

# pins
I2C0_SDA_PIN = 21  # default esp32
I2C0_SCL_PIN = 22  # default esp32
#I2C0_SDA_PIN = 28  # default rp2040
#I2C0_SCL_PIN = 29  # default rp2040

# I2C
# Wiring is important, you need good connections and pullup resisitors on the lines.
#  If you see continual 'OSError: with 'ENODEV' or 'ETIMEDOUT' you can try the SoftI2C
#  function instead, it is more tolerant of timing errors.
#  You can also play with frequency and timeout values, default:
#  freq=400000, timeout= 50000
#i2c0=SoftI2C(sda=Pin(I2C0_SDA_PIN), scl=Pin(I2C0_SCL_PIN),  freq=200000, timeout=100000)
i2c0=I2C(0,sda=Pin(I2C0_SDA_PIN), scl=Pin(I2C0_SCL_PIN))

# Display
display = SSD1306_I2C(128, 64, i2c0, addr=0x3c)
display.invert(False)  # as needed
display.rotate(0)      # as needed
display.contrast(128)  # as needed

# Font Init
heading = ezFBfont(display, header)
lcdm = ezFBfont(display, digits, halign='right', valign='baseline')
lcds = ezFBfont(display, decimals, valign='baseline')
icon = ezFBfont(display, icons, halign='center', valign='center')

# frame
def clean():
    display.fill(0)
    heading.write('UpTime:', 0, 0)
    display.show()

d = True
# loop
clean()
while True:
    upsecs = int(ticks_ms() / 1000)
    secs = upsecs % 60
    mins = int(upsecs / 60) % 60
    hrs = int(upsecs / 3600) % 24
    lcdm.write('{:d}:{:02d}'.format(hrs, mins), 84, 56)
    lcds.write(':{:02d}'.format(secs), 84, 56)
    beat = int(ticks_ms() / 333) % 2
    icon.write(chr(66), 118, 7, fg=beat)
    display.show()
# fin