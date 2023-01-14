from math import factorial


def seno(angulo):
    """Função que recebe um ângulo em graus e retorna o valor de seu seno usando sua respectiva
    série de Taylor num range de 0 até 5 """

    if angulo > 0:
        pi = 3.141593
        x = angulo * pi / 180
        sen = 0

        for n in range(6):
            sen += (((-1) ** n) / factorial(2 * n + 1)) * (x ** (2 * n + 1))
        return sen
    else:
        print('Valor inválido!')


print(seno(30))
