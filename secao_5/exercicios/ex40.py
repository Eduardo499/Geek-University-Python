fabrica = int(input('Digite o custo de fábrica: '))
if fabrica <= 12000:
    print(f'O custo ao consumidor é de R$ {fabrica * 1.05}')
elif 12000 < fabrica <= 25000:
    print(f'O custo ao consumidor é de R$ {fabrica * 1.25}')
elif fabrica > 25000:
    print(f'O custo ao consumidor é de R$ {fabrica * 1.35}')
