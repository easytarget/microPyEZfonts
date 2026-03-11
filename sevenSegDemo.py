# Demo the 7seg font

from sys import path
path.append('drivers')
from repl_1306 import REPL_1306
path.append('demo_extra')
from ezFBfont import ezFBfont
from ezFBsevenSeg import SEVEN_SEG

X = 20
Y = 32

# Display
display = REPL_1306(X * 7, Y * 3, clear=False, blocks=True)

# Create a font instance
bigtimefont = SEVEN_SEG(height = Y, width = X)

# Set font up
bigtimefont.set(led_high=None, led_wide=None, led_thick=None, led_gap=None)

# Now create a font writer
bigtime = ezFBfont(display, bigtimefont, fg=1, bg=0)

#bigtime.write(' -\u2009.\u00B7\u02D9:\n01234567\n89ABCDEF',0,0)
bigtime.write('08:34\n56.79\u00B721\n ABCDEF',0,0)

display.show()
print(' -\u2009.\u00B7\u02D9:\n01234567\n89ABCDEF')
print(bigtimefont.info())
