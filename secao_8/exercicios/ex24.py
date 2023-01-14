def triangulo(n):
    """Função que recebe um número inteiro e gera um triângulo de altura n e base 2 * n - 1"""

    if n > 0 and type(n) == int:
        for i in range(n + 1):
            for j in range(n):

                if i == n - j:
                    print((' ' * j) + ('*' * (2 * i - 1)))
    else:
        print('Número inválido!')


triangulo(500)
