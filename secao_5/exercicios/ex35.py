ano = int(input('Digite o ano: '))
mes = int(input('Digite o mês: '))
dia = int(input('Digite o dia: '))
if mes == 1:
    if 1 <= dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 2:
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        if 1 <= dia <= 29:
            print('Data válida')
        else:
            print('Data inválida')
    else:
        if 1 <= dia <= 28:
            print('Data válida')
        else:
            print('Data inválida')
elif mes == 3:
    if 1 <= dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 4:
    if 1 <= dia <= 30:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 5:
    if 1 <= dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 6:
    if 1 <= dia <= 30:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 7:
    if 1 <= dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 8:
    if 1 <= dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 9:
    if 1 <= dia <= 30:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 10:
    if 1 <= dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 11:
    if 1 <= dia <= 30:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 12:
    if 1 <= dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
else:
    print('Mês inválido')
