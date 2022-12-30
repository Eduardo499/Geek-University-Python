a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))


if a > 0 and b > 0:
    soma = 0
    cont_primos = 0

    for i in range(a, b + 1):
        cont = 0
        for c in range(1, i + 1):
            if i % 1 == 0 and i % c == 0:
                cont += 1
        if cont_primos <= b:
            if cont <= 2:
                cont_primos += 1
                soma += c
                print(c)

        else:
            break
    print()
    print(f'No intervalo fechado [{a}, {b}] existem {cont_primos} números primos')
    print(f'A soma entres eles é {soma}')
else:
    print('O número deve ser maior que zero')
