from Rho import Shape, Reshape
from Tally import Tally
from helpers import verify_args, handle_non_homogeneous_cube

def Plus(left_vector, right_vector):
    left_vector, right_vector = verify_args(left_vector, right_vector, n_args = 2)
    result = handle_non_homogeneous_cube(left_vector, right_vector, Plus)
    if result is not None:
        return result
    return Reshape(Shape(left_vector), map(lambda x, y: x + y, Reshape([Tally(left_vector)], left_vector),  Reshape([Tally(right_vector)], right_vector)))
