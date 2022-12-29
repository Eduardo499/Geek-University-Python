soma1 = 0
soma2 = 1

n = int(input('Digite um número: '))

if n > 0:

    print('0')
    print('1')

    for i in range(0, n):
        soma1 += soma2
        soma2 += soma1

        print(soma1)

        if soma1 > n:
            break

        print(soma2)

        if soma2 > n:
            break
else:
    print('O número deve ser positivo')
