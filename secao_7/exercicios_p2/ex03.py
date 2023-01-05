lista1 = []
lista2 = []

for i in range(4):
    for j in range(4):
        lista2.append(i * j)
    lista1.append(lista2)
    lista2 = []

for c in lista1:
    print(c)
    