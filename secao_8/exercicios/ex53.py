def matriz_identidade(*args):
    """Função que recebe uma matriz quadrada e verifica se ela é uma matriz identidade"""

    quadrada = True

    for i in range(len(args)):
        for j in range(len(args[i])):

            if not len(args) == len(args[i]):
                quadrada = False

    if quadrada:
        diagonal_1 = True
        resto_0 = True

        for i in range(len(args)):
            for j in range(len(args[i])):

                if i == j and not args[i][j] == 1:
                    diagonal_1 = False

                if not i == j and not args[i][j] == 0:
                    resto_0 = False

        if diagonal_1 and resto_0:
            return True

        return False

    return False


matriz = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

if matriz_identidade(*matriz):
    print('Essa matriz é uma matriz identidade')
else:
    print('Essa matriz não é uma matriz identidade')
