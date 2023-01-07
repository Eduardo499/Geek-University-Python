from random import randint

lista1 = []
lista2 = []

for i in range(4):
    for j in range(4):
        lista2.append(randint(1, 20))
    lista1.append(lista2)
    lista2 = []

print()
print('Matriz Original')
print()

for linha in lista1:
    for numero in linha:
        print(f'{numero:<3}', end=' ')
    print()

for i in range(4):
    for j in range(4):
        if i != 0 and i == j:
            for k in range(1, i + 1):
                lista1[i - k][j] = 0

print()
print('Matriz Transformada')
print()

for linha in lista1:
    for numero in linha:
        print(f'{numero:<3}', end=' ')
    print()
