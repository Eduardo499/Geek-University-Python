from math import sqrt
num = float(input('Digite um número: '))
if num > 0:
    print(f'A raiz quadradada de {num} é {sqrt(num)}')
else:
    print(f'{num} ao quadrado é {num ** 2}')
