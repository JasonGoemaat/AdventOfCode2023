# need to be sure about parsing
# The first line is a list of seeds:
#     seeds: 79 14 55 13
# So part 2 is different because instead of representing four seeds,
# these actually represent two ranges for seed values, 79-92 (14 values
# starting at 79) and 55-67 (13 values starting at 55).
# We still need to provide the lowest seed number.   I think in this case
# we need to use ranges because a range may overlap, enclose, or
# be outside of any of our mapping ranges.
#
# Ok, I settles on using the 'python-ranges' library (pip install python-ranges)
# This lets you use Range and RangeSet objects.   I also create a
# LocationMap class so I can associate a range with the difference

import sys, os, re, bisect
sys.path.insert(0, os.getcwd() + '/..')
from util import test_solution
from ranges import Range, RangeSet

# not much here, most of it is __str__ and __repr__ for pretty debugging
class LocationMap:
  def __init__(self, nums):
    self.source_range = Range(nums[1],nums[1]+nums[2])
    self.diff = nums[0]-nums[1]
  def __str__(self):
     s = ""
     if self.diff >=0:
         s = "+"
     return str(self.source_range)+s+str(self.diff)
  def __repr__(self):
     s = ""
     if self.diff >=0:
         s = "+"
     return str(self.source_range)+s+str(self.diff)

nums_re = re.compile(r"(\d+)")

def parse_map(line):
  v = [int(x) for x in nums_re.findall(line)]
  # list is start, end (last num + 1 as python end is after last), change (amount to add to convert if the value is in the range)
  return LocationMap(v)

def parse(lines):
  seed_ranges = RangeSet()
  seed_nums = [int(x) for x in nums_re.findall(lines[0])]
  for i in range(0, len(seed_nums), 2):
    a = seed_nums[i]
    b = seed_nums[i+1]
    seed_ranges += Range(a,a+b)
  
  map_types = []
  current = None
  for i in range(2,len(lines)):
    line = lines[i]
    if (line.endswith(' map:')):
      current = []
      map_types.append(current)
      continue
    if len(line) > 0:
      current.append(parse_map(line))
  return (seed_ranges, map_types)

def output(seeds, maps, debug):
  print('Seeds:', seeds, file=debug)

def solve(lines,debug):
  (seed_ranges, map_types) = parse(lines)
  # the actual result requires mapping all seeds, and returning the lowest
  # location number after applying all the maps
  output(seed_ranges, map_types, debug)
  for mt in map_types:
    new_ranges = RangeSet()
    for r in seed_ranges:
      # try to apply each mapping inside this list of LocationMaps
      for lm in mt:
        if r != None:
          i = RangeSet(r.intersection(lm.source_range))
          d = RangeSet(r.difference(lm.source_range))
          if i != None:
            new_ranges += Range(min(i).start+lm.diff,min(i).end+lm.diff)
            print('Intersection', r, 'lm', lm, 'i', i, 'd', d, 'new_ranges', new_ranges)
            r = d
      if r != None:
        new_ranges += r
        print('Unchanged', r, 'lm', lm, 'i', i, 'd', d, 'new_ranges', new_ranges)
    seed_ranges = new_ranges
  print(map_types,file=debug)
  return min(seed_ranges).start

# try solution on file(s)
test_solution(solve, 'test.input', 46)
test_solution(solve, 'my.input')
