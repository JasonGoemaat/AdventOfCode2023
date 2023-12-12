# much like the first puzzle, but the digits 0-9 can also be spelled out
import sys
sys.path.insert(0, '..')
from util import do_puzzle

string_values = {
  '0': 0,
  '1': 1,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'zero': 0,
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9
}

def value_at(line, index):
  length = len(line)
  for k,v in string_values.items(): # NOTE: .items() on a dictionary can enumerate keys and values, see https://docs.python.org/3/tutorial/datastructures.html
    if index+len(k) >= length:
      break
    sub = line[index:(index+len(k))] # NOTE: index with start:end to get substring, can also take step parameter
    if sub == k:
      return v
  return -1 # not valid

def solve_line(line):
  length = len(line)
  a = 0
  b = 0
  for i in range(length):
    x = value_at(line, i)
    if x >= 0:
      a = x
      break
  for i in range(length):
    x = value_at(line, i)
    if x >= 0:
      b = x
      break
  return a * 10 + b

def solve(lines, out):
  total = 0
  for line in lines:
    total += solve_line(line)
  print(total, file=out)

do_puzzle(solve)
