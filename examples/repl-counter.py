from sys import path
# paths for convenience
path.append('..')
path.append('../drivers')
from repl_1306 import REPL_1306
from ezFBfont import ezFBfont
from time import ticks_ms, sleep_ms

# fonts
path.append('fonts')
import ezFBfont_17_helvB12_ascii as header
import ezFBfont_37_7_Seg_41x21_base as digits
import ezFBfont_29_7_Seg_33x19_base as decimals
# Replace the digits and decimals to try a conventional font
#import ezFBfont_26_spleen_16x32_num as digits
#import ezFBfont_23_spleen_12x24_ascii as decimals
import ezFBfont_16_open_iconic_human_2x_lower as icons

'''
A demo of using ezMPfont to do a simple uptime counter.
The 'baseline' vertical alignment, along with 'left'
and 'right' horizontal alignment, is used to align the
different fonts used in the time display.
'''

# Display
display = REPL_1306(128, 64, clear=True, zero=' ')
display.invert(False)  # as needed
display.rotate(0)      # as needed
display.contrast(128)  # as needed

# Font Init
heading = ezFBfont(display, header)
lcdm = ezFBfont(display, digits, halign='right', hgap=-1, valign='baseline')
lcds = ezFBfont(display, decimals, valign='baseline')
icon = ezFBfont(display, icons, halign='center', valign='center')

numline = 60

# frame
def clean():
    display.fill(0)
    heading.write('UpTime:', 0, 0)
    display.show()

d = True
# loop
clean()
while True:
    upsecs = int(ticks_ms() / 1000)
    secs = upsecs % 60
    mins = int(upsecs / 60) % 60
    hrs = int(upsecs / 3600) % 24
    beat = int(ticks_ms() / 333) % 2
    lcdm.write('{:d}:{:02d}'.format(hrs, mins), 84, numline)
    lcds.write(':{:02d}'.format(secs), 84, numline)
    icon.write(chr(66), 118, 7, fg=beat)
    display.show()
    sleep_ms(10)
# fin
