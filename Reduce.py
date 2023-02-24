from helpers import verify_args
from ReduceFirst import ReduceFirst

def Reduce(f, vector, n_wise = None):
    vector = verify_args(vector)
    result = []
    if len(vector) == 1:
        return vector[0]
    for element in vector:
        if isinstance(element, list) and isinstance(element[0], (int, float)):
            new = ReduceFirst(f, element, n_wise)
            a = []
            if all(isinstance(x, (int, float)) for x in new):
                result.extend(new)
            elif all(isinstance(x, list) for x in new):
                for element in new:
                    a.extend(element)
                result.append(a)
        else:
            result.append(Reduce(f, element, n_wise))
    return result
