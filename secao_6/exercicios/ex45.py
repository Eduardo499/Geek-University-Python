while True:
    n = int(input('km/h para m/s - 1\nm/s para km/h - 2\nFinalizar - 3\n'))

    if n == 1:
        km = int(input('Digite a velocidade em km/h: '))
        print(f'Essa velocidade em m/s é {km / 3.6} m/s')
        print('-' * 20)
    elif n == 2:
        m = int(input('Digite a velocidade em m/s: '))
        print(f'Essa velocidade em km/h é {m * 3.6} km/h')
        print('-' * 20)
    elif n == 3:
        break
    else:
        print('Número inválido!')
