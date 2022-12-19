def str2dict(lista):
    """
    >>> str2dict(['1=uno', '2=dos', '3=tres', '4=cuatro'])
    {'1': 'uno', '2': 'dos', '3': 'tres', '4': 'cuatro'}
    >>> str2dict(['pepe=humano', 'pancho=perro', 'violeta=gato', 'gustavo=rana'])
    {'pepe': 'humano', 'pancho': 'perro', 'violeta': 'gato', 'gustavo': 'rana'}
    """
    return dict(e.split('=') for e in lista)


def ahorcado(intento):
    """
    >>> ahorcado('OFIMATICA')
    I_FO_MATICA
    >>> ahorcado('INFORMATICA')
    ¡Enhorabuena!
    >>> ahorcado('MANZANA')
    _N___MA___A
    >>> ahorcado('MATEMATICAS')
    I____MATICA
    """
    with open('ahorcado.txt') as f:
        solucion = f.readline().strip()
    if intento == solucion:
        print('¡Enhorabuena!')
    else:
        for c in solucion:
            print(c if c in intento else '_', end='')


def unicos(secuencia):
    """
    >>> unicos([1, 9, 8, 8, 7, 6, 1, 6]) == {7, 9}
    True
    >>> unicos((5, 5, 2, 4, 4, 4, 9, 9, 9, 1)) == {1, 2}
    True
    >>> unicos([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) == {5, 6}
    True
    >>> unicos([4, 3, 9, 9, 1, 1, 6, 1, 6, 2, 4]) == {2, 3}
    True
    """
    def auxiliar(sec, acc):
        if len(sec) == 0:
            return acc
        n = sec[0]
        if secuencia.count(n) == 1:
            acc.add(n)
        return auxiliar(sec[1:], acc)

    return auxiliar(secuencia, set())
