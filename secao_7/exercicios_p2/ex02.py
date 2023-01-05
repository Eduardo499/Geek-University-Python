lista1 = []
lista2 = []
cont = 0

for i in range(5):
    for j in range(5):
        if j == cont:
            lista2.append(1)
        else:
            lista2.append(0)
    cont += 1
    lista1.append(lista2)
    lista2 = []

for c in lista1:
    print(c)
