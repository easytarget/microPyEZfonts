from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
from ezFBfont import ezFBfont
from sys import path
from time import sleep_ms
from gc import collect, mem_free

# fonts
path.append('fonts')
import ezFBfont_23_spleen_12x24_ascii
import ezFBfont_26_spleen_16x32_num
import ezFBfont_10_6x12_ascii
import ezFBfont_24_symb18_lower

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
display = SSD1306_I2C(128, 64, i2c0, addr=0x3c)
display.invert(False)  # as needed
display.rotate(0)      # as needed
display.contrast(128)  # as needed

# Font Init
font1 = ezFBfont(display, ezFBfont_23_spleen_12x24_ascii, tkey=0, verbose=True)
font2 = ezFBfont(display, ezFBfont_26_spleen_16x32_num, verbose=True)
font3 = ezFBfont(display, ezFBfont_10_6x12_ascii, verbose=True)
font4 = ezFBfont(display, ezFBfont_24_symb18_lower, verbose=True)

# multiline demo stuff
font3.set_default(tkey=0, halign='center', valign='baseline', vgap=-1)
text = 'Hello!\nMPy\nWorld'
tx = 24
ty = 32
a,b,c,d = font3.rect(text, tx, ty)

# frame
display.rect(0, 0, 128, 64, 1)
display.show()

# write
font1.write('Test', 0, 0)
font2.write('1.23', 63, 0, fg=0, bg=1)
font3.write(text, tx, ty)
font4.write('^ezdemo', 44, 32)
display.show()

while True:  # rect() demo
    sleep_ms(1000)
    display.rect(a,b,c,d,0,True)
    display.show()
    sleep_ms(1000)
    font3.write(text, tx, ty)
    display.show()
# fin
