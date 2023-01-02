vetor = []

for c in range(10):
    vetor.append(int(input(f'Digite um número na posição {c}: ')))

print()

for i in vetor:

    cont = 0

    for j in range(1, i + 1):
        if i % j == 0:
            cont += 1
    if cont <= 2:
        print(f'O número {i} é primo e está na posição {vetor.index(i)}')
