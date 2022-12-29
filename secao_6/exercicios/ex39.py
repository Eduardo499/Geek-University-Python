base = int(input('Digite a medida da base: '))
altura = int(input('Digite a medida da altura: '))

if base > 0 and altura > 0:
    print(f'Área = {(base * altura) / 2}')
else:
    print('Valores inválidos')
