from math import sqrt
num = int(input('Digite um número: '))
if num > 0:
    print(f'A raiz quadrada de {num} é {sqrt(num)}')
    print(f'{num} ao quadrado é {num ** 2}')
else:
    print('Número inválido!')
