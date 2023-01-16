def fatorial_duplo(n):
    """Função que recebe um número e retornal o fatorial duplo do mesmo"""

    fatorial = 1

    if n > 0 and type(n) == int:
        for i in range(1, n + 1, 2):
            fatorial *= i

        return fatorial
    else:
        print('Valor inválido!')


print(fatorial_duplo(5))
