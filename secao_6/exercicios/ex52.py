valor_saque = int(input('Digite o valor do saque: '))

if valor_saque > 0:
    cont200 = 0
    cont100 = 0
    cont50 = 0
    cont20 = 0
    cont10 = 0
    cont5 = 0
    cont2 = 0
    cont1 = 0

    while True:
        if valor_saque - 200 >= 0:
            valor_saque -= 200
            cont200 += 1
        elif valor_saque - 100 >= 0:
            valor_saque -= 100
            cont100 += 1
        elif valor_saque - 50 >= 0:
            valor_saque -= 50
            cont50 += 1
        elif valor_saque - 20 >= 0:
            valor_saque -= 20
            cont20 += 1
        elif valor_saque - 10 >= 0:
            valor_saque -= 10
            cont10 += 1
        elif valor_saque - 5 >= 0:
            valor_saque -= 5
            cont5 += 1
        elif valor_saque - 2 >= 0:
            valor_saque -= 2
            cont2 += 1
        elif valor_saque - 1 >= 0:
            valor_saque -= 1
            cont1 += 1
        else:
            print(f'Notas de 200 = {cont200}')
            print(f'Notas de 100 = {cont100}')
            print(f'Notas de 50 = {cont50}')
            print(f'Notas de 20 = {cont20}')
            print(f'Notas de 10 = {cont10}')
            print(f'Notas de 5 = {cont5}')
            print(f'Notas de 2 = {cont2}')
            print(f'Notas de 1 = {cont1}')
            break
else:
    print('Valor de saque inválido')
