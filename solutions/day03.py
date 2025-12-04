from utils import solution

 
def parse_fn(s: str):
   return s.split('\n')


def max_with_index(s: str):
   m = "0"
   i_m = 0
   for i in range(len(s)):
      if s[i] > m:
         m = s[i]
         i_m = i
   return int(m), i_m


def max_joltage(battery_bank: str, n_batteries: int = 2):
   reserved = n_batteries - 1
   available = battery_bank[:len(battery_bank) - reserved]
   digit, i_digit = max_with_index(available)

   if n_batteries == 1:
      return digit
   else:
      following_digits = max_joltage(battery_bank[i_digit + 1:], n_batteries - 1)
      return int(str(digit) + str(following_digits))


@solution(parser=parse_fn)
def solve(battery_banks):
   print(sum([max_joltage(bb) for bb in battery_banks]))
   print(sum([max_joltage(bb, n_batteries=12) for bb in battery_banks]))




