preco_antigo = int(input('Digite o preço antigo: '))
if preco_antigo <= 50:
    preco_novo = preco_antigo * 1.05
elif 50 < preco_antigo <= 100:
    preco_novo = preco_antigo * 1.10
elif preco_antigo > 100:
    preco_novo = preco_antigo * 1.15

if preco_novo <= 80:
    print(preco_novo)
    print('Barato')
elif 80 < preco_novo <= 120:
    print(preco_novo)
    print('Normal')
elif 120 < preco_novo <= 200:
    print(preco_novo)
    print('Caro')
elif preco_novo > 200:
    print(preco_novo)
    print('Muito Caro')
