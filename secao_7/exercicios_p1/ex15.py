lista = []

for c in range(1, 21):
    n = int(input(f'Digite o {c}° número: '))
    if n in lista:
        pass
    else:
        lista.append(n)

print()
print(lista)
