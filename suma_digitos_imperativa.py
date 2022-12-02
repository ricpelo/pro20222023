"""
suma_digitos = lambda n(abs(n))
suma_aux = lambda n: n if n < 10 else \
                     (n % 10) + suma_aux(n // 10)
"""

"""
def suma_digitos(n):
    def aux(n):
        if n < 10:
            return n
        return (n % 10) + aux(n // 10)
    return aux(abs(n))
"""

def suma_digitos(n):
    def aux(n):
        suma = 0
        while n > 0:
            suma += n % 10
            n //= 10
        return suma
    return aux(abs(n))
