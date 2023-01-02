lista = []

for c in range(1, 6):
    n = int(input(f'Digite o {c}° número: '))
    lista.append(n)

print()
print(lista)
print(f'O maior valor digitado foi {max(lista)}')
print(f'O menor valor digitado foi {min(lista)}')
print(f'A média de valores digitado foi {sum(lista) / len(lista)}')
