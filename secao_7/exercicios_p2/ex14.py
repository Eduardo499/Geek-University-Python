from random import randint

lista1 = []
lista2 = []
lista3 = []

while len(lista1) < 5:
    while len(lista2) < 5:
        n = randint(0, 99)
        if n not in lista3:
            lista3.append(n)
            lista2.append(n)
    lista1.append(lista2)
    lista2 = []

for linha in lista1:
    for numero in linha:
        print(f'{numero:<3}', end=' ')
    print()
