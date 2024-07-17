from sys import path
# paths for convenience
path.append('..')
path.append('../drivers')
from repl_1306 import REPL_1306
from ezFBfont import ezFBfont

# fonts
path.append('fonts')
# Choose a font below.
#import ezFBfont_05_micro_ascii as thefont
import ezFBfont_07_font_tiny5_ascii as thefont
#import ezFBfont_10_6x12_ascii as thefont
#import ezFBfont_17_helvB12_ascii as thefont

'''
A demo of using ezMPfont to display text in a set font
'''

# Display
display = REPL_1306(128, 64, clear=True)
display.invert(False)  # as needed
display.rotate(0)      # as needed
display.contrast(128)  # as needed

# Font Init
font = ezFBfont(display, thefont, vgap=0, verbose=True)

# Some text
source = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in \
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia \
deserunt mollit anim id est laborum.'

# 'chunk' the text into lines that do not exceed the screen
wide = 128
high = 64
wordlist = source.split(' ')
line = ''
vertical = 0
text = ''

# scan the source text adding words only wnen they do not exceed
# the screen, and ending once the bottom is reached.
for word in wordlist:
    w, h = font.size(line + word)
    if w > wide:
        vertical += h + font.vgap
        if vertical > high:
            break  # we now have a screenful of text
        else:
            text += line + '\n'
            line = ''
    line += word + ' ' 

print('Quote:\n{}'.format(text))

# write
font.write(text, 0, 0)
display.show()

# fin
