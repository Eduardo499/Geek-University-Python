n = int(input('Digite um número: '))

if n > 0:
    cont = 1

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f'{cont:<4}', end=' ')
            cont += 1
        print()

else:
    print('Número inválido')
