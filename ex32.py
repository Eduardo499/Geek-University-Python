def simplifica(numerador, denominador):
    """Função que recebe o numerador e o denominador de uma fração e simplica, exemplo: 8/16 = 1/2"""

    if denominador > 0:
        for i in range(denominador, 1, -1):

            if numerador % i == 0 and denominador % i == 0:
                numerador = int(numerador / i)
                denominador = int(denominador / i)

                break

        return numerador, denominador
    else:
        print('Impossível dividir por zero')


numerador1 = int(input('Digite o valor do numerador: '))
denominador1 = int(input('Digite o valor do denominador: '))

numerador_simples, denominador_simples = simplifica(numerador1, denominador1)

print()
print(f'Fração Original: {numerador1}/{denominador1}')
print(f'Fração Simplificada: {numerador_simples}/{denominador_simples}')
