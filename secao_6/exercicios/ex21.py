n1 = int(input('Digite o número inicial: '))
n2 = int(input('Digite o número final: '))
soma = 0
multi = 1

for num in range(n1, n2 + 1):
    print(num)
    if num % 2 == 0:
        soma += num
    else:
        multi *= num
print(f'A soma dos números pares desse intervalo é {soma}')
print(f'O produto dos números ímpares desse intervalo é {multi}')
