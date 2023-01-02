lista = []

for i in range(50):
    lista.append((i + 5 * i) % (i + 1))

print(lista)
