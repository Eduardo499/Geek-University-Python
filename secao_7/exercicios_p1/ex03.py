lista1 = []
lista2 = []

for c in range(1, 11):
    n = float(input(f'Digite o {c}° número: '))
    lista1.append(n)
    lista2.append(n ** 2)

print(lista1)
print(lista2)
