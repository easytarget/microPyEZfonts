from sys import path
# paths for convenience
path.append('..')
path.append('../drivers')
from repl_1306 import REPL_1306
from ezFBfont import ezFBfont
from time import ticks_ms, sleep_ms

# fonts
path.append('fonts')
import ezFBfont_helvB12_ascii_17 as header
import ezFBfont_7_Seg_41x21_0x0_0x39_37 as digits
import ezFBfont_7_Seg_33x19_0x0_0x39_29_base as decimals
# Replace the digits and decimals to try a conventional font
#import ezFBfont_spleen_16x32_num_26 as digits
#import ezFBfont_spleen_12x24_ascii_23 as decimals
import ezFBfont_open_iconic_human_2x_0x40_0x79_16 as icons

'''
A demo of using ezMPfont to do a simple uptime counter.
The 'baseline' vertical alignment, along with 'left'
and 'right' horizontal alignment, is used to align the
different fonts used in the time display.
'''

# Display
display = REPL_1306(128, 64, clear=True)
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
