# basics
from sys import path, argv
from time import sleep, ticks_ms
# paths for convenience
path.append('..')
path.append('../drivers')
# Display
from repl_1306 import REPL_1306
# marquee
from ezFBmarquee import ezFBmarquee

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

# Display
w = 128
h = 64
display = REPL_1306(w, h, clear=True)

# two marquees
marquee1 = ezFBmarquee(display, font1)
marquee2 = ezFBmarquee(display, font2, x=32, y=35, width=64, mode='scroller', hgap=0)

def mstep():
    # Add a pause whenever marquee1 rolls over
    if marquee1.step(2):
        marquee1.pause(20)
    # Stop marquee2 when complete
    if marquee2.step(4):
        marquee2.stop()
    # Display results
    display.show()

# Start the main marquee
message = 'Info: This is a a long & boring informational message! [with ~{:d} chars]'
marquee1.start(message.format(len(message)), pause=20)

# A box around the uptime count
display.rect(41,21,46,14,1)

# Loop forever, starting the lower marquee at set times
tens = {0:'zero', 10:'ten', 20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty'}
# micropython on Linux doesnt support timer interrupts, so we have to call mstep()
# in the main loop and sleep()
while True:
    start = ticks_ms()
    # Uptime counter
    secs = int(start/1000 % 60)
    mins = int(start/60000 % 60)
    display.rect(44,24,40,8,0,True)
    display.text('{:02d}:{:02d}'.format(mins,secs),44,24)
    
    # start scrollbox on time based events
    if secs in tens.keys() and not marquee2.active():
        marquee2.start(tens[secs])
    mstep()
    while (start + 50) > ticks_ms():
        pass
