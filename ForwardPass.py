from F import F
from PowerOperator import PowerOperator

def ForwardPass(activation_f, network, inp):
    network = network.copy()
    ws, bs = network
    _, _, xs = PowerOperator(activation_f, F, len(ws), (ws, bs, [inp]))
    return xs

