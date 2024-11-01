# `ezFBmarquee.py`

[![Marquee](https://img.youtube.com/vi/tW0iqCkWGVc/default.jpg)](https://www.youtube.com/watch?v=tW0iqCkWGVc)

## A simple marquee/scroller class for a line of text

A marquee (scrolling info box) system optimised for ease of installation and use; especially for small 'info panel' type projects.

This will work with *any* display that has a driver for the built-in microPyton [framebuffer](https://docs.micropython.org/en/latest/library/framebuf.html).

## install:
Copy the `ezFBmarquee.py` file from this repository into the root (or path) of your MicroPython project, along with the relevant display driver and font files you want to use. There are no other requirements.

## quickstart
*ezFBmarquee* is a python class that is initiated against a framebuffer device, and a font. 

You declare an output area during *init()* and then allocate messages to that with *start()*. A *step()* method needs to be called regularlly to advance the animation.

See the [`examples`](examples) folder for some working code that uses the features described below, and shows how to drive the animation via a [Timer](https://docs.micropython.org/en/latest/library/machine.Timer.html) Interrupt.

```python
from ezFBfont import ezFBmarquee
import mPyEZFont_XYZ

... create a font object attached to a framebuffer device
mymarquee = ezFBmarquee(device, x, y, width)

... set the message to be displayed
mymarquee.start('Some very long string that we want to scroll')

... Use an interrupt, or a main loop that runs fast and steps the marquee before displaying
while True:
  ...
  mymarquee.step()
  device.show()
```

## In detail

You can only specify the *width* of the output box, the *height* will be derived from the font height.

The marquee has two **modes**:
* `marquee` mode starts with the message displayed left-aligned in the box, on each step the box scrolls left moving the next part of the message into view. The message will wrap around after a (configurable) padding space and the sequence begins again when the repeat of the message reaches the left edge.
  * If the message is *smaller* than the box width once rendered it is not scrolled.
* `scroller` mode starts with the box empty, the message will scroll into view from the right as it is stepped and scroll accross the box, before dissappearing on the left. Once the message has fully scrolled out of the box the cycle begins again.

(Do not forget to call *display.show()* after start() or step() to see your results)

### Create an instance for the font:

The font class and the font(s) required need to be imported:
```python
from ezFBmarquee import ezFBmarquee
import mPyEZFont_myfont as fontName
#...etc for all fonts
```

You then create a marquee instance for the imported font:
```python
mymarquee = ezFBmarquee(device, fontName,
                        x=0, y=0,
                        width=None,
                        mode='marquee',
                        pad=0.33, pause=0, hgap=0,
                        fg=1, bg=0,
                        cswap = False,
                        verbose=False)
```
Required Arguments:
* *device* : The framebuffer device to write to.
* *fontName* : the name of the imported font module.

Optional Arguments:
* *x*, *y*: (integer, px) : the top-left position of the output box.
  * Will default to zero if not specified.
* *width*: (integer, px) : the box width.
  * If 'None', the default, the width will go to the right-hand edge of the display (if it can be determined).
* *mode*: (string) : one of `'marquee'` or `'scroller'`
  * Defaults to *marquee*, see above.
* *pad*: (float) : message end padding.
  * Sets a fraction of the output box width that should be used as padding between repeats of the message in *marquee* mode.
  * Not used in *scroller* mode.
* *pause*: (integer) : an initial pause count to set when the font is started.
  * The output will not begin to animate until this many steps have been called after starting.
  * Setting to `-1` pauses indefinately until reset to zero or higher.
* *hgap*: (integer, px) : add or remove spacing between characters.
  * Defaults to `0`, and is only applied between individual characters.
  * Negative values are allowed, characters will render over each other as needed.
* *fg*, *bg*: (integers) : foreground and background colors.
  * Foreground will default to 1; for color displays this needs to be set appropriately.
  * The marquee cannot be displayed transparently the box will always fully overwrite the specified area.
* *cswap*: (bool) : Swap bytes in 16-bit color word.
  * Default False; only needs to be set True for RGB displays with reversed byte order (eg st7789).
* *verbose*: (bool) : enables verbose feedback on init, start, pause and stop.

### Methods:

#### start()
```python
mymarquee.start(string, mode=None, pause=None, pad=None, hgap=None, fg=None, bg=None)
```
Starts the marquee, will perform an initial *step(0)* call to display the marquee in it's start position.

Positional Arguments:
* *string* : The text to be displayed

Optional Arguments:
* as per init options, values supplied will override the default.

#### stop()
```python
mymarquee.stop()
```
Immediately stops and clears the marquee; fills the output box with the marquee background color.

#### step()
```python
mymarquee.step(steps=1)
```
Moves the animation by *steps* (in px), the value of steps will be constrained between 0 and the output box width.
* If the *pause* counter is above zero no animation is done, and the pause counter is reduced by one instead.
* The output is always re-drawn, even if paused or when steps=0.

Returns `True` if the animation has 'rolled over' and restarted from the initial postion.
* This can be used to add a *pause()* to marquees, or *stop()* a scroller after it has shown it's message.

If a *marquee* mode message's width is smaller than the output box width the message is not animated.
* But the internal step count still advances and a 'virtual' rollover will occur once the step count has exceeded the output box width.

#### pause()
```python
mymarquee.pause(pause)
```
Sets the pause counter to the supplied value (integer, -1 pauses indefinately)

#### active()
```python
mymarquee.active()
```
Returns `True` if the marquee is active (displaying a message)

-----------------------
### Thoughts:
None of these are planned; but due to the architecture of the marquee code they should be relative easy to implement.
* Make the scroll direction reversible, eg allow negative step()s and set a step() default.
* Vertical marquee (also for multi-line strings), Vertical scroller for the same.
* Allow changing text mid scroll, this could be nice for time displays etc. 
