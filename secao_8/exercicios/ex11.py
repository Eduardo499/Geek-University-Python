def media(n1, n2, n3, letra):
    """Função que recebe três notas de um aluno e retorna a média aritmética se a letra for A ou a média ponderada se
    a letra for P """

    if letra == 'A' or letra == 'a':
        return (n1 + n2 + n3) / 3
    elif letra == 'P' or letra == 'p':
        return (n1 * 5 + n2 * 3 + n3 * 2) / 3
    else:
        return 'Letra inválida!'


print(media(6, 5, 9, 'a'))
