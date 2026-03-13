# Demo the 7seg font

from sys import path
path.append('drivers')
from repl_1306 import REPL_1306
path.append('demo_extra')
from ezFBfont import ezFBfont
from ezFBsevenSeg import SEVEN_SEG

X = 24
Y = 34

# Display
display = REPL_1306(X * 5, Y * 2, clear=False, blocks=True)
display.fill(1)

# Create a font instance
bigtimefont = SEVEN_SEG(height = Y, width = X)

# Set font up
#bigtimefont.set()

# Now create a font writer
bigtime = ezFBfont(display, bigtimefont, hgap=1, vgap=1, fg=1, bg=0)

#bigtime.write(' -\u2009.\u00B7\u02D9:\n01234567\n89ABCDEF',0,0)
#bigtime.write('08:34\n56.79\u00B721\n ABCDEF',0,0)
bigtime.write('08:34\n¯-_.\u00B7\u02D9',0,0)
#bigtime.write(':8',0,0)

display.show()
#print(' -\u2009.\u00B7\u02D9:\n01234567\n89ABCDEF')
bigtimefont.info()
