lista1 = []
lista2 = []
lista3 = []
lista_transporta = []
somas = []

for i in range(3):
    for j in range(3):
        lista2.append(int(input('Digite um número: ')))
    lista1.append(lista2)
    lista2 = []

print()

for linha in lista1:
    for numero in linha:
        print(f'{numero:<2}', end=' ')
    print()

for i in range(3):
    for j in range(3):
        lista3.append(lista1[j][i])
    lista_transporta.append(lista3)
    lista3 = []

for i in range(3):
    soma = 0
    for j in range(3):
        soma += lista1[j][i]
    somas.append(soma)

print(f'A soma de cada coluna da matriz é: {somas}')
