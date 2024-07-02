# basics
from sys import path, argv
from time import sleep, ticks_ms
# display hardware
from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
# marquee
from ezFBmarquee import ezFBmarquee
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
w = 128
h = 64
display = SSD1306_I2C(w, h, i2c0, addr=0x3c)
display.invert(False)  # as needed
display.rotate(0)      # as needed
display.contrast(128)  # as needed

# two marquees
marquee1 = ezFBmarquee(display, font1, verbose=True)
marquee2 = ezFBmarquee(display, font2, x=32, y=35, width=64, mode='scroller', hgap=-1, verbose=True)

# Timer interrupt to step both marquees
def mstep(t):
    # Add a pause whenever marquee1 rolls over
    if marquee1.step(2):
        marquee1.pause(20)
    # Stop marquee2 when complete
    if marquee2.step(4):
        marquee2.stop()
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

# Loop forever, starting the second marquee at set times
tens = {0:'zero', 10:'ten', 20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty'}
while True:
    # Uptime counter
    secs = int(ticks_ms()/1000 % 60)
    mins = int(ticks_ms()/60000 % 60)
    display.rect(44,24,40,8,0,True)
    display.text('{:02d}:{:02d}'.format(mins,secs),44,24)
    
    # start scrollbox on time based events
    if secs in tens.keys() and not marquee2.active():
        marquee2.start(tens[secs])