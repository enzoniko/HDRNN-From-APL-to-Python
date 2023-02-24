from functools import reduce
import numpy as np

def homogeneous(vector) -> bool:
    if isinstance(vector, (int, float)):
        return True
    try:
        np.array(vector)
        return True
    except ValueError as e:
        if "homogeneous" in str(e):
            return False
        else:
            raise e

def Func0(vector) -> list[int]:
    return (
        [len(vector), list(map(Func0, vector))]
        if len(vector) > 0 and isinstance(vector[0], list)
        else [len(vector)]
    )
   
    
def Func1(vector):
    # Turns the ugly shape into a nice one pratically final one
    result = []
    for element in vector: 
        if isinstance(element, list) and all(isinstance(sub_element, (int, float)) for sub_element in element):
            result.append(element[0])
        elif isinstance(element, (int, float)):
            result.append(element)
        else:
            result.append(Func1(element))
    return result

def Func2(vector):
    # Turns the nice shape into a final one 
    if isinstance(vector, (int, float)):
        return vector
    if len(vector) == 1:
        return vector
    elif len(vector) > 1:
        if vector[1].count(vector[1][0]) == vector[0]:
            vector[1] = Func2(vector[1][0])
        else:
            vector[1] = list(map(Func2, vector[1]))

        return vector

def Func3(vector, is_homogenous):
    # Fixes the homogenous vectors
    if isinstance(vector, int) or len(vector) == 1:
        return vector
    if len(vector) > 1:
        result = vector
        if is_homogenous:
            result = [vector[0]]
            for i in range(1, len(vector)):
                if isinstance(vector[i], list):
                    result.extend(Func3(vector[i], True))
                elif isinstance(vector[i], int):
                    result.append(vector[i])
        return result

def flatten(vector) -> list[int]:
    flattened = []
    
    for element in vector:
        if isinstance(element, (int, float)):
            flattened.append(element)
        else:
            flattened.extend(flatten(element))
    return flattened

def shape_product(shape):
    
    products = []
    if isinstance(shape, int):
        pass
    elif all(isinstance(element, int) for element in shape):
        products.append(reduce(lambda x, y: x*y, shape))
    elif isinstance(shape[0], int) and isinstance(shape[1], list) and all(isinstance(element, int) for element in shape[1]):
        products.append(reduce(lambda x, y: x + y, shape[1]))
    else:
        shape = shape.copy()
        if isinstance(shape[0], int) and isinstance(shape[1], list) and not all(isinstance(element, int) for element in shape[1]):
            
            if isinstance(shape[1][0], int) and isinstance(shape[1][1], list):
                shape[1] = [shape[1]]
            if len(shape[1]) != shape[0]:
                shape[1] = shape[1]*shape[0]
        for element in shape:
            products.extend(shape_product(element))
        
    return products

def Shape(vector):

    if not homogeneous(vector):
        return Func3(Func2(Func1(Func0(vector))), homogeneous(vector))
    else:
        return list(np.array(vector).shape)

def Reshape(shape, vector):
    product = sum(shape_product(shape))
    vector = flatten(vector)
    s = shape.copy()
    s.reverse()
    if Shape(vector) == [1]:
        vector = vector*product
    if len(vector) != product:
        raise ValueError("The number of elements in the vector must match the product of the shape dimensions.")
    if all(isinstance(element, int) for element in shape):
        for num in s[:-1]:
            vector = [vector[i:i+num] for i in range(0, len(vector), num)]
    elif not all(isinstance(element, int) for element in shape):
        vector = especial_reshape(shape, vector)
    return vector

def especial_reshape(shape, vector):
    if not all(isinstance(element, int) for element in shape):
        if isinstance(shape[0], int) and isinstance(shape[1], list):
            if all((isinstance(element, int) for element in shape[1])):
                new_vector = []
                new_vector.extend(
                    vector[
                        sum(shape_product(Shape(new_vector))) : sum(shape_product(Shape(new_vector))) + num
                    ]
                    for num in shape[1]
                )
                return new_vector
            elif all((isinstance(element, list) for element in shape[1])):
                return recursive_part(shape, especial_reshape, vector)
            elif isinstance(shape[1][0], int) and isinstance(shape[1][1], list):
                shape = shape.copy()
                shape[1] = [shape[1]]
                if len(shape[1]) != shape[0]:
                    shape[1] *= shape[0]
                return recursive_part(shape, especial_reshape, vector)
    elif all(isinstance(element, int) for element in shape):
        return Reshape(shape, vector)


def recursive_part(shape, especial_reshape, vector):
    new_vector = []
    new_vector.extend(
        especial_reshape(
            element,
            vector[
                sum(shape_product(Shape(new_vector))) : sum(shape_product(Shape(new_vector))) + sum(shape_product(element))
            ],
        )
        for element in shape[1]
    )
    return new_vector
    