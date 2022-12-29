while True:
    r1 = int(input('Digite o valor do resistor 1: '))
    r2 = int(input('Digite o valor do resistor 2: '))

    if r1 != 0 and r2 != 0:
        r = (r1 * r2) / (r1 + r2)
        print(f'A associação em paralelo é {r}')
    else:
        break
