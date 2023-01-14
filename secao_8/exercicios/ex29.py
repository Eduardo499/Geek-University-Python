from math import factorial


def seno_hiperbolico(angulo):
    """Função que recebe um ângulo em graus e retorna o valor de seu seno hiperbólico usando sua respectiva
    série de Taylor num range de 0 até 5 """

    if angulo > 0:
        pi = 3.141593
        x = angulo * pi / 180
        senh = 0

        for n in range(6):
            senh += (x ** (2 * n + 1)) / factorial(2 * n + 1)
        return senh
    else:
        print('Valor inválido!')


print(seno_hiperbolico(30))
