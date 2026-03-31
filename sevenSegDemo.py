# Demo the 7seg font

from sys import path
path.append('drivers')
from repl_1306 import REPL_1306
path.append('demo_extra')
from ezFBfont import ezFBfont
from ezFBsevenSeg import SEVEN_SEG

X = 20
Y = 28

# Display
display = REPL_1306(X * 8, Y * 3, clear = False, blocks = True)
display.fill(0)

# Create a font instance
bigtimefont = SEVEN_SEG(height = Y, width = X)

# Set font up
#bigtimefont.set(led_wide = None, led_high = None, led_thick = None, led_gap = None)

# Now create a font writer
bigtime = ezFBfont(display, bigtimefont)

bigtime.write('n01234567\n89ABCDEF\nG _-¯≡\u2009.\u00B7\u02D9:', 1, 0)
#bigtime.write(' -\u2009.\u00B7\u02D9:\n01234567\n89ABCDEF', 0, 0)
#bigtime.write('08:34\n56.79\u00B721\n ABCDEF', 0, 0)
#bigtime.write('08:34\n¯-_.\u00B7\u02D9', 1, 1)
#bigtime.write('8.3', 0, 0)

display.show()
#print(' -\u2009.\u00B7\u02D9:\n01234567\n89ABCDEF')
bigtimefont.info()
