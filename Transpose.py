from helpers import verify_args
import numpy as np
def Transpose(vector):
    vector = verify_args(vector, n_args = 1)
    np.array(vector) 
    return np.transpose(vector).tolist()
