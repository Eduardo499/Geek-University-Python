def intercalar(str1, str2):
    """Função que recebe duas string e retorna a intercalação letra a letra da primeira com a segunda"""

    if type(str1) == str and type(str2) == str:
        inter = ''

        if len(str1) <= len(str2):
            for i in range(len(str1)):
                inter += str1[i] + str2[i]
        else:
            for i in range(len(str2)):
                inter += str1[i] + str2[i]

        return inter


texto1 = 'Geek'
texto2 = 'University'

print(intercalar(texto1, texto2))
