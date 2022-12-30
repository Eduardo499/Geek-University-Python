numero_habitante = int(input('Digite o número de habitantes: '))
kwh = int(input('Digite o valor do kwh: '))

menor = 0
maior = 0
cont = 0

residencial = 0
comercial = 0
industrial = 0

for i in range(1, numero_habitante + 1):
    consumo_mes = int(input('Digite o consumo do mês: '))
    codigo_consumidor = int(input('Digite o código do consumidor: '))

    if consumo_mes >= 0:
        if 1 <= codigo_consumidor <= 3:
            cont += 1

            if i == 1:
                menor = consumo_mes

            if consumo_mes > maior:
                maior = consumo_mes
            elif consumo_mes < menor:
                menor = consumo_mes

            if codigo_consumidor == 1:
                residencial += consumo_mes
            elif codigo_consumidor == 2:
                comercial += consumo_mes
            elif codigo_consumidor == 3:
                industrial += consumo_mes


        else:
            print('Código inválido')
    else:
        print('Valor de consumo inválido')

print(f'O maior consumo foi {maior}')
print(f'O menor consumo foi {menor}')
print(f'A média de consumo foi {(residencial + comercial + industrial) / cont}')
print(f'Total consumido por residencial: {residencial}')
print(f'Total consumido por comercial: {comercial}')
print(f'Total consumido por industrial: {industrial}')
