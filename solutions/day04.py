from dataclasses import Field, dataclass, field
from utils import find_neighbors, solution


def parse_fn(s: str):
   rows = []
   for line in s.split("\n"):
       rows.append([True if c == "@" else False for c in line])

   return rows


@dataclass
class Roll:
   row: int
   col: int
   neighbors: list['Roll'] = field(default_factory=list)
   removed: bool = False

@solution(parser=parse_fn)
def solve(grid):
   rolls = {}
   for r in range(len(grid)):
      for c in range(len(grid[r])):
         if grid[r][c]:
            rolls[(r,c)] = Roll(r, c)
   
   for roll in rolls.values():
      neighbor_spots = find_neighbors(roll.row, roll.col, len(grid), len(grid[0]))
      for r, c in neighbor_spots:
         neighbor = rolls.get((r, c))
         if neighbor:
            roll.neighbors.append(neighbor)
   
   # how many rolls are initially removable
   removable = [roll for roll in rolls.values() if len(roll.neighbors) < 4]
   print(len(removable))

   # remove all the rolls we can
   total_removed = 0
   while len(removable) > 0:
      for roll in removable:
         roll.removed = True
      total_removed += len(removable)

      remaining = [r for r in rolls.values() if not r.removed]
      removable = [roll for roll in remaining if len([n for n in roll.neighbors if not n.removed]) < 4]
   
   print(total_removed)

      





