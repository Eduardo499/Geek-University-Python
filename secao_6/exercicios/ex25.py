soma = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        soma += i
print(f'A soma de todos multiplos de 3 e 5 é {soma}')
