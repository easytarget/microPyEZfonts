from ezFBmarquee import ezFBmarquee
from sys import path, argv
from time import sleep, ticks_ms

# Interrupt timer
from machine import Timer
from micropython import schedule

# fonts
path.append('fonts')
import ezFBfont_15_helvR10_ascii as font1
import ezFBfont_23_spleen_12x24_ascii as font2

'''
A demo of using ezFBmarquee to animate messages

It uses a simple 'as fast as possible' loop for a splashscreen
and then uses an interrupt timer to step marquees in the background

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

# two marquees
marquee1 = ezFBmarquee(display, font1, verbose=True)
marquee2 = ezFBmarquee(display, font2, x=32, y=35, width=64, mode='scroller', hgap=0, verbose=True)

# Timer interrupt to step both marquees
def mstep(t):
    def uptime():
        s = int(ticks_ms()/1000 % 60)
        m = int(ticks_ms()/60000 % 60)
        display.rect(44,24,40,8,0,True)
        display.text('{:02d}:{:02d}'.format(m,s),44,24)

    # step marquee1 and add a pause whenever it rolls over
    if marquee1.step(2):
        marquee1.pause(20)
    # step marquee2 and stop when complete
    if marquee2.step(4):
        marquee2.stop()
    # add the uptime
    uptime()
    # Display results
    display.show()

# Start the timer
tim0 = Timer(0)
tim0.init(period=100, mode=Timer.PERIODIC, callback=mstep)

# Start the main marquee
message = 'Info: This is a a long & boring informational message! [with ~{:d} chars]'
marquee1.start(message.format(len(message)), pause=20)

# A box around the uptime count
display.rect(41,21,46,14,1)

# Loop forever, starting the lower marquee at set times
tens = {0:'zero', 10:'ten', 20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty'}
while True:
    # start scrollbox on time based events
    secs = int(ticks_ms()/1000 % 60)
    if secs in tens.keys() and not marquee2.active():
        marquee2.start(tens[secs])
