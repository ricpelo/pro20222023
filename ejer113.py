import random

with open('/usr/share/dict/words') as f:
    palabras = f.readlines()

secreta = random.choice(palabras).strip()
tabla = str.maketrans({'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'})
secreta = secreta.translate(tabla)
print('-' * len(secreta))

intentos = []
total_intentos = 2 * len(secreta)

for num_intento in range(1, total_intentos + 1):
    print('Intentos:', ''.join(intentos))
    letra = input(f'(Intento {num_intento} de {total_intentos}) Introduzca una letra: ')
    if letra not in intentos:
        intentos.append(letra)
    acertado = True
    for c in secreta:
        if c in intentos:
            print(c, end='')
        else:
            acertado = False
            print('-', end='')
    print()
    if acertado:
        print('¡Enhorabuena!')
        break
