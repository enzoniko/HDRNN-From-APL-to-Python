def Drop(drop_amount, vector):
    if drop_amount < 0:
        return vector[:drop_amount] if isinstance(vector, list) else vector
    return vector[drop_amount:] if isinstance(vector, list) else vector

