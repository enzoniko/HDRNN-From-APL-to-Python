from functools import partial

def PowerOperator(left_argument, f, n, right_argument):
    if n == 0:
        return right_argument
    if left_argument is not None:
        f = partial(f, left_argument)
    return f(PowerOperator(None, f, n - 1, right_argument))
