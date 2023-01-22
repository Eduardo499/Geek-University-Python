def ler_dados():
    """Função que ler idade, sexo, cor do cabelo e cor dos olhos e os armazena em uma lista"""

    habitantes = []

    for i in range(5):
        informacoes = []

        sexo = ''
        while not (sexo == 'masculino' or sexo == 'feminino'):
            sexo = str(input(f'Digite o sexo do habitante {i + 1} (masculino ou feminino): '))
            sexo = sexo.lower()
        informacoes.append(sexo)

        cor_olhos = ''
        while not (cor_olhos == 'azuis' or cor_olhos == 'castanhos'):
            cor_olhos = str(input(f'Digite a cor dos olhos do habitante {i + 1} (azuis ou castanhos): '))
            cor_olhos = cor_olhos.lower()
        informacoes.append(cor_olhos)

        cor_cabelo = ''
        while not (cor_cabelo == 'louros' or cor_cabelo == 'preto' or cor_cabelo == 'castanhos'):
            cor_cabelo = str(input(f'Digite a cor do cabelo do habitante {i + 1} (louros, preto ou castanhos: '))
            cor_cabelo = cor_cabelo.lower()
        informacoes.append(cor_cabelo)

        idade = int(input(f'Digite a idade do habitante {i + 1}: '))
        informacoes.append(idade)

        print()

        habitantes.append(informacoes)
    return habitantes


def media(args):
    """Função que recebe uma matriz com as informações de todos os habitantes e imprime a média de idade das pessoas
    com olhos castanhos e cabelos pretos """

    dados1 = True

    if len(args) == 5:
        for i in range(len(args)):
            if len(args[i]) != 4:
                dados1 = False
    else:
        dados1 = False

    if dados1:
        soma_idade = 0
        qtd = 0

        for i in range(5):

            if args[i][1] == 'castanhos':
                if args[i][2] == 'preto':
                    soma_idade += args[i][3]
                    qtd += 1

        if int(soma_idade / qtd) != 0:
            print(f'Média de idade de pessoas com olhos castanhos e cabelos pretos: {int(soma_idade / qtd)}')
        else:
            print('Não existe ninguém com olhos castanhos e cabelos pretos nesta lista')

    else:
        print('Dados inválidos')


def maior_idade(args):
    """Função que recebe uma matriz com as informações de todos os habitantes e retorna a maior idade"""

    dados2 = True

    if len(args) == 5:
        for i in range(len(args)):
            if len(args[i]) != 4:
                dados2 = False
    else:
        dados2 = False

    if dados2:
        maior = []

        for i in range(5):
            maior.append(args[i][3])

        return max(maior)


def qtd_individuos(args):
    """Função que recebe uma matriz com as informações de todos os habitantes e retorna a quantidade de indivíduos do
    sexo feminino cuja idade está entre 18 e 35 e que tenham olhos azuis e cabelos louros """

    dados3 = True

    if len(args) == 5:
        for i in range(len(args)):
            if len(args[i]) != 4:
                dados3 = False
    else:
        dados3 = False

    if dados3:
        quantidade = 0

        for i in range(5):
            if args[i][0] == 'feminino' and args[i][1] == 'azuis':
                if args[i][2] == 'louros' and 18 <= args[i][3] <= 35:
                    quantidade += 1

        return quantidade


dados = ler_dados()
media(dados)
print(f'A maior idade entre os habitantes é {maior_idade(dados)}')
print(f'Quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 e que tenham olhos azuis e cabelos '
      f'louros: {qtd_individuos(dados)}')
