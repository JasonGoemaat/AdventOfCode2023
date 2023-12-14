# need to be sure about parsing
# The first line is a list of seeds:
#     seeds: 79 14 55 13
# Following that are several 'maps' with multiple lines
#     seed-to-soil map:
#     50 98 2
#     52 50 48
# And empty lines between maps
# The mapping lines are (destination start) (source start) (length)
# So for example '50 98 2' on seed-to-soil converts seed values 98-99
# to soil values 50-51.   The second example '52 50 48' maps seed values 50-97
# to soil values 52-99. Values that aren't in a map are left unchanged.
# So for our example seeds, they would be mapped like this:
# 79 -> 81 (in 50-97, so map to 81 (add 2, the diference between dest and src))
# 14 -> 14 (not in ranges, so leave unchanged)
# 55 -> 57 (in 50-97, so map to 57 (add 2, the difference between dest and src))
# 13 -> 13 (not in ranges, so leave unchanged)

# These all appear to be in order, so we can have an array of mappings and
# process each one.   What we need is the source span and a value to indicate
# how much to add to the source number.  The '52 50 48' for example
# would be 50, 99, 2 (take from 50-98 not including 99 and add 2).  I'm using
# 99 here which is 1 past the actual last number because that seems to be how
# python handles ranges

import sys, os, re, bisect
sys.path.insert(0, os.getcwd() + '/..')
from util import test_solution

nums_re = re.compile(r"(\d+)")

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
