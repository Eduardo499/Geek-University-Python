def soma(*args):
    """Função que recebe uma matriz 4x4 e retorna a soma de todos os seus elementos"""

    tamanho_4 = True

    for i in range(len(args)):
        for j in range(len(args[i])):

            if not len(args) == len(args[i]) == 3:
                tamanho_4 = False

    if tamanho_4:

        soma_elementos = 0

        for i in range(3):
            for j in range(3):
                if i == j:
                    soma_elementos += args[i][j]

        soma_elementos += args[2][0] + args[0][2]

        return soma_elementos


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'A soma dos elementos dessa matriz é {soma(*matriz)}')
