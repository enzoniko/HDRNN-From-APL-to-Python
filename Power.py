from Rho import Shape, Reshape
from Tally import Tally
from helpers import verify_args, handle_non_homogeneous_cube

def Power(left_arg, right_arg):
    
    vector, power_vector = verify_args(left_arg, right_arg, n_args = 2)
    result = handle_non_homogeneous_cube(vector, power_vector, Power)
    if result is not None:
        return result
    return Reshape(Shape(vector), map(lambda x, y: x ** y, Reshape([Tally(vector)], vector), Reshape([Tally(power_vector)], power_vector)))
