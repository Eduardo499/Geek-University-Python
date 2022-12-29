maior = 0
menor = 0

while True:
    n = int(input('Digite um número: '))
    if n > 0:

        if n > maior:
            maior = n

        menor = n

        if n <= menor:
            menor = n
    else:
        break
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')
