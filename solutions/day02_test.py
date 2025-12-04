from solutions.day02 import next_invalid, next_invalid_multiple_repeat

next_invalid_test_cases = [
   (8, 11),
   (11, 22),
   (12, 22),
   (98, 99),
   (100, 1010),
   (12341111, 12341234)
]

def test_next_invalid():
   for t in next_invalid_test_cases:
      assert next_invalid(t[0]) == t[1]

multiple_repeat_test_cases =[
   (8, 11),
   (11, 22),
   (12, 22),
   (98, 99),
   (99, 111),
   (100, 111),
   (112, 222),
   (221, 222),
   (777, 888),
   (778, 888),
   (998, 999),
   (1000, 1010),
   (100000, 100100),
   (100055, 100100),
   (100999, 101010),
   (101011, 101101),
   (222221, 222222),
   (564534, 564564),
   (564565, 565565),
   (565566, 565656),
   (123123124, 124124124),
   (12345678, 12351235),
   (789000000,789789789)
]

def test_next_invalid_multiple_repeat():
   for t in multiple_repeat_test_cases:
      assert next_invalid_multiple_repeat(t[0]) == t[1]