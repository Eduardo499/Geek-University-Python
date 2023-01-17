def troque(a, b):
    """Função que recebe duas variáveis 'a' e 'b' e retorna as mesmas porém com ordem inversa"""
    if type(a) == float and type(b) == float:
        return b, a


n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print(troque(n1, n2))
