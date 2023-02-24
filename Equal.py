from Rho import Shape, Reshape
from Tally import Tally
from helpers import verify_args, handle_non_homogeneous_cube

def Equal(left_vector, right_vector):
    left_vector, right_vector = verify_args(left_vector, right_vector, n_args = 2)
    result = handle_non_homogeneous_cube(left_vector, right_vector, Equal)
    if result is not None:
        return result
    return Reshape(Shape(left_vector), map(lambda x, y: 1 if x == y else 0, Reshape([Tally(left_vector)], left_vector),  Reshape([Tally(right_vector)], right_vector)))
