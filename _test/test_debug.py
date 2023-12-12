################################################################################
# Testing debuging in VSCODE using launch.json

import os
print('cwd:')
print(os.getcwd()) # ok, this is the base folder VSCODE has open

# so try adding that to path to find util.py in it:
import sys
#sys.path.insert(0, os.getcwd()) # for debugging
#sys.path.insert(0, os.getcwd() + '/..') # for running in terminal from script dir
sys.path.insert(0, os.path.dirname(__file__) + "/../")

print('os.getcwd() is:', os.getcwd())
print('sys.path is: ', sys.path)
print('sys.executable is:' + sys.executable)
print('__file__ is: ', __file__)
print('os.path.dirname(__file__) is: ', os.path.dirname(__file__))
from util import do_puzzle, test_solver
print('__name__ is: ' + __name__)
data_dir = os.path.dirname(__file__) + "/data/"

def solve(lines, out):
  print('Hello, world!', file=out)
  for i, line in enumerate(lines):
    print('Line ' + str(i) + ': ' + line)
  return '281'

test_solver(solve, data_dir+"test_day01b.input", '281')

print('os.getcwd() is:', os.getcwd())
