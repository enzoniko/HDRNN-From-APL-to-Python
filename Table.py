from Rho import Shape, Reshape
from Tally import Tally

def Table(vector):
    shape = Shape(vector)
    first_dimension = shape[0]
    if len(shape) == 1:
        return Reshape([first_dimension, 1], vector)
    else:
        return Reshape([first_dimension, Tally(shape[1:], is_a_shape=True)], vector)
