from random import randint


def contador(*args):
    """Função que recebe uma matriz 4x4 e retorna quantos valores maiores que 10 ela possui"""

    matriz = [*args]
    cont = 0

    for linha in matriz:
        for numero in linha:
            if numero == 10:
                cont += 1
            print(f'{numero:<2}', end=' ')
        print()

    print()

    return f'Essa matriz possui {cont} números dez'


lista1 = []
lista2 = []

for i in range(4):
    for j in range(4):
        lista2.append(randint(1, 10))

    lista1.append(lista2)
    lista2 = []

print(contador(*lista1))
