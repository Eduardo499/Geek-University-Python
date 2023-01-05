lista1 = []
lista2 = []
maior = 0

for i in range(4):
    for j in range(4):
        n = int(input('Digite um número: '))
        lista2.append(n)
        if n > maior:
            maior = n
    lista1.append(lista2)
    lista2 = []

print()
for c in lista1:
    print(c)
print()
print(f'O maior elemento dessa matriz é {maior}')
