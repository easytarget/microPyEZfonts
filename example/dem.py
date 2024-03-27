from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
from ezFBstr import ezFBstr
from sys import path
from time import sleep_ms

# fonts
from writer import Writer
path.append('fonts')
import mPyEZfont_u8g2_spleen_16x32_n
import mPyEZfont_u8g2_6x12_r

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
font = ezFBstr(d0,
               mPyEZfont_u8g2_spleen_16x32_n,
               size=None,
               fmt=None,
               color=None,
               halign='left',
               valign='top',
               rot=0,
               verbose=True)

# Screen Init
d0.rect(0, 0, 127, 62, 1)
d0.show()
sleep_ms(1000)

font.write('12:34:56', (30, 20))
d0.show()
sleep_ms(1000)

font.write('56:7\n8:90', (30, 20))
d0.show()

 
