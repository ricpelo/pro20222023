f = open('suma.txt', 'r+')
x, y = [int(x) for x in f.readline().strip().split()]
f.seek(f.tell())
suma = x + y
f.write(str(suma) + '\n')
f.close()
