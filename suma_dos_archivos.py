try:
    with open('entrada.txt', 'r') as f:
        lineas = f.readlines()
    x, y = [int(x.strip()) for x in lineas]
    suma = x + y
    with open('salida.txt', 'w') as f:
        f.write(str(suma) + '\n')
    print('La operación se ha realizado correctamente.')
except FileNotFoundError:
    print('Archivo no encontrado.')
except ValueError:
    print('Las líneas del archivo deben contener un número entero.')
