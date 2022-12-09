from math import sqrt

def diferencia_diagonales(matriz: dict) -> int:
    """
    Esta función recibe una matriz cuadrada (mismo número de
    filas que de columnas) y devuelve la diferencia (en valor
    absoluto) de las sumas de sus diagonales.
    """
    n = int(sqrt(len(matriz)))

    suma_principal = 0
    for i in range(n):
        suma_principal += matriz[(i,i)]

    # suma_principal = sum(matriz[(i,i)] for i in range(n))

    suma_secundaria = 0
    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                suma_secundaria += matriz[(i,j)]

    # suma_secundaria = sum(matriz[(i,j)] for i in range(n)
    #                                     for j in range(n)
    #                                     if i + j == n -1)

    return abs(suma_principal - suma_secundaria)

m1 = {(0,0): 11, (0,1): 2, (0,2): 4,
      (1,0):  4, (1,1): 5, (1,2): 6,
      (2,0): 10, (2,1): 8, (2,2): -12}

m2 = {(0,0): 11, (0,1): 2, (0,2): 9,
      (1,0):  4, (1,1): 5, (1,2): 6,
      (2,0): 10, (2,1): 8, (2,2): -12}

assert diferencia_diagonales(m1) == 15
assert diferencia_diagonales(m2) == 20
