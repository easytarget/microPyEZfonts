# Demo the 7seg font

from sys import path
path.append('drivers')
from repl_1306 import REPL_1306
from ezFBfont import ezFBfont
import ezFBsevenSeg as sevenSeg

# Display
display = REPL_1306(160, 102, clear=False, blocks=True)
display.invert(False)  # as needed
display.rotate(0)      # as needed
display.contrast(128)  # as needed

bigtime = ezFBfont(display, sevenSeg)

sevenSeg.set(pre='0123456789 ')

print(sevenSeg.info())

bigtime.write('-+.:\'"°8%)',0,0)
bigtime.write('01234567',0,34)
bigtime.write('89ABCDEF',0,68)

display.show()
