lista = []

for c in range(1, 11):
    n = int(input(f'Digite o {c}° número: '))
    lista.append(n)

print()
print(f'O maior valor digitado foi {max(lista)}')
print(f'O menor valor digitado foi {min(lista)}')
