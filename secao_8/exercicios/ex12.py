def soma_algarismo(num):
    """Função que recebe um número e retorna a soma dos algarismos"""
    soma = []
    numero = str(num)
    for i in numero:
        soma.append(int(i))
    return sum(soma)


n = int(input('Digite um número maior que zero: '))

if n > 0:
    print(f'A soma dos algarismos de {n} é {soma_algarismo(n)}')
else:
    print('Número inválido!')
