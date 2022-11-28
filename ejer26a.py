"""
Escribir un programa que lea un archivo de texto llamado
carta.txt. Tenemos que contar los caracteres, las líneas
y las palabras. Para simplificar, supondremos que cada
palabra está separada de otra por un único espacio en
blanco o por un salto de línea.
"""
f = open('carta.txt', 'r')
contenido = f.readlines()
f.close()

caracteres, lineas, palabras = 0, 0, 0

i = 0
while i < len(contenido):
    linea = contenido[i]
    caracteres += len(linea)
    lineas += 1
    palabras += linea.count(' ') + 1
    i += 1

print(lineas, palabras, caracteres, 'carta.txt')
