from Roll import Roll
from Rho import Reshape
from Log import Log
from Times import Times
from Power import Power
from Circle import Circular, PiTimes
from helpers import verify_args

def MakeNormalArray(shape):
    shape = verify_args(shape)
    u1 = Roll(Reshape(shape, [0])) 
    u2 = Roll(Reshape(shape, [0])) 
 
    r = Power(Times(-2, Log(u1)), 0.5)
    s = Circular(2, Times(2, PiTimes(u2)))
    return Times(r, s)

