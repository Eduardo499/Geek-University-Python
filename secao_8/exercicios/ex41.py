def maior(*args):
    """Função que recebe vários números e retorna o maior"""

    lista = []

    for i in args:
        if type(i) == int:
            lista.append(i)

    return max(lista)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(maior(*numeros))
