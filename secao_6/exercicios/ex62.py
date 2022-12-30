unidades = ['um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove']
dezenas_10 = ['onze', 'doze', 'treze', 'quartoze',
              'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dezenas = ['dez', 'vinte', 'trinta', 'quarenta',
           'ciquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
centenas = ['cento', 'duzentos', 'trezentos', 'quatrocentos',
            'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

cont = 0

for i in range(1, 1001):
    n = str(i)

    if len(n) == 1:
        cont_unidade = int(n[0])
        unidade = unidades[cont_unidade - 1]
        cont += len(unidade)
        print(unidades[cont_unidade - 1])

    elif len(n) == 2:
        if 10 < int(n) < 20:
            cont_unidade = int(n[1]) - 1
            dezena_10 = dezenas_10[cont_unidade]
            cont += len(dezena_10)
            print(dezenas_10[cont_unidade])
        else:
            if len(n[1]) == 0:
                cont_dezena = int[n[0]]
                dezena = dezenas[cont_dezena - 1]
                cont += len(dezena)
                print(dezenas[cont_dezena - 1])
            else:
                cont_dezena = int(n[0]) - 1
                cont_unidade = int(n[1]) - 1
                dezena = dezenas[cont_dezena]
                unidade = unidades[cont_unidade]

                cont += len(unidade) + 1 + len(dezena)
                print(dezenas[cont_dezena] + ' e ' + unidades[cont_unidade])
    elif len(n) == 3:
        if int(n) == 100:
            cont += len('cem')
            print('cem')
        elif int(n[0]) >= 1 and int(n[1]) >= 1 and int(n[2]) == 0:
            cont_centena = int(n[0]) - 1
            cont_dezena = int(n[1]) - 1
            centena = centenas[cont_centena]
            dezena = dezenas[cont_dezena]

            cont += len(centena) + 1 + len(dezena)
            print(centenas[cont_centena] + ' e ' + dezenas[cont_dezena])
        elif int(n[0]) >= 1 and int(n[1]) == 0 and int(n[2]) >= 1:
            cont_centena = int(n[0]) - 1
            cont_unidade = int(n[2]) - 1
            centena = centenas[cont_centena]
            unidade = unidades[cont_unidade]

            cont += len(centena) + 1 + len(unidade)
            print(centenas[cont_centena] + ' e ' + unidades[cont_unidade])
        elif int(n[0]) >= 1 and int(n[1]) >= 1 and int(n[2]) >= 1:
            if int(n[0]) >= 1 and int(n[1]) == 1:
                cont_centena = int(n[0]) - 1
                cont_dezena = int(n[2]) - 1
                centena = centenas[cont_centena]
                dezena = dezenas_10[cont_dezena]

                cont += len(centena) + 1 + len(dezena)
                print(centenas[cont_centena] + ' e ' + dezenas_10[cont_dezena])
            else:
                cont_centena = int(n[0]) - 1
                cont_dezena = int(n[1]) - 1
                cont_unidade = int(n[2]) - 1
                centena = centenas[cont_centena]
                dezena = dezenas[cont_dezena]
                unidade = unidades[cont_unidade]

                cont += len(centena) + 1 + len(dezena) + 1 + len(unidade)
                print(centenas[cont_centena] + ' e ' + dezenas[cont_dezena] + ' e ' + unidades[cont_unidade])

    elif len(n) == 4:

        cont += len('mil')
        print('mil')

print(f'Entre 1 e 1000 existem {cont} letras')
