km = int(input('Digite a distância percorrida em Km: '))
litro = int(input('Digite a quantidade de litros de gasolinas gastos: '))
consumo = km / litro
if consumo < 8:
    print('Venda o carro!')
elif 8 <= consumo <= 14:
    print('Econômico!')
elif consumo > 14:
    print('Super econômico!')
