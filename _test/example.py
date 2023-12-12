import sys, os
sys.path.insert(0, os.getcwd() + '/..')
from util import test_solution

def solve(lines):
  return sum([int(f) for f in lines])

test_solution(solve, 'example.input', 45)