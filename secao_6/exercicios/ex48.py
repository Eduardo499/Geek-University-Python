soma1 = 0
soma2 = 1
soma_pares = 0

for i in range(1, 1_000_000):
    soma1 += soma2
    soma2 += soma1

    if soma1 > 4_000_000 or soma2 > 4_000_000:
        break

    if soma1 <= 4_000_000 and soma1 % 2 == 0:
        soma_pares += soma1

    if soma2 <= 4_000_000 and soma2 % 2 == 0:
        soma_pares += soma2
print(soma_pares)
