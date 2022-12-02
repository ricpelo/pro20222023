"""
Escribir un programa que determine si un número entero
introducido por teclado es primo o compuesto.
"""

def es_primo(n):
    def divisores(n):
        res = 0
        i = 1
        while i <= n:
            if n % i == 0:
                res += 1
            i += 1
        return res
    return divisores(n) == 2

while True:
    try:
        num = int(input('Introduzca un número entero: '))
        if num < 2:
            print('El número debe ser mayor o igual que 2.')
        else:
            break
    except ValueError:
        print('El dato introducido no es correcto.')

if es_primo(num):
    print('El número', num, 'es primo.')
else:
    print('El número', num, 'NO es primo.')
