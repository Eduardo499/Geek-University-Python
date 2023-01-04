a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

if 0 < a < 10000 and 0 < b < 10000:
    algarismo1 = str(a)
    algarismo2 = str(b)

    tamanho1 = len(algarismo1)
    tamanho2 = len(algarismo2)

    lista1 = []
    lista2 = []

    lista1.append(int(algarismo1[tamanho1 - 1]))

    for i in range(int(tamanho1 - 1)):
        lista1.append(int(algarismo1[i]))

    lista2.append(int(algarismo2[tamanho2 - 1]))

    for i in range(int(tamanho2 - 1)):
        lista2.append(int(algarismo2[i]))

    soma = [0, 0, 0, 0, 0]

    for i in range(4):
        if len(lista1) > i and len(lista2) > i:
            soma[i] += int(lista1[i] + lista2[i])

            if soma[i] > 10:
                soma[i] -= 10
                soma[i + 1] += 1

        if not len(lista1) > i and len(lista2) > i:
            soma[i] += int(lista2[i])

        if len(lista1) > i and not len(lista2) > i:
            soma[i] += int(lista1[i])

    if len(lista1) >= len(lista2):
        while len(soma) > len(lista1):
            if soma[-1] == 0:
                soma.pop()
            else:
                break
    elif len(lista2) >= len(lista1):
        while len(soma) > len(lista2):
            if soma[-1] == 0:
                soma.pop()
            else:
                break

    print()
    print(f'Lista 1: {lista1}')
    print(f'Lista 2: {lista2}')
    print(f'Soma das listas: {soma}')
else:
    print('O número deve ser positivo e menor que 10.000')
