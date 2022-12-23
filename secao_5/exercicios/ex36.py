valor = int(input('Digite o valor da venda: '))
if valor < 20000:
    print(f'Sua comissão é R$ {400 + valor * 0.14}')
elif 20000 <= valor < 40000:
    print(f'Sua comissão é R$ {500 + valor * 0.14}')
elif 40000 <= valor < 60000:
    print(f'Sua comissão é R$ {550 + valor * 0.14}')
elif 60000 <= valor < 80000:
    print(f'Sua comissão é R$ {600 + valor * 0.14}')
elif 80000 <= valor < 100000:
    print(f'Sua comissão é R$ {650 + valor * 0.14}')
elif valor >= 100000:
    print(f'Sua comissão é R$ {700 + valor * 0.16}')
