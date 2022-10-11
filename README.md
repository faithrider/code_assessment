# grid_interpolation

### Purpose of the program:
This program allows a user to input a 4x4 grid of values, then interpolate any number of those values. Interpolation, in this context is averaging the surrounding values
(including corners), then setting the cell equal to that. If the average is a decimal number, it rounds down to the next whole number (integer floor division)

### Example:

| 0 | 0 | 1 | 0 |
|---|---|---|---|
| 0 | 6 | 3 | 2 |
| 0 | 4 | 0 | 0 |
| 5 | 0 | 0 | 0 |

User wants to interpolate the 4 (index 2,1). There are 8 neighbors, so the average is (0+6+3+0+0+5+0+0 / 8) = 1.75, rounded down is 1.

Thus, the new grid is as follows.

| 0 | 0 | 1 | 0 |
|---|---|---|---|
| 0 | 6 | 3 | 2 |
| 0 | 1 | 0 | 0 |
| 5 | 0 | 0 | 0 |

##### Language is python, GUI framework is TKinter.
