def posicao_substring(string, substring):
    """Função que recebe uma string e uma substring e retorna a posição onde foi encontrada a substring, caso ela não
    for encontra a função retorna -1 """

    tipo_string = True

    if not type(string) == str and type(substring) == str:
        tipo_string = False

    if tipo_string:

        try:
            posicao = string.index(substring)
            return posicao

        except ValueError:
            return -1

    return -1


texto = """Na cidade, a lua:
a joia branca que boia
na lama da rua."""

substring = 'lua'

print(f'A palavra "{substring}" foi encontrada na posição: {posicao_substring(texto, substring)}')
