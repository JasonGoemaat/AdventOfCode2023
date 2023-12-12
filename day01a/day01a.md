# Day 01 Puzzle A

https://adventofcode.com/2023/day/1

Test input:

```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

> In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

## Reasoning

* The *FIRST* and *LAST* digits on the line are taken to produce a two digit number.
* These numbers are totalled together for all the lines to produce the result
* As the last example line shows, there may be only 1 digit

