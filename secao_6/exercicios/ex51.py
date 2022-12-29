ano_atual = 2022
ano_inicial = 1995
aumento = 1.5

for i in range(ano_inicial, ano_atual + 1):
    salario = 2000

    if i == ano_inicial:
        pass
    elif ano_inicial < i < ano_atual:
        salario += salario * (aumento / 100)
        aumento *= 2
    elif i == ano_atual:
        salario += salario * (aumento / 100)
        print(f'Salário = {salario}')
