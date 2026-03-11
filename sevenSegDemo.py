# Demo the 7seg font

from sys import path
path.append('drivers')
from repl_1306 import REPL_1306
path.append('demo_extra')
from ezFBfont import ezFBfont
from ezFBsevenSeg import SEVEN_SEG

# Display
display = REPL_1306(100, 64, clear=False, blocks=True)
display.invert(False)  # as needed
display.rotate(0)      # as needed
display.contrast(128)  # as needed

# Create a font instance
bigtimefont = SEVEN_SEG()

# Set it up
bigtimefont.set(height=58, width=32, thick=5, gap=3)

# Now create a font writer
bigtime = ezFBfont(display, bigtimefont)

#bigtime.write(' -\u2009.\u00B7\u02D9:\n01234567\n89ABCDEF',0,0)
bigtime.write('8:2',0,0)

display.show()
print(' -\u2009.\u00B7\u02D9:\n01234567\n89ABCDEF')
print(bigtimefont.info())
