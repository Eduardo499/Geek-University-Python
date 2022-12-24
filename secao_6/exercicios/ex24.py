num = int(input('Digite um número Natural: '))
soma = 0

if num > 0:
    print('Seus divisores são:')
    for i in range(1, num + 1):
        if num % i == 0 and num != i:
            soma += i
else:
    print('Digite um número Natural (inteiro positivo)')

print(f'A soma dos divisores desse número com excessão dele mesmo é {soma}')
