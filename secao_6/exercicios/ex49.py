carlos = 3000
joao = carlos / 3

for i in range(1, 100):
    carlos += carlos * 0.02
    joao += joao * 0.05

    if joao >= carlos:
        print(f'Salário de Carlos: R$ {carlos}')
        print(f'Salário de João: R$ {joao}')
        print(f'Em {i} meses o salário de João igualou ou ultrapassou o de Carlos')
        break
