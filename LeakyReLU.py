from Times import Times, Direction
from Upstile import Maximum

alpha = 0.01

def F(vector):
    return Maximum(vector, Times(alpha, vector))

def DF(vector):
    return Maximum(alpha, Direction(vector))

