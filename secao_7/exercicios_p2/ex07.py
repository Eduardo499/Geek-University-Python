lista1 = []
lista2 = []

for i in range(10):
    for j in range(10):
        if i < j:
            lista2.append(2 * i + 7 * j - 2)
        elif i == j:
            lista2.append(3 * (i ** 2) - 1)
        elif i > j:
            lista2.append(4 * (i ** 3) - 5 * (j ** 2) + 1)
    lista1.append(lista2)
    lista2 = []

for linha in lista1:
    for numero in linha:
        print(f'{numero:>6}', end=' ')
    print()
