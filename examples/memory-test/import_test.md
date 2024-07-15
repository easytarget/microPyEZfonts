# Import test results (13 June 2024)

I tested the dictionary based (*dict*) fonts from 'bdf2font' against nominally identical modules from 'micropython-font-to-py' (*binary*).

## Hardware
For these memory tests I used a ESP8266 dev board (Wemos D1 Mini) (32k RAM, 4Mb flash).

## Test Script

See: [import_test.py](import_test.py)

The script loads a list of font files and records how much memory is used during the import.

It does this in 'pairs' for the matching font modules and then lists the results for these side-by-side.

### Test data

There are two test sets, with 4 tests in each:
* `size`: Four different fonts of increasing pixel size (height) are compared.
* `set` : The same font (17px high) is compared with four different character sets ranging from 'time' (15 chars) to 'full' (192 chars).

## CAVEAT:
This is 'rough' testing. I'm just using `gc.collect()` then `gc.mem_free()` before and after importing the module. The imported module is then indexed to make sure it has data, and references to it a deleted with `del`.

Repeated runs produce slightly different results, the ones below are 'typical', ymmv.

## Method

The test was run twice; once for 'frozen' font modules, and once for 'uploaded' ones.

### Frozen font files:
I followed the documentation to create a uploadable micropython firmware with the font files frozen in the `modules` folder. This was then flashed to the test board, the test script was then uploaded via the IDE and run.

### Uploaded font iles:
I flashed the test board with a vanilla micropython firmware from the main download site. Then all the font files were uploaded to the filesystem via the IDE, along with the test script. I then ran the test script.

The raw results are in [import_test_frozen.txt](import_test_frozen.txt) and [import_test_uploaded.txt](import_test_uploaded.txt)

## Results

### Frozen:
```text
test       :     bin     dict
-----      :   -----    -----
size:6     :     416     1104
size:14    :     384     1232
size:23    :     384     1104
size:33    :     384     1136
set:time   :     480      464
set:num    :     384      512
set:ascii  :     416     1136
set:full   :     400     1872
```
These results show that the binary font files are *very* efficient, using 400'ish bytes of RAM no matter how large or long the font and character set is.

The dictionary font modules show increasing size dependent on how many characters they encode, however the size (width,height) of the font makes no practical difference to the RAM used.

#### Uploaded
```text
test       :     bin     dict
-----      :   -----    -----
size:6     :    2144     4944
size:14    :    3232     5408
size:23    :    6704     8000
size:33    :   10032    12944
set:time   :    2432     1776
set:num    :    1824     2432
set:ascii  :    5104     8000
set:full   :   11264    15232
```
Both font module types show increasing RAM use as the pixel size and character set increase. The binary modules seem to typically use 2/3 the ram of the dictionary based ones. 

# Conclusion:

The fonts created by micropython-font-to-py show a definate advantage in terms of RAM use in all scenarios, but both font packaging methods are acceptably small for use in smaller devices in both uploaded and frozen useage.

## Reference: Font files
```console
-rw-r--r--. 1 owen owen  6627 Jul 13 12:19 mPyEZfont_u8g2_4x6_r.py
-rw-r--r--. 1 owen owen 47842 Jul 13 12:19 mPyEZfont_u8g2_courB14_e.py
-rw-r--r--. 1 owen owen  7487 Jul 13 12:19 mPyEZfont_u8g2_courB14_n.py
-rw-r--r--. 1 owen owen 21346 Jul 13 12:19 mPyEZfont_u8g2_courB14_r.py
-rw-r--r--. 1 owen owen  5031 Jul 13 12:19 mPyEZfont_u8g2_courB14_t.py
-rw-r--r--. 1 owen owen 27168 Jul 13 12:19 mPyEZfont_u8g2_spleen_12x24_r.py
-rw-r--r--. 1 owen owen 13268 Jul 13 12:19 mPyEZfont_u8g2_timB10_r.py
-rw-r--r--. 1 owen owen 42593 Jul 13 12:19 mPyEZfont_u8g2_timB24_r.py
-rw-r--r--. 1 owen owen  3971 Jul 13 13:51 ezFBfont_06_4x6_ascii.py
-rw-r--r--. 1 owen owen  4238 Jul 13 13:49 ezFBfont_12_courB14_time.py
-rw-r--r--. 1 owen owen  9504 Jul 13 15:42 ezFBfont_14_timB10_ascii.py
-rw-r--r--. 1 owen owen  5614 Jul 13 13:48 ezFBfont_16_courB14_num.py
-rw-r--r--. 1 owen owen 15962 Jul 13 13:49 ezFBfont_17_courB14_ascii.py
-rw-r--r--. 1 owen owen 33876 Jul 13 13:47 ezFBfont_20_courB14_full.py
-rw-r--r--. 1 owen owen 17010 Jul 13 13:52 ezFBfont_23_spleen_12x24_ascii.py
-rw-r--r--. 1 owen owen 34031 Jul 13 13:53 ezFBfont_33_timB24_ascii.py
```
