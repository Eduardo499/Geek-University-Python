from random import randint

n = int(input('Digite quantas vezes quer rolar os dados: '))

print()

for i in range(1, n + 1):
    print(f'Lançamento {i}/{n}')

    print()
    
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    print(f'Dado 1: {d1}')
    print(f'Dado 2: {d2}')

    if d1 > d2:
        print(f'{d1} é maior que {d2}')
    elif d2 > d1:
        print(f'{d2} é maior que {d1}')
    elif d1 == d2:
        print(f'Os dois dados são iguais, {d1} = {d2}')

    print('-------------------------------------')
    print()
