from random import random, randint
from Rho import Shape, Reshape
from Tally import Tally
from helpers import verify_args
def Roll(vector):
    vector = verify_args(vector)
    # For every element in the flattened vector.
    # If the element is 0, get a random number between 0 and 1
    # If the element is not 0, get a random integer between 0 and the element - 1
    # Reshape the randomized flattened vector to the shape of the original vector and return it.
    return Reshape(Shape(vector), [random() if element == 0 else randint(0, element - 1) for element in Reshape([Tally(vector)], vector)])
