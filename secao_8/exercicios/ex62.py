def comprimento_string(string):
    """Função que recebe uma string e retorna seu comprimento"""

    if type(string) == str:
        return len(string)


texto = 'Teste realizado com sucesso!'

print(comprimento_string(texto))
