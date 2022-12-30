n = int(input('Digite um número: '))
cont = 0

if n > 1:
    for c in range(1, n + 1):
        if n % 1 == 0 and n % c == 0:
            cont += 1

    if cont <= 2:
        print('Número primo')
    else:
        print('Não é primo')
else:
    print('O número deve ser maior que um')
