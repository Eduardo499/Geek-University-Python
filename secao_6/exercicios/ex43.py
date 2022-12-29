soma = 0
cont = 0

while True:
    idade = int(input('Digite a idade: '))

    if idade > 0:
        soma += idade
        cont += 1
    else:
        break
print(f'A média de idades é {soma / cont}')
