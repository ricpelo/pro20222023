f = open('entrada.txt', 'r')
lineas = f.readlines()
f.close()
x, y = [int(x.strip()) for x in lineas]
suma = x + y
f = open('salida.txt', 'w')
f.write(str(suma) + '\n')
f.close()
