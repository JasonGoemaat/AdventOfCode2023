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
# Looks like iterables might be a good fit for figuring this out, and I'd like
# to learn: https://stackoverflow.com/questions/14099872/concatenating-two-range-function-results
# That page shows how to create one:
# def chain(*iterables):
#     # chain('ABC', 'DEF') --> A B C D E F
#     for it in iterables:
#         for element in it:
#             yield element
# I'm not thinking of the seed locations to be iterable, but for ranges to
# be iterable since they can change.   For an example if we have the range (5,10)
# and apply mappings that will add 20 for 2-6 and add 40 for 7-15, the range
# would then be split into two ranges: (25-26) and (47-50)
# I don't know if more than one seed can be planted in a final location, but
# since we're just returning the lowest location number we could then join
# overlapping ranges also.
# Ranges will be pythonesque, a tuple with start and end, where end is actually
# the element AFTER the start (i.e. (5,11) means elements 5 through 10)

import sys, os, re, bisect
sys.path.insert(0, os.getcwd() + '/..')
from util import test_solution

nums_re = re.compile(r"(\d+)")

def map_ranges(maps, ranges):
  pass

def combine_ranges(ranges):
  pass

def parse_map(line):
  vals = [int(x) for x in nums_re.findall(line)]
  # list is start, end (last num + 1 as python end is after last), change (amount to add to convert if the value is in the range)
  return [vals[1], vals[1] + vals[2], vals[0] - vals[1]]

def parse(lines):
  seeds = [int(x) for x in nums_re.findall(lines[0])]
  maps = []
  current = None
  for i in range(2,len(lines)):
    line = lines[i]
    if (line.endswith(' map:')):
      current = {"name": line[0:(len(line)-5)], 'maps':[]}
      maps.append(current)
      continue
    if len(line) > 0:
      current['maps'].append(parse_map(line))
  return (seeds, maps)

def apply_maps(seed, maps):
  for map in maps:
    old = seed
    for m in map["maps"]:
      if seed >= m[0] and seed < m[1]:
        # print('Mapping',seed,'to',seed+m[2],'using',map['name'])
        seed += m[2]
        break
    #print(map['name'],old,'-->',seed)      
  return seed

def output(seeds, maps, debug):
  print('Seeds:', seeds, file=debug)
  for m in maps:
    print('Map', m['name'], file=debug)
    for m2 in m['maps']:
      print('  ',m2[0],'to',m2[1]-1,'add',m2[2],'giving',m2[0]+m2[2],'to',m2[1]-1+m2[2], file=debug)

def solve(lines,debug):
  (seeds, maps) = parse(lines)
  # the actual result requires mapping all seeds, and returning the lowest
  # location number after applying all the maps
  output(seeds, maps, debug)
  locations = [apply_maps(s, maps) for s in seeds]
  print(locations,file=debug)
  return min(locations)

# try solution on file(s)
test_solution(solve, 'test.input', 35)
test_solution(solve, 'my.input')
