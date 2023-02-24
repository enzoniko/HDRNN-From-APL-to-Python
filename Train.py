from ForwardPass import ForwardPass
from Each import Each
from InitNetwork import InitNetwork
from Reverse import Reverse
from Drop import Drop
from Catenate import Catenate
from Times import Times
from Product import InnerProduct
from Plus import Plus
from Minus import Minus
from Transpose import Transpose

def Train(target, net, derivatives, inp):
    ws, bs = net
    actFn, lossFn = derivatives
    xs = ForwardPass(actFn, net, inp)
    dbs, dws = [], []
    dx = lossFn.DLoss(target, xs[-1])
    for w, b, x in zip(*Each(Reverse, [ws, bs, Drop(-1, xs)])):
        dbs = Catenate(dbs, [Times(dx, actFn.DF(Plus(b, InnerProduct(w, Plus, Times, x))))])
        dx = InnerProduct(Transpose(w), Plus, Times, dbs[-1])
        dws = Catenate(dws, [InnerProduct(dbs[-1], Plus, Times, Transpose(x))])
    return [Minus(ws, Times(0.01, Reverse(dws))), Minus(bs, Times(0.01, Reverse(dbs)))]
