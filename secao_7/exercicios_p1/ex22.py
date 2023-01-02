lista1 = []
lista2 = []
lista3 = []

for c in range(1, 11):
    n1 = int(input(f'Digite o {c}° número para a primeira lista: '))
    n2 = int(input(f'Digite o {c}° número para a segunda lista: '))
    lista1.append(n1)
    lista2.append(n2)

for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print()
print(lista1)
print(lista2)
print(lista3)
