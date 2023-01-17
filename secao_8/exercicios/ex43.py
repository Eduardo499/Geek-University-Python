from random import randint


def preencher(*args):
    """Função que recebe um vetor vários números e preenche ele com números aleátorios sem repetição"""

    lista = []

    for i in args:
        if type(i) == int:
            lista.append(i)

    for i in lista:
        n = randint(1, 99)
        if n not in lista:
            lista.append(n)

    return lista


numeros = [1, 2, 3, 4, 5, 6, 8, 9]
print(preencher(*numeros))
