salario = int(input('Digite seu salário: '))
parcela = int(input('Digite o valor da prestação: '))
if parcela > salario * 0.20:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
