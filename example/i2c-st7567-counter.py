from machine import Pin,I2C
from st7567_i2c import ST7567
from ezFBfont import ezFBfont
from sys import path
from time import sleep_ms,ticks_ms

# fonts
path.append('fonts')
import mPyEZfont_u8g2_spleen_12x24_r
import mPyEZfont_u8g2_spleen_16x32_n
import mPyEZfont_u8g2_helvR14_r

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
i2c0=I2C(0,sda=Pin(I2C0_SDA_PIN), scl=Pin(I2C0_SCL_PIN))

# Display
# Display
d0 = ST7567(128, 64, i2c0, addr=0x3f)
d0.set_contrast(31)  # as needed (max 63)

# Font Init
heading = ezFBfont(d0, mPyEZfont_u8g2_helvR14_r)
minutes = ezFBfont(d0, mPyEZfont_u8g2_spleen_16x32_n, halign='right', valign='baseline')
seconds = ezFBfont(d0, mPyEZfont_u8g2_spleen_12x24_r, valign='baseline')

# frame
d0.rect(0, 24, 127, 38, 1)
heading.write('UpTime:', 0, 2)
d0.show()

x = 86
y = 53
# loop
while True:
    upsecs = int(ticks_ms() / 1000)
    secs = upsecs % 60
    mins = int(upsecs / 60) % 60
    hrs = int(upsecs / 3600) % 24
    minutes.write('%d:%02.d' % (hrs, mins), x, y)
    seconds.write('.%02.d' % secs, x, y)
    d0.show()
# fin