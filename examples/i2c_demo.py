from ezFBfont import ezFBfont
from sys import path
from time import sleep_ms
from gc import collect, mem_free

# fonts
path.append('fonts')
import ezFBfont_spleen_12x24_ascii_23
import ezFBfont_spleen_16x32_num_26
import ezFBfont_6x12_ascii_10
import ezFBfont_symb18_0x40_0x79_24

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
# EXAMPLE: You need to uncomment pins below, and modify if different for your hardware
#SDA = 4   # default esp8266 (D2 / gpio4)
#SCL = 5   # default esp8266 (D1 / gpio5)
#SDA = 21  # default esp32
#SCL = 22  # default esp32
#SDA = 28  # default rp2040
#SCL = 29  # default rp2040

# I2C
from machine import Pin, I2C, SoftI2C
# EXAMPLE: You need to uncomment one of the I2C entries below
# Wiring is important, you need good connections and pullup resisitors on the lines.
#  If you see continual 'OSError: with 'ENODEV' or 'ETIMEDOUT' you can try the SoftI2C
#  function instead, it is more tolerant of timing errors.
#  You can also play with frequency and timeout values, default:
#  freq=400000, timeout= 50000

#i2c=SoftI2C(sda=Pin(SDA), scl=Pin(SCL))  # rp2040/esp32 (alt)
#i2c=I2C(0,sda=Pin(SDA), scl=Pin(SCL))    # rp2040/esp32
#i2c = I2C(sda=Pin(SDA), scl=Pin(SCL))    # esp8266  (No hardware I2c..)

# Display
# You need to uncomment one of the entries below, as appropriate.
# The Device addresses used below are default for many screens
# You can use the `i2c-scanner.py` tool in the /devices folder to check
# this and verify your device.

# SSD 1306
#from ssd1306 import SSD1306_I2C
#display = SSD1306_I2C(128, 64, i2c, addr=0x3c)
#display.invert(1)      # as needed
#display.rotate(0)      # as needed
#display.contrast(128)  # as needed

# ST7567
#from st7567_i2c import ST7567
#display = ST7567(128, 64, i2c, addr=0x3f)
#display.set_contrast(31)  # as needed (max 63)

# SH1106
#from sh1106 import SH1106_I2C
#display = SH1106_I2C(128, 64, i2c, addr=0x3c)
#display.sleep(False)
#display.fill(0)
#display.invert(1)      # as needed
#display.flip()         # as needed
#display.contrast(128)  # as needed

# Font Init
font1 = ezFBfont(display, ezFBfont_spleen_12x24_ascii_23, tkey=0, verbose=True)
font2 = ezFBfont(display, ezFBfont_spleen_16x32_num_26, verbose=True)
font3 = ezFBfont(display, ezFBfont_6x12_ascii_10, verbose=True)
font4 = ezFBfont(display, ezFBfont_symb18_0x40_0x79_24, verbose=True)

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
