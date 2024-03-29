from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
from ezFBfont import ezFBfont
from sys import path
from time import sleep_ms,ticks_ms

# fonts
path.append('fonts')
import mPyEZfont_u8g2_spleen_12x24_r
import mPyEZfont_u8g2_spleen_16x32_n
import mPyEZfont_u8g2_helvR14_r

'''
WIP
'''

# pins
I2C0_SDA_PIN = 21  # default esp32
I2C0_SCL_PIN = 22  # default esp32
#I2C0_SDA_PIN = 28  # default rp2040
#I2C0_SCL_PIN = 29  # default rp2040

# I2C
i2c0=I2C(0,sda=Pin(I2C0_SDA_PIN), scl=Pin(I2C0_SCL_PIN))

# Display
d0 = SSD1306_I2C(128, 64, i2c0, addr=0x3c)
d0.invert(False)  # as needed
d0.rotate(0)      # as needed
d0.contrast(128)  # as needed

# Font Init
heading = ezFBfont(d0, mPyEZfont_u8g2_helvR14_r)
seconds = ezFBfont(d0, mPyEZfont_u8g2_spleen_12x24_r)
boxtime = ezFBfont(d0, mPyEZfont_u8g2_spleen_16x32_n)

# frame
d0.rect(0, 24, 127, 38, 1)
heading.write('UpTime:', 7, 1)
d0.show()

# loop
while True:
    upsecs = int(ticks_ms() / 1000)
    secs = upsecs % 60
    mins = int(upsecs / 60) % 60
    hrs = int(upsecs / 3600)
    boxtime.write('%d:%02.d' % (hrs, mins), 17, 27)
    seconds.write('.%02.d' % secs, 82, 34)
    d0.show()