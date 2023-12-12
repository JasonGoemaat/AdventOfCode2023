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
    symbols.append([match.span()[0] for match in iterator])

  def is_symbol_touching(index, span):
    print('Checking these lines from', max(0,index-1), 'to', index+2) # +2 since it is AFTER
    print(lines[max(0,index-1):index+2])
    for symbol_line in symbols[max(0, index-1):index+2]:
      for symbol in symbol_line:
        if symbol >= span[0] - 1 and symbol <= span[1]:
          return True
    return False
  
  nums = []

  for i,line in enumerate(lines):
    print('Line',i,'"' + line + '"')
#    print('symbols:', symbols_re.findall(line))
#    print('Line',i,'numbers:', numbers_re.findall(line))
    for number in numbers_re.finditer(line):
      print('Number ', number.group(1), 'has span', number.span()) # group(1) is first matching parenthesised group (0) is full string
      if is_symbol_touching(i, number.span()):
        print('HAS SYMBOL!')
        nums.append(int(number.group(1)))
  print('nums:', nums)
  print('total:', sum(nums))
          

# attempt solution from lines in `example.input` in the `data`
test_solution(solve, 'test.input') # add expected = 4361 when ready
# test_solution(solve, 'my.input')
