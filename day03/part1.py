import sys, os, re
sys.path.insert(0, os.getcwd() + '/..')
from util import test_solution

numbers_re = re.compile(r"(\d+)")
symbols_re = re.compile("([^\\d\\.])")

def solve(lines, debug):
  # symbols will be array of arrays of positions of symbols
  symbols = []

  for line in lines:
    # finditer returns an iterator of matches, and span() on the match
    # gives a tuple with the first and last+1 character of the match,
    # as in all the range and substring methods where the 'end' is actually
    # the index *after* the last one that matches
    iterator = symbols_re.finditer(line)

    # we're looking for single character positions, so use [0] of the span
    # which is the actual position of the first character of the match.
    # [1] would be the position AFTER the last character of the match
    symbols.append([match.span()[0] for match in iterator])

  # helper function, check symbols array for three lines, the one above,
  # the current line, and the line below.   Returns True if there is a symbol
  # touching the number up, down, left, right, or diagonal.
  def is_symbol_touching(index, span):
    for symbol_line in symbols[max(0, index-1):index+2]:
      for symbol in symbol_line:
        if symbol >= span[0] - 1 and symbol <= span[1]:
          return True
    return False
  
  total = 0

  # use enumerate() to get index we need to pass for finding adjacent lines,
  # and we get the index in i and the actual string in line
  for i,line in enumerate(lines):
    # use an iterator to find numbers which gives Match objects, so it is
    # easy to get the actual number since the digits are in parenthesis in the
    # regular expression using number.group(1), and we can also access 
    # number.span() which gives the index OF the first character and the
    # index AFTER the last character for use in findign symbols
    for number in numbers_re.finditer(line):
      if is_symbol_touching(i, number.span()):
        # at least one symbol is touching, add number to total
        total += int(number.group(1))
  return total

# attempt solution from lines in `example.input` in the `data`
test_solution(solve, 'test.input', 4361) # add expected = 4361 when ready
test_solution(solve, 'my.input')
