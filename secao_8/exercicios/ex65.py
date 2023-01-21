def concatenar(string1, string2, n):
    """Função que recebe duas string e um número n e as concatena até n caracteres"""

    if type(string1) == str and type(string2) == str:
        if type(n) == int and n > 0:
            return string1 + string2[:n:]


texto1 = 'Conca'
texto2 = 'tenação'
n = 5

print(concatenar(texto1, texto2, n))
