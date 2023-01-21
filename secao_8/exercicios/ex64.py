def concatenar(string1, string2):
    """Função que recebe duas string e as concatena"""

    if type(string1) == str and type(string2) == str:
        return string1 + string2


texto1 = 'Conca'
texto2 = 'tenação'

print(concatenar(texto1, texto2))
