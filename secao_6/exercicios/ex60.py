soma = 0
cont = 0
maior = 0
menor = 0
soma_pares = 0
cont_pares = 0

while True:
    n = int(input('Digite um número: '))

    if n != 0:
        if cont == 0:
            menor = n
            maior = n

        soma += n
        cont += 1

        if n > maior:
            maior = n
        elif n < menor:
            menor = n

        if n % 2 == 0:
            cont_pares += 1
            soma_pares += n
    else:
        break

if cont_pares == 0:
    cont_pares = 1

print()
print(f'A soma dos números digitados foi {soma}')
print(f'Foram digitados {cont} números')
print(f'A média dos números digitados é {soma / cont}')
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
print(f'A média dos números pares digitados foi {soma_pares / cont_pares}')
