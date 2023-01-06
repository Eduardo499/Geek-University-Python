lista1 = []
lista2 = []
soma = 0
cont = 0

for i in range(3):
    for j in range(3):
        n = int(input('Digite um número: '))
        lista2.append(n)
        if j == cont:
            soma += n
    cont += 1
    lista1.append(lista2)
    lista2 = []
print()
for i in range(3):
    for j in range(3):
        print(f'{lista1[i][j]:<2}', end=' ')
    print()
print()
print(f'A soma de todos os elementos na diagonal principal é {soma}')
