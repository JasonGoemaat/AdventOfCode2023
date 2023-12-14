# Getting silly now, but you start with 1 of each card.  Once you 'scratch'
# a copy of the card, check for winning numbers.   You get extra copies of
# the following 'x' cards.   For example if card 1 had 2 winning numbers,
# you get extra copies of cards 2 and 3, so now you have 1 copy of card 1,
# 2 copies of card 2, and 2 copies of card 3.  If card 2 has 1 winning number,
# that gives you 2 *more* copies of card 3 because you have 2 copies of card 2,
# leaving you with 1 copy of card 1, 2 copies of card 2, and 4 copies of card 3.
# The answer is the TOTAL number of cards including originals and copies

import sys, os, re, bisect
sys.path.insert(0, os.getcwd() + '/..')
from util import test_solution

line_re = re.compile(r"Card +(\d+):([^|]+)\|(.*)")
nums_re = re.compile(r"(\d+)")

def count_winners(line):
  found = line_re.findall(line) # since there are multiple groups, a tuple with a value for each group is returned
  first = found[0]
  (card_index, winning_string, mine_string) = first
  winning = [int(x) for x in nums_re.findall(winning_string)] # since there is just one group, only that value of that gruop si returned
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
  return count

def solve(lines):
  cards = [1 for line in lines] # array filled with a 1 for each line
  for i,line in enumerate(lines):
    count = count_winners(line)
    for j in range(count):
      cards[i+j+1] += cards[i]
  return sum(cards)

test_solution(solve, 'test.input',30)
test_solution(solve, 'my.input')
