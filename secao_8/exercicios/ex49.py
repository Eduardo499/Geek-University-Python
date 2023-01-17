from random import randint


def soma(*args):
    """Função que recebe uma matriz 4x4 e retorna a soma dos valores que estão abaixo da diagonal principal"""

    matriz = [*args]

    if len(args) == 3:

        for linha in range(len(args)):

            if len(args[linha]) == 3:

                for numero in range(len(args[linha])):
                    print(f'{matriz[linha][numero]:<2}', end=' ')

                print()

    print()

    return matriz[2][2] + matriz[2][1] + matriz[1][2]


lista1 = []
lista2 = []

for i in range(3):
    for j in range(3):
        lista2.append(randint(1, 10))

    lista1.append(lista2)
    lista2 = []

print(soma(*lista1))
