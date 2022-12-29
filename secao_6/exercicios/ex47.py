while True:
    op = int(input('Adição - 1\nSubtração - 2\nMultiplicação - 3\nDivisão - 4\nSaída - 5\n'))

    if op == 1:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print(f'A soma entre esses dois números é {n1 + n2}')
        print('-' * 20)
    elif op == 2:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print(f'A diferença entre esses dois números é {n1 - n2}')
        print('-' * 20)
    elif op == 3:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print(f'O produto entre esses dois números é {n1 * n2}')
        print('-' * 20)
    elif op == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print(f'O quociente entre esses dois números é {n1 / n2}')
        print('-' * 20)
    elif op == 5:
        break
    else:
        print('Opção inválida!')
