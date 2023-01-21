def uniao(args_a, args_b):
    """Função que recebe dois vetores com 10 elementos e retorna um vetor sendo a união entre eles"""

    tamanho_a = True
    tamanho_b = True

    for i in range(len(args_a)):
        if not len(args_a) == 10:
            tamanho_a = False
        if not type(args_a[i]) == int:
            tamanho_a = False

    for i in range(len(args_b)):
        if not len(args_b) == 10:
            tamanho_b = False
        if not type(args_b[i]) == int:
            tamanho_b = False

    if tamanho_a and tamanho_b:

        conjunto_a = set(args_a)
        conjunto_b = set(args_b)

        vetor_uniao = list(conjunto_a.union(conjunto_b))

        return vetor_uniao


vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(uniao(vetor1, vetor2))
