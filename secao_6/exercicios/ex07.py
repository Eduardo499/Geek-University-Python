soma = 0
for num in range(1, 11):
    numero = int(input(f'Digite o número {num}/10: '))
    if numero > 0:
        soma += numero
    else:
        pass
print(f'A média desses números é {soma / 10}')
