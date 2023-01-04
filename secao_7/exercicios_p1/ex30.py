vetor1 = []
vetor2 = []

for i in range(10):
    vetor1.append(int(input(f'Digite um elemento para o primeiro vetor: ')))
    vetor2.append(int(input(f'Digite um elemento para o segundo vetor: ')))

conjunto1 = set(vetor1)
conjunto2 = set(vetor2)

print(f'A intersecção entre esses dois vetores é {conjunto1.intersection(conjunto2)}')
