qtd = int(input('Digite quantas vezes você quer que o algorítimo leia: '))
maior = 0
repeticao = 0

for num in range(1, qtd + 1):
    numero = int(input(f'Digite o {num}° número: '))

    if num == 1:
        maior = numero
        repeticao = 1
    elif numero > maior:
        maior = numero
    elif numero == maior:
        repeticao += 1

print(f'O maior número digitado foi {maior}')
print(f'O número {maior} repetiu {repeticao} vezes')
