def exp(x, y):
    """Função que recebe dois números e retorna o valor de x ** y"""

    return x ** y


a = int(input('Digite um número: '))
b = int(input(f'Digite um número para ser o expoente de {a}: '))
print()
print(exp(a, b))
