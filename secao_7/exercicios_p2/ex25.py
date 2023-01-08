jogo = []

for i in range(3):
    velha = []
    for j in range(3):
        velha.append(0)
    jogo.append(velha)

cont = 1

continua = True
vezes = 0

while continua:
    for i in range(3):
        for j in range(3):
            print(f'{jogo[i][j]:<2}', end=' ')
        print()

    print()

    if cont % 2 == 0:
        print(f'Vez do jogador -1')
    elif cont % 2 == 1:
        print(f'Vez do jogador 1')

    linha = int(input('Digite a linha que você deseja colocar a peça (1 à 3): '))

    if 1 <= linha <= 3:
        coluna = int(input('Digite a coluna que você deseja colocar a peça (1 à 3):  '))

        if 1 <= coluna <= 3:
            if cont % 2 == 0:
                if jogo[linha - 1][coluna - 1] == 0:
                    jogo[linha - 1][coluna - 1] = -1

                    vezes += 1

                    cont += 1
                else:

                    print('Perdeu a vez, pois já existe uma peça neste local\n')
                    cont += 1
                    continue

            elif cont % 2 == 1:
                if jogo[linha - 1][coluna - 1] == 0:
                    jogo[linha - 1][coluna - 1] = 1

                    vezes += 1

                    cont += 1
                else:

                    print('Perdeu a vez, pois já existe uma peça neste local\n')
                    cont += 1
                    continue

        else:
            print('Perdeu a vez, pois a coluna é inválida\n')
            cont += 1
            continue
    else:
        print('Perdeu a vez, pois a linha é inválida\n')
        cont += 1
        continue

    for i in range(-1, 2, 1):

        if i == -1 or i == 1:
            for j in range(3):

                if jogo[j][0] == i and jogo[j][1] == i and jogo[j][2] == i:
                    print(f'\nO jogador {i} venceu!')
                    continua = False
                    break
                elif jogo[0][j] == i and jogo[1][j] == i and jogo[2][j] == i:
                    print(f'\nO jogador {i} venceu!')
                    continua = False
                    break
                elif jogo[0][0] == i and jogo[1][1] == i and jogo[2][2] == i:
                    print(f'\nO jogador {i} venceu!')
                    continua = False
                    break
                elif jogo[0][2] == i and jogo[1][1] == i and jogo[2][0] == i:
                    print(f'\nO jogador {i} venceu!')
                    continua = False
                    break

    if continua and vezes >= 9:
        print('\nEmpate')
        continua = False

    if not continua:
        print()
        for i in range(3):
            for j in range(3):
                print(f'{jogo[i][j]:<2}', end=' ')
            print()
