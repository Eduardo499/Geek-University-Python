from math import factorial


def superfatorial(n):
    """Função que recebe um número e retorna seu superfatorial"""

    if n > 0 and type(n) == int:
        fatorial = 1

        for i in range(1, n + 1):
            fatorial *= factorial(i)

        return fatorial
    else:
        print('Valor inválido!')


print(superfatorial(4))
