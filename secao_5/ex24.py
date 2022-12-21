valor = int(input('Digite o valor do produto: '))
estado = int(input("""Selecione o estado:
1 - MG
2 - SP
3 - RJ
4 - MS
"""))
if estado == 1:
    print(f'O valor do produto com os impostos é {valor * 1.07}')
elif estado == 2:
    print(f'O valor do produto com os impostos é {valor * 1.12}')
elif estado == 3:
    print(f'O valor do produto com os impostos é {valor * 1.15}')
elif estado == 4:
    print(f'O valor do produto com os impostos é {valor * 1.08}')
else:
    print('Estado inválido!')
