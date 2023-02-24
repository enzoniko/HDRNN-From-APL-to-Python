from Rho import Shape, Reshape, homogeneous
import numpy as np
from Tally import Tally
def verify_args(*args, **kwargs):
    args = list(args)
    n_args = kwargs.get("n_args", 1)
    enlarge_to_match = kwargs.get("enlarge_to_match", True)
    if n_args != len(args):
        raise ValueError("Not enough arguments were given.")
    if n_args == 1:
        return [args[0]] if isinstance(args[0], (int, float)) else args[0]
    elif n_args == 2:

        args[0] = [args[0]] if isinstance(args[0], (int, float)) else args[0]
        args[1] = [args[1]] if isinstance(args[1], (int, float)) else args[1]
        if not homogeneous(args[0]) or not homogeneous(args[1]) and all(homogeneous(element) for element in args[0]) and all(homogeneous(element) for element in args[1]) and Shape(args[0])[0] == Shape(args[1])[0]:
            return args[0], args[1]
        if enlarge_to_match:
            args[0] = Reshape(Shape(args[1]), args[0]) if Shape(args[0]) == [1] else args[0]
            args[1] = Reshape(Shape(args[0]), args[1]) if Shape(args[1]) == [1] else args[1]
        
            if Shape(args[0]) != Shape(args[1]) and Tally(args[0]) != Tally(args[1]):
                raise ValueError("The arguments are not the same shape.")
        return args[0], args[1]

def Print(vector, is_a_shape=False):
    if homogeneous(vector):
        print(np.array(vector))
    elif not is_a_shape:
        print("--------------------------------")
        print()
        for element in vector:
            Print(element)
        print("________________________________")
    else:
        print(vector)
    print()

def handle_non_homogeneous_cube(left_vector, right_vector, f):
    if not homogeneous(left_vector) or not homogeneous(right_vector) and all(homogeneous(element) for element in left_vector) and all(homogeneous(element) for element in right_vector) and Shape(left_vector)[0] == Shape(right_vector)[0]:
        return list(map(lambda x, y: f(x, y), left_vector, right_vector))
    return None

def gen_chunks(reader, chunksize=100):
    """ 
    Chunk generator. Take a CSV `reader` and yield
    `chunksize` sized slices. 
    """
    chunk = []
    for i, line in enumerate(reader):
        if (i % chunksize == 0 and i > 0):
            yield chunk
            del chunk[:]  # or: chunk = []
        chunk.append(line)
    yield chunk
