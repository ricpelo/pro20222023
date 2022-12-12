"""
1 Devolver el último elemento

Crear una función que devuelva el valor del último elemento de
una lista o cadena.

Ejemplos

last_ind([0, 4, 19, 34, 50, -9, 2]) == 2
last_ind("The quick brown fox jumped over the lazy dog") == "g"
last_ind([]) == None

Notas

• Las listas/cadenas pueden ser de cualquier tamaño.
• Devuelve None si la lista/cadena está vacía.
"""

def last_ind(sec):
    """
    Devuelve el valor del último elemento de una lista o cadena.
    Las listas/cadenas pueden ser de cualquier tamaño.
    Devuelve None si la lista/cadena está vacía.

    >>> last_ind([0, 4, 19, 34, 50, -9, 2])
    2
    >>> last_ind("The quick brown fox jumped over the lazy dog")
    'g'
    >>> last_ind([]) is None
    True
    """
    return None if len(sec) == 0 else sec[-1]

names = ["Dennis", "Vera", "Mabel", "Annette", "Sussan"]
jobs = ["Butcher", "Programmer", "Doctor", "Teacher", "Lecturer"]

def assign_person_to_job(nombres, profesiones):
    """
    Devuelve un diccionario que asocia los nombres de las
    personas con su respectiva profesión.

    >>> assign_person_to_job(names, jobs) == \
        {'Dennis': 'Butcher', 'Vera': 'Programmer', \
         'Mabel': 'Doctor', 'Annette': 'Teacher', \
         'Sussan': 'Lecturer'}
    True
    """
    # Una solución:
    # return dict(zip(nombres, profesiones))

    # Otra solución:
    # res = {}
    # for i, nombre in enumerate(nombres):
    #     profesion = profesiones[i]
    #     res[nombre] = profesion
    # return res

    # Otra solución:
    res = {}
    for nombre, profesion in zip(nombres, profesiones):
        res[nombre] = profesion
    return res

def calculate_losses(dic):
    return "Lucky you!" if dic == {} else sum(dic.values())

def add_name(obj, name, value):
    res = obj.copy()
    res[name] = value
    return res
