from random import randint


def produto_matrizes(args_a, args_b):
    """Função que recebe dua matrizes quadradas de tamanho n e retorna uma matriz 'c', que é o produto entre a matriz
    'a' e a matriz 'b' """

    quadrada_a = True
    quadrada_b = True

    for i in range(len(args_a)):
        for j in range(len(args_a[i])):

            if not len(args_a) == len(args_a[i]):
                quadrada_a = False

    for i in range(len(args_b)):
        for j in range(len(args_b[i])):

            if not len(args_b) == len(args_b[i]):
                quadrada_b = False

    if quadrada_a and quadrada_b:
        matriz_c = []

        for i in range(len(args_a)):
            produto = []
            for j in range(len(args_a[i])):
                produto.append(args_a[i][j] * args_b[i][j])
            matriz_c.append(produto)

        return matriz_c


n = int(input('Digite o tamanho das matrizes: '))
print()

matriz_quadrada1 = []
matriz_quadrada2 = []

for i in range(n):
    elementos1 = []
    elementos2 = []
    for j in range(n):
        elementos1.append(randint(1, 10))
        elementos2.append(randint(1, 10))
    matriz_quadrada1.append(elementos1)
    matriz_quadrada2.append(elementos2)


print('Matriz A')
print()

for i in range(n):
    for j in range(n):
        print(f'{matriz_quadrada1[i][j]:<2}', end=' ')
    print()

print()

print('Matriz B')
print()
for i in range(n):
    for j in range(n):
        print(f'{matriz_quadrada2[i][j]:<2}', end=' ')
    print()

print()

print('Matriz C = A * B')
print()

matriz_quadrada3 = produto_matrizes(matriz_quadrada1, matriz_quadrada2)

for i in range(n):
    for j in range(n):
        print(f'{matriz_quadrada3[i][j]:<2}', end=' ')
    print()
