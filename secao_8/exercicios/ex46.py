def imprimir(*args):
    """Função que recebe um vetor e o imprimi"""

    v = [*args]

    print(v)


def imprimir_inverso(*args):
    """Função que recebe um vetor e o imprimi inversamente"""

    v = [*args]

    print(v[::-1])


def media_aritmetica(*args):
    """Função que recebe um vetor e retorna a média aritmética"""

    v = [*args]

    return sum(v) / len(v)


vetor = [1, 2, 3, 4, 5]
imprimir(*vetor)
imprimir_inverso(*vetor)
print(media_aritmetica(*vetor))
