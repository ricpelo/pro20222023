"""
Pedir por consola un número n y dibujar un triángulo
rectángulo de n elementos de lado, utilizando para ello
asteriscos (*). Por ejemplo, para n = 4:

* * * *
* * *
* *
*

"""

while True:
    try:
        n = int(input('Introduzca un número entero: '))
        break
    except ValueError:
        print('El valor introducido no es correcto.')
