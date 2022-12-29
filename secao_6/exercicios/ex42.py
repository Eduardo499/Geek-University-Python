while True:
    n = int(input('Digite um número: '))

    if n > 0:
        print(f'{n}² = {n ** 2}')
        print(f'{n}³ = {n ** 3}')
        print(f'Raiz quadrada de {n} = {n ** 0.5}')
    else:
        break
