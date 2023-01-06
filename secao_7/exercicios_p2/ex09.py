lista1 = []
lista2 = []
soma = 0

for i in range(3):
    for j in range(3):
        n = int(input('Digite um número: '))
        lista2.append(n)
    lista1.append(lista2)
    lista2 = []

print()
for i in range(3):
    for j in range(3):
        print(f'{lista1[i][j]:<2}', end=' ')

        if i != 0 and i == j:

            for c in range(1, i + 1):
                soma += lista1[i][j - c]
    print()
print()
print(f'A soma de todos os elementos que não estão na diagonal principal é {soma}')
