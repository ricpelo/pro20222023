from math import gcd

while True:
    try:
        a = int(input('Introduzca el primer número: '))
        b = int(input('Introduzca el segundo número: '))
        if 0 in (a, b):
            print('No puede haber ningún cero.')
        else:
            break
    except ValueError:
        print('El dato introducido no es correcto.')

"""
def mcd(a, b):
    resto = a % b
    if resto == 0:
        return b
    return mcd(b, resto)
"""

def mcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

res = mcd(a, b)
print('El máximo común divisor es', res)
