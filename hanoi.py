"""
Versión funcional:
hanoi = lambda a, b, c, n: '' if n == 0 else \
    hanoi(a, c, b, n - 1) + \
    f'mueve un disco de {a} a {b}\n' + \
    hanoi(c, b, a, n - 1)
"""


# Versión imperativa:
def hanoi(a, b, c, n):
    if n == 0:
        return
    hanoi(a, c, b, n - 1)
    print(f'mueve un disco de {a} a {b}')
    hanoi(c, b, a, n - 1)
