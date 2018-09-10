# Overview
Prints a diamond of alphabetic characters starting at "A" and ending at the specified character.
For example,

`./print-diamond g` produces
```
      A
     B B
    C   C
   D     D
  E       E
 F         F
G           G
 F         F
  E       E
   D     D
    C   C
     B B
      A
```

# Installation
This project requires Python3 to run. No other external dependencies or modules required.

# Running
If `python3` is on your PATH, you can run the file from the terminal as

`./print-diamond end-character`

where `end-character` is any alphabetic character.

---

If `python3` is not on your PATH, you can run the file by using

`/path/to/python3 print-diamond end-character`

### Internal Parameters
Within `diamond.py`, there are some global parameters you can tweak:

- INNER_SPACER : Character to to print on the interior of the diamond (should remain a single character)
- OUTER_SPACER : Character to to print on the exterior of the diamond (should remain a single character)
- START_CHAR : Character printed at the top/bottom of the diamond

# Project Structure
The UI logic can be found in `print-diamond`.

The core logic can be found in `diamond.py`.

The unit tests can be found in `tests.py` and the associated `.txt` files.





