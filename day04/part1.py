# should be easy-peasy, take a line like this:
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# First numbers before | are winning, numbers after are our numbers.  Count
# how many of our numbers are winning.   The point value is pow(2,count-1),
# so 1 for 1 match, 2 for 2, 4 for 3, 8 for 4, 16 for 5, etc.

# Well, this is similar to part 1, but in reverse.  I should have gone
# ahead and processed both numbers and symbols, then I could have just
# changed a couple lines of code :).   Instead of looking at numbers and
# if *any* symbols are adjacent, we look for only the '*' symbol and
# find where *exactly* two numbers are adjacent.   We then multiply those
# numbers and sum all those products to get the answer.

import sys, os, re, bisect
sys.path.insert(0, os.getcwd() + '/..')
from util import test_solution

line_re = re.compile(r"Card +(\d+):([^|]+)\|(.*)")
nums_re = re.compile(r"(\d+)")

def solve(lines):
  total=0
  for i,line in enumerate(lines):
    # findall returns an array with one tuple element, a little confusing,
    # but it could be a big string with the whole thing found multiple times
    # which I guess makes sense.   So instead, maybe find?
    found = line_re.findall(line) # this returns tuples?
    first = found[0]
    (card_index, winning_string, mine_string) = first

    winning = [int(x) for x in nums_re.findall(winning_string)] # since there is just one group, this works?
    winning.sort() # for using bisect as binary search
    
    mine = [int(x) for x in nums_re.findall(mine_string)]
    count = 0
    for m in mine:
      # bisect_left finds position of element if it exists, or position to
      # insert if it does not (i.e. all values left will be lower and index
      # and all positions after will be higher)
      index = bisect.bisect_left(winning, m)
      if (index<len(winning) and winning[index]==m):
        count+=1
    if count>0:
      total += 2**(count-1)
  return total

# attempt solution from lines in `example.input` in the `data`
test_solution(solve, 'test.input',13)
test_solution(solve, 'my.input')
