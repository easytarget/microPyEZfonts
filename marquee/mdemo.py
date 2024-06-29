from repl_1306 import REPL_1306
from ezFBmarquee import ezFBmarquee
from sys import path, argv
from time import sleep

# fonts
path.append('fonts')
import ezFBfont_17_helvB12_ascii as font
#import ezFBfont_23_spleen_12x24_ascii as font
#import ezFBfont_16_open_iconic_all_2x_full as font

speed = float(argv[1]) if len(argv) == 2 else 1

message = 'This is quite a long 123 message, with %$@ stuff...'

w = 80
h = 18

display = REPL_1306(w, h, zero='.', one ='█', clear=True)

marquee = ezFBmarquee(display, font, verbose=True)

marquee.start(message, pause=100)

i = True
while True:
    sleep(speed)
    if marquee.step(1):
        if i:
            marquee.start('This is not so long', fg=1, bg=0, pause=50)
        else:
            marquee.start('Short', fg=0, bg=1)
        i = not i
    display.show()

