vetor = []

for i in range(1, 100 ** 2):

    if len(vetor) >= 100:
        break
    else:
        numero = str(i)

        if i % 7 == 0 or numero[len(numero) - 1] == '7':
            vetor.append(i)

print(vetor)
print(len(vetor))