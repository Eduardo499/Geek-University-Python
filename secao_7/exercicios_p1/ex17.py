lista = []

for c in range(1, 11):
    n = int(input(f'Digite o {c}° número: '))
    lista.append(n)

print()
print(lista)
for i in lista:
    if i < 0:
        lista[lista.index(i)] = 0

print()
print(lista)
