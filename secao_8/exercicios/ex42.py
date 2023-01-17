def media(*args):
    """Função que recebe vários números e retorna a média aritmética"""

    lista = [*args]

    return sum(lista) / len(lista)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(media(*numeros))
