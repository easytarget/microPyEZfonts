# Fremebuffer 'disply' driver for REPL console
# 
# Emulates the interface of the 'classic' ssd1306.py display driver from:
#   https://github.com/stlehmann/micropython-ssd1306
# Provides a log output of all operations to the REPL console,
# Displays a ascii-art dump of the framebuffer when show() is called
# Allows debugging of display operations when running micropython on 
#  desktop systems without needing an attached device (eg with thonny)
#
# Init requires just two options: width, height
# The screen will only be ascii dumped when it has changed
# Three optional arguments are: 'clear=True' which will send a clean screen 
# sequence to the console before displaying the ascii 'display'.
#  'txt=False' will suppress the ascii-art output completely.
#  'zero=<char>' will replace the ascii character (.) that represents zero.
#
# O.Carter, June 2024.
# This code is released as-is.
# The author disclaims any responsibility or liability arising from it's use.

from micropython import const
import framebuf

class REPL_1306(framebuf.FrameBuffer):
    def __init__(self, width, height, txt=True, clear=False, zero='.'):
        self.width = width
        self.height = height
        self.txt = txt
        self.clr = clear
        self.zero = zero
        self.bytes = self.width // 8
        self.buffer = bytearray(self.bytes * self.height)
        self.lastbuf = ''
        self.format = framebuf.MONO_HLSB
        self._name = __name__
        super().__init__(self.buffer, self.width, self.height, self.format)
        self.init_display()

    def init_display(self):
        print('{}: init {}x{}'.format(self._name, self.width, self.height))
        self.fill(0)
        self.show()

    def poweroff(self):
        print('{}: poweroff'.format(self._name))

    def poweron(self):
        print('{}: poweron'.format(self._name))

    def contrast(self, contrast):
        print('{}: contrast {}'.format(self._name, contrast))

    def invert(self, invert):
        print('{}: invert'.format(self._name))

    def rotate(self, rotate):
        print('{}: rotate {}'.format(self._name, rotate))

    def show(self):
        if not self.txt:
            print('{}: show'.format(self._name))
            return
        if (self.buffer.hex() != self.lastbuf):
            if self.clr:
                print('\x1b[2J\x1b[H{}: show'.format(self._name))
            else:
                print('{}: show'.format(self._name))
            for l in range(0,self.height):
                t = ''
                for p in range(0,self.bytes):
                    t += ('{:08b}'.format(self.buffer[(l*self.bytes)+p]))
                print(t.replace('0',self.zero).replace('1','#'))
            self.lastbuf = self.buffer.hex()
        else:
            if self.clr:
                print('show: ',end='')  # stop show() operations scrolling the screen when clear is set
            else:
                print('{}: show (framebuffer has not changed)'.format(self._name))
        
