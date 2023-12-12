import os

def add(a, b):
  return a+b

def _input_name(f):
  return 'data/'+f

def _output_name(f):
  return 'data/'+f.replace('input','output')

def get_inputs():
  files = os.listdir('data')
  files = [(_input_name(f),_output_name(f)) for f in files if os.path.isfile('data/'+f) and f.endswith('.input')]
  return files

def start_file(tuple):
  _in, _out = tuple
  with open(_in) as f:
    lines = f.read().splitlines()
  return (lines, open(_out, "w"))

# this auto-processes all '.input' files in the data directory, and uses the form
# that writes to the output
def do_puzzle(solver):
  for f in get_inputs():
    (lines, out) = start_file(f)
    solver(lines, out)

#
def test_solver(solver, input_file_name, expected = None):
  output_file_name = input_file_name.replace('.input', '.output')
  with open(input_file_name) as f:
    lines = f.read().splitlines()
  out = open(output_file_name, "w")
  result = solver(lines, out)
  if expected == None:
    print(input_file_name + ' got ' + result)
  else:
    print(input_file_name + ' got ' + result + ' expected ' + expected)
    assert result == expected