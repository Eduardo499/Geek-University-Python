def getchar():
    """Função que retorna o caracter informado"""

    caractere = input('Digite um caractere: ')

    if len(caractere) <= 1:
        return caractere


def rotina(args, tamanho):
    """Função que recebe um vetor e seu tamanho e o preenche até atingir seu tamanho máximo"""

    for _ in range(tamanho):

        valor = getchar()

        if valor != '':
            args.append(valor)
        else:
            break

    return args


vetor = []
tam = 10

print(f'{rotina(vetor, tam)}')
