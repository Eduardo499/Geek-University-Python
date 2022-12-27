lista = []
l = []

multiplo_i = 0
multiplo_j = 0

n = int(input('Digite um número: '))
i = int(input('Digite outro número: '))
j = int(input('Digite o último número: '))

# Verifica se i e j é maior que zero
if i > 0 and j > 0:

    # Encontra os n primeiros multiplos de i e j
    for c in range(0, n + 1):
        multiplo_i = c * i
        lista.append(multiplo_i)

        multiplo_j = c * j
        lista.append(multiplo_j)

    # Remove as repetições
    for x in lista:
        if x not in l:
            l.append(x)

    # Organiza a lista em ordem crescente
    l.sort()

    print(l)

else:
    print('O número deve ser maior que zero')
