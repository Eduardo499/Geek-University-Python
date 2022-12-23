numero = int(input('Digite um número inteiro positivo: '))
soma = 0

if numero > 0:
    for num in range(1, numero + 1):
        soma += num

else:
    print('Digite um número inteiro positivo')

print(f'A soma dos {numero} primeiros números naturais é {soma}')
