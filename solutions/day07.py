from typing import Set
from utils import solution

 
def parse_fn(s: str):
   lines = s.split("\n")
   beam = lines[0].find("S")

   splitter_levels = []
   for l in lines[1:]:
      splitter_levels.append(set([i for i, c in enumerate(l) if c == '^']))

   return beam, [l for l in splitter_levels if len(l) > 0]



@solution(parser=parse_fn)
def solve(beam, splitter_levels):
   
   # part 1 - simulate beam splitting
   split_count = 0
   beams = set([beam])
   for splitters in splitter_levels:
      splits_at = beams & splitters
      split_count += len(splits_at)
      
      for i in splits_at:
         beams.remove(i)
         beams.add(i - 1)
         beams.add(i + 1)
   
   print(split_count)

   # part 2
   # recursively split the beam and count the number of paths

   memo = {}
   def iter(beam: int, level: int = 0):
      # find the next level where this beam will be split
      while level < len(splitter_levels) and beam not in splitter_levels[level]:
         level += 1

      # beam will not be split any more
      if level == len(splitter_levels):
         return 1
      
      # check if we have a stored solution
      if (beam, level) in memo:
         return memo[(beam, level)]

      paths = iter(beam - 1, level) + iter(beam + 1, level)
      memo[(beam, level)] = paths
      return paths

   print(iter(beam))





