num = int(input('Digite um número Natural: '))

if num > 0:
    print('Seus divisores são:')
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
else:
    print('Digite um número Natural (inteiro positivo)')
