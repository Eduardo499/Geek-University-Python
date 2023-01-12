def data(dia, mes, ano):
    """Uma função que tem como parâmetro o dia, o mês e o ano e retorna uma lista, com o dia, mês em extenso e o ano"""
    lista = []

    if mes == 1:
        if 1 <= dia <= 31:
            lista.append(dia)
            lista.append('Janeiro')
            lista.append(ano)
        else:
            print('Dia inválido!')
    elif mes == 2:
        if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
            if 1 <= dia <= 29:
                lista.append(dia)
                lista.append('Fevereiro')
                lista.append(ano)
            else:
                print('Dia inválido!')
        else:
            if 1 <= dia <= 28:
                lista.append(dia)
                lista.append('Fevereiro')
                lista.append(ano)
            else:
                print('Dia inválido!')
    elif mes == 3:
        if 1 <= dia <= 31:
            lista.append(dia)
            lista.append('Março')
            lista.append(ano)
        else:
            print('Dia inválido!')
    elif mes == 4:
        if 1 <= dia <= 30:
            lista.append(dia)
            lista.append('Abril')
            lista.append(ano)
        else:
            print('Dia inválido!')
    elif mes == 5:
        if 1 <= dia <= 31:
            lista.append(dia)
            lista.append('Maio')
            lista.append(ano)
        else:
            print('Dia inválido!')
    elif mes == 6:
        if 1 <= dia <= 30:
            lista.append(dia)
            lista.append('Junho')
            lista.append(ano)
        else:
            print('Dia inválido!')
    elif mes == 7:
        if 1 <= dia <= 31:
            lista.append(dia)
            lista.append('Julho')
            lista.append(ano)
        else:
            print('Dia inválido!')
    elif mes == 8:
        if 1 <= dia <= 31:
            lista.append(dia)
            lista.append('Agosto')
            lista.append(ano)
        else:
            print('Dia inválido!')
    elif mes == 9:
        if 1 <= dia <= 30:
            lista.append(dia)
            lista.append('Setembro')
            lista.append(ano)
        else:
            print('Dia inválido!')
    elif mes == 10:
        if 1 <= dia <= 31:
            lista.append(dia)
            lista.append('Outubro')
            lista.append(ano)
        else:
            print('Dia inválido!')
    elif mes == 11:
        if 1 <= dia <= 30:
            lista.append(dia)
            lista.append('Novembro')
            lista.append(ano)
        else:
            print('Dia inválido!')
    elif mes == 12:
        if 1 <= dia <= 31:
            lista.append(dia)
            lista.append('Dezembro')
            lista.append(ano)
        else:
            print('Dia inválido!')
    else:
        print('Mês inválido')

    return lista


dia, mes, ano = data(12, 1, 2022)

print(f'Hoje é {dia} de {mes} de {ano}')
