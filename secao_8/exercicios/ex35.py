def fatorial_quadruplo(n):
    """Função que recebe um número e retorna seu fatorial quádruplo"""

    if n > 0 and type(n) == int:

        fatorial_numerador = 1
        fatorial_denominador = 1

        for i in range(n, 1, -1):
            fatorial_denominador *= i

        for i in range(n * 2, 1, -1):
            fatorial_numerador *= i

        return fatorial_numerador / fatorial_denominador
    else:
        print('Valor inválido!')


print(fatorial_quadruplo(5))
