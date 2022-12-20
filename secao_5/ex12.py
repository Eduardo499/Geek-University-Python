from math import log10
num = int(input('Digite um número: '))
if num > 0:
    print(f'O logaritimo de {num} na base 10 é {log10(num)}')
else:
    print('Número inválido')
