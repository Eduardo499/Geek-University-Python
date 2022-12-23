menor = 0
maior = 0
for num in range(1, 11):
    numero = int(input(f'Digite o número {num}/10:  '))
    if menor == 0 and maior == 0:
        menor = numero
        maior = num
    elif menor > numero:
        menor = numero
    elif maior < numero:
        maior = numero
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')
