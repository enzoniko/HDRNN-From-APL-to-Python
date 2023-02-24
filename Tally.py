from Rho import Shape, shape_product

def Tally(vector, is_a_shape = False) -> int:

    return sum(shape_product(vector)) if is_a_shape else sum(shape_product(Shape(vector)))
# TALLY IN APL IS LITERALLY JUST LEN, SO THIS WILL BE MY TALLY, IT MULTIPLIES THE ELEMENTS OF THE SHAPE TOGETHER
