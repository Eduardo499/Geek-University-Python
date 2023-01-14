def somatorio(n):
    """Função que recebe um parâmetro 'n' e retorna o somátorio de 1 até 'n'"""

    soma = 0

    for i in range(1, n + 1):
        soma += i

    return soma


print(somatorio(5))
