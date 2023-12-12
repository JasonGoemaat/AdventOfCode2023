import sys
sys.path.insert(0, '..')
from util import do_puzzle

def solve_line(line):
  length = len(line)
  a = 0
  b = 0
  for i in range(length):
    if line[i] >= '0' and line[i] <= '9':
      a = int(line[i])
      break
  for i in range(length):
    ch = line[length - i - 1]
    if ch >= '0' and ch <= '9':
      b = int(ch)
      break
  return a * 10 + b

def solve(lines, out):
  total = 0
  for line in lines:
    total += solve_line(line)
  print(total, file=out)

do_puzzle(solve)
