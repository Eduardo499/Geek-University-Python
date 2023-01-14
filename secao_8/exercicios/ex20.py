def fatorial(n):
    """Função que recebe um número 'n' e retorna n!"""

    fat = 1

    for i in range(n, 1, -1):
        fat *= i
    return fat


num = int(input('Digite um número: '))
print()
print(fatorial(num))
