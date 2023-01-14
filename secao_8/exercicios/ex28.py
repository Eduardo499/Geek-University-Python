from math import factorial


def cosseno(angulo):
    """Função que recebe um ângulo em graus e retorna o valor de seu cosseno usando sua respectiva
    série de Taylor num range de 0 até 5 """

    if angulo > 0:
        pi = 3.141593
        x = angulo * pi / 180
        cos = 0

        for n in range(6):
            cos += (((-1) ** n) / factorial(2 * n)) * (x ** (2 * n))
        return cos
    else:
        print('Valor inválido!')


print(cosseno(60))
