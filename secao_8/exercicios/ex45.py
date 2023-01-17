def desvio_padrao(*args):
    """Função que recebe um vetor e calcula o desvio padrão"""

    v = [*args]
    m = sum(v) / len(v)
    dv = 0

    for i in v:
        dv += ((i - m) ** 2) / len(v)
    return dv ** 0.5


numeros = (1, 6, 4, 7, 8, 3, 2, 8, 7, 6)
print(desvio_padrao(*numeros))
