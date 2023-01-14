def desenha_linha(x):
    """Função que recebe um número e retorna '=' vezes o tanto que o usuário digitou"""
    return '=' * x


num = int(input("Digite quantas vezes você deseja repetir o sinal '=': "))
print()
print(desenha_linha(num))
