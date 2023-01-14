def operacao(n1, n2, sb):
    """Função que recebe dois números e um símbolo e retorna a operação realizada pelo mesmo"""

    if sb == '+':
        return n1 + n2
    elif sb == '-':
        return n1 - n2
    elif sb == '*':
        return n1 * n2
    elif sb == '/':
        return n1 / n2
    else:
        return 'Operação inválida!'


num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print()
simbolo = str(input("""Escolha uma dessas operações:
+ -> Soma
- -> Subtração
* -> Multiplicação
/ -> Divisão
"""))
print()
print(operacao(num1, num2, simbolo))
