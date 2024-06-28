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

message = 'This is quite a long 123 message, with %$@ stuff...'

w = 100
h = 28

display = REPL_1306(w, h, zero=' ', one ='█', clear=True)
display.rect(0,0,w,h,1)

marquee = ezFBmarquee(display, font, message, y=2, hgap=-1, pause=10, verbose=True)

while True:
    sleep(speed)
    if marquee.step(3):
        print('Rollover')
        marquee.pause(10)
    display.show()

