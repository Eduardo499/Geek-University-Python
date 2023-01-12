def verificador(numero):
    """Função que verifica se um número é positivo ou negativo, retorna 1 se for positivo, retonar -1 se negativo e 0
    se for zero """

    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    elif numero == 0:
        return 0


print(verificador(0))
