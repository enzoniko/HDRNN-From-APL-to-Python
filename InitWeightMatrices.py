from Switch import Switch
from Catenate import Catenate
from ReduceFirst import ReduceFirst
from Each import Each
from MakeNormalArray import MakeNormalArray
from Times import Times
from Power import Power
from Divide import Divide

def InitWeightMatrices(nn_shape):
    # HAD TO USE REDUCE FIRST HERE BECAUSE THE NORMAL REDUCE ONLY WORKS IF WE CONSIDER APL'S ESCALARS, WHICH WE DON'T. 
    shapes = ReduceFirst(Switch(Catenate), nn_shape, 2)
    normalMatrices = Each(MakeNormalArray, shapes)
    # ISSO POSSIVELMENTE SÓ FUNCIONA COM LISTA DE MATRIZES 
    return Divide(normalMatrices, Power(ReduceFirst(Times, nn_shape, 2), 0.5))
