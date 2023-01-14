def serie(n):
    """Função que recebe um parâmetro 'n' e retorna a soma da série (n² + 1) / (n + 3) num range de 1 a 'n'"""

    s = 0

    for i in range(1, n + 1):
        s += (i ** 2 + 1) / (i + 3)

    return s


print(serie(500))
