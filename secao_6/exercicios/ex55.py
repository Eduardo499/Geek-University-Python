n = int(input('Digite um número: '))


if n > 0:
    soma = 0
    cont_primos = 0
    for i in range(1, n ** 3):
        cont = 0
        for c in range(1, i + 1):
            if i % 1 == 0 and i % c == 0:
                cont += 1
        if cont_primos <= n:
            if cont <= 2:
                soma += i
                cont_primos += 1
                print(c)
        else:
            break
    print(f'A soma dos {n} primeiros números primos é {soma}')
else:
    print('O número deve ser maior que um')
