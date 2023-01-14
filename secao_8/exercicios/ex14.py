def kilometros_litros(km, l):
    """Função que recebe uma distância em Km e o consumo em Litros e calcula o Km/L"""

    consumo = km/l

    if consumo < 8:
        return 'Venda o carro!'
    elif 8 <= consumo <= 12:
        return 'Econômico!'
    elif consumo > 12:
        return 'Super econômico!'


kilometros = int(input('Digite a distância percorrida em Km: '))
litros = int(input('Digite o consumo em Litros: '))

print(kilometros_litros(kilometros, litros))
