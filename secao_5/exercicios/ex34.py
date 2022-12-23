nota = float(input('Digite sua nota: '))
faltas = int(input('Digite a quantidade de faltas: '))
if faltas <= 20:
    if 9 <= nota <= 10:
        print('A')
    elif 7.5 <= nota <= 8.9:
        print('B')
    elif 5 <= nota <= 7.4:
        print('C')
    elif 4 <= nota <= 4.9:
        print('D')
    elif 0 <= nota <= 4.9:
        print('E')
elif faltas > 20:
    if 9 <= nota <= 10:
        print('B')
    elif 7.5 <= nota <= 8.9:
        print('C')
    elif 5 <= nota <= 7.4:
        print('D')
    elif 4 <= nota <= 4.9:
        print('E')
    elif 0 <= nota <= 4.9:
        print('E')
