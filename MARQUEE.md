# `ezFBmarquee.py`

[![Marquee](https://img.youtube.com/vi/tW0iqCkWGVc/default.jpg)](https://www.youtube.com/watch?v=tW0iqCkWGVc)

## Simple Marquee/Scrolling Text Class

A marquee (scrolling text box) system designed for easy installation and use, particularly useful for small "info panel" type projects.

This works with *any* display that has a compatible driver for the built-in MicroPython [framebuffer](https://docs.micropython.org/en/latest/library/framebuf.html).

## Installation:
Copy the `ezFBmarquee.py` file from this repository into the main directory (or specified path) of your MicroPython project. Also include any necessary display drivers and font files. No additional requirements are needed.

## Quick Start
*ezFBmarquee* is a Python class you set up with a framebuffer device and a font.

You specify an output area with *init()*, set a message with *start()*, and then use *step()* regularly to advance the animation.

Check the [`examples`](examples) folder for code that demonstrates the features explained below and shows how to control the animation with a [Timer](https://docs.micropython.org/en/latest/library/machine.Timer.html) interrupt.

```python
from ezFBfont import ezFBmarquee
import mPyEZFont_XYZ

# Create a font object attached to a framebuffer device
mymarquee = ezFBmarquee(device, x, y, width)

# Set the message to display
mymarquee.start('Some very long string that we want to scroll')

# Use an interrupt or a fast-running main loop to step the marquee and display it
while True:
  ...
  mymarquee.step()
  device.show()
```

## Detailed Guide

You only need to specify the *width* of the output box; the *height* will be set automatically based on the font height.

The marquee has two **modes**:
* `marquee` mode: Starts with the message displayed left-aligned in the box. With each step, the box scrolls left, showing the next part of the message. The message wraps around after a configurable padding space, repeating when the text reaches the left edge again.
  * If the message is *shorter* than the box width, it doesn’t scroll.
* `scroller` mode: Starts with the box empty, and the message scrolls in from the right as you step. The message scrolls across and exits on the left. Once it’s fully out, the cycle begins again.

*(Remember to call *display.show()* after start() or step() to update the display.)*

### Creating a Font Instance:

Import the font class and any font(s) you need:
```python
from ezFBmarquee import ezFBmarquee
import mPyEZFont_myfont as fontName
# Repeat for additional fonts as needed
```

Then create a marquee instance for each imported font:
```python
mymarquee = ezFBmarquee(device, fontName,
                        x=0, y=0,
                        width=None,
                        mode='marquee',
                        pad=0.33, pause=0, hgap=0,
                        fg=1, bg=0,
                        cswap=False,
                        verbose=False)
```

**Required Arguments:**
* *device*: The framebuffer device for display.
* *fontName*: The imported font module name.

**Optional Arguments:**
* *x*, *y* (integers, px): Top-left corner of the output box.
  * Defaults to 0 if not set.
* *width* (integer, px): Width of the box.
  * If `None` (the default), the width extends to the display’s right edge (if determinable).
* *mode* (string): Set to `'marquee'` or `'scroller'`
  * Default is `'marquee'`, as explained above.
* *pad* (float): Padding space at the end of the message.
  * Sets a fraction of the box width to add space between repeats of the message in *marquee* mode.
  * Not used in *scroller* mode.
* *pause* (integer): Initial pause before the message starts moving.
  * Animation doesn’t start until this many steps are called.
  * Setting to `-1` pauses indefinitely until reset.
* *hgap* (integer, px): Adds/removes space between characters.
  * Defaults to `0`, applied between individual characters only.
  * Negative values allow characters to overlap.
* *fg*, *bg* (integers): Foreground and background colors.
  * Foreground defaults to 1; adjust as needed for color displays.
  * Marquee always fully overwrites the specified area.
* *cswap* (bool): Swaps bytes in 16-bit color words.
  * Default is `False`; set `True` for RGB displays with reversed byte order (e.g., st7789).
* *verbose* (bool): Enables detailed feedback on initialization, starting, pausing, and stopping.

### Methods:

#### `start()`
```python
mymarquee.start(string, mode=None, pause=None, pad=None, hgap=None, fg=None, bg=None)
```
Starts the marquee, calling an initial *step(0)* to show the marquee in its start position.

**Positional Arguments:**
* *string*: Text to be displayed.

**Optional Arguments:**
* Can override any defaults specified in the initialization.

#### `stop()`
```python
mymarquee.stop()
```
Stops and clears the marquee, filling the output box with the background color.

#### `step()`
```python
mymarquee.step(steps=1)
```
Advances the animation by *steps* (in px). Steps are kept between 0 and the output box width.
* If the *pause* counter is above zero, it reduces the pause counter by one instead of advancing.
* Redraws the output, even if paused or *steps=0*.

Returns `True` if the animation loops back to the start.
* This can trigger *pause()* for marquees or *stop()* a scroller after showing the message.

If a *marquee* message is smaller than the box width, it won’t scroll.
* Internal step count still advances, so a "virtual" rollover occurs once steps exceed box width.

#### `pause()`
```python
mymarquee.pause(pause)
```
Sets the pause counter to the provided value (integer; `-1` pauses indefinitely).

#### `active()`
```python
mymarquee.active()
```
Returns `True` if the marquee is active (showing a message).

-----------------------
### Future Ideas:
These are not currently planned but should be relatively easy to add based on the marquee’s architecture:
* Reversible scroll direction, e.g., allow negative step() values.
* Vertical marquee for multi-line text, or vertical scroller for the same.
* Allow mid-scroll text changes, useful for time displays, etc.
