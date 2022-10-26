"""
suma_digitos = lambda n: abs(n) if abs(n) < 10 else \
                         (abs(n) % 10) + suma_digitos(abs(n) // 10)
"""

suma_digitos = lambda n: suma_aux(abs(n))

suma_aux = lambda n: n if n < 10 else \
                     (n % 10) + suma_aux(n // 10)
