from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
from ezFBfont import ezFBfont
from sys import path
from time import sleep_ms
from gc import collect, mem_free

# fonts
path.append('fonts')
import mPyEZfont_u8g2_spleen_12x24_r
import mPyEZfont_u8g2_spleen_16x32_n
import mPyEZfont_u8g2_6x12_r
import mPyEZfont_u8g2_symb18_e

'''
A demo of using ezMPfont to splat a load of fonts onto
a display; showing color setting, alignment, and changing
defaults for a font.
Also shows how to use info obtained from font.rect() to
blank (fill with display.rect()) the written string.

This is a good example to 'play' with, try changing fonts,
adding/removing options etc.
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
font1 = ezFBfont(d0, mPyEZfont_u8g2_spleen_12x24_r, tkey=0, verbose=True)
font2 = ezFBfont(d0, mPyEZfont_u8g2_spleen_16x32_n, verbose=True)
font3 = ezFBfont(d0, mPyEZfont_u8g2_6x12_r, verbose=True)
font4 = ezFBfont(d0, mPyEZfont_u8g2_symb18_e, verbose=True)

# multiline demo stuff
font3.set_default(halign='center', valign='baseline')
text = 'Hello!\nmy\nWorld'
tx = 24
ty = 32
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

while True:  # rect() demo
    sleep_ms(1000)
    d0.rect(a,b,c,d,0,True)
    d0.show()
    sleep_ms(1000)
    font3.write(text, tx, ty)
    d0.show()
# fin
