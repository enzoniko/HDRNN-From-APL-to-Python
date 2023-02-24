from Rho import Shape, Reshape
from Tally import Tally
from helpers import verify_args, handle_non_homogeneous_cube

def Direction(vector):
    if len(Shape(vector)) == 2 and Shape(vector)[-1] == 1:
        vector = Reshape(Shape(vector)[:-1], vector)
    if len(Shape(vector)) != 1:
        print(Shape(vector))
        print(vector)
        raise TypeError("Direction() only accepts a numeric vector.")
    result = []
    for x in vector:
        if x == 0:
            result.append(0)
        elif x > 0:
            result.append(1)
        else:
            result.append(-1)
    return result
    
def Times(vector1, vector2):
    vector1, vector2 = verify_args(vector1, vector2, n_args = 2)
    result = handle_non_homogeneous_cube(vector1, vector2, Times)
    if result is not None:
        return result
    return Reshape(Shape(vector1), map(lambda x, y: x * y, Reshape([Tally(vector1)], vector1),  Reshape([Tally(vector2)], vector2)))
