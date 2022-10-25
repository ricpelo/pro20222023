# Ejercicio 5:

aprox = lambda long_tibia, sexo: \
            69.089 + 2.232 * long_tibia if sexo == 'V' else \
            61.412 + 2.317 * long_tibia

altura = lambda long_tibia, sexo, edad: \
            aprox(long_tibia, sexo) - \
                (0.06 * (edad - 29) if edad >= 30 else 0)

"""
>>> altura(20, 'V', 35)
113.369
"""

"""
Ejercicio 6:

Escribir una función que calcule el volumen de una esfera a
partir de su radio, usando la siguiente fórmula:
"""

from math import pi

volumen = lambda r: (4 / 3) * pi * (r ** 3)

"""
>>> volumen(5)
523.5987755982989
"""

"""
7. Escribir una función que compruebe si tres datos de entrada
tienen el mismo valor.
"""

iguales3 = lambda x, y, z: x == y and y == z

"""
>>> iguales3(4, 5, 6)
False
>>> iguales3(5, 5, 5)
True
"""

"""
8. Escribir una función que compruebe si cuatro datos de entrada
tienen el mismo valor.
"""

# iguales4 = lambda a, b, c, d: a == b and b == c and c == d

iguales4 = lambda a, b, c, d: iguales3(a, b, c) and c == d

"""
>>> iguales4(1, 2, 3, 4)
False
>>> iguales4(2, 2, 2, 2)
True
"""

"""
11. Escribir una función que calcule el mínimo común múltiplo
(mcm) de dos números enteros, de dos formas diferentes:
a) Mediante la función lcm del módulo math.
b) Aprovechando la siguiente propiedad:
   𝑎 · 𝑏 = 𝑚𝑐𝑑(𝑎, 𝑏) · 𝑚𝑐𝑚(𝑎, 𝑏)
"""

from math import lcm, gcd

# mcm = lcm

mcm = lambda a, b: (a * b) // gcd(a, b)

"""
>>> mcm(16, 6)
48
"""

"""
12. Escribir una función que quite todos los espacios en blanco
que se encuentren dentro de una cadena. La salida será la cadena
de entrada pero sin los espacios en blanco. Por ejemplo, ante la
entrada "Esto es una prueba" la salida debería ser
"Estoesunaprueba".
"""

quita_espacios = lambda s: s.replace(' ', '')

"""
>>> quita_espacios('Esto es una prueba')
'Estoesunaprueba'
"""

"""
13. Escribir una función que diga si dos cadenas son iguales sin
tener en cuenta las mayúsculas y minúsculas. Por ejemplo, el
programa debería decir que las cadenas "Hola" y "hoLa" son iguales.
"""

compara_insensible = lambda s1, s2: s1.lower() == s2.lower()

"""
>>> compara_insensible('Hola', 'hoLa')
True
"""

"""
14. Usando el método maketrans definido sobre las cadenas,
escribir una función que sustituya en una cadena las vocales
acentuadas por sus correspondientes sin acentuar. Por ejemplo,
si la entrada es la cadena "¡Ramón! ¡Cuánto tiempo! ¿Cómo estás?",
la salida deberá ser "¡Ramon! ¡Cuanto tiempo! ¿Como estas?".
"""

sustituye = lambda s: s.translate(
    str.maketrans('áéíóúÁÉÍÓÚ', 'aeiouAEIOU')
)

"""
>>> sustituye("¡Ramón! ¡Cuánto tiempo! ¿Cómo estás?")
'¡Ramon! ¡Cuanto tiempo! ¿Como estas?'
"""

"""
15. Escribir una función que diga si una cadena es un palíndromo.
Un palíndromo es una cadena que se lee igual de izquierda a
derecha que al revés.

Por ejemplo: «Dábale arroz a la zorra el abad».

Deben ignorarse las tildes, las mayúsculas y los espacios en
blanco. Para ello, hacer uso de las soluciones encontradas en los
ejercicios anteriores.
"""

sanear = lambda s: quita_espacios(sustituye(s.lower()))

es_palindromo = lambda s: sanear(s)[::-1] == sanear(s)

"""
>>> es_palindromo('Dábale arroz a la zorra el abad')
True
"""
