def comparar(string1, string2):
    """Função que recebe duas string e compara se elas são iguais ou diferentes"""

    if type(string1) == str and type(string2) == str:

        if string1 == string2:
            return 'Iguais'
        return 'Diferentes'


texto1 = 'Teste igual'
texto2 = 'Teste igual'

print(f'Os dois textos são iguais ou diferentes? {comparar(texto1, texto2)}')
