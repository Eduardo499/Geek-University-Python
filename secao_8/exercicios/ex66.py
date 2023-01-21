def maiusculo(string):
    """Função que recebe uma string e a retorna tudo em maiúsculo"""

    if type(string) == str:
        return string.upper()


texto = 'python'

print(maiusculo(texto))
