from repl_1306 import REPL_1306
from ezFBmarquee import ezFBmarquee
from sys import path, argv
from time import sleep

# fonts
path.append('fonts')
#import ezFBfont_17_helvB12_ascii as font
import ezFBfont_23_spleen_12x24_ascii as font
#import ezFBfont_16_open_iconic_all_2x_full as font

speed = float(argv[1]) if len(argv) == 2 else 1

message = 'This_is-a.long*message! [with ~{:d} chars]'
message = message.format(len(message))

w = 120
h = 32

display = REPL_1306(w, h, zero='.', one ='█', clear=True)
display.rect(0,0,w,h,1)
display.line(0,0,w-1,h-1,1)
display.line(0,h-1,w-1,0,1)
display.show()

marquee = ezFBmarquee(display, font, x=10, y=3, width=80, verbose=True)

marquee.set(message, pause=2//speed)

while True:
    sleep(speed)
    display.hline(0,h//2,w,1)
    display.vline(w//2,0,h,1)
    if marquee.step(1):
        marquee.pause(1//speed)
        #marquee.set(None)
    display.show()

