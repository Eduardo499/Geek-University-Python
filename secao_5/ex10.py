altura = float(input('Digite sua altura: '))
sexo = str(input('Digite seu sexo [M/F]: '))
if sexo == 'M' or sexo == 'm':
    print(f'Seu peso ideal é {(72.7 * altura) - 58} Kg')
elif sexo == 'F' or sexo == 'f':
    print(f'Seu peso ideal é {(62.1 * altura) - 44.7} Kg')
else:
    print('Sexo inválido!')
