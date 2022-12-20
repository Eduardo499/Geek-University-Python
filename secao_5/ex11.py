def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


n = int(input('Digite um número: '))
if n > 0:
    print(f'A soma dos algarismos de {n} é {getSum(n)}')
else:
    print('Número inválido')
