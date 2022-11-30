"""
Ejercicios de funciones creadas con expresiones lambda.
"""

"""
division_segura = lambda x, y: x / y if y != 0 else 'error'
"""

def division_segura(x, y):
    if y != 0:
        return x / y
    return 'error'

"""
maximo2 = lambda x, y: x if x >= y else y
"""

def maximo2(x, y):
    if x >= y:
        return x
    return y

"""
maximo3 = lambda x, y, z: maximo2(x, maximo2(y, z))
"""

def maximo3(x, y, z):
    return maximo2(x, maximo2(y, z))


"""maximo3 = lambda x, y, z: x if x >= y and x >= z else \
                          y if y >= x and y >= z else \
                          z
"""
