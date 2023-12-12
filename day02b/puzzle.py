import sys, os, re
sys.path.insert(0, os.getcwd() + '/..')
from util import test_solution

# Very similar to part 1, but isntead of comparing each values, I need
# to find the max of each color and multiply them together for each
# game, then total all those values.

colors_re = re.compile("(\\d+) (red|blue|green)")


def game_value(line, debug):
  totals = { "red": 0, "green": 0, "blue": 0 }
  all = colors_re.findall(line)
  for (count_string, color) in all:
    count = int(count_string)
    totals[color] = max(totals[color], count)
  return totals["red"] * totals["green"] * totals["blue"]

# take an array of lines and return the solution
def solve(lines, debug):
  total = 0
  for line in lines:
    total += game_value(line, debug)
  return total

# attempt solution from lines in `example.input` in the `data`
test_solution(solve, 'test.input', expected=2286) # add expected = 8 when ready
test_solution(solve, 'my.input')
