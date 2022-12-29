chico = 1.50
ze = 1.10

for i in range(100):
    chico += 0.02
    ze += 0.03

    if ze > chico:
        print(f'Chico = {chico} metros')
        print(f'Zé = {ze} metros')
        print(f'Necessita de {i} anos para Zé ultrapassar Chico')
        break
