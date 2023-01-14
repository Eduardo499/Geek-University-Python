def qtd_primos(n):
    """Função que recebe um número e retorna a quantidade de primos abaixo desse número"""

    cont = 0

    if 0 < n == n // 1:

        for i in range(1, n):
            cont = 0

            for j in range(1, i + 1):
                if i % j == 0:
                    cont += 1

            if cont <= 2:
                cont += 1

        return cont


print(qtd_primos(5))
