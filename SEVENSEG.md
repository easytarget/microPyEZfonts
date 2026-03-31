# Dynamic 7-Segment display font

*   Supports all hexidecimal digits (`0123456789ABCDEF`) at full width, plus hyphen (minus, `-`), decimal (`.`), space (` `) and colon (`:`) as half-width chars.
    *   It also has half width chars for 'center dot' and 'upper dot', and full width chars for 'underscore', 'top bar', 'tri-bar' and 'degrees'.

## Features:
*   Scales smothly from a 4x6 (width * height) to infinity (memory limited).
*   Characters are drawn on demand when first used, then cached for faster access later.
    *   You can pre-cache characters when the font is initialised
    *   Caching can also be disabled
*   Automatic sizing and placement of LED elements within the character
