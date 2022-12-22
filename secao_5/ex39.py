salario = int(input('Digite seu salário: '))
tempo = int(input('Digite seu tempo de serviço: '))

if salario <= 500:
    if tempo < 1:
        print('Sem bônus')
        print(f'Seu salário com o reajuste é de R$ {salario * 1.25}')
    elif 1 <= tempo <= 3:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.25 + 100}')
    elif 4 <= tempo <= 6:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.25 + 200}')
    elif 7 <= tempo <= 10:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.25 + 300}')
    elif tempo > 10:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.25 + 500}')
elif 500 < salario <= 1000:
    if tempo < 1:
        print('Sem bônus')
        print(f'Seu salário com o reajuste é de R$ {salario * 1.20}')
    elif 1 <= tempo <= 3:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.20 + 100}')
    elif 4 <= tempo <= 6:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.20 + 200}')
    elif 7 <= tempo <= 10:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.20 + 300}')
    elif tempo > 10:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.20 + 500}')
elif 1000 < salario <= 1500:
    if tempo < 1:
        print('Sem bônus')
        print(f'Seu salário com o reajuste é de R$ {salario * 1.15}')
    elif 1 <= tempo <= 3:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.15 + 100}')
    elif 4 <= tempo <= 6:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.15 + 200}')
    elif 7 <= tempo <= 10:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.15 + 300}')
    elif tempo > 10:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.15 + 500}')
elif 1500 < salario <= 2000:
    if tempo < 1:
        print('Sem bônus')
        print(f'Seu salário com o reajuste é de R$ {salario * 1.10}')
    elif 1 <= tempo <= 3:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.10 + 100}')
    elif 4 <= tempo <= 6:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.10 + 200}')
    elif 7 <= tempo <= 10:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.10 + 300}')
    elif tempo > 10:
        print(f'Seu salário com o reajuste é de R$ {salario * 1.10 + 500}')
elif salario > 2000:
    print('Sem reajuste')
    if tempo < 1:
        print('Sem bônus')
    elif 1 <= tempo <= 3:
        print(f'Seu salário com o bônus é de R$ {salario + 100}')
    elif 4 <= tempo <= 6:
        print(f'Seu salário com o bônus é de R$ {salario + 200}')
    elif 7 <= tempo <= 10:
        print(f'Seu salário com o bônus é de R$ {salario + 300}')
    elif tempo > 10:
        print(f'Seu salário com o bônus é de R$ {salario + 500}')
