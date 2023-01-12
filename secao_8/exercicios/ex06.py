def segundos(hora, minuto, segundo):
    """Função que recebe hora, minuto e segundo e converte para segundos"""

    segundo += minuto * 60
    segundo += hora * 60 * 60

    return segundo


print(segundos(11, 18, 45))
