from helpers import verify_args

def ReduceFirst(f, vector, n_wise = None):
    vector = verify_args(vector)

    if len(vector) == 1:
        return vector[0]

    if n_wise is None:
        partial = f(vector[0], vector[1])
        for i in range(2, len(vector)):
            partial = f(partial, vector[i])
        return partial
    vector = [vector[i:i+ n_wise] for i in range(len(vector) - n_wise + 1)]
    return [ReduceFirst(f, v) for v in vector]

