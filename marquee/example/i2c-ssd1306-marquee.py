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

w = 128
h = 64

# Display
display = SSD1306_I2C(128, 64, i2c0, addr=0x3c)
display.invert(False)  # as needed
display.rotate(0)      # as needed
display.contrast(128)  # as needed

speed = 0.1

message = 'This is a a long & boring informational message! [with ~{:d} chars]'
message = message.format(len(message))

marquee1 = ezFBmarquee(display, font1, verbose=True)
marquee2 = ezFBmarquee(display, font2, x=32, y=35, pre=1, pad=1, hgap=-1, width=64, verbose=True)

# splash
marquee2.text('Splash!', pre=0.2, pad=0.2, hgap=2)
display.show()
sleep(0.25)
while not marquee2.step(2, event='endpad'):
    display.show()
sleep(0.25)
marquee2.text(None)
display.show()


# Timer interrupt to step both marquees
def mstep(t):
    marquee1.step(2)
    if marquee2.step(1, event='endstr'):
        marquee2.text(None)
    display.show()

# Start the timer
tim0 = Timer(0)
tim0.init(period=100, mode=Timer.PERIODIC, callback=mstep)

# Start the main marquee
marquee1.text(message, pause=20)

# A box for the uptime count
display.rect(41,21,46,14,1)

# Loop forever, starting the second marquee at set times
while True:
    secs = int(ticks_ms()/1000 % 60)
    mins = int(ticks_ms()/60000 % 60)
    display.rect(44,24,40,8,0,True)
    display.text('{:02d}:{:02d}'.format(mins,secs),44,24)
    if secs == 0 and marquee2._string is None:
        marquee2.text('Hello World')
    if secs == 30 and marquee2._string is None:
        marquee2.text('Goodbye World')
