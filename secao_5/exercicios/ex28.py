from math import cbrt
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
op = int(input("""Escolha a opção:
1 - Médid Geométrica
2 - Média Ponderada
3 - Média Harmônica
4 - Média Aritmética
"""))
if op == 1:
    print(f'A média geométrica é {cbrt(n1 * n2 * n3)}')
elif op == 2:
    print(f'A média ponderada é {(n1 + n2 * 2 + n3 * 3) / 6}')
elif op == 3:
    print(f'A média harmônica é {1 / (1 / n1 + 1 / n2 + 1 / n3)}')
elif op == 4:
    print(f'A média aritmética é {(n1 + n2 + n3) / 3}')
else:
    print('Opção inválida!')
