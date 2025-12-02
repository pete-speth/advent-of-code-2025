from collections import deque


def solution(parser):
    def decorator(f):
        def inner(**kwargs):
            assert 'input_file' in kwargs
            with open(kwargs['input_file']) as fp:
                s = fp.read()
                parsed_input = parser(s)
                if type(parsed_input) is tuple:
                    return f(*parsed_input)
                else:
                    return f(parsed_input)
        return inner
    return decorator
