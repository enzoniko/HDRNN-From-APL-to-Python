from math import ceil
from Rho import Shape, Reshape
from helpers import verify_args

def Ceiling(vector):
    """Returns a list of the ceiling of each element in the numeric vector."""
    vector = verify_args(vector)
    if len(Shape(vector)) != 1:
        raise TypeError("Ceiling() only accepts a numeric vector.")
    return [ceil(x) for x in vector]

def Maximum(vector1, vector2):
    """Returns a list of the maximum of each element in the numeric vectors."""
    vector1, vector2 = verify_args(vector1, vector2, n_args = 2)
    
    return Reshape(Shape(vector1), [max(x, y) for x, y in zip(Reshape(Shape(vector1), vector1), Reshape(Shape(vector2), vector2))])

