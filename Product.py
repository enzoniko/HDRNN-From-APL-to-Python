from Rho import Shape, Reshape
from helpers import verify_args
from ReduceFirst import ReduceFirst
from Transpose import Transpose
from Catenate import Catenate

# Not sure if it works for other functions besides Plus and Times
def InnerProduct(left_vector, left_f, right_f, right_vector):
    left_vector = verify_args(left_vector)
    right_vector = verify_args(right_vector)
    if Shape(left_vector) == Shape(right_vector) and len(Shape(left_vector)) == 1:
        r = ReduceFirst(left_f, right_f(left_vector, right_vector))
        return r[0] if isinstance(r, list) else r
    elif len(Shape(left_vector)) == 2 and len(Shape(right_vector)) == 2 and Shape(left_vector)[1] == Shape(right_vector)[0]:
        transposed_right_vector = Transpose(right_vector)
        result = Reshape(Catenate(Shape(left_vector)[0], Shape(right_vector)[1]), [0])
        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i][j] = InnerProduct(left_vector[i], left_f, right_f, transposed_right_vector[j])
        return result
    else:
        raise NotImplementedError("Higher dimensional vectors are not supported yet.")

def OuterProduct(left_vector, right_vector, f):
    left_vector = verify_args(left_vector)
    right_vector = verify_args(right_vector)
    final_shape = Catenate(Shape(left_vector), Shape(right_vector))
    result = Reshape(final_shape, [0])
    for i in range(len(left_vector)):
        for j in range(len(right_vector)):
            result[i][j] = f(left_vector[i], right_vector[j])[0]
    return result
