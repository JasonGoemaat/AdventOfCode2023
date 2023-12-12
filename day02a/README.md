# Day 2 part 1

Seems simple enough, just have to figure out how to parse these lines:

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

Each game is a set of values separated by semicolons it seems.   These
sets of values are themselves comma-separated lists of numbers and colors
('red', 'green', 'blue').   Each of these separate lists must have less
than 12 red, less than 13 green, and less than 14 blue to be 'possible'.

We have to total the ids (i.e. '1' in 'Game 1') that are possible and
that is the answer.

Right away I'm thinking of a function named 'calc' that takes a line and
returns the integer of the id if it is possible, or 0 if not.  Then I can
use something like this to quickly total all the lines for the result:

```py
result = sum([calc(line) for line in lines])
```

The `calc()` function needs to do the parsing and return 0 if any of the
sets exceed the limits.  I'm thinking about using regular expressions
for this since it seems like a natural way to do it, and since I want to
learn how to use them in python.   Another option would be splitting,
first based on ':' to separate out the 'Game {id}', then by semicolon
to separate the individual options, then by ', ' to separate individual values.
And maybe then by space to separate 'Game' from the game id and number from
the color, and using int() on the game id and number strings.

Using regex and testing python on https://regex101.com it looks like this would
pull the game id:

