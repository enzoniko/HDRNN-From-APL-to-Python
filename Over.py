from helpers import verify_args

def Over(left_argument, left_function, right_function, right_argument):
    left_argument = right_function(verify_args(left_argument))
    right_argument = right_function(verify_args(right_argument))
    return left_function(left_argument, right_argument)

