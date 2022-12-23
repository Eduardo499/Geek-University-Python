nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
if 0 <= nota_1 <= 10 and 0 <= nota_2 <= 10:
    print(f'A média é {(nota_1 + nota_2) / 2}')
else:
    print('Nota (s) inválida (s)')
