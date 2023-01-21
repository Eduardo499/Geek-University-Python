def anagrama(frase1, frase2):
    """Função que recebe duas frases e retorna True se as duas for anagrama ou False se não forem"""

    if type(frase1) == str and type(frase2) == str:

        a = True

        for i in range(len(frase1)):
            if frase1.count(frase1[i]) == frase2.count(frase1[i]):
                pass
            else:
                a = False

        if a:
            return True

    return False


texto1 = 'Teste'
texto2 = 'esteT'

print(f"'{texto1}' é anagrama de '{texto2}'? {anagrama(texto1, texto2)}")
