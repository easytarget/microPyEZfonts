# Fremebuffer 'display' driver for REPL console
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
#
# Four optional arguments are:
# 'blocks=True' : use unicode blocks to do the display, otherwise use 'pure' ascii'
# 'clear=True'  : will send a clean screen sequence to the console before displaying.
# 'txt=False' : will suppress the ascii-art output completely.
# 'zero=<char>' and 'one=<char>' : will replace the ascii chars that represents zero and one.
#
# O.Carter, July 2024.
# This code is released as-is.
# The author disclaims any responsibility or liability arising from it's use.

from micropython import const
import framebuf

blks = ' ▄▀█'

class REPL_1306(framebuf.FrameBuffer):
    def __init__(self, width, height, txt=True, blocks=True, clear=False, zero='.', one='#'):
        self.width = width
        self.height = height
        self.txt = txt
        self._blocks = blocks
        self.clr = clear
        self.zero = zero
        self.one = one
        self.bytes = ((self.width - 1) // 8 ) + 1
        self.buffer = bytearray(self.bytes * self.height)
        self.lastbuf = ''
        self.format = framebuf.MONO_HLSB
        self._name = __name__
        super().__init__(self.buffer, self.width, self.height, self.format)
        self.init_display()

    def init_display(self):
        print('{}: init {}x{}'.format(self._name, self.width, self.height))
        self.fill(0)
        # self.show()

    def poweroff(self):
        print('{}: poweroff'.format(self._name))

    def poweron(self):
        print('{}: poweron'.format(self._name))

    def contrast(self, contrast):
        print('{}: contrast {}'.format(self._name, contrast))

    def invert(self, invert):
        print('{}: invert {}'.format(self._name, invert))

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
            out = []
            for l in range(0,self.height):
                t = ''
                for p in range(0,self.bytes):
                    t += ('{:08b}'.format(self.buffer[(l*self.bytes)+p]))
                out.append(t[:self.width])
            self.lastbuf = self.buffer.hex()
            if self._blocks:
                if len(out) % 2 != 0:   # add a dummy height as needed
                    out.append('0' * self.width)
                for l in range(0,len(out),2):
                    for b in range(0,len(out[l])):
                        blk = out[l][b:b+1] + out[l+1][b:b+1]
                        print(blks[int(blk,2)],end='')
                    print()
            else:
                for l in out:
                    print(l.replace('0',self.zero).replace('1',self.one))
        else:
            if self.clr:
                print('show: ',end='')  # stop show() operations scrolling the screen when clear is set
            else:
                print('{}: show (framebuffer has not changed)'.format(self._name))
