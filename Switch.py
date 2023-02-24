def Switch(f):
    def g(left, right):
        return f(right, left)
    return g
