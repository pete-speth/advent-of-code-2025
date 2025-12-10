from utils import solution

 
def parse_fn(s: str):
   ranges_raw, ingredients_raw = s.split('\n\n')

   ranges = [[int(s) for s in line.split("-")] for line in ranges_raw.split("\n")]
   ingredients = [int(line) for line in ingredients_raw.split("\n")]

   return (ranges, ingredients)


def combine_ranges(r1, r2):
   start1, end1 = r1
   start2, end2 = r2

   if end1 < start2:
      return None
   if end2 < start1:
      return None
   
   return (min(start1, start2), max(end1, end2))


def consolidate_range_list(ranges: list[(int, int)]):
   consolidated = []
   included = set()
   
   i = 0
   while i < len(ranges):
      if i not in included:
         this_range = ranges[i]
         j = i + 1
         while j < len(ranges):
            if j not in included:
               combined = combine_ranges(this_range, ranges[j])
               if combined:
                  this_range = combined
                  included.add(j)
            j += 1
      
         consolidated.append(this_range)
      i += 1
   
   if len(consolidated) == len(ranges):
      return consolidated
   else:
      return consolidate_range_list(consolidated)



@solution(parser=parse_fn)
def solve(fresh_ranges, ingredients):
   # consolidate ranges
   consolidated_ranges = consolidate_range_list(fresh_ranges)

   
   # for each ingredient, check if it's in a fresh range
   fresh_count = 0
   for ing in ingredients:
      for r in consolidated_ranges:
         start, end = r
         if ing >= start and ing <= end:
            fresh_count += 1
            break
   print(fresh_count)

   # get the combined size of consolidated ranges
   total_fresh = 0
   for r in consolidated_ranges:
      total_fresh += r[1] - r[0] + 1
   print(total_fresh)





