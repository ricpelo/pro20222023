def obtener_numero(prompt):
    intentos = 0
    while True:
        intentos += 1
        if intentos > 3:
            print('Me cansé.')
            raise Exception('Final')
        try:
            res = int(input(prompt))
            break
        except ValueError:
            print('El dato introducido no es un número entero.')
    return res

try:
    x = obtener_numero('Introduzca el primer número: ')
    y = obtener_numero('Introduzca el segundo número: ')
    print('El resultado es:', x + y)
except Exception:
    print('Ha ocurrido un error.')
