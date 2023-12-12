import sys, os, re
sys.path.insert(0, os.getcwd() + '/..')
from util import test_solution

game_re = re.compile("Game (\\d+):")
colors_re = re.compile("(\\d+) (red|blue|green)")

maxes = { "red": 12, "green": 13, "blue": 14 }

def game_value(line, debug):
  game_id = int(game_re.match(line).group(1))
  print('Game id', game_id, 'line: "' + line + '"', file=debug)

  all = colors_re.findall(line)
  for (count_string, color) in all:
    count = int(count_string)
    if (count > maxes[color]):
      # count is too high, return 0
      return 0

  return game_id

# take an array of lines and return the solution
def solve(lines, debug):
  total = 0
  for line in lines:
    total += game_value(line, debug)
  return total

# attempt solution from lines in `example.input` in the `data`
test_solution(solve, 'test.input', expected=8) # add expected = 8 when ready
test_solution(solve, 'my.input', 3099)
