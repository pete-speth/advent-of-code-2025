from solutions.day05 import combine_ranges, consolidate_range_list


def test_combine_ranges():
    testcases = [
        {
            "r1": (1,4),
            "r2": (5,9),
            "expected": None
        },
        {
            "r1": (6,9),
            "r2": (1,4),
            "expected": None
        },
        {
            "r1": (1,4),
            "r2": (4,9),
            "expected": (1,9)
        },
        {
            "r1": (4,9),
            "r2": (1,4),
            "expected": (1,9)
        },
        {
            "r1": (1,4),
            "r2": (2,8),
            "expected": (1,8)
        },
        {
            "r1": (1,4),
            "r2": (2,3),
            "expected": (1,4)
        },
    ]

    for tc in testcases:
        assert combine_ranges(tc["r1"], tc["r2"]) == tc["expected"]

def test_consolidate_range_list():
    actual = consolidate_range_list(
        [(1,3), (2,4), (6,8), (10,15), (12,13), (2,7)]
    )
    print(actual)
    expected = [(1,8), (10,15)]
    assert actual == expected