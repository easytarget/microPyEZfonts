from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
from ezFBfont import ezFBfont
from sys import path
from time import sleep_ms

# fonts
path.append('fonts')
import ezFBfont_05_micro_ascii as crtfont

'''
A demo of using ezMPfont to simulate the login
screen of a Commodore PET, my first computer
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
screen = SSD1306_I2C(128, 64, i2c0, addr=0x3c)
screen.invert(False)  # as needed
screen.rotate(0)      # as needed
screen.contrast(128)  # as needed

# Font Init
crt = ezFBfont(screen, crtfont, verbose=True)

text1 = '*** COMMODORE BASIC ***\n\n 3066 BYTES FREE\n'
text2 = 'READY.'
blink = 330

crt.write(text1, 0, 0)
_, v1 = crt.size(text1)

screen.show()
sleep_ms(blink*2)

crt.write(text2, 0, v1)
_, v2 = crt.size(text2)
sleep_ms(blink)

v = v1 + v2
b = 0
while True:
    crt.write(' ', 0, v, bg=b)
    b = 0 if b == 1 else 1
    screen.show()
    sleep_ms(blink)
# fin
