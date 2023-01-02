lista = []
cont = 0
soma = 0

for c in range(1, 11):
    n = float(input(f'Digite o {c}° número: '))
    lista.append(n)

    if n < 0:
        cont += 1
    else:
        soma += n

print()
print(f'Foram digitado {cont} números negativos')
print(f'A soma dos números positivos é {soma}')
