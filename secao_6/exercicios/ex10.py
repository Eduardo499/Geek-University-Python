numero = int(input('Digite um número: '))
soma = 0
for num in range(1, numero * 2 + 1):
    if num % 2 == 0 and num > 0:
        soma += num
    else:
        pass
print(f'A soma dos {numero} primeiro pares é {soma}')
