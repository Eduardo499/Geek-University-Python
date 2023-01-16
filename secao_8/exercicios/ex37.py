def hiperfatorial(n):
    """Função que recebe um número e retorna seu hiperfatorial"""

    if n > 0 and type(n) == int:
        fatorial = 1

        for i in range(1, n + 1):
            fatorial *= i ** i

        return fatorial
    else:
        print('Valor inválido!')


print(hiperfatorial(5))
