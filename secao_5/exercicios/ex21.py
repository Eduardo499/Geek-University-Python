op = int(input("""Escolha a opção:
1 - Soma de 2 números
2 - Diferença entre 2 números (maior pelo menor)
3 - Produto entre 2 números
4 - Divisão entre 2 números (o denominador não pode ser zero)
"""))
if op == 1:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print(f'A soma entre esses números é {n1 + n2}')
elif op == 2:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    if n1 > n2:
        print(f'A diferença entre o maior pelo menor é {n1 - n2}')
    else:
        print(f'A diferença entre o maior pelo menor é {n2 - n1}')
elif op == 3:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print(f'O produto entre esses números é {n1 * n2}')
elif op == 4:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    if n2 == 0:
        print('É impossível dividir por zero!')
    else:
        print(f'O quociente entre esses números é {n1 / n2}')
else:
    print('Número inválido"')
