peso = float(input('Digitie seu peso: '))
altura = float(input('Digitie sua altura: '))
if peso <= 60:
    if altura < 1.20:
        print('A')
    elif 1.20 <= altura <= 1.70:
        print('B')
    elif altura > 1.70:
        print('C')
elif 60 < peso <= 90:
    if altura < 1.20:
        print('D')
    elif 1.20 <= altura <= 1.70:
        print('E')
    elif altura > 1.70:
        print('F')
elif peso > 90:
    if altura < 1.20:
        print('G')
    elif 1.20 <= altura <= 1.70:
        print('H')
    elif altura > 1.70:
        print('I')
