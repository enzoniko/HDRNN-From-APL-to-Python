from helpers import verify_args

def Catenate(left_vector, right_vector):
    left_vector, right_vector = verify_args(left_vector, right_vector, n_args = 2, enlarge_to_match = False)
    left_vector.extend(right_vector)
    return left_vector
    # # Not implementing the case where one of the vectors is a scalar