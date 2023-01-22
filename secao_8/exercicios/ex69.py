def cria_fracao():
    """Função que cria uma fração a partir de dados digitados durante a execução da mesma e retorna o numerador e o
    denominador de duas frações """

    numerador1 = int(input('Digite o numerador da primeira fração: '))
    denominador1 = int(input('Digite o denominador da primeira fração: '))

    numerador2 = int(input('Digite o numerador da segunda fração: '))
    denominador2 = int(input('Digite o denominador da segunda fração: '))
    print()

    return numerador1, denominador1, numerador2, denominador2


def simplifica_fracao(numerador, denominador):
    """Função que recebe o numerador e o denominador de uma fração e os simplifica encontrando seu Máximo Divisor
    Comum (MDC) """

    if denominador > 0:
        for i in range(denominador, 0, -1):
            if numerador % i == 0 and denominador % i == 0:
                return int(numerador / i), int(denominador / i)


def calculo_fracoes(numerador1, denominador1, numerador2, denominador2):
    """Função que recebe o numerador e o denominador de duas frações e faz operações como soma, subtração,
    multiplicação e divisão """

    # Soma
    soma_numerador = (numerador1 * denominador2 + numerador2 * denominador1)
    soma_denominador = denominador1 * denominador2
    soma_numerador_simplificado, soma_denominador_simplificado = simplifica_fracao(soma_numerador, soma_denominador)
    print(
        f'{numerador1} / {denominador1} + {numerador2} / {denominador2} = {soma_numerador_simplificado} / {soma_denominador_simplificado}')
    print()

    # Subtração
    sub_numerador = (numerador1 * denominador2 - numerador2 * denominador1)
    sub_denominador = denominador1 * denominador2
    sub_numerador_simplificado, sub_denominador_simplificado = simplifica_fracao(sub_numerador, sub_denominador)
    print(
        f'{numerador1} / {denominador1} - {numerador2} / {denominador2} = {sub_numerador_simplificado} / {sub_denominador_simplificado}')
    print()

    # Multiplicação
    mult_numerador = numerador1 * numerador2
    mult_denominador = denominador1 * denominador2
    mult_numerador_simplificado, mult_denominador_simplificado = simplifica_fracao(mult_numerador, mult_denominador)
    print(f'{numerador1} / {denominador1} * {numerador2} / {denominador2} = {mult_numerador_simplificado} / {mult_denominador_simplificado} ')
    print()

    # Divisão
    div_numerador = numerador1 * denominador2
    div_denominador = denominador1 * numerador2
    div_numerador_simplificado, div_denominador_simplificado = simplifica_fracao(div_numerador, div_denominador)
    print(
        f'{numerador1} / {denominador1} / {numerador2} / {denominador2} = {div_numerador_simplificado} / {div_denominador_simplificado} ')
    print()


# Cria as duas frações
num1, den1, num2, den2 = cria_fracao()

# Simplifica as duas frações
num1_simplificado, den1_simplificado = simplifica_fracao(num1, den1)
num2_simplificado, den2_simplificado = simplifica_fracao(num2, den2)

# Imprime as frações simplificadas
print(f'{num1} / {den1} = {num1_simplificado} / {den1_simplificado}')
print()
print(f'{num2} / {den2} = {num2_simplificado} / {den2_simplificado}')
print()

# Faz as operações matemáticas
calculo_fracoes(num1, den1, num2, den2)
