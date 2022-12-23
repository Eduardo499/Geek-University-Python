op = int(input("""Escolha a opção:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
"""))
if op == 1:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print(f'A soma entre esses números é {n1 + n2}')
elif op == 2:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print(f'A diferença entre esses números é {n1 - n2}')
elif op == 3:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print(f'O produto entre esses números é {n1 * n2}')
elif op == 4:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print(f'O quociente entre esses números é {n1 / n2}')
else:
    print('Opção inválida!')
