from math import factorial


def numero_neperiano(n):
    """Função que recebe um número de termos 'n' e retorna o número neperiano, quanto maior o valor de 'n' mais
    próximo o resultado fica do número 'e' """

    if n > 0:

        e = 0

        for i in range(n + 1):
            e += 1 / factorial(i)
        return e
    else:
        print('Número inválido!')


print(numero_neperiano(500))
