from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
from sh1106 import SH1106_I2C
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
#I2C0_SDA_PIN = 21  # default esp32
#I2C0_SCL_PIN = 22  # default esp32
#I2C0_SDA_PIN = 28  # default rp2040
#I2C0_SCL_PIN = 29  # default rp2040

# I2C
# Wiring is important, you need good connections and pullup resisitors on the lines.
#  If you see continual 'OSError: with 'ENODEV' or 'ETIMEDOUT' you can try the SoftI2C
#  function instead, it is more tolerant of timing errors.
#  You can also play with frequency and timeout values, default:
#  freq=400000, timeout= 50000
#i2c0=SoftI2C(sda=5, scl=2)
#i2c0=I2C(0,sda=Pin(I2C0_SDA_PIN), scl=Pin(I2C0_SCL_PIN))

# from machine import Pin, I2C
# 
#
i2c = I2C(sda=Pin(4), scl=Pin(14), freq=400000)
display = SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
display.sleep(False)
display.fill(0)
display.text('Testing 1', 0, 0, 1)
display.show()


# Display
#display = SSD1306_I2C(128, 64, i2c0, addr=0x78)
#display.invert(False)  # as needed
#display.rotate(0)      # as needed
#display.contrast(128)  # as needed

# Font Init
font = ezFBfont(display, thefont, vgap=0, verbose=False)

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