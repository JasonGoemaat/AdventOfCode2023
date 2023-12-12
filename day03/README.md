# Day 3 - part numbers

This day I am using one folder for both puzzles since I think days usually
share the test and personal inputs.   So there will be `part.py` and `part2.py`.
Also this would let me put common functions into a module in the same
directory (I think), maybe later.

Given a grid like this as input:

```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```

Find the numbers (i.e. 467) that are touching a symbol (not digit and not '.'),
and total their values to get the result.

I'm thinking pre-process lines looking for symbols and creating a list the
same size as the number of lines with locations for the symbols.   Then
use regular expressions on each line to find number locations and
check the symbol locations in the three lines (above, same, and below) to
see if a symbol exists within (start-1:end+1)
