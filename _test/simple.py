################################################################################
# This shows the simple way to do a puzzle, write a solver function and
# pass it to do_puzzle from the util.py module in the parent directory.
# This will call the solver function for each '.input' file in the data
# subdirectory, passing the contents as a list of lines and an output file
# for writing to named the same but with the '.output' extension.
################################################################################
import sys
sys.path.insert(0, '..')
from util import do_puzzle

def solve(lines, out):
  result = sum([int(line) for line in lines])
  out.write(str(result))

# this helper will call a solve function for each `.input` file in the
# `data` subdirectory.   The solve function should take two arguments,
# a list with strings for each l ine in the file and an output file object
# to write to.
do_puzzle(solve)

################################################################################
# Now to test our results :)
################################################################################
def assert_file(name, expected):
  with open(name) as f:
    text = f.read()
    print(name + ' contains: ' + text)
    assert text == expected

assert_file('data/test.output','154')
assert_file('data/second.output','45')

#with open('data/second.input') as f:
#  for line in f.read().splitlines(): # NOTE: does not include last line if empty due to POSIX standard, each line should contain a LF, even the last
#    print("line: '" + line + '"')