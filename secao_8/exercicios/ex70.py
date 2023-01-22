def reduz(a, b):
    """Função que recebe o numerador 'a' e o denominador 'b' e retorna seu racional, os dois número devem ser
    inteiros """

    if type(a) == int and type(b) == int:
        if a > 0 and b > 0:
            return a / b


def neg(x):
    """Função que recebe um número x e retorna -x"""

    if type(x) == int or type(x) == float:
        if x > 0:
            return x * (-1)


def soma(x, y):
    """Função que recebe dois números x e y e retorna x + y"""

    if type(x) == int or type(x) == float and type(y) == int or type(y) == float:
        if x > 0 and y > 0:
            return x + y


def produto(x, y):
    """Função que recebe dois números x e y e retorna x * y"""

    if type(x) == int or type(x) == float and type(y) == int or type(y) == float:
        if x > 0 and y > 0:
            return x * y


def quociente(x, y):
    """Função que recebe dois números x e y e retorna x / y"""

    if type(x) == int or type(x) == float and type(y) == int or type(y) == float:
        if x > 0 and y > 0:
            return x / y


num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

print(f'\nO Racional de {num1} / {num2} = {reduz(num1, num2)}')
print(f'Número {num1} negativo = {neg(num1)}')
print(f'Número {num2} negativo = {neg(num2)}')
print(f'Soma de {num1} + {num2} = {soma(num1, num2)}')
print(f'Produto de {num1} * {num2} = {produto(num1, num2)}')
print(f'Quociente de {num1} / {num2} = {quociente(num1, num2)}')
