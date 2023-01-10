def sin_repetidos(lst: list) -> list:
    """
    Ejercicio 85.

    >>> sin_repetidos([1, 2, 3, 2, 1, 2, 3, 3, 4, 2, 1, 2])
    [1, 2, 3, 4]
    >>> sin_repetidos([])
    []
    >>> sin_repetidos([1, 2, 3, 4])
    [1, 2, 3, 4]
    """
    res = []
    for e in lst:
        if e not in res:
            res.append(e)

    return res
