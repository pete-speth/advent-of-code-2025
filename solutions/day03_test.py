
from solutions.day03 import max_joltage


def test_max_joltage():
    test_cases = [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92)
    ]

    for t in test_cases:
        assert max_joltage(t[0]) == t[1]


def test_max_joltage_12_batteries():
    test_cases = [
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111)
    ]

    for t in test_cases:
        assert max_joltage(t[0], n_batteries=12) == t[1]

