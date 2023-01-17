def separador(*args):
    """Função que recebe um vetor com números inteiros e separa em outros dois, vetor A com números pares e B com
    número ímpares """

    x = []

    for i in args:
        if type(i) == int:
            x.append(i)

    a = []
    b = []

    for i in x:
        if i % 2 == 0:
            a.append(i)
        elif i % 2 == 1:
            b.append(i)

    return a, b


numeros = range(30)
print(separador(*numeros))
