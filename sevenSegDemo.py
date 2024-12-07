# Demo the 7seg font

from sys import path
path.append('drivers')
from repl_1306 import REPL_1306
from ezFBfont import ezFBfont
import ezFBsevenSeg as sevenSeg

# Display
display = REPL_1306(100, 32, clear=False, blocks=False)
display.invert(False)  # as needed
display.rotate(0)      # as needed
display.contrast(128)  # as needed

bigtime = ezFBfont(display, sevenSeg, hgap=2)

print(sevenSeg.info())

sevenSeg.set(pre='8')

print(sevenSeg.info())

bigtime.write('0123456789',0,0)

display.show()