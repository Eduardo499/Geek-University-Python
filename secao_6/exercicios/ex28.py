from math import factorial

num = int(input('Digite um número inteiro e positivo: '))
e = 1

if num > 0:
    for i in range(1, num + 1):
        e += 1 / factorial(i)
else:
    print('O número deve ser positivo!')

print(f'e = {e}')
