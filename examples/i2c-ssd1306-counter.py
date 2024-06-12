from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
from ezFBfont import ezFBfont
from sys import path, stdin
from time import sleep_ms,ticks_ms
import select

# fonts
path.append('fonts')
import ezFBfont_17_helvR12_ascii
import ezFBfont_37_7_Seg_41x21_base
import ezFBfont_29_7_Seg_33x19_base
import ezFBfont_16_open_iconic_human_2x_lower

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
d0 = SSD1306_I2C(128, 64, i2c0, addr=0x3c)
d0.invert(False)  # as needed
d0.rotate(0)      # as needed
d0.contrast(128)  # as needed

# Font Init
heading = ezFBfont(d0, ezFBfont_17_helvR12_ascii)
lcdm = ezFBfont(d0, ezFBfont_37_7_Seg_41x21_base, halign='right', valign='baseline')
lcds = ezFBfont(d0, ezFBfont_29_7_Seg_33x19_base, valign='baseline')
icon = ezFBfont(d0, ezFBfont_16_open_iconic_human_2x_lower, halign='center', valign='center')

# frame
def clean():
    d0.fill(0)
    heading.write('UpTime:', 0, 0)
    d0.show()

d = True
# loop
clean()
while True:
    upsecs = int(ticks_ms() / 1000)
    secs = upsecs % 60
    mins = int(upsecs / 60) % 60
    hrs = int(upsecs / 3600) % 24
    lcdm.write('{:d}:{:02d}'.format(hrs, mins), 84, 57)
    lcds.write(':{:02d}'.format(secs), 84, 57)
    beat = int(ticks_ms() / 333) % 2
    icon.write(chr(66), 118, 7, fg=beat)
    d0.show()
# fin

