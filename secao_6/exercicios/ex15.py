numero = int(input('Digite um número: '))
if numero > 0 and numero % 2 == 1:
    for num in range(0, numero * 2):
        if num % 2 == 1 and num >= 0:
            print(num)
        else:
            pass
else:
    print('Digite um número inteiro positivo ímpar')
