vetor = []

while len(vetor) < 10:
    n = int(input('Digite um número para adicionar ao vetor: '))

    if n in vetor:
        print(f'O número {n} já está no vetor, por favor digite outro.')
        print()
    else:
        vetor.append(n)

print()
print(vetor)
