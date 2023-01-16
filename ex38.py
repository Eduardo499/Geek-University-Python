def fatorial_exponencial(n):
    """Função que recebe um número e retorna seu fatorial exponencial"""

    if n > 0 and type(n) == int:

        for i in range(1, n + 1):

            if n - i != 0:
                n **= (n - i)

        return n
    else:
        print('Valor inválido!')


print(fatorial_exponencial(3))
