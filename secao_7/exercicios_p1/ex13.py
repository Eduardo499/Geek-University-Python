lista = []

for c in range(1, 6):
    n = int(input(f'Digite o {c}° número: '))
    lista.append(n)

print()
print(f'O maior valor digitado foi {max(lista)}, que se encontra na posição {lista.index(max(lista))}')
print(f'O menor valor digitado foi {min(lista)}, que se encontra na posição {lista.index(min(lista))}')
