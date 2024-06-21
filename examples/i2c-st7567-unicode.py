from machine import Pin, I2C, SoftI2C
from st7567_i2c import ST7567
from ezFBfont import ezFBfont
from sys import path
from time import sleep_ms

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
display = ST7567(128, 64, i2c0, addr=0x3f)
display.set_contrast(31)  # as needed (max 63)

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
    text = 'Hello\nWorld'
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

