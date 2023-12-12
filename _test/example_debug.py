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