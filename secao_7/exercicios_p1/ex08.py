lista = []

for c in range(1, 7):
    n = int(input(f'Digite o {c}° número: '))
    lista.append(n)

print()
print(lista[::-1])
