lista = []
cont = 0

for c in range(1, 11):
    n = int(input(f'Digite o {c}° número: '))
    lista.append(n)

for i in lista:
    if i % 2 == 0:
        cont += 1

print()
print(f'A lista possuí {cont} valores pares')
