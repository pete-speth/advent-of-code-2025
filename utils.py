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


def find_neighbors(row, col, n_rows, n_cols):
   l = []
   for r in range(row - 1, row + 2):
      for c in range(col - 1, col + 2):
         if r >= 0 and r < n_rows and c >= 0 and c < n_cols and not (r == row and c == col):
            l.append((r,c))
   return l


