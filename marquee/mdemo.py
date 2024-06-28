from repl_1306 import REPL_1306
from ezFBmarquee import ezFBmarquee
from sys import path
from time import sleep

# fonts
path.append('fonts')
import ezFBfont_10_courR08_ascii as font

message = 'Peachy'

print('go')
display = REPL_1306(80,12, zero=' ')

marquee = ezFBmarquee(display, font, 'Peachy Demo of marquee.', verbose=True)
#marquee = ezFBmarquee(display, font, 'Peachy', verbose=True)

while True:
    marquee.step()
    #display.show()
    sleep(0.2)

