from random import randint

matriz_grande = []

for i in range(20):
    elementos = []
    for j in range(20):
        elementos.append(randint(0, 99))
    matriz_grande.append(elementos)

for linha in matriz_grande:
    for numero in linha:
        print(f'{numero:<2}', end=' ')
    print()

matriz_cima = []
matriz_baixo = []
matriz_direita = []
matriz_esquerda = []
matriz_diagonal = []

for i in range(19, -1, -1):

    if i >= 2:
        num = 1

        for j in range(20):
            num = matriz_grande[i][j] * matriz_grande[i - 1][j] * matriz_grande[i - 2][j] * matriz_grande[i - 3][j]
            matriz_cima.append(num)

print()
print(len(matriz_cima))

for i in range(20):
    if i <= 16:
        num = 1

        for j in range(20):
            num = matriz_grande[i][j] * matriz_grande[i + 1][j] * matriz_grande[i + 2][j] * matriz_grande[i + 3][j]
            matriz_baixo.append(num)

print()
print(len(matriz_baixo))

for i in range(20):
    num = 1
    for j in range(20):
        if j <= 16:
            num = matriz_grande[i][j] * matriz_grande[i][j + 1] * matriz_grande[i][j + 2] * matriz_grande[i][j + 3]
            matriz_direita.append(num)

print()
print(len(matriz_direita))

for i in range(20):
    num = 1

    for j in range(19, -1, -1):

        if j >= 2:
            num = matriz_grande[i][j] * matriz_grande[i][j - 1] * matriz_grande[i][j - 2] * matriz_grande[i][j - 3]
            matriz_esquerda.append(num)

print()
print(len(matriz_esquerda))

for i in range(20):
    num = 1

    for j in range(20):
        if i <= 16 and j <= 16:
            num = matriz_grande[i][j] * matriz_grande[i + 1][j + 1] * matriz_grande[i + 2][j + 2] * matriz_grande[i + 3][j + 3]
        matriz_diagonal.append(num)

    for j in range(19, -1, -1):
        if i <= 16 and j >= 3:
            num = matriz_grande[i][j] * matriz_grande[i + 1][j - 1] * matriz_grande[i + 2][j - 2] * matriz_grande[i + 3][j - 3]
        matriz_diagonal.append(num)

print()
print(len(matriz_diagonal))

produtos = [max(matriz_cima), max(matriz_baixo), max(matriz_direita), max(matriz_esquerda), max(matriz_diagonal)]

maior_produto = max(produtos)

print()
print(f'O maior produto é {maior_produto}')
