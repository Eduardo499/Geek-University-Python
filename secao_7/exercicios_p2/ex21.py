matriz = []
matriz2 = []

for i in range(2):
    elementos = []
    for j in range(2):
        elementos.append(float(input('Digite um número para a primeira matriz: ')))
    matriz.append(elementos)

for i in range(2):
    elementos = []
    for j in range(2):
        elementos.append(float(input('Digite um número para a segunda matriz: ')))
    matriz2.append(elementos)

print()

while True:
    op = int(input("""Escolha a opção:
1 - Somar as duas matrizes
2 - Subtrair a primeira matriz da segunda
3 - Adicionar uma constante às duas matrizes
4 - Imprimir as matrizes
"""))

    print()

    if op == 1:

        matriz_soma = []
        for i in range(2):
            elementos = []
            for j in range(2):
                elementos.append(matriz[i][j] + matriz2[i][j])
            matriz_soma.append(elementos)
        for linha in matriz_soma:
            for numero in linha:
                print(f'{numero:<2}', end=' ')
            print()
        break

    elif op == 2:

        matriz_sub = []
        for i in range(2):
            elementos = []
            for j in range(2):
                elementos.append(matriz[i][j] - matriz2[i][j])
            matriz_sub.append(elementos)
        for linha in matriz_sub:
            for numero in linha:
                print(f'{numero:<2}', end=' ')
            print()
        break

    elif op == 3:
        constante = float(input('Digite uma constante para adicionar as duas matrizes: '))

        for i in range(2):
            for j in range(2):
                matriz[i][j] += constante
                matriz2[i][j] += constante
        print('Primeira matriz:')
        print()
        for linha in matriz:
            for numero in linha:
                print(f'{numero:<2}', end=' ')
            print()

        print()
        print('Segunda matriz:')
        print()

        for linha in matriz2:
            for numero in linha:
                print(f'{numero:<2}', end=' ')
            print()

        break

    elif op == 4:

        print('Primeira matriz:')
        print()
        for linha in matriz:
            for numero in linha:
                print(f'{numero:<2}', end=' ')
            print()

        print()
        print('Segunda matriz:')
        print()

        for linha in matriz2:
            for numero in linha:
                print(f'{numero:<2}', end=' ')
            print()

        break
    else:
        print('Opção inválida!')
        print()
