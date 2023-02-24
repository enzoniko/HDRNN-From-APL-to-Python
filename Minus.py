from Rho import Reshape, Shape
from Tally import Tally
from helpers import handle_non_homogeneous_cube, verify_args

def Minus(left_vector, right_vector):
    left_vector, right_vector = verify_args(left_vector, right_vector, n_args = 2)
    result = handle_non_homogeneous_cube(left_vector, right_vector, Minus)
    if result is not None:
        return result
    return Reshape(Shape(left_vector), map(lambda x, y: x - y, Reshape([Tally(left_vector)], left_vector),  Reshape([Tally(right_vector)], right_vector)))

