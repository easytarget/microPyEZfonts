from repl_1306 import REPL_1306
from ezFBfont import ezFBfont
from sys import path
from time import sleep_ms

# fonts
path.append('fonts')
import ezFBfont_unicode_hello_b24 as unicode_font

'''
A demo of using ezMPfont to splat a load of fonts onto
a display; showing color setting, alignment, and changing
defaults for a font.
'''

# Display
display = REPL_1306(80, 40, zero=' ')
display.invert(False)  # as needed
display.rotate(0)      # as needed
display.contrast(128)  # as needed

# Font Init
font = ezFBfont(display,
                unicode_font,
                tkey = 0,
                halign='center',
                valign='top',
                hgap=2,
                vgap=-4,
                verbose=True)

# What to display
xpos = 39
ypos = 0
file = 'unicode.txt'
# Enable for a 'box display' showing printed areas
boxes = False

try:
    # read the unicode file
    with open(file, 'r') as source:
        text = source.read()
    # strip trailing newline(s) left by text editors etc..
    while text[-1] == '\n':
        text = text[0:-1]
except:
    # default text if reading fails for any reason
    text = 'Hello\nWorld'
print(text)

# write
font.write(text, xpos, ypos, tkey=0)
display.show()

if boxes:
    sleep_ms(1000)
    font.write(text, xpos, ypos, fg=0, bg=1)
    display.show()
    x,y,w,h = font.rect(text, xpos, ypos)
    sleep_ms(1000)
    display.rect(x,y,w,h,1,False)
    display.show()

# fin
