from dataclasses import dataclass
from functools import reduce
from utils import solution

 
def parse_fn(s: str):
   return s.split("\n")


@dataclass
class Problem:
   offset: int
   width: int
   operation: str


def solve_problem(p: Problem, lines: list[str]):
   ns = []
   for c in range(p.offset, p.offset + p.width):
      s = ''.join([line[c] for line in lines[:-1]])
      ns.append(int(s))
   
   if p.operation == "*":
         reduce_fn = lambda a, b: a * b
         initial = 1
   else:
      reduce_fn = lambda a, b: a + b
      initial = 0

   return reduce(reduce_fn, ns, initial)


@solution(parser=parse_fn)
def solve(lines):

   # part 1
   numbers = [[int(s) for s in line.split()] for line in lines[:-1]]
   ops = lines[-1].split()
   solution_sum = 0
   for col in range(len(ops)):
      if ops[col] == "*":
         reduce_fn = lambda a, b: a * b
         initial = 1
      else:
         reduce_fn = lambda a, b: a + b
         initial = 0

      solution_sum += reduce(reduce_fn, [row[col] for row in numbers], initial)
   
   print(solution_sum)

   # part 2
   
   # parse problems from the input
   problems = []
   offset = 0
   op = lines[-1][0]
   
   i = 1
   while i < len(lines[-1]):
      if lines[-1][i] != " ":
         width = i - offset - 1
         problems.append(Problem(offset, width, op))

         op = lines[-1][i]
         offset = i
      i += 1
   
   # add the final column after loop completes
   width = i - offset
   problems.append(Problem(offset, width, op))

   # solve problems and report sum
   print(sum([solve_problem(p, lines) for p in problems]))







