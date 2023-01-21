def matriz_transporta(*args):
    """Função que recebe uma matriz de tamanho n e retorna sua transporta"""

    transporta = []

    for i in range(len(args)):
        matriz = []
        for j in range(len(args)):
            matriz.append(args[j][i])
        transporta.append(matriz)

    return transporta


lista1 = []
lista2 = []

tamanho = int(input('Digite o tamanho da matriz: '))

for i in range(tamanho):
    for j in range(tamanho):
        lista1.append(int(input('Digite um número: ')))

    lista2.append(lista1)
    lista1 = []

print()
print('Matriz Original')
print()
for linha in lista2:
    for numero in linha:
        print(f'{numero:<2}', end=' ')
    print()
print()
print('Matriz Transporta')
print()

lista2_transporta = matriz_transporta(*lista2)

for linha in lista2_transporta:
    for numero in linha:
        print(f'{numero:<2}', end=' ')
    print()
