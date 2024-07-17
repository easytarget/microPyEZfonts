from ezFBfont import ezFBfont
from sys import path

# fonts
path.append('fonts')
# Choose a font below.
#import ezFBfont_05_micro_ascii as thefont
#import ezFBfont_07_font_tiny5_ascii as thefont
import ezFBfont_10_6x12_ascii as thefont
#import ezFBfont_17_helvB12_ascii as thefont

'''
A demo of using ezMPfont to splat a load of fonts onto
a display; showing color setting, alignment, and changing
defaults for a font.
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
font = ezFBfont(display, thefont, vgap=0, verbose=True)

# Some text
source = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in \
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia \
deserunt mollit anim id est laborum.'

# 'chunk' the text into lines that do not exceed the screen
wide = 128
high = 64
wordlist = source.split(' ')
line = ''
vertical = 0
text = ''

# scan the source text adding words only wnen they do not exceed
# the screen, and ending once the bottom is reached.
for word in wordlist:
    w, h = font.size(line + word)
    if w > wide:
        vertical += h + font.vgap
        if vertical > high:
            break  # we now have a screenful of text
        else:
            text += line + '\n'
            line = ''
    line += word + ' ' 

print('Quote:\n{}'.format(text))

# write
font.write(text, 0, 0)
display.show()

# fin
