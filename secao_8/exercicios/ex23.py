def triangulo_lateral(n):
    """Função que recebe um número inteiro e gera um triângulo lateral de altura 2 * n - 1 e n de largura"""

    if n > 0 and type(n) == int:

        for i in range(1, n + 1):
            print('*' * i)
        for i in range(n - 1, 0, -1):
            print('*' * i)
    else:
        print('Número inválido!')


triangulo_lateral(500)
