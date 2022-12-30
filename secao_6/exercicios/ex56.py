soma = 0
cont_primos = 0

for i in range(1, 2_000_000):
    cont = 0

    for c in range(1, i + 1):
        if i % 1 == 0 and i % c == 0:
            cont += 1

    if cont_primos <= 2_000_000:
        if cont <= 2:
            cont_primos += 1
            soma += c
print(f'A soma dos números primos abaixo de 2 milhões é {soma}')
