from machine import Pin, I2C, SoftI2C
#from ssd1306 import SSD1306_I2C
from sh1106 import SH1106_I2C
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
SDA = 4   # default esp8266 (D2 / gpio4)
#SCL = 5   # default esp8266 (D1 / gpio5)
SCL = 14  #(D5 / gpio14)
#SDA = 21  # default esp32
#SCL = 22  # default esp32
#SDA = 28  # default rp2040
#SCL = 29  # default rp2040

# I2C
# Wiring is important, you need good connections and pullup resisitors on the lines.
#  If you see continual 'OSError: with 'ENODEV' or 'ETIMEDOUT' you can try the SoftI2C
#  function instead, it is more tolerant of timing errors.
#  You can also play with frequency and timeout values, default:
#  freq=400000, timeout= 50000
#i2c=SoftI2C(sda=Pin(SDA), scl=Pin(SCL))  # rp2040/esp32
#i2c=I2C(0,sda=Pin(SDA), scl=Pin(SCL))    # rp2040/esp32
i2c = I2C(sda=Pin(SDA), scl=Pin(SCL))    # esp8266  (No hardware I2c..)

# Display
#display = SSD1306_I2C(128, 64, i2c, addr=0x3c)
display = SH1106_I2C(128, 64, i2c, addr=0x3c)
display.sleep(False)
display.fill(0)
display.show()
#display.invert(False)  # as needed
#display.rotate(0)      # as needed
#display.contrast(128)  # as needed

# Font Init
crt = ezFBfont(display, crtfont, verbose=True)

# Display in stages, as if machine is starting up
text1 = '*** COMMODORE BASIC ***\n\n 3066 BYTES FREE\n'
text2 = 'READY.'
blink = 330

crt.write(text1, 0, 0)
_, v1 = crt.size(text1)

display.show()
sleep_ms(blink*2)

crt.write(text2, 0, v1)
_, v2 = crt.size(text2)
sleep_ms(blink)

# Position a cursor and blink it..
v = v1 + v2
b = 0
while True:
    crt.write(' ', 0, v, bg=b)
    b = 0 if b == 1 else 1
    display.show()
    sleep_ms(blink)
# fin
