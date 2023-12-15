# First I activated the venv by running /.venv/scripts/activate
# in this repository using a bash shell.
# then I ran t his to install python-ranges:
#       pip install python-ranges
# Well, that doesn't work in a bash shell apparently, the activate script did nothing.
# Using powershell and the activate.ps1 did seem to work.
from ranges import RangeSet, Range

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

def test1():
  seed_ranges = RangeSet(Range(79,79+14),Range(55,55+13))
  print(seed_ranges)
  # very nice, uses brackets[] for inclusive and parens() for exclusive:
  # {[55, 68), [79, 93)}

def get_location_maps():
  a = [LocationMap([50,98,2]),LocationMap([52,50,48])]
  b = [LocationMap([0,15,37]),LocationMap([37,52,2]),LocationMap([39,0,15])]
  c = [LocationMap([49,53,8]),LocationMap([0,11,42]),LocationMap([42,0,7]),LocationMap([57,7,4])]
  d = [LocationMap([88,18,7]),LocationMap([18,25,70])]
  e = [LocationMap([45,77,23]),LocationMap([81,45,19]),LocationMap([68,64,13])]
  f = [LocationMap([0,69,1]),LocationMap([1,0,69])]
  g = [LocationMap([60,56,37]),LocationMap([56,93,4])]
  location_maps = [a,b,c,d,e,f,g]
  return location_maps

def test2():
  location_maps = get_location_maps()
  print(location_maps)

def test3():
  seed_ranges = RangeSet(Range(79,79+14),Range(55,55+13))
  for r in seed_ranges:
    # try to apply each mapping inside this list of LocationMaps
    print('start', r.start, 'end', r.end)
  location_maps = get_location_maps()
  for lms in location_maps:
    new_ranges = RangeSet()
    for r in seed_ranges:
      # try to apply each mapping inside this list of LocationMaps
      for lm in lms:
        if r != None:
          i = r.intersection(lm.source_range)
          d = r.difference(lm.source_range)
          if i != None:
            new_ranges += Range(i.start+lm.diff,i.end+lm.diff)
            print('Intersection', r, 'lm', lm, 'i', i, 'd', d, 'new_ranges', new_ranges)
            r = d
      if r != None:
        new_ranges += r
        print('Unchanged', r, 'lm', lm, 'i', i, 'd', d, 'new_ranges', new_ranges)
    seed_ranges = new_ranges

### OMG that works!
### With hard-coding the results, my final range shows the lowest value of 46,
### so the anser is the final value of seed_ranges.start

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4

test3()
