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

def do_puzzle(solver):
  for f in get_inputs():
    (lines, out) = start_file(f)
    solver(lines, out)
