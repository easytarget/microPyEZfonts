from time import sleep_ms,ticks_ms,ticks_diff
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
from sys import path

# fonts
from writer import Writer
path.append('fonts')
import mPyEZfont_u8g2_spleen_12x24_n
import mPyEZfont_u8g2_spleen_16x32_n
import mPyEZfont_u8g2_6x12_r
import mPyEZfont_u8g2_helvR14_r

'''
WIP
'''

# I2C
I2C0_SDA_PIN = 21  # ESP32
I2C0_SCL_PIN = 22
#I2C0_SDA_PIN = 28 # rp2040
#I2C0_SCL_PIN = 29
i2c0=I2C(0,sda=Pin(I2C0_SDA_PIN), scl=Pin(I2C0_SCL_PIN))

# Display
d0 = SSD1306_I2C(128, 64, i2c0, addr=0x3c)
d0.invert(False)
d0.rotate(0)
d0.contrast(255)  # my screen is very bright

# Writer Init
wTop = Writer(d0, mPyEZfont_u8g2_helvR14_r)
wMins = Writer(d0, mPyEZfont_u8g2_spleen_12x24_n)
wSecs = Writer(d0, mPyEZfont_u8g2_spleen_16x32_n)
wSecsDec = Writer(d0, mPyEZfont_u8g2_6x12_r)

# Screen Init
d0.rect(0, 0, 127, 62, 1)
Writer.set_textpos(d0, 5, 15)  # Y,X
wTop.printstring('mpyEZfont')
d0.show()

begin = ticks_ms()

while True:
    # Show Mins / Secs/ 10's of sec
    now = int(ticks_diff(ticks_ms(), begin)*10)
    secs = int((now / 10000) % 60)
    mins = int((now / 600000) % 60)
    d0.rect(11, 21, 105, 21, 0,True)
    Writer.set_textpos(d0, 36, 22)  # Y,X
    wMins.printstring('{0:02d}'.format(mins) + ':')
    Writer.set_textpos(d0, 28, 55)  # Y,X
    wSecs.printstring('{0:02d}'.format(secs))
    Writer.set_textpos(d0, 44, 88)  # Y,X
    wSecsDec.printstring(':' + '{0:01d}'.format(int(now/10 % 10)))
    d0.show()


 
