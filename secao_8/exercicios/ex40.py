def contador_pares(*args):
    """Função que recebe quantos números for necessário e conta quantos pares existem"""
    inteiros = 0

    for i in args:
        if type(i) == int:
            inteiros += 1

    if inteiros == len(args):
        cont = 0

        for i in args:
            if i % 2 == 0:
                cont += 1

        return cont


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(contador_pares(*numeros))
