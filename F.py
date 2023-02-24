from Pick import Pick
from Plus import Plus
from Product import InnerProduct
from Times import Times
from Drop import Drop
from Catenate import Catenate

def F(activation_f, components):
    ws, bs, xs = components
    w = Pick(1, ws)
    b = Pick(1, bs)
    inp = xs[-1]
    X = activation_f.F(Plus(b, InnerProduct(w, Plus, Times, inp)))
    return Drop(1, ws), Drop(1, bs), Catenate(xs, [X])
