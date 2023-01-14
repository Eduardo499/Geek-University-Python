from math import factorial


def cosseno_hiperbolico(angulo):
    """Função que recebe um ângulo em graus e retorna o valor de seu cosseno hiperbólico usando sua respectiva
    série de Taylor num range de 0 até 5 """

    if angulo > 0:
        pi = 3.141593
        x = angulo * pi / 180
        cosh = 0

        for n in range(6):
            cosh += (x ** (2 * n)) / factorial(2 * n)
        return cosh
    else:
        print('Valor inválido!')


print(cosseno_hiperbolico(30))
