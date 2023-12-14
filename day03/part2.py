# Well, this is similar to part 1, but in reverse.  I should have gone
# ahead and processed both numbers and symbols, then I could have just
# changed a couple lines of code :).   Instead of looking at numbers and
# if *any* symbols are adjacent, we look for only the '*' symbol and
# find where *exactly* two numbers are adjacent.   We then multiply those
# numbers and sum all those products to get the answer.

import sys, os, re
sys.path.insert(0, os.getcwd() + '/..')
from util import test_solution

numbers_re = re.compile(r"(\d+)")
symbols_re = re.compile("([^\\d\\.])")
engines_re = re.compile(r"([\*])") # NOTE: use r"" to ignore escape characters in string

def solve(lines, debug):
  # numbers will be dict of (value,first,last) with number value and first/last
  # positions in the line
  numbers = []

  for line in lines:
    iterator = numbers_re.finditer(line)
    numbers.append([{"value": int(n.group(1)), "first": n.span()[0], "last": n.span()[1]-1} for n in iterator])

  # take the line index and position in line of a '*' and
  # return an array of integers for touching numbers
  def get_touching_numbers(index, pos):
    results = []
    for number_line in numbers[max(0,index-1):index+2]:
      for number in number_line:
        #print('checking pos',pos,'number',number)
        if pos >= number["first"]-1 and pos <= number["last"]+1:
          #print('ADDING VALUE')
          results.append(number["value"])
    return results

  total = 0

  # use enumerate() to get index we need to pass for finding adjacent lines,
  # and we get the index in i and the actual string in line
  for i,line in enumerate(lines):
    for engine in engines_re.finditer(line):
        nums = get_touching_numbers(i,engine.span()[0])
        #print('nums:',nums)
        if(len(nums)==2):
          total += nums[0]*nums[1]
  
  # error, I'm getting an extra number for the third engine: nums: [755, 664, 598]
  # the three rows:
  # ......755.
  # ...$.*....
  # .664.598..
  # obviously the 664 should not be included.
  
  return total

# attempt solution from lines in `example.input` in the `data`
test_solution(solve, 'test.input', 467835) # add expected = 4361 when ready
test_solution(solve, 'my.input')
