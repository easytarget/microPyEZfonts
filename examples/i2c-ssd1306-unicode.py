from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
from ezFBfont import ezFBfont
from sys import path
from time import sleep_ms
from gc import collect, mem_free

# fonts
path.append('fonts')
import ezFBfont_unicode_hello_b24 as unicode_font

'''
A demo of using ezMPfont to splat a load of fonts onto
a display; showing color setting, alignment, and changing
defaults for a font.
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
font = ezFBfont(display, unicode_font, halign='center', vgap=4, verbose=True)

file = 'unicode.txt'

try:
    with open(file, 'r') as source:
        text = source.read()
    print(text)
except Exception as e:
    print('failed to open file {}\n{}'.format(file, e))
    while True:
        sleep_ms(1000)  # go into loop

# frame
#d0.rect(0, 0, 127, 62, 1)

# write
font.write(text, 63, 6)
display.show()

# fin
