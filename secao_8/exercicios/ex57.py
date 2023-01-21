from random import randint


def soma_coluna(coluna, *args):
    """Função que recebe uma matriz 7x6 e retorna a soma da coluna n"""
    soma = 0
    tamanho = True

    if len(args) == 7:

        for i in range(len(args)):

            if len(args[i]) == 6:
                for j in range(len(args[i])):

                    if type(args[i][j]) == str:
                        tamanho = False

                    if j == coluna:
                        soma += args[i][j]
            else:
                tamanho = False

        if tamanho:
            return soma


matriz = []

for i in range(7):
    elementos = []
    for j in range(6):
        elementos.append(randint(1, 10))
    matriz.append(elementos)

for i in range(7):
    for j in range(6):
        print(f'{matriz[i][j]:<2}', end=' ')
    print()

print()
n = int(input('Digite uma coluna para somar: '))
print()
print(f'A soma dos elementos da coluna {n} dessa matriz é {soma_coluna(n, *matriz)}')
