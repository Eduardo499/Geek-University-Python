lista1 = []
lista2 = []

for i in range(3):
    for j in range(6):
        lista2.append(float(input('Digite um número: ')))

    lista1.append(lista2)
    lista2 = []

print()

for linha in lista1:
    for numero in linha:
        print(f'{numero:<2}', end=' ')
    print()

print()

somas_impares = 0

for i in range(3):
    for j in range(6):
        if (j + 1) % 2 == 1:
            somas_impares += lista1[i][j]

print(f'Soma das colunas ímpares: {somas_impares}')

print()

media = []

for i in range(3):
    media.append(lista1[i][1])
    media.append(lista1[i][3])

print(f'Média aritmética das colunas 2 e 4: {sum(media) / len(media)}')

print()

for i in range(3):
    lista1[i][5] = lista1[i][0] + lista1[i][1]

for linha in lista1:
    for numero in linha:
        print(f'{numero:<2}', end=' ')
    print()
