from InitBiasVectors import InitBiasVectors
from InitWeightMatrices import InitWeightMatrices

def InitNetwork(nn_shape):
    return [InitWeightMatrices(nn_shape), InitBiasVectors(nn_shape)]


