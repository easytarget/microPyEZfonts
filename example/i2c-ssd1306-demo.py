from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
from ezFBfont import ezFBfont
from sys import path
from time import sleep_ms

# fonts
path.append('fonts')
import mPyEZfont_u8g2_spleen_12x24_r
import mPyEZfont_u8g2_spleen_16x32_n
import mPyEZfont_u8g2_6x12_r
import mPyEZfont_u8g2_symb18_e

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
font1 = ezFBfont(d0, mPyEZfont_u8g2_spleen_12x24_r, tkey=0)
font2 = ezFBfont(d0, mPyEZfont_u8g2_spleen_16x32_n)
font3 = ezFBfont(d0, mPyEZfont_u8g2_6x12_r, halign='center')
font4 = ezFBfont(d0, mPyEZfont_u8g2_symb18_e)

# main
font3.set_default(fg=0, bg=1)
text = 'Hello!\nNew\nWorld'
tx = 6
ty = 22
a,b,c,d = font3.rect(text, tx, ty)

# frame
d0.rect(0, 0, 127, 62, 1)
d0.show()
# write
font1.write('Test', 0, 0)
font2.write('1.23', 63, 0, fg=0, bg=1)
font3.write(text, tx, ty)
font4.write('bB1!%Z', 44, 32)
d0.show()

if False:  # rect() demo
    sleep_ms(1500)
    d0.rect(a,b,c,d,0,True)
    d0.show()
# fin
