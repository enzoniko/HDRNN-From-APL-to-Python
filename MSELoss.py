from Divide import Divide
from Minus import Minus
from Plus import Plus
from Power import Power
from ReduceFirst import ReduceFirst
from Switch import Switch
from Times import Times

def Loss(target, output):
    square = Switch(Power)(2, Minus(target, output))
    return ReduceFirst(Plus, Divide(square, len(output)))[0]

def DLoss(target, output):
    return Switch(Divide)(len(output), Times(2, Minus(output, target)))
