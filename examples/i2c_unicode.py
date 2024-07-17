from ezFBfont import ezFBfont
from sys import path
from time import sleep_ms

# fonts
path.append('fonts')
import ezFBfont_unicode_hello_b24 as unicode_font

'''
A demo of using ezMPfont to display a unicode font
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
#i2c = I2C(sda=Pin(SDA), scl=Pin(SCL))    # esp8266  (No hardware i2c)

# Display
# EXAMPLE: You need to uncomment one of the entries below, as appropriate.
# The Device addresses used below are default for many screens
# You can use the `i2c-scanner.py` tool in the /devices folder to check
# this and verify your device.

# SSD 1306
#from ssd1306 import SSD1306_I2C
#display = SSD1306_I2C(128, 64, i2c, addr=0x3c)
#display.invert(False)  # as needed
#display.rotate(0)      # as needed
#display.contrast(128)  # as needed

# ST7567
#from st7567_i2c import ST7567
#display = ST7567(128, 64, i2c, addr=0x3f)
#display.set_contrast(31)  # as needed (max 63)

# SH1106
#from sh1106 import SH1106_I2C
#display = SH1106_I2C(128, 64, i2c, addr=0x3c)
#display.invert(1)  # as needed
#display.flip()      # as needed
#display.contrast(128)  # as needed
#display.sleep(False)
#display.fill(0)

# Font Init
font = ezFBfont(display, unicode_font,
                halign='center',
                valign='center',
                hgap=1,
                vgap=1,
                verbose=True)

# What to display
xpos = 63
ypos = 31
file = 'unicode.txt'
# Enable for a 'box display' showing printed areas
boxes = False

try:
    # read the unicode file
    with open(file, 'r') as source:
        text = source.read()
    # strip trailing newline(s) left by text editors etc..
    while text[-1] == '\n':
        text = text[0:-1]
except:
    # default text if reading fails for any reason
    text = 'File\nnot\nFound'
print(text)

# write
font.write(text, xpos, ypos, tkey=0)
display.show()

if boxes:
    sleep_ms(1000)
    font.write(text, xpos, ypos, fg=0, bg=1)
    display.show()
    x,y,w,h = font.rect(text, xpos, ypos)
    sleep_ms(1000)
    display.rect(x,y,w,h,1,False)
    display.show()

# fin
