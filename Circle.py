from Times import Times
from math import pi, sin, cos
from Rho import Shape, Reshape
from Tally import Tally
from helpers import verify_args

def PiTimes(vector):
    vector = verify_args(vector, n_args = 1)
    return Times([pi], vector)

def Circular(selector, vector):
   
    selector, vector = verify_args(selector, vector, n_args = 2)
    # implementing only sin and cos for now
    functions = [sin, cos]
    # Selector must be composed by integers between 1 and 2 (included)
    reshaped_selector = Reshape([Tally(selector)], selector)
    if not all(map(lambda x: x in [1, 2], reshaped_selector)):
        raise ValueError("Selector must be composed by integers between 1 and 2 (included)")
    return Reshape(Shape(vector), map(lambda s, a: functions[s-1](a), reshaped_selector, Reshape([Tally(vector)], vector)))

