from Rho import Shape, Reshape
from Tally import Tally
from math import log
from helpers import verify_args

def Log(vector):
    vector = verify_args(vector)
    return Reshape(Shape(vector), map(log, Reshape([Tally(vector)], vector)))
