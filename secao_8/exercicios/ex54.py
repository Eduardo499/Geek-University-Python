def soma(*args):
    """Função que recebe uma matriz 4x4 e retorna a soma de todos os seus elementos"""

    tamanho_4 = True

    for i in range(len(args)):
        for j in range(len(args[i])):

            if not len(args) == len(args[i]) == 4:
                tamanho_4 = False

    if tamanho_4:

        soma_elementos = 0

        for i in range(4):
            for j in range(4):
                soma_elementos += args[i][j]

        return soma_elementos


matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(f'A soma dos elementos dessa matriz é {soma(*matriz)}')
