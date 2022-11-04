suma_tupla = lambda t: 0 if t == () else t[0] + suma_tupla(t[1:])
longitud = lambda t: 0 if t == () else 1 + longitud(t[1:])
media = lambda t: suma_tupla(t) / longitud(t)
esta_aprobado = lambda t: media(t) >= 4.5
nombre = lambda alumno: alumno[0]
notas = lambda alumno: alumno[1:][0]

antonio = ('Antonio Pérez', (1., 4., 2.))
maria = ('María Rodríguez', (8., 7., 5.))
sonia = ('Sonia González', (9., 10.))
matriculas = (maria, antonio, sonia)

"""
aprobados(m: tuple[tuple[str, tuple[float]]]) -> tuple[str]
"""
aprobados = lambda m: () if m == () else \
      ((nombre(m[0]),) if esta_aprobado(notas(m[0])) else ()) + aprobados(m[1:])
