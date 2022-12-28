soma = 0

valor_inicial = int(input('Digite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))

if valor_inicial >= valor_final:
    print('Intervalo de valores inválido!')
else:
    for i in range(valor_inicial, valor_final + 1):
        if i % 2 == 1:
            soma += i

    print(f'A soma de todos os números ímpares no intervalo fechado [{valor_inicial}, {valor_final}] é {soma}')
