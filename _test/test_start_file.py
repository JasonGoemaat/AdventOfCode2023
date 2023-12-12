# This tests the util methods to handle `.input` files in the data directory
# by loading the first file and returning a file object to output to an
# `.output` file with the same name.
import sys
import os
sys.path.insert(0, '..')
from util import get_inputs, start_file

###############################################################################
# get_inputs returns a list of tuples.   Each tuple has two values, the
# path to a '.input' file in the data directory, and a corresponding path
# to an '.output' file with the same name in the data directory
files = get_inputs()

# we have two test files in the data directory
assert len(files) == 1

###############################################################################
# start_file takes a tuple with the input and output file names and returns
# a tuple with two values: a list of the lines in the input file and a FILE
# that you can use for output

# find 'test.input' as input name (first index 0 of tuple) for files
# and put tuple values into variables
# 1. filter files where tuple 0 (`f[0]`) contains the string 'test.input',
# 2. return element 0 of results which should be a tuple
# 3. put tuple elements into variables in_filename and out_filename
file = [f for f in files if 'test.input' in f[0]][0]

(in_filename, out_filename) = file
assert in_filename == 'data/test.input'
assert out_filename == 'data/test.output'

# delete output file if it exists
try:
  os.remove('data/test.output')
except OSError:
  pass

# start file, should return lines and file for outputing, total int values
(lines, out) = start_file(file)
result = sum([int(line) for line in lines])
assert result == 154

# write to file, close it, read it back and validate results
out.write(str(result))
out.close()
with open(out_filename) as f:
  output_file_contents = f.read()
assert output_file_contents == '154'