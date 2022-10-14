"""
Programa que calcula las soluciones reales de una
ecuación de segundo grado.

Entrada: a, b, c: reales
Salida: x1, x2: soluciones reales de la ecuación ax² + bx + c = 0
"""

from math import sqrt

# Entradas:
a = 2.0
b = 4.0
c = 6.0

# Datos intermedios:
disc = b ** 2 - 4 * a * c
denom = 2 * a

# Salidas:
x1 = (-b + sqrt(disc)) / denom if disc >= 0 else 'ERROR'
x2 = (-b - sqrt(disc)) / denom if disc >= 0 else 'ERROR'
