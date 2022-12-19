def aprobados_si_o_no(lista: list[dict]) -> list[tuple]:
    """
    Ejercicio 3.

    >>> aprobados_si_o_no([ \
        {"nombre": "Juan", "media": 7.2}, \
        {"nombre": "Antonio", "media": 2.5}, \
        {"nombre": "María", "media": 8.5} \
    ])
    [('Juan', True), ('Antonio', False), ('María', True)]
    """
    def auxiliar(dics):
        if len(dics) == 0:
            return
        alum = dics[0]
        res.append((alum['nombre'], alum['media'] >= 4.5))
        auxiliar(dics[1:])
    res = []
    auxiliar(lista)
    return res


def aprobados(lista):
    """
    Ejercicio 3.

    >>> aprobados([('Juan', True), ('Antonio', False), ('María', True)])
    ['Juan', 'María']
    """
    return [nombre for nombre, aprobado in lista if aprobado]
