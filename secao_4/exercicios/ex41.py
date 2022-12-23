valor_hora = int(input('Digite o valor da hora de trabalho: '))
hora_dia = int(input('Digite a hora trabalhada por dia: '))
hora_mes = hora_dia * 30
valor = (valor_hora * hora_mes) * 1.10
print(f'O valor a ser pago é {valor} reais')
