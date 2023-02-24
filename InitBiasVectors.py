from Drop import Drop
from Each import Each
from Bind import Bind
from MakeNormalArray import MakeNormalArray
from Table import Table
from Divide import Divide
from Power import Power

def InitBiasVectors(nn_shape):
    shape = Drop(1, nn_shape)
    normalArray = Each(Bind(MakeNormalArray, Table), shape)
    return Divide(normalArray, Power(shape, 0.5))
