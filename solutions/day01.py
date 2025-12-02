from utils import solution

 
def parse_op(s: str):
   n = int(s[1:])
   if s[0] == "L":
      n = -n
   return n


def parse_fn(s: str):
   return [parse_op(line) for line in s.split('\n')]


@solution(parser=parse_fn)
def solve(moves):
   position = 50
   zeros = 0
   cross_zero = 0
   for move in moves:
      abs_position = position + move

      # how many times did it cross 0?
      if abs_position <= 0:
         if position > 0:
            cross_zero += 1
         
         # add crossings for additional rotations
         cross_zero += -abs_position // 100
      
      if abs_position > 99:
         cross_zero += abs_position // 100

      # did it land on 0?
      position = abs_position % 100
      if position == 0:
         zeros += 1

   
   print(zeros)
   print(cross_zero)




