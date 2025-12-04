from utils import solution

 
def parse_fn(s: str):
   return [map(int, range_str.split("-")) for range_str in s.split(',')]


def next_invalid(n):
   s = str(n)
   
   # must have an even number of digits
   l = len(s)
   if l % 2 != 0:
      return next_invalid(int("1" + "0" * l))
   
   first_half = str(s[:l//2])
   second_half = str(s[l//2:])
   
   # if first half is not larger than the second half, add 1 to it
   if first_half <= second_half:
      first_half = str(int(first_half) + 1)

   # return the first half repeated
   return int(first_half + first_half)


def next_invalid_multiple_repeat(n):
   def next_invalid_with(n_segments):
      s = str(n)

      if len(s) % n_segments != 0:
         return None
      
      seg_size = len(s) // n_segments
      if seg_size < 1:
         return None

      # find the first segment that differs, or use the last segment
      seg1 = s[:seg_size]
      seg_number = 2
      comparison_seg = s[seg_size * (seg_number - 1): seg_size * seg_number]
      while seg_number < n_segments and seg1 == comparison_seg:
         seg_number += 1
         comparison_seg = s[seg_size * (seg_number - 1): seg_size * seg_number]

      # if seg1 is not greater than the comparison segment
      # we need to add 1 to it
      if seg1 <= comparison_seg:
         seg1 = str(int(seg1) + 1)
         if len(seg1) > len(comparison_seg):
            # seg1 added a digit, no solution
            return None
      
      return int(seg1 * n_segments)
   

   # get values for all possible number of repeating segments (up to the number of digits)
   num_digits = len(str(n))
   invalids = []
   for i in range(2, num_digits + 1):
      invalid = next_invalid_with(n_segments=i)
      if invalid is not None:
         invalids.append(invalid)
   
   # if there were no solutions, try again with an additional digit
   if len(invalids) == 0:
      return next_invalid_multiple_repeat(int("1" + "0" * num_digits))

   # otherwise, return the minimum invalid value
   return min(invalids)
   

@solution(parser=parse_fn)
def solve(ranges):
   sum = 0
   sum2 = 0

   for start, stop in ranges:
      # part 1
      n = next_invalid(start - 1)
      while n <= stop:
         sum += n
         n = next_invalid(n)

      # part 2
      n = next_invalid_multiple_repeat(start - 1)
      while n <= stop:
         sum2 += n
         n = next_invalid_multiple_repeat(n)
   
   print(sum)
   print(sum2)





