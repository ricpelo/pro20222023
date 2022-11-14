"""
suma_digitos = lambda n: abs(n) if abs(n) < 10 else \
                         (abs(n) % 10) + suma_digitos(abs(n) // 10)
"""

suma_digitos = lambda n: suma_aux(abs(n))
suma_aux = lambda n: n if n < 10 else \
                     (n % 10) + suma_aux(n // 10)

insertar = lambda t, e, p: (e,) if t == () else \
                           (e,) + t if p == 0 else \
        (t[0],) + insertar(t[1:], e, p - 1)

rota = lambda n, t: () if t == () else \
                    t if n == 0 else \
        insertar(rota(n - 1, t[1:]), t[0], len(t) - n)

rota_iter = lambda n, t: t if n == 0 else \
                         rota_iter(n - 1, t[1:] + (t[0],))

rota1 = lambda t: rota(1, t)

concatenar = lambda t1, t2: t2 if t1 == () else \
                            t1 + t2 if len(t1) == 1 else \
        (t1[0],) + concatenar(t1[1:], t2)

menor_mayor = lambda t: menor_aux(t, t[0], t[0])
menor_aux = lambda t, me, ma: (me, ma) if t == () else \
        menor_aux(t[1:], min(t[0], me), max(t[0], ma))
