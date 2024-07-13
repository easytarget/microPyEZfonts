from machine import Pin, I2C, SoftI2C
#from ssd1306 import SSD1306_I2C
from sh1106 import SH1106_I2C
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
