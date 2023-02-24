from helpers import verify_args

def Each(f, vector):
    
    vector = verify_args(vector)
    return list(map(f, vector))
    