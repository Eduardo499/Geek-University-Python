codigo = int(input(print("""Cardápio:
Especificação - Código - Preço
Cachorro Quente - 100 - 1.20
Bauru Simples - 101 - 1.30
Bauru com Ovo - 102 - 1.50
Hamburguer - 103 - 1.20
Cheeseburguer - 104 - 1.70
Suco - 105 - 2.20
Refrigerante - 106 - 1.00
""")))
if codigo == 100:
    qtd = int(input('Digite a quantidade: '))
    print(f'O valor a ser pago é de R$ {qtd * 1.20}')
elif codigo == 101:
    qtd = int(input('Digite a quantidade: '))
    print(f'O valor a ser pago é de R$ {qtd * 1.30}')
elif codigo == 102:
    qtd = int(input('Digite a quantidade: '))
    print(f'O valor a ser pago é de R$ {qtd * 1.50}')
elif codigo == 103:
    qtd = int(input('Digite a quantidade: '))
    print(f'O valor a ser pago é de R$ {qtd * 1.20}')
elif codigo == 104:
    qtd = int(input('Digite a quantidade: '))
    print(f'O valor a ser pago é de R$ {qtd * 1.70}')
elif codigo == 105:
    qtd = int(input('Digite a quantidade: '))
    print(f'O valor a ser pago é de R$ {qtd * 2.20}')
elif codigo == 106:
    qtd = int(input('Digite a quantidade: '))
    print(f'O valor a ser pago é de R$ {qtd}')
else:
    print('Código inválido!')
