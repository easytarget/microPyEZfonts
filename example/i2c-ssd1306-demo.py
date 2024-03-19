from time import sleep_ms,ticks_ms,ticks_diff
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
from sys import path
# fonts
path.append('fonts')

'''
'''

# I2C
I2C0_SDA_PIN = 28
I2C0_SCL_PIN = 29
i2c0=I2C(0,sda=Pin(I2C0_SDA_PIN), scl=Pin(I2C0_SCL_PIN))
# Dispayl
d0 = SSD1306_I2C(128, 64, i2c0, addr=0x3c)
d0.invert(False)
d0.rotate(1)
do.contrast(0.5)  # my screen is very bright

# Init
d0.rect(0, 0, 127, 16, 1)
d0.rect(10, 20, 107, 43, 1)
d0.text('serialOM', 40, 5, 1)
w0 = Writer(self._d0, mpyFbFont_u8g2_spleen_12x24)
w0.printstring("abcdef")
d0.show()

sleep_ms(2500)

while True:
    now = int(ticks_diff(ticks_ms(), self._begin))
    secs = int((now / 1000) % 60)
    mins = int((now / 60000) % 60)
    self._d0.fill_rect(11, 21, 105, 41, 0)
    self._d0.text(str(secs), 58, 35, 1)
    self._d0.rect(1, 1, 125, 14, 0, True)
    self._d0.show()
    slep_ms(1000)
