from helpers import verify_args
from Drop import Drop

def Pick(index, vector):
    vector = verify_args(vector)
    if index is None:
        return Pick(1, vector)
    elif isinstance(index, int) and index <= len(vector) and index > 0:
        return vector[index - 1]
    elif isinstance(index, list) and len(index) == 1:
        return Pick(index[0], vector)
    elif isinstance(index, list) and len(index) > 1:
        return Pick(Drop(1, index), Pick(index[0], vector))
    else:
        raise ValueError("The index is invalid.")
