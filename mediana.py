def mediana(dic: dict) -> dict:
    """
    Ejercicio 2 del examen.

    >>> mediana({"nombre": "Juan", "notas": [7.5, 3.5, 9.0, 8.6]})
    {'nombre': 'Juan', 'notas': [7.5, 3.5, 9.0, 8.6], 'mediana': 8.1}
    >>> mediana({"nombre": "Juan", "notas": [7.5, 3.5, 9.0]})
    {'nombre': 'Juan', 'notas': [7.5, 3.5, 9.0], 'mediana': 7.5}
    """
    notas = sorted(dic['notas'])
    l = len(notas)
    mitad = l // 2

    if l % 2 == 0:
        mediana = (notas[mitad - 1] + notas[mitad]) / 2
    else:
        mediana = notas[mitad]

    # mediana = notas[mitad] if l % 2 == 0 else \
    #           (notas[mitad - 1] + notas[mitad]) / 2

    res = dic.copy()
    res['mediana'] = round(mediana, 1)
    return res
