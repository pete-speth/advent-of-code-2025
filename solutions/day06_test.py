from solutions.day06 import Problem, solve_problem


lines = [
    '123 328  51 64 ',
    ' 45 64  387 23 ', 
    '  6 98  215 314',
    '*   +   *   +  ',
]

def test_solve_problem():
    testcases = [
        (Problem(0, 3, '*'), 8544),
        (Problem(4, 3, '+'), 625)
    ]

    for tc in testcases:
        assert solve_problem(tc[0], lines) == tc[1]