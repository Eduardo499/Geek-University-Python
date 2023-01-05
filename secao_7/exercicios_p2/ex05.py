lista1 = []
lista2 = []

for i in range(4):
    for j in range(4):
        lista2.append(int(input('Digite um número: ')))
    lista1.append(lista2)
    lista2 = []

print()
for c in lista1:
    print(c)
print()
n = int(input('Digite um número para verificar se ele existe na matriz: '))
print()
for k in lista1:
    if n in k:
        print(f'Encontrei o número {n} na linha: {k.index(n)  + 1}, da coluna: {lista1.index(k) + 1}')
    else:
        print(f'Não encontrei o número {n} na coluna {lista1.index(k) + 1}')
