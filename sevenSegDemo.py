# Demo the 7seg font

from sys import path
path.append('drivers')
from repl_1306 import REPL_1306
from ezFBfont import ezFBfont
import ezFBsevenSeg as sevenSeg

# Display
display = REPL_1306(128, 64, clear=True)
display.invert(False)  # as needed
display.rotate(0)      # as needed
display.contrast(128)  # as needed

bigtime = ezFBfont(display, sevenSeg, halign='center', valign='center')

sevenSeg.get()
