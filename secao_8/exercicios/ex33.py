def soma_algarismo_fatorial(n):
    """Função que recebe um número e retorna a soma dos algarismos de seu fatorial"""

    fatorial = 1
    lista = []

    if n > 0 and type(n) == int:
        for i in range(n, 1, -1):
            fatorial *= i

        numero = str(fatorial)

        for i in numero:
            lista.append(int(i))

        return sum(lista)
    else:
        print('Valor inválido!')


print(soma_algarismo_fatorial(4))
