# AdventOfCode2023

For solving Advent Of Code 2023 puzzles using python

There are a total of 50 puzzles, two puzzles each day for 25 days.
Each puzzle has it's own directory (i.e. `day01a` for day 1 puzzle a)
for the code (normally `puzzle01a.py` for example for day 1 puzzle a).
These directories have a subdirectory `data` for sample data, usually
`test.input` for the sample given with the puzzle and `my.input` as
the actual random input given for the competition.    

The puzzle program should look in the data directory for `.input` files
and produce corresponding `.output` files.

Common utilities can be found in `util.py` in the root directory, for example
functions to list the input files.

## Example

In the `_test` folder is a script called `example.py`.   This will sum
all the integers in `_test/data/example.input` and return the output.
Since `45` is passed as the 'expected' parameter, it asserts that the result
matches that value (`str()` called on each so numbers or strings can be
specified) and an error occurs if it doesn't equal.  If you have this
file open and there is an `example.input` file in the `data` subdirectory
you can hit 'F5' to debug:

```py
import sys, os
sys.path.insert(0, os.getcwd() + '/..')
from util import test_solution

# take an array of lines and return the solution
def solve(lines):
  return sum([int(f) for f in lines])

# attempt solution from lines in `example.input` in the `data`
test_solution(solve, 'example.input', 45)
```

If your solve function contains a parameter named `debug`, a file with
`.input` replaced with `.debug` will be created in the data directory
and the file object will be passed to your solve function also so that
you can print to it for debugging:

```py
import sys, os
sys.path.insert(0, os.getcwd() + '/..')
from util import test_solution

def solve(lines, debug):
  total = 0
  for i,line in enumerate(lines):
    intvalue = int(line)
    total += intvalue
    # output to debug file
    print("Line " + str(i) + " is '" + line + "', total is now " + str(total), file=debug)
  return total

test_solution(solve, 'example.input', 45)
```

## Notes

`test_solution` expects 2-3 parameters:

1. the solver function which takes a list of strings that are lines in the input file
2. the input file name, which should be in the 'data' directory under the current working directory
  * configured in launch.json to set CWD to the directory the python file being run is in
  * if running the puzzles from the console, you should change to their directory before running them
  * if using the Run (play button) on top of the code window, it uses the current console so you should change that to be the correct one where the file is in.
3. the expected output - displayed and throws an error if the result of calling the solver function is different (converted to strings to check)

`launch.config` should be setup so that these methods all use the debugger anbd
work, you need to install the Python addon (first available when searching
for Python, by Microsoft).  You should also probably create a virtual
environment (`CTRL+SHIFT_P` and `Python: Create Environment`) and then
select the interpreter from the environment (`CTRL+SHIFT_P` and 
`Python: Select Interpreter`).

> If using the play (not debug) icon at the top of a python file window,
it will be run in the current directory in the current console, so if you
aren't in the right directory you might get:
`ModuleNotFoundError: No module named 'util'`.   This is because `os.getcwd()`
is used to simplify code and the current directory should be the one
with your python file and with a `data` directory for inputs and debug outputs.
