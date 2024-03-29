from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
from ezFBfont import ezFBfont
from sys import path
from time import sleep_ms

# fonts
from writer import Writer
path.append('fonts')
import mPyEZfont_u8g2_spleen_12x24_r
import mPyEZfont_u8g2_spleen_16x32_n
import mPyEZfont_u8g2_6x12_r
import mPyEZfont_u8g2_symb18_e

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
d0.invert(False)  # as needed
d0.rotate(0)      # as needed
d0.contrast(128)  # as needed

# Font Init
font1 = ezFBfont(d0, mPyEZfont_u8g2_spleen_12x24_r)
font2 = ezFBfont(d0, mPyEZfont_u8g2_spleen_16x32_n, fg=0, bg=1)
font3 = ezFBfont(d0, mPyEZfont_u8g2_6x12_r)
font4 = ezFBfont(d0, mPyEZfont_u8g2_symb18_e)

font4.set_color(tkey=0)

# Screen Init
d0.rect(0, 0, 127, 62, 1)
d0.show()
# demo
font1.write('Test', (0, 0))
font2.write('1.23', (56, 4))
font3.write('Hello\nWorld', (6, 32))
font4.write('bB1!%Z', (44, 32))
d0.show()
