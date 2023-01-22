def soma(args1, args2):
    """Função que recebe dois vetores e retorna outro vetor, que é a soma entre os dois vetores"""

    elementos = True

    for i in args1:
        if not type(i) == int or type(i) == float:
            elementos = False

    for i in args2:
        if not type(i) == int or type(i) == float:
            elementos = False

    if elementos:
        novo_vetor = []

        if len(args1) >= len(args2):
            for i in range(len(args2)):
                novo_vetor.append(args1[i] + args2[i])

            for i in range(len(novo_vetor)), len(args1):
                novo_vetor.append(args1[i])

        elif len(args2) > len(args1):
            for i in range(len(args1)):
                novo_vetor.append(args1[i] + args2[i])

            for i in range(len(novo_vetor), len(args2)):
                novo_vetor.append(args2[i])

        return novo_vetor


vetor1 = [1, 2, 4, 5, 6, 7, 4, 3, 7, 8]
vetor2 = [2, 5, 6, 7, 3, 8, 4, 3, 5, 3, 5, 2]

print(f'Soma dos vetores = {soma(vetor1, vetor2)}')
