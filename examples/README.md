# Examples

Examples for use with all compatible displays!

# Use:
* Copy display driver for your device to the root of the project
* Copy *ezFBfont* (and *ezFBmarquee*) from the root of this repo to your project root
* Copy the required fonts to a folder named /fonts in your project.
* Copy the examples to the project, read (or at least skim) the comments, then uncomment & edit all the indicated entries as needed

## I2C vs SPI vs ???
All the current examples are for I2C devices, I have not (yet?) tested with SPI devices, and so have no examples for them. However; my drivers are for the framebuffer, not specific displays, so any properly configured framebuffer enabled SPI display will work.

## Tested Displays/Devices
I have tested these fonts with three physical I2C displays +  drivers: SSD1306, SH1106 and ST7567
* Uncomment the appropriate lines in the i2c examples for these.
* The examples contain defaults for RP2040, ESP32 and ESP8266 based development boards, and have been tested on them.

## The list
* 'demo' : just a bunch of fonts, colors and alignments rendered by `ezFBfont`. Good for 'playing' with to see how things work in practice.
* 'counter' : a simple uptime counter.
* 'lorum-ipsum' : demonstrating small fonts text.
* 'commodore_welcome' : simulating the login screen of a commodore PET (for nostalgia).
* 'unicode' : Display Unicode text from the `unicode.txt` file, an expanded version of the example given on the [Unicode](/Unicode) page.
* 'marquee' : An example for `exFBmarquee`.

[![two different displays](doc/demo-collage2.thumb.jpg)](examples/doc/demo-collage2.jpg)

# REPL driver examples:

`repl_1306.py` (in the [drivers](/drivers) folder) is a 'fake' display driver that outputs to the console. Useful for debug, on-the-go development and checking alignments etc.

## There are demos for the repl_1306 text-based test driver:

These examples are designed to be run 'in place' on the repo using micropython from the command line eg:
```console
owen@sam:examples$ micropython repl_unicode.py 
repl_1306: init 80x42
repl_1306: invert False
repl_1306: rotate 0
repl_1306: contrast 128
ezFBfont_unicode_hello_b24 : initialised: height: 24, max width: 24, baseline: 22
ezFBfont_unicode_hello_b24 = fg: 1, bg: 0, tkey: -1, halign: center, valign: center, hgap: 1, vgap: -3, split: '\n'
你好
Hello
repl_1306: show
                   ▄██   ▄█▀                ██    ▀▀▀▀▀▀▀▀▀██▀                  
                   ██   ▄█▀       ▄▄        ██  ▄▄        █▀                    
                  ██▄  ▄█▀▀▀█▀▀▀▀▀██▀  ▀▀▀▀██▀▀▀██▀    █▄▀                      
                ▄███  ▄█▀   ██▀  ▀         ██   ██     ██                       
               ▄▀ ██ ▄▀ ▄   ██             ██  ▄█▀     ██   ▄▄                  
              ▀   ██    ██▀ ██ ▀█▄        ██   ██ ▀▀▀▀▀██▀▀▀▀▀▀                 
                  ██   ██   ██   ▀█▄      ██  ▄█▀      ██                       
                  ██  ▄█    ██    ▀█▄    ██ ▀▄█▀       ██                       
                  ██ ▄▀     ██     █▀       ▄█▀█▄      ██                       
                  ██    ▄▄▄▄██             ▄▀  ▀██     ██                       
                  █▀      ▀█▀           ▄▄▀     ▀▀  ▀▀██▀                       
                                                                                
         ██     ██                    ██           ██                           
         ██     ██                    ██           ██                           
         ██     ██     ▄█████▄        ██           ██         ▄█████▄           
         █████████    ██▀    ██       ██           ██        ██▀   ▀██          
         ██     ██    █████████       ██           ██        ██     ██          
         ██     ██    ██     ▄▄       ██           ██        ██▄   ▄██          
         ██     ██     ▀██████▀       ▀███         ▀███       ▀█████▀           
                                                                                
```
The `repl_1306` driver replicates the functions of the 'default' ssd_1306' driver:
```python
owen@sam: $ micropython
MicroPython v1.22.2 on 2024-03-22; linux [GCC 14.0.1] version
Use Ctrl-D to exit, Ctrl-E for paste mode
>>> import repl_1306
>>> d = repl_1306.REPL_1306(80, 10, blocks=False)
repl_1306: init 80x10
>>> d.text('Hello',10,2)
>>> d.show()
repl_1306: show
................................................................................
................................................................................
...........##..##...........###.....###.........................................
...........##..##............##......##.........................................
...........##..##...####.....##......##.....####................................
...........######..##..##....##......##....##..##...............................
...........##..##..######....##......##....##..##...............................
...........##..##..##........##......##....##..##...............................
...........##..##...#####...####....####....####................................
................................................................................
>>>
```
